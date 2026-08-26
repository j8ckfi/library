"""Comprehensive unit and integration test suite for j8ckfi/library."""

import unittest
import tempfile
import shutil
import json
from pathlib import Path

from library.graph import KnowledgeGraph, Node, Edge
from library.loader import load_graph, parse_frontmatter, load_node_from_file
from library.validator import validate_graph, validate_node_schema, validate_references, validate_supersession_cycles
from library.query import QueryEngine, tokenize
from library.traverse import describe_node_neighborhood, find_shortest_path
from library.exporter import export_graph_to_dict, export_graph
from library.ingest import create_node_from_template


class TestKnowledgeGraphLoaderAndValidation(unittest.TestCase):
    def setUp(self):
        self.workspace_graph_path = Path("graph")
        self.graph = load_graph(self.workspace_graph_path)

    def test_seeded_graph_is_not_empty(self):
        self.assertGreater(len(self.graph.nodes), 20)
        self.assertGreater(len(self.graph.edges), 30)

    def test_node_types_present(self):
        tasks = self.graph.get_nodes_by_type("task")
        methods = self.graph.get_nodes_by_type("method")
        papers = self.graph.get_nodes_by_type("paper")
        recipes = self.graph.get_nodes_by_type("recipe")

        self.assertGreaterEqual(len(tasks), 8)
        self.assertGreaterEqual(len(methods), 10)
        self.assertGreaterEqual(len(papers), 10)
        self.assertGreaterEqual(len(recipes), 8)

    def test_seeded_graph_validation_passes(self):
        res = validate_graph(self.graph)
        self.assertFalse(res.has_errors, f"Validation errors found: {[str(e) for e in res.errors]}")
        self.assertEqual(len(res.errors), 0)

    def test_all_sota_methods_have_papers_and_recipes(self):
        sota_methods = [n for n in self.graph.get_nodes_by_type("method") if n.status == "sota"]
        self.assertGreaterEqual(len(sota_methods), 8)

        for m in sota_methods:
            # Check papers
            papers = m.metadata.get("papers", [])
            self.assertTrue(len(papers) > 0, f"SOTA method {m.id} has no attached papers")
            for p_id in papers:
                self.assertIn(p_id, self.graph.nodes, f"Paper {p_id} referenced by {m.id} not found in graph")

            # Check recipes
            recipes = m.metadata.get("recipes", [])
            self.assertTrue(len(recipes) > 0, f"SOTA method {m.id} has no attached recipes")
            for r_id in recipes:
                self.assertIn(r_id, self.graph.nodes, f"Recipe {r_id} referenced by {m.id} not found in graph")

            # Check claims
            claims = m.metadata.get("claims", [])
            self.assertTrue(len(claims) > 0, f"SOTA method {m.id} has no empirical claims")


class TestQueryEngine(unittest.TestCase):
    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.engine = QueryEngine(self.graph)

    def test_query_keyword_search(self):
        results = self.engine.query("Muon optimizer", top_k=3)
        self.assertTrue(len(results) > 0)
        node_ids = [r.node.id for r in results]
        self.assertTrue(any("muon" in nid for nid in node_ids))

    def test_query_sota_filtering(self):
        results = self.engine.query("alignment", sota_only=True)
        for r in results:
            self.assertTrue(r.node.is_sota)

    def test_sota_path_resolution(self):
        paths = self.engine.sota("task:llm-pretraining-optimization")
        self.assertTrue(len(paths) > 0)
        p = paths[0]
        self.assertEqual(p["task"].id, "task:llm-pretraining-optimization")
        self.assertTrue(p["method"].id in ("method:muon-scalable", "method:muon", "method:muon-optimizer"))
        self.assertTrue(any("muon" in paper.id for paper in p["papers"]))
        self.assertTrue(any(recipe.id == "recipe:muon-pretraining" for recipe in p["recipes"]))

    def test_sota_reasoning_rl(self):
        paths = self.engine.sota("reasoning")
        self.assertTrue(len(paths) > 0)
        method_ids = [p["method"].id for p in paths]
        self.assertTrue(any(m in method_ids for m in ("method:dapo", "method:dr-grpo", "method:gspo", "method:grpo")))


class TestGraphTraversalAndPaths(unittest.TestCase):
    def setUp(self):
        self.graph = load_graph(Path("graph"))

    def test_describe_neighborhood(self):
        info = describe_node_neighborhood(self.graph, "method:muon-scalable")
        self.assertIsNotNone(info)
        outgoing_targets = [e["target_id"] for e in info["outgoing"]]
        self.assertIn("task:pretrain-dense-7b", outgoing_targets)
        self.assertIn("paper:muon-scalable", outgoing_targets)
        self.assertIn("recipe:muon-pretraining", outgoing_targets)

    def test_shortest_path(self):
        steps = find_shortest_path(self.graph, "task:pretrain-dense-7b", "recipe:muon-pretraining")
        self.assertIsNotNone(steps)
        self.assertGreaterEqual(len(steps), 2)
        node_ids = [s["id"] for s in steps]
        self.assertEqual(node_ids[0], "task:pretrain-dense-7b")
        self.assertEqual(node_ids[-1], "recipe:muon-pretraining")


class TestExporterAndIngest(unittest.TestCase):
    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_export_to_json(self):
        export_file = Path(self.temp_dir) / "test_graph.json"
        export_graph(self.graph, export_file, format_type="json")
        self.assertTrue(export_file.exists())

        with export_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("nodes", data)
        self.assertIn("edges", data)
        self.assertEqual(len(data["nodes"]), len(self.graph.nodes))

    def test_create_node_from_template(self):
        out_path = Path(self.temp_dir) / "tasks"
        created = create_node_from_template("task", "custom-eval-task", title="Custom Eval Task", output_dir=out_path)
        self.assertTrue(created.exists())
        self.assertTrue(created.name == "custom-eval-task.md")

        node = load_node_from_file(created)
        self.assertIsNotNone(node)
        self.assertEqual(node.id, "task:custom-eval-task")
        self.assertEqual(node.type, "task")


if __name__ == "__main__":
    unittest.main()
