---
id: paper:transolver-3
type: paper
title: 'Transolver-3: Scaling Up Transformer Solvers to Industrial-Scale Geometries'
authors:
- Hang Zhou
- Haixu Wu
- Haonan Shangguan
- Yuezhou Ma
- Huikun Weng
- Jianmin Wang
- Mingsheng Long
year: 2026
month: 2
arxiv_id: '2602.04940'
url: https://arxiv.org/abs/2602.04940
methods:
- method:transolver-3
cites:
- paper:transolver
- paper:transolver-pp
- paper:ab-upt
- paper:gaot
tags:
- scientific-ml
- neural-operator
- cad-mesh
- cfd
- aerodynamics
- transolver-3
- sota
---

# Transolver-3: Scaling Up Transformer Solvers to Industrial-Scale Geometries

## Abstract Summary
Deep learning has emerged as a transformative tool for the neural surrogate modeling of partial differential equations (PDEs), known as neural PDE solvers. However, scaling these solvers to industrial-scale geometries with over $10^8$ cells remains a fundamental challenge due to the prohibitive memory complexity of processing high-resolution meshes. We present Transolver-3, a new member of the Transolver family as a highly scalable framework designed for high-fidelity physics simulations. To bridge the gap between limited GPU capacity and the resolution requirements of complex engineering tasks, we introduce two key architectural optimizations: faster slice and deslice by exploiting matrix multiplication associative property and geometry slice tiling to partition the computation of physical states. Combined with an amortized training strategy by learning on random subsets of original high-resolution meshes and a physical state caching technique during inference, Transolver-3 enables high-fidelity field prediction on industrial-scale meshes. Extensive experiments demonstrate that Transolver-3 can handle meshes with over 160 million cells, achieving impressive performance across three challenging simulation benchmarks, including aircraft and automotive design tasks. Code is available at https://github.com/thuml/Transolver-3.

## Key Contributions
- Formulates and evaluates `transolver-3` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/thuml/Transolver-3`
