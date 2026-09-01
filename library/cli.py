"""CLI interface for training agents and human researchers to query the ML library."""

import argparse
import sys
from pathlib import Path

from library.decide import build_decision, decision_brief_lines, format_decision
from library.exporter import export_graph
from library.graph import KnowledgeGraph
from library.indexgen import write_index
from library.ingest import create_node_from_template
from library.loader import load_graph
from library.query import QueryEngine
from library.render import (
    emit_json,
    format_claim,
    output_mode,
    print_brief,
    top_claim,
)
from library.stale import DEFAULT_MAX_AGE_DAYS, collect_stale
from library.supersede import apply_supersede
from library.traverse import describe_node_neighborhood, find_shortest_path
from library.validator import validate_graph


def add_tier_flags(parser: argparse.ArgumentParser, brief: bool = True) -> None:
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON output (unbounded, superset of prose)",
    )
    if brief:
        parser.add_argument(
            "--brief",
            action="store_true",
            help="~10 line brief output (ids, status, top claim, freshness, next step)",
        )


def cmd_query(args, graph: KnowledgeGraph):
    engine = QueryEngine(graph)
    results = engine.query(
        query_str=args.query,
        top_k=args.top_k,
        node_type=args.type,
        domain=args.domain,
        sota_only=args.sota_only,
    )
    mode = output_mode(args)

    payload = []
    for r in results:
        payload.append({
            "id": r.node.id,
            "type": r.node.type,
            "title": r.node.title,
            "score": round(r.score, 2),
            "reasons": r.reasons,
            "status": r.sota_status,
            "file_path": str(r.node.file_path),
            "metadata": r.node.metadata,
        })

    if mode == "json":
        emit_json(payload)
        return

    if mode == "brief":
        lines = [f"query: {args.query} ({len(results)} hits)"]
        for r in results[:8]:
            lines.append(f"{r.node.id} [{r.sota_status}] score={r.score:.1f} — {r.node.title}")
        if not results:
            lines.append("no matches")
        print_brief(lines)
        return

    if not results:
        print(f"No matching nodes found for query: '{args.query}'")
        return

    print(f"\n--- Search Results for: '{args.query}' (Found {len(results)}) ---")
    for i, r in enumerate(results, 1):
        n = r.node
        print(f"\n{i}. [{r.sota_status}] {n.id} - {n.title} (Score: {r.score:.1f})")
        print(f"   File: {n.file_path}")
        if r.reasons:
            print(f"   Reasons: {'; '.join(r.reasons)}")

        summary = n.metadata.get("summary") or n.metadata.get("abstract_summary")
        if summary:
            print(f"   Summary: {summary}")

        claims = n.metadata.get("claims", [])
        if claims:
            print(f"   Verified Claims ({len(claims)}):")
            for c in claims[:2]:
                if isinstance(c, dict):
                    print(f"     * {format_claim(c)}")

        if n.type == "method":
            recipes = n.metadata.get("recipes", [])
            papers = n.metadata.get("papers", [])
            if recipes:
                print(f"   Recipes: {', '.join(recipes)}")
            if papers:
                print(f"   Papers: {', '.join(papers)}")
        elif n.type == "task":
            sota_list = n.metadata.get("current_sota", [])
            if sota_list:
                print("   Current SOTA Methods:")
                for s in sota_list:
                    print(
                        f"     * {s.get('method')} ({s.get('benchmark')}: "
                        f"{s.get('metric')}={s.get('value')}, as of {s.get('as_of')})"
                    )


def _sota_payload(res: dict) -> dict:
    task = res.get("task")
    method = res.get("method")
    papers = res.get("papers") or []
    recipes = res.get("recipes") or []
    claims = [c for c in (res.get("claims") or []) if isinstance(c, dict)]
    return {
        "task": task.metadata if task else None,
        "method": method.metadata if method else None,
        "papers": [p.metadata for p in papers],
        "recipes": [r.metadata for r in recipes],
        "claims": claims,
        "gotchas": method.metadata.get("assumptions", []) if method else [],
        "do_not_use_for": (method.metadata.get("do_not_use_for") or []) if method else [],
        "redirects": (task.metadata.get("redirects") or []) if task else [],
    }


