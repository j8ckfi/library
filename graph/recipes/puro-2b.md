---
id: recipe:puro-2b
type: recipe
title: "Puro-2B Budget Consumer Pretrain Recipe"
method: method:puro-2b
task: task:budget-consumer-pretrain
target_hardware: "Phase 1: 24x RTX 5090 32GB; Phase 2: 96x RTX 5090 32GB"
framework: "Megatron Core v0.16 / Transformer Engine / PyTorch (blockwise FP8)"
repo_url: "https://github.com/thu-pacman/Puro-Megatron"
pip_dependencies:
  - "torch>=2.6.0"
  - "transformer-engine>=2.0.0"
tags:
  - recipe
  - pretraining
  - fp8
  - muonh
  - puro-2b
---

# Puro-2B Budget Consumer Pretrain Recipe

## Hardware & Environment Setup
- Phase 1: 24x RTX 5090, PP=2 DP=12, no TP. Phase 2: 96x RTX 5090, PP=4 DP=24, no TP.
- Megatron Core v0.16 + Transformer Engine. Sequence 4096, global batch 1536 sequences.
- Optional unsupported NVIDIA driver P2P/GDR tweaks for PCIe/IB bandwidth. Stock drivers run the same recipe at lower interconnect BW.
- Data materialization: `https://github.com/thu-pacman/Kaiyuan-Spark`. Checkpoints: `https://huggingface.co/collections/thu-pacman/puro-2b`.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def muonh_step(weight: torch.Tensor, muon_update: torch.Tensor, eta: torch.Tensor, radius: torch.Tensor) -> torch.Tensor:
    """Hyperball Muon step: unit-normalize the Muon update, displace by eta * R, project to ||W0||_F.

    Wrap scale-invariant 2D attn/MLP matrices only. Embeddings, LN, lm_head, and the rest stay AdamW.
    Production Hyperball LR is 10x the AdamW base LR.
    """
    u_hat = muon_update / muon_update.norm(p="fro").clamp_min(1e-12)
    displaced = weight - eta * radius * u_hat
    return radius * F.normalize(displaced.flatten(), dim=0).view_as(weight)


def average_late_checkpoints(states: list[dict[str, torch.Tensor]]) -> dict[str, torch.Tensor]:
    """Equal-weight average of the six late CMA checkpoints (optimizer states are not averaged)."""
    keys = states[0].keys()
    n = float(len(states))
    return {k: sum(s[k] for s in states) / n for k in keys}
```

Production schedule: FP8 E4M3 GEMMs from init (128 / 128x128 block scales, MXFP8 on SM120); master weights and opt states BF16/FP32; Phase 1 power LR then Phase 2 linear decay; CMA holds base LR at $4.08\times 10^{-5}$ (Hyperball $4.08\times 10^{-4}$) from step 218,000 and averages 6 late ckpts over 376 within-source buckets.

## Critical Hyperparameters & Tuning Advice
- **MuonH radius** $R=\|W_0\|_F$ is frozen per wrapped matrix. Do not let weight decay change that radius.
- **Do not enable TP** on this interconnect. PP+DP only.
- **FP8 is not NVFP4.** Keep `method:quartet-ii` for native FP4 hardware training.
- **7B default unchanged**: this recipe is not a substitute for `method:muon2` + KL-SOAP or OLMo-3 7B.
