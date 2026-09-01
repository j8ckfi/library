"""Decision-shaped resolution: use / instead / do-not-use / gotchas / code / trust."""

import re
from datetime import date
from typing import Any, Dict, List, Optional

from library.dates import age_days
from library.graph import KnowledgeGraph, Node
from library.query import QueryEngine
from library.render import format_claim, top_claim
from library.stale import DEFAULT_MAX_AGE_DAYS

GOTCHA_HEADING = re.compile(
    r"^##\s+Gotchas.*?\n(.*?)(?=^##\s|\Z)",
    re.MULTILINE | re.DOTALL,
)


def extract_gotchas(body: str) -> List[str]:
    if not body:
        return []
    match = GOTCHA_HEADING.search(body)
    block = match.group(1) if match else ""
    bullets = re.findall(r"^[-*]\s+(.+)$", block, re.MULTILINE)
    cleaned = []
    for bullet in bullets:
        text = re.sub(r"\s+", " ", bullet).strip()
        if text:
            cleaned.append(text)
    return cleaned[:8]


def _as_list(value) -> List[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [value]
    return [str(v) for v in value]


def resolve_task(graph: KnowledgeGraph, task_or_nl: str) -> Optional[Node]:
    raw = (task_or_nl or "").strip()
    if not raw:
        return None
    node = graph.get_node(raw)
    if node and node.type == "task":
        return node
    if not raw.startswith("task:"):
        node = graph.get_node(f"task:{raw}")
        if node and node.type == "task":
            return node
    engine = QueryEngine(graph)
    ranked = engine.route(raw, top_k=1)
    if ranked:
        return ranked[0].node
    return None


def _supersedes_lineage(graph: KnowledgeGraph, method_id: str, depth: int = 4) -> List[str]:
    seen = []
    stack = [(method_id, 0)]
    visited = {method_id}
    while stack:
        current, level = stack.pop()
        if level >= depth:
            continue
        node = graph.get_node(current)
        if not node:
            continue
        for other in _as_list(node.metadata.get("supersedes")):
            if other in visited:
                continue
            visited.add(other)
            seen.append(other)
            stack.append((other, level + 1))
    return seen


def _evidence_rank(level: Optional[str]) -> int:
    order = {
        "peer-reviewed": 4,
        "preprint": 3,
        "unofficial-repro": 2,
        "self-reported": 1,
    }
    return order.get(level or "", 0)


def build_decision(
    graph: KnowledgeGraph,
    task_or_nl: str,
    today: Optional[date] = None,
    max_age_days: int = DEFAULT_MAX_AGE_DAYS,
) -> Dict[str, Any]:
    if today is None:
        today = date.today()

    engine = QueryEngine(graph)
    task = resolve_task(graph, task_or_nl)
    route_candidates = []
    if task is None or not (task_or_nl or "").strip().startswith("task:"):
        route_candidates = [
            {
                "id": r.node.id,
                "title": r.node.title,
                "score": r.score,
                "reasons": r.reasons,
            }
            for r in engine.route(task_or_nl or "", top_k=5)
        ]

    if task is None:
        return {
            "task": None,
            "query": task_or_nl,
            "use": [],
            "instead": [],
            "do_not_use": [],
            "gotchas": [],
            "code": [],
            "trust": {"stale": True, "reason": "no task resolved"},
            "route_candidates": route_candidates,
        }

    paths = graph.get_sota_path_for_task(task.id)
    sota_ids = []
    for entry in task.metadata.get("current_sota") or []:
        if isinstance(entry, dict) and entry.get("method"):
            sota_ids.append(entry["method"])
    if not sota_ids:
        sota_ids = [p["method"].id for p in paths]

    use_rows = []
    gotchas: List[str] = []
    code_rows = []
    do_not_use = []
    claims_for_trust: List[dict] = []
    as_of_dates = []

    for entry in task.metadata.get("current_sota") or []:
        if isinstance(entry, dict) and entry.get("as_of"):
            as_of_dates.append(entry.get("as_of"))

    seen_methods = set()
    for path in paths:
        method = path["method"]
        if method.id in seen_methods:
            continue
        if sota_ids and method.id not in sota_ids:
            continue
        seen_methods.add(method.id)
        claims = [c for c in (path.get("claims") or []) if isinstance(c, dict)]
        claims_for_trust.extend(claims)
        use_rows.append({
            "id": method.id,
            "title": method.title,
            "status": method.status,
            "claims": claims,
            "top_claim": top_claim(claims),
            "papers": [p.id for p in path.get("papers") or []],
            "recipes": [r.id for r in path.get("recipes") or []],
            "assumptions": list(method.metadata.get("assumptions") or []),
        })
        for gotcha in extract_gotchas(method.body):
            if gotcha not in gotchas:
                gotchas.append(gotcha)
        for assumption in method.metadata.get("assumptions") or []:
            text = f"assumption: {assumption}"
            if text not in gotchas:
                gotchas.append(text)
        for recipe in path.get("recipes") or []:
            code_rows.append({
                "id": recipe.id,
                "title": recipe.title,
                "target_hardware": recipe.metadata.get("target_hardware"),
                "framework": recipe.metadata.get("framework"),
                "repo_url": recipe.metadata.get("repo_url"),
                "pip_dependencies": list(recipe.metadata.get("pip_dependencies") or []),
            })
        for guard in method.metadata.get("do_not_use_for") or []:
            if isinstance(guard, dict):
                do_not_use.append({
                    "when": guard.get("when"),
                    "reason": guard.get("reason"),
                    "use_instead": guard.get("use_instead"),
                    "source": method.id,
                })
        for old_id in _supersedes_lineage(graph, method.id):
            old = graph.get_node(old_id)
            title = old.title if old else old_id
            do_not_use.append({
                "when": "as the default for this task",
                "reason": f"{title} is on the superseded lineage of {method.id}",
                "use_instead": method.id,
                "source": old_id,
            })

    for redirect in task.metadata.get("redirects") or []:
        if isinstance(redirect, dict):
            do_not_use.append({
                "when": redirect.get("when"),
                "reason": f"task redirect from {task.id}",
                "use_instead": redirect.get("to"),
                "source": task.id,
            })

    lineage = set()
    for used_id in seen_methods:
        lineage.update(_supersedes_lineage(graph, used_id))

    instead = []
    for method_id in _as_list(task.metadata.get("methods")):
        if method_id in seen_methods:
            continue
        method = graph.get_node(method_id)
        if not method:
            continue
        retired = (
            method.status == "superseded"
            or bool(method.metadata.get("superseded_by"))
            or method_id in lineage
        )
        if retired:
            do_not_use.append({
                "when": "as the default for this task",
                "reason": f"{method.id} is superseded or on the superseded lineage",
                "use_instead": use_rows[0]["id"] if use_rows else None,
                "source": method.id,
            })
            continue
        instead.append({
            "id": method.id,
            "title": method.title,
            "status": method.status,
            "note": "listed on the task, not current_sota",
        })

    as_of = as_of_dates[0] if as_of_dates else None
    last_reviewed = task.metadata.get("last_reviewed")
    age = age_days(as_of, today)
    if age is None:
        age = age_days(last_reviewed, today)
    stale_flag = age is None or age > max_age_days

    verified_any = any(c.get("verified") for c in claims_for_trust)
    levels = [c.get("evidence_level") for c in claims_for_trust if c.get("evidence_level")]
    best_level = None
    if levels:
        best_level = max(levels, key=_evidence_rank)

    trust = {
        "verified": verified_any,
        "evidence_level": best_level,
        "evidence_levels": levels,
        "as_of": str(as_of) if as_of is not None else None,
        "last_reviewed": str(last_reviewed) if last_reviewed is not None else None,
        "age_days": age,
        "stale": stale_flag,
        "freshness_budget_days": max_age_days,
    }

    return {
        "query": task_or_nl,
        "task": {
            "id": task.id,
            "title": task.title,
            "domain": task.domain,
            "scope": task.metadata.get("scope") or "",
            "out_of_scope": list(task.metadata.get("out_of_scope") or []),
            "redirects": [
                {"when": r.get("when"), "to": r.get("to")}
                for r in (task.metadata.get("redirects") or [])
                if isinstance(r, dict)
            ],
            "last_reviewed": last_reviewed,
            "summary": task.metadata.get("summary") or "",
        },
        "use": use_rows,
        "instead": instead,
        "do_not_use": do_not_use,
        "gotchas": gotchas,
        "code": code_rows,
        "trust": trust,
        "route_candidates": route_candidates,
    }


def decision_brief_lines(payload: Dict[str, Any]) -> List[str]:
    task = payload.get("task") or {}
    use = payload.get("use") or []
    trust = payload.get("trust") or {}
    code = payload.get("code") or []
    lines = []
    task_id = task.get("id") or "(unresolved)"
    lines.append(f"task: {task_id}")
    if use:
        primary = use[0]
        lines.append(f"use: {primary.get('id')} [{primary.get('status')}]")
        claim = primary.get("top_claim")
        if claim:
            lines.append(f"claim: {format_claim(claim)}")
        others = [u.get("id") for u in use[1:]]
        if others:
            lines.append("also: " + ", ".join(others))
    else:
        lines.append("use: (none)")
    fresh = "STALE" if trust.get("stale") else "fresh"
    lines.append(
        f"freshness: {fresh} as_of={trust.get('as_of')} "
        f"last_reviewed={trust.get('last_reviewed')} age_days={trust.get('age_days')}"
    )
    if trust.get("evidence_level") or "verified" in trust:
        lines.append(
            f"trust: verified={trust.get('verified')} evidence={trust.get('evidence_level')}"
        )
    instead = payload.get("instead") or []
    if instead:
        lines.append("instead: " + ", ".join(i.get("id") for i in instead[:4] if i.get("id")))
    dnu = payload.get("do_not_use") or []
    if dnu:
        labels = []
        for item in dnu[:4]:
            labels.append(item.get("source") or item.get("use_instead") or item.get("when"))
        lines.append("do_not_use: " + "; ".join(str(x) for x in labels if x))
    if code:
        rec = code[0]
        lines.append(
            f"code: {rec.get('id')} hardware={rec.get('target_hardware')} repo={rec.get('repo_url')}"
        )
        lines.append(f"next: python -m library show {rec.get('id')}")
    else:
        method_id = use[0]["id"] if use else task_id
        lines.append(f"next: python -m library show {method_id}")
    return lines


def format_decision(payload: Dict[str, Any]) -> str:
    task = payload.get("task")
    if not task:
        lines = ["No task resolved."]
        for cand in payload.get("route_candidates") or []:
            lines.append(f"- {cand.get('id')} ({cand.get('title')}) score={cand.get('score')}")
        return "\n".join(lines)

    lines = [
        "=======================================================",
        f" DECISION: {task['id']} — {task['title']}",
        "=======================================================",
        "",
        "What do I use?",
    ]
    if payload.get("use"):
        for row in payload["use"]:
            lines.append(f"  {row['id']} ({row['title']}) [{str(row.get('status') or '').upper()}]")
            claim = row.get("top_claim")
            if claim:
                lines.append(f"    {format_claim(claim)}")
            extra = row.get("claims") or []
            for claim in extra[1:3]:
                lines.append(f"    {format_claim(claim)}")
    else:
        lines.append("  (no current_sota method)")

    lines.append("")
    lines.append("What would I use instead?")
    if payload.get("instead"):
        for row in payload["instead"][:6]:
            lines.append(f"  {row['id']} ({row['title']}) [{row.get('status')}] — {row.get('note')}")
    else:
        lines.append("  (no listed alternates)")

    lines.append("")
    lines.append("What must I NOT use?")
    redirects = task.get("redirects") or []
    if redirects:
        for redirect in redirects:
            lines.append(f"  when {redirect.get('when')} -> {redirect.get('to')}")
    dnu = payload.get("do_not_use") or []
    if dnu:
        seen = set()
        for item in dnu:
            key = (item.get("source"), item.get("when"), item.get("use_instead"))
            if key in seen:
                continue
            seen.add(key)
            instead = f" -> {item.get('use_instead')}" if item.get("use_instead") else ""
            reason = f" ({item.get('reason')})" if item.get("reason") else ""
            when = item.get("when") or ""
            source = item.get("source") or ""
            lines.append(f"  {source}: when {when}{instead}{reason}")
            if len(seen) >= 12:
                break
    if not redirects and not dnu:
        lines.append("  (no redirects / do_not_use_for recorded)")

    lines.append("")
    lines.append("What will bite me?")
    if payload.get("gotchas"):
        for gotcha in payload["gotchas"][:8]:
            lines.append(f"  - {gotcha}")
    else:
        lines.append("  (no gotchas section on the SOTA method node)")

    lines.append("")
    lines.append("Where's the code?")
    if payload.get("code"):
        for rec in payload["code"][:4]:
            lines.append(f"  {rec['id']}: {rec.get('title')}")
            lines.append(f"    hardware: {rec.get('target_hardware')}")
            lines.append(f"    framework: {rec.get('framework')}")
            lines.append(f"    repo: {rec.get('repo_url')}")
    else:
        lines.append("  (no recipe linked)")

    trust = payload.get("trust") or {}
    fresh = "STALE — re-check literature before an expensive run" if trust.get("stale") else "within freshness budget"
    lines.append("")
    lines.append("How much should I trust this?")
    lines.append(
        f"  verified={trust.get('verified')} evidence_level={trust.get('evidence_level')} "
        f"as_of={trust.get('as_of')} last_reviewed={trust.get('last_reviewed')} "
        f"age_days={trust.get('age_days')} ({fresh})"
    )
    return "\n".join(lines)
