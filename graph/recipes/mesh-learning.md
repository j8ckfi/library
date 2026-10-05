---
id: recipe:mesh-learning
type: recipe
title: "Mesh Learning Strategy Heads"
method: method:mesh-learning
task: task:math-code-rl-dense
target_hardware: "GRPO-style RLVR host with m strategy heads; paper: Qwen3-4B, Qwen2.5-7B"
framework: "PyTorch"
repo_url: "https://github.com/Ayanami-0123/Open-Mesh-Learning"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - mesh-learning
  - rl-alignment
  - rlvr
---

# Mesh Learning Strategy Heads

## Hardware & Environment Setup
- Official: `https://github.com/Ayanami-0123/Open-Mesh-Learning`. `code_status: released`.
- Pass@1 default stays CISPO.

```bash
git clone https://github.com/Ayanami-0123/Open-Mesh-Learning.git && cd Open-Mesh-Learning
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def balance_penalty(head_mass: list[float], eps: float = 1e-8) -> float:
    if len(head_mass) < 2:
        raise ValueError("need at least two strategy heads")
    if any(p < 0.0 for p in head_mass):
        raise ValueError("head mass must be non-negative")
    total = sum(head_mass)
    if total <= eps:
        raise ValueError("head mass sums to zero")
    probs = [p / total for p in head_mass]
    entropy = -sum(p * math.log(p + eps) for p in probs)
    return -entropy
```

Run \(m\) concurrent strategy heads with a coach prompt that names the strategy. Add `balance_penalty` (negative entropy of head mass) to the GRPO-style loss. Paper AIME26 uses \(m=4\).

## Critical Hyperparameters & Tuning Advice
- Qwen3-4B m=4 AIME26 56.7 vs GRPO 43.3. Do not retarget CISPO.
