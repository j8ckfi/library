---
id: recipe:staple
type: recipe
title: STAPLE Static Sparse Embedding Upcycle
method: method:staple
task: task:dense-to-moe-upcycling
target_hardware: 'Dense continued-train host with CPU embedding offload; paper: OLMo-2 1B/7B'
framework: PyTorch continued pretrain
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- staple
---

# STAPLE Static Sparse Embedding Upcycle

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def residual_ffn(ffn_out, embed_out):
    if ffn_out is None or embed_out is None:
        raise ValueError("STAPLE keeps FFN and adds embedding residual")
    return ffn_out + embed_out
```

Do not replace the FFN. Do not retarget MASKerade.
