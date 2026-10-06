---
id: recipe:repetition-count-selection
type: recipe
title: "Repetition-Count Shortlist Across Scales"
method: method:repetition-count-selection
task: task:data-constrained-pretrain
target_hardware: "small-proxy plus target-scale NTP box; paper: 200M / 520M"
framework: "any NTP trainer; schedule is data-side"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - repetition-count-selection
  - data-curriculum
---

# Repetition-Count Shortlist Across Scales

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.05126`). `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def retain_counts(losses: dict[int, float], keep: int = 3) -> list[int]:
    if not losses:
        raise ValueError("need at least one measured r")
    if keep <= 0:
        raise ValueError("keep must be positive")
    ranked = sorted(losses, key=losses.get)
    return ranked[: min(keep, len(ranked))]
```

Measure several r on a smaller model. Evaluate `retain_counts` at the target scale. Do not transfer the single best small-model r.

## Critical Hyperparameters & Tuning Advice
- 520M Proof-Pile-2: r=8 beat r=16. Dual-active with repeated-token-worth. Do not retarget OLMo-3.
