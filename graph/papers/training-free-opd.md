---
id: paper:training-free-opd
type: paper
title: 'Training-Free On-Policy Distillation'
authors:
- Bangji Yang
- Jiajun Fan
- Zhaoyu Zhu
- Hongbo Ma
- Ge Liu
year: 2026
month: 10
arxiv_id: '2610.22236'
url: https://arxiv.org/abs/2610.22236
methods:
- method:training-free-opd
cites:
- paper:opd
tags:
- distillation
- opd
- model-merge
---

# Training-Free On-Policy Distillation

## Abstract Summary
When specialists share a base, consolidating them is a layer-wise least-squares problem on specialist-input second moments. One forward pass over a few hundred rollouts supplies those moments. No gradients. Truncated repetition-loop answers hurt more than their count suggests.

## Key Contributions
1. Exact layer-wise least-squares fusion of same-base specialists.
2. Forward-only on-policy second moments.
3. Olmo 3 7B math/code specialist merge.

## Empirical Highlights
- Removing repetition-loop answers lifts AIME25 from task-arithmetic level to the specialist at matched precision.
- A few GPU-hours of forwards per specialist keep most of each specialist's gain on seven math and code benches.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22236`
- Code: `none found` (`code_status: none`).

