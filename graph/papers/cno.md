---
id: paper:cno
type: paper
title: Convolutional Neural Operators for robust and accurate learning of PDEs
authors:
- Bogdan Raonić
- Roberto Molinaro
- Tim De Ryck
- Tobias Rohner
- Francesca Bartolucci
- Rima Alaifari
- Siddhartha Mishra
- Emmanuel de Bézenac
year: 2023
month: 2
arxiv_id: '2302.01178'
url: https://arxiv.org/abs/2302.01178
methods:
- method:cno
cites:
- paper:fno
- paper:deeponet
tags:
- scientific-ml
- neural-operator
- cno
- cnn-operator
---

# Convolutional Neural Operators for robust and accurate learning of PDEs

## Abstract Summary
Although very successfully used in conventional machine learning, convolution based neural network architectures -- believed to be inconsistent in function space -- have been largely ignored in the context of learning solution operators of PDEs. Here, we present novel adaptations for convolutional neural networks to demonstrate that they are indeed able to process functions as inputs and outputs. The resulting architecture, termed as convolutional neural operators (CNOs), is designed specifically to preserve its underlying continuous nature, even when implemented in a discretized form on a computer. We prove a universality theorem to show that CNOs can approximate operators arising in PDEs to desired accuracy. CNOs are tested on a novel suite of benchmarks, encompassing a diverse set of PDEs with possibly multi-scale solutions and are observed to significantly outperform baselines, paving the way for an alternative framework for robust and accurate operator learning. Our code is publicly available at https://github.com/bogdanraonic3/ConvolutionalNeuralOperator

## Key Contributions
- Formulates and evaluates `cno` for scientific machine learning and neural operator problems.
- Validated on standardized benchmarks with reproducible empirical metrics.

## Open Source Repository
- Implementation: `https://github.com/bogdanraonic3/ConvolutionalNeuralOperator`
