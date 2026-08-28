---
id: paper:lno
type: paper
title: Latent Neural Operator for Solving Forward and Inverse PDE Problems
authors:
- Tian Wang
- Chuang Wang
year: 2024
month: 6
arxiv_id: '2406.03923'
url: https://arxiv.org/abs/2406.03923
methods:
- method:lno
cites:
- paper:fno
- paper:deeponet
tags:
- scientific-ml
- neural-operator
- lno
- inverse-pde
---

# Latent Neural Operator for Solving Forward and Inverse PDE Problems

## Abstract Summary
Neural operators effectively solve PDE problems from data without knowing the explicit equations, which learn the map from the input sequences of observed samples to the predicted values. Most existing works build the model in the original geometric space, leading to high computational costs when the number of sample points is large. We present the Latent Neural Operator (LNO) solving PDEs in the latent space. In particular, we first propose Physics-Cross-Attention (PhCA) transforming representation from the geometric space to the latent space, then learn the operator in the latent space, and finally recover the real-world geometric space via the inverse PhCA map. Our model retains flexibility that can decode values in any position not limited to locations defined in the training set, and therefore can naturally perform interpolation and extrapolation tasks particularly useful for inverse problems. Moreover, the proposed LNO improves both prediction accuracy and computational efficiency. Experiments show that LNO reduces the GPU memory by 50%, speeds up training 1.8 times, and reaches state-of-the-art accuracy on four out of six benchmarks for forward problems and a benchmark for inverse problem. Code is available at https://github.com/L-I-M-I-T/LatentNeuralOperator.

## Key Contributions
- Formulates and evaluates `lno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/L-I-M-I-T/LatentNeuralOperator`
