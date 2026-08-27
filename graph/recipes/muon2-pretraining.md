---
id: recipe:muon2-pretraining
type: recipe
title: "Muon2 Dense 7B Pretraining Recipe"
method: method:muon2
task: task:pretrain-dense-7b
target_hardware: "8x NVIDIA H100 SXM5 80GB (or 1x RTX 4090 24GB for single-layer proxy)"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - pretraining
  - muon2
---

# Muon2 Dense 7B Pretraining Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB SXM5.
- PyTorch Version: 2.5.0+ with CUDA 12.4.

## Quickstart Implementation

```python
import torch

def newton_schulz_iteration(G: torch.Tensor, steps: int = 5, eps: float = 1e-7) -> torch.Tensor:
    """Muon2 matrix orthogonalization via Newton-Schulz polynomial iterations."""
    a, b, c = 3.4445, -4.7750, 2.0315
    X = G.bfloat16()
    X /= (X.norm() + eps)
    if G.size(0) > G.size(1):
        X = X.T
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    if G.size(0) > G.size(1):
        X = X.T
    return X.to(G.dtype)
```
