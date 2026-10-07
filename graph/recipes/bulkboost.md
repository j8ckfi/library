---
id: recipe:bulkboost
type: recipe
title: "BulkBoost Two-Band Muon Reweight"
method: method:bulkboost
task: task:llm-pretraining-optimization
target_hardware: "Muon-family pretrain box; paper: Pythia 14M–410M"
framework: "PyTorch Muon-family trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - bulkboost
---

# BulkBoost Two-Band Muon Reweight

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def two_band_weight(sigma: float, bulk_edge: float, bulk_w: float, spike_w: float) -> float:
    if bulk_edge <= 0:
        raise ValueError("bulk_edge must be positive")
    return bulk_w if sigma <= bulk_edge else spike_w
```

Marchenko–Pastur bulk vs spike. Fine-grained maps are unnecessary in the paper. Do not retarget Muon2.
