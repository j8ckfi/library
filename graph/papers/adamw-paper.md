---
id: paper:adamw-paper
type: paper
title: "Decoupled Weight Decay Regularization"
authors:
  - "Ilya Loshchilov"
  - "Frank Hutter"
year: 2019
month: 1
arxiv_id: "1711.05101"
url: "https://arxiv.org/abs/1711.05101"
methods:
  - method:adamw-optimizer
cites: []
tags:
  - optimizer
  - classic
---

# Decoupled Weight Decay Regularization

## Abstract Summary
This foundational paper demonstrates that standard L2 regularization in Adam is fundamentally flawed when combined with adaptive gradient moment scaling. The authors propose AdamW, which decouples weight decay updates from gradient moment computation, restoring optimal regularization across deep learning tasks.

## Key Contributions
1. Discovered the discrepancy between L2 regularization and true weight decay in adaptive moment optimizers.
2. Introduced the decoupled AdamW formulation now ubiquitous in deep learning.
