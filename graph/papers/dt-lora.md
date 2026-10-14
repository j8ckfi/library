---
id: paper:dt-lora
type: paper
title: 'DT-LoRA: Reaching Beyond the Tangent Space of Low-Rank Adaptation'
authors:
- Yangming Zhang
- Ling Yi
- Datong Li
- Jinliang Ding
- Xiaojie Wang
- Tiecheng Song
- Zhaolong Ning
year: 2026
month: 10
arxiv_id: '2610.17730'
url: https://arxiv.org/abs/2610.17730
methods:
- method:dt-lora
cites:
- paper:lr-matters-lora
tags:
- peft
- lora
- tangent-space
---

# DT-LoRA

## Abstract Summary
Split LoRA rank into a stable branch and a dynamic branch that captures residual gradient directions outside LoRA's tangent space via matrix-free randomized SVD. Does **not** supersede vanilla LoRA + rsLoRA + LR sweep. GitHub Snipine/DT-LoRA is an empty-ish stub (`code_status: announced`).

## Key Contributions
1. Residual-gradient SVD branch outside the LoRA tangent.
2. VTAB-1K and COCO vs LoRA (single-paper).
3. ρ 85.4–96.9% of residual energy outside the tangent.

## Empirical Highlights
- ρ 85.4–96.9% outside tangent.
- VTAB-1K 76.2 vs LoRA 75.7.
- COCO r=16 avg 46.6 (+8.2 vs LoRA).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17730`
- Code: `https://github.com/Snipine/DT-LoRA` (`code_status: announced`; README/hashes only as of 2026-10-14).
