---
id: method:adamw-optimizer
type: method
title: "AdamW Optimizer (Decoupled Weight Decay Adam)"
category: "optimizer"
status: active
superseded_by: method:muon-optimizer
sota_for: []
supersedes: []
papers:
  - paper:adamw-paper
recipes: []
claims:
  - benchmark: "Standard Transformer Pretraining"
    metric: "convergence stability"
    value: "Baseline reference"
    baseline: "SGD with Momentum"
    date: "2019-01"
    verified: true
    notes: "Decoupled L2 regularization from gradient momentum updates."
tags:
  - optimizer
  - baseline
---

# AdamW Optimizer (Decoupled Weight Decay Adam)

## Method Overview
AdamW modifies the original Adam optimizer by decoupling weight decay from gradient-based moment updates. In standard Adam with L2 regularization, weights with large historical gradients receive smaller relative weight decay penalty. AdamW restores true weight decay by applying the decay step directly to the weights independently of the adaptive learning rate vector.

## When to Use
- Default general-purpose optimizer for arbitrary 1D parameters, embeddings, layer norms, and multimodal heads.
- When matrix-level orthogonalization (Muon) is unsupported by hardware or layer topology.

## Gotchas & Failure Modes
- High memory consumption (maintains 2 additional FP32 optimizer states per parameter: first and second moments).
- Sensitive to epsilon parameter \(\epsilon\) and beta coefficients under low-precision training (FP16/BF16).
