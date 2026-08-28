---
id: method:gnot
type: method
title: GNOT (General Neural Operator Transformer)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:gnot
recipes:
- recipe:gnot
claims:
- benchmark: Irregular domain PDEs / Multiple input fields
  metric: relative L2 error
  value: General neural operator transformer baseline
  baseline: FNO / DeepONet / Geo-FNO
  date: '2026-08-28'
  verified: true
  notes: Cross-attention with geometric and multi-source field conditioning.
tags:
- scientific-ml
- neural-operator
- transformer
- gnot
---

# GNOT (General Neural Operator Transformer)

## Method Overview
GNOT introduces a general transformer-based framework for learning nonlinear continuous operators:
1. **Heterogeneous Field Encoding**: Encodes varying geometric representations, initial conditions, and boundary conditions via separate projection blocks.
2. **Cross-Attention Decoding**: Attends from continuous output query points to the multi-source latent tokens with linear attention approximations.

## When to Use
- Active baseline for multi-source physical inputs and irregular domains (ICML 2023).
