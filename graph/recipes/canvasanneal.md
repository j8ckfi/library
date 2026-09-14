---
id: recipe:canvasanneal
type: recipe
title: "CanvasAnneal DLM Curriculum"
method: method:canvasanneal
task: task:posttrain-diffusion
target_hardware: "LLaDA-7B-A1B-Instruct diffu-GRPO box"
framework: "masked diffusion LM + group-relative policy optimization"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - canvasanneal
  - dlm
---

# CanvasAnneal DLM Curriculum

## Hardware & Environment Setup
- No official GitHub as of 2026-09-14 (`arXiv:2609.13060`). `repo_url: none found`.
- Image/flow defaults stay DiffusionOPSD / Self-OPD. AR serving stays Uno.

## Quickstart Implementation

```python
import torch


def anneal_keep_frac(step: int, total: int, start: float = 1.0, end: float = 0.0) -> float:
    """Fraction of teacher-trace tokens kept on the diffusion canvas."""
    t = min(1.0, max(0.0, step / max(total, 1)))
    return start + (end - start) * t


def inject_teacher_canvas(masked, teacher_ids, keep_frac: float, generator=None):
    """Write a random subset of teacher tokens onto the initial canvas."""
    n = max(1, int(round(keep_frac * teacher_ids.numel())))
    idx = torch.randperm(teacher_ids.numel(), generator=generator, device=teacher_ids.device)[:n]
    out = masked.clone()
    flat = out.view(-1)
    flat[idx] = teacher_ids.view(-1)[idx]
    return out
```

## Critical Hyperparameters & Tuning Advice
- Host remains diffu-GRPO. Anneal keep_frac down as reward rises.
- MATH500/Countdown/Tau2 benefited; GSM8K did not. Do not copy one schedule across tasks.
