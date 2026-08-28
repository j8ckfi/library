---
id: recipe:upt
type: recipe
title: Universal Physics Transformers (UPT) Recipe
method: method:upt
task: task:operator-industrial-mesh
target_hardware: 2x NVIDIA A100 (80GB) or RTX 4090
framework: PyTorch 2.5+
repo_url: https://github.com/ml-jku/UPT
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
- timm>=1.0.0
tags:
- scientific-ml
- neural-operator
- transformer
- upt
---

# Universal Physics Transformers (UPT) Recipe

## Hardware & Environment Setup
- Recommended Hardware: 2x NVIDIA A100 (80GB).
- Repository: `https://github.com/ml-jku/UPT`.
- Project Page: `https://ml-jku.github.io/UPT`.

## Hyperparameters & Optimization
- Loss: Relative L2 / MSE Loss.
- Optimizer: AdamW, lr=5e-4, cosine decay.
