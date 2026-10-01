---
id: recipe:scout
type: recipe
title: "SCOUT Student-Conditioned Teacher Updates"
method: method:scout
task: task:student-distillation
target_hardware: "teacher+student box that can run periodic teacher RL; paper: Qwen3 pairs"
framework: "PyTorch OPD host plus group-relative teacher RL"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - scout
  - distillation
  - on-policy
---

# SCOUT Student-Conditioned Teacher Updates

## Hardware & Environment Setup
- No official GitHub as of 2026-10-01 (`arXiv:2609.38360`). `repo_url: none found`. `code_status: none`.
- Frozen-teacher matching stays OPD. Student-side gating stays TrOPD / SAKI.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScoutStep:
    student_opd: bool
    teacher_rl: bool
    prefix_ratio: float


def prefix_ratio(step: int, total: int, start: float = 0.1, end: float = 0.9) -> float:
    if total <= 0:
        raise ValueError("total steps must be positive")
    if not 0.0 <= start <= end <= 1.0:
        raise ValueError("prefix schedule must satisfy 0 <= start <= end <= 1")
    t = min(max(step, 0), total) / total
    return start + (end - start) * t


def scout_step(step: int, interval: int, total: int) -> ScoutStep:
    if interval <= 0:
        raise ValueError("teacher interval must be positive")
    return ScoutStep(True, step % interval == 0, prefix_ratio(step, total))


def split_prefix(tokens: list[int], ratio: float) -> list[int]:
    if not tokens:
        raise ValueError("student trajectory is empty")
    if not 0.0 <= ratio <= 1.0:
        raise ValueError("ratio must be in [0, 1]")
    k = max(1, min(len(tokens), int(round(ratio * len(tokens)))))
    return tokens[:k]
```

Run student OPD on the full trajectory. On teacher-RL steps, condition the teacher on `split_prefix` and apply outcome RL only to continuation tokens.

## Critical Hyperparameters & Tuning Advice
- Interval \(f\): too small is expensive; too large leaves the off-policy teacher in place.
- Linear prefix-ratio schedule. Teacher RL without student prefixes is not SCOUT.
