---
id: recipe:diem
type: recipe
title: "DIEM Gradient-Alignment Reweight Recipe"
method: method:diem
task: task:math-code-rl-dense
target_hardware: "16x NVIDIA H200 (paper LLM runs) or 8x H100 with a smaller batch"
framework: "PyTorch / veRL"
repo_url: "https://github.com/hrtan/DIEM"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - diem
  - rlvr
  - data-selection
---

# DIEM Gradient-Alignment Reweight Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/hrtan/DIEM`. Plug into an existing GRPO/PPO-family veRL step. Host Pass@1 algorithm stays CISPO.
- Paper LLM config: prompt batch 64, 8 rollouts, mini-batch 32, micro-batch 8 (4 for 7B/8B), lr 1e-6, no KL / entropy bonus on the GRPO baseline, clip 0.2.

## Quickstart Implementation

```python
import torch


def diem_weights(sample_grads: torch.Tensor, eta: float = 1.0) -> torch.Tensor:
    """sample_grads: [N, D] per-example policy gradients (already computed).

    Returns non-negative weights that preserve ||W^T G||_2 vs the unweighted sum.
    """
    g_batch = sample_grads.sum(dim=0)
    importance = eta * (sample_grads @ g_batch)
    gram = sample_grads @ sample_grads.transpose(0, 1)
    gram = gram + 1e-6 * torch.eye(gram.size(0), device=gram.device, dtype=gram.dtype)
    inv = torch.linalg.inv(gram)
    c = g_batch.square().sum().clamp_min(1e-12)
    tmp = inv @ importance
    scale = torch.sqrt((importance * tmp).sum().clamp_min(0.0) / c)
    weights = tmp * scale
    return weights.clamp_min(0.0)
```

## Critical Hyperparameters & Tuning Advice
- Clip negative weights. Do not backprop through the Gram inverse as a learned gate.
- Host algorithm stays CISPO for labeled Pass@1. This mask/reweight does not change that default.
- Distinct from GMTS (token filter) and MAGIC (LDS diagnostic).
