---
id: method:cppo
type: method
title: "CPPO (Cumulative Prefix-divergence Policy Optimization)"
category: "rl-alignment"
status: active
papers:
  - paper:cppo
recipes:
  - recipe:cppo
claims:
  - benchmark: "Mathematical & Reasoning Benchmarks"
    metric: "policy improvement & stability"
    value: "Non-uniform token-level trust region via prefix divergence"
    baseline: "PPO / GRPO"
    date: "2026-06-15"
    verified: true
    notes: "Token-level masking with position-weighted thresholds and cumulative prefix budget to align with finite-horizon policy improvement bounds."
tags:
  - post-training
  - rl-alignment
  - reasoning
  - trust-region
  - cppo
---

# CPPO (Cumulative Prefix-divergence Policy Optimization)

## Method Overview
CPPO (Cumulative Prefix-divergence Policy Optimization) replaces position-agnostic token-level trust regions with a non-uniform trust-region mechanism:
1. **Position-Weighted Threshold**: Enforces stricter trust-region constraints at early token positions and looser constraints at later positions.
2. **Cumulative Prefix Budget**: Restricts further deviation after prefix drift accumulates along the trajectory.
3. **Finite-Horizon Policy Improvement**: Directly aligns token-level update masking with finite-horizon policy-improvement bounds.

## When to Use
- LLM reinforcement learning where uniform token-level trust regions allow cascading prefix divergence or over-constrain later tokens.
