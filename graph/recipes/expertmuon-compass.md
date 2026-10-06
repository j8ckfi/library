---
id: recipe:expertmuon-compass
type: recipe
title: "ExpertMuon-Compass Per-Expert Step Sizes"
method: method:expertmuon-compass
task: task:llm-pretraining-optimization
target_hardware: "MoE Muon-family pretrain box; paper: FineWeb-Edu"
framework: "PyTorch Muon-family MoE trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - expertmuon-compass
  - optimizer
  - moe
---

# ExpertMuon-Compass Per-Expert Step Sizes

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.04140`). `repo_url: none found`. `code_status: none`.
- Dense 7B optimizer stays Muon2.

## Quickstart Implementation

```python
from __future__ import annotations

def compass_scale(expert_cos: float, family_mean: float, radius: float) -> float:
    if family_mean == 0.0:
        raise ValueError("family mean cosine is zero")
    if radius <= 0:
        raise ValueError("radius must be positive")
    return (expert_cos / family_mean) * radius
```

After the Muon orthogonalized update, multiply that expert's step by `compass_scale`. Leave direction and momentum as Muon computed them.

## Critical Hyperparameters & Tuning Advice
- Weight decay matched to NorMuon on longer runs in the paper.
- Strongest when expert data mix shifts. Do not retarget Muon2.
