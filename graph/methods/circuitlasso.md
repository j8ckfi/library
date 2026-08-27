---
id: method:circuitlasso
type: method
title: "CircuitLasso"
category: "circuits"
status: active
papers:
  - paper:circuitlasso
recipes:
  - recipe:circuitlasso
claims:
  - benchmark: "Causal Circuit Identification"
    metric: "circuit edge sparsity vs faithfulness"
    value: "Scalable continuous L1 Lasso circuit pruning"
    baseline: "Edge Attribution Patching"
    date: "2026-08-26"
    verified: true
    notes: "Continuous L1 relaxation for finding minimal causal sub-circuits."
tags:
  - interpretability
  - circuits
  - circuitlasso
---

# CircuitLasso

## Method Overview
CircuitLasso uses continuous L1 relaxation to identify minimal causal sub-circuits in large transformer models.

## When to Use
- Discovering causal circuit pathways in models up to 70B parameters.
