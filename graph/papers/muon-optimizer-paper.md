---
id: paper:muon-optimizer-paper
type: paper
title: "Muon: An Optimizer for Hidden Layers in Neural Networks"
authors:
  - "Keller Jordan"
  - "Yuchen Jin"
  - "Vojtech Cima"
  - "Jeremy Bernstein"
year: 2025
month: 2
arxiv_id: "2502.16738"
url: "https://arxiv.org/abs/2502.16738"
methods:
  - method:muon-optimizer
cites:
  - paper:adamw-paper
tags:
  - optimizer
  - pretraining
  - fast-convergence
---

# Muon: An Optimizer for Hidden Layers in Neural Networks

## Abstract Summary
The Muon optimizer replaces coordinate-wise second-moment scaling in standard optimizers with matrix-orthogonalized updates. For any 2D weight matrix in a neural network, Muon calculates the nearest orthogonal matrix to the accumulated momentum buffer using a hardware-accelerated Newton-Schulz polynomial iteration. When applied to 2D parameters in transformer architectures, Muon achieves identical validation perplexity in roughly half the steps and wall-clock time of heavily tuned AdamW baselines.

## Key Contributions
1. **Newton-Schulz Orthogonalization**: Practical polynomial formulation that runs in pure matrix multiplications on GPU Tensor Cores.
2. **Spectral Norm Invariance**: Update steps maintain constant spectral norm, stabilizing training dynamics across deep networks.
3. **Speedup Verification**: Demonstrated ~1.5x–2x step efficiency across NanoGPT, CIFAR, and large-scale language model pretraining runs.

## Empirical Highlights
- Surpassed tuned AdamW on standard 1.5B token FineWeb-Edu language modeling baselines.
- Scales efficiently without numerical overflow when paired with RMSNorm and standard precision regimes.
