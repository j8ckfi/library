---
id: method:standard-sae
type: method
title: "Standard L1 ReLU Sparse Autoencoder"
category: "circuits"
status: active
superseded_by: method:gated-sae
sota_for: []
supersedes: []
papers:
  - paper:standard-sae-paper
recipes: []
claims:
  - benchmark: "Toy Models of Superposition / Anthropic Dictionary Learning"
    metric: "feature interpretability"
    value: "Baseline dictionary learning"
    baseline: "PCA / ICA"
    date: "2023-10"
    verified: true
    notes: "Overcomplete autoencoder with L1 penalty on hidden activations."
tags:
  - interpretability
  - baseline
---

# Standard L1 ReLU Sparse Autoencoder

## Method Overview
Standard SAEs map dense model activations \(x\) through a single linear encoder with ReLU activation and reconstruct with normalized linear decoder columns, penalized by a combined MSE and \(L_1\) regularization loss.

## When to Use
- Historical baseline and conceptual reference for mechanistic interpretability.

## Gotchas & Failure Modes
- Severe feature shrinkage caused by \(L_1\) regularization pulling true activation magnitudes toward zero.
