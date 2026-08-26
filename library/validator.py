"""Graph integrity, schema, and reference validator."""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Set, Any
from pathlib import Path

from library.graph import KnowledgeGraph, Node


@dataclass
class Issue:
    level: str  # "ERROR" or "WARNING"
    node_id: str
    file_path: Path
    message: str


@dataclass
class ValidationResult:
    issues: List[Issue] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(issue.level == "ERROR" for issue in self.issues)

    @property
    def errors(self) -> List[Issue]:
        return [issue for issue in self.issues if issue.level == "ERROR"]

    @property
    def warnings(self) -> List[Issue]:
        return [issue for issue in self.issues if issue.level == "WARNING"]


DATE_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
ID_PATTERN = re.compile(r"^(task|method|paper|recipe):[a-zA-Z0-9._-]+$")


def validate_node_schema(node: Node) -> List[Issue]:
    """Validates individual node frontmatter against required ontology fields."""
    issues: List[Issue] = []
    meta = node.metadata
    n_id = node.id
    path = node.file_path

    # Check parse errors
    if "_parse_error" in meta:
        issues.append(Issue("ERROR", n_id, path, f"YAML parse error: {meta['_parse_error']}"))
        return issues

    # ID format
    if not ID_PATTERN.match(n_id):
        issues.append(Issue("ERROR", n_id, path, f"Invalid ID format '{n_id}'. Expected prefix 'task:', 'method:', 'paper:', or 'recipe:' with alphanumeric slug."))

    # Type matching
    expected_type = n_id.split(":", 1)[0]
    if node.type != expected_type:
        issues.append(Issue("ERROR", n_id, path, f"Node type mismatch: ID is '{n_id}' but type field is '{node.type}'"))

    # Type specific required fields
    if node.type == "task":
        for req in ["title", "domain", "summary"]:
            if req not in meta:
                issues.append(Issue("ERROR", n_id, path, f"Task missing required field '{req}'"))

        for sota_entry in meta.get("current_sota", []):
            if not isinstance(sota_entry, dict):
                issues.append(Issue("ERROR", n_id, path, "current_sota items must be dictionaries"))
                continue
            for req in ["method", "as_of", "benchmark", "metric", "value"]:
                if req not in sota_entry:
                    issues.append(Issue("ERROR", n_id, path, f"current_sota entry missing required field '{req}'"))
            if "as_of" in sota_entry and not DATE_PATTERN.match(str(sota_entry["as_of"])):
                issues.append(Issue("ERROR", n_id, path, f"current_sota as_of date '{sota_entry.get('as_of')}' must match YYYY-MM format"))

    elif node.type == "method":
        for req in ["title", "category", "status"]:
            if req not in meta:
                issues.append(Issue("ERROR", n_id, path, f"Method missing required field '{req}'"))

        status = meta.get("status")
        if status not in ("sota", "active", "superseded", "niche", "experimental"):
            issues.append(Issue("ERROR", n_id, path, f"Invalid method status '{status}'. Expected one of: sota, active, superseded, niche, experimental"))

        for claim in meta.get("claims", []):
            if not isinstance(claim, dict):
                issues.append(Issue("ERROR", n_id, path, "claims items must be dictionaries"))
                continue
            for req in ["benchmark", "metric", "value", "date"]:
                if req not in claim:
                    issues.append(Issue("ERROR", n_id, path, f"Claim missing required field '{req}'"))
            if "date" in claim and not DATE_PATTERN.match(str(claim["date"])):
                issues.append(Issue("ERROR", n_id, path, f"Claim date '{claim.get('date')}' must match YYYY-MM format"))

    elif node.type == "paper":
        for req in ["title", "authors", "year", "month", "arxiv_id", "url"]:
            if req not in meta:
                issues.append(Issue("ERROR", n_id, path, f"Paper missing required field '{req}'"))

        if "year" in meta and not isinstance(meta["year"], int):
            issues.append(Issue("ERROR", n_id, path, f"Paper year must be integer, got {meta['year']}"))
        if "month" in meta and not isinstance(meta["month"], int):
            issues.append(Issue("ERROR", n_id, path, f"Paper month must be integer, got {meta['month']}"))

    elif node.type == "recipe":
        for req in ["title", "method", "task", "framework", "repo_url"]:
            if req not in meta:
                issues.append(Issue("ERROR", n_id, path, f"Recipe missing required field '{req}'"))

    return issues


def validate_references(graph: KnowledgeGraph) -> List[Issue]:
    """Ensures all target node IDs referenced in metadata actually exist in the graph."""
    issues: List[Issue] = []

    for node in graph.nodes.values():
        meta = node.metadata
        n_id = node.id
        path = node.file_path

        def check_ref(ref_id: Any, field_name: str) -> None:
            if isinstance(ref_id, str):
                if ref_id not in graph.nodes:
                    issues.append(Issue("ERROR", n_id, path, f"Dangling reference in '{field_name}': target node '{ref_id}' does not exist"))
            elif isinstance(ref_id, list):
                for item in ref_id:
                    check_ref(item, field_name)

        if node.type == "task":
            for sota_entry in meta.get("current_sota", []):
                if isinstance(sota_entry, dict) and "method" in sota_entry:
                    check_ref(sota_entry["method"], "current_sota.method")
            check_ref(meta.get("methods", []), "methods")

        elif node.type == "method":
            check_ref(meta.get("sota_for", []), "sota_for")
            check_ref(meta.get("supersedes", []), "supersedes")
            if meta.get("superseded_by"):
                check_ref(meta["superseded_by"], "superseded_by")
            check_ref(meta.get("papers", []), "papers")
            check_ref(meta.get("recipes", []), "recipes")

        elif node.type == "paper":
            check_ref(meta.get("methods", []), "methods")
            check_ref(meta.get("cites", []), "cites")

        elif node.type == "recipe":
            if meta.get("method"):
                check_ref(meta["method"], "method")
            if meta.get("task"):
                check_ref(meta["task"], "task")

    return issues


def validate_supersession_cycles(graph: KnowledgeGraph) -> List[Issue]:
    """Detects cycles in the supersedes relationships."""
    issues: List[Issue] = []
    visited: Set[str] = set()
    rec_stack: Set[str] = set()

    def has_cycle(curr: str) -> bool:
        visited.add(curr)
        rec_stack.add(curr)

        for edge in graph.get_outgoing_edges(curr):
            if edge.relation == "supersedes":
                target = edge.target
                if target not in visited:
                    if has_cycle(target):
                        return True
                elif target in rec_stack:
                    node = graph.get_node(curr)
                    path = node.file_path if node else Path("unknown")
                    issues.append(Issue("ERROR", curr, path, f"Cyclic supersession detected involving '{curr}' and '{target}'"))
                    return True

        rec_stack.remove(curr)
        return False

    for node_id in graph.nodes:
        if node_id not in visited:
            has_cycle(node_id)

    return issues


def validate_graph(graph: KnowledgeGraph) -> ValidationResult:
    """Runs all schema, reference, and consistency checks on the graph."""
    res = ValidationResult()

    for node in graph.nodes.values():
        res.issues.extend(validate_node_schema(node))

    res.issues.extend(validate_references(graph))
    res.issues.extend(validate_supersession_cycles(graph))

    return res
