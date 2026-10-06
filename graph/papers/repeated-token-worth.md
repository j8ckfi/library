---
id: paper:repeated-token-worth
type: paper
title: "What Is a Repeated Token Worth? The Scaling Geometry of Multi-Epoch Pretraining"
authors:
  - Yekun Chai
  - Haoyi Xiong
year: 2026
month: 10
arxiv_id: "2610.05591"
url: "https://arxiv.org/abs/2610.05591"
methods:
  - method:repeated-token-worth
cites:
  - paper:olmo-3
tags:
  - pretraining
  - data-curriculum
  - data-repetition
  - repeated-token-worth
---

# What Is a Repeated Token Worth? The Scaling Geometry of Multi-Epoch Pretraining

## Abstract Summary
Prices a repeated token against one epoch on the same data (value) and fresh data at equal compute (cost). Cost of repetition collapses to extra epochs divided by unique tokens per parameter. A second epoch is worth nearly as much as a fresh one; repeated tokens fall to half the value of fresh ones after a critical epoch count that grows with training budget per parameter but hardly with model size. With unique data fixed, larger models tolerate fewer epochs (~15 at 127M to ~4 at 2B). Counts alone do not determine loss: consecutive shard replay can raise loss by up to 0.46 bits/byte. Dual-active first hop on task:data-constrained-pretrain. No public code as of 2026-10-06.

## Key Contributions
1. **Single cost variable**: extra epochs / unique tokens per parameter vs fresh data.
2. **Value curve**: second epoch nearly as valuable as fresh; half-value at a critical epoch that tracks budget/param, not size.
3. **Fixed-U size trend**: ~15 epochs at 127M to ~4 at 2B when unique data are fixed.

## Empirical Highlights
- Second epoch nearly as valuable as a fresh token on the same data.
- Repeated tokens fall to half the value of fresh ones after the critical epoch.
- Fixed unique data: ~15 epochs at 127M to ~4 at 2B.
- Consecutive shard replay: up to +0.46 bits/byte vs shuffled repeats.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05591`
- Code: none found as of 2026-10-06 (`code_status: none`).
