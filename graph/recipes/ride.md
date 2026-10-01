---
id: recipe:ride
type: recipe
title: "RIDE Representation Residual Extrapolation"
method: method:ride
task: task:student-distillation
target_hardware: "student + frozen RL teacher + frozen pre-RL checkpoint; paper: 1.5B–4B pairs"
framework: "PyTorch OPD host with hidden-state hooks"
repo_url: "https://github.com/xixixixixxxx/RIDE"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - ride
  - distillation
  - on-policy
---

# RIDE Representation Residual Extrapolation

## Hardware & Environment Setup
- Official: `https://github.com/xixixixixxxx/RIDE`. `code_status: released`.
- Frozen-teacher matching stays OPD. Direct-OPD keep-mask stays S2D-OPD.

```bash
git clone https://github.com/xixixixixxxx/RIDE.git && cd RIDE
```

## Quickstart Implementation

```python
from __future__ import annotations


def ride_target(teacher: list[float], base: list[float], lam: float) -> list[float]:
    if lam < 0.0:
        raise ValueError("lambda must be non-negative")
    if len(teacher) != len(base):
        raise ValueError("teacher and base hidden states must align")
    return [t + (lam - 1.0) * (t - b) for t, b in zip(teacher, base)]


def mse(student: list[float], target: list[float]) -> float:
    if len(student) != len(target) or not student:
        raise ValueError("student and target must align and be non-empty")
    acc = 0.0
    for s, t in zip(student, target):
        d = s - t
        acc += d * d
    return acc / len(student)
```

\(\lambda=1\) is OPRD (match the teacher). \(\lambda>1\) extrapolates along the RL residual. Student starts at the pre-RL checkpoint.

## Critical Hyperparameters & Tuning Advice
- One scalar \(\lambda\) shared across layers. Do not replace this with a sampled-token log-ratio scale.
- Different-init teachers are out of scope.
