---
id: recipe:graft
type: recipe
title: "GRAFT Off-Policy Cross-Model Trajectory Exchange"
method: method:graft
task: task:math-code-rl-dense
target_hardware: "two-model GRPO box (or one learner plus stored peer groups); paper n=8, five math benches"
framework: "PyTorch / GRPO-family host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - graft
  - rlvr
  - off-policy
---

# GRAFT Off-Policy Cross-Model Trajectory Exchange

## Hardware & Environment Setup
- No official GitHub as of 2026-09-30 (`arXiv:2609.37868`). `repo_url: none found`. `code_status: none`.
- Pass@1 stays CISPO. All-zero PRM gating stays VeriGate.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Group:
    rewards: list[int]
    advantages: list[float]
    token_logp: list[list[float]]


def mixed_success(rewards: list[int]) -> bool:
    if not rewards:
        return False
    s = sum(1 for r in rewards if r > 0)
    return 0 < s < len(rewards)


def graft_replace(receiver: Group, peer: Group) -> Group | None:
    if mixed_success(receiver.rewards) or any(r > 0 for r in receiver.rewards):
        return None
    if not mixed_success(peer.rewards):
        return None
    if len(peer.rewards) != len(peer.advantages):
        raise ValueError("peer rewards and advantages must align")
    return peer


def token_is_clip(ratio: float, low: float = 0.2, high: float = 5.0) -> float:
    if low <= 0.0 or high < low:
        raise ValueError("clip bounds must satisfy 0 < low <= high")
    return min(max(ratio, low), high)


def compatibility_weight(recv_mean_logp: float, lo: float, hi: float) -> float:
    if hi < lo:
        raise ValueError("compatibility range inverted")
    if hi == lo:
        return 1.0
    t = (recv_mean_logp - lo) / (hi - lo)
    return min(max(t, 0.0), 1.0)
```

Gate on receiver all-fail × peer mixed-success. Keep `peer.advantages`. Clip token IS of the receiver vs stored tokens. Run peer minibatches after on-policy ones. Do not pool rewards across models.

## Critical Hyperparameters & Tuning Advice
- Paper \(n=8\). Stored peer groups from finished GRPO runs recover +1.8 of the +2.1 live lift.
- Sharing on already-informative receiver groups is HACPO and lost here.
- Cross-tokenizer scores are a proxy; keep the IS clip.
