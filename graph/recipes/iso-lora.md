---
id: recipe:iso-lora
type: recipe
title: "Iso-LoRA Tangent-Space Descent"
method: method:iso-lora
task: task:lora-quality-tuning
target_hardware: "1x 24GB GPU (host LoRA box; paper up to 7B)"
framework: "PyTorch / PEFT LoRA parameterization"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
  - "peft"
tags:
  - recipe
  - iso-lora
  - lora
---

# Iso-LoRA Tangent-Space Descent

## Hardware & Environment Setup
- No official GitHub as of 2026-09-14 (`arXiv:2609.12123`). `repo_url: none found`.
- 24GB quality default stays vanilla LoRA + rsLoRA + LR sweep.

## Quickstart Implementation

```python
import torch


def induced_update(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Weight-space perturbation BA."""
    return b @ a


def iso_lora_step(a: torch.Tensor, b: torch.Tensor, grad_a: torch.Tensor, grad_b: torch.Tensor, lr: float) -> tuple[torch.Tensor, torch.Tensor]:
    """Spectral-whiten the induced tangent update, then factor-wise apply."""
    g = grad_b @ a + b @ grad_a
    u, s, vh = torch.linalg.svd(g, full_matrices=False)
    scale = (s.mean().clamp_min(1e-8) / s.clamp_min(1e-8))
    g_iso = (u * (s * scale).unsqueeze(0)) @ vh
    b_new = b - lr * (g_iso @ a.transpose(-1, -2))
    a_new = a - lr * (b.transpose(-1, -2) @ g_iso)
    return a_new, b_new
```

## Critical Hyperparameters & Tuning Advice
- Strongest paper gains at rank 32-128. Combine with an rsLoRA + global LR sweep.
- AdamW underuses rank; do not read a failed high-rank AdamW sweep as "rank does not help".