def cmd_sota(args, graph: KnowledgeGraph):
    engine = QueryEngine(graph)
    sota_resolutions = engine.sota(args.task)
    mode = output_mode(args)
    payload = [_sota_payload(res) for res in sota_resolutions]
    decision = build_decision(graph, args.task)

    if mode == "json":
        emit_json({"resolutions": payload, "decision": decision})
        return

    if mode == "brief":
        print_brief(decision_brief_lines(decision))
        return

    if not sota_resolutions:
        print(f"No SOTA resolution found for '{args.task}'. Try 'library query \"{args.task}\"'")
        return

    print(format_decision(decision))
    if len(sota_resolutions) > 1:
        print("\nAdditional SOTA paths:")
        for item in sota_resolutions[1:]:
            method = item["method"]
            print(f"  - {method.id} ({method.title}) [{method.status}]")


def cmd_show(args, graph: KnowledgeGraph):
    node = graph.get_node(args.node_id)
    if not node:
        print(f"Error: Node '{args.node_id}' not found in knowledge graph.")
        sys.exit(1)

    mode = output_mode(args)
    payload = {
        "id": node.id,
        "type": node.type,
        "title": node.title,
        "file_path": str(node.file_path),
        "metadata": node.metadata,
        "body": node.body,
    }
    if mode == "json":
        emit_json(payload)
        return

    if mode == "brief":
        summary = node.metadata.get("summary") or node.metadata.get("abstract_summary") or ""
        claim = top_claim(node.metadata.get("claims") or [])
        lines = [
            f"{node.id} | {node.title}",
            f"type={node.type} status={node.status} domain={node.domain}",
            f"file: {node.file_path}",
        ]
        if summary:
            lines.append(f"summary: {summary}")
        if claim:
            lines.append(f"claim: {format_claim(claim)}")
        sota = node.metadata.get("current_sota") or []
        if sota and isinstance(sota[0], dict):
            lines.append(f"sota: {sota[0].get('method')} as_of={sota[0].get('as_of')}")
        lines.append(f"next: python -m library walk {node.id}")
        print_brief(lines)
        return

    print(f"\n=======================================================")
    print(f" Node: {node.id} ({node.type.upper()})")
    print(f" Title: {node.title}")
    print(f" File: {node.file_path}")
    print(f"=======================================================\n")
    print("--- METADATA ---")
    for k, v in node.metadata.items():
        if k not in ("id", "type", "title"):
            print(f"{k}: {v}")
    print("\n--- CONTENT ---")
    print(node.body)


def cmd_walk(args, graph: KnowledgeGraph):
    info = describe_node_neighborhood(graph, args.node_id)
    if not info:
        print(f"Error: Node '{args.node_id}' not found.")
        sys.exit(1)

    node = info["node"]
    payload = {
        "id": node.id,
        "title": node.title,
        "type": node.type,
        "status": node.status,
        "outgoing": info["outgoing"],
        "incoming": info["incoming"],
    }
    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        return

    if mode == "brief":
        lines = [
            f"{node.id} neighborhood",
            f"outgoing={len(info['outgoing'])} incoming={len(info['incoming'])}",
        ]
        for edge in info["outgoing"][:4]:
            lines.append(f"-> [{edge['relation']}] {edge['target_id']}")
        for edge in info["incoming"][:3]:
            lines.append(f"<- [{edge['relation']}] {edge['source_id']}")
        print_brief(lines)
        return

    print(f"\nNeighborhood for node: {node.id} ({node.title})")

    outgoing = info["outgoing"]
    print(f"\nOutgoing Edges ({len(outgoing)}):")
    if not outgoing:
        print("  (none)")
    for edge in outgoing:
        print(
            f"  --[{edge['relation']}]--> {edge['target_id']} "
            f"({edge['target_title']}) [{edge['target_type']}]"
        )

    incoming = info["incoming"]
    print(f"\nIncoming Edges ({len(incoming)}):")
    if not incoming:
        print("  (none)")
    for edge in incoming:
        print(
            f"  <--[{edge['relation']}]-- {edge['source_id']} "
            f"({edge['source_title']}) [{edge['source_type']}]"
        )


