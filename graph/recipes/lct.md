---
id: recipe:lct
type: recipe
title: 'GPU Huffman train tensors'
method: method:lct
task: task:full-param-memory-efficient-pretrain
target_hardware: 'Paper: NanoGPT 162M; Qwen3-4B FT'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- lct
---

# GPU Huffman train tensors

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def ratio(raw_bytes: int, coded_bytes: int) -> float:
    if raw_bytes <= 0 or coded_bytes <= 0:
        raise ValueError("byte counts must be positive")
    return raw_bytes / float(coded_bytes)
```

Do not retarget locked SOTA from this recipe.

