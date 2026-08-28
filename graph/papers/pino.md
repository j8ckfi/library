---
id: paper:pino
type: paper
title: Physics-Informed Neural Operator for Learning Partial Differential Equations
authors:
- Zongyi Li
- Hongkai Zheng
- Nikola Kovachki
- David Jin
- Haoxuan Chen
- Burigede Liu
- Kamyar Azizzadenesheli
- Anima Anandkumar
year: 2021
month: 11
arxiv_id: '2111.03794'
url: https://arxiv.org/abs/2111.03794
methods:
- method:pino
cites:
- paper:fno
tags:
- scientific-ml
- neural-operator
- physics-informed
- pino
---

# Physics-Informed Neural Operator for Learning Partial Differential Equations

## Abstract Summary
In this paper, we propose physics-informed neural operators (PINO) that combine training data and physics constraints to learn the solution operator of a given family of parametric Partial Differential Equations (PDE). PINO is the first hybrid approach incorporating data and PDE constraints at different resolutions to learn the operator. Specifically, in PINO, we combine coarse-resolution training data with PDE constraints imposed at a higher resolution. The resulting PINO model can accurately approximate the ground-truth solution operator for many popular PDE families and shows no degradation in accuracy even under zero-shot super-resolution, i.e., being able to predict beyond the resolution of training data. PINO uses the Fourier neural operator (FNO) framework that is guaranteed to be a universal approximator for any continuous operator and discretization-convergent in the limit of mesh refinement. By adding PDE constraints to FNO at a higher resolution, we obtain a high-fidelity reconstruction of the ground-truth operator. Moreover, PINO succeeds in settings where no training data is available and only PDE constraints are imposed, while previous approaches, such as the Physics-Informed Neural Network (PINN), fail due to optimization challenges, e.g., in multi-scale dynamic systems such as Kolmogorov flows.

## Key Contributions
- Formulates and evaluates `pino` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/neuraloperator/physics_informed`
