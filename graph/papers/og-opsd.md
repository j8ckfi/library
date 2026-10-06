---
id: paper:og-opsd
type: paper
title: "Outcome-Guided On-Policy Self-Distillation"
authors:
  - ZheXu Wang
  - Mao-Lin Luo
  - Yankun Hong
  - Zi-Hao Zhou
  - Bo Ye
  - Jian Zhao
  - Xialiang Tong
  - Min-Ling Zhang
  - Tong Wei
year: 2026
month: 10
arxiv_id: "2610.05070"
url: "https://arxiv.org/abs/2610.05070"
methods:
  - method:og-opsd
cites:
  - paper:vista
  - paper:opsd-collapse-review
  - paper:u-opsd
tags:
  - post-training
  - distillation
  - opsd
  - og-opsd
---

# Outcome-Guided On-Policy Self-Distillation

## Abstract Summary
Vanilla OPSD uses a fixed divergence regardless of outcome, under-penalizing and over-rewarding incorrect trajectories. Teacher reliability tracks both outcome and cumulative average teacher entropy. OG-OPSD switches FKL/RKL and the distillation prefix cutoff from binary outcome plus that entropy prefix. Improves vanilla OPSD and several baselines on math, multimodal, and OOD across Qwen3 1.7B/4B/8B and Qwen3-VL-2B. No numeric table in the abstract. Beside VISTA / u-OPSD. No public code as of 2026-10-06.

## Key Contributions
1. **Outcome-aware divergence**: FKL vs RKL from binary correctness.
2. **Entropy prefix cutoff** for where teacher supervision is reliable.
3. **Cross-scale / VL**: Qwen3 1.7B/4B/8B and Qwen3-VL-2B.

## Empirical Highlights
- Abstract: consistently improves vanilla OPSD and multiple strong baselines on math, multimodal, and OOD.
- No specific numeric table in the abstract; do not invent one.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05070`
- Code: none found as of 2026-10-06 (`code_status: none`).
