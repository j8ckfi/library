---
id: recipe:kronlstm
type: recipe
title: 'Kronecker-delta linear-attention memory update'
method: method:kronlstm
task: task:linear-time-sequence-modeling
target_hardware: 'Paper: linear-attention LM / long-context benches'
framework: PyTorch
repo_url: https://github.com/NX-AI/KronLSTM
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- kronlstm
---

# Kronecker-delta linear-attention memory update

## Hardware & Environment Setup
- Official: `https://github.com/NX-AI/KronLSTM`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def revision_rank() -> int:
    return 1
```

Do not retarget locked SOTA from this recipe.
