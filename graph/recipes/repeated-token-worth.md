---
id: recipe:repeated-token-worth
type: recipe
title: "Repeated-Token Epoch Geometry"
method: method:repeated-token-worth
task: task:data-constrained-pretrain
target_hardware: "dense pretrain box under a unique-token budget"
framework: "any NTP trainer; schedule is data-side"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - repeated-token-worth
  - data-curriculum
---

# Repeated-Token Epoch Geometry

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.05591`). `repo_url: none found`. `code_status: none`.
- Open mix stays OLMo-3.

## Quickstart Implementation

```python
from __future__ import annotations

def extra_epoch_cost(epochs: float, unique_tokens_per_param: float) -> float:
    if epochs < 1:
        raise ValueError("epochs must be >= 1")
    if unique_tokens_per_param <= 0:
        raise ValueError("unique tokens per parameter must be positive")
    return (epochs - 1.0) / unique_tokens_per_param
```

Track `extra_epoch_cost` as the paper's single cost variable vs fresh data. Prefer shuffled repeats over consecutive shard replay.

## Critical Hyperparameters & Tuning Advice
- Second epoch is still valuable. Fixed-U: ~15 epochs at 127M to ~4 at 2B. Do not retarget OLMo-3.
