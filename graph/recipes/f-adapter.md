---
id: recipe:f-adapter
type: recipe
title: F-Adapter (Frequency-Adaptive Fourier Operator PEFT) Recipe
method: method:f-adapter
task: task:operator-fourier-adapt
target_hardware: 1x NVIDIA RTX 4090 (24GB)
framework: PyTorch 2.5+
repo_url: https://github.com/fogradio/F-Adapter
pip_dependencies:
- torch>=2.5.0
- peft>=0.14.0
- neuraloperator>=1.0.0
tags:
- scientific-ml
- neural-operator
- peft
- fourier-adapter
- f-adapter
- sota
---

# F-Adapter Parameter-Efficient Fine-Tuning Recipe

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA RTX 4090.
- Repository: `https://github.com/fogradio/F-Adapter`.
- Base Models: Pretrained FNO, DPOT backbones.

## Hyperparameters & Optimization
- Trainable Parameter Budget: ~2% total parameters.
- Loss: Relative L2 Loss.
- Optimizer: AdamW, lr=5e-4, cosine decay.
