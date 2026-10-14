---
id: paper:scaling-repeated-data
type: paper
title: 'Scaling Repeated-Data Pretraining: Batch Size, Regularization, and GPU-Time Tradeoffs'
authors:
- Sewon Min
year: 2026
month: 10
arxiv_id: '2610.15965'
url: https://arxiv.org/abs/2610.15965
methods:
- method:scaling-repeated-data
cites:
- paper:repeated-token-worth
tags:
- pretraining
- data-constrained
- batch-size
- regularization
---

# Scaling Repeated-Data Pretraining

## Abstract Summary
Multi-epoch dense pretrain under a finite unique-token budget. Loss vs batch size is U-shaped. Smaller batches, per-epoch sequence repacking, weight tying, and positive embedding weight decay extend the useful epoch budget. GPU-time vs quality is an explicit tradeoff.

## Key Contributions
1. U-shaped CE vs batch size under multi-epoch (not the single-epoch large-batch rule).
2. Tying + embedding WD plus per-epoch packing as the paper's regularization stack.
3. Epoch-budget extension: 20→32 (1.5B) and 112→240 (153M) before overfitting.

## Empirical Highlights
- 1.5B: B=64 vs B=512 CE 3.124→2.977; tying+emb WD 2.971→2.946 at B=64 (single-paper).
- Smaller batches cost GPU-time; packing recovers some of that.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.15965`
- Code: `none found` (`code_status: none`).
