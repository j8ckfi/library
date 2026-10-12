---
id: recipe:soloq
type: recipe
title: SoloQ Calibration-Free dLLM Quantization
method: method:soloq
task: task:fp4-hardware-training
target_hardware: 'dLLM inference PTQ; paper: LLaDA / Dream / Fast-dLLM v2'
framework: PyTorch dLLM PTQ
repo_url: https://github.com/Intelligent-Computing-Lab-Panda/SoloQ
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- soloq
---

# SoloQ Calibration-Free dLLM Quantization

## Hardware & Environment Setup
- Official: `https://github.com/Intelligent-Computing-Lab-Panda/SoloQ`.
- `code_status: announced` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def commit_time_kv(block_committed: bool) -> bool:
    return block_committed
```

No calibration. Do not quantize the live block. Do not retarget Quartet-II.
