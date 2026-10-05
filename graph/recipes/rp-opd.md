---
id: recipe:rp-opd
type: recipe
title: "RP-OPD Rubric-Privileged Warm Start"
method: method:rp-opd
task: task:student-distillation
target_hardware: "OPD then RL host; paper: Qwen2.5-3B/7B, Llama-3.1-8B"
framework: "PyTorch OPD then rubric-reward RL"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - rp-opd
  - distillation
  - rubric
---

# RP-OPD Rubric-Privileged Warm Start

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.02781`). `repo_url: none found`. `code_status: none`.
- Verifiable OPD then RLVR stays `method:opd-then-rlvr`. Matching distillation stays OPD.

## Quickstart Implementation

```python
from __future__ import annotations


def teacher_prefix(prompt: str, rubric: str) -> str:
    if not prompt.strip():
        raise ValueError("prompt is empty")
    if not rubric.strip():
        raise ValueError("rubric is empty")
    return rubric.rstrip() + "\n\n" + prompt.lstrip()


def student_prefix(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("prompt is empty")
    return prompt
```

Stage 1: teacher sees `teacher_prefix`; student sees `student_prefix`; OPD matches next-token distributions on student rollouts. Stage 2: drop the teacher and optimize the rubric reward with the usual RL host.

## Critical Hyperparameters & Tuning Advice
- Student must not receive the rubric at train or serve. That is the privileged split.
