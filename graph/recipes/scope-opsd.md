---
id: recipe:scope-opsd
type: recipe
title: "SCOPE-OPSD Fisher Subspace Auxiliary"
method: method:scope-opsd
task: task:privileged-teacher-opsd
target_hardware: "paper: Qwen3-1.7B/4B/8B on PPU/HBM2e cluster; H100-class VERL box is the practical substitute"
framework: "PyTorch 2.9 / VERL / FSDP / SGLang eval"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.9.0"
tags:
  - recipe
  - scope-opsd
  - opsd
  - distillation
---

# SCOPE-OPSD Fisher Subspace Auxiliary

## Hardware & Environment Setup
- No official GitHub as of 2026-09-14 (`arXiv:2609.12579`). `repo_url: none found`.
- Paper: OpenThoughts Math OPSD 29,434, 100 steps, batch 32, student max 1024 tokens, teacher frozen step-zero self-teacher. Calibrate rank-64 \(F\) on 128 prompts per scale.
- Privileged-teacher first hop stays VISTA. Pass@1 stays CISPO.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def scope_opsd_hidden_loss(
    student_h: torch.Tensor,
    teacher_h: torch.Tensor,
    factor: torch.Tensor,
    coeff: float,
) -> torch.Tensor:
    """Project the privileged residual onto a frozen Fisher-conditioned basis."""
    residual = (teacher_h.detach() - student_h)
    projected = residual @ factor
    return coeff * projected.pow(2).mean()


def match_random_factor(factor: torch.Tensor, generator: torch.Generator) -> torch.Tensor:
    """Spectrum-matched random orientation for the Random control."""
    u, s, vh = torch.linalg.svd(factor, full_matrices=False)
    q, _ = torch.linalg.qr(torch.randn(u.shape, generator=generator, device=factor.device))
    return (q * s.unsqueeze(0)) @ vh
```

## Critical Hyperparameters & Tuning Advice
- Rank 64 won {32, 64, 128} at 1.7B. Recalibrate the auxiliary coefficient to match initial gradient RMS across arms.
- Report one shared checkpoint (paper: step 75), not a per-benchmark oracle.
