---
id: paper:normtune
type: paper
title: 'NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks'
authors:
- 'Zhangming Li'
- 'Qinghao Hu'
- 'Weifan Guan'
- 'Yifan Zhang'
- 'Peisong Wang'
- 'Jian Cheng'
year: 2026
month: 10
arxiv_id: '2610.29134'
url: https://arxiv.org/abs/2610.29134
methods:
- method:normtune
cites:
- paper:lr-matters-lora
tags:
- peft
- lora
- active
---

# NormTune

## Abstract Summary
NormTune watches per-layer weight-update norms during PEFT and adaptively strengthens layers that stay far below full-FT update scale, which the paper ties to reasoning-token under-adaptation.

## Key Contributions
1. NormTune as an active plug-in on `task:lora-quality-tuning`.

## Empirical Highlights
- +24.24 / +11.33 / +16.21 vs LoRA / Bone / MoRA; rank-256 hosts still gain +2.17 / +0.93 / +3.00. Does not retarget `method:lr-matters-lora`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29134`
- Code: `none found` (`code_status: none`).
