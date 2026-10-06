---
id: recipe:flash-opd
type: recipe
title: "Flash-OPD First-Passage Horizon"
method: method:flash-opd
task: task:student-distillation
target_hardware: "OPD host with cheap teacher prefix checks; paper: diverse teacher–student pairs"
framework: "PyTorch OPD host; official Flash-OPD"
repo_url: "https://github.com/Onedean/Flash-OPD"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - flash-opd
  - distillation
---

# Flash-OPD First-Passage Horizon

## Hardware & Environment Setup
- Official: `https://github.com/Onedean/Flash-OPD`. `code_status: released` as of 2026-10-06.
- Distill default stays OPD.

## Quickstart Implementation

```python
from __future__ import annotations

def first_passage(events: int, threshold: int) -> bool:
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    if events < 0:
        raise ValueError("event count must be non-negative")
    return events >= threshold
```

Generate with KV cache. Count low-compatibility events. Stop independently per trajectory when `first_passage` is true. Use event rate only to pick the next verification step.

## Critical Hyperparameters & Tuning Advice
- 2.2×–7.5× vs standard OPD. Do not retarget OPD.
