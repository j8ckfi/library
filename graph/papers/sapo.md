---
id: paper:sapo
type: paper
title: "SAPO: Soft Adaptive Policy Optimization for MoE Reasoning"
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

# SAPO: Soft Adaptive Policy Optimization for MoE Reasoning

## Abstract Summary
SAPO (Soft Adaptive Policy Optimization) introduces soft token-adaptive gating via a sigmoid function instead of rigid hard clipping for Mixture-of-Experts (MoE) and Vision-Language (VL) reasoning policies, preventing optimization collapse and routing degradation.

## Key Contributions
1. **Sigmoid Soft Gating**: Replaces hard clip boundaries with smooth, token-adaptive sigmoid bounds.
2. **MoE/VL SOTA**: Preferred default for Qwen-MoE and multimodal reasoning alignment (ms-swift `loss_type=sapo`).

## Open Source Implementation
- Implementation: `ms-swift loss_type=sapo`
