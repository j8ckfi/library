---
id: paper:ap-opd
type: paper
title: 'Adaptive Pullback: Reweighting Supervision at Penalty Jumps in On-Policy Distillation'
authors:
- 'Guangyu Liu'
- 'Siyuan Gan'
- 'Shilong Zhou'
- 'Linjian Meng'
- 'Boyan Wang'
- 'Jing Huo'
year: 2026
month: 10
arxiv_id: '2610.28194'
url: https://arxiv.org/abs/2610.28194
methods:
- method:ap-opd
cites:
- paper:opd
tags:
- distillation
- opd
- active
---

# Adaptive Pullback

## Abstract Summary
AP-OPD detects persistent penalty jumps in sampled-token OPD, then scales the next block's coefficients so its weighted penalty matches the previous block mean, without an extra strength constant.

## Key Contributions
1. Block-wise pullback at penalty-confidence tension.

## Empirical Highlights
- Improves math and code OPD vs ordinary sampled-token OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28194`
- Code: `none found` (`code_status: none`).
