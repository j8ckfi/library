---
id: task:full-param-memory-efficient-pretrain
type: task
title: "Full-Parameter Memory-Efficient Pretraining & Fine-Tuning"
domain: "efficiency"
summary: "Full-parameter optimization of large models on memory-constrained GPUs via low-rank gradient subspace projections."
current_sota:
  - method: method:scale
    as_of: "2026-08-26"
    benchmark: "Full-Parameter 24GB Pretraining / Fine-Tuning"
    metric: "loss convergence & memory reduction"
    value: "Default SOTA for memory-efficient full-parameter training"
    notes: "SCALE (2506.16659, ICML 2026) not GaLore."
methods:
  - method:scale
  - method:galore
tags:
  - efficiency
  - optimizer
  - memory-efficient
  - scale
---

# Full-Parameter Memory-Efficient Pretraining & Fine-Tuning

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **SCALE** (`method:scale`, 2506.16659, ICML 2026) — not GaLore.
