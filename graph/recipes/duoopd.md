---
id: recipe:duoopd
type: recipe
title: "DuoOPD Joint-Outcome Gating"
method: method:duoopd
task: task:student-distillation
target_hardware: "single-teacher OPD box with verifiers; paper: Qwen3 and Llama mixtures"
framework: "PyTorch sampled-token OPD host"
repo_url: "https://github.com/YongYuanDeAo/DuoOPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - duoopd
  - distillation
  - multi-teacher
  - on-policy
---

# DuoOPD Joint-Outcome Gating

## Hardware & Environment Setup
- Official: `https://github.com/YongYuanDeAo/DuoOPD`. `code_status: released`.
- Multi-teacher default stays Open-MOPD. Subspace cycling stays PMOPD.

```bash
git clone https://github.com/YongYuanDeAo/DuoOPD.git && cd DuoOPD
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def softplus(x: float) -> float:
    if x > 20.0:
        return x
    return math.log1p(math.exp(x))


def duoopd_weight(
    student_ok: bool,
    teacher_ok: bool,
    log_ratio: float,
    teacher_ctx_log_ratio: float,
    shared: float,
) -> float:
    if shared <= 0.0:
        raise ValueError("shared student-success weight must be positive")
    sign = 1.0 if student_ok else -1.0
    if teacher_ok == student_ok:
        mag = softplus(sign * log_ratio)
    elif teacher_ok and not student_ok:
        mag = softplus(-teacher_ctx_log_ratio)
    else:
        mag = shared
    return sign * mag
```

Cache one verified teacher response per question. Student outcome sets the sign; joint outcome selects magnitude. Direction-only gating is OPDVR, not DuoOPD.

## Critical Hyperparameters & Tuning Advice
- Shared student-success weight is per-task, not a router.
- Teacher-only success must score the failed student response with the teacher's verified answer in context.
