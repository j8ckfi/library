---
id: paper:tante
type: paper
title: 'TANTE: Time-Adaptive Operator Learning via Neural Taylor Expansion'
authors:
- Zhikai Wu
- Sifan Wang
- Shiyang Zhang
- Sizhuang He
- Min Zhu
- Anran Jiao
- Lu Lu
- David van Dijk
year: 2025
month: 2
arxiv_id: '2502.08574'
url: https://arxiv.org/abs/2502.08574
methods:
- method:tante
cites:
- paper:fno
- paper:cvit
tags:
- scientific-ml
- neural-operator
- tante
- time-adaptive
---

# TANTE: Time-Adaptive Operator Learning via Neural Taylor Expansion

## Abstract Summary
Operator learning for time-dependent partial differential equations (PDEs) has seen rapid progress in recent years, enabling efficient approximation of complex spatiotemporal dynamics. However, most existing methods rely on fixed time step sizes during rollout, which limits their ability to adapt to varying temporal complexity and often leads to error accumulation. Here, we propose the Time-Adaptive Transformer with Neural Taylor Expansion (TANTE), a novel operator-learning framework that produces continuous-time predictions with adaptive step sizes. TANTE predicts future states by performing a Taylor expansion at the current state, where neural networks learn both the higher-order temporal derivatives and the local radius of convergence. This allows the model to dynamically adjust its rollout based on the local behavior of the solution, thereby reducing cumulative error and improving computational efficiency. We demonstrate the effectiveness of TANTE across a wide range of PDE benchmarks, achieving superior accuracy and adaptability compared to fixed-step baselines, delivering accuracy gains of 60-80 % and speed-ups of 30-40 % at inference time. The code is publicly available at https://github.com/zwu88/TANTE for transparency and reproducibility.

## Key Contributions
- Formulates and evaluates `tante` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/zwu88/TANTE`
