---
id: method:gspo
type: method
title: "GSPO (Group Sequence Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-moe
supersedes:
  - method:grpo
papers:
  - paper:gspo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "Qwen3 MoE Reasoning RL"
    metric: "pass@1 accuracy"
    value: "State of the art on MoE reasoning RL"
    baseline: "Token-level GRPO"
    date: "2025-07"
    verified: true
    notes: "Sequence-level importance sampling ratio to stabilize RL policy updates under dynamic expert routing."
tags:
  - rl-alignment
  - reasoning
  - moe
  - gspo
---

# GSPO (Group Sequence Policy Optimization)

## Method Overview
GSPO replaces token-level importance sampling (IS) with a sequence-level importance sampling ratio. In sparse MoE models, token-level routing probabilities change rapidly across gradient steps, causing extreme variance and divergence in token-level IS ratios. GSPO stabilizes policy gradient updates across dynamically routed architectures.

## When to Use
- Default reinforcement learning optimizer when policy is a Mixture-of-Experts (e.g. Qwen3 / DeepSeek MoE).

## Supersession
- Supersedes token-level IS methods (like vanilla GRPO) when training MoE policies.
