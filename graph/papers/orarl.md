---
id: paper:orarl
type: paper
title: "Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs"
authors:
  - "Yunheng Li"
  - "Guohong Mu"
  - "Hao Li"
  - "Shengsheng Qian"
  - "Dingwen Zhang"
  - "Qibin Hou"
  - "Ming-Ming Cheng"
year: 2026
month: 8
arxiv_id: "2608.20492"
url: "https://arxiv.org/abs/2608.20492"
methods:
  - method:orarl
cites:
  - paper:grpo
  - paper:sapo
tags:
  - video-mllm
  - multimodal-rl
  - post-training
  - orarl
---

# Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs

## Abstract Summary
OraRL establishes an efficient reinforcement learning paradigm for video multimodal large language models (MLLMs) by treating dataset annotations directly as oracle rollouts within the on-policy group. To prevent the high-reward oracle from distorting the advantage baseline and suppressing high-quality exploratory rollouts (advantage inversion), OraRL decouples the advantage baseline to depend solely on on-policy samples while applying sign-balanced pruning. Evaluated across seven video task families, Video-ORA-9B achieves state-of-the-art results across TimeLens, GOT-10k, RefCOCO, and VSI-Bench without chain-of-thought overhead, requiring only 2.2x the step time of SFT (compared to 4.9x for GRPO with CoT).

## Key Contributions
1. **Annotation-as-Rollout Principle**: Incorporates dataset annotations directly as oracle rollouts in the candidate group to provide reliable positive optimization anchors for sample-starved video tasks.
2. **Decoupled Advantage Estimation**: Resolves advantage inversion by computing the group baseline strictly over on-policy rollouts and treating the oracle as a detached optimization target.
3. **Sign-Balanced Pruning**: Selectively backpropagates through the oracle and top rollouts of each advantage sign, yielding a 1.48x speedup over full-group backprop and enabling direct answer decoding in 130 ms.

## Open Source Repository
- Implementation: `https://github.com/HVision-NKU/OraRL`
