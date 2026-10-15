---
id: paper:latentloop
type: paper
title: 'LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation'
authors:
- Zefeng He
- Yunkai Chai
- Xiaoyang Chen
- Tong Zhu
- Zongliang Wu
- Yun Luo
- Yafu Li
- Yu Cheng
year: 2026
month: 10
arxiv_id: '2610.19975'
url: https://arxiv.org/abs/2610.19975
methods:
- method:latentloop
cites:
- paper:smelt
- paper:elr
tags:
- architecture
- moe
- looped-transformer
---

# LatentLoop

## Abstract Summary
Looped MoE visits play different roles even with shared parameters. Learned residual scales shrink on the first visit. LatentLoop compresses that visit, keeps the second full-res, and reallocates compute to width.

## Key Contributions
1. Asymmetric compute across loop visits.
2. Shared MoE, unshared attention, learned first-visit writeback.
3. 15 configs 1.3B-7B including a >10^21 FLOP point.

## Empirical Highlights
- Fitted NLL 1.988: 19.0% vs MoE Base, 7.9% vs MoE Loop.
- Nine-bench 5-shot +0.73-1.18 vs Loop at all sizes.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19975`
- Code: `none found` (`code_status: none`).
