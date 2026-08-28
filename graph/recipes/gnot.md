---
id: recipe:gnot
type: recipe
title: GNOT (General Neural Operator Transformer) Recipe
method: method:gnot
task: task:operator-industrial-mesh
target_hardware: 1x NVIDIA RTX 4090 or 1x A100
framework: PyTorch 2.5+
repo_url: https://github.com/thu-ml/GNOT
pip_dependencies:
- torch>=2.5.0
- torch-geometric>=2.5.0
- einops>=0.8.0
tags:
- scientific-ml
- neural-operator
- transformer
- gnot
---

# GNOT Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090 or A100.
- Repository: `https://github.com/thu-ml/GNOT`.
- Data: Multiple-input irregular domain benchmarks.

## Hyperparameters & Optimization
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=1e-3, cosine decay with warmup.
