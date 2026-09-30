---
id: recipe:lspd
type: recipe
title: "LSPD Least Square Policy Distillation"
method: method:lspd
task: task:student-distillation
target_hardware: "multi-GPU OPD box; paper: six math benches, three teacher–student pairs"
framework: "PyTorch / OPD host with optional replay"
repo_url: "https://github.com/UNCSciML/LSPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - lspd
  - distillation
  - on-policy
  - off-policy
---

# LSPD Least Square Policy Distillation

## Hardware & Environment Setup
- Official: `https://github.com/UNCSciML/LSPD`. `code_status: released`.
- Single-teacher default stays OPD. Pass@1 RLVR stays CISPO.

```bash
git clone https://github.com/UNCSciML/LSPD.git && cd LSPD
```

## Quickstart Implementation

```python
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


def huber(residual: float, delta: float = 1.0) -> float:
    if delta <= 0.0:
        raise ValueError("delta must be positive")
    a = abs(residual)
    if a <= delta:
        return 0.5 * residual * residual
    return delta * (a - 0.5 * delta)


def lspd_token_loss(
    student_logp: float,
    teacher_logp: float,
    entropy: float,
    delta: float = 1.0,
    eta: float = 0.01,
) -> float:
    if eta < 0.0:
        raise ValueError("entropy weight must be non-negative")
    return huber(student_logp - teacher_logp, delta) - eta * entropy


@dataclass
class ReplayRow:
    prefix: object
    token: object
    teacher_logp: float


class LspdReplay:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._buf: deque[ReplayRow] = deque(maxlen=capacity)

    def add(self, row: ReplayRow) -> None:
        self._buf.append(row)

    def __len__(self) -> int:
        return len(self._buf)
```

Train on current student rollouts with several optimizer steps per batch, then mix `LspdReplay` rows (LSPD-RB). Keep the entropy term on both streams.

## Critical Hyperparameters & Tuning Advice
- Huber \(\delta=1\) is the usual robust default. \(\eta\) too small collapses Pass@k.
- LSPD-RB in the paper saturates ~10 rollout batches vs >40 one-update-per-batch; ~25% of OPD rollouts to matched Avg@16.
- Do not retarget OPD from +1.59 Avg@16.
