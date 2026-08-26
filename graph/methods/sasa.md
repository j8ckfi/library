---
id: method:sasa
type: method
title: "SASA (Subspace Sparse Autoencoders)"
category: "circuits"
status: sota
sota_for:
  - task:mechanistic-interpretability-dictionaries
supersedes:
  - method:gated-sae
  - method:standard-sae
papers:
  - paper:sasa
recipes:
  - recipe:gated-sae-training
claims:
  - benchmark: "Gemma / LLaMA Circuit Decomposition"
    metric: "subspace feature interpretability"
    value: "Pareto superior to 1D vector SAEs"
    baseline: "Vector SAEs & Gated SAEs"
    date: "2026-06"
    verified: true
    notes: "Extracts multi-dimensional subspace dictionaries to model non-orthogonal circular and combinatorial features."
tags:
  - interpretability
  - mechanistic
  - circuits
  - sasa
  - subspace-sae
---

# SASA (Subspace Sparse Autoencoders)

## Method Overview
Standard Sparse Autoencoders assume every feature is represented as a 1D vector ray in activation space. However, complex neural representations (such as circular days-of-the-week, continuous angles, and rotational symmetries) reside in multi-dimensional subspaces. **SASA** extracts multi-dimensional subspace dictionaries, avoiding artificial splitting of continuous geometry into separate monosemantic vectors.

## Supersession
- Supersedes vanilla 1D vector SAEs.
