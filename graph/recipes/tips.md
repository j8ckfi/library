---
id: recipe:tips
type: recipe
title: TIPS Outcome-Only Generative PRMs
method: method:tips
task: task:all-zero-verifier-groups
target_hardware: 'Generative PRM RLVR host; paper: 3.2K outcome trajectories'
framework: PyTorch RLVR host; official TIPS
repo_url: https://github.com/RUCBM/TIPS
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- tips
---

# TIPS Outcome-Only Generative PRMs

## Hardware & Environment Setup
- Official: `https://github.com/RUCBM/TIPS`.
- `code_status: released` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def outcome_only_reward(pred_outcome: bool, gold_outcome: bool) -> float:
    return 1.0 if pred_outcome == gold_outcome else 0.0
```

Reward the outcome, keep the steps. Do not retarget VeriGate.
