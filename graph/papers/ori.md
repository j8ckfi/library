---
id: paper:ori
type: paper
title: 'Ori: Drift-Aware Streaming k-PCA for Very Low-Rank LLM Training'
authors:
- 'Xinyu Luo'
- 'Jincheng Zhou'
- 'Mengbo Wang'
- 'Zilin Shen'
- 'Nadia Atallah Lanman'
- 'Petros Drineas'
- 'Bruno Ribeiro'
- 'Brian Bullins'
year: 2026
month: 10
arxiv_id: '2610.22794'
url: https://arxiv.org/abs/2610.22794
methods:
- method:ori
cites:
- paper:galore
- paper:scale
tags:
- optimizer
- low-rank
- galore
- active
---

# Ori

## Abstract Summary
A prominent family of low-rank LLM optimizers, pioneered by GaLore, performs gradient-subspace projection: at each step, they project the gradient into a low-dimensional subspace and map the update back to the full model. Most existing work either recomputes the gradient subspace at certain intervals, or performs post-hoc adaptation to catch up to the moving subspace. In this work, we explicitly identify in practice the slow, stable manner in which LLM gradient subspaces drift across time. To this end, we propose Ori, a novel low-rank optimizer for training LLMs that captures the shifting principal gradient directions over time to achieve state-of-the-art accuracy under stringent low-rank co

## Key Contributions
1. Ori tracks drifting LLM gradient principal directions with a streaming k-PCA (Oja++) update so the projection subspace stays current without expensive periodic SVDs.

## Empirical Highlights
- up to 69.3% gap cut vs prior low-rank optimizers on 1B; best on 10/16 RoBERTa-Base scenarios

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22794`
- Code: `none found` (`code_status: none`).
