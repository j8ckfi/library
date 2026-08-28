---
id: method:cno
type: method
title: Convolutional Neural Operator (CNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:cno
recipes:
- recipe:cno
claims:
- benchmark: Compressible Euler / Navier-Stokes / Shear Layer
  metric: relative L2 error & aliasing robustness
  value: Continuous representation-equivalent CNN operator baseline
  baseline: FNO / U-Net
  date: '2026-08-28'
  verified: true
  notes: Anti-aliased continuous convolutional filters ensuring representation equivalence
    across resolutions.
tags:
- scientific-ml
- neural-operator
- cno
- cnn-operator
---

# Convolutional Neural Operator (CNO)

## Method Overview
Convolutional Neural Operators (CNO) formulate neural operators via continuous, alias-free convolutions:
1. **Representation Equivalence**: Ensures model predictions commute with continuous spatial translations and resolution changes (stricter than discretization convergence).
2. **Anti-Aliasing Filters**: Employs low-pass filtering and continuous activation functions to eliminate spectral aliasing errors.

Disambiguation: CNO refers specifically to Convolutional Neural Operator (Raonić et al., 2302.01178) with continuous anti-aliased filtering.

## When to Use
- Active grid baseline for shock waves, shear layers, and discontinuous transport problems.
