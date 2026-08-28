---
id: method:transolver
type: method
title: Transolver (Physics-Attention PDE Transformer)
category: neural-operator
status: active
sota_for: []
supersedes: []
superseded_by: method:transolver-3
papers:
- paper:transolver
recipes:
- recipe:transolver
claims:
- benchmark: Car-Design / ShapeNet / 2D/3D Complex Geometries
  metric: relative L2 error & throughput
  value: Physics-Attention slice operator baseline
  baseline: GNOT / Geo-FNO / PointNet
  date: '2026-08-28'
  verified: true
  notes: Discretizes arbitrary continuous physical domains into learned 1D slice representations
    for linear-complexity attention (ICML 2024).
tags:
- scientific-ml
- neural-operator
- transformer
- transolver
---

# Transolver (Physics-Attention PDE Transformer)

## Method Overview
Transolver solves PDEs on general geometries via learned Physics-Attention:
1. **Physics-Attention Slices**: Discretizes arbitrary 3D continuous domains into learned 1D slice representations.
2. **Linear Complexity Attention**: Computes self-attention across the compact physical slice tokens rather than millions of raw mesh vertices.

Disambiguation: Transolver refers to the original Physics-Attention transformer solver (Wu et al., 2402.02366, ICML 2024).

## Supersession
- Superseded by `method:transolver-3` (2602.04940, ICML 2026) as the industrial CAD default; remains active.
