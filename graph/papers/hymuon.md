---
id: paper:hymuon
type: paper
title: 'Hybrid Momentum Methods for Optimizing Deep Learning Models'
authors:
- 'Haifeng Xu'
- 'Yijin Ren'
- 'Qi Deng'
- 'Chenyu Zhou'
- 'Dongdong Ge'
- 'Yinyu Ye'
year: 2026
month: 10
arxiv_id: '2610.27674'
url: https://arxiv.org/abs/2610.27674
methods:
- method:hymuon
cites:
- paper:muon2
tags:
- optimizer
- muon
- active
---

# Hybrid Momentum Methods for Optimizing Deep Learning Models

## Abstract Summary
HyM mixes a linearly weighted growing-history average with a fast EMA. HyMUON orthogonalizes that hybrid direction with Newton-Schulz.

## Key Contributions
1. Two-timescale hybrid momentum, modular with Muon orthogonalization.

## Empirical Highlights
- LLaMA-1.3B C4 val 2.777 vs Muon 2.903; gains on IWSLT14 and GPT-2 124M OpenWebText.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.27674`
- Code: `none found` (`code_status: none`).
