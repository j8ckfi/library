---
id: paper:simhack
type: paper
title: 'SimHack: Predicting the onset of detectable reward hacking before RL training'
authors:
- 'Junwei Deng'
- 'Alex Bie'
- 'Natalia Ponomareva'
year: 2026
month: 10
arxiv_id: '2610.28707'
url: https://arxiv.org/abs/2610.28707
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- rlvr
- gotcha
- reward-hacking
---

# SimHack

## Abstract Summary
SimHack learns reward-hacking onset from a few small RL runs and simulates unseen recipes so you can pick a lower-risk curriculum before a full run. Median onset relative error 11.3%, rank correlation 0.85; a screened curriculum trained 96.6% longer without hacking.

## Key Contributions
1. Pre-run onset predictor for detectable reward hacking; not a train-kernel.

## Empirical Highlights
- Does not retarget CISPO. Initial hacking rate alone does not determine onset.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28707`
- Code: `none found` (`code_status: none`).
