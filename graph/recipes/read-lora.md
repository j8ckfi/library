---
id: recipe:read-lora
type: recipe
title: "READ LoRA Skill Composition"
method: method:read-lora
task: task:lora-skill-composition
target_hardware: "1x GPU matching the source LoRA box; paper: Llama-3.2-3B and Qwen3-4B, r=8"
framework: "PyTorch / PEFT LoRA factors"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
  - "peft"
tags:
  - recipe
  - read-lora
  - lora
  - peft
---

# READ LoRA Skill Composition

## Hardware & Environment Setup
- No official GitHub as of 2026-09-28 (`arXiv:2609.31600`). `repo_url: none found`. `code_status: none`.
- Single-adapter quality stays vanilla LoRA + rsLoRA + LR sweep. 4-bit PEFT stays AQLoRA-Q.

## Quickstart Implementation

```python
from __future__ import annotations

import torch


def canonicalize_lora(b: torch.Tensor, a: torch.Tensor, eps: float = 1e-8) -> tuple[torch.Tensor, torch.Tensor]:
    if b.ndim != 2 or a.ndim != 2:
        raise ValueError("B and A must be rank-2")
    if b.shape[1] != a.shape[0]:
        raise ValueError("inner rank of B and A must match")
    q_b, r_b = torch.linalg.qr(b, mode="reduced")
    q_a, r_a = torch.linalg.qr(a.transpose(0, 1), mode="reduced")
    u, s, vh = torch.linalg.svd(r_b @ r_a.transpose(0, 1), full_matrices=False)
    sigma_sqrt = torch.sqrt(s.clamp_min(eps)).unsqueeze(0)
    b_c = q_b @ (u * sigma_sqrt)
    a_c = (sigma_sqrt.transpose(0, 1) * vh) @ q_a.transpose(0, 1)
    return b_c, a_c


def grow_read_only_g(old_g: torch.Tensor, rank: int, diag_init: float = 0.3) -> torch.Tensor:
    if old_g.ndim != 2 or old_g.shape[0] != old_g.shape[1]:
        raise ValueError("G must be square")
    if rank <= 0:
        raise ValueError("rank must be positive")
    k_r = old_g.shape[0]
    g = old_g.new_zeros(k_r + rank, k_r + rank)
    g[:k_r, :k_r] = old_g
    eye = torch.eye(rank, device=old_g.device, dtype=old_g.dtype)
    g[k_r:, k_r:] = diag_init * eye
    return g


def fold_update(b_stack: torch.Tensor, g: torch.Tensor, a_stack: torch.Tensor) -> torch.Tensor:
    return b_stack @ g @ a_stack
```

Canonicalize every incoming adapter. Install frozen \(G^{(k)}\), keep the write column at zero, and train only the new row/diagonal. Fold once per module and serve the merged projection.

## Critical Hyperparameters & Tuning Advice
- Paper source adapters: \(r=8\), \(\alpha=16\), q/v only. New-diagonal init \(0.3 I_r\). One pass over the stage task union per append.
- Do not train old \(G\) blocks or any canonical factors. Write column stays zero.
- Do not retarget lr-matters-lora or AQLoRA-Q from the SuperGLUE / Domain lifts.
