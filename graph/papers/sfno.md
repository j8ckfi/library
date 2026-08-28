---
id: paper:sfno
type: paper
title: 'Spherical Fourier Neural Operators: Learning Stable Dynamics on the Sphere'
authors:
- Boris Bonev
- Thorsten Kurth
- Christian Hundt
- Jaideep Pathak
- Maximilian Baust
- Karthik Kashinath
- Anima Anandkumar
year: 2023
month: 6
arxiv_id: '2306.03838'
url: https://arxiv.org/abs/2306.03838
methods:
- method:sfno
cites:
- paper:fno
tags:
- scientific-ml
- neural-operator
- spherical
- sfno
- weather
---

# Spherical Fourier Neural Operators: Learning Stable Dynamics on the Sphere

## Abstract Summary
Fourier Neural Operators (FNOs) have proven to be an efficient and effective method for resolution-independent operator learning in a broad variety of application areas across scientific machine learning. A key reason for their success is their ability to accurately model long-range dependencies in spatio-temporal data by learning global convolutions in a computationally efficient manner. To this end, FNOs rely on the discrete Fourier transform (DFT), however, DFTs cause visual and spectral artifacts as well as pronounced dissipation when learning operators in spherical coordinates since they incorrectly assume a flat geometry. To overcome this limitation, we generalize FNOs on the sphere, introducing Spherical FNOs (SFNOs) for learning operators on spherical geometries. We apply SFNOs to forecasting atmospheric dynamics, and demonstrate stable auto\-regressive rollouts for a year of simulated time (1,460 steps), while retaining physically plausible dynamics. The SFNO has important implications for machine learning-based simulation of climate dynamics that could eventually help accelerate our response to climate change.

## Key Contributions
- Formulates and evaluates `sfno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/neuraloperator/neuraloperator`
