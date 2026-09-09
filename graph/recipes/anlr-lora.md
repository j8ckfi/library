---
id: recipe:anlr-lora
type: recipe
title: "AnLR-LoRA Anisotropic Rank LR"
method: method:anlr-lora
task: task:lora-quality-tuning
target_hardware: "1x 24GB GPU (host LoRA box)"
framework: "PyTorch / PEFT"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "peft"
tags:
  - recipe
  - lora
  - anlr-lora
---

# AnLR-LoRA Anisotropic Rank LR

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Wrap AdamW LoRA with per-rank LR factors.
- 24GB quality default stays vanilla LoRA + rsLoRA + LR sweep.

## Quickstart Implementation

```python
import torch


def mean_normalize(scale: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Keep the module's mean LR equal to the global LR."""
    return scale / scale.mean().clamp(min=eps)


def anlr_factors(velocity: torch.Tensor, adam_snr: torch.Tensor) -> torch.Tensor:
    """Per-rank scale from function-space velocity and Adam SNR. Both rank-length."""
    raw = (velocity.abs() + 1e-8) * (adam_snr.abs() + 1e-8)
    return mean_normalize(raw)
```

## Critical Hyperparameters & Tuning Advice
- Mean-normalize inside each adapter module, not globally across the model.
- Combine with an rsLoRA + global LR sweep; do not skip the sweep.
