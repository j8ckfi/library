---
id: paper:fno
type: paper
title: Fourier Neural Operator for Parametric Partial Differential Equations
authors:
- Zongyi Li
- Nikola Kovachki
- Kamyar Azizzadenesheli
- Burigede Liu
- Kaushik Bhattacharya
- Andrew Stuart
- Anima Anandkumar
year: 2020
month: 10
arxiv_id: '2010.08895'
url: https://arxiv.org/abs/2010.08895
methods:
- method:fno
cites: []
tags:
- scientific-ml
- neural-operator
- spectral
- fno
- baseline
---

# Fourier Neural Operator for Parametric Partial Differential Equations

## Abstract Summary
The classical development of neural networks has primarily focused on learning mappings between finite-dimensional Euclidean spaces. Recently, this has been generalized to neural operators that learn mappings between function spaces. For partial differential equations (PDEs), neural operators directly learn the mapping from any functional parametric dependence to the solution. Thus, they learn an entire family of PDEs, in contrast to classical methods which solve one instance of the equation. In this work, we formulate a new neural operator by parameterizing the integral kernel directly in Fourier space, allowing for an expressive and efficient architecture. We perform experiments on Burgers' equation, Darcy flow, and Navier-Stokes equation. The Fourier neural operator is the first ML-based method to successfully model turbulent flows with zero-shot super-resolution. It is up to three orders of magnitude faster compared to traditional PDE solvers. Additionally, it achieves superior accuracy compared to previous learning-based solvers under fixed resolution.

## Key Contributions
- Formulates and evaluates `fno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/neuraloperator/neuraloperator`
