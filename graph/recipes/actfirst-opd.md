---
id: recipe:actfirst-opd
type: recipe
title: "ActFirst-OPD Inverse Dynamics Distill"
method: method:actfirst-opd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "multi-turn agent OPD box; paper: Qwen3-0.6B/1.7B/4B on ALFWorld/WebShop/ScienceWorld"
framework: "PyTorch multi-turn OPD host"
repo_url: "https://anonymous.4open.science/r/ActFirst-OPD"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - actfirst-opd
  - distillation
  - agentic
  - on-policy
---

# ActFirst-OPD Inverse Dynamics Distill

## Hardware & Environment Setup
- Review-anonymous code as of 2026-10-01: `https://anonymous.4open.science/r/ActFirst-OPD`. `code_status: announced`.
- AppWorld TGC stays CANOPY. Pivotal-mistake OPD stays PivotOPD.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ActFirstTurn:
    inverse_dynamics: bool
    distill_later: bool


def actfirst_policy(deviated: bool) -> ActFirstTurn:
    if deviated:
        return ActFirstTurn(False, True)
    return ActFirstTurn(True, True)


def matches_reference(obs: str, ref_next: str) -> bool:
    if not obs or not ref_next:
        raise ValueError("observation and reference next-obs are required")
    return obs == ref_next
```

Act with inverse dynamics while the transition matches the reference next observation. After deviation, switch to autonomous next-action prediction. Distill full think-then-act responses asynchronously without putting the reference next-obs in the OPD prefix.

## Critical Hyperparameters & Tuning Advice
- Reference next observations are for acting only.
- Dropping the deviation switch is the direct-action ablation that loses quality.
