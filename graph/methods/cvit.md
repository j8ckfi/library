---
id: method:cvit
type: method
title: CViT (Continuous Vision Transformer)
category: neural-operator
status: sota
sota_for:
- task:operator-grid-pde
supersedes: []
papers:
- paper:cvit
recipes:
- recipe:cvit
claims:
- benchmark: PDEBench / 2D Darcy / 2D Navier-Stokes / Shallow Water
  metric: relative L2 error across variable grid resolutions
  value: Default SOTA for regular-grid continuous operator learning (ICLR 2025)
  baseline: FNO / F-FNO / CNO / ViT
  date: '2026-08-28'
  verified: true
  notes: ViT encoder with continuous coordinate embeddings and query-wise cross-attention
    for resolution-invariant inference.
tags:
- scientific-ml
- neural-operator
- cvit
- transformer
- sota
---

# CViT (Continuous Vision Transformer)

## Method Overview
CViT establishes the state-of-the-art for regular-grid parametric PDE operator learning:
1. **Continuous Coordinate Embeddings**: Replaces fixed patch positional embeddings with continuous spatial coordinate functions.
2. **Query-Wise Cross-Attention**: Employs continuous cross-attention to query solution states at arbitrary continuous evaluation points, ensuring zero-shot resolution invariance.

## When to Use
- Default SOTA method for regular-grid parametric PDEs (Darcy flow, Navier-Stokes, shallow water).
