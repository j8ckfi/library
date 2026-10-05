---
id: recipe:adastep
type: recipe
title: "AdaStep Per-State Shrinkage"
method: method:adastep
task: task:tool-agent-segment-credit
target_hardware: "GiGPO-style agent RL host; paper: Qwen3-1.7B/4B, Qwen2.5-7B-Instruct"
framework: "PyTorch group-relative RL plus per-state scalar shrinkage"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - adastep
  - rl-alignment
  - agentic
---

# AdaStep Per-State Shrinkage

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.03223`). `repo_url: none found`. `code_status: none`.
- Tool vs summary token split stays SLCA-GRPO. Sparse-outcome coverage stays CANOPY.

## Quickstart Implementation

```python
from __future__ import annotations


def shrinkage(signal_var: float, total_var: float, eps: float = 1e-8) -> float:
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    if total_var < 0.0 or signal_var < 0.0:
        raise ValueError("variances must be non-negative")
    if total_var <= eps:
        return 0.0
    coef = signal_var / (total_var + eps)
    return max(0.0, min(1.0, coef))


def mix_advantage(traj_adv: float, step_adv: float, coef: float) -> float:
    if not 0.0 <= coef <= 1.0:
        raise ValueError("coef must be in [0, 1]")
    return traj_adv + coef * step_adv
```

Keep the trajectory-level group advantage. For each shared-state group, estimate how much return variance is attributable to the chosen action vs downstream noise, then mix with `shrinkage`.

## Critical Hyperparameters & Tuning Advice
- Qwen3-1.7B Δ vs GiGPO ends at ScienceWorld +9.36. Qwen3-4B ALFWorld In +4.99.
- Do not retarget SLCA-GRPO or CANOPY.
