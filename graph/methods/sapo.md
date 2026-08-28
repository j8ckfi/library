---
id: method:sapo
type: method
title: "SAPO (Soft Adaptive Policy Optimization)"
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
    notes: "Soft adaptive policy optimization with sigmoid gating for MoE/VL architectures (ms-swift loss_type=sapo)."
tags:
  - post-training
  - rl-alignment
  - moe
  - reasoning
  - sapo
  - sota
---

# SAPO (Soft Adaptive Policy Optimization)

## Method Overview
SAPO (Soft Adaptive Policy Optimization) introduces soft token-adaptive gating for sparse Mixture-of-Experts (MoE) and Vision-Language (VL) policies (e.g. Qwen3-VL):
1. **Sigmoid Soft Gating**: Employs a sigmoid gate instead of hard clipping, providing smooth token-adaptive bounds.
2. **MoE/VL Optimization**: Prevents policy collapse during long-horizon multimodal and MoE reasoning rollouts without rigid truncation.

## When to Use
- Default SOTA optimizer for mathematical and coding reinforcement learning on MoE and VL architectures (e.g. Qwen MoE / Qwen3-VL / DeepSeek MoE). Supported in ms-swift via `loss_type=sapo`.

## Supersession
- Supersedes `method:gspo` as the primary Qwen MoE/VL algorithm.
