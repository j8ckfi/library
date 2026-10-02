---
id: recipe:taco
type: recipe
title: "TACO Ternary Column-wise One-sparse FT"
method: method:taco
task: task:full-param-memory-efficient-pretrain
target_hardware: "1x NVIDIA H100 80GB; paper: OPT-13B/30B, Qwen3-32B full-param FT"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/Jichao2357/TACO_optimizer"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - taco
  - optimizer
  - memory-efficient
---

# TACO Ternary Column-wise One-sparse FT

## Hardware & Environment Setup
- Official: `https://github.com/Jichao2357/TACO_optimizer`. `code_status: released`.
- ~7B pretrain optimizer stays Muon2. 24GB full-param pretrain subspace stays SCALE.

```bash
git clone https://github.com/Jichao2357/TACO_optimizer.git && cd TACO_optimizer
```

## Quickstart Implementation

```python
from __future__ import annotations


def taco_column_update(grad_col: list[float]) -> list[float]:
    if not grad_col:
        raise ValueError("column gradient is empty")
    best = 0
    best_abs = -1.0
    for i, g in enumerate(grad_col):
        mag = abs(g)
        if mag > best_abs:
            best = i
            best_abs = mag
    if best_abs == 0.0:
        return [0.0] * len(grad_col)
    scale = float(len(grad_col))
    sign = 1.0 if grad_col[best] > 0.0 else -1.0
    out = [0.0] * len(grad_col)
    out[best] = sign * scale
    return out
```

Apply per column of 2D weights. Embeddings / 1D tensors keep a conventional fallback. Use the paper's sparse FP8 heavy-hitter state, not history-free vanilla TACO, under minibatch noise.

## Critical Hyperparameters & Tuning Advice
- Scale \(m/n\) is the dimension-normalization factor, not a free HP.
- Do not swap an AdamW-pretrained checkpoint onto dense Muon and call it TACO.
