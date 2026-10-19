---
id: paper:topa
type: paper
title: 'ToPA: Block-wise Toeplitz Adaptation for Expressive and Efficient Fine-Tuning'
authors:
- 'Sicong Li'
- 'Qianqian Xu'
- 'Zhiyong Yang'
- 'Zitai Wang'
- 'Longtao Huang'
- 'Xiaochun Cao'
- 'Qingming Huang'
year: 2026
month: 10
arxiv_id: '2610.22883'
url: https://arxiv.org/abs/2610.22883
methods:
- method:topa
cites:
- paper:lr-matters-lora
tags:
- peft
- toeplitz
- lora
- active
---

# ToPA

## Abstract Summary
Parameter-Efficient Fine-Tuning (PEFT) has emerged as a prevalent strategy for adapting large pre-trained models. Among PEFT techniques, reparameterization-based methods, particularly those that employ low-rank or sparsity structures, have attracted significant attention. However, these approaches often underperform full fine-tuning. Specifically, low-rank methods constrain the update rank, which is misaligned with the inherently high-rank nature of full fine-tuning. In contrast, sparsity-based techniques limit the flexibility of the parameter space and compromise connectivity across weights. To overcome these limitations, we explore the use of Toeplitz matrices, whose entries are constant a

## Key Contributions
1. ToPA replaces long products of Toeplitz matrices with block-wise Toeplitz factors so each factor has more capacity, the chain is shorter, and training stays stable while remaining more expressive than low-rank or sparse PEFT.

## Empirical Highlights
- products of block-wise Toeplitz matrices approximate arbitrary matrices at shorter chain length; consistently validates vs low-rank and sparse PEFT

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22883`
- Code: `https://github.com/scongl/ToPA` (`code_status: released`).
