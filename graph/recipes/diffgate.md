---
id: recipe:diffgate
type: recipe
title: "DiffGate Failure-Gated Teacher Mix"
method: method:diffgate
task: task:student-distillation
target_hardware: "GRPO + white-box teacher; paper: Qwen3-0.6B/1.7B"
framework: "verl-style GRPO host plus teacher reverse-KL"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - diffgate
  - distillation
---

# DiffGate Failure-Gated Teacher Mix

## Hardware & Environment Setup
- No dedicated GitHub as of 2026-10-06 (`arXiv:2610.04596`). `repo_url: none found`. `code_status: none`. Paper cites verl.

## Quickstart Implementation

```python
from __future__ import annotations

def teacher_gate(reward: float, group_fail_frac: float) -> float:
    if not 0.0 <= group_fail_frac <= 1.0:
        raise ValueError("fail fraction must be in [0, 1]")
    if reward > 0:
        return 0.0
    return group_fail_frac
```

On failed trajectories only, add `teacher_gate * bounded_teacher_kl` to the GRPO loss. Successful rollouts stay GRPO.

## Critical Hyperparameters & Tuning Advice
- Code avg@8 +1.7/+1.8 vs GRPO. Do not retarget OPD-then-RLVR.
