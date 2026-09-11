---
id: paper:moe-data-repetition
type: paper
title: "Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data"
authors:
  - "Atindra Jha"
  - "Margaret Li"
  - "Jure Leskovec"
  - "Percy Liang"
  - "Luke Zettlemoyer"
year: 2026
month: 9
arxiv_id: "2609.11917"
url: "https://arxiv.org/abs/2609.11917"
methods:
  - method:moe-data-repetition
cites: []
tags:
  - pretraining
  - moe
  - data-repetition
  - overfitting
---

# Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data

## Abstract Summary
Repeating pretrain data is now standard as unique text runs out. Prior repetition studies were dense. Across 80M–1B active (up to 8.5B total) MoEs, sparse models degrade faster under repetition than dense models, and the effect tracks total (not active) parameters. Dense 80M models tolerate 8× repeats with little damage; MoEs start hurting at 4× and underperform dense after 32×. Dropout and strong masking-based regularization can let MoEs beat dense even past 64×, but nothing matches all-unique data. Routing stabilizes early; expert specialization correlates with overfitting. Niche gotcha, not an architecture default.

## Key Contributions
1. **MoEs overfit repeated data faster than dense**, scaling with total parameters / sparsity.
2. **4× vs 8×**: MoE pain starts earlier than dense.
3. **Regularization helps but does not recover unique-data performance.**

## Empirical Highlights
- 80M dense: 8× repeats with minimal degradation. MoEs: damage from 4×; collapse vs dense by 32×.
- Masking-based regularization: MoEs can still beat dense past 64× repeats, below the all-unique curve.

## Open Source Repository & Resources
- No official code as of 2026-09-11.
