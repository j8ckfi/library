---
id: task:operator-foundation
type: task
title: Pretrained Foundation Neural Operators
domain: scientific-ml
summary: Large-scale pre-trained foundation models across diverse PDE families and
  physical dynamics for zero-shot and few-shot transfer.
current_sota:
- method: method:poseidon
  as_of: '2026-08-28'
  benchmark: PDEBench / 15 Diverse PDE Families
  metric: fine-tuned relative L2 error & sample efficiency
  value: Default SOTA Foundation Neural Operator
  notes: Poseidon (2405.19101); scOT SwinV2 backbone with all2all multi-physics pre-training.
- method: method:unisolver
  as_of: '2026-08-28'
  benchmark: Cross-PDE Transfer / Multi-Physics Benchmark
  metric: PDE-conditioned relative L2 error
  value: Co-Default SOTA PDE-Conditional Solver
  notes: Unisolver (2405.17527); PDE-conditional transformer with domain-wise and
    point-wise PDE symbolic embedding.
methods:
- method:poseidon
- method:unisolver
- method:dpot
- method:upt
tags:
- scientific-ml
- neural-operator
- foundation-model
- poseidon
- unisolver
---

# Pretrained Foundation Neural Operators

## Problem Definition
Pretraining large-scale foundation operator models on diverse, multi-physics partial differential equation trajectories to enable zero-shot transfer, rapid few-shot fine-tuning, and general operator capabilities across distinct physical regimes.

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **Poseidon** (`method:poseidon`, 2405.19101) multiscale foundation operator using scOT SwinV2 architecture (fine-tune when PDE family shifts).
- **Co-Default SOTA**: **Unisolver** (`method:unisolver`, 2405.17527, ICML 2025) explicitly conditioning on mathematical PDE equation tokens.
- **Ancestors**: **DPOT** (`method:dpot`, 2403.03542) autoregressive denoising operator, **UPT** (`method:upt`, 2402.12365).
