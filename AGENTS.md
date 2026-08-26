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

## 2. Agent Routing Cheat-Sheet (First-Hop SOTA Index)

Use this quick-routing table as of **2026-08-26**:

```
task: pretrain dense 7B     -> muon-scalable  (+ soap-muon-scale if big batch / extra mem)
task: pretrain MoE          -> deepseek-v3 arch, muonclip-kimi-k2 opt; read kimi-k3 if 2026-frontier
task: open data recipe      -> olmo-2-curriculum
task: instruct SFT          -> tulu3-rlvr (SFT stage)
task: general alignment     -> tulu3-rlvr (SFT->DPO->RLVR)
task: math/code RL, dense   -> dapo + dr-grpo
task: math/code RL, MoE     -> gspo + dr-grpo
task: process supervision   -> verigate (not un-gated PRM)
task: LoRA 24GB             -> qlora; quality: dora or delora
task: full-param, 24GB      -> galore
task: tiny on-device LLM    -> bitnet-b158 (from-scratch) else qlora+GGUF
task: distill student       -> on-policy-distillation
task: SNN audio/event       -> silif
task: SAE / circuits        -> sasa
task: neural video train    -> dcvcrt
task: continuous control    -> td-mpc2, then dream-mpc planner
```

---

## 3. SOTA Map (What You Actually Pick Today — 2026-08-26)

1. **Train a ~7B dense LM from scratch**: Use **Muon** (`method:muon-scalable`) with Moonshot's two scale-up fixes: weight decay + per-parameter update-RMS matching. Keep embeddings / `lm_head` on AdamW. If GPU memory is not the bottleneck and you can pay SOAP's extra state, NVIDIA's Jul-2026 Megatron study recommends **KL-SOAP** (`method:soap-muon-scale`) over Muon at large batch (up to ~100M tokens). Architecture: dense Llama-like is still the open default. Data: two-stage OLMo-2 curriculum (`paper:olmo-2-curriculum`). Do not Chinchilla-copy an AdamW token budget—Muon is ~2x more token-efficient in Moonshot's scaling laws.
2. **SFT a chat / instruct model**: **Tülu-3 stack** (`method:tulu3-rlvr`): curated SFT → on-policy DPO → **RLVR** (verifiable rewards, no learned RM). Code: `allenai/open-instruct`. Prefer decontaminated, skill-specific mixes over "just ShareGPT." If you only have a weekend and a 24 GB card, skip to QLoRA/DoRA on a strong instruct checkpoint instead of training a base.
3. **RL a reasoner (math/code, verifiable)**: Start from a base or light-SFT checkpoint (R1-Zero path is real). Optimizer: **DAPO** (`method:dapo`) for dense long-CoT (clip-higher, dynamic sampling, token-level loss, overlong shaping). Switch to **GSPO** (`method:gspo`) if the policy is MoE (Qwen3 recipe; sequence-level IS ratio). Apply **Dr. GRPO**'s de-bias (`method:dr-grpo`, drop length and std-normalization) so incorrect traces don't get rewarded for being long. Reward = unit-test / math verifier / boxed-answer match. A learned process-reward model is *optional* and dangerous; if you add one, gate it behind a verifier (**VeriGate**-style `paper:verigate`) so PRM noise cannot override a trusted outcome check.
4. **LoRA a local model on one GPU**: Default is still **QLoRA** (`method:qlora`, NF4 + LoRA, bitsandbytes / transformers / PEFT). Quality bump: **DoRA** (`method:dora`, magnitude/direction split) or **DeLoRA** (`method:delora`, bounded Frobenius update, more robust to LR / long runs). Merge adapters before serving. Full-rank-but-cheap alternative for pretrain/finetune memory: **GaLore** (`method:galore`).
5. **Distill a small local student from a strong teacher**: Do **on-policy distillation** (`method:on-policy-distillation`, GKD / Thinking Machines 2025 recipe), not offline SFT on teacher traces. Sample from the *student*, score tokens with teacher log-probs (reverse or mixed KL).
6. **Extreme compression / on-device**: If you control pretraining: train **BitNet b1.58** (`method:bitnet-b158`) from scratch. Infer with `bitnet.cpp` kernels. Do not post-train-quantize all the way to 1.58-bit and expect BitNet-native quality.
7. **Train a spiking net (audio / event)**: Use **SiLIF / C-SiLIF** (`method:silif`). Train with surrogate-gradient BPTT, not conversion.
8. **Learned control / world-model RL**: Default remains **TD-MPC2** (`method:td-mpc2`). If planning cost dominates, swap the MPPI planner for **Dream-MPC** (`method:dream-mpc`). Dream-MPC code: `none found`—do not invent a GitHub URL.
9. **Honorable extra**: Video compression training is **DCVC-RT** (`method:dcvcrt`); 2026 successor **MLVC** (`paper:mlvc`). Interpretability training is **SASA** (`method:sasa`, subspace SAEs) over vanilla vector SAEs.

