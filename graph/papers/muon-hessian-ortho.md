---
id: paper:muon-hessian-ortho
type: paper
title: 'How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization'
authors:
- 'Shenyang Deng'
- 'Garvit Goyal'
- 'Tianyu Pang'
- 'Shuhua Yu'
- 'Yaoqing Yang'
year: 2026
month: 10
arxiv_id: '2610.28975'
url: https://arxiv.org/abs/2610.28975
methods:
- method:muon2
cites:
- paper:muon2
tags:
- optimizer
- muon
- gotcha
---

# How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization

## Abstract Summary
Muon's implicit Kronecker preconditioner matches the row-block diagonally dominant layer-wise Hessian of a neural net at initialization, which is why orthogonalization is a better default than a generic polar-factor story.

## Key Contributions
1. Hessian-structure explanation for Muon orthogonalization at init.

## Empirical Highlights
- Does not retarget Muon2. Init analysis, not a 7B bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28975`
- Code: `none found` (`code_status: none`).
