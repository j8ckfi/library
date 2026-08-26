---
id: task:mechanistic-interpretability-dictionaries
type: task
title: "Mechanistic Interpretability & Sparse Feature Dictionaries"
domain: "interpretability"
summary: "Extracting monosemantic, interpretable circuit features from transformer residual streams via sparse autoencoders."
current_sota:
  - method: method:sasa
    as_of: "2026-08-26"
    benchmark: "Gemma / LLaMA Circuit Decomposition"
    metric: "subspace feature interpretability"
    value: "Pareto superior to 1D vector SAEs"
    notes: "Subspace Sparse Autoencoders (SASA) over vanilla vector SAEs."
methods:
  - method:sasa
  - method:gated-sae
  - method:standard-sae
tags:
  - interpretability
  - mechanistic
  - sparse-autoencoders
---

# Mechanistic Interpretability & Sparse Feature Dictionaries

## Problem Definition
Deep neural network activations suffer from superposition, where linear representations represent more features than there are orthogonal dimensions in the activation space. Mechanistic interpretability leverages overcomplete Sparse Autoencoders (SAEs) to unroll dense residual stream representations into sparse dictionaries of monosemantic concepts.

## Evaluation Protocol & Benchmarks
- **Standard Metrics**: Reconstruction fidelity (Mean Squared Error / Fraction of Variance Unexplained), \(L_0\) activation sparsity (mean active features per token), downstream CE loss recovery, and automated interpretability scoring.

## SOTA Landscape
Standard TopK and \(L_1\)-penalized SAEs suffer from shrinkage bias, where \(L_1\) regularization systematically suppresses the magnitudes of true feature activations. **Gated SAEs** solve this by splitting the autoencoder into a gating network for feature selection and a separate linear path for magnitude estimation.
