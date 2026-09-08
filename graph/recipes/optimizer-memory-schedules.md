---
id: recipe:optimizer-memory-schedules
type: recipe
title: "Optimizer Memory Schedules Recipe"
method: method:optimizer-memory-schedules
task: task:llm-pretraining-optimization
target_hardware: "small/mid dense pretrain (paper: 51M–253M; not a 7B box)"
framework: "PyTorch"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - optimizer
  - overtraining
  - hyperparameter
---

# Optimizer Memory Schedules Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-08. Apply the HP rules on top of the host optimizer. ~7B default stays `method:muon2`.
- Paper: seq 2048, global batch 256 sequences, independent base-LR sweep per $(P,f)$.

## Quickstart Implementation

```python
import math


def ot_factor(tokens: float, params: float) -> float:
    """f = T / (20 P). Chinchilla-normalized overtraining."""
    return float(tokens) / (20.0 * float(params))


def weight_decay_for_ot(f: float, schedule: str = "uniform") -> float:
    """Preferred WD coefficient after the paper's 51M LR×WD sweep."""
    root = math.sqrt(max(f, 1e-12))
    if schedule == "uniform":
        return 8.0 * root
    if schedule == "log-time":
        return 2.0 * root
    raise ValueError(f"unknown WD schedule {schedule!r}")


def lr_decay_kind(f: float) -> str:
    """Linear wins at 1× OT; cosine wins at 8× and 32× for all four optimizers."""
    if f <= 2.0:
        return "linear_to_zero"
    return "cosine_to_zero"
```

## Critical Hyperparameters & Tuning Advice
- Sweep base LR at the actual OT. Do not transfer a $1\times$ LR.
- Longer OT → longer fixed memory ($M$ grew $20$→$640$–$1280$ on 51M from $1\times$ to $128\times$). $\beta=0.98$ is moderate-OT, not universal.
- ADANA treatment in the paper: $\kappa=0.85$, $\delta=8$, $g_3=8$, log-time WD, momentum cooldown. Still not a Muon2 replacement.
- Does not replace Muon2, KL-SOAP, or Puro-2B.
