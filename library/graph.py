"""Graph data structures for nodes, edges, and the in-memory knowledge graph."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Any
from pathlib import Path


@dataclass
class Edge:
    """Directed edge in the knowledge graph."""
    source: str
    target: str
    relation: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Node:
    """Node in the knowledge graph with frontmatter metadata and markdown body."""
    id: str
    type: str
    title: str
    file_path: Path
    metadata: Dict[str, Any] = field(default_factory=dict)
    body: str = ""

    @property
    def domain(self) -> Optional[str]:
        return self.metadata.get("domain")

    @property
    def status(self) -> Optional[str]:
        return self.metadata.get("status")

    @property
    def tags(self) -> List[str]:
        return self.metadata.get("tags", [])

    @property
    def is_sota(self) -> bool:
        return self.status == "sota" or bool(self.metadata.get("sota_for"))

    def get(self, key: str, default: Any = None) -> Any:
        return self.metadata.get(key, default)


class KnowledgeGraph:
    """In-memory index of tasks, methods, papers, and recipes with typed edges."""

    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []
        self._outgoing: Dict[str, List[Edge]] = {}
        self._incoming: Dict[str, List[Edge]] = {}

    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node
        if node.id not in self._outgoing:
            self._outgoing[node.id] = []
        if node.id not in self._incoming:
            self._incoming[node.id] = []

    def add_edge(self, source: str, target: str, relation: str, properties: Optional[Dict[str, Any]] = None) -> None:
        # Avoid duplicate edges with the same source, target, and relation
        for existing in self._outgoing.get(source, []):
            if existing.target == target and existing.relation == relation:
                return
        edge = Edge(source=source, target=target, relation=relation, properties=properties or {})
        self.edges.append(edge)
        self._outgoing.setdefault(source, []).append(edge)
        self._incoming.setdefault(target, []).append(edge)

    def get_node(self, node_id: str) -> Optional[Node]:
        return self.nodes.get(node_id)

    def get_nodes_by_type(self, node_type: str) -> List[Node]:
        return [node for node in self.nodes.values() if node.type == node_type]

    def get_outgoing_edges(self, node_id: str) -> List[Edge]:
        return self._outgoing.get(node_id, [])

    def get_incoming_edges(self, node_id: str) -> List[Edge]:
        return self._incoming.get(node_id, [])

    def get_neighbors(self, node_id: str, relation: Optional[str] = None) -> List[Node]:
        neighbors = []
        for edge in self.get_outgoing_edges(node_id):
            if relation is None or edge.relation == relation:
                target_node = self.get_node(edge.target)
                if target_node:
                    neighbors.append(target_node)
        return neighbors

    def get_predecessors(self, node_id: str, relation: Optional[str] = None) -> List[Node]:
        predecessors = []
        for edge in self.get_incoming_edges(node_id):
            if relation is None or edge.relation == relation:
                source_node = self.get_node(edge.source)
                if source_node:
                    predecessors.append(source_node)
        return predecessors

    def find_path(self, start_id: str, end_id: str) -> Optional[List[str]]:
        """Breadth-first search for the shortest path between two nodes."""
        if start_id not in self.nodes or end_id not in self.nodes:
            return None
        if start_id == end_id:
            return [start_id]

        queue: List[List[str]] = [[start_id]]
        visited: Set[str] = {start_id}

        while queue:
            path = queue.pop(0)
            curr = path[-1]

            # Check all adjacent nodes (both outgoing and incoming for bidirectional navigation)
            adjacent: Set[str] = set()
            for edge in self.get_outgoing_edges(curr):
                adjacent.add(edge.target)
            for edge in self.get_incoming_edges(curr):
                adjacent.add(edge.source)

            for neighbor in adjacent:
                if neighbor == end_id:
                    return path + [neighbor]
                if neighbor not in visited and neighbor in self.nodes:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None

    def get_sota_path_for_task(self, task_id: str) -> List[Dict[str, Any]]:
        """Finds canonical SOTA resolution paths: task -> sota method -> paper -> recipe."""
        task_node = self.get_node(task_id)
        if not task_node or task_node.type != "task":
            return []

        results = []
        current_sota = task_node.get("current_sota", [])

        # Also look up methods pointing to this task with sota_for
        sota_method_ids = set()
        for sota_entry in current_sota:
            if isinstance(sota_entry, dict) and "method" in sota_entry:
                sota_method_ids.add(sota_entry["method"])

        for edge in self.get_incoming_edges(task_id):
            if edge.relation == "sota_for":
                sota_method_ids.add(edge.source)

        for method_id in sota_method_ids:
            method_node = self.get_node(method_id)
            if not method_node:
                continue

            # Find papers
            papers = []
            seen_paper_ids = set()
            for edge in self.get_outgoing_edges(method_id):
                if edge.relation in ("cites", "described_in"):
                    p_node = self.get_node(edge.target)
                    if p_node and p_node.id not in seen_paper_ids:
                        seen_paper_ids.add(p_node.id)
                        papers.append(p_node)
            for edge in self.get_incoming_edges(method_id):
                if edge.relation in ("introduces", "describes"):
                    p_node = self.get_node(edge.source)
                    if p_node and p_node.id not in seen_paper_ids:
                        seen_paper_ids.add(p_node.id)
                        papers.append(p_node)

            # Find recipes
            recipes = []
            seen_recipe_ids = set()
            for edge in self.get_outgoing_edges(method_id):
                if edge.relation == "implemented_by":
                    r_node = self.get_node(edge.target)
                    if r_node and r_node.id not in seen_recipe_ids:
                        seen_recipe_ids.add(r_node.id)
                        recipes.append(r_node)
            for edge in self.get_incoming_edges(method_id):
                if edge.relation in ("implements", "uses_method"):
                    r_node = self.get_node(edge.source)
                    if r_node and r_node.id not in seen_recipe_ids:
                        seen_recipe_ids.add(r_node.id)
                        recipes.append(r_node)

            results.append({
                "task": task_node,
                "method": method_node,
                "papers": papers,
                "recipes": recipes,
                "claims": method_node.get("claims", [])
            })

        return results
