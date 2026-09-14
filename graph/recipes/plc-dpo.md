---
id: recipe:plc-dpo
type: recipe
title: "PLC-DPO Posterior Label Correction"
method: method:plc-dpo
task: task:direct-preference-alignment
target_hardware: "1-2 GPU LoRA (repo default: LoRA rank 16, effective batch 64)"
framework: "PyTorch 2.10 / CUDA 12.8 / flash-attn 2.8.3"
repo_url: "https://github.com/VennTum99/PLC-DPO"
pip_dependencies:
  - "torch==2.10.0"
  - "flash-attn==2.8.3"
tags:
  - recipe
  - plc-dpo
  - dpo
  - preference-alignment
---

# PLC-DPO Posterior Label Correction

## Hardware & Environment Setup
- Official: `https://github.com/VennTum99/PLC-DPO` (EMNLP 2026 Findings).
- `python -m pip install -r requirements/train.txt && python -m pip install -e .`
- Data: `python -m plcdpo.prepare_data --dataset ultrafeedback-binarized`
- Open stack stays OLMo-3 Dolci. Simple clean prefs stay SimPO.

## Quickstart Implementation

```bash
python -m plcdpo.prepare_data --dataset ultrafeedback-binarized
CUDA_VISIBLE_DEVICES=0,1 NPROC_PER_NODE=2 bash scripts/train.sh \
  --config configs/train.yaml configs/models/qwen2.5-1.5b.yaml \
  configs/datasets/ultrafeedback-binarized.yaml configs/methods/plc-dpo-balanced.yaml \
  --set output_dir=outputs/qwen1.5b-plc
```

Routing sketch (policy-reference margin → clean / flip / tie):

```python
import torch
import torch.nn.functional as F


def plc_dpo_weights(margin: torch.Tensor, tau_dir: float, tau_tie: float) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Calibrated margin; mix forward DPO, reversed DPO, and a tie regularizer."""
    clean, flip = F.softmax(torch.stack([margin, -margin], dim=0) / tau_dir, dim=0)
    tie = torch.sigmoid(-margin.abs() / tau_tie)
    keep = 1.0 - tie
    return keep * clean, keep * flip, tie
```

## Critical Hyperparameters & Tuning Advice
- Start from `plc-dpo-balanced.yaml` (\(\alpha=0.99\), \(\tau_{\mathrm{dir}}=0.75\), \(\tau_{\mathrm{tie}}=1.0\), warm-up 0.10, \(\gamma_{\max}=0.70\), \(\kappa=1.0\)).
- LoRA rank 16, LR 1e-5, one epoch. Separate eval env for vLLM (`requirements/eval.txt`).