def cmd_path(args, graph: KnowledgeGraph):
    steps = find_shortest_path(graph, args.start_id, args.end_id)
    payload = {
        "from": args.start_id,
        "to": args.end_id,
        "hops": (len(steps) - 1) if steps else None,
        "steps": steps or [],
    }
    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        return

    if not steps:
        print(f"No path found between '{args.start_id}' and '{args.end_id}'.")
        return

    if mode == "brief":
        ids = [s["id"] for s in steps]
        print_brief([f"path ({len(steps)-1} hops): " + " -> ".join(ids)])
        return

    print(f"\nPath ({len(steps)-1} hops) from '{args.start_id}' to '{args.end_id}':")
    for s in steps:
        trans = f"  {s['transition']} " if "transition" in s else ""
        print(f"{trans}[{s['type'].upper()}] {s['id']} - {s['title']}")


def cmd_validate(args, graph: KnowledgeGraph):
    res = validate_graph(graph)
    payload = {
        "nodes": len(graph.nodes),
        "edges": len(graph.edges),
        "errors": len(res.errors),
        "warnings": len(res.warnings),
        "issues": [
            {
                "level": issue.level,
                "node_id": issue.node_id,
                "file_path": str(issue.file_path),
                "message": issue.message,
            }
            for issue in res.issues
        ],
    }
    if getattr(args, "json", False):
        emit_json(payload)
        if res.has_errors:
            sys.exit(1)
        return

    print("\n--- Graph Validation Report ---")
    print(f"Total Nodes: {len(graph.nodes)}")
    print(f"Total Edges: {len(graph.edges)}")
    print(f"Errors: {len(res.errors)}")
    print(f"Warnings: {len(res.warnings)}")

    if res.issues:
        print("\nIssues found:")
        for issue in res.issues:
            print(f"[{issue.level}] {issue.node_id} ({issue.file_path}): {issue.message}")

    if res.has_errors:
        print("\nValidation FAILED with errors.")
        sys.exit(1)
    else:
        print("\nValidation PASSED. Graph is healthy and consistent.")
        if res.warnings:
            print("Warnings do not fail validation (INDEX/cheat-sheet drift, staleness).")


def cmd_stats(args, graph: KnowledgeGraph):
    type_counts = {}
    for node in graph.nodes.values():
        type_counts[node.type] = type_counts.get(node.type, 0) + 1

    sota_methods = [n for n in graph.get_nodes_by_type("method") if n.status == "sota"]
    payload = {
        "node_count": len(graph.nodes),
        "edge_count": len(graph.edges),
        "by_type": type_counts,
        "sota_methods": len(sota_methods),
    }
    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        return
    if mode == "brief":
        print_brief([
            f"nodes={payload['node_count']} edges={payload['edge_count']} sota={payload['sota_methods']}",
            "types: " + ", ".join(f"{k}={v}" for k, v in sorted(type_counts.items())),
        ])
        return

    print("\n=======================================================")
    print(" Knowledge Graph Statistics")
    print("=======================================================")
    print(f"Total Nodes: {len(graph.nodes)}")
    for ntype, count in sorted(type_counts.items()):
        print(f"  - {ntype.capitalize()}s: {count}")
    print(f"Total Edges: {len(graph.edges)}")
    print(f"Active SOTA Methods: {len(sota_methods)}")
    print("=======================================================\n")


