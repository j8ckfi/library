"""Output-tier helpers: brief (~10 lines), default prose, JSON."""

import json
from typing import Any, Iterable, List, Optional

BRIEF_MAX_LINES = 10


def emit_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))


def print_brief(lines: Iterable[str], max_lines: int = BRIEF_MAX_LINES) -> None:
    """Print up to max_lines, cutting whole lines (never mid-claim)."""
    count = 0
    for line in lines:
        if count >= max_lines:
            break
        print(line)
        count += 1


def format_claim(claim: dict) -> str:
    """One atomic claim row. Do not split this string across budget cuts."""
    if not isinstance(claim, dict):
        return str(claim)
    baseline = f" vs {claim.get('baseline')}" if claim.get("baseline") else ""
    verified = "verified" if claim.get("verified") else "unverified"
    level = claim.get("evidence_level")
    level_bit = f", {level}" if level else ""
    return (
        f"{claim.get('benchmark')}: {claim.get('metric')} = {claim.get('value')}"
        f"{baseline} [{claim.get('date')}; {verified}{level_bit}]"
    )


def top_claim(claims: Optional[List[Any]]) -> Optional[dict]:
    if not claims:
        return None
    verified = [c for c in claims if isinstance(c, dict) and c.get("verified")]
    pool = verified or [c for c in claims if isinstance(c, dict)]
    return pool[0] if pool else None


def node_json(node) -> dict:
    if node is None:
        return None
    return {
        "id": node.id,
        "type": node.type,
        "title": node.title,
        "status": node.status,
        "domain": node.domain,
        "file_path": str(node.file_path) if node.file_path else None,
        "metadata": node.metadata,
        "body": node.body,
    }


def node_json_brief(node) -> dict:
    if node is None:
        return None
    return {
        "id": node.id,
        "type": node.type,
        "title": node.title,
        "status": node.status,
        "domain": node.domain,
        "file_path": str(node.file_path) if node.file_path else None,
    }


def output_mode(args) -> str:
    if getattr(args, "json", False):
        return "json"
    if getattr(args, "brief", False):
        return "brief"
    return "default"
