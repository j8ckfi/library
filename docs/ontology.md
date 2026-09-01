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
domain: "<pretraining|post-training|efficiency|compression|snn|interpretability|video|control|scientific-ml|systems|algorithms|agents>"
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
category: "<optimizer|architecture|rl-alignment|quantization|peft|spiking|circuits|codec|servo-control|neural-operator|training-systems|graph-algorithms|data-attribution|agent-harness|agent-protocol|agent-memory|agent-recursion>"
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

`category: data-attribution` is leave-one-out / influence / MAGIC-style scoring of training tokens or sequences for a query behavior. Diagnostic tooling, not a train kernel, mix-ratio search, or SAE dictionary. Do not reuse `data-curriculum` or `training-systems` for this shelf.

`category: agent-harness`, `agent-protocol`, `agent-memory`, and `agent-recursion` are the Agents shelf. They are not `rl-alignment` (SAO trains a policy) and not `training-systems`.

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

### 4.1.1 Ergonomic Schema Extensions (v1.1 — backward-compatible, optional)

These fields implement the routing, evidence, and decay contracts defined in
[system-design.md](system-design.md). All are **optional** and add no new required fields, so existing
nodes remain valid. They exist to move the highest-value knowledge (routing guards, scope boundaries,
evidence quality, review freshness) out of prose and into machine-queryable structure.

**Task node extensions:**
```yaml
scope: "<one sentence: what problems this task node owns>"
out_of_scope:
  - "<near-miss problem that looks like this task but is not>"
redirects:
  - when: "<condition, e.g. 'budget is ~2B on consumer GPUs'>"
    to: "task:<other-task-slug>"
last_reviewed: "YYYY-MM-DD"   # last time a agent re-verified current_sota against literature
```

**Method node extensions:**
```yaml
do_not_use_for:
  - when: "<condition>"
    reason: "<why this method is the wrong pick here>"
    use_instead: "method:<better-method-slug> | task:<redirect-slug>"
assumptions:
  - "<precondition on hardware scale, data regime, or model family>"
last_reviewed: "YYYY-MM-DD"
```

**Claim extensions (inside `claims:` items):**
```yaml
evidence_level: "peer-reviewed"   # peer-reviewed | preprint | self-reported | unofficial-repro
source_url: "https://..."          # where the number actually lives
```

**Semantics:**
- `redirects` are routing guards: an agent whose user request matches `when` must go to `to` instead of
  treating this task as resolved. `out_of_scope` is the prose complement for fuzzy matching.
- `do_not_use_for` is load-bearing negative knowledge ("NOT DoRA", "not this scale") and must be rendered
  by decision-shaped outputs (`sota`/`decide`) alongside the positive recommendation.
- `last_reviewed` + `current_sota[].as_of` power the staleness budget (§4.3).
- `evidence_level`/`source_url` upgrade the verified bit into a trust gradient (§4.4).

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
   - Update `task.last_reviewed` to today.
5. Append a receipt to `graph/CHANGELOG.md` (see [ingestion-guide.md](ingestion-guide.md) §5).
6. Run `python -m library validate` to confirm reference integrity, absence of cycles, and the §4.5
   supersession post-conditions. Steps 2–4 form **one transaction**: a supersession that updates the new
   method but not the old method or the parent task is an incomplete write and must not be committed.

### 4.3 Staleness Budget

A recommendation's truth decays. Mechanical rule:

- A task whose `current_sota[].as_of` is older than **4 months** (relative to today's date) is **stale**.
  Its recommendation must be re-verified against current literature before an agent acts on it.
- `task.last_reviewed` records when a routing/SOTA re-check last happened; `method.last_reviewed` when the
  method's claims were last re-checked. Both default to the claim date when absent.
- The command `library stale --max-age-days N` (see [system-design.md §8](system-design.md)) turns
  this into a prioritized maintenance queue and a CI-able exit code.

### 4.4 Evidence Trust Gradient

`verified: true/false` is the floor, not the ceiling. When `evidence_level` is present, weight decisions as:
`peer-reviewed` > `preprint` > `unofficial-repro` > `self-reported`. A `status: sota` method must carry at
least one claim with `verified: true` and an explicit comparator baseline. Self-reported-only claims must
set `verified: false` and say so in decision output — never silently.

### 4.5 Validator Rule Targets (post-conditions, not prose suggestions)

The following checks are enforced by `library/validator.py` (`python -m library validate`).
Warnings do not fail the graph (exit 0); errors do (exit 1).

| Level | Rule |
| :--- | :--- |
| ERROR | A `status: superseded` method appears in any task's `current_sota` |
| ERROR | `superseded_by` set without a matching `supersedes` edge on the new method (one-way supersession) |
| ERROR | `redirects[].to` and `do_not_use_for[].use_instead` references must resolve to existing nodes |
| ERROR | `evidence_level` must be one of the four enumerated values |
| WARNING | Any task's `current_sota[].as_of` older than the 4-month staleness budget |
| WARNING | `graph/INDEX.md` or the AGENTS.md cheat-sheet block out of sync with graph state (`python -m library index`) |
