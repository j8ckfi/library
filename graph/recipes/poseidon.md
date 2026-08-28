---
id: recipe:poseidon
type: recipe
title: Poseidon (PDE Foundation Model) Recipe
method: method:poseidon
task: task:operator-foundation
target_hardware: 4x NVIDIA A100 (80GB) or H100
framework: PyTorch 2.5+ / HuggingFace
repo_url: https://github.com/camlab-ethz/poseidon
pip_dependencies:
- torch>=2.5.0
- transformers>=4.48.0
- einops>=0.8.0
- timm>=1.0.0
tags:
- scientific-ml
- neural-operator
- foundation-model
- poseidon
- sota
---

# Poseidon Pretraining & Fine-Tuning Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA A100 (80GB) or H100.
- Repository: `https://github.com/camlab-ethz/poseidon`.
- HF Hub: `camlab-ethz/poseidon`.

## Fine-Tuning Hyperparameters
- Loss: Relative L2 / Normalized MSE Loss.
- Optimizer: AdamW, fine-tuning lr=1e-4, cosine decay, weight_decay=1e-2.
