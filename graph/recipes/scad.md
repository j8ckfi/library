---
id: recipe:scad
type: recipe
title: "SCAD Structured Planning and Local Distill"
method: method:scad
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "long-horizon agent RL+OPD host; paper: Qwen3-4B text, Qwen3-VL multimodal"
framework: "PyTorch hybrid RL / on-policy distillation"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - scad
  - rl-alignment
  - agentic
---

# SCAD Structured Planning and Local Distill

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.03372`). `repo_url: none found`. `code_status: none`.
- AppWorld coverage stays CANOPY. Folding stays FoldGRPO.

## Quickstart Implementation

```python
from __future__ import annotations


def execution_credit(terminal: float, teacher_kl: float) -> float:
    if terminal < 0.0:
        return teacher_kl
    return terminal + teacher_kl


def planning_credit(terminal: float, tree_adv: float) -> float:
    return terminal + tree_adv
```

Segment traces into plan steps and bounded subtasks. Distill execution in the local subtask context. Build a prefix tree over completed (subtask, report) keys and compare terminal returns under matched prefixes. Mix with `planning_credit` on plan tokens and `execution_credit` on act tokens (block negative terminal on execution).

## Critical Hyperparameters & Tuning Advice
- Text macro-average 46.10 vs ATOD 41.62. Do not retarget CANOPY.
