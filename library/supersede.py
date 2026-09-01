"""Transactional supersession writes with dry-run and post-condition checks."""

from datetime import date
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import yaml

from library.dates import iso_today, year_month
from library.graph import KnowledgeGraph
from library.loader import load_graph, parse_frontmatter
from library.validator import validate_graph

Mutator = Callable[[Dict[str, Any]], None]


def normalize_method_id(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return text
    if ":" not in text:
        return f"method:{text}"
    return text


def normalize_task_id(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return text
    if ":" not in text:
        return f"task:{text}"
    return text


def _stringify(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _stringify(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify(v) for v in obj]
    if hasattr(obj, "isoformat") and not isinstance(obj, str):
        try:
            return obj.isoformat()
        except Exception:
            return str(obj)
    return obj


def dump_frontmatter(meta: Dict[str, Any]) -> str:
    cleaned = _stringify(meta)
    dumped = yaml.safe_dump(
        cleaned,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )
    return dumped


def split_document(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    return {"text": text, "body": body, "meta": meta}


def apply_frontmatter(path: Path, mutator: Mutator) -> str:
    parsed = split_document(path)
    meta = dict(parsed["meta"])
    mutator(meta)
    body = parsed["body"]
    if not body.endswith("\n"):
        body += "\n"
    dumped = dump_frontmatter(meta)
    if not dumped.endswith("\n"):
        dumped += "\n"
    return f"---\n{dumped}---\n{body}"


def _ensure_list(meta: Dict[str, Any], key: str) -> List[Any]:
    value = meta.get(key)
    if value is None:
        meta[key] = []
        return meta[key]
    if isinstance(value, list):
        return value
    meta[key] = [value]
    return meta[key]


def plan_supersede(
    graph: KnowledgeGraph,
    new_id: str,
    old_id: str,
    task_id: str,
    today: Optional[date] = None,
) -> Dict[str, Any]:
    new_id = normalize_method_id(new_id)
    old_id = normalize_method_id(old_id)
    task_id = normalize_task_id(task_id)
    if today is None:
        today = date.today()

    new_node = graph.get_node(new_id)
    old_node = graph.get_node(old_id)
    task_node = graph.get_node(task_id)
    errors = []
    if new_node is None:
        errors.append(f"new method '{new_id}' not found")
    if old_node is None:
        errors.append(f"old method '{old_id}' not found")
    if task_node is None:
        errors.append(f"task '{task_id}' not found")
    if new_id == old_id:
        errors.append("new and old method ids must differ")
    if errors:
        return {"ok": False, "errors": errors, "edits": [], "receipt": ""}

    as_of = year_month(today)
    reviewed = iso_today(today)

    def mutate_new(meta: Dict[str, Any]) -> None:
        meta["status"] = "sota"
        sota_for = _ensure_list(meta, "sota_for")
        if task_id not in sota_for:
            sota_for.append(task_id)
        supersedes = _ensure_list(meta, "supersedes")
        if old_id not in supersedes:
            supersedes.append(old_id)
        if meta.get("superseded_by") == old_id:
            meta.pop("superseded_by", None)

    def mutate_old(meta: Dict[str, Any]) -> None:
        meta["status"] = "superseded"
        meta["superseded_by"] = new_id
        sota_for = _ensure_list(meta, "sota_for")
        meta["sota_for"] = [t for t in sota_for if t != task_id]

    def mutate_task(meta: Dict[str, Any]) -> None:
        current = [e for e in (meta.get("current_sota") or []) if isinstance(e, dict)]
        kept = [e for e in current if e.get("method") != old_id]
        existing_new = [e for e in kept if e.get("method") == new_id]
        if existing_new:
            existing_new[0]["as_of"] = as_of
        else:
            template = next((e for e in current if e.get("method") == old_id), None) or {}
            kept.append({
                "method": new_id,
                "as_of": as_of,
                "benchmark": template.get("benchmark") or "Benchmark",
                "metric": template.get("metric") or "metric",
                "value": template.get("value") if "value" in template else "updated SOTA",
                "notes": template.get("notes") or f"Supersedes {old_id}.",
            })
        meta["current_sota"] = kept
        methods = _ensure_list(meta, "methods")
        if new_id not in methods:
            methods.append(new_id)
        meta["last_reviewed"] = reviewed

    edits = [
        {
            "path": str(new_node.file_path),
            "node": new_id,
            "mutator": mutate_new,
            "summary": f"{new_id}: status=sota, sota_for+={task_id}, supersedes+={old_id}",
        },
        {
            "path": str(old_node.file_path),
            "node": old_id,
            "mutator": mutate_old,
            "summary": f"{old_id}: status=superseded, superseded_by={new_id}",
        },
        {
            "path": str(task_node.file_path),
            "node": task_id,
            "mutator": mutate_task,
            "summary": f"{task_id}: current_sota -> {new_id}, last_reviewed={reviewed}",
        },
    ]

    receipt = (
        f"### {reviewed} — supersede {new_id} over {old_id} for {task_id}\n"
        f"- {new_id} status: sota; sota_for includes {task_id}; supersedes {old_id}.\n"
        f"- {old_id} status: superseded; superseded_by {new_id}; removed from {task_id} current_sota.\n"
        f"- {task_id} current_sota updated (as_of {as_of}); last_reviewed {reviewed}.\n"
    )

    planned_text = []
    for edit in edits:
        planned_text.append({
            "path": edit["path"],
            "node": edit["node"],
            "summary": edit["summary"],
            "content": apply_frontmatter(Path(edit["path"]), edit["mutator"]),
        })

    return {
        "ok": True,
        "errors": [],
        "edits": planned_text,
        "receipt": receipt,
        "changelog_path": str(Path(task_node.file_path).resolve().parent.parent / "CHANGELOG.md"),
        "new_id": new_id,
        "old_id": old_id,
        "task_id": task_id,
    }


def _append_receipt(changelog_path: Path, receipt: str) -> None:
    if changelog_path.exists():
        text = changelog_path.read_text(encoding="utf-8")
        marker = "\n---\n"
        idx = text.find(marker)
        if idx != -1:
            insert_at = idx + len(marker)
            updated = text[:insert_at] + "\n" + receipt.rstrip() + "\n" + text[insert_at:]
        else:
            updated = text.rstrip() + "\n\n" + receipt.rstrip() + "\n"
        changelog_path.write_text(updated, encoding="utf-8")
    else:
        changelog_path.write_text(
            "# Graph Change Log\n\n---\n\n" + receipt.rstrip() + "\n",
            encoding="utf-8",
        )


def postconditions_hold(graph: KnowledgeGraph, new_id: str, old_id: str, task_id: str) -> List[str]:
    failures = []
    new_node = graph.get_node(new_id)
    old_node = graph.get_node(old_id)
    task_node = graph.get_node(task_id)
    if not new_node or not old_node or not task_node:
        return ["post-condition reload missing nodes"]

    if new_node.status != "sota":
        failures.append(f"{new_id} status is {new_node.status}, expected sota")
    if task_id not in (new_node.metadata.get("sota_for") or []):
        failures.append(f"{new_id} sota_for missing {task_id}")
    if old_id not in (new_node.metadata.get("supersedes") or []):
        failures.append(f"{new_id} supersedes missing {old_id}")
    if old_node.status != "superseded":
        failures.append(f"{old_id} status is {old_node.status}, expected superseded")
    if old_node.metadata.get("superseded_by") != new_id:
        failures.append(f"{old_id} superseded_by is {old_node.metadata.get('superseded_by')}")

    current = [
        e.get("method")
        for e in (task_node.metadata.get("current_sota") or [])
        if isinstance(e, dict)
    ]
    if new_id not in current:
        failures.append(f"{task_id} current_sota missing {new_id}")
    if old_id in current:
        failures.append(f"{task_id} current_sota still lists superseded {old_id}")

    for task in graph.get_nodes_by_type("task"):
        for entry in task.metadata.get("current_sota") or []:
            if not isinstance(entry, dict):
                continue
            method = graph.get_node(entry.get("method"))
            if method and method.status == "superseded":
                failures.append(f"{method.id} is superseded but listed on {task.id} current_sota")

    return failures


def apply_supersede(
    graph: KnowledgeGraph,
    new_id: str,
    old_id: str,
    task_id: str,
    dry_run: bool = False,
    today: Optional[date] = None,
) -> Dict[str, Any]:
    plan = plan_supersede(graph, new_id, old_id, task_id, today=today)
    if not plan["ok"]:
        return {**plan, "dry_run": dry_run, "written": False}

    if dry_run:
        return {
            **plan,
            "dry_run": True,
            "written": False,
            "edits": [
                {k: v for k, v in edit.items() if k != "content"} | {"preview": edit["content"][:500]}
                for edit in plan["edits"]
            ],
            "full_edits": plan["edits"],
        }

    backups = []
    try:
        for edit in plan["edits"]:
            path = Path(edit["path"])
            original = path.read_text(encoding="utf-8")
            backups.append((path, original))
            path.write_text(edit["content"], encoding="utf-8")
        changelog = Path(plan["changelog_path"])
        if changelog.exists():
            backups.append((changelog, changelog.read_text(encoding="utf-8")))
        _append_receipt(changelog, plan["receipt"])

        graph_root = Path(plan["edits"][2]["path"]).resolve().parent.parent
        reloaded = load_graph(graph_root)
        failures = postconditions_hold(reloaded, plan["new_id"], plan["old_id"], plan["task_id"])
        validation = validate_graph(reloaded, check_derived=False)
        if validation.has_errors:
            failures.extend(f"{i.node_id}: {i.message}" for i in validation.errors)
        if failures:
            for path, original in reversed(backups):
                path.write_text(original, encoding="utf-8")
            return {
                **plan,
                "dry_run": False,
                "written": False,
                "ok": False,
                "errors": failures,
            }
        return {**plan, "dry_run": False, "written": True, "ok": True}
    except Exception as exc:
        for path, original in reversed(backups):
            path.write_text(original, encoding="utf-8")
        return {**plan, "dry_run": False, "written": False, "ok": False, "errors": [str(exc)]}
