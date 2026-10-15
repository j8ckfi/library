---
id: paper:pmrc
type: paper
title: 'Memory-Efficient Subspace Optimization with Residual Correction: From Momentum SGD to Muon'
authors:
- Sifan Yang
- Hongyi Tao
- Dingzhi Yu
- Haomin Bai
- Wei Jiang
- Silin Gao
- Pi Bu
- Lijun Zhang
year: 2026
month: 10
arxiv_id: '2610.19844'
url: https://arxiv.org/abs/2610.19844
methods:
- method:pmrc
cites:
- paper:galore
- paper:scale
- paper:muon2
tags:
- optimizer
- memory-efficient
- muon
- pretraining
---

# PMRC / SMRC residual-correction subspace

## Abstract Summary
GaLore-style leading singular subspaces can be noise-dominated late in training. Residual correction keeps optimizer states in the subspace and adds the orthogonal residual to the update. SMRC is momentum SGD; PMRC is projected Muon. Both get O(T^{-1/4}) matching full-space rates.

## Key Contributions
1. Subspace virtual iterate for SMRC; weighted momentum tracking for PMRC.
2. Multi-stage basis refresh with boundary correction.
3. LLaMA C4 60M-1.3B vs GaLore / GoLore / Fira / GUM.

## Empirical Highlights
- 1.3B train 2.500 vs Fira 2.657 vs GaLore 2.842; val 2.570 vs 2.730 vs 2.875.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19844`
- Host: `https://github.com/OptimAI-Lab/Minimalist_LLM_Pretraining` (not a dedicated PMRC repo; `code_status: none`).
