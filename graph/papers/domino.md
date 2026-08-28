---
id: paper:domino
type: paper
title: 'DoMINO: A Decomposable Multi-scale Iterative Neural Operator for Modeling
  Large Scale Engineering Simulations'
authors:
- Rishikesh Ranade
- Mohammad Amin Nabian
- Kaustubh Tangsali
- Alexey Kamenev
- Oliver Hennigh
- Ram Cherukuri
- Sanjay Choudhry
year: 2025
month: 1
arxiv_id: '2501.13350'
url: https://arxiv.org/abs/2501.13350
methods:
- method:domino
cites:
- paper:gino
- paper:fno
tags:
- scientific-ml
- neural-operator
- domino
- point-cloud
- physicsnemo
---

# DoMINO: A Decomposable Multi-scale Iterative Neural Operator for Modeling Large Scale Engineering Simulations

## Abstract Summary
Numerical simulations play a critical role in design and development of engineering products and processes. Traditional computational methods, such as CFD, can provide accurate predictions but are computationally expensive, particularly for complex geometries. Several machine learning (ML) models have been proposed in the literature to significantly reduce computation time while maintaining acceptable accuracy. However, ML models often face limitations in terms of accuracy and scalability and depend on significant mesh downsampling, which can negatively affect prediction accuracy and generalization. In this work, we propose a novel ML model architecture, DoMINO (Decomposable Multi-scale Iterative Neural Operator) developed in NVIDIA Modulus to address the various challenges of machine learning based surrogate modeling of engineering simulations. DoMINO is a point cloudbased ML model that uses local geometric information to predict flow fields on discrete points. The DoMINO model is validated for the automotive aerodynamics use case using the DrivAerML dataset. Through our experiments we demonstrate the scalability, performance, accuracy and generalization of our model to both in-distribution and out-of-distribution testing samples. Moreover, the results are analyzed using a range of engineering specific metrics important for validating numerical simulations.

## Key Contributions
- Formulates and evaluates `domino` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `none found`
