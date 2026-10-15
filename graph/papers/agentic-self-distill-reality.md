---
id: paper:agentic-self-distill-reality
type: paper
title: 'More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning'
authors:
- Linhao Zhong
- Bozhen Fang
- Xuehao Wang
- Duochao Shi
- Zekai Luo
- Guangming Yao
- Yi Yuan
- Hao Chen
- Jingdong Chen
- Chunhua Shen
year: 2026
month: 10
arxiv_id: '2610.19789'
url: https://arxiv.org/abs/2610.19789
methods:
- method:canopy
cites:
- paper:canopy
- paper:opd
tags:
- post-training
- agentic
- self-distillation
- gotcha
---

# Reality check on self-distillation in agentic RL

## Abstract Summary
Ten self-distillation methods vs GRPO on ALFWorld, ScienceWorld, Search-QA, and WebShop across three sizes. 132 runs, 12124.4 H800 GPU-hours, eight eval seeds. No method consistently beats GRPO. Strong finals can hide unstable training. Extra GPU-hours do not reliably buy gains. Does not retarget CANOPY, SAO, or CISPO.

## Key Contributions
1. Common-protocol bake-off instead of reused published scores.
2. Stability and cost, not only final task score.
3. Negative result: self-distill plug-ins are not a free upgrade on these agent benches.

## Empirical Highlights
- No method consistently outperforms GRPO across settings.
- Cost does not track gains.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19789`
- Code: `none found` (`code_status: none`).
