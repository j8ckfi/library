---
id: recipe:og-opsd
type: recipe
title: "OG-OPSD Outcome-Guided Divergence"
method: method:og-opsd
task: task:privileged-teacher-opsd
target_hardware: "OPSD host with a binary verifier; paper: Qwen3 1.7B/4B/8B and Qwen3-VL-2B"
framework: "PyTorch privileged-OPSD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - og-opsd
  - distillation
---

# OG-OPSD Outcome-Guided Divergence

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.05070`). `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def divergence_mode(correct: bool) -> str:
    return "rkl" if correct else "fkl"
```

On correct rollouts use reverse KL; on incorrect use forward KL. Cut the teacher prefix where cumulative teacher entropy says reliability dropped.

## Critical Hyperparameters & Tuning Advice
- Improves vanilla OPSD on Qwen3 1.7B/4B/8B and Qwen3-VL-2B. Do not retarget VISTA.
