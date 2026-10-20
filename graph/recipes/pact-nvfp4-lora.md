---
id: recipe:pact-nvfp4-lora
type: recipe
title: 'NVFP4 data-flow LoRA on consumer GPUs'
method: method:pact-nvfp4-lora
task: task:4bit-peft-quantization
target_hardware: 'Paper: 16 GB RTX 5080, 1B-3B SLMs'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- pact-nvfp4-lora
---

# NVFP4 data-flow LoRA on consumer GPUs

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def nvfp4_gemm_speedup_vs_bf16() -> tuple[int, int]:
    return 6, 7
```

Do not retarget locked SOTA from this recipe.
