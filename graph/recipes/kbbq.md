---
id: recipe:kbbq
type: recipe
title: "KBBQ W4A4 Quantization"
method: method:kbbq
task: task:fp4-hardware-training
target_hardware: "inference GPU with FP4 kernels"
framework: "PyTorch"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - quantization
  - fp4
  - kbbq
---

# KBBQ W4A4 Quantization

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Native FP4 training stays Quartet-II / MXFP4.

## Quickstart Implementation

```python
import torch


def participation_factor(weight: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Scalar κ proxy: mean square over max square on a block."""
    w2 = weight.float() * weight.float()
    return w2.mean() / w2.max().clamp(min=eps)


def brake(kappa: torch.Tensor, kappa_star: float = 1.0, brake: float = 0.9) -> torch.Tensor:
    """Stay below the flatten ceiling κ*."""
    return torch.minimum(kappa, kappa.new_tensor(brake * kappa_star))
```

## Critical Hyperparameters & Tuning Advice
- Do not push every block to κ*. The method is a brake, not a maximizer.
