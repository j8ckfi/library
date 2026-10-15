---
id: paper:cast-ssc
type: paper
title: 'CAST: History-Adaptive Spectral Clipping for LLM Pretraining'
authors:
- Jiacheng Li
- Jianchao Tan
- Kefeng Zhang
- Yuchen Xie
- Xunliang Cai
year: 2026
month: 10
arxiv_id: '2610.19761'
url: https://arxiv.org/abs/2610.19761
methods:
- method:cast-ssc
cites:
- paper:muon2
- paper:musec
tags:
- pretraining
- optimizer
- spectral-clipping
---

# CAST (History-Adaptive Spectral Clipping)

## Abstract Summary
Soft spectral clipping depends on gradient scale and threshold. CAST uses AdamW's previous second moment for row/column scales and an EMA of the clipped spectral norm as the threshold, then restores coordinates before AdamW. Distinct from CAST cross-tokenizer OPD (`paper:cast`).

## Key Contributions
1. Historical scaling from AdamW V plus output-feedback threshold EMA around pre-optimizer SSC.
2. 19.08B MoE / 83.89B tokens / 5000-step bake-off vs nine gradient-processing baselines.
3. Fewest relative gradient spikes among the compared clippers.

## Empirical Highlights
- Mean val loss 1.26e-2 below SSC-constant and 2.10e-2 below SSC-cosine (20 subsets).
- Reaches AdaGC final smoothed train loss at step 4639 (7.2% fewer steps); estimated 5.5% less time vs 5000 ClipByValue.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19761`
- Code: `none found` (`code_status: none`).
