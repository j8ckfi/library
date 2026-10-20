---
id: paper:nvfp4-pretrain-recipe
type: paper
title: 'What Matters for NVFP4 Training? A Comparative Study of Low-Precision Pretraining Recipes'
authors:
- 'Anjulie Agrusa'
- 'Andrei Panferov'
- 'Elizabeth Wei'
- 'Keith Wyss'
- 'Paul Gibbons'
- 'Erik Schultheis'
- 'Jinhang Choi'
- 'Frank Sun'
- 'Tijmen Blankevoort'
- 'Dan Alistarh'
year: 2026
month: 10
arxiv_id: '2610.24343'
url: https://arxiv.org/abs/2610.24343
methods:
- method:nvfp4-pretrain-recipe
cites:
- paper:quartet-ii
tags:
- quantization
- nvfp4
- pretrain
- active
---

# NVFP4 Pretrain Recipe

## Abstract Summary
Compares NVFP4 pretrain ingredients on Nemotron dense 8B and 30B-A3B MoE up to 1T tokens. The stacked recipe uses unbiased gradient estimation with lower error than stochastic rounding and keeps selective high-precision layers. Claimed strongest FP4 loss gap to BF16 at this scale.

## Key Contributions
1. Ablation of which NVFP4 recipe knobs survive medium-scale, long-horizon pretrain.

## Empirical Highlights
- Not all backward tensors benefit equally from de-biasing. ICML 2026 AdaptFM workshop.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24343`
- Code: `none found` (`code_status: none`).
