---
id: recipe:gapo
type: recipe
title: "GAPO Adaptive Clip Plug-in"
method: method:gapo
task: task:math-code-rl-dense
target_hardware: "8x NVIDIA H200 141GB (paper); 8x H100 80GB is the usual host RLVR box"
framework: "PyTorch / veRL"
repo_url: "https://github.com/Sheng-J/GAPO"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - gapo
  - rlvr
  - clipping
---

# GAPO Adaptive Clip Plug-in

## Hardware & Environment Setup
- Official code: `https://github.com/Sheng-J/GAPO`. Clone, `pip install -e .`, pin verl to `9bda8b9a`, apply `patches/gapo-verl-9bda8b9a.patch`.
- Paper runs: 8x H200, torch 2.9.0+cu128, vLLM 0.12.0, flash-attn 2.8.3, ray 2.55.0. Host algorithm for Pass@1 labeled RLVR stays CISPO; this only replaces the clip width on a GRPO/GSPO surrogate.
- Scripts in the repo: Qwen2.5-Math-1.5B `(7e-4, 1.5e-3)` or `(3e-3, 5e-3)`; R1-Distill-Qwen-1.5B `(7e-5, 3e-4)`. Prefer $k=16$ over $k=8$ when budget allows.

## Quickstart Implementation

```python
import torch


def adaptive_upper_clip(
    correct: torch.Tensor,
    group_ids: torch.Tensor,
    eps_lo: float,
    eps_hi_max: float,
) -> torch.Tensor:
    """Per-rollout ε_hi. correct is a boolean [B]; group_ids is [B] prompt ids.

    Correct rollouts: ε_lo + (ε_hi_max - ε_lo) * (k - c) / (k - 1).
    Incorrect rollouts and c=0 groups keep ε_lo. k=1 groups get ε_hi_max if correct.
    """
    b = correct.shape[0]
    eps_hi = torch.full((b,), float(eps_lo), dtype=torch.float32, device=correct.device)
    delta = float(eps_hi_max) - float(eps_lo)
    if delta == 0.0:
        return eps_hi
    for gid in group_ids.unique():
        idx = (group_ids == gid).nonzero(as_tuple=False).squeeze(-1)
        k = int(idx.numel())
        c = int(correct[idx].sum().item())
        for i in idx.tolist():
            if not bool(correct[i]) or c == 0:
                continue
            if k == 1:
                eps_hi[i] = float(eps_hi_max)
                continue
            t = (k - c) / (k - 1)
            eps_hi[i] = float(eps_lo) + delta * t
    return eps_hi


def gapo_clip_ratio(ratio: torch.Tensor, advantages: torch.Tensor, eps_lo: float, eps_hi: torch.Tensor) -> torch.Tensor:
    """PPO/GSPO surrogate with a per-row upper clip. ratio, advantages: [B, T]; eps_hi: [B]."""
    upper = (1.0 + eps_hi.to(ratio)).unsqueeze(-1)
    clipped = ratio.clamp(min=1.0 - eps_lo)
    clipped = torch.minimum(clipped, upper)
    unclipped = -advantages * ratio
    clipped_loss = -advantages * clipped
    return torch.maximum(unclipped, clipped_loss)
```

## Critical Hyperparameters & Tuning Advice
- Token-IS: $(\epsilon_{\mathrm{lo}},\epsilon_{\mathrm{hi}}^{\max})=(0.2,0.28)$. Sequence-IS: $(3\times10^{-3},5\times10^{-3})$; long-context R1-Distill $(7\times10^{-5},3\times10^{-4})$.
- Linear scarcity is the reported default. Do not reward-shape advantages on top of this unless you are reproducing an ablation.
- Host algorithm stays CISPO for Pass@1 labeled RLVR. GAPO does not replace OPD, OPSA, or CANOPY.
