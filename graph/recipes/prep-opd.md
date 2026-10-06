---
id: recipe:prep-opd
type: recipe
title: "Prep-OPD Prepare-then-Freeze Teacher"
method: method:prep-opd
task: task:student-distillation
target_hardware: "teacher RL box plus student OPD box; paper: Qwen3-4B → 0.6B/1.7B"
framework: "PyTorch group-relative teacher RL then OPD"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - prep-opd
  - distillation
---

# Prep-OPD Prepare-then-Freeze Teacher

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.04950`). `repo_url: none found`. `code_status: none`.
- Interleaved teacher RL stays SCOUT.

## Quickstart Implementation

```python
from __future__ import annotations

def prep_then_freeze(phase: str) -> str:
    if phase not in {"teacher_rl", "student_opd"}:
        raise ValueError("phase must be teacher_rl or student_opd")
    return phase
```

Phase `teacher_rl`: sample student prefixes, freeze them, RL the teacher on continuations with final-answer reward. Phase `student_opd`: freeze the prepared teacher and run ordinary OPD.

## Critical Hyperparameters & Tuning Advice
- 4B→1.7B: +8.28 vs OPD, +2.30 vs Relay-OPD. Do not retarget OPD or SCOUT.
