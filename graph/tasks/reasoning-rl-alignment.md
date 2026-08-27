---
id: task:reasoning-rl-alignment
type: task
title: "Reinforcement Learning & Reasoning Post-Training"
domain: "post-training"
summary: "Aligning foundation language models with rule-based verifiers and group-relative policy optimization for long-horizon mathematical and code reasoning."
current_sota:
  - method: method:cispo
    as_of: "2026-08-26"
    benchmark: "AIME 2024 / MATH-500"
    metric: "pass@1 accuracy"
    value: "SOTA for Dense Long-CoT"
    notes: "CISPO for dense policies (2506.13585, 2510.13786); SAPO for MoE/VL (2511.20347)."
  - method: method:sapo
    as_of: "2026-08-26"
    benchmark: "Qwen MoE / VL Reasoning"
    metric: "pass@1 accuracy"
    value: "SOTA for MoE/VL RL"
    notes: "SAPO (2511.20347) for MoE and Vision-Language policies."
methods:
  - method:cispo
  - method:sapo
  - method:dapo
  - method:gspo
  - method:cppo
  - method:dr-grpo
  - method:grpo
  - method:ppo-rlhf
tags:
  - post-training
  - reinforcement-learning
  - reasoning
---

# Reinforcement Learning & Reasoning Post-Training

## SOTA Recommendation (as of 2026-08-26)
- **Dense Policies**: **CISPO** (`method:cispo`).
- **MoE / VL Policies**: **SAPO** (`method:sapo`).
- **Process Supervision**: **VeriGate** (`method:verigate`, 2605.30451).
