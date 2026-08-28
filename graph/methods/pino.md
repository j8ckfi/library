---
id: method:pino
type: method
title: Physics-Informed Neural Operator (PINO)
category: neural-operator
status: active
sota_for: []
supersedes: []
superseded_by: method:pi-cvit
papers:
- paper:pino
recipes:
- recipe:pino
claims:
- benchmark: 2D Navier-Stokes / Darcy / High Reynolds number PDEs
  metric: relative L2 error with limited/zero data
  value: Physics-informed spectral operator baseline
  baseline: PINN / Pure Data FNO
  date: '2026-08-28'
  verified: true
  notes: Combines data loss and PDE residual loss across multiple discretization resolutions.
tags:
- scientific-ml
- neural-operator
- physics-informed
- pino
---

# Physics-Informed Neural Operator (PINO)

## Method Overview
Physics-Informed Neural Operator (PINO) trains operator architectures with physical governing equations:
1. **Dual Objective**: Optimizes both empirical data loss on known trajectories and PDE residual loss at collocation points.
2. **Multi-Resolution PDE Loss**: Computes physical derivative residuals across multiple discretization grids using exact Fourier differentiation.

Disambiguation: PINO refers to Physics-Informed Neural Operator (Li et al., 2111.03794).

## Supersession
- Superseded by `method:pi-cvit` (2606.06164) as 2026 physics-informed SOTA default; remains active.
