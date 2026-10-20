---
id: paper:echo-mtp
type: paper
title: 'ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction'
authors:
- 'Yuxuan Zhou'
- 'Junyuan Shang'
- 'Tianyu Wang'
- 'Chunrui Zheng'
- 'Zichang Liu'
- 'Wenbin Chang'
- 'Shuohuan Wang'
- 'Dianhai Yu'
year: 2026
month: 10
arxiv_id: '2610.24766'
url: https://arxiv.org/abs/2610.24766
methods:
- method:echo-mtp
cites:
- paper:uno
tags:
- architecture
- mtp
- active
---

# ECHO

## Abstract Summary
Auxiliary MTP trains extra modules. ECHO supervises every horizon with the backbone final layer and uses Dynamic Depth Sampling so longer horizons stay cheap. ECHO-1.5(3) matches ECHO-3 at half MTP overhead. Drafting with pretrained weights avoids post-hoc drafter overfit.

## Key Contributions
1. Causal self-recursion MTP plus decaying-depth sampling.

## Empirical Highlights
- Deeper supervision continues to help where DeepSeek-style MTP plateaus.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24766`
- Code: `none found` (`code_status: none`).
