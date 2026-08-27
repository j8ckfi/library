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
papers:
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

## Supersession
- Supersedes `method:galore` for memory-efficient full-parameter pretraining.
