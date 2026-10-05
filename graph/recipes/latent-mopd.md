---
id: recipe:latent-mopd
type: recipe
title: "Latent-MOPD Hidden-State Multi-Teacher OPD"
method: method:latent-mopd
task: task:student-distillation
target_hardware: "multi-teacher OPD box that can store specialist hidden states; paper: 1.5B"
framework: "PyTorch"
repo_url: "https://github.com/fangzy96/Latent-MOPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - latent-mopd
  - distillation
  - multi-teacher
---

# Latent-MOPD Hidden-State Multi-Teacher OPD

## Hardware & Environment Setup
- Official: `https://github.com/fangzy96/Latent-MOPD`. `code_status: released`.
- Multi-teacher default stays Open-MOPD. LastOPD stays the single-teacher latent-collapse schedule.

```bash
git clone https://github.com/fangzy96/Latent-MOPD.git && cd Latent-MOPD
```

## Quickstart Implementation

```python
from __future__ import annotations


def fade_latent_to_token(step: int, window: int) -> tuple[float, float]:
    if window <= 0:
        raise ValueError("window must be positive")
    if step < 0:
        raise ValueError("step must be non-negative")
    beta = max(0.0, 1.0 - step / window)
    alpha = 1.0 - beta
    return alpha, beta
```

Route one specialist per domain. Match its late-layer hidden state (shared projection if widths differ) and its token distribution. Fade `beta` (latent) into `alpha` (token) over `window` steps.

## Critical Hyperparameters & Tuning Advice
- Last-3 same-family is the main table (Norm 1.05). All-layer OPRD-style is 0.64.
