---
id: task:math-code-rl-moe
type: task
title: "Mathematical and Code RL Reasoning (MoE Policies)"
domain: "post-training"
summary: "Reinforcement learning for large-scale sparse Mixture-of-Experts (MoE) reasoning models."
current_sota:
  - method: method:gspo
    as_of: "2026-08-26"
    benchmark: "Qwen3 / MATH-500 / AIME MoE RL"
    metric: "pass@1 accuracy & MoE routing stability"
    value: "SOTA for MoE RL"
    notes: "GSPO uses sequence-level importance sampling ratio to stabilize RL updates when routing is non-stationary."
methods:
  - method:gspo
  - method:dr-grpo
  - method:grpo
tags:
  - post-training
  - reasoning
  - moe
  - gspo
---

# Mathematical and Code RL Reasoning (MoE Policies)

## Problem Definition
Training sparse Mixture-of-Experts policies with reinforcement learning where token-level routing decisions introduce extreme non-stationarity in importance sampling ratios.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **GSPO** (`method:gspo`) with sequence-level importance sampling (IS) ratio (Qwen3 recipe).
- **De-biasing**: Combine with **Dr. GRPO** (`method:dr-grpo`) fixes.
