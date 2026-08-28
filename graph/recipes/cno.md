---
id: recipe:cno
type: recipe
title: Convolutional Neural Operator (CNO) Recipe
method: method:cno
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090 or 1x A100
framework: PyTorch 2.5+
repo_url: https://github.com/bogdanraonic3/ConvolutionalNeuralOperator
pip_dependencies:
- torch>=2.5.0
- scipy>=1.13.0
- numpy>=1.26.0
tags:
- scientific-ml
- neural-operator
- cno
- cnn-operator
---

# Convolutional Neural Operator (CNO) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/bogdanraonic3/ConvolutionalNeuralOperator`.
- Data: Compressible Euler, Navier-Stokes, and Shear Layer datasets.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, step lr scheduler.
