---
id: recipe:looped-models-done-right
type: recipe
title: "Looped Models Done Right (xllm-loop)"
method: method:looped-models-done-right
task: task:recurrent-encoder-decoder-lm
target_hardware: "dense looped LM pretrain 100M–1.6B; paper KV-sharing / RL-from-saved-state"
framework: "PyTorch; official xllm-loop"
repo_url: "https://github.com/ifm-ai/xllm-loop"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - looped-models-done-right
  - architecture
---

# Looped Models Done Right (xllm-loop)

## Hardware & Environment Setup
- Official: `https://github.com/ifm-ai/xllm-loop`. `code_status: released` as of 2026-10-06.
- CED experimental hop stays RLT. MoE looping stays SMELT.

## Quickstart Implementation

```python
from __future__ import annotations

import math


def depth_prior_entropy(probs: list[float]) -> float:
    if not probs:
        raise ValueError("depth prior is empty")
    total = sum(probs)
    if total <= 0:
        raise ValueError("depth prior must be positive")
    ent = 0.0
    for p in probs:
        q = p / total
        if q > 0:
            ent -= q * math.log(q)
    return ent
```

Clone xllm-loop. Learn the depth prior with an entropy keep-broad term. Use orthogonal injection. For decode, share terminal KV; for RL, backprop from saved states.

## Critical Hyperparameters & Tuning Advice
- 1.6B: 3x smaller KV matches fixed-depth full cache. Prefill distill up to 1.79x. RL 2x. Do not retarget RLT or SMELT.
