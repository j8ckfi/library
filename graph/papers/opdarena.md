---
id: paper:opdarena
type: paper
title: 'OPDArena: Understanding Learning and Forgetting in On-Policy Distillation'
authors:
- 'Yuanze Xu'
- 'Tianzhu Ye'
- 'Hui Sun'
- 'Wenhui Wang'
- 'Li Dong'
- 'Furu Wei'
year: 2026
month: 10
arxiv_id: '2610.25651'
url: https://arxiv.org/abs/2610.25651
methods:
- method:opd
cites:
- paper:opd
tags:
- distillation
- opd
- gotcha
---

# OPDArena

## Abstract Summary
OPDArena compares SFT, RLVR, and OPD across five pretrained models and teacher sources. Teacher choice dominates retention: RLVR-trained teachers improve the target task while keeping prior skills; SFT-trained teachers cause more forgetting. Self-OPD from an RLVR teacher reproduces the retention pattern. Code StellarCurtain/OPDArena.

## Key Contributions
1. Learning vs forgetting protocol for OPD teacher sources.

## Empirical Highlights
- Do not pick an SFT teacher for OPD if retention matters. Does not retarget OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25651`
- Code: `https://github.com/StellarCurtain/OPDArena` (`code_status: released`).
