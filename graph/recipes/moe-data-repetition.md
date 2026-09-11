---
id: recipe:moe-data-repetition
type: recipe
title: "MoE Repetition Regularization Note"
method: method:moe-data-repetition
task: task:pretrain-moe-frontier
target_hardware: "n/a (gotcha; paper 80M–1B active / 8.5B total)"
framework: "any MoE pretrain stack"
repo_url: "none found"
pip_dependencies: []
tags:
  - recipe
  - moe
  - data-repetition
---

# MoE Repetition Regularization Note

## Hardware & Environment Setup
- No official code (`arXiv:2609.11917`). Architecture defaults stay DeepSeek-V4 / Kimi-K3.

## Quickstart Implementation

```python
def moe_repeat_budget(dense_ok_repeats: int = 8) -> dict:
    """MoEs start hurting near 4×; dense 80M tolerated 8× in the paper."""
    return {
        "moe_warn_repeats": max(1, dense_ok_repeats // 2),
        "moe_collapse_repeats": 32,
        "unique_data_still_wins": True,
        "try_masking_dropout": True,
    }
```

## Critical Hyperparameters & Tuning Advice
- Prefer unique tokens. If you must repeat, plan MoE repeats tighter than dense folklore and add dropout / FFN-output masking.
- Effect scales with total params, not active FLOPs.
