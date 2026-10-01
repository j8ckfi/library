---
id: recipe:lsd
type: recipe
title: "LSD Length Self-Distillation"
method: method:lsd
task: task:math-code-rl-dense
target_hardware: "RLVR box with an EMA copy of the actor; paper: Qwen3-4B-Base, DAPO-Math-17K"
framework: "PyTorch GRPO/CISPO-family host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - lsd
  - rlvr
  - distillation
---

# LSD Length Self-Distillation

## Hardware & Environment Setup
- No official GitHub as of 2026-10-01 (`arXiv:2609.38854`). `repo_url: none found`. `code_status: none`.
- Pass@1 stays CISPO. Engine stays Miles.

## Quickstart Implementation

```python
from __future__ import annotations


def ema_update(shadow: list[float], params: list[float], decay: float) -> list[float]:
    if not 0.0 <= decay < 1.0:
        raise ValueError("decay must be in [0, 1)")
    if len(shadow) != len(params):
        raise ValueError("shadow and params must align")
    return [decay * s + (1.0 - decay) * p for s, p in zip(shadow, params)]


def lsd_route(rewards: list[int], threshold: float = 1.0) -> str:
    if not rewards:
        raise ValueError("group is empty")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be in [0, 1]")
    rate = sum(1 for r in rewards if r > 0) / len(rewards)
    if rate >= threshold:
        return "opd"
    return "rl"


def lst(length: float, reference: float) -> float:
    if reference <= 0.0:
        raise ValueError("reference length must be positive")
    return (length - reference) / reference
```

Route all-correct groups to SG-FKL against the EMA teacher. Keep the host RLVR loss on unsolved groups. Freeze the easy set when reporting LST.

## Critical Hyperparameters & Tuning Advice
- Default threshold 1.0 (all-correct). Lowering it distills unsolved groups.
- EMA half-life: too fast copies verbosity; too slow freezes a stale short policy.
