---
id: recipe:saki
type: recipe
title: "SAKI Maximal-Coupling Teacher Supervision"
method: method:saki
task: task:student-distillation
target_hardware: "teacher+student box with engine-resident speculative verification; paper: 0.6B/1.7B students"
framework: "PyTorch teacher-guided OPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - saki
  - distillation
  - on-policy
---

# SAKI Maximal-Coupling Teacher Supervision

## Hardware & Environment Setup
- No official GitHub as of 2026-09-30 (`arXiv:2609.36601`). `repo_url: none found`. `code_status: none`.
- Student-rollout matching stays OPD. Trust-region OPD steps stay TrOPD. Transport stays RouteOPD.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CouplingEvent:
    token: int
    corrected: bool
    teacher_top1: int


def maximal_couple(p: list[float], q: list[float], student_id: int, residual_id: int) -> CouplingEvent:
    if len(p) != len(q) or not p:
        raise ValueError("p and q must be aligned and non-empty")
    if not 0 <= student_id < len(p) or not 0 <= residual_id < len(q):
        raise IndexError("token ids out of range")
    overlap = min(p[student_id], q[student_id])
    accept_mass = overlap / p[student_id] if p[student_id] > 0.0 else 0.0
    teacher_top1 = max(range(len(q)), key=lambda i: q[i])
    if accept_mass >= 1.0:
        return CouplingEvent(student_id, False, teacher_top1)
    # Caller supplies a uniform u in [0, 1) vs accept_mass; residual_id ~ (q-p)+ / TV.
    return CouplingEvent(residual_id, True, teacher_top1)


def saki_token_loss(
    event: CouplingEvent,
    sampled_rkl: float,
    teacher_top1_nll: float,
) -> float:
    if event.corrected:
        return teacher_top1_nll
    return sampled_rkl
```

Continue the prefix with `event.token`. Train RKL on accepts and teacher-top-1 NLL on corrections. Do not train on the residual id or continue with top-1.

## Critical Hyperparameters & Tuning Advice
- TRB radius \(\epsilon\) bounds \(\Pr(C_t=1)\le\sqrt{\epsilon/2}\). Too small is student OPD; too large is teacher cloning.
- Speculative first-rejection commit is how the paper gets 4.22×; an external teacher loop is correct but slow.
- Placement controls: correction routing beat random and TV-weighted at equal budget.
