---
id: recipe:evors
type: recipe
title: "EvoRS Reward-DAG Evolution"
method: method:evors
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "Qwen3-4B/8B policy + 8B-27B GRM"
framework: "open-ended RL with an executable Reward-DAG"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - evors
  - rubrics
---

# EvoRS Reward-DAG Evolution

## Hardware & Environment Setup
- No official GitHub as of 2026-09-14 (`arXiv:2609.12459`). `repo_url: none found`.
- Checker agents stay CANOPY. Frozen-judge step credit stays DRACO.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass
class Candidate:
    dag: object
    delta_success: float
    delta_hack: float
    delta_health: float
    info_std: float
    info_range: float


def accept_candidate(c: Candidate, tau_succ: float = 1.0, tau_guard: float = 0.05, tau_health: float = 0.15) -> bool:
    """Paper-style guards: success, anti-hack, health, informativeness."""
    if c.delta_success < tau_succ - 1.0:
        return False
    if c.delta_hack > tau_guard:
        return False
    if c.delta_health < -tau_health:
        return False
    return c.info_std >= 0.02 and c.info_range >= 0.05
```

## Critical Hyperparameters & Tuning Advice
- Paper evolves every five RL steps from the RLAIF single-node scorer.
- Reject candidates that flatten reward variance even if mean quality ticks up.
