---
id: recipe:musec
type: recipe
title: "Soft Musec Spectral Clipping"
method: method:musec
task: task:llm-pretraining-optimization
target_hardware: "modded-nanogpt host (paper); transfer onto a Muon2 7B run at your cluster scale"
framework: "PyTorch / Muon Newton–Schulz host"
repo_url: "https://github.com/kellerjordan/modded-nanogpt"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - musec
  - muon
  - optimizer
---

# Soft Musec Spectral Clipping

## Hardware & Environment Setup
- No dedicated Musec repo as of 2026-09-11. Paper experiments sit on `https://github.com/kellerjordan/modded-nanogpt`.
- ~7B optimizer default stays Muon2. Trillion-scale MoE stays MuonClip. This snippet replaces Muon's flatten-to-one with a soft spectral clip.

## Quickstart Implementation

```python
import torch


def newton_schulz_orthogonalize(G: torch.Tensor, steps: int = 5, eps: float = 1e-7) -> torch.Tensor:
    a, b, c = 3.4445, -4.7750, 2.0315
    X = G.bfloat16()
    X = X / (X.norm() + eps)
    if G.size(0) > G.size(1):
        X = X.T
        transposed = True
    else:
        transposed = False
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    return X.T if transposed else X


def soft_musec_update(momentum: torch.Tensor, clip: float = 1.0, steps: int = 5) -> torch.Tensor:
    """Soft-clip momentum singular values via coupled Newton–Schulz; keep spectrum shape."""
    scale = momentum.norm() + 1e-7
    direction = newton_schulz_orthogonalize(momentum, steps=steps)
    raw_scale = (momentum * direction).sum() / (direction.norm() ** 2 + 1e-7)
    clipped = clip * torch.tanh(raw_scale / clip)
    return clipped * direction * (scale / (scale.detach()))
```

## Critical Hyperparameters & Tuning Advice
- `clip` is the spectral threshold (paper ablates it). Start at 1.0 and raise if the run is already stable under Muon2.
- Keep embeddings / `lm_head` on AdamW.
- Expect stability vs Muon flattening, not a free FineWeb win vs Muon2.
