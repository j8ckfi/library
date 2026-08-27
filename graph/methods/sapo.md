---
id: method:sapo
type: method
title: "SAPO (Sequence-Level Advantage Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-moe
supersedes:
  - method:gspo
papers:
  - paper:sapo
recipes:
  - recipe:sapo
claims:
  - benchmark: "Qwen MoE / VL Reasoning & MATH-500"
    metric: "pass@1 accuracy & MoE routing stability"
    value: "Default SOTA for MoE/VL RL reasoning"
    baseline: "GSPO / GRPO"
    date: "2026-08-26"
    verified: true
    notes: "Sequence-level advantage normalization and importance sampling for MoE/VL architectures (ms-swift loss_type=sapo)."
tags:
  - post-training
  - rl-alignment
  - moe
  - reasoning
  - sapo
  - sota
---

# SAPO (Sequence-Level Advantage Policy Optimization)

## Method Overview
SAPO introduces sequence-level advantage normalization and importance sampling for sparse Mixture-of-Experts (MoE) and Vision-Language (VL) policies:
1. **Sequence Advantage Normalization**: Eliminates routing non-stationarity across dynamically routed expert layers.
2. **MoE/VL Optimization**: Prevents policy collapse during long-horizon multimodal and MoE reasoning rollouts.

## When to Use
- Default SOTA optimizer for mathematical and coding reinforcement learning on MoE and VL architectures (e.g. Qwen MoE / DeepSeek MoE).

## Supersession
- Supersedes `method:gspo` as the primary Qwen MoE/VL algorithm.
