---
id: recipe:pivotopd
type: recipe
title: "PivotOPD Preventive and Recovery Distillation"
method: method:pivotopd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "multi-turn agent OPD box with env replay; paper: Qwen3-1.7B/8B plus a Nemotron-3.5 SWE transfer"
framework: "PyTorch group-RL host with a privileged self-teacher"
repo_url: "https://research.nvidia.com/labs/lpr/pivotopd/"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - pivotopd
  - distillation
  - agentic
  - on-policy
---

# PivotOPD Preventive and Recovery Distillation

## Hardware & Environment Setup
- Project: `https://research.nvidia.com/labs/lpr/pivotopd/` (`arXiv:2609.40285`). `code_status: announced`. No dedicated public GitHub as of 2026-10-01.
- AppWorld TGC stays CANOPY. Frozen-teacher matching stays OPD.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PivotEvent:
    turn: int
    gold_action: str
    student_action: str
    recovery: list[str]

    @property
    def pivotal(self) -> bool:
        return self.student_action != self.gold_action


def pivotopd_weights(event: PivotEvent, prevent_rkl: float, recover_fkl: list[float]) -> float:
    if not event.pivotal:
        return 0.0
    if len(recover_fkl) != len(event.recovery):
        raise ValueError("recovery forward-KL must align with recovery actions")
    return prevent_rkl + sum(recover_fkl)
```

Reverse-KL the student toward the gold-hinted self-teacher at the pivotal turn. Forward-KL onto recovery responses written without the hint. Combine with the group RL surrogate.

## Critical Hyperparameters & Tuning Advice
- Recovery budget \(K\). Skipping recovery is not PivotOPD.
- Teacher-named pivots, not random turns. ALFWorld oracle labeling is analysis-only.
