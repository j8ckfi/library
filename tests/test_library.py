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
        self.assertGreater(len(self.graph.nodes), 50)
        self.assertGreater(len(self.graph.edges), 100)

    def test_node_types_present(self):
        tasks = self.graph.get_nodes_by_type("task")
        methods = self.graph.get_nodes_by_type("method")
        papers = self.graph.get_nodes_by_type("paper")
        recipes = self.graph.get_nodes_by_type("recipe")

        self.assertGreaterEqual(len(tasks), 15)
        self.assertGreaterEqual(len(methods), 30)
        self.assertGreaterEqual(len(papers), 40)
        self.assertGreaterEqual(len(recipes), 30)

    def test_seeded_graph_validation_passes(self):
        res = validate_graph(self.graph)
        self.assertFalse(res.has_errors, f"Validation errors found: {[str(e) for e in res.errors]}")
        self.assertEqual(len(res.errors), 0)

    def test_all_sota_methods_have_papers_and_recipes(self):
        sota_methods = [n for n in self.graph.get_nodes_by_type("method") if n.status == "sota"]
        self.assertGreaterEqual(len(sota_methods), 15)

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
        results = self.engine.query("Muon2 optimizer", top_k=3)
        self.assertTrue(len(results) > 0)
        node_ids = [r.node.id for r in results]
        self.assertTrue(any("muon2" in nid for nid in node_ids))

    def test_query_sota_filtering(self):
        results = self.engine.query("alignment", sota_only=True)
        for r in results:
            self.assertTrue(r.node.is_sota)

    def test_sota_path_resolution(self):
        paths = self.engine.sota("task:pretrain-dense-7b")
        self.assertTrue(len(paths) > 0)
        p = paths[0]
        self.assertEqual(p["task"].id, "task:pretrain-dense-7b")
        self.assertTrue(p["method"].id in ("method:muon2", "method:soap-muon-scale"))
        self.assertTrue(any("muon" in paper.id or "soap" in paper.id for paper in p["papers"]))

    def test_sota_reasoning_rl(self):
        paths = self.engine.sota("reasoning")
        self.assertTrue(len(paths) > 0)
        method_ids = [p["method"].id for p in paths]
        self.assertTrue(any(m in method_ids for m in ("method:cispo", "method:sapo", "method:verigate", "method:dapo")))

    def test_first_hop_sota_routing(self):
        # Verify new first-hop SOTA routing resolves correctly
        dense_opt = self.engine.sota("task:pretrain-dense-7b")
        self.assertTrue(any(p["method"].id == "method:muon2" for p in dense_opt))

        open_data = self.engine.sota("task:open-data-recipe")
        self.assertTrue(any(p["method"].id == "method:olmo-3" for p in open_data))

        moe_arch = self.engine.sota("task:pretrain-moe-frontier")
        self.assertTrue(any(p["method"].id == "method:deepseek-v4" for p in moe_arch))

        instruct = self.engine.sota("task:instruct-sft-alignment")
        self.assertTrue(any(p["method"].id in ("method:olmo-3", "method:nemotron-cascade-2") for p in instruct))

        dense_rl = self.engine.sota("task:math-code-rl-dense")
        self.assertTrue(any(p["method"].id == "method:cispo" for p in dense_rl))

        moe_rl = self.engine.sota("task:math-code-rl-moe")
        self.assertTrue(any(p["method"].id == "method:sapo" for p in moe_rl))

        async_rl = self.engine.sota("task:agentic-async-rl")
        self.assertTrue(any(p["method"].id == "method:sao" for p in async_rl))

        distill = self.engine.sota("task:student-distillation")
        self.assertTrue(any(p["method"].id == "method:opd" for p in distill))

        snn = self.engine.sota("task:spiking-neural-networks-training")
        self.assertTrue(any(p["method"].id == "method:longspike" for p in snn))

        control = self.engine.sota("task:continuous-control-world-model")
        self.assertTrue(any(p["method"].id == "method:efficienttdmpc" for p in control))

        video = self.engine.sota("task:learned-video-compression")
        self.assertTrue(any(p["method"].id in ("method:dcvc-uf", "method:mlvc") for p in video))

        nvl72_moe = self.engine.sota("task:train-moe-nvl72")
        self.assertTrue(any(p["method"].id == "method:mixture-of-kittens" for p in nvl72_moe))

        opdvr_res = self.engine.sota("task:distill-reasoner-verifier")
        self.assertTrue(any(p["method"].id == "method:opdvr" for p in opdvr_res))

        bpco_res = self.engine.sota("task:token-level-critic-rl")
        self.assertTrue(any(p["method"].id == "method:bpco" for p in bpco_res))

        diff_res = self.engine.sota("task:posttrain-diffusion")
        self.assertTrue(any(p["method"].id == "method:diffusion-opsd" for p in diff_res))

        orarl_res = self.engine.sota("task:rl-video-mllm")
        self.assertTrue(any(p["method"].id == "method:orarl" for p in orarl_res))


class TestGraphTraversalAndPaths(unittest.TestCase):
    def setUp(self):
        self.graph = load_graph(Path("graph"))

    def test_describe_neighborhood(self):
        info = describe_node_neighborhood(self.graph, "method:muon2")
        self.assertIsNotNone(info)
        outgoing_targets = [e["target_id"] for e in info["outgoing"]]
        self.assertIn("task:pretrain-dense-7b", outgoing_targets)
        self.assertIn("paper:muon2", outgoing_targets)
        self.assertIn("recipe:muon2-pretraining", outgoing_targets)

    def test_shortest_path(self):
        steps = find_shortest_path(self.graph, "task:pretrain-dense-7b", "recipe:muon2-pretraining")
        self.assertIsNotNone(steps)
        self.assertGreaterEqual(len(steps), 2)
        node_ids = [s["id"] for s in steps]
        self.assertEqual(node_ids[0], "task:pretrain-dense-7b")
        self.assertEqual(node_ids[-1], "recipe:muon2-pretraining")


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
