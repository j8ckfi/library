---
id: recipe:moe-sparsity-hp-scaling
type: recipe
title: "MoE Sparsity LR/Batch Scaling"
method: method:moe-sparsity-hp-scaling
task: task:pretrain-moe-frontier
target_hardware: "MoE pretrain cluster (paper: H800-hours at 6B–12B)"
framework: "PyTorch"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - moe
  - hyperparameters
  - moe-sparsity-hp-scaling
---

# MoE Sparsity LR/Batch Scaling

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Architecture default stays DeepSeek-V4 / Kimi-K3.

## Quickstart Implementation

```python
def scale_batch(tokens: float, activation: float, b0: float, d_exp: float, a_exp: float) -> float:
    """B* ∝ D^{d_exp} * A^{a_exp} at the paper's fixed-sparsity-then-A form."""
    return b0 * (tokens ** d_exp) * (activation ** a_exp)


def scale_lr(compute: float, activation: float, lr0: float, c_exp: float, a_exp: float) -> float:
    """η* ∝ C^{c_exp} * A^{a_exp}. Robust to size/data split at fixed sparsity."""
    return lr0 * (compute ** c_exp) * (activation ** a_exp)
```

## Critical Hyperparameters & Tuning Advice
- Fit exponents on a sparsity family you control; do not copy dense μP LR blindly onto ultra-sparse MoE.
- Held-out check in the paper is 12B / 1/64. Re-check before a frontier run.
