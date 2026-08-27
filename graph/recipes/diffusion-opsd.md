---
id: recipe:diffusion-opsd
type: recipe
title: "DiffusionOPSD Diffusion Alignment Recipe"
method: method:diffusion-opsd
task: task:posttrain-diffusion
target_hardware: "8x NVIDIA H100 80GB (or 1x RTX 4090 24GB with batch reduction)"
framework: "PyTorch 2.5+ / Diffusers"
repo_url: "https://github.com/worldbench/DiffusionOPSD"
pip_dependencies:
  - "torch>=2.5.0"
  - "diffusers>=0.32.0"
  - "transformers>=4.48.0"
  - "accelerate>=1.2.0"
tags:
  - recipe
  - diffusion
  - alignment
  - diffusion-opsd
---

# DiffusionOPSD Diffusion Alignment Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB (or single RTX 4090 24GB with reduced batch size).
- Framework: PyTorch 2.5+ with Hugging Face `diffusers` and `accelerate`.

## Quickstart Code

```python
import torch
from diffusers import StableDiffusion3Pipeline

def construct_opsd_target(
    clean_anchor: torch.Tensor,
    reward_grad: torch.Tensor,
    step_size: float = 0.1,
    bound_delta: float = 0.5,
) -> torch.Tensor:
    """Constructs bounded positive clean-output target for DiffusionOPSD.

    Args:
        clean_anchor: Clean image prediction from frozen behavior policy.
        reward_grad: Gradients from reward model with respect to clean prediction.
        step_size: Ascent step multiplier.
        bound_delta: Maximum allowed perturbation norm around anchor.

    Returns:
        Bounded clean-output target tensor for finite fitting.
    """
    perturbation = step_size * reward_grad
    clamped_perturbation = torch.clamp(perturbation, -bound_delta, bound_delta)
    return (clean_anchor + clamped_perturbation).detach()
```

## Critical Hyperparameters
- `bound_delta`: 0.5 (limits target construction deviation from behavior anchor).
- `ema_decay`: 0.99 (behavior policy update rate).
- `finite_fitting_steps`: 1-4 gradient steps per outer trajectory batch.
