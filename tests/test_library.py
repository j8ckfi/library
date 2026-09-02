"""Comprehensive unit and integration test suite for j8ckfi/library."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from library.decide import build_decision
from library.exporter import export_graph, export_graph_to_dict
from library.graph import Edge, KnowledgeGraph, Node
from library.indexgen import derived_drift, write_index
from library.ingest import create_node_from_template
from library.loader import load_graph, load_node_from_file, parse_frontmatter
from library.query import QueryEngine, tokenize
from library.stale import collect_stale
from library.supersede import apply_supersede
from library.traverse import describe_node_neighborhood, find_shortest_path
from library.validator import (
    validate_graph,
    validate_node_schema,
    validate_references,
    validate_supersession_cycles,
)


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
        self.assertFalse(any(p["method"].id == "method:puro-2b" for p in dense_opt))

        budget_pretrain = self.engine.sota("task:budget-consumer-pretrain")
        self.assertTrue(any(p["method"].id == "method:puro-2b" for p in budget_pretrain))

        open_data = self.engine.sota("task:open-data-recipe")
        self.assertTrue(any(p["method"].id == "method:olmo-3" for p in open_data))

        moe_arch = self.engine.sota("task:pretrain-moe-frontier")
        self.assertTrue(any(p["method"].id == "method:deepseek-v4" for p in moe_arch))

        instruct = self.engine.sota("task:instruct-sft-alignment")
        self.assertTrue(any(p["method"].id in ("method:olmo-3", "method:nemotron-cascade-2") for p in instruct))

        dense_rl = self.engine.sota("task:math-code-rl-dense")
        self.assertTrue(any(p["method"].id == "method:cispo" for p in dense_rl))
        self.assertFalse(any(p["method"].id == "method:es-reasoning" for p in dense_rl))

        es_coverage = self.engine.sota("task:passk-reasoning-coverage")
        self.assertTrue(any(p["method"].id == "method:es-reasoning" for p in es_coverage))

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

        vista_res = self.engine.sota("task:privileged-teacher-opsd")
        self.assertTrue(any(p["method"].id == "method:vista" for p in vista_res))

        j_zero_res = self.engine.sota("task:data-free-self-evolution")
        self.assertTrue(any(p["method"].id == "method:j-zero" for p in j_zero_res))

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

        directed_sssp = self.engine.sota("task:directed-sssp-nonneg")
        self.assertTrue(any(p["method"].id == "method:bmssp" for p in directed_sssp))
        self.assertFalse(any(
            p["method"].id in ("method:muon2", "method:cispo", "method:olmo-3", "method:dijkstra")
            for p in directed_sssp
        ))

        tda = self.engine.sota("task:training-data-attribution")
        self.assertTrue(any(p["method"].id == "method:magic" for p in tda))
        self.assertFalse(any(p["method"].id == "method:bergson" for p in tda))

        keyword_sssp = self.engine.sota("directed sssp")
        self.assertTrue(any(p["method"].id == "method:bmssp" for p in keyword_sssp))

    def test_bmssp_isolated_from_training_sota(self):
        training_tasks = (
            "task:pretrain-dense-7b",
            "task:pretrain-moe-frontier",
            "task:math-code-rl-dense",
            "task:instruct-sft-alignment",
            "task:open-data-recipe",
            "task:parameter-efficient-fine-tuning",
        )
        for task_id in training_tasks:
            task = self.graph.get_node(task_id)
            self.assertIsNotNone(task, f"missing {task_id}")
            sota_ids = [entry["method"] for entry in task.metadata.get("current_sota", [])]
            self.assertNotIn("method:bmssp", sota_ids)
            self.assertNotIn("method:bmssp", task.metadata.get("methods", []))

        sssp_task = self.graph.get_node("task:directed-sssp-nonneg")
        self.assertEqual(sssp_task.domain, "algorithms")
        bmssp = self.graph.get_node("method:bmssp")
        self.assertEqual(bmssp.metadata.get("category"), "graph-algorithms")
        self.assertEqual(bmssp.status, "sota")
        self.assertEqual(bmssp.metadata.get("sota_for"), ["task:directed-sssp-nonneg"])
        dijkstra = self.graph.get_node("method:dijkstra")
        self.assertEqual(dijkstra.status, "superseded")
        self.assertEqual(dijkstra.metadata.get("superseded_by"), "method:bmssp")
        self.assertEqual(dijkstra.metadata.get("sota_for"), [])


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

    def test_shortest_path_directed_sssp(self):
        steps = find_shortest_path(self.graph, "task:directed-sssp-nonneg", "recipe:bmssp-python")
        self.assertIsNotNone(steps)
        self.assertGreaterEqual(len(steps), 2)
        node_ids = [s["id"] for s in steps]
        self.assertEqual(node_ids[0], "task:directed-sssp-nonneg")
        self.assertEqual(node_ids[-1], "recipe:bmssp-python")


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


class TestDataAttributionShelf(unittest.TestCase):
    """Bergson/MAGIC is diagnostic tooling; it must not retarget train-kernel SOTA."""

    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.engine = QueryEngine(self.graph)

    def test_training_data_attribution_sota_is_magic_not_bergson(self):
        task = self.graph.get_node("task:training-data-attribution")
        self.assertIsNotNone(task)
        self.assertEqual(task.domain, "interpretability")
        sota_ids = [entry["method"] for entry in task.metadata.get("current_sota", [])]
        self.assertEqual(sota_ids, ["method:magic"])
        self.assertNotIn("method:bergson", sota_ids)
        paths = self.engine.sota("task:training-data-attribution")
        self.assertTrue(any(p["method"].id == "method:magic" for p in paths))
        self.assertFalse(any(p["method"].id == "method:bergson" for p in paths))

    def test_bergson_is_active_library_with_empty_sota_for(self):
        bergson = self.graph.get_node("method:bergson")
        self.assertIsNotNone(bergson)
        self.assertEqual(bergson.status, "active")
        self.assertEqual(bergson.metadata.get("sota_for") or [], [])
        self.assertEqual(bergson.metadata.get("category"), "data-attribution")
        self.assertEqual(bergson.metadata.get("supersedes") or [], [])
        magic = self.graph.get_node("method:magic")
        self.assertNotEqual(magic.metadata.get("superseded_by"), "method:bergson")
        self.assertNotIn("method:magic", bergson.metadata.get("supersedes") or [])

    def test_bergson_does_not_appear_on_mix_or_factory_sota(self):
        open_data = self.graph.get_node("task:open-data-recipe")
        factory = self.graph.get_node("task:industrial-model-building")
        open_sota = [entry["method"] for entry in open_data.metadata.get("current_sota", [])]
        factory_sota = [entry["method"] for entry in factory.metadata.get("current_sota", [])]
        self.assertNotIn("method:bergson", open_sota)
        self.assertNotIn("method:bergson", factory_sota)
        self.assertIn("method:olmo-3", open_sota)
        self.assertIn("method:poolside-model-factory", factory_sota)
        self.assertNotIn("method:bergson", factory.metadata.get("methods") or [])
        recipe = self.graph.get_node("recipe:small-lab-model-factory")
        self.assertEqual(recipe.get("method"), "method:poolside-model-factory")

    def test_trackstar_ekfac_source_exist(self):
        trackstar = self.graph.get_node("method:trackstar")
        ekfac = self.graph.get_node("method:ek-fac")
        source = self.graph.get_node("method:source-unrolling")
        self.assertIsNotNone(trackstar)
        self.assertIsNotNone(ekfac)
        self.assertIsNotNone(source)
        self.assertEqual(trackstar.status, "active")
        self.assertEqual(ekfac.status, "active")
        self.assertEqual(source.status, "niche")
        for method in (trackstar, ekfac, source):
            self.assertEqual(method.metadata.get("category"), "data-attribution")
            self.assertEqual(method.metadata.get("sota_for") or [], [])

    def test_locked_training_sota_unchanged(self):
        locks = {
            "task:pretrain-dense-7b": "method:muon2",
            "task:math-code-rl-dense": "method:cispo",
            "task:open-data-recipe": "method:olmo-3",
            "task:industrial-model-building": "method:poolside-model-factory",
            "task:directed-sssp-nonneg": "method:bmssp",
            "task:teacher-free-on-policy-self-adaptation": "method:opsa",
        }
        for task_id, method_id in locks.items():
            paths = self.engine.sota(task_id)
            self.assertTrue(
                any(p["method"].id == method_id for p in paths),
                f"{task_id} lost {method_id}",
            )
            self.assertFalse(any(p["method"].id == "method:bergson" for p in paths))
            self.assertFalse(any(p["method"].id == "method:magic" for p in paths))

        sae = self.engine.sota("task:mechanistic-interpretability-dictionaries")
        sae_ids = [p["method"].id for p in sae]
        self.assertIn("method:sasa", sae_ids)
        self.assertIn("method:circuitsteer", sae_ids)
        self.assertIn("method:fega", sae_ids)
        self.assertNotIn("method:bergson", sae_ids)
        self.assertNotIn("method:magic", sae_ids)


def run_cli(*cli_args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "library", *cli_args],
        capture_output=True,
        text=True,
        cwd=str(Path(".").resolve()),
    )


class TestCliErgonomics(unittest.TestCase):
    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.engine = QueryEngine(self.graph)

    def test_index_writes_and_is_idempotent(self):
        first = write_index(self.graph)
        self.assertTrue(first["written"])
        index_path = Path("graph/INDEX.md")
        self.assertTrue(index_path.exists())
        text1 = index_path.read_text(encoding="utf-8")
        self.assertIn("task:pretrain-dense-7b", text1)
        self.assertIn("DO NOT HAND-EDIT", text1)
        second = write_index(load_graph(Path("graph")))
        text2 = Path(second["written"][0]).read_text(encoding="utf-8")
        self.assertEqual(text1, text2)
        self.assertFalse(second["stale"])
        agents = Path("AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("<!-- CHEAT-SHEET:START -->", agents)
        self.assertIn("<!-- CHEAT-SHEET:END -->", agents)

    def test_validate_warns_if_index_missing_or_stale(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            res = validate_graph(self.graph, graph_root=tmp, agents_path=tmp / "AGENTS.md")
            self.assertFalse(res.has_errors)
            self.assertTrue(
                any("INDEX" in w.message or "missing" in w.message.lower() for w in res.warnings)
            )
        finally:
            shutil.rmtree(tmp)

        write_index(self.graph)
        index_path = Path("graph/INDEX.md")
        original = index_path.read_text(encoding="utf-8")
        try:
            index_path.write_text(original + "\n# tamper\n", encoding="utf-8")
            res_stale = validate_graph(load_graph(Path("graph")))
            self.assertFalse(res_stale.has_errors)
            self.assertTrue(any("stale" in w.message.lower() for w in res_stale.warnings))
        finally:
            index_path.write_text(original, encoding="utf-8")

    def test_sota_brief_and_json_parse(self):
        brief = run_cli("sota", "task:math-code-rl-dense", "--brief")
        self.assertEqual(brief.returncode, 0, brief.stderr)
        self.assertIn("cispo", brief.stdout.lower())
        self.assertLessEqual(len(brief.stdout.strip().splitlines()), 12)

        js = run_cli("sota", "task:math-code-rl-dense", "--json")
        self.assertEqual(js.returncode, 0, js.stderr)
        data = json.loads(js.stdout)
        self.assertIn("resolutions", data)
        self.assertIn("decision", data)
        self.assertTrue(data["resolutions"])
        self.assertTrue(data["resolutions"][0]["claims"])

    def test_decide_math_code_rl_dense_cispo_not_grpo(self):
        out = run_cli("decide", "task:math-code-rl-dense")
        self.assertEqual(out.returncode, 0, out.stderr)
        use_section = out.stdout.split("What would I use instead?")[0]
        self.assertIn("CISPO", use_section.upper() + out.stdout.upper())
        self.assertIn("method:cispo", out.stdout)
        self.assertNotIn("method:grpo", use_section.lower())
        payload = build_decision(self.graph, "task:math-code-rl-dense")
        use_ids = [row["id"] for row in payload["use"]]
        self.assertIn("method:cispo", use_ids)
        self.assertNotIn("method:grpo", use_ids)
        instead_ids = [row["id"] for row in payload["instead"]]
        self.assertNotIn("method:grpo", instead_ids)

    def test_stale_max_age_days_1_reports(self):
        out = run_cli("stale", "--max-age-days", "1", "--json")
        self.assertEqual(out.returncode, 1, out.stdout)
        data = json.loads(out.stdout)
        self.assertTrue(data["over_budget"])
        self.assertTrue(any(item.get("over_budget") for item in data["items"]))
        self.assertIn("id", data["items"][0])
        self.assertIn("age_days", data["items"][0])

        report = collect_stale(self.graph, max_age_days=1)
        self.assertTrue(report["over_budget"])

    def test_route_pretrain_dense_7b(self):
        out = run_cli("route", "pretrain dense 7B", "--json")
        self.assertEqual(out.returncode, 0, out.stderr)
        data = json.loads(out.stdout)
        self.assertTrue(data["candidates"])
        self.assertEqual(data["candidates"][0]["id"], "task:pretrain-dense-7b")
        self.assertTrue(data["candidates"][0]["reasons"])
        nonsense = run_cli("route", "zzzz-not-a-real-task-qqq", "--json")
        miss = json.loads(nonsense.stdout)
        self.assertTrue(miss["candidates"])

    def test_supersede_dry_run_does_not_write(self):
        method_path = Path("graph/methods/cispo.md")
        task_path = Path("graph/tasks/math-code-rl-dense.md")
        changelog = Path("graph/CHANGELOG.md")
        before = {
            str(method_path): method_path.read_text(encoding="utf-8"),
            str(task_path): task_path.read_text(encoding="utf-8"),
            str(changelog): changelog.read_text(encoding="utf-8"),
        }
        out = run_cli(
            "supersede",
            "method:cispo",
            "method:dapo",
            "--task",
            "task:math-code-rl-dense",
            "--dry-run",
        )
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("DRY RUN", out.stdout)
        for path, text in before.items():
            self.assertEqual(Path(path).read_text(encoding="utf-8"), text)

    def test_supersede_fixture_write_and_rollback_graph_untouched(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            (tmp / "methods").mkdir()
            (tmp / "tasks").mkdir()
            (tmp / "CHANGELOG.md").write_text("# Graph Change Log\n\n---\n", encoding="utf-8")
            (tmp / "methods" / "alpha.md").write_text(
                """---
