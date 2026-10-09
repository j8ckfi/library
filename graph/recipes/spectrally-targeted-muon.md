---
id: recipe:spectrally-targeted-muon
type: recipe
title: "Spectrally Targeted Muon Thresholded Orthogonalization"
method: method:spectrally-targeted-muon
task: task:llm-pretraining-optimization
target_hardware: "Muon-family matrix optimizer; paper: CIFAR-10 / NanoGPT"
framework: "PyTorch Muon host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - spectrally-targeted-muon
---

# Spectrally Targeted Muon Thresholded Orthogonalization

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def use_full_muon(all_sv_below_one: bool) -> bool:
    return bool(all_sv_below_one)
```

If every momentum singular value is far below one, amplify them (full Muon). Do not retarget Muon2.
