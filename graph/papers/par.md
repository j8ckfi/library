---
id: paper:par
type: paper
title: 'PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking'
authors:
- 'Pan Wang'
- 'Yihao Hu'
- 'Guangyuan Dong'
- 'Yitong Lin'
- 'Hang Wang'
- 'Zimi Liu'
- 'Zhihao Wen'
- 'Jianshe Li'
- 'Jiang-Ming Yang'
- 'Wei Wu'
- 'Yongqi Tong'
year: 2026
month: 10
arxiv_id: '2610.27628'
url: https://arxiv.org/abs/2610.27628
methods:
- method:par
cites:
- paper:recurrent-looped-transformer
tags:
- looped-lm
- length-generalization
- active
---

# PAR

## Abstract Summary
PAR trains looped-LM iteration k to match the state after k operations and anchors recurrent-state norms to the first iteration so extra test-time loops track longer sequences.

## Key Contributions
1. Progress-aligned targets plus norm anchoring for looped length generalization.

## Empirical Highlights
- Qwen2.5-0.5B swap-S5 95.5% at 512 moves (16x train) vs RLT 55.7% and CoT 0.8%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27628`
- Code: `none found` (`code_status: none`).
