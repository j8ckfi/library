---
id: recipe:exppo
type: recipe
title: "ExPPO Exploration-Preserving Advantages"
method: method:exppo
task: task:math-code-rl-dense
target_hardware: "GRPO-family RLVR box"
framework: "PyTorch GRPO host; official ExPPO"
repo_url: "https://github.com/jinhangzhan/ExPPO"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - exppo
  - rl-alignment
---

# ExPPO Exploration-Preserving Advantages

## Hardware & Environment Setup
- Official: `https://github.com/jinhangzhan/ExPPO`. `code_status: released` as of 2026-10-06.
- Pass@1 stays CISPO.

## Quickstart Implementation

```python
from __future__ import annotations

def surprisal_weight(neg_logp: float, length: int) -> float:
    if length <= 0:
        raise ValueError("length must be positive")
    return neg_logp / length
```

Clone ExPPO. After group rewards, reshape advantages with length-normalized surprisal and prompt pass rate, then shared-normalize. Keep verifier sign.

## Critical Hyperparameters & Tuning Advice
- Coverage / diversity lift vs equal-advantage GRPO. Do not retarget CISPO.
