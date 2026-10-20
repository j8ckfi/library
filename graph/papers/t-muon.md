---
id: paper:t-muon
type: paper
title: 'T-MUON: Tensorizing Muon via t-SVD for Large Language Model Pre-training'
authors:
- 'Dongyang Li'
- 'Mingsong Yan'
- 'Zheng Zhang'
- 'Sui Tang'
year: 2026
month: 10
arxiv_id: '2610.24938'
url: https://arxiv.org/abs/2610.24938
methods:
- method:t-muon
cites:
- paper:muon2
tags:
- optimizer
- muon
- active
---

# T-MUON

## Abstract Summary
Muon orthogonalizes each matrix independently. T-MUON groups related Transformer gradients into third-order tensors and defines the update through the M-transform / t-SVD. Head-wise identity-transform t-Muon records the lowest FineWeb val PPL among AdamW, Muon, and DFT/DCT/DST variants from 51M to 1.3B.

## Key Contributions
1. t-SVD Muon update that is steepest descent under the star_M-spectral norm.

## Empirical Highlights
- 51M-1.3B GPT-2 and LLaMA-style FineWeb / FineWeb-Edu; longer context and token-budget checks.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24938`
- Code: `none found` (`code_status: none`).
