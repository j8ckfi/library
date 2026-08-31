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
        self.assertTrue(any(p["method"].id in ("method:diffusion-opsd", "method:self-opd") for p in diff_res))

        orarl_res = self.engine.sota("task:rl-video-mllm")
        self.assertTrue(any(p["method"].id == "method:orarl" for p in orarl_res))

        ttpo_res = self.engine.sota("task:label-free-test-time-reasoner")
        self.assertTrue(any(p["method"].id == "method:ttpo" for p in ttpo_res))

        u_opsd_res = self.engine.sota("task:label-free-reasoner-posttrain")
        self.assertTrue(any(p["method"].id == "method:u-opsd" for p in u_opsd_res))

        mopd_res = self.engine.sota("task:student-distillation")
        self.assertTrue(any(p["method"].id in ("method:opd", "method:open-mopd") for p in mopd_res))

        grid_pde = self.engine.sota("task:operator-grid-pde")
        self.assertTrue(any(p["method"].id in ("method:cvit", "method:poseidon") for p in grid_pde))

        industrial_mesh = self.engine.sota("task:operator-industrial-mesh")
        self.assertTrue(any(p["method"].id == "method:transolver-3" for p in industrial_mesh))

        foundation_op = self.engine.sota("task:operator-foundation")
        self.assertTrue(any(p["method"].id in ("method:poseidon", "method:unisolver") for p in foundation_op))

        pi_op = self.engine.sota("task:operator-physics-informed")
        self.assertTrue(any(p["method"].id == "method:pi-cvit" for p in pi_op))

        fourier_adapt = self.engine.sota("task:operator-fourier-adapt")
        self.assertTrue(any(p["method"].id == "method:f-adapter" for p in fourier_adapt))

        weather_op = self.engine.sota("task:operator-weather")
        self.assertTrue(any(p["method"].id == "method:fourcastnet-3" for p in weather_op))

        factory = self.engine.sota("task:industrial-model-building")
        self.assertTrue(any(p["method"].id == "method:poolside-model-factory" for p in factory))


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


class TestModelFactorySystemsShelf(unittest.TestCase):
    """Industrial Model Factory is a process shelf, orthogonal to train-kernel SOTA."""

    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.engine = QueryEngine(self.graph)

    def test_systems_domain_is_recognized(self):
        domains = {n.domain for n in self.graph.get_nodes_by_type("task")}
        self.assertIn("systems", domains)

    def test_industrial_model_building_domain_and_sota(self):
        task = self.graph.get_node("task:industrial-model-building")
        self.assertIsNotNone(task)
        self.assertEqual(task.type, "task")
        self.assertEqual(task.domain, "systems")
        paths = self.engine.sota("task:industrial-model-building")
        self.assertTrue(len(paths) > 0)
        self.assertTrue(any(p["method"].id == "method:poolside-model-factory" for p in paths))

    def test_poolside_factory_is_training_systems_sota_for_process_task_only(self):
        method = self.graph.get_node("method:poolside-model-factory")
        self.assertIsNotNone(method)
        self.assertEqual(method.get("category"), "training-systems")
        self.assertEqual(method.status, "sota")
        self.assertEqual(method.get("sota_for"), ["task:industrial-model-building"])
        self.assertEqual(method.get("supersedes") or [], [])

    def test_pretrain_dense_7b_sota_remains_muon2_and_kl_soap(self):
        paths = self.engine.sota("task:pretrain-dense-7b")
        method_ids = [p["method"].id for p in paths]
        self.assertTrue(any(m in method_ids for m in ("method:muon2", "method:soap-muon-scale")))
        self.assertNotIn("method:poolside-model-factory", method_ids)

    def test_factory_does_not_retarget_train_kernel_sota(self):
        dense_rl = self.engine.sota("task:math-code-rl-dense")
        self.assertTrue(any(p["method"].id == "method:cispo" for p in dense_rl))
        self.assertFalse(any(p["method"].id == "method:poolside-model-factory" for p in dense_rl))

        open_data = self.engine.sota("task:open-data-recipe")
        self.assertTrue(any(p["method"].id == "method:olmo-3" for p in open_data))
        self.assertFalse(any(p["method"].id in ("method:poolside-model-factory", "method:automixer") for p in open_data))

        moe_arch = self.engine.sota("task:pretrain-moe-frontier")
        moe_ids = [p["method"].id for p in moe_arch]
        self.assertTrue(any(m in moe_ids for m in ("method:deepseek-v4", "method:kimi-k3")))
        self.assertNotIn("method:poolside-model-factory", moe_ids)

    def test_automixer_is_active_component_not_data_recipe_sota(self):
        automixer = self.graph.get_node("method:automixer")
        self.assertIsNotNone(automixer)
        self.assertEqual(automixer.status, "active")
        self.assertNotIn("task:open-data-recipe", automixer.get("sota_for") or [])
        self.assertNotIn("method:olmo-3", automixer.get("supersedes") or [])
        olmo = self.graph.get_node("method:olmo-3")
        self.assertNotEqual(olmo.get("superseded_by"), "method:automixer")

    def test_blender_and_hive_are_active_factory_components(self):
        blender = self.graph.get_node("method:blender-streaming")
        hive = self.graph.get_node("method:hive-synth")
        self.assertIsNotNone(blender)
        self.assertIsNotNone(hive)
        self.assertEqual(blender.status, "active")
        self.assertEqual(hive.status, "active")
        self.assertEqual(blender.get("category"), "training-systems")
        self.assertEqual(hive.get("category"), "training-systems")

    def test_small_lab_recipe_implements_factory_not_internal_packages(self):
        recipe = self.graph.get_node("recipe:small-lab-model-factory")
        self.assertIsNotNone(recipe)
        self.assertEqual(recipe.get("method"), "method:poolside-model-factory")
        self.assertEqual(recipe.get("task"), "task:industrial-model-building")
        deps = " ".join(recipe.get("pip_dependencies") or [])
        self.assertIn("dagster", deps.lower())
        body = recipe.body.lower()
        self.assertNotIn("poolside-titan", body)
        self.assertNotIn("poolside-atlas", body)
        self.assertNotIn("poolside-hive", body)


if __name__ == "__main__":
    unittest.main()