---

## 4. Supersedes Edges & Lineage

The knowledge graph encodes the following explicit supersession relationships:
- `muon` supersedes `adamw-optimizer` for hidden matrices.
- `muon-scalable` supersedes raw `muon` defaults at LLM scale.
- `muonclip-kimi-k2` supersedes `muon-scalable` at trillion scale.
- `kimi-k3` supersedes `deepseek-v3` architecture for 2026-frontier deployments.
- `soap` supersedes `shampoo`.
- `soap-muon-scale` supersedes original small-scale `soap`.
- `dapo` supersedes vanilla `grpo` for dense long-CoT.
- `gspo` supersedes token-level IS (`grpo`) when policy is MoE.
- `dr-grpo` supersedes unpatched `grpo` length/std normalization.
- `tulu3-rlvr` supersedes RM-only `ppo-rlhf` as the open path.
- `on-policy-distillation` supersedes offline teacher-CoT SFT.
- `dora` supersedes vanilla `lora` as quality default.
- `delora` supersedes `dora` for long/LR-sensitive runs.
- `silif` supersedes `surrogate-gradient-snn` / `AdLIF`.
- `sasa` supersedes `gated-sae` and `standard-sae` vector SAEs.
- `dcvcrt` supersedes `dcvc-dc` for real-time video coding.
- `bitnet-b158` supersedes PTQ-to-1-bit as a quality path.

---

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
2. Resolve SOTA Method: method:dapo (Dense Advantage Policy Optimization)
   │
   ├──► 3. Inspect Literature: paper:dapo / paper:dr-grpo
   │
   └──► 4. Load Runnable Code: recipe:grpo-trl-training
```

---

## 6. Querying the Library via CLI

The library provides a zero-dependency CLI (`python -m library`):

### 6.1 Resolving SOTA for a Task or Domain
```bash
# Look up canonical SOTA method, claims, paper, and recipe for pretraining
python -m library sota "pretrain dense 7B"

# Direct task ID lookup
python -m library sota "task:math-code-rl-dense"

# Structured JSON output for agent tools
python -m library sota "task:parameter-efficient-fine-tuning" --json
```

### 6.2 Searching the Graph
```bash
# Keyword query across all nodes
python -m library query "muon scalable"

# Filter by node type or domain
python -m library query "quantization" --type method
python -m library query "silif" --domain snn

# Filter only active SOTA nodes
python -m library query "distillation" --sota-only --json
```

### 6.3 Reading Node Content & Walking Neighbors
```bash
# Display node markdown body and metadata
python -m library show "method:dapo"

# Inspect connected edges (papers, tasks, recipes, supersedes)
python -m library walk "method:muon-scalable"

# Find path between any two graph nodes
python -m library path --from "task:pretrain-dense-7b" --to "recipe:muon-pretraining"
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
