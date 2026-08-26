---
id: paper:grpo
type: paper
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO Formulation)"
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
  - grpo
---

# DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO Formulation)

## Abstract Summary
Introduces Group Relative Policy Optimization (GRPO), eliminating the value/critic model in RLHF by standardizing advantage scores across sampled response groups.

## Open Source Repositories
- Code: `https://github.com/deepseek-ai/DeepSeek-Math`
- Hugging Face TRL: `GRPOTrainer`
- Framework: `verl`
