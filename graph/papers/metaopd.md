---
id: paper:metaopd
type: paper
title: "MetaOPD: Meta-Learned Token Weighting for On-Policy Distillation"
authors:
  - "Zipeng Wang"
  - "Xinpeng Dong"
  - "Yuefan Wang"
  - "Pingchen Lu"
  - "Xian Wei"
  - "Kun Kuang"
  - "Fei Wu"
  - "Zhongxiang Dai"
  - "Min Zhang"
year: 2026
month: 10
arxiv_id: "2610.11989"
url: "https://arxiv.org/abs/2610.11989"
methods:
  - method:metaopd
cites:
  - paper:opd
  - paper:ier-opd
  - paper:sparse-opd-supervision
tags:
  - post-training
  - distillation
  - opd
  - token-weighting
  - metaopd
---

# MetaOPD: Meta-Learned Token Weighting for On-Policy Distillation

## Abstract Summary
Uniform OPD token weights miss learning-value differences. Static proxies (entropy, disagreement) use a frozen map from prediction signals to weights. MetaOPD jointly trains the student and a lightweight weighting network: inner weighted OPD, outer validation loss after a virtual student update. Avg@8/Pass@8 vs OPD: +1.99/+5.97 (0.6B) and +2.25/+6.41 (1.7B) across six math and three OOD sets, seven baselines. Beside IER-OPD / sparse OPD. No official GitHub as of 2026-10-09.

## Key Contributions
1. Bilevel token weighting: outer validation loss after a virtual weighted OPD update.
2. Weighting network maps a 74-d detached descriptor (logp, entropy, agreement, position, top-32 profiles) to residual unit-mean weights.
3. Beats uniform OPD and static proxy weighting (EOPD / TIP) on two student scales.

## Empirical Highlights
- 0.6B student Avg@8/Pass@8 +1.99/+5.97 vs OPD.
- 1.7B student Avg@8/Pass@8 +2.25/+6.41 vs OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11989`
- Code: none found as of 2026-10-09 (`code_status: none`).
