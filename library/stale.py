"""Freshness ranking over task current_sota and node last_reviewed."""

from datetime import date
from typing import Any, Dict, List, Optional

from library.dates import age_days, parse_partial_date
from library.graph import KnowledgeGraph, Node

DEFAULT_MAX_AGE_DAYS = 120


def _entry_dates(node: Node, sota_entry: Optional[dict] = None) -> Dict[str, Any]:
    as_of = None
    if sota_entry:
        as_of = sota_entry.get("as_of")
    if as_of is None:
        as_of = node.metadata.get("as_of")
    last_reviewed = node.metadata.get("last_reviewed")
    return {"as_of": as_of, "last_reviewed": last_reviewed}


def _age_payload(as_of, last_reviewed, today: date, max_age_days: int) -> Dict[str, Any]:
    as_of_age = age_days(as_of, today)
    reviewed_age = age_days(last_reviewed, today)
    missing = parse_partial_date(as_of) is None and parse_partial_date(last_reviewed) is None
    candidates = [a for a in (as_of_age, reviewed_age) if a is not None]
    if missing:
        age = None
        over = True
    elif as_of_age is None and reviewed_age is None:
        age = None
        over = True
    else:
        # Staleness is driven by current_sota as_of when present, else last_reviewed.
        age = as_of_age if as_of_age is not None else reviewed_age
        over = age is None or age > max_age_days
    return {
        "as_of": str(as_of) if as_of is not None else None,
        "last_reviewed": str(last_reviewed) if last_reviewed is not None else None,
        "age_days": age,
        "over_budget": over,
    }


def collect_stale(
    graph: KnowledgeGraph,
    max_age_days: int = DEFAULT_MAX_AGE_DAYS,
    today: Optional[date] = None,
) -> Dict[str, Any]:
    if today is None:
        today = date.today()

    items: List[Dict[str, Any]] = []
    task_over = False

    for task in graph.get_nodes_by_type("task"):
        entries = [e for e in (task.metadata.get("current_sota") or []) if isinstance(e, dict)]
        if not entries:
            payload = _age_payload(None, task.metadata.get("last_reviewed"), today, max_age_days)
            payload["id"] = task.id
            payload["kind"] = "task"
            items.append(payload)
            if payload["over_budget"]:
                task_over = True
            continue
        for entry in entries:
            payload = _age_payload(
                entry.get("as_of"),
                task.metadata.get("last_reviewed"),
                today,
                max_age_days,
            )
            payload["id"] = task.id
            payload["kind"] = "task"
            payload["method"] = entry.get("method")
            items.append(payload)
            if payload["over_budget"]:
                task_over = True

    for method in graph.get_nodes_by_type("method"):
        last_reviewed = method.metadata.get("last_reviewed")
        if last_reviewed is None:
            for claim in method.metadata.get("claims") or []:
                if isinstance(claim, dict) and claim.get("date"):
                    last_reviewed = claim.get("date")
                    break
        payload = _age_payload(
            None,
            last_reviewed,
            today,
            max_age_days,
        )
        payload["id"] = method.id
        payload["kind"] = "method"
        items.append(payload)

    items.sort(key=lambda row: (
        0 if row.get("over_budget") else 1,
        -(row.get("age_days") if row.get("age_days") is not None else 10**9),
        row.get("id") or "",
    ))

    return {
        "max_age_days": max_age_days,
        "today": today.isoformat(),
        "over_budget": task_over,
        "items": items,
    }
