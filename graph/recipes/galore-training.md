---
id: recipe:galore-training
type: recipe
title: "Pretraining and Fine-Tuning with GaLore Gradient Low-Rank Projection"
method: method:galore
task: task:parameter-efficient-fine-tuning
target_hardware: "1x NVIDIA RTX 3090 / 4090 (24GB VRAM)"
framework: "PyTorch 2.5+ / GaLore"
repo_url: "https://github.com/jiaweizzhao/GaLore"
pip_dependencies:
  - "torch>=2.5.0"
  - "galore-torch>=0.3.0"
  - "transformers>=4.48.0"
tags:
  - optimizer
  - peft
  - galore
---

# Pretraining and Fine-Tuning with GaLore Gradient Low-Rank Projection

## Hardware & Environment Setup
- Recommended Hardware: Single 24GB GPU (RTX 4090, RTX 3090, A10G).
- Python Packages: `galore-torch>=0.3.0`, `transformers`.

## Quickstart Code

```python
import torch
from transformers import AutoModelForCausalLM
from galore_torch import GaLoreAdamW8bit

def setup_galore_optimizer(model, lr=1e-4, rank=128, update_proj_gap=200):
    # Separate projection matrices from standard 1D parameters
    galore_params = []
    regular_params = []
    
    for name, p in model.named_parameters():
        if p.requires_grad:
            if "attn" in name or "mlp" in name:
                galore_params.append(p)
            else:
                regular_params.append(p)
                
    param_groups = [
        {"params": regular_params, "lr": lr},
        {
            "params": galore_params,
            "lr": lr,
            "rank": rank,
            "update_proj_gap": update_proj_gap,
            "scale": 0.25,
            "proj_type": "std"
        }
    ]
    
    optimizer = GaLoreAdamW8bit(param_groups)
    return optimizer
```
