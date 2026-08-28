---
id: method:fno
type: method
title: Fourier Neural Operator (FNO)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:fno
recipes:
- recipe:fno
claims:
- benchmark: 2D Darcy Flow / 2D Navier-Stokes
  metric: relative L2 error
  value: Discretization-convergent zero-shot super-resolution baseline
  baseline: Standard CNN / FCN
  date: '2026-08-28'
  verified: true
  notes: Foundational spectral neural operator operating in Fourier frequency domain
    via FFT.
tags:
- scientific-ml
- neural-operator
- spectral
- fno
- baseline
---

# Fourier Neural Operator (FNO)

## Method Overview
Fourier Neural Operator (FNO) parameterizes the integral kernel in Fourier space directly:
1. **Global Convolution via FFT**: Computes continuous kernel integration efficiently using the Fast Fourier Transform (FFT) on regular grids.
2. **Zero-Shot Super-Resolution**: Invariant to discretization grid resolution, allowing evaluation at resolutions different from training data.

Disambiguation: Classical Fourier Neural Operator operating on regular grids via Fast Fourier Transforms (FFT).

## When to Use
- Canonical baseline for parametric PDEs on regular Cartesian grids.
- Transolver-3 / CViT supersede as current defaults.
