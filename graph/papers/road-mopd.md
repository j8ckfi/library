---
id: paper:road-mopd
type: paper
title: 'Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation'
authors:
- Shi-Yu Tian
- Yong Liu
- Ximan Liu
- Tianrui Zhu
- Sule Bai
- Xinwei Yang
- Ruiqi Liu
- Kun-Yang Yu
- Ming Yang
- Zhi Zhou
- Yu-Feng Li
- Yipeng Sun
- Gu Simiu
year: 2026
month: 10
arxiv_id: '2610.13521'
url: https://arxiv.org/abs/2610.13521
methods:
- method:road-mopd
cites:
- paper:open-mopd
- paper:opd
- paper:pmopd
tags:
- distillation
- mopd
- multi-teacher
---

# Road MOPD (Cross-Teacher Guarding)

## Abstract Summary
Domain-routed MOPD still updates shared parameters from every domain. When teachers disagree in style, medical accuracy falls below single-domain OPD. Road MOPD uses non-routed teachers as critics on the same trajectories for token credit and preventive gradient projection.

## Key Contributions
1. Failure mode: high-conflict medical x math/code joint training.
2. Cross-teacher agreement token weights plus preventive projection.
3. Qwen3-4B/1.7B 11-task math/code/medical bake-off.

## Empirical Highlights
- High-conflict Medical +5.6-8.8pp vs Vanilla MOPD.
- Qwen3-4B Math x Medical All 47.92 vs ExOPD 45.53.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13521`
- Code: `none found` (`code_status: none`).
- HF Daily 2026-10-15 top paper.
