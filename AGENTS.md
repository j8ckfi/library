# AGENTS.md: Autonomous Agent Operating Guide for `j8ckfi/library`

This document provides exact instructions for autonomous training and research agents interacting with `j8ckfi/library`.

---

## 1. What This Library Is

`j8ckfi/library` is a machine-readable and human-navigable knowledge graph of current (2025–2026) state-of-the-art machine learning training methods, papers, and code recipes.

When using this library to choose a training method, resolve the relevant task and inspect its evidence to determine:
1. What the current date-stamped SOTA method is.
2. What empirical claims, benchmarks, and baselines substantiate it.
3. What primary paper authored the technique.
4. What exact runnable PyTorch/JAX recipe and dependencies execute it.

---

## 2. Agent Routing Cheat-Sheet (First-Hop SOTA Index)

Use this quick-routing table as of **2026-09-02**:

<!-- CHEAT-SHEET:START -->
```
task:agent-communication -> method:mcp (2602.11988, 2026-07)
  when building the SWE loop rather than the tool protocol -> task:software-engineering-agent-harness
  when wanting a multi-agent crew as the communication layer -> task:multi-agent-orchestration
task:agent-harness-runtime -> method:omp2-harness (2026-09-02)
  when issue-to-patch / locked eval -> task:software-engineering-agent-harness
  when train agent RL -> task:agentic-async-rl
  when outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit) -> task:outcome-only-long-horizon-agent-rl
  when dumped long prompt -> task:long-context-prompt-offload
  when how to talk to tools/agents as a protocol -> task:agent-communication
task:agent-memory -> method:ace (2510.04618, 2025-10)
  when dumped corpus ≫ window -> task:long-context-prompt-offload
  when SWE issue-to-patch without a playbook -> task:software-engineering-agent-harness
task:computer-use-agent -> method:claude-computer-use (2606.29537, 2026-06)
  when GitHub issue to patch -> task:software-engineering-agent-harness
task:long-context-prompt-offload -> method:rlm (2512.24601, 2025-12)
  when GitHub issue to patch without a dumped corpus -> task:software-engineering-agent-harness
  when long tool/web/SWE trajectory with folding -> task:long-horizon-tool-agent
task:long-horizon-tool-agent -> method:foldgrpo (2510.11967, 2025-10)
  when dumped corpus much larger than the window -> task:long-context-prompt-offload
  when SWE harness without folding -> task:software-engineering-agent-harness
  when outcome-only long-horizon agent RL (signal starvation / drift or outcome-blind rubrics) -> task:outcome-only-long-horizon-agent-rl
task:multi-agent-orchestration -> method:single-agent-plus-tools (2606.04455, 2026-06)
  when GitHub issue to patch -> task:software-engineering-agent-harness
  when train asynchronous RL for a tool-use policy -> task:agentic-async-rl
task:software-engineering-agent-harness -> method:mini-swe-agent (2405.15793, 2026-09)
  when train asynchronous RL for a tool-use policy -> task:agentic-async-rl
  when math-code RLVR with verifiable rewards -> task:math-code-rl-dense
  when GUI / OS desktop computer-use -> task:computer-use-agent
  when 10M-token dumped corpus that does not fit the window -> task:long-context-prompt-offload
  when building a production engine (rewind, sandbox, remote, TUI) -> task:agent-harness-runtime
  when train outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit) -> task:outcome-only-long-horizon-agent-rl
task:directed-sssp-nonneg -> method:bmssp (2504.17033, 2026-08)
task:1bit-extreme-quantization -> method:sparse-bitnet (2603.05168, 2026-08-26)
task:fp4-hardware-training -> method:quartet-ii (2601.22813, 2026-08-26) + method:mxfp4-mi355x (2605.09825, 2026-08-26)
task:post-training-ternary-quantization -> method:scaleq-158 (2608.01078, 2026-08-26)
task:continuous-control-world-model -> method:efficienttdmpc (2605.16692, 2026-08-26) + method:dream-mpc (2605.04568, 2026-08-26)
task:visuomotor-servo-control -> method:td-mpc2 (2310.16828, 2026-08-26)
task:posttrain-diffusion -> method:diffusion-opsd (2608.24646, 2026-08-27) + method:self-opd (2608.26872, 2026-08-28)
task:4bit-peft-quantization -> method:aqlora-q (2608.23816, 2026-08-26) + method:autoqra (2602.22268, 2026-08-26)
task:full-lowbit-finetune -> method:gradcodes (2608.30908, 2026-09-01)
  when memory must fit a 4-bit stack but a mixed-precision adapter at inference is acceptable -> task:4bit-peft-quantization
  when native FP4 forward/backward hardware training from scratch -> task:fp4-hardware-training
  when quality LoRA on 24GB without a fully quantized checkpoint constraint -> task:lora-quality-tuning
task:full-param-memory-efficient-pretrain -> method:scale (2506.16659, 2026-08-26)
task:lora-quality-tuning -> method:lr-matters-lora (2602.04998, 2026-08-26)
task:parameter-efficient-fine-tuning -> method:lr-matters-lora (2602.04998, 2026-08-26) + method:aqlora-q (2608.23816, 2026-08-26)
task:mechanistic-interpretability-dictionaries -> method:sasa (2606.06333, 2026-08-26) + method:circuitsteer (2608.05732, 2026-08-26) + method:fega (2607.24645, 2026-08-26)
task:sae-circuits -> method:circuitsteer (2608.05732, 2026-08-26)
task:sae-effect-geometry -> method:fega (2607.24645, 2026-08-26)
task:training-data-attribution -> method:magic (2504.16430, 2026-09-01)
  when mix-ratio search or replacing an open pretrain mix -> task:open-data-recipe
  when SAE dictionaries, circuits, or effect geometry -> task:mechanistic-interpretability-dictionaries
  when factory process / experiments-as-code / lineage -> task:industrial-model-building
task:agentic-async-rl -> method:sao (2607.07508, 2026-08-26)
  when build an agent rather than train a policy -> task:software-engineering-agent-harness
  when outcome-only long-horizon agent RL (coverage / anti-drift), not async stragglers -> task:outcome-only-long-horizon-agent-rl
task:all-zero-verifier-groups -> method:verigate (2605.30451, 2026-08-26)
task:data-free-self-evolution -> method:j-zero (2608.26582, 2026-08-31)
task:direct-preference-alignment -> method:olmo-3 (2512.13961, 2026-08-26)
task:distill-reasoner-verifier -> method:opdvr (2608.24696, 2026-08-27)
task:instruct-sft-alignment -> method:olmo-3 (2512.13961, 2026-08-26) + method:nemotron-cascade-2 (2603.19220, 2026-08-26)
task:label-free-reasoner-posttrain -> method:u-opsd (2608.06296, 2026-08-28)
task:label-free-test-time-reasoner -> method:ttpo (2608.27448, 2026-08-28)
task:math-code-rl-dense -> method:cispo (2506.13585, 2026-08-26)
  when outcome-only long-horizon interactive agent RL -> task:outcome-only-long-horizon-agent-rl
  when train asynchronous RL for a tool-use policy -> task:agentic-async-rl
task:math-code-rl-moe -> method:sapo (2511.20347, 2026-08-26)
task:outcome-only-long-horizon-agent-rl -> method:canopy (2609.01245, 2026-09-04)
  when variable environment latency / async stragglers, not sparse-outcome coverage -> task:agentic-async-rl
  when the problem is context folding of a long tool trajectory, not the RL signal -> task:long-horizon-tool-agent
  when single-turn math/code Pass@1 RLVR -> task:math-code-rl-dense
  when build an agent loop rather than train a policy -> task:software-engineering-agent-harness
  when production engine (rewind, sandbox, remote, TUI) -> task:agent-harness-runtime
task:passk-reasoning-coverage -> method:es-reasoning (2608.27351, 2026-08-31)
task:privileged-teacher-opsd -> method:vista (2608.28306, 2026-08-31)
task:reasoning-rl-alignment -> method:cispo (2506.13585, 2026-08-26) + method:sapo (2511.20347, 2026-08-26)
task:student-distillation -> method:opd (2604.13016, 2026-08-26) + method:open-mopd (2608.19098, 2026-08-28)
task:teacher-free-on-policy-self-adaptation -> method:opsa (2608.31046, 2026-09-01)
  when verifiable labels exist and the goal is Pass@1 RLVR -> task:math-code-rl-dense
  when a strong teacher is available and the goal is intentional distillation -> task:student-distillation
  when unlabeled existing math problems with majority-vote pseudo-solutions -> task:label-free-reasoner-posttrain
  when test-time adaptation on unlabeled queries -> task:label-free-test-time-reasoner
  when zero external problems, including unverifiable domains -> task:data-free-self-evolution
  when flow matching or continuous diffusion post-training -> task:posttrain-diffusion
task:token-level-critic-rl -> method:bpco (2608.23566, 2026-08-27)
task:budget-consumer-pretrain -> method:puro-2b (2608.27370, 2026-08-31)
task:linear-time-sequence-modeling -> method:mamba-2 (2405.21060, 2024-05)
task:llm-pretraining-optimization -> method:muon2 (2604.09967, 2026-08-26)
task:open-data-recipe -> method:olmo-3 (2512.13961, 2026-08-26)
task:pretrain-dense-7b -> method:muon2 (2604.09967, 2026-08-26)
task:pretrain-moe-frontier -> method:deepseek-v4 (2606.19348, 2026-08-26) + method:kimi-k3 (2607.24653, 2026-08-26)
task:operator-foundation -> method:poseidon (2405.19101, 2026-08-28) + method:unisolver (2405.17527, 2026-08-28)
task:operator-fourier-adapt -> method:f-adapter (2509.23173, 2026-08-28)
task:operator-grid-pde -> method:cvit (2405.13998, 2026-08-28) + method:poseidon (2405.19101, 2026-08-28)
task:operator-industrial-mesh -> method:transolver-3 (2602.04940, 2026-08-28)
task:operator-physics-informed -> method:pi-cvit (2606.06164, 2026-08-28)
task:operator-weather -> method:fourcastnet-3 (2507.12144, 2026-08-28)
task:snn-sequence-modeling -> method:longspike (2606.12895, 2026-08-26)
task:spiking-neural-networks-training -> method:longspike (2606.12895, 2026-08-26) + method:a2sg (2606.11236, 2026-08-26)
task:industrial-model-building -> method:poolside-model-factory (2605.27605, 2026-08)
task:train-moe-nvl72 -> method:mixture-of-kittens (2026-08-26)
task:learned-video-compression -> method:dcvc-uf (2606.04410, 2026-08-26) + method:mlvc (2606.28027, 2026-08-26)
task:neural-video-deploy -> method:mlvc (2606.28027, 2026-08-26)
task:neural-video-gpu -> method:dcvc-uf (2606.04410, 2026-08-26)
task:rl-video-mllm -> method:orarl (2608.20492, 2026-08-27)
```
<!-- CHEAT-SHEET:END -->

