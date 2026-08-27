---
id: method:fega
type: method
title: "FEGA (Feature Effect Geometry Analysis)"
category: "interpretability"
status: sota
sota_for:
  - task:mechanistic-interpretability-dictionaries
  - task:sae-effect-geometry
papers:
  - paper:fega
recipes:
  - recipe:fega
claims:
  - benchmark: "SAE Effect Geometry & Feature Interaction"
    metric: "geometric fidelity & causal influence explanation"
    value: "Default SOTA for SAE effect geometry analysis"
    baseline: "Cosine Feature Similarity"
    date: "2026-08-26"
    verified: true
    notes: "Models non-linear geometric interactions across Sparse Autoencoder feature dictionaries."
tags:
  - interpretability
  - circuits
  - geometry
  - sae
  - fega
  - sota
---

# FEGA (Feature Effect Geometry Analysis)

## Method Overview
FEGA introduces Feature Effect Geometry Analysis:
1. **Riemannian Effect Manifolds**: Characterizes non-linear interactions between sparse dictionary features across transformer layers.
2. **Causal Influence Mapping**: Disentangles geometric superposition from true causal interactions.

## When to Use
- Default SOTA method for SAE effect geometry and multi-layer feature interaction analysis.