def cmd_export(args, graph: KnowledgeGraph):
    output_path = Path(args.output)
    export_graph(graph, output_path, format_type=args.format)
    print(
        f"Successfully exported {len(graph.nodes)} nodes and {len(graph.edges)} "
        f"edges to {output_path} ({args.format})"
    )


def cmd_new(args, graph: KnowledgeGraph):
    try:
        path = create_node_from_template(args.type, args.slug, title=args.title)
        print(f"Created new {args.type} template at: {path}")
    except Exception as e:
        print(f"Error creating node: {e}")
        sys.exit(1)


def cmd_index(args, graph: KnowledgeGraph):
    result = write_index(graph)
    if output_mode(args) == "json":
        emit_json({"written": result["written"], "stale": result["stale"]})
        return
    status = "was stale" if result["stale"] else "already current"
    print(f"Index write complete ({status}).")
    for path in result["written"]:
        print(f"  wrote {path}")


def cmd_decide(args, graph: KnowledgeGraph):
    payload = build_decision(graph, args.task)
    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        return
    if mode == "brief":
        print_brief(decision_brief_lines(payload))
        return
    print(format_decision(payload))


def cmd_stale(args, graph: KnowledgeGraph):
    report = collect_stale(graph, max_age_days=args.max_age_days)
    items = [
        {
            "id": row["id"],
            "as_of": row.get("as_of"),
            "last_reviewed": row.get("last_reviewed"),
            "age_days": row.get("age_days"),
            "over_budget": row.get("over_budget"),
        }
        for row in report["items"]
    ]
    payload = {
        "max_age_days": report["max_age_days"],
        "today": report["today"],
        "over_budget": report["over_budget"],
        "items": items,
    }
    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        if report["over_budget"]:
            sys.exit(1)
        return

    over_tasks = [row for row in report["items"] if row.get("over_budget") and row.get("kind") == "task"]
    over_methods = [row for row in report["items"] if row.get("over_budget") and row.get("kind") == "method"]
    if mode == "brief":
        lines = [
            f"stale budget={report['max_age_days']}d over_budget={report['over_budget']} "
            f"task_hits={len(over_tasks)}",
        ]
        for row in over_tasks[:8]:
            lines.append(
                f"{row['id']} as_of={row.get('as_of')} age_days={row.get('age_days')} "
                f"last_reviewed={row.get('last_reviewed')}"
            )
        if not over_tasks:
            lines.append("no task current_sota over budget")
        print_brief(lines)
        if report["over_budget"]:
            sys.exit(1)
        return

    print(f"\nStaleness report (budget {report['max_age_days']} days, today {report['today']})")
    print(f"Task current_sota over budget: {report['over_budget']}")
    print("Over-budget tasks:")
    if not over_tasks:
        print("  (none)")
    for row in over_tasks:
        print(
            f"  {row['id']} as_of={row.get('as_of')} "
            f"last_reviewed={row.get('last_reviewed')} age_days={row.get('age_days')}"
        )
    print("Over-budget methods (ranked, not CI-gating):")
    for row in over_methods[:20]:
        print(
            f"  {row['id']} last_reviewed={row.get('last_reviewed')} age_days={row.get('age_days')}"
        )
    if report["over_budget"]:
        sys.exit(1)


