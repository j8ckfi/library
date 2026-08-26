"""CLI interface for training agents and human researchers to query the ML library."""

import argparse
import sys
from pathlib import Path
import json

from library.graph import KnowledgeGraph
from library.loader import load_graph
from library.validator import validate_graph
from library.query import QueryEngine
from library.traverse import describe_node_neighborhood, find_shortest_path
from library.exporter import export_graph
from library.ingest import create_node_from_template


def format_node_header(node) -> str:
    status_tag = f" [{node.status.upper()}]" if node.status else ""
    return f"{node.id} | {node.title}{status_tag}"


def cmd_query(args, graph: KnowledgeGraph):
    engine = QueryEngine(graph)
    results = engine.query(
        query_str=args.query,
        top_k=args.top_k,
        node_type=args.type,
        domain=args.domain,
        sota_only=args.sota_only
    )

    if args.json:
        out = []
        for r in results:
            out.append({
                "id": r.node.id,
                "type": r.node.type,
                "title": r.node.title,
                "score": round(r.score, 2),
                "reasons": r.reasons,
                "status": r.sota_status,
                "file_path": str(r.node.file_path),
                "metadata": r.node.metadata
            })
        print(json.dumps(out, indent=2))
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

        # Print summary or claim preview
        summary = n.metadata.get("summary") or n.metadata.get("abstract_summary")
        if summary:
            print(f"   Summary: {summary}")

        claims = n.metadata.get("claims", [])
        if claims:
            print(f"   Verified Claims ({len(claims)}):")
            for c in claims[:2]:
                print(f"     * {c.get('benchmark')}: {c.get('metric')} = {c.get('value')} (as of {c.get('date')})")

        # Related connected recipes or papers
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
                    print(f"     * {s.get('method')} ({s.get('benchmark')}: {s.get('metric')}={s.get('value')}, as of {s.get('as_of')})")


def cmd_sota(args, graph: KnowledgeGraph):
    engine = QueryEngine(graph)
    sota_resolutions = engine.sota(args.task)

    if args.json:
        out = []
        for res in sota_resolutions:
            out.append({
                "task": res["task"].metadata if res.get("task") else None,
                "method": res["method"].metadata if res.get("method") else None,
                "papers": [p.metadata for p in res.get("papers", [])],
                "recipes": [r.metadata for r in res.get("recipes", [])],
                "claims": res.get("claims", [])
            })
        print(json.dumps(out, indent=2))
        return

    if not sota_resolutions:
        print(f"No SOTA resolution found for '{args.task}'. Try 'library query \"{args.task}\"'")
        return

    print(f"\n=======================================================")
    print(f" SOTA RESOLUTION FOR: {args.task}")
    print(f"=======================================================")

    for i, item in enumerate(sota_resolutions, 1):
        task = item.get("task")
        method = item["method"]
        papers = item.get("papers", [])
        recipes = item.get("recipes", [])
        claims = item.get("claims", [])

        print(f"\n--- [Path {i}] ---")
        if task:
            print(f"Task:    {task.id} ({task.title})")
        print(f"Method:  {method.id} ({method.title}) [Status: {method.status}]")

        if claims:
            print("\n  Evidence & Benchmark Claims:")
            for c in claims:
                baseline_str = f" vs baseline {c.get('baseline')}" if c.get('baseline') else ""
                print(f"    - {c.get('benchmark')}: {c.get('metric')} = {c.get('value')}{baseline_str} [Date: {c.get('date')}]")

        if papers:
            print("\n  Reference Papers:")
            for p in papers:
                print(f"    - {p.id}: \"{p.title}\" (arXiv: {p.metadata.get('arxiv_id')}) -> {p.metadata.get('url')}")

        if recipes:
            print("\n  Ready-to-Use Code Recipes:")
            for r in recipes:
                print(f"    - {r.id}: {r.title}")
                print(f"      Hardware: {r.metadata.get('target_hardware')}")
                print(f"      Framework: {r.metadata.get('framework')}")
                print(f"      Repo: {r.metadata.get('repo_url')}")
                print(f"      File: {r.file_path}")


def cmd_show(args, graph: KnowledgeGraph):
    node = graph.get_node(args.node_id)
    if not node:
        print(f"Error: Node '{args.node_id}' not found in knowledge graph.")
        sys.exit(1)

    if args.json:
        print(json.dumps({
            "id": node.id,
            "type": node.type,
            "title": node.title,
            "file_path": str(node.file_path),
            "metadata": node.metadata,
            "body": node.body
        }, indent=2))
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
    print(f"\nNeighborhood for node: {node.id} ({node.title})")

    outgoing = info["outgoing"]
    print(f"\nOutgoing Edges ({len(outgoing)}):")
    if not outgoing:
        print("  (none)")
    for edge in outgoing:
        print(f"  --[{edge['relation']}]--> {edge['target_id']} ({edge['target_title']}) [{edge['target_type']}]")

    incoming = info["incoming"]
    print(f"\nIncoming Edges ({len(incoming)}):")
    if not incoming:
        print("  (none)")
    for edge in incoming:
        print(f"  <--[{edge['relation']}]-- {edge['source_id']} ({edge['source_title']}) [{edge['source_type']}]")


