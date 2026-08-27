---
id: task:math-code-rl-moe
type: task
title: "Mathematical and Code RL Reasoning (MoE Policies)"
domain: "post-training"
summary: "Reinforcement learning for large-scale sparse Mixture-of-Experts (MoE) reasoning models."
current_sota:
  - method: method:sapo
    as_of: "2026-08-26"
    benchmark: "Qwen3 MoE / MATH-500 MoE RL"
    metric: "pass@1 accuracy & MoE routing stability"
    value: "Default SOTA for MoE/VL RL"
    notes: "SAPO (2511.20347); GSPO only if Qwen3.5-Omni Talker."
methods:
  - method:sapo
  - method:gspo
  - method:qwen35-omni
  - method:dr-grpo
  - method:grpo
tags:
  - post-training
  - reasoning
  - moe
  - sapo
---

# Mathematical and Code RL Reasoning (MoE Policies)

## Problem Definition
Training sparse Mixture-of-Experts policies with reinforcement learning where dynamic expert routing introduces variance in token-level importance weights.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **SAPO** (`method:sapo`, 2511.20347, ms-swift `loss_type=sapo`).
- **Omni / Talker**: **GSPO** (`method:gspo`) only if training Qwen3.5-Omni Talker (`paper:qwen35-omni`).
