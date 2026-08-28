---
id: paper:rno
type: paper
title: 'Recurrent Neural Operators: Stable Long-Term PDE Prediction'
authors:
- Zaijun Ye
- Chen-Song Zhang
- Wansheng Wang
year: 2025
month: 5
arxiv_id: '2505.20721'
url: https://arxiv.org/abs/2505.20721
methods:
- method:rno
cites:
- paper:fno
tags:
- scientific-ml
- neural-operator
- rno
- recurrent
---

# Recurrent Neural Operators: Stable Long-Term PDE Prediction

## Abstract Summary
Neural operators have emerged as powerful tools for learning solution operators of partial differential equations. However, in time-dependent problems, standard training strategies such as teacher forcing introduce a mismatch between training and inference, leading to compounding errors in long-term autoregressive predictions. To address this issue, we propose Recurrent Neural Operators (RNOs)-a novel framework that integrates recurrent training into neural operator architectures. Instead of conditioning each training step on ground-truth inputs, RNOs recursively apply the operator to their own predictions over a temporal window, effectively simulating inference-time dynamics during training. This alignment mitigates exposure bias and enhances robustness to error accumulation. Theoretically, we show that recurrent training can reduce the worst-case exponential error growth typical of teacher forcing to linear growth. Empirically, we demonstrate that recurrently trained Multigrid Neural Operators significantly outperform their teacher-forced counterparts in long-term accuracy and stability on standard benchmarks. Our results underscore the importance of aligning training with inference dynamics for robust temporal generalization in neural operator learning.

## Key Contributions
- Formulates and evaluates `rno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/ZaijunYe/RNO`