id: method:alpha
type: method
title: "Alpha"
category: "optimizer"
status: active
sota_for: []
supersedes: []
papers: []
recipes: []
claims:
  - benchmark: "B"
    metric: "m"
    value: 1
    date: "2026-09"
    verified: true
tags: []
---

# Alpha
""",
                encoding="utf-8",
            )
            (tmp / "methods" / "beta.md").write_text(
                """---
id: method:beta
type: method
title: "Beta"
category: "optimizer"
status: sota
sota_for:
  - task:demo
supersedes: []
papers: []
recipes: []
claims:
  - benchmark: "B"
    metric: "m"
    value: 1
    date: "2026-01"
    verified: true
tags: []
---

# Beta
""",
                encoding="utf-8",
            )
            (tmp / "tasks" / "demo.md").write_text(
                """---
id: task:demo
type: task
title: "Demo"
domain: "pretraining"
summary: "Demo task"
current_sota:
  - method: method:beta
    as_of: "2026-01"
    benchmark: "B"
    metric: "m"
    value: 1
methods:
  - method:beta
  - method:alpha
tags: []
---

# Demo
""",
                encoding="utf-8",
            )
            g = load_graph(tmp)
            result = apply_supersede(g, "method:alpha", "method:beta", "task:demo", dry_run=False)
            self.assertTrue(result["ok"], result.get("errors"))
            self.assertTrue(result["written"])
            reloaded = load_graph(tmp)
            res = validate_graph(reloaded, check_derived=False)
            self.assertFalse(res.has_errors, res.errors)
            alpha = reloaded.get_node("method:alpha")
            beta = reloaded.get_node("method:beta")
            task = reloaded.get_node("task:demo")
            self.assertEqual(alpha.status, "sota")
            self.assertEqual(beta.status, "superseded")
            self.assertEqual(beta.metadata.get("superseded_by"), "method:alpha")
            self.assertEqual(task.metadata["current_sota"][0]["method"], "method:alpha")
        finally:
            shutil.rmtree(tmp)

    def test_validate_real_graph_zero_errors(self):
        write_index(self.graph)
        res = validate_graph(load_graph(Path("graph")))
        self.assertEqual(len(res.errors), 0, res.errors)
        drift = derived_drift(load_graph(Path("graph")))
        self.assertEqual(drift, [])

    def test_sota_defaults_locked(self):
        dense = self.engine.sota("task:pretrain-dense-7b")
        self.assertTrue(any(p["method"].id == "method:muon2" for p in dense))
        factory = self.engine.sota("task:industrial-model-building")
        self.assertTrue(any(p["method"].id == "method:poolside-model-factory" for p in factory))
        sssp = self.engine.sota("task:directed-sssp-nonneg")
        self.assertTrue(any(p["method"].id == "method:bmssp" for p in sssp))
        opsa = self.engine.sota("task:teacher-free-on-policy-self-adaptation")
        self.assertTrue(any(p["method"].id == "method:opsa" for p in opsa))
        self.assertFalse(any(p["method"].id == "method:cispo" for p in opsa))
        tda = self.engine.sota("task:training-data-attribution")
        self.assertTrue(any(p["method"].id == "method:magic" for p in tda))
        self.assertFalse(any(p["method"].id == "method:bergson" for p in tda))

    def test_json_on_walk_path_stats_index(self):
        walk = run_cli("walk", "method:cispo", "--json")
        self.assertEqual(walk.returncode, 0, walk.stderr)
        walk_data = json.loads(walk.stdout)
        self.assertEqual(walk_data["id"], "method:cispo")
        self.assertIn("outgoing", walk_data)

        path = run_cli(
            "path",
            "--from",
            "task:pretrain-dense-7b",
            "--to",
            "recipe:muon2-pretraining",
            "--json",
        )
        self.assertEqual(path.returncode, 0, path.stderr)
        path_data = json.loads(path.stdout)
        self.assertGreaterEqual(path_data["hops"], 1)

        stats = run_cli("stats", "--json")
        self.assertEqual(stats.returncode, 0, stats.stderr)
        stats_data = json.loads(stats.stdout)
        self.assertIn("node_count", stats_data)

        idx = run_cli("index", "--json")
        self.assertEqual(idx.returncode, 0, idx.stderr)
        idx_data = json.loads(idx.stdout)
        self.assertIn("written", idx_data)
        self.assertIn("stale", idx_data)


class TestAgentsShelf(unittest.TestCase):
    """Agents shelf is orthogonal to training SOTA (CISPO, Muon2, SAO, ...)."""

    def setUp(self):
        self.graph = load_graph(Path("graph"))
        self.engine = QueryEngine(self.graph)

    def _sota_ids(self, task_id: str):
        task = self.graph.get_node(task_id)
        self.assertIsNotNone(task, f"missing {task_id}")
        return [entry["method"] for entry in task.metadata.get("current_sota", [])]

    def test_agents_domain_is_recognized(self):
        domains = {n.domain for n in self.graph.get_nodes_by_type("task")}
        self.assertIn("agents", domains)

    def test_software_engineering_agent_harness_sota_is_mini_not_cca_sao_rlm(self):
        ids = self._sota_ids("task:software-engineering-agent-harness")
        self.assertEqual(ids, ["method:mini-swe-agent"])
        self.assertNotIn("method:cca", ids)
        self.assertNotIn("method:sao", ids)
        self.assertNotIn("method:rlm", ids)
        paths = self.engine.sota("task:software-engineering-agent-harness")
        self.assertTrue(any(p["method"].id == "method:mini-swe-agent" for p in paths))
        self.assertFalse(any(p["method"].id in ("method:cca", "method:sao", "method:rlm") for p in paths))

    def test_build_an_agent_routes_to_swe_harness_not_sao(self):
        ranked = self.engine.route("build an agent")
        self.assertGreaterEqual(len(ranked), 1)
        self.assertEqual(ranked[0].node.id, "task:software-engineering-agent-harness")
        self.assertNotEqual(ranked[0].node.id, "task:agentic-async-rl")

    def test_long_context_prompt_offload_sota_is_rlm(self):
        self.assertEqual(self._sota_ids("task:long-context-prompt-offload"), ["method:rlm"])
        rlm = self.graph.get_node("method:rlm")
        self.assertEqual(rlm.status, "sota")
        self.assertEqual(rlm.metadata.get("category"), "agent-recursion")

    def test_long_horizon_tool_agent_sota_is_foldgrpo(self):
        self.assertEqual(self._sota_ids("task:long-horizon-tool-agent"), ["method:foldgrpo"])

    def test_agent_memory_sota_is_ace(self):
        self.assertEqual(self._sota_ids("task:agent-memory"), ["method:ace"])

    def test_agent_communication_sota_is_mcp(self):
        self.assertEqual(self._sota_ids("task:agent-communication"), ["method:mcp"])

    def test_computer_use_sota_is_claude_osworld2_not_aggregator(self):
        self.assertEqual(self._sota_ids("task:computer-use-agent"), ["method:claude-computer-use"])
        method = self.graph.get_node("method:claude-computer-use")
        blobs = []
        for claim in method.metadata.get("claims", []):
            blobs.append(str(claim.get("value") or ""))
            blobs.append(str(claim.get("notes") or ""))
        blob = " ".join(blobs)
        self.assertIn("20.6", blob)
        self.assertIn("70.6", blob)

    def test_multi_agent_default_is_single_agent_plus_tools(self):
        self.assertEqual(
            self._sota_ids("task:multi-agent-orchestration"),
            ["method:single-agent-plus-tools"],
        )

    def test_agents_methods_do_not_appear_on_training_sota(self):
        locked = (
            "task:math-code-rl-dense",
            "task:pretrain-dense-7b",
            "task:open-data-recipe",
            "task:industrial-model-building",
            "task:agentic-async-rl",
        )
        banned = (
            "method:rlm",
            "method:cca",
            "method:foldgrpo",
            "method:mini-swe-agent",
            "method:omp2-harness",
        )
        for task_id in locked:
            sota_ids = self._sota_ids(task_id)
            for method_id in banned:
                self.assertNotIn(method_id, sota_ids, f"{method_id} on {task_id}")

        magic = self.graph.get_node("task:training-data-attribution")
        if magic is not None:
            sota_ids = [e["method"] for e in magic.metadata.get("current_sota", [])]
            for method_id in banned:
                self.assertNotIn(method_id, sota_ids)

    def test_sao_remains_sota_for_agentic_async_rl(self):
        ids = self._sota_ids("task:agentic-async-rl")
        self.assertEqual(ids, ["method:sao"])
        sao = self.graph.get_node("method:sao")
        self.assertEqual(sao.status, "sota")
        self.assertIn("task:agentic-async-rl", sao.metadata.get("sota_for") or [])
        paths = self.engine.sota("task:agentic-async-rl")
        self.assertTrue(any(p["method"].id == "method:sao" for p in paths))

    def test_locked_training_sota_untouched(self):
        self.assertIn("method:cispo", self._sota_ids("task:math-code-rl-dense"))
        self.assertIn("method:muon2", self._sota_ids("task:pretrain-dense-7b"))
        self.assertIn("method:olmo-3", self._sota_ids("task:open-data-recipe"))
        self.assertIn("method:poolside-model-factory", self._sota_ids("task:industrial-model-building"))
        self.assertIn("method:bmssp", self._sota_ids("task:directed-sssp-nonneg"))
        self.assertIn("method:opsa", self._sota_ids("task:teacher-free-on-policy-self-adaptation"))
        automixer = self.graph.get_node("method:automixer")
        self.assertEqual(automixer.metadata.get("sota_for") or [], [])

    def test_agent_method_categories(self):
        self.assertEqual(self.graph.get_node("method:mini-swe-agent").get("category"), "agent-harness")
        self.assertEqual(self.graph.get_node("method:mcp").get("category"), "agent-protocol")
        self.assertEqual(self.graph.get_node("method:ace").get("category"), "agent-memory")
        self.assertEqual(self.graph.get_node("method:rlm").get("category"), "agent-recursion")
        self.assertEqual(self.graph.get_node("method:foldgrpo").get("category"), "agent-recursion")
        self.assertEqual(self.graph.get_node("method:omp2-harness").get("category"), "agent-harness")

    def test_agent_harness_runtime_sota_is_omp2_not_mini(self):
        ids = self._sota_ids("task:agent-harness-runtime")
        self.assertEqual(ids, ["method:omp2-harness"])
        omp2 = self.graph.get_node("method:omp2-harness")
        self.assertEqual(omp2.status, "sota")
        self.assertEqual(omp2.metadata.get("sota_for"), ["task:agent-harness-runtime"])
        self.assertEqual(omp2.metadata.get("supersedes") or [], [])
        paths = self.engine.sota("task:agent-harness-runtime")
        self.assertTrue(any(p["method"].id == "method:omp2-harness" for p in paths))
        self.assertFalse(any(p["method"].id == "method:mini-swe-agent" for p in paths))

    def test_omp2_does_not_appear_on_training_or_eval_sota(self):
        expected = {
            "task:software-engineering-agent-harness": "method:mini-swe-agent",
            "task:math-code-rl-dense": "method:cispo",
            "task:pretrain-dense-7b": "method:muon2",
            "task:agentic-async-rl": "method:sao",
            "task:training-data-attribution": "method:magic",
            "task:long-context-prompt-offload": "method:rlm",
            "task:agent-communication": "method:mcp",
        }
        for task_id, method_id in expected.items():
            sota_ids = self._sota_ids(task_id)
            self.assertIn(method_id, sota_ids, f"{task_id} lost {method_id}")
            self.assertNotIn("method:omp2-harness", sota_ids, f"omp2-harness on {task_id}")

    def test_harness_kernel_redirects_both_ways(self):
        swe = self.graph.get_node("task:software-engineering-agent-harness")
        runtime = self.graph.get_node("task:agent-harness-runtime")
        swe_tos = [r["to"] for r in swe.metadata.get("redirects") or []]
        runtime_tos = [r["to"] for r in runtime.metadata.get("redirects") or []]
        self.assertIn("task:agent-harness-runtime", swe_tos)
        self.assertIn("task:software-engineering-agent-harness", runtime_tos)
        ranked_loop = self.engine.route("build an agent")
        self.assertEqual(ranked_loop[0].node.id, "task:software-engineering-agent-harness")
        ranked_engine = self.engine.route("building a production engine rewind sandbox remote TUI")
        self.assertEqual(ranked_engine[0].node.id, "task:agent-harness-runtime")


if __name__ == "__main__":
    unittest.main()
