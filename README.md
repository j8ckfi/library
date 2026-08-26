# j8ckfi/library

> Sprawling, agent-navigable knowledge graph of cutting-edge machine learning research, SOTA methods, primary literature, and executable training recipes (2025–2026).

---

## 1. Overview

`j8ckfi/library` is designed for autonomous training agents and ML engineers. When tasked with *"train model X to do Y"*, agents can query this graph to identify current, date-stamped SOTA methods, read empirical validation claims, trace arXiv papers, and pull runnable PyTorch/JAX recipes in a few hops.

```
+---------------+        has_sota_method       +-----------------+
|     Task      | ───────────────────────────> │     Method      |
| (task:<slug>) │ <─────────────────────────── │ (method:<slug>) │
+---------------+           sota_for           +-----------------+
        │                                               │
        │ recipe_for_task                 described_in  │ implements
        ▼                                               ▼
+---------------+                              +-----------------+
|    Recipe     | ───────────────────────────> │      Paper      |
|(recipe:<slug>)|          implements          | (paper:<slug>)  |
+---------------+                              +-----------------+
```

---

## 2. Fast Navigation for Training Agents

### CLI Quickstart
```bash
# 1. Look up SOTA method, paper, and runnable code recipe for a task
python -m library sota "llm pretraining"

# 2. Search for methods across domains
python -m library query "matrix optimizer" --type method

# 3. Inspect a node's full details and code
python -m library show "method:muon-optimizer"

# 4. View connected edges
python -m library walk "method:grpo"

# 5. Check graph integrity
python -m library validate
```

For agent integration instructions and autonomous workflow steps, see [AGENTS.md](AGENTS.md).

---

## 3. Seeded Method Families (2025–2026 SOTA)

| Domain | Task | SOTA Method | Key Paper / Reference | Recipe |
| :--- | :--- | :--- | :--- | :--- |
| **Pretraining** | LLM Matrix Optimization | **Muon Optimizer** | Jordan et al. (2024–2025) `arXiv:2502.16738` | `recipe:muon-pretraining` |
| **Pretraining** | Linear Attention Architecture | **Mamba-2 (SSD)** | Dao & Gu (2024–2025) `arXiv:2405.21060` | `recipe:mamba2-training` |
| **Post-Training** | Reasoning RL Alignment | **GRPO** | DeepSeek-AI (2024–2025) `arXiv:2402.03300` | `recipe:grpo-trl-training` |
| **Post-Training** | Direct Preference Alignment | **SimPO** | Meng et al. (2024–2025) `arXiv:2405.14734` | `recipe:simpo-alignment` |
| **Efficient Training** | Low-Rank Adaptation | **DoRA** | Liu et al. (2024–2025) `arXiv:2402.09353` | `recipe:dora-finetuning` |
| **Efficient Training** | Quantized 4-bit PEFT | **QLoRA** | Dettmers et al. (2023–2025) `arXiv:2305.14314` | `recipe:qlora-peft` |
| **Extreme Compression**| 1-bit Ternary Pretraining | **BitNet b1.58** | Wang et al. (2024–2025) `arXiv:2402.17764` | `recipe:bitnet-b158` |
| **SNNs** | Direct Spiking Training | **Surrogate Gradient SNN** | Fang et al. (SpikingJelly / IEEE TPAMI) | `recipe:spikingjelly-snn` |
| **Interpretability** | Sparse Feature Dictionary | **Gated SAEs** | Rajamanoharan et al. (2024–2025) `arXiv:2404.16014` | `recipe:gated-sae-training` |
| **Video Compression** | Neural Video Codec | **DCVC-DC** | Li et al. (IEEE TPAMI / CVPR) `arXiv:2403.11180` | `recipe:dcvc-video-codec` |
| **Control / Servos** | Visual Robot Motor Control | **Diffusion Policy** | Chi et al. (2023–2025) `arXiv:2303.04137` | `recipe:diffusion-policy-servo` |

---

## 4. Repository Structure

```
├── AGENTS.md               # Operating instructions and protocol for AI agents
├── README.md               # One-screen library reference and quickstart
├── pyproject.toml          # Package definition and dependencies
├── schema/
│   └── schema.json         # JSON Schema for task, method, paper, and recipe nodes
├── docs/
│   ├── ontology.md         # Schema rules, edge semantics, and supersession protocol
│   └── ingestion-guide.md  # 5-minute guide for adding new papers and methods
├── templates/              # Markdown templates for new nodes
│   ├── task.md
│   ├── method.md
│   ├── paper.md
│   └── recipe.md
├── library/                # Core Python package (zero heavy dependencies)
│   ├── __init__.py
│   ├── __main__.py
│   ├── graph.py            # Node, Edge, and KnowledgeGraph in-memory index
│   ├── loader.py           # Markdown frontmatter parser and edge compiler
│   ├── validator.py        # Schema validation, ref checking, cycle detection
│   ├── query.py            # Search and SOTA ranking query engine
│   ├── traverse.py         # Neighborhood inspection and pathfinding
│   ├── exporter.py         # JSON and JSONL graph exporter
│   ├── ingest.py           # Node scaffolding helper
│   └── cli.py              # `python -m library` CLI
└── graph/                  # Sprawling knowledge graph
    ├── tasks/              # Problem statements and SOTA resolutions
    ├── methods/            # Algorithms, architectures, and optimizers
    ├── papers/             # Literature summaries and arXiv citations
    └── recipes/            # Runnable PyTorch/JAX code recipes
```

---

## 5. Adding New Papers

To ingest a new paper in 5 minutes:
```bash
python -m library new paper <paper-slug> --title "Paper Title"
python -m library new method <method-slug> --title "Method Name"
python -m library new recipe <recipe-slug> --title "Recipe Title"
```
Populate YAML frontmatter and markdown sections according to [docs/ingestion-guide.md](docs/ingestion-guide.md), then validate with `python -m library validate`.
