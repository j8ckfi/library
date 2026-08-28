---
id: method:lno
type: method
title: Latent Neural Operator (LNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:lno
recipes:
- recipe:lno
claims:
- benchmark: Forward and Inverse PDEs (Darcy / Poisson / Helmholtz)
  metric: relative L2 error
  value: Latent neural operator baseline for forward/inverse problems
  baseline: FNO / DeepONet
  date: '2026-08-28'
  verified: true
  notes: Learns mapping between infinite-dimensional latent representations for forward
    and inverse PDE problems.
tags:
- scientific-ml
- neural-operator
- lno
- inverse-pde
---

# Latent Neural Operator (LNO)

## Method Overview
Latent Neural Operator (LNO) formulates forward and inverse operator learning in latent function spaces:
1. **Latent Space Mapping**: Projects infinite-dimensional functional inputs into continuous latent spaces.
2. **Bidirectional Solving**: Enables both forward state propagation and inverse coefficient identification.

Disambiguation: LNO (2406.03923) refers to Latent Neural Operator by Wang & Wang (2024) for forward and inverse PDE problems, NOT Laplace Neural Operator.

## When to Use
- Active baseline for forward and inverse PDE problems.
