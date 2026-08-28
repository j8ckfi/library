---
id: recipe:pi-cvit
type: recipe
title: PI-CViT (Physics-Informed Continuous Vision Transformer) Recipe
method: method:pi-cvit
task: task:operator-physics-informed
target_hardware: 2x NVIDIA RTX 4090 (24GB) or 2x A100 (80GB)
framework: PyTorch 2.5+
repo_url: https://github.com/NanxiiChen/PI-CViT
pip_dependencies:
- torch>=2.5.0
- timm>=1.0.0
- soap-optimizer>=0.1.0
tags:
- scientific-ml
- neural-operator
- physics-informed
- pi-cvit
- sota
---

# PI-CViT Physics-Informed Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 2x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/NanxiiChen/PI-CViT`.
- Datasets / PDEs: 2D Darcy, Kolmogorov Flow, Allen-Cahn PDE residuals.

## Training Hyperparameters
- Loss: PDE Residual Loss + Boundary/Initial Condition Loss balanced dynamically with GradNorm.
- Optimizer: SOAP optimizer (second-order preconditioner) with lr=1e-3, weight_decay=1e-4.
- Collocation Strategy: Adaptive causal temporal sampling.
