---
id: recipe:dial-opd
type: recipe
title: "DIAL-OPD Probability-Space Token Keep-Mask"
method: method:dial-opd
task: task:student-distillation
target_hardware: "Sampled-token OPD host; paper: four teacher-student pairs"
framework: "PyTorch OPD host; official DIAL-OPD"
repo_url: "https://github.com/EIT-NLP/DIAL-OPD"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - dial-opd
---

# DIAL-OPD Probability-Space Token Keep-Mask

## Hardware & Environment Setup
- Official: `https://github.com/EIT-NLP/DIAL-OPD`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

from math import log, exp

def dial_keep_score(logp_t: float, logp_s: float, beta: float) -> float:
    if beta < 0:
        raise ValueError("beta must be non-negative")
    reward = abs(logp_t - logp_s)
    log_mean = ((logp_t + logp_s) / 2.0) if beta == 0 else (log((exp(beta * logp_t) + exp(beta * logp_s)) / 2.0) / beta)
    return reward * exp(log_mean)
```

Keep reverse-KL matching. Downweight low-low tokens. Do not retarget OPD.
