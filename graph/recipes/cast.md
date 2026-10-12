---
id: recipe:cast
type: recipe
title: CAST Chunk-Aware Credit Alignment
method: method:cast
task: task:cross-tokenizer-opd
target_hardware: 'Cross-tokenizer OPD host; paper: Qwen3-8B teacher'
framework: PyTorch OPD host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cast
---

# CAST Chunk-Aware Credit Alignment

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def preserve_chunk_advantage(weights: list[float], chunk_adv: float) -> list[float]:
    if not weights:
        raise ValueError("empty chunk")
    s = sum(weights)
    if s <= 0:
        raise ValueError("non-positive credit mass")
    return [w / s * chunk_adv for w in weights]
```

Keep the chunk total. Anchor unaligned tokens. Do not retarget Cross-Tokenizer OPD.
