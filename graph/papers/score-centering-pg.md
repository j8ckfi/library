---
id: paper:score-centering-pg
type: paper
title: 'Baselines and Score Centering in Policy Gradient Estimation'
authors:
- Shuo Han
- Ziqing Hu
year: 2026
month: 10
arxiv_id: '2610.22263'
url: https://arxiv.org/abs/2610.22263
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- rlvr
- gotcha
---

# Baselines and score centering in policy gradients

## Abstract Summary
Under regularized importance sampling, the importance-weighted policy gradient is no longer invariant to constant reward shifts. Using the covariance between reward and importance-weighted score recovers that invariance. Group-mean baselines subtract a sample mean; score centering subtracts a population mean. With sequence-level IS, score centering adds nothing once the group-mean baseline is used. With token-level IS, a group-mean baseline without score centering is generally biased when the ratio is regularized.

## Key Contributions
1. Covariance estimand for regularized IS policy gradients.
2. Sample vs population centering distinction.
3. Sequence-level vs token-level IS interaction.

## Empirical Highlights
- Theory/note; practice implication for GRPO/CISPO-family trainers that clip, mask, or truncate IS.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22263`
- Code: `none found` (`code_status: none`).

