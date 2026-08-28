---
id: task:operator-physics-informed
type: task
title: Physics-Informed Neural Operators (PINO)
domain: scientific-ml
summary: Training neural operators with partial differential equation residual constraints
  and collocation points under scarce or zero labeled data.
current_sota:
- method: method:pi-cvit
  as_of: '2026-08-28'
  benchmark: Kolmogorov Flow / 2D Darcy / Allen-Cahn without labeled data
  metric: relative L2 error & training stability
  value: Default SOTA Physics-Informed Operator
  notes: PI-CViT (2606.06164); Continuous Vision Transformer with GradNorm, causal
    temporal weighting, and SOAP optimizer.
methods:
- method:pi-cvit
- method:pino
tags:
- scientific-ml
- neural-operator
- physics-informed
- pino
- pi-cvit
---

# Physics-Informed Neural Operators (PINO)

## Problem Definition
Solving parametric PDE families using PDE residual losses and boundary/initial condition penalties on collocation points when labeled simulation data is scarce, expensive, or completely unavailable.

## SOTA Recommendation (as of 2026-08-28)
- **Primary SOTA**: **PI-CViT** (`method:pi-cvit`, 2606.06164), combining Continuous Vision Transformer architecture with GradNorm balancing, causal temporal weighting, and SOAP second-order optimization.
- **Baseline**: **PINO** (`method:pino`, 2111.03794).
