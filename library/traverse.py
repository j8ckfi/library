"""Graph traversal and neighborhood inspection tools."""

from typing import Dict, Any, List, Optional
from library.graph import KnowledgeGraph, Node, Edge


def describe_node_neighborhood(graph: KnowledgeGraph, node_id: str) -> Optional[Dict[str, Any]]:
    """Returns incoming and outgoing edges and connected nodes for inspection."""
    node = graph.get_node(node_id)
    if not node:
        return None

    outgoing = []
    for edge in graph.get_outgoing_edges(node_id):
        target = graph.get_node(edge.target)
        outgoing.append({
            "relation": edge.relation,
            "target_id": edge.target,
            "target_title": target.title if target else "Unknown",
            "target_type": target.type if target else "Unknown",
            "properties": edge.properties
        })

    incoming = []
    for edge in graph.get_incoming_edges(node_id):
        source = graph.get_node(edge.source)
        incoming.append({
            "relation": edge.relation,
            "source_id": edge.source,
            "source_title": source.title if source else "Unknown",
            "source_type": source.type if source else "Unknown",
            "properties": edge.properties
        })

    return {
        "node": node,
        "outgoing": outgoing,
        "incoming": incoming
    }


def find_shortest_path(graph: KnowledgeGraph, start_id: str, end_id: str) -> Optional[List[Dict[str, Any]]]:
    """Finds shortest path between start and end node and returns annotated step-by-step hops."""
    path_ids = graph.find_path(start_id, end_id)
    if not path_ids:
        return None

    steps = []
    for i, n_id in enumerate(path_ids):
        node = graph.get_node(n_id)
        step_info = {
            "step": i,
            "id": n_id,
            "type": node.type if node else "Unknown",
            "title": node.title if node else n_id
        }
        if i > 0:
            prev_id = path_ids[i - 1]
            # Find edge relation between prev and curr
            rel = "connected_to"
            for edge in graph.get_outgoing_edges(prev_id):
                if edge.target == n_id:
                    rel = f"--({edge.relation})-->"
                    break
            if rel == "connected_to":
                for edge in graph.get_incoming_edges(prev_id):
                    if edge.source == n_id:
                        rel = f"<--({edge.relation})--"
                        break
            step_info["transition"] = rel
        steps.append(step_info)

    return steps
