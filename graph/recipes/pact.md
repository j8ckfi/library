---
id: recipe:pact
type: recipe
title: "PACT Actor-then-Critic IS"
method: method:pact
task: task:token-level-critic-rl
target_hardware: "actor-critic box matching a BPCO/PPO host; paper: Qwen3.5-4B math / Qwen3.6-35B-A3B SWE"
framework: "PyTorch actor-critic host"
repo_url: "https://github.com/AllSpark-Research/PACT"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - pact
  - actor-critic
  - credit-assignment
---

# PACT Actor-then-Critic IS

## Hardware & Environment Setup
- Claimed repo: `https://github.com/AllSpark-Research/PACT`. Empty stub as of 2026-09-24. `code_status: announced`. Do not treat it as a runnable trainer.
- Token-level critic first hop stays BPCO. Pass@1 stays CISPO. Async stays SAO.

## Quickstart Implementation

```python
from __future__ import annotations

import math


def unique_token_credit(v_after: float, v_before: float) -> float:
    return v_after - v_before


def critic_is_weight(pi_logp: float, mu_logp: float, clip: float = 1.0) -> float:
    ratio = math.exp(pi_logp - mu_logp)
    return min(max(ratio, 1.0 - clip), 1.0 + clip)


def bce_value_loss(logit: float, target: float) -> float:
    p = 1.0 / (1.0 + math.exp(-logit))
    t = min(max(target, 1e-6), 1.0 - 1e-6)
    return -(t * math.log(p) + (1.0 - t) * math.log(1.0 - p))


def pact_step_order() -> tuple[str, str]:
    return ("actor", "critic")
```

Update the actor on the current critic, then train the critic with `critic_is_weight` against the updated policy. Prefer BCE over MSE for the value head.

## Critical Hyperparameters & Tuning Advice
- Actor-then-Critic is load-bearing. Critic-then-actor reintroduces the lag the paper targets.
- Clip the critic IS weight. Unclipped ratios explode on long agentic traces.
- Do not retarget CISPO or SAO from the 72.87% / 67.4% numbers.
