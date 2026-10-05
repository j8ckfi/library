---
id: recipe:sf-mopd
type: recipe
title: "SF-MOPD Slow-Fast Student Coupling"
method: method:sf-mopd
task: task:student-distillation
target_hardware: "MOPD host that can keep an EMA student copy; paper: Qwen3-VL-8B/4B/2B"
framework: "PyTorch multi-teacher OPD plus EMA slow student"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - sf-mopd
  - distillation
  - multi-teacher
---

# SF-MOPD Slow-Fast Student Coupling

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.02324`). `repo_url: none found`. `code_status: none`.
- Multi-teacher default stays Open-MOPD.

## Quickstart Implementation

```python
from __future__ import annotations


def ema_slow(slow: list[float], fast: list[float], decay: float) -> list[float]:
    if not 0.0 < decay < 1.0:
        raise ValueError("decay must be in (0, 1)")
    if len(slow) != len(fast):
        raise ValueError("slow and fast must share a length")
    return [decay * s + (1.0 - decay) * f for s, f in zip(slow, fast)]
```

Update the fast student with the usual teacher OPD step. After each step, refresh the slow copy with `ema_slow`. Deploy the slow weights.

## Critical Hyperparameters & Tuning Advice
- Do not cite Table 1 All Avg as beating library Open-MOPD 83.4% headroom recovery.
