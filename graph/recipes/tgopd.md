---
id: recipe:tgopd
type: recipe
title: "TGOPD Teacher-Gating Recipe"
method: method:tgopd
task: task:student-distillation
target_hardware: "asynchronous OPD cluster (paper: 5 nodes at 4B / 7 nodes at 35B; teacher is 1 node)"
framework: "PyTorch / slime"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - tgopd
  - distillation
  - on-policy
---

# TGOPD Teacher-Gating Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-08. Add a prompt-level gate to an existing asynchronous OPD loop (student rollouts, frozen teacher logps, outcome verifier).
- Paper: slime + IcePop, $K_T=3$, $\tau=2/3$. Issue probes at cycle start so they overlap student decode.
- Host distill algorithm stays `method:opd`. Pass@1 labeled RLVR stays CISPO.

## Quickstart Implementation

```python
from typing import Sequence


def teacher_reliability(probe_rewards: Sequence[float]) -> float:
    """q_T(x): mean verifier pass rate over K_T teacher probes."""
    if not probe_rewards:
        return 0.0
    return sum(float(r) for r in probe_rewards) / len(probe_rewards)


def tgopd_gate(q_t: float, tau: float = 2.0 / 3.0) -> bool:
    """True → dense OPD; False → verifier-grounded GRPO."""
    return q_t >= tau


def select_advantage(use_opd: bool, opd_adv, grpo_adv):
    """Exclusive routing. Never add the two advantages."""
    return opd_adv if use_opd else grpo_adv
```

## Critical Hyperparameters & Tuning Advice
- $K_T=3$, $\tau=2/3$ are the reported MOPD settings. Do not blend branches.
- Teacher scoring can stay unconditional; the extra work is the probe decodes.
- Does not replace OPD, CISPO, OPSA, or Open-MOPD.