def cmd_route(args, graph: KnowledgeGraph):
    engine = QueryEngine(graph)
    ranked = engine.route(args.query, top_k=args.top_k)
    payload = {"query": args.query, "candidates": []}
    for r in ranked:
        task = r.node
        payload["candidates"].append({
            "id": task.id,
            "title": task.title,
            "score": round(r.score, 2),
            "reasons": r.reasons,
            "scope": task.metadata.get("scope") or "",
            "out_of_scope": list(task.metadata.get("out_of_scope") or []),
            "redirects": [
                {"when": item.get("when"), "to": item.get("to")}
                for item in (task.metadata.get("redirects") or [])
                if isinstance(item, dict)
            ],
            "current_sota": task.metadata.get("current_sota") or [],
            "domain": task.domain,
        })

    mode = output_mode(args)
    if mode == "json":
        emit_json(payload)
        return

    if mode == "brief":
        lines = [f"route: {args.query}"]
        for cand in payload["candidates"][:8]:
            lines.append(f"{cand['id']} score={cand['score']} — {cand['title']}")
            for redirect in cand["redirects"][:2]:
                lines.append(f"  when {redirect['when']} -> {redirect['to']}")
        if not payload["candidates"]:
            lines.append("no candidates (graph has no tasks)")
        print_brief(lines)
        return

    print(f"\nRoute '{args.query}' — {len(payload['candidates'])} candidate tasks")
    for i, cand in enumerate(payload["candidates"], 1):
        print(f"\n{i}. {cand['id']} — {cand['title']} (score {cand['score']})")
        if cand["scope"]:
            print(f"   Scope: {cand['scope']}")
        if cand["out_of_scope"]:
            print("   Out of scope: " + "; ".join(cand["out_of_scope"]))
        if cand["redirects"]:
            print("   Redirects:")
            for redirect in cand["redirects"]:
                print(f"     when {redirect['when']} -> {redirect['to']}")
        if cand["reasons"]:
            print(f"   Reasons: {'; '.join(cand['reasons'])}")
        sota = cand["current_sota"]
        if sota:
            methods = ", ".join(
                f"{s.get('method')} [{s.get('as_of')}]"
                for s in sota if isinstance(s, dict)
            )
            print(f"   SOTA: {methods}")


def cmd_supersede(args, graph: KnowledgeGraph):
    result = apply_supersede(
        graph,
        args.new,
        args.old,
        args.task,
        dry_run=args.dry_run,
    )
    mode = output_mode(args)
    json_payload = {
        "ok": result.get("ok"),
        "dry_run": bool(result.get("dry_run")),
        "written": bool(result.get("written")),
        "errors": result.get("errors") or [],
        "receipt": result.get("receipt"),
        "edits": [
            {
                "path": edit.get("path"),
                "node": edit.get("node"),
                "summary": edit.get("summary"),
            }
            for edit in (result.get("edits") or result.get("full_edits") or [])
        ],
    }
    if mode == "json":
        emit_json(json_payload)
        if not result.get("ok"):
            sys.exit(1)
        return

    if not result.get("ok"):
        print("Supersede refused:")
        for err in result.get("errors") or []:
            print(f"  - {err}")
        sys.exit(1)

    label = "DRY RUN (no writes)" if result.get("dry_run") else "APPLIED"
    print(f"Supersede {label}: {result.get('new_id')} over {result.get('old_id')} for {result.get('task_id')}")
    for edit in result.get("edits") or []:
        print(f"  {edit.get('summary')} ({edit.get('path')})")
    if result.get("receipt"):
        print("\nReceipt:\n" + result["receipt"])


