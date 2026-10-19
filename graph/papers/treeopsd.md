---
id: paper:treeopsd
type: paper
title: 'Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning'
authors:
- 'Heming Zou'
- 'Qi Wang'
- 'Yixiu Mao'
- 'Yun Qu'
- 'Yuyi Guo'
- 'Zeyuan Liu'
- 'Chenglin Li'
- 'Weijie Liu'
- 'Saiyong Yang'
- 'Xiangyang Ji'
year: 2026
month: 10
arxiv_id: '2610.23181'
url: https://arxiv.org/abs/2610.23181
methods:
- method:treeopsd
cites:
- paper:canopy
tags:
- agent-rl
- opsd
- tree
- active
---

# TreeOPSD

## Abstract Summary
Reinforcement learning with verifiable rewards has become a scalable post-training paradigm for large language models. However, training agents over long-horizon interactions presents two challenges: using only terminal rewards makes turn-level credit assignment sparse and high-variance, while sequential mini-batch updates on a fixed rollout batch introduce policy staleness as the current policy drifts from the behavior policy. Existing approaches obtain denser credit via learned critics, process reward models, or on-policy distillation, but they rely on a value network, step-level annotations, or a stronger external teacher that increase training complexity. Meanwhile, importance sampling a

## Key Contributions
1. TreeOPSD treats each interaction turn as a tree node, branches alternative continuations from shared prefixes, backs up terminal rewards into turn-level credit, and maps each credit to a bounded teacher parameterized by the likelihood ratio versus the frozen behavior policy.

## Empirical Highlights
- +4.97 vs GRPO

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23181`
- Code: `none found` (`code_status: none`).
