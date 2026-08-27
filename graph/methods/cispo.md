---
id: method:cispo
type: method
title: "CISPO (Clipped Importance Sampling Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-dense
  - task:reasoning-rl-alignment
supersedes:
  - method:dapo
papers:
  - paper:minimax-m1
  - paper:scalerl
recipes:
  - recipe:cispo
claims:
  - benchmark: "MATH-500 / AIME 2024 / LiveCodeBench"
    metric: "pass@1 accuracy & sample efficiency"
    value: "Default SOTA for dense long-CoT reasoning RL"
    baseline: "DAPO / GRPO / PPO"
    date: "2026-08-26"
    verified: true
    notes: "MiniMax-M1 and ScaleRL recipe with clipped importance sampling."
tags:
  - post-training
  - rl-alignment
  - dense-rl
  - cispo
  - sota
---

# CISPO (Clipped Importance Sampling Policy Optimization)

## Method Overview
CISPO (Clipped Importance Sampling Policy Optimization) establishes the state-of-the-art reinforcement learning standard for dense reasoning models:
1. **Clipped Importance Sampling**: Stabilizes policy ratio trajectories during long-horizon exploration.
2. **Dense Reasoning Alignment**: Maximizes verifiable pass@1 accuracy across competitive math and programming benchmarks.

## When to Use
- Default SOTA optimizer for dense model math and code reasoning RL.

## Supersession
- Supersedes `method:dapo` as the dense RL default (DAPO remains as a systems reference).
