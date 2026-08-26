"""Graph compiler and exporter to JSON / JSONL formats."""

import json
from pathlib import Path
from typing import Dict, Any, List
from library.graph import KnowledgeGraph


def export_graph_to_dict(graph: KnowledgeGraph) -> Dict[str, Any]:
    """Serializes the entire graph into a single dictionary."""
    nodes_data = []
    for node in graph.nodes.values():
        nodes_data.append({
            "id": node.id,
            "type": node.type,
            "title": node.title,
            "domain": node.domain,
            "status": node.status,
            "file_path": str(node.file_path),
            "metadata": node.metadata,
            "body": node.body
        })

    edges_data = []
    for edge in graph.edges:
        edges_data.append({
            "source": edge.source,
            "target": edge.target,
            "relation": edge.relation,
            "properties": edge.properties
        })

    return {
        "version": "1.0",
        "node_count": len(nodes_data),
        "edge_count": len(edges_data),
        "nodes": nodes_data,
        "edges": edges_data
    }


def export_graph(graph: KnowledgeGraph, output_path: Path, format_type: str = "json") -> None:
    """Exports graph to a file in json or jsonl format."""
    data = export_graph_to_dict(graph)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if format_type.lower() == "jsonl":
        with output_path.open("w", encoding="utf-8") as f:
            for node in data["nodes"]:
                f.write(json.dumps({"record_type": "node", **node}) + "\n")
            for edge in data["edges"]:
                f.write(json.dumps({"record_type": "edge", **edge}) + "\n")
    else:
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
