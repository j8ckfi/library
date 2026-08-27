---
id: paper:sapo
type: paper
title: "SAPO: Sequence-Level Advantage Policy Optimization for MoE Reasoning"
authors:
  - "SAPO Research Authors"
year: 2025
month: 11
arxiv_id: "2511.20347"
url: "https://arxiv.org/abs/2511.20347"
methods:
  - method:sapo
cites:
  - paper:gspo
tags:
  - post-training
  - rl-alignment
  - moe
  - reasoning
  - sapo
---

# SAPO: Sequence-Level Advantage Policy Optimization for MoE Reasoning

## Abstract Summary
SAPO introduces sequence-level advantage normalization and importance sampling for Mixture-of-Experts (MoE) and Vision-Language (VL) reasoning policies, resolving the routing non-stationarity of token-level RL algorithms.

## Key Contributions
1. **Sequence Advantage Normalization**: Stabilizes policy gradients across dynamically routed MoE layers.
2. **MoE/VL SOTA**: Preferred default for Qwen-MoE and multimodal reasoning alignment.

## Open Source Implementation
- Implementation: `ms-swift loss_type=sapo`
