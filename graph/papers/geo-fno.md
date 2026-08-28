---
id: paper:geo-fno
type: paper
title: Fourier Neural Operator with Learned Deformations for PDEs on General Geometries
authors:
- Zongyi Li
- Daniel Zhengyu Huang
- Burigede Liu
- Anima Anandkumar
year: 2022
month: 7
arxiv_id: '2207.05209'
url: https://arxiv.org/abs/2207.05209
methods:
- method:geo-fno
cites:
- paper:fno
tags:
- scientific-ml
- neural-operator
- geo-fno
- mesh-pde
---

# Fourier Neural Operator with Learned Deformations for PDEs on General Geometries

## Abstract Summary
Deep learning surrogate models have shown promise in solving partial differential equations (PDEs). Among them, the Fourier neural operator (FNO) achieves good accuracy, and is significantly faster compared to numerical solvers, on a variety of PDEs, such as fluid flows. However, the FNO uses the Fast Fourier transform (FFT), which is limited to rectangular domains with uniform grids. In this work, we propose a new framework, viz., geo-FNO, to solve PDEs on arbitrary geometries. Geo-FNO learns to deform the input (physical) domain, which may be irregular, into a latent space with a uniform grid. The FNO model with the FFT is applied in the latent space. The resulting geo-FNO model has both the computation efficiency of FFT and the flexibility of handling arbitrary geometries. Our geo-FNO is also flexible in terms of its input formats, viz., point clouds, meshes, and design parameters are all valid inputs. We consider a variety of PDEs such as the Elasticity, Plasticity, Euler's, and Navier-Stokes equations, and both forward modeling and inverse design problems. Geo-FNO is $10^5$ times faster than the standard numerical solvers and twice more accurate compared to direct interpolation on existing ML-based PDE solvers such as the standard FNO.

## Key Contributions
- Formulates and evaluates `geo-fno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/neuraloperator/Geo-FNO`
