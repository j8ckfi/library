---
id: method:ffno
type: method
title: Factorized Fourier Neural Operator (F-FNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:ffno
recipes:
- recipe:ffno
claims:
- benchmark: 2D/3D Navier-Stokes / Turbulence
  metric: relative L2 error & memory footprint
  value: Factorized spectral mode parameterization baseline
  baseline: Standard FNO
  date: '2026-08-28'
  verified: true
  notes: Separable 1D Fourier transforms along each spatial dimension to reduce parameters
    and memory.
tags:
- scientific-ml
- neural-operator
- spectral
- ffno
---

# Factorized Fourier Neural Operator (F-FNO)

## Method Overview
Factorized Fourier Neural Operators (F-FNO) address the quadratic parameter scaling of standard FNO in multidimensional settings:
1. **Separable Fourier Layers**: Decomposes multidimensional spectral weights into separable 1D Fourier transforms along each coordinate axis.
2. **Spectral Skip Connections**: Incorporates spectral domain residual connections and improved normalization.

## When to Use
- Active baseline when memory constraints prevent scaling standard FNO to 3D domains.
