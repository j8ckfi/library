---
id: paper:deepseek-math-paper
type: paper
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
authors:
  - "Zhihong Shao"
  - "Peiyi Wang"
  - "Qihao Zhu"
  - "Runxin Xu"
  - "Junxiao Song"
  - "Xiao Bi"
  - "Haowei Zhang"
  - "Mingchuan Zhang"
year: 2024
month: 2
arxiv_id: "2402.03300"
url: "https://arxiv.org/abs/2402.03300"
methods:
  - method:grpo
cites:
  - paper:ppo-paper
tags:
  - post-training
  - reasoning
  - mathematics
---

# DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

## Abstract Summary
DeepSeekMath introduces Group Relative Policy Optimization (GRPO) to train open foundation models on complex mathematical reasoning. By eliminating the memory and compute overhead of separate critic networks through group-standardized advantage estimation, GRPO allows large-scale reinforcement learning with rule-based outcome verifiers, setting new open-source mathematical reasoning records.

## Key Contributions
1. **GRPO Algorithm**: Formulated group-relative baseline estimation for RLHF without critic models.
2. **Mathematical Corpus Pretraining**: Curated a 120B token math pretraining dataset (DeepSeekMath Corpus).
3. **Outcome Reward Verification**: Validated pure correctness scoring for multi-step reasoning rollouts.