---

## 3. Method selection

Resolve the requested task against the current graph with `python -m library sota` or `decide`. Inspect the chosen method's scope, evidence, date, hardware requirements, paper, and recipe before applying it. A dated routing snapshot is a starting point, not a requirement to replace an explicitly requested model or algorithm.

## 4. Supersession and lineage

Read supersession from the canonical method and task nodes. Keep old-method, new-method, and parent-task records consistent when updating a recommendation; follow the ingestion contract below. Avoid maintaining a second handwritten catalog of these relationships here.

## 5. Fast Navigation Paths (Hops)

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
1. Query Task: task:math-code-rl-dense
   │
   ▼
2. Resolve SOTA Method: method:cispo (Clipped IS-weight Policy Optimization)
   │
   ├──► 3. Inspect Literature: paper:minimax-m1 / paper:scalerl
   │
   └──► 4. Load Runnable Code: recipe:cispo
```

---

## 6. Querying the Library via CLI

The library provides a zero-dependency CLI (`python -m library`). Prefer `sota` / `decide` over `query`. JSON is first-class (`--json`); `--brief` is the ~10-line tier. `graph/INDEX.md` and the §2 cheat-sheet are L3 derived views — regenerate with `index`, never hand-edit them.

### 6.1 Resolving SOTA for a Task or Domain
```bash
# Look up canonical SOTA method, claims, paper, and recipe for pretraining
python -m library sota "pretrain dense 7B"

