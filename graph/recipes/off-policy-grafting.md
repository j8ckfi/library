---
id: recipe:off-policy-grafting
type: recipe
title: "Off-Policy Grafting Merge"
method: method:off-policy-grafting
task: task:agent-continual-learning
target_hardware: "donor SFT plus CPU/GPU merge; paper: post-trained LLM CL"
framework: "SFT then scaled weight merge"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - off-policy-grafting
  - continual-learning
---

# Off-Policy Grafting Merge

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.05872`). `repo_url: none found`. `code_status: none`.
- Agent-CL first hop stays ACLArena. GRAFT stays method:graft.

## Quickstart Implementation

```python
from __future__ import annotations

def scaled_merge(base: list[float], donor: list[float], alpha: float) -> list[float]:
    if len(base) != len(donor):
        raise ValueError("base and donor must match")
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    return [(1.0 - alpha) * b + alpha * d for b, d in zip(base, donor)]
```

SFT a donor copy on the new data. Merge with `scaled_merge`. Do not run OPSD as the CL default on the strength of on-policy folklore.

## Critical Hyperparameters & Tuning Advice
- Off-policy merging beats OPSD in the paper. Do not retarget ACLArena.
