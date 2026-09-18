---
id: recipe:retireopd
type: recipe
title: "RetireOPD Adaptive Retirement"
method: method:retireopd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "multi-GPU RL box for Qwen2.5 1.5B–7B agent rollouts"
framework: "PyTorch agent RL host with privileged OPD"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - retireopd
  - opsd
  - agentic
---

# RetireOPD Adaptive Retirement

## Hardware & Environment Setup
- No official GitHub as of 2026-09-18 (`arXiv:2609.20784`). `repo_url: none found`. `code_status: none`.
- Outcome-only first hop stays CANOPY. Async stays SAO. Distill default stays OPD. Privileged math OPSD stays VISTA.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetirementState:
    discrepancy: list[float]
    student_success: float
    teacher_success: float
    fraction: float = 0.9
    window: int = 3


def discrepancy_stopped_shrinking(history: list[float], window: int) -> bool:
    if len(history) < window + 1:
        return False
    recent = history[-window:]
    return min(recent) >= history[-(window + 1)]


def should_retire(state: RetirementState) -> bool:
    """Drop privileged OPD when discrepancy stalls and the student is close enough."""
    if state.teacher_success <= 0:
        return False
    caught_up = state.student_success >= state.fraction * state.teacher_success
    return caught_up and discrepancy_stopped_shrinking(state.discrepancy, state.window)
```

## Critical Hyperparameters & Tuning Advice
- Train the skill-conditioned teacher on environment rewards first. Joint RL+OPD is the student phase only.
- Sweep the success-fraction gate; retiring too early throws away dense tokens, retiring too late copies a stale teacher.
- After retirement, keep the RL loss; do not keep a token-level OPD term "just in case".
