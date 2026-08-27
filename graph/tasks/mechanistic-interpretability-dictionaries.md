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
    value: "Default SOTA SAE Dictionary"
    notes: "SASA (2606.06333) KEEP."
  - method: method:circuitsteer
    as_of: "2026-08-26"
    benchmark: "Transformer Circuit Steering"
    metric: "causal steering specificity"
    value: "Default SOTA SAE Circuits"
    notes: "CircuitSteer (2608.05732)."
  - method: method:fega
    as_of: "2026-08-26"
    benchmark: "SAE Effect Geometry & Feature Interaction"
    metric: "geometric fidelity"
    value: "Default SOTA SAE Effect Geometry"
    notes: "FEGA (2607.24645)."
methods:
  - method:sasa
  - method:circuitsteer
  - method:fega
  - method:circuitlasso
  - method:hsae
  - method:sae-causal-audit
  - method:gated-sae
  - method:standard-sae
tags:
  - interpretability
  - mechanistic
  - sparse-autoencoders
  - sasa
  - circuits
---

# Mechanistic Interpretability & Sparse Feature Dictionaries

## Problem Definition
Unrolling dense residual stream representations into sparse dictionaries of monosemantic concepts and causal circuits.

## SOTA Recommendation (as of 2026-08-26)
- **SAE Dictionary**: **SASA** (`method:sasa`, 2606.06333) KEEP.
- **SAE Circuits**: **CircuitSteer** (`method:circuitsteer`, 2608.05732).
- **SAE Effect Geometry**: **FEGA** (`method:fega`, 2607.24645).
