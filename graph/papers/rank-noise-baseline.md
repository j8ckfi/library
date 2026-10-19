---
id: paper:rank-noise-baseline
type: paper
title: 'Rank Measures of Fine-Tuning Updates Need a Noise Baseline'
authors:
- 'Muhammad Usman Altaf'
year: 2026
month: 10
arxiv_id: '2610.22438'
url: https://arxiv.org/abs/2610.22438
methods:
- method:lr-matters-lora
cites:
- paper:lr-matters-lora
tags:
- peft
- lora
- gotcha
---

# Rank Measures of Fine-Tuning Updates Need a Noise Baseline

## Abstract Summary
Rank summaries of fine-tuning ΔW are compared to a same-shape random matrix, pretrained weights, and matched fine-tunes without alignment content. Direction-counting ranks sit only a little below noise; stable rank, from the same singular values, sits far below. The pattern holds for thirteen released pairs up to 8B and is not a mark of alignment: with training held fixed, instruct and non-instruct updates look the same.

## Key Contributions
1. Noise baseline for rank-of-update claims.
2. Stable rank vs counting-rank disagreement (few strong directions plus a long tail).
3. Alignment content is not what makes the update look low-rank.

## Empirical Highlights
- Do not cite raw ΔW rank as evidence of LoRA-like structure without a noise/stable-rank baseline.
- Does not retarget vanilla LoRA + rsLoRA + LR sweep.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22438`
- Code: `none found` (`code_status: none`).
