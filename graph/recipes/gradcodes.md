---
id: recipe:gradcodes
type: recipe
title: "GradCodeS Fully Low-Bit Fine-Tune Recipe"
method: method:gradcodes
task: task:full-lowbit-finetune
target_hardware: "1x NVIDIA GPU 24GB+"
framework: "PyTorch / torchrun"
repo_url: "https://github.com/ovo67/GradCodes"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "lm-eval"
tags:
  - recipe
  - gradcodes
  - quantization
  - 4bit
---

# GradCodeS Fully Low-Bit Fine-Tune Recipe

## Hardware & Environment Setup

```bash
git clone https://github.com/ovo67/GradCodes.git
cd GradCodes
pip install -r requirements.txt
CUDA_VISIBLE_DEVICES=0 torchrun --standalone --nproc_per_node=1 \
  src/train_gradcodes.py --dataset gsm8k
```

## Quickstart Implementation

```python
import torch


def code_surrogate_grad(weight_grad: torch.Tensor, scale: torch.Tensor, gap_plus: torch.Tensor, gap_minus: torch.Tensor) -> torch.Tensor:
    """Effective-step code gradient: weight_grad * scale * descent-aligned codebook gap."""
    pos = weight_grad > 0
    step = torch.where(pos, gap_minus, gap_plus)
    return weight_grad * scale * step


def select_lowest_loss(candidates: list[torch.Tensor], losses: torch.Tensor) -> torch.Tensor:
    """Keep the deployable code tensor with lowest realized loss; ties keep index 0."""
    return candidates[int(torch.argmin(losses).item())]
```

## Critical Hyperparameters & Tuning Advice
- Datatype: NF4 or MXFP4 over INT4 in the paper sweep.
- Accept updates only on realized deployed loss. Do not follow $Z^{\mathrm{ref}}$ as a real-valued code.
- Full-matrix vs LoRA code parameterization both work; LoRA-rank 8 is the paper default for the structured variant.
- This is not AQLoRA-Q (mixed adapter) and not Quartet-II (native FP4 pretrain).
