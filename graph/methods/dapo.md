---
id: method:dapo
type: method
title: "DAPO (Dense Advantage Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-dense
supersedes:
  - method:grpo
papers:
  - paper:dapo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "Long-CoT Mathematical & Code Reasoning"
    metric: "pass@1 accuracy & stability"
    value: "Strictly outperforms vanilla GRPO on dense models"
    baseline: "Vanilla GRPO"
    date: "2025-03"
    verified: true
    notes: "Clip-higher, dynamic sampling, token-level loss, and overlong trace shaping for dense policies."
tags:
  - rl-alignment
  - reasoning
  - dapo
  - long-cot
---

# DAPO (Dense Advantage Policy Optimization)

## Method Overview
DAPO (Dense Advantage Policy Optimization) optimizes long-CoT reasoning rollouts in dense models through four key mechanisms:
1. **Clip-Higher**: Asymmetric policy clipping preventing collapse on high-reward exploration rollouts.
2. **Dynamic Sampling**: Dynamically modulates group rollout sizes based on prompt difficulty.
3. **Token-Level Loss**: Weighting gradient updates by token positions to avoid penalizing early reasoning steps.
4. **Overlong Trace Shaping**: Suppresses degenerate rambling traces without killing valid reasoning chains.

## When to Use
- Default reinforcement learning optimizer for dense long-CoT reasoning models.

## Supersession
- Supersedes vanilla `method:grpo` for dense long-CoT reasoning.
