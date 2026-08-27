---
id: method:circuitsteer
type: method
title: "CircuitSteer (SAE Circuit Steering)"
category: "circuits"
status: sota
sota_for:
  - task:mechanistic-interpretability-dictionaries
  - task:sae-circuits
papers:
  - paper:circuitsteer
recipes:
  - recipe:circuitsteer
claims:
  - benchmark: "Transformer Circuit Steering & Causal Interventions"
    metric: "steering specificity & downstream perplexity retention"
    value: "Default SOTA for SAE circuit steering"
    baseline: "Vector Activation Steering"
    date: "2026-08-26"
    verified: true
    notes: "Causal representation steering via Sparse Autoencoder subspace dictionary projections."
tags:
  - interpretability
  - circuits
  - steering
  - sae
  - circuitsteer
  - sota
---

# CircuitSteer (SAE Circuit Steering)

## Method Overview
CircuitSteer establishes the state-of-the-art methodology for steering transformer representations:
1. **Subspace Circuit Steering**: Projects interventions along multi-dimensional subspace boundaries extracted by SAEs.
2. **Targeted Causal Control**: Modifies specific downstream behaviors (e.g. bias, persona, reasoning steps) while preserving general language fluency.

## When to Use
- Default SOTA method for SAE circuits and representation steering.
