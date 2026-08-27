---
id: paper:minpro
type: paper
title: "A Step Back: Prefix Importance Ratio Stabilizes Policy Optimization"
authors:
  - "Shiye Lei"
  - "Zhihao Cheng"
  - "Dacheng Tao"
year: 2026
month: 1
arxiv_id: "2601.22718"
url: "https://arxiv.org/abs/2601.22718"
methods:
  - method:minpro
cites: []
tags:
  - post-training
  - rl-alignment
  - reasoning
  - importance-sampling
  - minpro
---

# A Step Back: Prefix Importance Ratio Stabilizes Policy Optimization

## Abstract Summary
Token-level importance sampling becomes highly unstable when policy optimization encounters substantial off-policyness, while cumulative prefix importance ratios suffer from exponential variance growth across long reasoning chains. MinPRO replaces the unstable cumulative prefix ratio with a non-cumulative surrogate defined as the minimum token-level ratio in the preceding prefix, stabilizing policy optimization across dense and MoE math reasoning tasks.

## Key Contributions
1. **Diagnosis of Off-Policy Instability**: Analyzes failure modes of standard token-level importance sampling under large policy shifts.
2. **Minimum Prefix Ratio Surrogate**: Introduces a stable, non-cumulative surrogate using the minimum token ratio across the preceding prefix.
3. **Empirical Validation**: Demonstrates enhanced convergence and reasoning performance on dense and MoE architectures on mathematical reasoning benchmarks.

## Open Source Repository
- Implementation: `none found`
