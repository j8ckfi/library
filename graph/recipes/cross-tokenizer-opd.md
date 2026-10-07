---
id: recipe:cross-tokenizer-opd
type: recipe
title: "Cross-Tokenizer OPD Top-k Shared-Vocab Reverse-KL"
method: method:cross-tokenizer-opd
task: task:cross-tokenizer-opd
target_hardware: "OPD host with teacher and student tokenizers; paper: Qwen3 / Llama / Gemma pairs"
framework: "PyTorch OPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - cross-tokenizer-opd
---

# Cross-Tokenizer OPD Top-k Shared-Vocab Reverse-KL

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def shared_topk_mask(student_logits, shared_ids, k: int):
    if k <= 0:
        raise ValueError("k must be positive")
    if not shared_ids:
        raise ValueError("shared vocab is empty")
    scores = student_logits[list(shared_ids)]
    keep = set(shared_ids[i] for i in scores.argsort()[-k:])
    return [tid in keep for tid in shared_ids]
```

Keep 1:1 coverage for the bulk of tokens. Restrict reverse KL to student-selected top-16 of the shared vocab. Span MSE hurts. Do not retarget OPD.
