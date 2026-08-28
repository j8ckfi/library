---
id: method:pi-cvit
type: method
title: PI-CViT (Physics-Informed Continuous Vision Transformer)
category: neural-operator
status: sota
sota_for:
- task:operator-physics-informed
supersedes:
- method:pino
papers:
- paper:pi-cvit
recipes:
- recipe:pi-cvit
claims:
- benchmark: 2D Darcy / Kolmogorov Flow / Allen-Cahn without labeled data
  metric: relative L2 error & training stability
  value: SOTA physics-informed operator training (free collocation matches/beats labeled
    data)
  baseline: PINO / classical PINNs
  date: '2026-08-28'
  verified: true
  notes: Combines Continuous Vision Transformer (CViT) backbone with GradNorm loss
    balancing, causal temporal weighting, and SOAP second-order optimizer.
tags:
- scientific-ml
- neural-operator
- physics-informed
- pi-cvit
- sota
---

# PI-CViT (Physics-Informed Continuous Vision Transformer)

## Method Overview
PI-CViT advances physics-informed neural operator training under scarce or zero labeled data:
1. **Continuous Vision Transformer Backbone**: Uses CViT coordinate embeddings to represent continuous solution manifolds.
2. **GradNorm & Causal Temporal Weighting**: Balances stiff gradient magnitudes between boundary penalties and interior PDE residuals with causal time-stepping.
3. **SOAP Second-Order Optimizer**: Leverages SOAP optimizer to navigate ill-conditioned physics-informed optimization landscapes.

## When to Use
- Default SOTA method for physics-informed operator learning without ground-truth simulation trajectories.

## Supersession
- Supersedes `method:pino` (2111.03794) as the physics-informed operator default.
