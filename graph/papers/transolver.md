---
id: paper:transolver
type: paper
title: 'Transolver: A Fast Transformer Solver for PDEs on General Geometries'
authors:
- Haixu Wu
- Huakun Luo
- Haowen Wang
- Jianmin Wang
- Mingsheng Long
year: 2024
month: 2
arxiv_id: '2402.02366'
url: https://arxiv.org/abs/2402.02366
methods:
- method:transolver
cites:
- paper:fno
- paper:gnot
tags:
- scientific-ml
- neural-operator
- transformer
- transolver
---

# Transolver: A Fast Transformer Solver for PDEs on General Geometries

## Abstract Summary
Transformers have empowered many milestones across various fields and have recently been applied to solve partial differential equations (PDEs). However, since PDEs are typically discretized into large-scale meshes with complex geometries, it is challenging for Transformers to capture intricate physical correlations directly from massive individual points. Going beyond superficial and unwieldy meshes, we present Transolver based on a more foundational idea, which is learning intrinsic physical states hidden behind discretized geometries. Specifically, we propose a new Physics-Attention to adaptively split the discretized domain into a series of learnable slices of flexible shapes, where mesh points under similar physical states will be ascribed to the same slice. By calculating attention to physics-aware tokens encoded from slices, Transovler can effectively capture intricate physical correlations under complex geometrics, which also empowers the solver with endogenetic geometry-general modeling capacity and can be efficiently computed in linear complexity. Transolver achieves consistent state-of-the-art with 22% relative gain across six standard benchmarks and also excels in large-scale industrial simulations, including car and airfoil designs. Code is available at https://github.com/thuml/Transolver.

## Key Contributions
- Formulates and evaluates `transolver` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/thuml/Transolver`