def main():
    parser = argparse.ArgumentParser(
        prog="library",
        description="j8ckfi/library - Agent-navigable ML papers and SOTA methods knowledge graph."
    )
    parser.add_argument("--root", default="graph", help="Root directory containing the graph markdown files (default: graph)")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    p_query = subparsers.add_parser("query", help="Query knowledge graph nodes by keyword, domain, or status")
    p_query.add_argument("query", help="Search query string")
    p_query.add_argument("--top-k", type=int, default=5, help="Number of results to return")
    p_query.add_argument("--type", choices=["task", "method", "paper", "recipe"], help="Filter by node type")
    p_query.add_argument("--domain", help="Filter by task domain")
    p_query.add_argument("--sota-only", action="store_true", help="Return only SOTA nodes")
    add_tier_flags(p_query)

    p_sota = subparsers.add_parser("sota", help="Lookup current SOTA method, paper, claims, and recipe for a task")
    p_sota.add_argument("task", help="Task ID or search keyword (e.g. 'task:llm-pretraining' or 'pretraining')")
    add_tier_flags(p_sota)

    p_show = subparsers.add_parser("show", help="Display full details and body of a node")
    p_show.add_argument("node_id", help="Node ID (e.g. 'method:muon-optimizer')")
    add_tier_flags(p_show)

    p_walk = subparsers.add_parser("walk", help="Inspect connected incoming and outgoing edges for a node")
    p_walk.add_argument("node_id", help="Node ID to inspect")
    add_tier_flags(p_walk)

    p_path = subparsers.add_parser("path", help="Find shortest path between two nodes")
    p_path.add_argument("--from", dest="start_id", required=True, help="Start node ID")
    p_path.add_argument("--to", dest="end_id", required=True, help="Target node ID")
    add_tier_flags(p_path)

    p_validate = subparsers.add_parser("validate", help="Validate graph schema, integrity, references, and supersession cycles")
    p_validate.add_argument("--json", action="store_true", help="JSON output")

    p_stats = subparsers.add_parser("stats", help="Display knowledge graph metrics and counts")
    add_tier_flags(p_stats)

    p_export = subparsers.add_parser("export", help="Export compiled graph to JSON or JSONL")
    p_export.add_argument("--output", default="dist/graph.json", help="Output file path (default: dist/graph.json)")
    p_export.add_argument("--format", choices=["json", "jsonl"], default="json", help="Export format")

    p_new = subparsers.add_parser("new", help="Scaffold a new node from template")
    p_new.add_argument("type", choices=["task", "method", "paper", "recipe"], help="Type of node")
    p_new.add_argument("slug", help="Slug identifier for the node")
    p_new.add_argument("--title", help="Human-readable title")

    p_index = subparsers.add_parser("index", help="Regenerate graph/INDEX.md and the AGENTS.md cheat-sheet")
    add_tier_flags(p_index, brief=False)

    p_decide = subparsers.add_parser("decide", help="Decision-shaped SOTA resolution for a task or NL query")
    p_decide.add_argument("task", help="Task ID or natural-language request")
    add_tier_flags(p_decide)

    p_stale = subparsers.add_parser("stale", help="Rank tasks/methods against the freshness budget")
    p_stale.add_argument(
        "--max-age-days",
        type=int,
        default=DEFAULT_MAX_AGE_DAYS,
        help=f"Freshness budget in days (default {DEFAULT_MAX_AGE_DAYS})",
    )
    add_tier_flags(p_stale)

    p_route = subparsers.add_parser("route", help="Rank candidate tasks for a natural-language request")
    p_route.add_argument("query", help="Natural-language training request")
    p_route.add_argument("--top-k", type=int, default=8, help="Number of candidate tasks")
    add_tier_flags(p_route)

    p_supersede = subparsers.add_parser("supersede", help="Transactional SOTA supersession write")
    p_supersede.add_argument("new", help="New method id (the successor)")
    p_supersede.add_argument("old", help="Old method id (the incumbent)")
    p_supersede.add_argument("--task", required=True, help="Task id whose current_sota is updated")
    p_supersede.add_argument("--dry-run", action="store_true", help="Print planned edits without writing")
    add_tier_flags(p_supersede, brief=False)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "new":
        cmd_new(args, None)
        return

    root_path = Path(args.root)
    if not root_path.exists():
        root_path = Path(".")

    graph = load_graph(root_path)

    dispatch = {
        "query": cmd_query,
        "sota": cmd_sota,
        "show": cmd_show,
        "walk": cmd_walk,
        "path": cmd_path,
        "validate": cmd_validate,
        "stats": cmd_stats,
        "export": cmd_export,
        "index": cmd_index,
        "decide": cmd_decide,
        "stale": cmd_stale,
        "route": cmd_route,
        "supersede": cmd_supersede,
    }
    handler = dispatch.get(args.command)
    if handler is None:
        parser.print_help()
        sys.exit(1)
    handler(args, graph)


if __name__ == "__main__":
    main()
