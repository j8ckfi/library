---
id: method:taco
type: method
title: "TACO"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Muon2 remains the 7B pretrain default; TACO is a full-param FT memory geometry"
    use_instead: "method:muon2"
  - when: "full-parameter memory-efficient pretraining on 24GB (subspace projections)"
    reason: "SCALE remains that first hop; TACO is ternary column-wise one-sparse FT"
    use_instead: "method:scale"
  - when: "native FP4 forward/backward hardware training from scratch"
    reason: "Quartet-II / MXFP4 remain FP4 hardware training"
    use_instead: "method:quartet-ii"
  - when: "quality LoRA on 24GB without a fully quantized checkpoint constraint"
    reason: "TACO is full-param FT; LoRA quality stays vanilla LoRA + rsLoRA + LR sweep"
    use_instead: "method:lr-matters-lora"
assumptions:
  - "Full-parameter LLM fine-tuning of 2D weight matrices. Vanilla TACO is history-free column Top-1; practical TACO keeps a small FP8 heavy-hitter set per column."
  - "Paper: OPT-13B/30B, Qwen3-32B, Pythia / Llama / Mistral families on an 80 GB H100. AdamW-pretrained checkpoints; Muon geometry mismatch is a cited FT failure mode."
  - "Official code Jichao2357/TACO_optimizer."
last_reviewed: "2026-10-02"
papers:
  - paper:taco
recipes:
  - recipe:taco
claims:
  - benchmark: "OPT-13B SST-2 full-param FT, 80 GB H100"
    metric: "accuracy / peak training memory / optimizer state"
    value: "94.22% at 27.5 GB peak; optimizer state 0.16 GB"
    baseline: "AdamW8bit 80.6 GB peak / 27.7 GB state (174× state, 2.9× peak)"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02199"
    notes: "Abstract / Figure 1. Comparable accuracy and runtime. Not a Muon2 or SCALE retarget."
  - benchmark: "Full-param FT of 30–32B models on one 80 GB H100"
    metric: "fits / optimizer-state share of peak"
    value: "OPT-30B and Qwen3-32B; optimizer state <0.5% of peak (0.267 GB on OPT-30B)"
    baseline: "AdamW does not fit OPT-30B on one H100 80 GB"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02199"
    notes: "FT axis on task:full-param-memory-efficient-pretrain. Pretrain optimizer stays Muon2."
tags:
  - optimizer
  - efficiency
  - memory-efficient
  - taco
  - fine-tuning
  - active
---

# TACO

## Method Overview
TACO (Ternary Absolute-max Column-wise One-sparse optimizer) takes Muon's operator-norm steepest-descent view to a dimension-normalized \(1\to 1\) geometry. The exact minimizer is separable per column: pick the sign of the largest-magnitude gradient entry. An \(m\times n\) update has at most \(n\) nonzeros. Scale \(m/n\) is the dimension-normalization factor, not a free HP. Practical TACO stores a small FP8 heavy-hitter history per column so persistent optimizer state is \(\mathcal{O}(n)\) rather than a dense Muon momentum matrix. Embeddings / 1D tensors keep a conventional fallback.

## When to Use
- Full-parameter LLM fine-tuning when AdamW/Muon optimizer state does not fit, including 30–32B on one 80 GB H100.

## When NOT to Use
- ~7B pretrain optimizer → `method:muon2`. 24GB full-param pretrain subspace → `method:scale`. FP4 from-scratch hardware → `method:quartet-ii`. Quality LoRA → `method:lr-matters-lora`.

## Relation to Existing SOTA
- Active plug-in on `task:full-param-memory-efficient-pretrain` (FT axis) beside `method:scale`. Does **not** enter SCALE or Muon2 `current_sota`. Does **not** replace Muon2, SCALE, or GaLore's already-superseded slot.

## Gotchas & Failure Modes
- Geometry is for 2D matrices. Do not apply column Top-1 to embeddings / LM head without the paper's fallback.
- Vanilla (history-free) TACO is unstable under minibatch noise; use the sparse heavy-hitter state.
- Switching an AdamW-pretrained model to dense Muon can mismatch; TACO claims a different dual geometry, not "run Muon2 at FT."
- Not a pretrain-from-scratch recipe.
