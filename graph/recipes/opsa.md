---
id: recipe:opsa
type: recipe
title: "OPSA On-Policy Self-Adaptation Recipe"
method: method:opsa
task: task:teacher-free-on-policy-self-adaptation
target_hardware: "8x NVIDIA GPU (paper: 4 actor + 4 rollout)"
framework: "PyTorch / slime / Megatron-LM"
repo_url: "https://github.com/DripNowhy/On-Policy-Self-Adaptation"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - opsa
  - slime
  - teacher-free
---

# OPSA On-Policy Self-Adaptation Recipe

## Hardware & Environment Setup
- Paper launcher: 8 GPUs, 4 actor + 4 rollout, 700 steps, eval every 20. Canonical model Qwen3-1.7B.
- Install from the slime snapshot in the official repo:

```bash
git clone https://github.com/DripNowhy/On-Policy-Self-Adaptation.git
cd On-Policy-Self-Adaptation/slime
pip install -e .
```

Train on DAPO-17k questions only (labels unused). Project page: `https://dripnowhy.github.io/On-Policy-Self-Adaptation/`

## Quickstart Implementation

```python
import torch


def opsa_advantages(logp: torch.Tensor, entropy: torch.Tensor, valid: torch.Tensor, fraction: float = 0.2) -> torch.Tensor:
    """Entropy-adaptive negative advantages on the lowest-logp valid tokens.

    logp, entropy, valid: [T] response-token tensors. Advantages in [-1.0, -0.5]
    on the selected set; zeros elsewhere. High entropy -> more negative.
    """
    idx = torch.nonzero(valid, as_tuple=False).squeeze(-1)
    adv = torch.zeros_like(logp)
    if idx.numel() == 0:
        return adv
    k = max(1, int(idx.numel() * fraction))
    selected = idx[torch.topk(logp[idx], k=k, largest=False).indices]
    h = entropy[selected]
    h_min = h.min()
    h_max = h.max()
    scale = (h - h_min) / (2.0 * (h_max - h_min).clamp_min(1e-8))
    adv[selected] = -0.5 - scale
    return adv


def opsa_loss(logp: torch.Tensor, advantages: torch.Tensor, valid: torch.Tensor) -> torch.Tensor:
    mask = valid & (advantages != 0)
    if not mask.any():
        return logp.new_zeros(())
    return -(advantages[mask] * logp[mask]).mean()
```

## Critical Hyperparameters & Tuning Advice
- Keep fraction 0.2 (lowest 20% logp). 10% underperforms; 30–40% also work.
- Advantages are always negative. Do not assign positive advantages to this set.
- Eval: 32 samples, temperature 0.7, top-k 20, top-p 0.8, max length 32768.
- Official launcher: `bash examples/opsa/run_opsa.sh --model qwen3-1.7b --preset opsa --fraction 0.2` with HF + Megatron checkpoints.
