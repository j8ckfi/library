---
id: recipe:tv-opd
type: recipe
title: "TV-OPD Sign-and-Scale Recipe"
method: method:tv-opd
task: task:student-distillation
target_hardware: "same as host sampled-token OPD (paper: 1.5B JustRL pair; also 8B)"
framework: "PyTorch / host OPD trainer"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - tv-opd
  - distillation
  - on-policy
---

# TV-OPD Sign-and-Scale Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Replace the sampled OPD coefficient with sign × shared TV scale on an existing OPD loop.
- Paper diagnostic: DAPO-Math-17K, batch 64 prompts, one rollout per prompt, AdamW 1e-6.
- Host distill algorithm stays OPD.

## Quickstart Implementation

```python
import torch


def sampled_delta(teacher_logp: torch.Tensor, student_logp: torch.Tensor) -> torch.Tensor:
    """Δ = log π_T(y|h) − log π_θ(y|h). Shapes [T]."""
    return teacher_logp - student_logp


def sign_tv(delta: torch.Tensor) -> torch.Tensor:
    """Bounded directional coefficient. sign(0)=0."""
    return torch.sign(delta)


def tv_from_signs(signs: torch.Tensor) -> torch.Tensor:
    """Cheap sampled TV proxy: mean absolute sign is the fraction of unequal coordinates."""
    if signs.numel() == 0:
        return signs.new_tensor(0.0)
    return signs.abs().mean()


def tv_opd_advantage(delta: torch.Tensor, alpha: float = 0.5) -> torch.Tensor:
    """A = c * sign(Δ). c shrinks as estimated TV shrinks. alpha is the Table 2 regulator."""
    signs = sign_tv(delta)
    scale = (tv_from_signs(signs) ** float(alpha)).clamp(min=0.0, max=1.0)
    return signs * scale
```

## Critical Hyperparameters & Tuning Advice
- Keep the sign. Do not reintroduce per-token |Δ| weights.
- α=0.5 is the Table 2 reported regulator. Sign-TV is α=0 (unit magnitude).
- Expect the gain in the late window, not necessarily in the first 250 steps.
