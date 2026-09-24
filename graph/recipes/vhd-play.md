---
id: recipe:vhd-play
type: recipe
title: "VHD-Play Mechanism-First Envs"
method: method:vhd-play
task: task:mechanism-grounded-agentic-rl-env
target_hardware: "setter plus agentic RL box for Qwen3.6-35B-A3B-class rollouts"
framework: "mechanism solver then stateful tool wrapper; episode reward from the solved reference"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - vhd-play
  - environments
  - agentic
---

# VHD-Play Mechanism-First Envs

## Hardware & Environment Setup
- No official GitHub as of 2026-09-24 (`arXiv:2609.27321`). `repo_url: none found`. `code_status: none`.
- Source-code coding envs stay CodeMidas. AppWorld coverage stays CANOPY. Async stays SAO. SWE loop stays mini-SWE-agent.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MechanismRef:
    u_star: float
    u_default: float


def episode_reward(u_policy: float, ref: MechanismRef) -> float:
    denom = ref.u_star - ref.u_default
    if abs(denom) < 1e-8:
        return 0.0
    raw = (u_policy - ref.u_default) / denom
    return min(1.0, max(0.0, raw))


def admit_environment(solver_ok: bool, wrap_ok: bool, hidden_params: bool) -> bool:
    return solver_ok and wrap_ok and hidden_params
```

Solve \(M(\theta)\) first. Fix \(\mathcal{R}_\theta\) from \(z_\theta\). Wrap dynamics as tools. Reject any instance that publishes parameters or the reference to the player.

## Critical Hyperparameters & Tuning Advice
- Environment-first generation (sandbox before the scoring rule) is the failure mode this reverses.
- Probe actions and decision actions share the turn budget. Do not give free parameter dumps.
- Scale admitted, hidden-parameter instances. Written-out twins are a diagnostic, not the train set.
