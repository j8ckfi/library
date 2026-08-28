---
id: method:upt
type: method
title: Universal Physics Transformers (UPT)
category: neural-operator
status: active
sota_for: []
supersedes: []
papers:
- paper:upt
recipes:
- recipe:upt
claims:
- benchmark: 1D/2D/3D Multi-Domain PDE Tasks
  metric: relative L2 error & parameter scaling
  value: Latent mesh-free physics transformer ancestor
  baseline: FNO / GNO / Perceiver
  date: '2026-08-28'
  verified: true
  notes: Encodes arbitrary meshes and point clouds into a fixed-size latent transformer
    representation with cross-attention.
tags:
- scientific-ml
- neural-operator
- transformer
- upt
---

# Universal Physics Transformers (UPT)

## Method Overview
Universal Physics Transformers (UPT) decouple spatial discretization from transformer capacity:
1. **Perceiver-Style Latent Encoding**: Compresses arbitrary geometric inputs into a fixed number of latent tokens via cross-attention.
2. **Latent Physics Propagation**: Propagates physical interactions in latent space using standard transformer self-attention blocks.
3. **Query-Based Decoding**: Decodes latent features back to arbitrary evaluation points.

Disambiguation: UPT refers specifically to Universal Physics Transformers (Alkin et al., 2402.12365).

## When to Use
- Active ancestor of AB-UPT; general framework for scaling neural operators.