# Direct task ID lookup (decision-shaped default)
python -m library sota "task:math-code-rl-dense"

# Brief (~10 lines) and structured JSON
python -m library sota "task:math-code-rl-dense" --brief
python -m library sota "task:parameter-efficient-fine-tuning" --json

# Six-question decision: use / instead / do-not-use / gotchas / code / trust
python -m library decide "task:math-code-rl-dense"
python -m library decide "task:math-code-rl-dense" --json
```

### 6.2 Searching the Graph
```bash
# Keyword query across all nodes
python -m library query "muon2"

# Filter by node type or domain
python -m library query "quantization" --type method
python -m library query "longspike" --domain snn

# Filter only active SOTA nodes
python -m library query "distillation" --sota-only --json
```

### 6.3 Reading Node Content & Walking Neighbors
```bash
# Display node markdown body and metadata
python -m library show "method:cispo"

# Inspect connected edges (papers, tasks, recipes, supersedes)
python -m library walk "method:muon2"

# Find path between any two graph nodes
python -m library path --from "task:pretrain-dense-7b" --to "recipe:muon2-pretraining"
```

### 6.4 Routing, freshness, index, and supersession
```bash
# Rank candidate tasks (scope / out_of_scope / redirects). Never empty without near-misses.
python -m library route "pretrain dense 7B"
python -m library route "pretrain dense 7B" --json

