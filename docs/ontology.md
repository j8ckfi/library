# Knowledge Graph Ontology and Schema Specification

## 1. Core Principles

The `j8ckfi/library` graph organizes machine learning research so both autonomous training agents and human engineers can identify state-of-the-art methods, understand their mathematical mechanisms, trace primary literature, and retrieve runnable code recipes.

### Graph Architecture
The graph contains four primary node types connected by typed directed edges:

```
+----------------+      has_sota_method       +-----------------+
|   Task Node    | -------------------------> |   Method Node   |
| (task:<slug>)  | <------------------------- | (method:<slug>) |
+----------------+         sota_for           +-----------------+
        ^                                        |          ^
        |                                        |          |
 recipe_for_task                      described_in          | implements
        |                                        |          |
        |                                        v          |
+----------------+                       +-----------------+ |
|  Recipe Node   | --------------------> |   Paper Node    | |
| (recipe:<slug>)|     implements        |  (paper:<slug>) | |
+----------------+                       +-----------------+ |
        |                                                    |
        +----------------------------------------------------+
```

---

## 2. Node Types & Required Schemas

Every node is stored as a Markdown document with YAML frontmatter located in `graph/<type>s/<slug>.md`.

### 2.1 Task Node (`task:<slug>`)
Represents an ML objective, optimization problem, or capability benchmark.
- Location: `graph/tasks/<slug>.md`
- Schema:
```yaml
---
id: task:<slug>
type: task
title: "<Human Readable Title>"
domain: "<pretraining|post-training|efficiency|compression|snn|interpretability|video|control|scientific-ml|systems|algorithms>"
summary: "<1-2 sentence problem description>"
current_sota:
  - method: method:<method-slug>
    as_of: "YYYY-MM"
    benchmark: "<Benchmark Name>"
    metric: "<Metric Name (e.g. loss, accuracy, pass@1)>"
    value: <numeric or string value>
    notes: "<Context, compute budget, or evaluation split>"
methods:
  - method:<method-slug>
tags:
  - <tag-1>
  - <tag-2>
---
```

### 2.2 Method Node (`method:<slug>`)
Represents an algorithm, architecture, loss function, or training technique.
- Location: `graph/methods/<slug>.md`
- Schema:
```yaml
---
id: method:<slug>
type: method
title: "<Method Name>"
category: "<optimizer|architecture|rl-alignment|quantization|peft|spiking|circuits|codec|servo-control|neural-operator|training-systems|graph-algorithms>"
status: "<sota|active|superseded|niche|experimental>"
sota_for:
  - task:<task-slug>
supersedes:
  - method:<older-method-slug>
superseded_by: method:<newer-method-slug> # Optional, when status is 'superseded'
papers:
  - paper:<paper-slug>
recipes:
  - recipe:<recipe-slug>
claims:
  - benchmark: "<Benchmark Name>"
    metric: "<Metric>"
    value: <Value>
    baseline: "<Baseline method and score>"
    date: "YYYY-MM"
    verified: true # false if self-reported only or unverified
    notes: "<Conditions and constraints>"
tags:
  - <tag-1>
---
```

### 2.3 Paper Node (`paper:<slug>`)
Represents published or preprint literature describing the technique.
- Location: `graph/papers/<slug>.md`
- Schema:
```yaml
---
id: paper:<slug>
type: paper
title: "<Full Paper Title>"
authors:
  - "<Author 1>"
  - "<Author 2>"
year: 2026
month: 1
arxiv_id: "2601.12345"
url: "https://arxiv.org/abs/2601.12345"
methods:
  - method:<method-slug>
cites:
  - paper:<cited-paper-slug>
tags:
  - <tag-1>
---
```

### 2.4 Recipe Node (`recipe:<slug>`)
Represents executable, dependency-specified PyTorch/JAX implementation code.
- Location: `graph/recipes/<slug>.md`
- Schema:
```yaml
---
id: recipe:<slug>
type: recipe
title: "<Recipe Title>"
method: method:<method-slug>
task: task:<task-slug>
target_hardware: "<Hardware requirement, e.g. 1x H100 80GB, 1x RTX 4090>"
framework: "<e.g. PyTorch 2.5+, vLLM, HuggingFace TRL>"
repo_url: "<Canonical GitHub repository URL>"
pip_dependencies:
  - "<package>=<version>"
tags:
  - <tag-1>
---
```

---

## 3. Standard Relations & Edge Semantics

| Relation | Source Type | Target Type | Semantics |
| :--- | :--- | :--- | :--- |
| `has_sota_method` | Task | Method | The method is the date-stamped state-of-the-art for this task |
| `sota_for` | Method | Task | Inverse of `has_sota_method` |
| `addresses_task_method` | Task | Method | Method is a known technique addressing this task |
| `targets_task` | Method | Task | Inverse of `addresses_task_method` |
| `supersedes` | Method | Method | Source method beats or replaces target method on benchmarks |
| `superseded_by` | Method | Method | Target method beats or replaces source method |
| `described_in` | Method | Paper | The method is formulated in this paper |
| `introduces` | Paper | Method | Paper introduced or formulated this method |
| `implemented_by` | Method | Recipe | Code recipe providing runnable execution |
| `implements` | Recipe | Method | Recipe implements this method |
| `recipe_for_task` | Recipe | Task | Recipe demonstrates end-to-end task execution |
| `cites` | Paper | Paper | Paper references foundational work |

---

## 4. SOTA Definition & Supersession Protocol

### 4.1 SOTA Evidence Standard
A method is designated `status: sota` if and only if:
1. It holds verifiable, date-stamped Pareto-optimal performance (loss, throughput, accuracy, sample efficiency) on standard benchmarks against explicit baselines.
2. The claim contains a date (`YYYY-MM`), baseline comparator, metric, and verification status.

### 4.2 Supersession Workflow
When a new paper/method establishes superior Pareto performance over an existing method:
1. Create new `paper:<new-slug>`, `method:<new-slug>`, and `recipe:<new-slug>`.
2. In `method:<new-slug>` frontmatter:
   - Add `supersedes: [method:<old-slug>]`.
   - Add `sota_for: [task:<task-slug>]`.
   - Set `status: sota`.
3. In `method:<old-slug>` frontmatter:
   - Update `status: superseded` (or `niche` if it remains optimal in constrained niches).
   - Add `superseded_by: method:<new-slug>`.
4. In `task:<task-slug>` frontmatter:
   - Update `current_sota` list with the new method, metric values, and current `as_of: "YYYY-MM"`.
5. Run `python -m library validate` to confirm reference integrity and absence of cycles.
