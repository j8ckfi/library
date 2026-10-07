---
id: recipe:np-opd
type: recipe
title: "NP-OPD Negative-Policy Rollouts"
method: method:np-opd
task: task:student-distillation
target_hardware: "OPD host; paper: NAVER NP-OPD"
framework: "PyTorch OPD host; official NP-OPD"
repo_url: "https://github.com/naver-ai/np-opd"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - np-opd
---

# NP-OPD Negative-Policy Rollouts

## Hardware & Environment Setup
- Official: `https://github.com/naver-ai/np-opd`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def mix_teacher_and_negative(teacher_w: float, neg_w: float) -> float:
    if teacher_w < 0 or neg_w < 0:
        raise ValueError("weights must be non-negative")
    total = teacher_w + neg_w
    if total == 0:
        raise ValueError("at least one stream must be on")
    return teacher_w / total
```

Official: naver-ai/np-opd. Use when teacher/student overlap is low. Do not retarget OPD or NSD.
