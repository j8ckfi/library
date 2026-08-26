---
id: paper:gated-sae-paper
type: paper
title: "Improving Dictionary Learning with Gated Sparse Autoencoders"
authors:
  - "Senthooran Rajamanoharan"
  - "Arthur Conmy"
  - "Lewis Smith"
  - "Vikrant Varma"
  - "Janos Kramar"
  - "Rohin Shah"
year: 2024
month: 4
arxiv_id: "2404.16014"
url: "https://arxiv.org/abs/2404.16014"
methods:
  - method:gated-sae
cites:
  - paper:standard-sae-paper
tags:
  - interpretability
  - mechanistic
  - sae
---

# Improving Dictionary Learning with Gated Sparse Autoencoders

## Abstract Summary
Gated Sparse Autoencoders address the fundamental shrinkage issue present in standard \(L_1\)-penalized SAEs by separating the task of identifying which features are active (gating) from estimating their magnitudes (magnitude pathway). The resulting Gated SAEs achieve strictly superior Pareto frontiers of reconstruction fidelity versus sparsity across large foundation models like Gemma-2 and Claude.

## Key Contributions
1. **Shrinkage Analysis**: Mathematically formulated the downward bias of \(L_1\) penalties in dictionary learning.
2. **Gated Architecture**: Decoupled feature detection gate from linear magnitude projection.
3. **Pareto Dominance**: Outperformed standard SAEs across multiple model layers and sparsity levels.
