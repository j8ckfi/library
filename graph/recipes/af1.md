---
id: recipe:af1
type: recipe
title: "AF1 Genuine 1-Bit PTQ"
method: method:af1
task: task:1bit-extreme-quantization
target_hardware: "inference GPU; paper reports ~2.5× vs BF16"
framework: "PyTorch"
repo_url: "https://github.com/Kishon-zzx/AF1"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - quantization
  - 1bit
  - af1
---

# AF1 Genuine 1-Bit PTQ

## Hardware & Environment Setup
- Paper code: `https://github.com/Kishon-zzx/AF1` (verify; 404 at 2026-09-09 ingest).
- Native 1.58-bit pretrain stays Sparse-BitNet. Budget must stay 1.0 BPW including scales.

## Quickstart Implementation

```python
import torch


def binarize(weight: torch.Tensor, scale: torch.Tensor) -> torch.Tensor:
    """Genuine 1-bit codes with a detached scale."""
    return scale.detach() * torch.sign(weight)


def bits_per_weight(n_codes: int, n_scale_bytes: int, n_params: int) -> float:
    """Count hidden overhead. AF1 target is 1.0."""
    return (n_codes + 8 * n_scale_bytes) / float(n_params)
```

## Critical Hyperparameters & Tuning Advice
- Reject recipes that store extra high-precision residuals if they blow the 1.0-BPW budget.
- NABF reconstruction then HiSA allocation; do not skip the Shapley capacity step if reproducing the paper.
