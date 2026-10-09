---
id: recipe:expdis
type: recipe
title: "ExpDis Explorer-then-Distill"
method: method:expdis
task: task:math-code-rl-dense
target_hardware: "RLVR host plus one or more explorer replicas"
framework: "PyTorch RLVR host; official ExpDis"
repo_url: "https://github.com/SaifPunjwani/Exploration-Distillation"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - expdis
---

# ExpDis Explorer-then-Distill

## Hardware & Environment Setup
- Official: `https://github.com/SaifPunjwani/Exploration-Distillation`.
- Checkpoints: `https://huggingface.co/SaifPunjwani/expdis-checkpoints`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_explorer_trace(correct: bool, quality: float, min_quality: float) -> bool:
    if min_quality < 0:
        raise ValueError("min_quality must be non-negative")
    return bool(correct) and quality >= min_quality
```

Novelty on explorers only. Distill filtered traces. Do not retarget CISPO.
