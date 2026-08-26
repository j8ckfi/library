# AGENTS.md: Autonomous Agent Operating Guide for `j8ckfi/library`

This document provides exact instructions for autonomous training and research agents interacting with `j8ckfi/library`.

---

## 1. What This Library Is

`j8ckfi/library` is a machine-readable and human-navigable knowledge graph of current (2025–2026) state-of-the-art machine learning training methods, papers, and code recipes.

When you are asked to **"train model X to do Y"**, **do not rely on outdated pre-training knowledge**. Query this library to determine:
1. What the current date-stamped SOTA method is.
2. What empirical claims, benchmarks, and baselines substantiate it.
3. What primary paper authored the technique.
4. What exact runnable PyTorch/JAX recipe and dependencies execute it.

---

## 2. Fast Navigation Paths (Hops)

The graph connects concepts across 4 node types:
- **`task:<slug>`** (Problem / Benchmark)
- **`method:<slug>`** (Algorithm / Architecture / Optimizer)
- **`paper:<slug>`** (Literature / arXiv reference)
- **`recipe:<slug>`** (Executable PyTorch/JAX implementation)

Canonical query paths:
```
[User Request] "Train an LLM with RL reasoning"
   │
   ▼
1. Query Task: task:rl-reasoning-alignment
   │
   ▼
2. Resolve SOTA Method: method:grpo (Group Relative Policy Optimization)
   │
   ├──► 3. Inspect Literature: paper:deepseek-math / paper:deepseek-r1
   │
   └──► 4. Load Runnable Code: recipe:grpo-trl-training
```

---

## 3. Querying the Library via CLI

The library provides a zero-dependency CLI (`python -m library`):

### 3.1 Resolving SOTA for a Task or Domain
```bash
# Look up canonical SOTA method, claims, paper, and recipe for pretraining
python -m library sota "llm pretraining"

# Direct task ID lookup
python -m library sota "task:reasoning-rl-alignment"

# Structured JSON output for agent tools
python -m library sota "task:low-rank-adaptation" --json
```

### 3.2 Searching the Graph
```bash
# Keyword query across all nodes
python -m library query "matrix optimizer muon"

# Filter by node type or domain
python -m library query "quantization" --type method
python -m library query "snn" --domain snn

# Filter only active SOTA nodes
python -m library query "compression" --sota-only --json
```

### 3.3 Reading Node Content & Walking Neighbors
```bash
# Display node markdown body and metadata
python -m library show "method:muon-optimizer"

# Inspect connected edges (papers, tasks, recipes)
python -m library walk "method:muon-optimizer"

# Find path between any two graph nodes
python -m library path --from "task:llm-pretraining" --to "recipe:muon-pretraining"
```

---

## 4. Graph Navigation via Filesystem (Grep & Read)

If invoking Python is unavailable, agents can traverse directly on the filesystem:
- Tasks: `graph/tasks/*.md`
- Methods: `graph/methods/*.md`
- Papers: `graph/papers/*.md`
- Recipes: `graph/recipes/*.md`

### Standard Frontmatter Reference Traversal:
- Read `graph/tasks/<task>.md` → find `current_sota.method: method:<slug>`
- Read `graph/methods/<slug>.md` → check `status: sota`, find `papers` and `recipes`
- Read `graph/recipes/<recipe-slug>.md` → inspect `pip_dependencies` and runnable code block.

---

## 5. What "SOTA" Means in This Library

In this library, **SOTA is not a vibe or marketing label**. A method is labeled `status: sota` only when:
1. **Date-stamped**: An explicit `as_of: "YYYY-MM"` or claim date exists.
2. **Benchmark-grounded**: Measured against specific competitive baselines on established benchmarks (e.g. MMLU-Pro, MATH-500, perplexity on FineWeb-Edu, throughput per GPU).
3. **Verifiable**: Contains link to verified literature and reproducible recipes.

---

## 6. How an Agent Must Ingest a New Paper (5 Minutes)

When given a new paper or instructed to add a technique:

1. **Scaffold the templates**:
   ```bash
   python -m library new paper <paper-slug> --title "Paper Title"
   python -m library new method <method-slug> --title "Method Name"
   python -m library new recipe <recipe-slug> --title "Recipe Title"
   ```

2. **Populate metadata**:
   - `paper:<paper-slug>`: arXiv ID, authors, publication date, abstract summary, contributions.
   - `method:<method-slug>`: status, sota_for, supersedes, claims with metric & date, mathematical overview, gotchas.
   - `recipe:<recipe-slug>`: hardware, framework, pip dependencies, runnable code snippet.

3. **Handle Supersession**:
   - If the new method supersedes an older method `method:old-method`, edit `graph/methods/old-method.md`:
     - Change `status: superseded`
     - Add `superseded_by: method:<new-slug>`
   - Update the parent task in `graph/tasks/<task-slug>.md`: update `current_sota`.

4. **Validate**:
   ```bash
   python -m library validate
   ```
   Every PR must pass validation with 0 errors.
