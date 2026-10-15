---
id: paper:muon-ns-bias
type: paper
title: 'From Spectral to Frobenius: When Muon Loses Its Spectral Implicit Bias'
authors:
- Yongtao Wu
- Mahdi Mansouri
- Zhenyu Zhu
year: 2026
month: 10
arxiv_id: '2610.20112'
url: https://arxiv.org/abs/2610.20112
methods:
- method:muon2
cites:
- paper:muon2
- paper:musec
tags:
- optimizer
- muon
- implicit-bias
- gotcha
---

# Muon Newton-Schulz implicit-bias gotcha

## Abstract Summary
Idealized Muon with exact orthogonalization has spectral max-margin bias. Finite Newton-Schulz iterations plus a positive stabilization constant send practical Muon onto the Frobenius max-margin direction of gradient descent, for both EMA and Nesterov momentum. Log-growing NS iteration count recovers the spectral bias.

## Key Contributions
1. Summable-perturbation argument: finite-NS Muon stays bounded-distance from GD trajectories.
2. Distinct roles of NS count, epsilon, and the NS polynomial, including directions that hit neither margin.
3. Recovery recipe: grow NS iterations logarithmically over training.

## Empirical Highlights
- Theory on linearly separable linear classification; not a 7B bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.20112`
- Code: `none found` (`code_status: none`).
