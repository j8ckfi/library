---
id: recipe:dpot
type: recipe
title: DPOT (Denoising Pre-trained Operator Transformer) Recipe
method: method:dpot
task: task:operator-foundation
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+
repo_url: https://github.com/thu-ml/DPOT
pip_dependencies:
- torch>=2.5.0
- transformers>=4.48.0
- einops>=0.8.0
tags:
- scientific-ml
- neural-operator
- foundation-model
- dpot
---

# DPOT Training Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB).
- Repository: `https://github.com/thu-ml/DPOT`.
- Data: PDEBench pre-training corpus.

## Hyperparameters & Optimization
- Loss: Masked Denoising Reconstruction Loss (Relative L2).
- Optimizer: AdamW, lr=1e-3, cosine decay with warmup.
