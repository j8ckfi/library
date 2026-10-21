---
id: recipe:e8-qat
type: recipe
title: 'Implicit E8-lattice 2-bit QAT'
method: method:e8-qat
task: task:full-lowbit-finetune
target_hardware: 'Paper: Qwen3.6-35B-A3B'
framework: PyTorch
repo_url: https://github.com/lxy2137/E8_QAT
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- e8-qat
---

# Implicit E8-lattice 2-bit QAT

## Hardware & Environment Setup
- Official: `https://github.com/lxy2137/E8_QAT`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def e8_group_size() -> int:
    return 8
```

Do not retarget locked SOTA from this recipe.
