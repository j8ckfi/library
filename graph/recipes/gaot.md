---
id: recipe:gaot
type: recipe
title: GAOT (Geometry-Aware Operator Transformer) Recipe
method: method:gaot
task: task:operator-industrial-mesh
target_hardware: 2x NVIDIA A100 (80GB) or RTX 4090
framework: PyTorch 2.5+
repo_url: https://github.com/camlab-ethz/GAOT
pip_dependencies:
- torch>=2.5.0
- einops>=0.8.0
- scipy>=1.13.0
tags:
- scientific-ml
- neural-operator
- transformer
- gaot
---

# GAOT Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 2x NVIDIA A100 (80GB).
- Repository: `https://github.com/camlab-ethz/GAOT`.
- Project Page: `https://camlab-ethz.github.io/GAOT`.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine schedule.
