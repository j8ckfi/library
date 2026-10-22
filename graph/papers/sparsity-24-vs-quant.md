---
id: paper:sparsity-24-vs-quant
type: paper
title: 'Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference'
authors:
- 'Xiuyi Qin'
year: 2026
month: 10
arxiv_id: '2610.28947'
url: https://arxiv.org/abs/2610.28947
methods:
- method:quartet-ii
cites:
- paper:quartet-ii
tags:
- sparsity
- quantization
- gotcha
---

# Is 2

## Abstract Summary
At equal bits (sparsity metadata counted) and equal tensor-core tiers, adding 2:4 sparsity is the worse next step whenever a lower precision exists: less accurate and slower, because 2:4 discards energy no remaining bits recover.

## Key Contributions
1. Equal-bit 2:4 vs next-lower-precision decision rule for inference.

## Empirical Highlights
- Code PuppyQ08/24_quant_compare. Does not retarget Quartet-II. Retraining can win 2:4 quality back, which is a different budget.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28947`
- Code: `https://github.com/PuppyQ08/24_quant_compare` (`code_status: released`).
