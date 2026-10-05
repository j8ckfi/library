---
id: recipe:ftw
type: recipe
title: "FTW Replay Ordinal Filter"
method: method:ftw
task: task:agentic-async-rl
target_hardware: "critic-free RFT host with a CPU replay buffer; paper: Qwen2.5-3B-Instruct Search-R1"
framework: "PyTorch RFT plus CEM-style quantile filter on replay"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - ftw
  - rl-alignment
  - agentic
---

# FTW Replay Ordinal Filter

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.03361`). `repo_url: none found`. `code_status: none`.
- Async stragglers stay SAO. Do not treat verl-agent as an FTW repo.

## Quickstart Implementation

```python
from __future__ import annotations


def winners(returns: list[float], keep: float) -> list[int]:
    if not 0.0 < keep <= 1.0:
        raise ValueError("keep must be in (0, 1]")
    if not returns:
        raise ValueError("replay minibatch is empty")
    order = sorted(range(len(returns)), key=lambda i: returns[i], reverse=True)
    k = max(1, int(keep * len(returns)))
    return order[:k]
```

Sample a minibatch from replay. Keep the top-`keep` trajectories by return. Project the policy onto those winners (cross-entropy / NLL on winner tokens). Tune `keep` as selection pressure; smaller `keep` is more risk-seeking.

## Critical Hyperparameters & Tuning Advice
- FTW-K1-C4 on Search-R1 is 35.46 ± 0.15 vs GRPO 33.6 / PPO 32.5.
- Do not invent a Sokoban scalar; the paper reports curves.
