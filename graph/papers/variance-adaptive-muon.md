---
id: paper:variance-adaptive-muon
type: paper
title: "Variance-Adaptive Muon for Non-Stationary LLM Pretraining"
authors:
  - "Variance-Adaptive Muon Authors"
year: 2026
month: 1
arxiv_id: "2601.14603"
url: "https://arxiv.org/abs/2601.14603"
methods:
  - method:variance-adaptive-muon
cites:
  - paper:muon-scalable
tags:
  - optimizer
  - pretraining
  - variance-adaptive-muon
---

# Variance-Adaptive Muon for Non-Stationary LLM Pretraining

## Abstract Summary
Variance-Adaptive Muon modulates matrix orthogonalization step sizes using running gradient variance estimates, stabilizing pretraining on heterogeneous multimodal data streams.

## Key Contributions
1. **Adaptive Step Sizing**: Couples second-moment variance scaling with Newton-Schulz orthogonalization.
2. **Training Stability**: Prevents loss divergence across curriculum stage transitions.

## Open Source Repository
- Implementation: `none found`
