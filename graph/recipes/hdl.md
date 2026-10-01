---
id: recipe:hdl
type: recipe
title: "HDL Hindsight-Divergence Localization"
method: method:hdl
task: task:math-code-rl-dense
target_hardware: "GRPO-family box; paper: math / code / agent, slime host"
framework: "PyTorch / slime group-relative host"
repo_url: "https://github.com/THUDM/slime"
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - hdl
  - rlvr
---

# HDL Hindsight-Divergence Localization

## Hardware & Environment Setup
- No dedicated HDL GitHub as of 2026-10-01 (`arXiv:2609.36864`). `repo_url` is the slime host `https://github.com/THUDM/slime`. `code_status: none`.
- Pass@1 stays CISPO. Peer all-fail salvage stays GRAFT.

## Quickstart Implementation

```python
from __future__ import annotations

import math


def hindsight_scores(logp: list[float], logp_h: list[float]) -> list[float]:
    if len(logp) != len(logp_h) or not logp:
        raise ValueError("original and hindsight logps must align and be non-empty")
    return [abs(h - o) for o, h in zip(logp, logp_h)]


def branch_index(scores: list[float]) -> int:
    if not scores:
        raise ValueError("scores are empty")
    best = 0
    best_s = -math.inf
    for i, s in enumerate(scores):
        if s > best_s:
            best = i
            best_s = s
    return best


def suffix_mask(length: int, branch: int) -> list[bool]:
    if length <= 0:
        raise ValueError("length must be positive")
    if not 0 <= branch < length:
        raise IndexError("branch out of range")
    return [i >= branch for i in range(length)]
```

Score root tokens with and without hindsight, branch at the max absolute logp change, reuse the prefix, and train only the new suffix. Continuations never see the hindsight context.

## Critical Hyperparameters & Tuning Advice
- Roots \(M<G\). Shrinking \(G\) is not the method.
- Entropy branch points are a different algorithm.
