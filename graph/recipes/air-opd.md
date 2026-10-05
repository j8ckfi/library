---
id: recipe:air-opd
type: recipe
title: "Air-OPD Iterative Error-to-Repair Guidance"
method: method:air-opd
task: task:privileged-teacher-opsd
target_hardware: "OPSD box that can retry failed rollouts; paper: Qwen3-4B/8B Avg@12"
framework: "PyTorch privileged OPSD host plus a guidance generator"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - air-opd
  - distillation
  - privileged-teacher
---

# Air-OPD Iterative Error-to-Repair Guidance

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.02700`). `repo_url: none found`. `code_status: none`.
- Privileged-OPSD first hop stays VISTA. Scale-collapse scaffolds stay OASIS. Neighborhood teachers stay N-OPSD.

## Quickstart Implementation

```python
from __future__ import annotations


def stage_weight(round_idx: int, verified: bool, decay: float) -> float:
    if decay <= 0.0 or decay > 1.0:
        raise ValueError("decay must be in (0, 1]")
    if round_idx < 0:
        raise ValueError("round_idx must be non-negative")
    w = decay ** round_idx
    if verified:
        w *= 2.0
    return w


def error_aligned_mask(teacher_corrects: list[bool]) -> list[float]:
    if not teacher_corrects:
        raise ValueError("need at least one token flag")
    return [1.0 if flag else 0.0 for flag in teacher_corrects]
```

On a failed response, generate repair guidance, retry on-policy, and if the retry fails, regenerate. Teacher sees guidance only. Weight earlier stages; boost stages whose retry verifies. Apply OPSD only where `error_aligned_mask` is 1.

## Critical Hyperparameters & Tuning Advice
- Self-G (current student as generator) already lifts Math Avg 63.1→65.8 on Qwen3-4B. External-G is optional.
- Do not cite 66.7 as a VISTA bake-off retarget.
