---
id: recipe:lesser
type: recipe
title: "LESSER Output-Layer Gradient Features"
method: method:lesser
task: task:training-data-attribution
target_hardware: "SFT/RL selection box; paper: Llama-2-7B vs 4-checkpoint LESS"
framework: "PyTorch; wrap LESS / GIST / GradAlign / GRACE"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - lesser
  - data-attribution
---

# LESSER Output-Layer Gradient Features

## Hardware & Environment Setup
- No official GitHub as of 2026-10-05 (`arXiv:2610.03702`). `repo_url: none found`. `code_status: none`.
- Peak LDS stays MAGIC.

## Quickstart Implementation

```python
from __future__ import annotations


def lm_head_feature(head_grad: list[float]) -> list[float]:
    if not head_grad:
        raise ValueError("lm_head gradient is empty")
    nrm = sum(x * x for x in head_grad) ** 0.5
    if nrm == 0.0:
        raise ValueError("lm_head gradient is zero")
    return [x / nrm for x in head_grad]
```

Backprop only through the LM head for each candidate. L2-normalize that vector and pass it to the existing LESS / GradAlign scorer instead of a full-parameter embedding.

## Critical Hyperparameters & Tuning Advice
- 9.7× SFT / 3.0× RL vs 4-checkpoint LESS on Llama-2-7B. Jaccard 0.53 vs random 0.075. Do not retarget MAGIC.
