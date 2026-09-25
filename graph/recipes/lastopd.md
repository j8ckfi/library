---
id: recipe:lastopd
type: recipe
title: "LastOPD Last-Layer Crossfade"
method: method:lastopd
task: task:student-distillation
target_hardware: "OPD host matching reverse top-k OPD; paper: 62 steps on DAPO-Math-17k, Qwen3-4B/8B → 1.7B-Base"
framework: "PyTorch OPD host"
repo_url: "https://github.com/Muyiiiii/LastOPD"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - lastopd
  - distillation
  - on-policy
---

# LastOPD Last-Layer Crossfade

## Hardware & Environment Setup
- Claimed repo: `https://github.com/Muyiiiii/LastOPD`. 404 as of 2026-09-25. `code_status: announced`. Do not treat it as a runnable trainer.
- Distill default stays OPD. Multi-teacher stays Open-MOPD. Same-lineage latent-only stays OPRD-Vanilla.

## Quickstart Implementation

```python
from __future__ import annotations


def crossfade_weights(step: int, window: int = 10) -> tuple[float, float]:
    if window <= 0:
        raise ValueError("window must be positive")
    t = max(0, step)
    token_w = min(1.0, t / window)
    latent_w = max(0.0, 1.0 - t / window)
    return token_w, latent_w


def last_layer_rep_loss(student_z: list[float], teacher_z: list[float]) -> float:
    if len(student_z) != len(teacher_z) or not student_z:
        raise ValueError("last-layer states must be non-empty and same width after the projector")
    n = len(student_z)
    s_norm = sum(x * x for x in student_z) ** 0.5
    t_norm = sum(x * x for x in teacher_z) ** 0.5
    if s_norm < 1e-8 or t_norm < 1e-8:
        return 0.0
    acc = 0.0
    for s, t in zip(student_z, teacher_z):
        d = s / s_norm - t / t_norm
        acc += d * d
    return acc / n
```

Use `crossfade_weights` as \(\alpha(t),\beta(t)\). Apply `last_layer_rep_loss` only at the pre-LM-head state (after a width MLP if needed). After `window` steps, drop the latent term.

## Critical Hyperparameters & Tuning Advice
- \(T_w=10\) is the paper default (the latent-only peak). Windows of 5 or 15 sit near token-only OPD.
- Keep reverse top-k token OPD (\(k=16\)) on the same rollouts. A hard switch without overlap underperforms token-only OPD.
- Do not retarget OPD from the +5.55 / +4.02 MATH-500 numbers.
