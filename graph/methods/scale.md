---
id: method:scale
type: method
title: "SCALE (Memory-Efficient Pretraining)"
category: "optimizer"
status: sota
sota_for:
  - task:full-param-memory-efficient-pretrain
supersedes:
  - method:galore
do_not_use_for:
  - when: "low-rank gradient sketches + predicted-KL step control for RL memory"
    reason: "SCALE remains full-param pretrain memory; LoGRA is an RL-step memory sketch"
    use_instead: "method:logra"
  - when: "ternary abs-max column-wise one-sparse optimizer for full-param LLM FT"
    reason: "SCALE remains the subspace-projection first hop; TACO is an FT-axis sparse geometry"
    use_instead: "method:taco"
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Muon2 remains the 7B pretrain default"
    use_instead: "method:muon2"
papers:
  - paper:logra
  - paper:scale
recipes:
  - recipe:scale
claims:
  - benchmark: "Full-Parameter 24GB Pretraining / Fine-Tuning"
    metric: "loss convergence & memory reduction"
    value: "Default SOTA for memory-efficient full-parameter training (ICML 2026)"
    baseline: "GaLore"
    date: "2026-08-26"
    verified: true
    notes: "Scaled subspace gradient projections for smooth trajectory updates without SVD latency stalls."
last_reviewed: "2026-10-06"
tags:
  - optimizer
  - pretraining
  - memory-efficient
  - scale
  - sota
---

# SCALE (Memory-Efficient Pretraining)

## Method Overview
SCALE (ICML 2026) develops scaled subspace gradient projections for full-parameter pretraining within tight memory budgets (e.g. 7B models on 24GB GPUs):
1. **Scaled Subspace Projections**: Smooth projection updates avoiding the periodic SVD synchronization pauses of GaLore.
2. **Full-Rank Dynamics**: Maintains full-rank parameter evolution trajectories with low-rank optimizer state memory.

## When to Use
- Default SOTA method for full-parameter memory-efficient pretraining and fine-tuning on consumer hardware (NOT GaLore).
- Optional FT-axis sparse optimizer (`method:taco`) does not replace SCALE.

## Supersession
- Supersedes `method:galore` for memory-efficient full-parameter pretraining.
