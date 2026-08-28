---
id: recipe:cvit
type: recipe
title: CViT (Continuous Vision Transformer) Recipe
method: method:cvit
task: task:operator-grid-pde
target_hardware: 1x NVIDIA RTX 4090 (24GB) or 1x A100 (80GB)
framework: PyTorch 2.5+
repo_url: https://github.com/PredictiveIntelligenceLab/cvit
pip_dependencies:
- torch>=2.5.0
- timm>=1.0.0
- einops>=0.8.0
tags:
- scientific-ml
- neural-operator
- cvit
- transformer
- sota
---

# CViT Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/PredictiveIntelligenceLab/cvit`.
- Datasets: PDEBench 2D Darcy Flow, 2D Navier-Stokes, Shallow Water.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, weight_decay=1e-4, CosineAnnealingLR.
- Patch Size: 8x8 or 16x16 with continuous coordinate query cross-attention.
