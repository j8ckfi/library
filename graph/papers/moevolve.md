---
id: paper:moevolve
type: paper
title: 'A Stronger Teacher Within: Strengthening MoE Models via On-Policy Bidirectional Distillation'
authors:
- 'Haoyu Chen'
- 'Jun Bai'
- 'Yang Liu'
- 'Jianfei Zhang'
- 'Wenge Rong'
year: 2026
month: 10
arxiv_id: '2610.23185'
url: https://arxiv.org/abs/2610.23185
methods:
- method:moevolve
cites:
- paper:sapo
- paper:opd
tags:
- moe
- opd
- rlvr
- active
---

# MoEvolve

## Abstract Summary
Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved Mixture-of-Experts (MoE) LLMs, but its outcome-level rewards provide only sparse supervision. On-Policy Distillation offers dense token-level feedback, yet requires a stronger compatible teacher, while on-policy self-distillation relies on hand-designed privileged information. We observe that the MoE architecture itself offers a way to resolve this dilemma, as increasing the activation budget per token exposes latent expert capacity and yields a potentially stronger teacher within the model. However, naive expansion degrades performance because newly co-activated experts are not optimized to work together. We th

## Key Contributions
1. MoEvolve first restores an activation-expanded high-k MoE and strengthens it, then reverse-distills those capabilities into the original low-k routing so inference keeps the original activation budget.

## Empirical Highlights
- up to +22.2 vs initial; up to +6.5 vs same-budget RLVR; final low-k often beats the expanded teacher

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23185`
- Code: `none found` (`code_status: none`).