# Freshness queue. Default budget 120 days. Exit 1 if any task current_sota is over budget.
python -m library stale
python -m library stale --max-age-days 120 --json

# Regenerate graph/INDEX.md and this file's §2 cheat-sheet from graph state
python -m library index
python -m library index --json

# Validate: exit 1 only for schema/integrity errors. INDEX.md / cheat-sheet drift is a WARNING (exit 0).
python -m library validate

# Transactional supersession (refuses unless post-conditions hold). --dry-run writes nothing.
python -m library supersede method:new method:old --task task:example --dry-run
```

---

## 7. What "SOTA" Means in This Library

In this library, **SOTA is not a vibe or marketing label**. A method is labeled `status: sota` only when:
1. **Date-stamped**: An explicit `as_of: "YYYY-MM-DD"` or claim date exists.
2. **Benchmark-grounded**: Measured against specific competitive baselines on established benchmarks.
3. **Verifiable**: Contains link to verified literature and reproducible recipes.

---

## 8. Ingesting a Paper (5-Minute Recipe)

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
     - Change `status: superseded` (or `active`)
     - Add `superseded_by: method:<new-slug>`
   - Update the parent task in `graph/tasks/<task-slug>.md`: update `current_sota`.

4. **Validate**:
   ```bash
   python -m library validate
   ```
   Every PR must pass validation with 0 errors.

5. **Write the receipt**: append a one-paragraph audit entry to `graph/CHANGELOG.md` (format in
   [docs/ingestion-guide.md](docs/ingestion-guide.md) §5). A supersession that updates the new method but
   not the old method and its parent task is an **incomplete write** — do not commit it.

---

## 9. Agent Decision Protocol

This section is the operating protocol for any agent driving this library. The full system design — the
abstraction tower, the contracts behind these rules, and the CLI ergonomics roadmap — is in
[docs/system-design.md](docs/system-design.md). Schema extensions (routing guards, evidence levels,
staleness) are in [docs/ontology.md](docs/ontology.md) §4.1.1.

### 9.1 Decision loop

```
1. ROUTE    user request -> task:<slug>. Try the cheat-sheet (§2) first; if no hit or the request
            plausibly sits near a task boundary, check that task's `scope`, `out_of_scope`, and
            `redirects` before resolving. Follow `redirects` mechanically — they encode hard-won
            negative knowledge ("not this scale", "NOT DoRA"). First hop for "build an agent" is
            task:software-engineering-agent-harness / mini-swe-agent (not multi-agent, not SAO).
            Building a harness kernel → task:agent-harness-runtime / omp2; running SWE-bench → mini-swe-agent.
2. RESOLVE  `python -m library sota <task>` or `python -m library decide <task>` -> method + claims + papers + recipes.
3. VERIFY   weight each claim by evidence (verified + evidence_level) and freshness
            (as_of / last_reviewed). If a task's current_sota is older than 4 months, say so in your
            answer and re-check literature before committing an expensive plan.
4. EXECUTE  `python -m library show recipe:<slug>`; check `target_hardware` and `pip_dependencies`
            against the user's actual budget before promising anything.
5. WRITE    if you discovered something the graph lacks: ingest per §8, appending a receipt to
            `graph/CHANGELOG.md`. Ingestion includes the supersession check (§8 step 3).
```

### 9.2 Token discipline

- **Remote first**: if you are working against the GitHub remote (no local clone), fetch the compiled
  graph in one call — `gh api repos/j8ckfi/library/contents/dist/graph.json` (CI keeps it fresh) — and
  fall back to per-node `contents/` fetches only for files you will act on.
- Prefer `sota` / `decide` over `query` (one call returns the whole resolution path); prefer `query --json` for
  scripted filtering; use `show` only on the specific nodes you will act on; use `walk`/`path` only when
  `sota`/`query` leave a genuine traversal question open.
- Never re-derive what a single `validate` can tell you; run it after a coherent batch of graph edits and before reporting graph changes.

### 9.3 Trust calibration

- `verified: true` + comparator baseline is the only basis for a default recommendation.
- `evidence_level` ranks claims: `peer-reviewed` > `preprint` > `unofficial-repro` > `self-reported`.
- A `current_sota[].as_of` older than ~4 months means **stale**: the routing may still be right, but the
  rank order deserves a literature re-check before you stake a training run on it.