def cmd_path(args, graph: KnowledgeGraph):
    steps = find_shortest_path(graph, args.start_id, args.end_id)
    if not steps:
        print(f"No path found between '{args.start_id}' and '{args.end_id}'.")
        return

    print(f"\nPath ({len(steps)-1} hops) from '{args.start_id}' to '{args.end_id}':")
    for s in steps:
        trans = f"  {s['transition']} " if "transition" in s else ""
        print(f"{trans}[{s['type'].upper()}] {s['id']} - {s['title']}")


def cmd_validate(args, graph: KnowledgeGraph):
    res = validate_graph(graph)
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


def cmd_stats(args, graph: KnowledgeGraph):
    type_counts = {}
    for node in graph.nodes.values():
        type_counts[node.type] = type_counts.get(node.type, 0) + 1

    sota_methods = [n for n in graph.get_nodes_by_type("method") if n.status == "sota"]

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
    print(f"Successfully exported {len(graph.nodes)} nodes and {len(graph.edges)} edges to {output_path} ({args.format})")


def cmd_new(args, graph: KnowledgeGraph):
    try:
        path = create_node_from_template(args.type, args.slug, title=args.title)
        print(f"Created new {args.type} template at: {path}")
    except Exception as e:
        print(f"Error creating node: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="library",
        description="j8ckfi/library - Agent-navigable ML papers and SOTA methods knowledge graph."
    )
    parser.add_argument("--root", default="graph", help="Root directory containing the graph markdown files (default: graph)")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # query
    p_query = subparsers.add_parser("query", help="Query knowledge graph nodes by keyword, domain, or status")
    p_query.add_argument("query", help="Search query string")
    p_query.add_argument("--top-k", type=int, default=5, help="Number of results to return")
    p_query.add_argument("--type", choices=["task", "method", "paper", "recipe"], help="Filter by node type")
    p_query.add_argument("--domain", help="Filter by task domain")
    p_query.add_argument("--sota-only", action="store_true", help="Return only SOTA nodes")
    p_query.add_argument("--json", action="store_true", help="Output results in JSON format")

    # sota
    p_sota = subparsers.add_parser("sota", help="Lookup current SOTA method, paper, claims, and recipe for a task")
    p_sota.add_argument("task", help="Task ID or search keyword (e.g. 'task:llm-pretraining' or 'pretraining')")
    p_sota.add_argument("--json", action="store_true", help="Output in JSON format")

    # show
    p_show = subparsers.add_parser("show", help="Display full details and body of a node")
    p_show.add_argument("node_id", help="Node ID (e.g. 'method:muon-optimizer')")
    p_show.add_argument("--json", action="store_true", help="Output in JSON format")

    # walk
    p_walk = subparsers.add_parser("walk", help="Inspect connected incoming and outgoing edges for a node")
    p_walk.add_argument("node_id", help="Node ID to inspect")

    # path
    p_path = subparsers.add_parser("path", help="Find shortest path between two nodes")
    p_path.add_argument("--from", dest="start_id", required=True, help="Start node ID")
    p_path.add_argument("--to", dest="end_id", required=True, help="Target node ID")

    # validate
    subparsers.add_parser("validate", help="Validate graph schema, integrity, references, and supersession cycles")

    # stats
    subparsers.add_parser("stats", help="Display knowledge graph metrics and counts")

    # export
    p_export = subparsers.add_parser("export", help="Export compiled graph to JSON or JSONL")
    p_export.add_argument("--output", default="dist/graph.json", help="Output file path (default: dist/graph.json)")
    p_export.add_argument("--format", choices=["json", "jsonl"], default="json", help="Export format")

    # new
    p_new = subparsers.add_parser("new", help="Scaffold a new node from template")
    p_new.add_argument("type", choices=["task", "method", "paper", "recipe"], help="Type of node")
    p_new.add_argument("slug", help="Slug identifier for the node")
    p_new.add_argument("--title", help="Human-readable title")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Ingest command does not require pre-loading graph
    if args.command == "new":
        cmd_new(args, None)
        return

    root_path = Path(args.root)
    if not root_path.exists():
        # Fallback to current directory if running in workspace root
        root_path = Path(".")

    graph = load_graph(root_path)

    if args.command == "query":
        cmd_query(args, graph)
    elif args.command == "sota":
        cmd_sota(args, graph)
    elif args.command == "show":
        cmd_show(args, graph)
    elif args.command == "walk":
        cmd_walk(args, graph)
    elif args.command == "path":
        cmd_path(args, graph)
    elif args.command == "validate":
        cmd_validate(args, graph)
    elif args.command == "stats":
        cmd_stats(args, graph)
    elif args.command == "export":
        cmd_export(args, graph)


if __name__ == "__main__":
    main()
