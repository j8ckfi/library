"""Parser and loader for markdown graph nodes and frontmatter metadata."""

import re
from pathlib import Path
from typing import Dict, Any, Tuple, Optional
import yaml

from library.graph import KnowledgeGraph, Node


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Extracts YAML frontmatter and markdown body from file content."""
    pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
    match = re.match(pattern, content, re.DOTALL)
    if not match:
        # Fallback if no frontmatter or malformed
        return {}, content

    frontmatter_raw = match.group(1)
    body = match.group(2)
    try:
        data = yaml.safe_load(frontmatter_raw) or {}
        if not isinstance(data, dict):
            data = {}
        return data, body
    except Exception as e:
        return {"_parse_error": str(e)}, body


def load_node_from_file(file_path: Path) -> Optional[Node]:
    """Loads a single markdown node file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return None

    metadata, body = parse_frontmatter(content)
    node_id = metadata.get("id")
    node_type = metadata.get("type")

    # If missing in frontmatter, infer from directory and filename
    if not node_type:
        parent_name = file_path.parent.name
        if parent_name in ("tasks", "methods", "papers", "recipes"):
            node_type = parent_name.rstrip("s")
            if node_type == "task":
                node_type = "task"
            elif node_type == "method":
                node_type = "method"
            elif node_type == "paper":
                node_type = "paper"
            elif node_type == "recipe":
                node_type = "recipe"

    if not node_id:
        slug = file_path.stem
        node_id = f"{node_type}:{slug}" if node_type else slug

    title = metadata.get("title")
    if not title:
        # Try extracting the first H1 header in markdown body
        h1_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        title = h1_match.group(1).strip() if h1_match else file_path.stem

    return Node(
        id=node_id,
        type=node_type or "unknown",
        title=title,
        file_path=file_path,
        metadata=metadata,
        body=body.strip()
    )


def load_graph(root_dir: Path) -> KnowledgeGraph:
    """Recursively scans directory and builds the KnowledgeGraph with all typed edges."""
    graph = KnowledgeGraph()
    root_path = Path(root_dir)

    # 1. Scan and register all markdown nodes
    node_files = list(root_path.rglob("*.md"))
    for file_path in node_files:
        # Skip docs, templates, and top-level README/AGENTS files when loading graph/
        if "templates" in file_path.parts or "docs" in file_path.parts:
            continue
        if file_path.name in ("README.md", "AGENTS.md", "PULL_REQUEST_TEMPLATE.md"):
            continue

        node = load_node_from_file(file_path)
        if node and node.type in ("task", "method", "paper", "recipe"):
            graph.add_node(node)

    # 2. Extract and link edges based on ontology relationships
    for node in graph.nodes.values():
        meta = node.metadata
        n_id = node.id
        n_type = node.type

        if n_type == "task":
            # task -> method edges
            for sota_entry in meta.get("current_sota", []):
                if isinstance(sota_entry, dict) and "method" in sota_entry:
                    m_id = sota_entry["method"]
                    graph.add_edge(n_id, m_id, "has_sota_method", sota_entry)
                    graph.add_edge(m_id, n_id, "sota_for", sota_entry)

            for m_id in meta.get("methods", []):
                graph.add_edge(n_id, m_id, "addresses_task_method")
                graph.add_edge(m_id, n_id, "targets_task")

        elif n_type == "method":
            # sota_for
            for t_id in meta.get("sota_for", []):
                graph.add_edge(n_id, t_id, "sota_for")

            # supersedes / superseded_by
            for s_id in meta.get("supersedes", []):
                graph.add_edge(n_id, s_id, "supersedes")
                graph.add_edge(s_id, n_id, "superseded_by")

            sup_by = meta.get("superseded_by")
            if sup_by:
                graph.add_edge(n_id, sup_by, "superseded_by")
                graph.add_edge(sup_by, n_id, "supersedes")

            # papers
            for p_id in meta.get("papers", []):
                graph.add_edge(n_id, p_id, "described_in")
                graph.add_edge(p_id, n_id, "introduces")

            # recipes
            for r_id in meta.get("recipes", []):
                graph.add_edge(n_id, r_id, "implemented_by")
                graph.add_edge(r_id, n_id, "implements")

        elif n_type == "paper":
            for m_id in meta.get("methods", []):
                graph.add_edge(n_id, m_id, "introduces")
                graph.add_edge(m_id, n_id, "described_in")

            for cited_p_id in meta.get("cites", []):
                graph.add_edge(n_id, cited_p_id, "cites")
                graph.add_edge(cited_p_id, n_id, "cited_by")

        elif n_type == "recipe":
            m_id = meta.get("method")
            if m_id:
                graph.add_edge(n_id, m_id, "implements")
                graph.add_edge(m_id, n_id, "implemented_by")

            t_id = meta.get("task")
            if t_id:
                graph.add_edge(n_id, t_id, "recipe_for_task")

    return graph
