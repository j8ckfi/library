---
id: method:minpro
type: method
title: "MinPRO (Minimum Prefix Ratio Policy Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:minpro
recipes:
  - recipe:minpro
claims:
  - benchmark: "Dense & MoE Math Reasoning Benchmarks"
    metric: "training stability & accuracy"
    value: "Stabilizes off-policy policy optimization via minimum prefix ratio"
    baseline: "PPO / GRPO"
    date: "2026-01-22"
    verified: true
    notes: "Non-cumulative surrogate replacing unstable cumulative prefix importance ratios with the minimum token-level ratio in the preceding prefix."
tags:
  - post-training
  - rl-alignment
  - reasoning
  - importance-sampling
  - minpro
---

# MinPRO (Minimum Prefix Ratio Policy Optimization)

## Method Overview
MinPRO stabilizes policy optimization under off-policy trajectory rollouts:
1. **Prefix Importance Ratio**: Identifies the theoretical necessity of prefix importance weighting over naive token-level importance sampling.
2. **Minimum Prefix Surrogate**: Replaces the numerically unstable cumulative product of prefix ratios with a non-cumulative surrogate—the minimum token-level ratio within the preceding prefix.
3. **Dense & MoE Scalability**: Delivers robust policy updates across both dense and Mixture-of-Experts (MoE) reasoning models without exponential variance blowup.

## When to Use
- Policy optimization runs with off-policy data or large batch sampling where token-level importance sampling destabilizes training.
