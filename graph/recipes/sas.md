---
id: recipe:sas
type: recipe
title: "SAS Gated Sparse Attention"
method: method:sas
task: task:posttrain-attention-sparsification
target_hardware: "8x NVIDIA H20 (paper); train AttnGates only"
framework: "PyTorch / pixi / Triton FlashAttention-style kernel / SGLang block-sparse eval"
repo_url: "https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification"
pip_dependencies: []
tags:
  - recipe
  - sas
  - sparse-attention
---

# SAS Gated Sparse Attention

## Hardware & Environment Setup
- Official: `https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification` (branch `release`).
- Weights: `https://huggingface.co/tencent/Simple-Attention-Sparsification`.
- `pixi install && git submodule update --init --recursive`
- Train: OpenR1-Math-220k, Qwen3-4B/8B/14B, freeze backbone.

## Quickstart Implementation

```bash
export MODEL_PATH=/path/to/Qwen3-4B
export DATA_PATH=/path/to/OpenR1-Math-220k/data
bash scripts/train/simple_sparse_attention_Qwen3-4B.sh
```

Eval (build `third_party/sglang-blocksparse` first):

```bash
export GATES=/path/to/AttnGates
export BUDGET=2048
export TP=1 DP=8
export TASK=math,gpqa,aime24,aime25
bash scripts/eval/run_reasoning.sh
```

Gate sketch:

```python
import torch
import torch.nn.functional as F


def sas_logits(qk: torch.Tensor, gate_scores: torch.Tensor, current_block: int) -> torch.Tensor:
    """Add log-space selector gates; always keep the current block."""
    gates = F.softmax(gate_scores, dim=-1).clamp_min(1e-8).log()
    gates[..., current_block] = 0.0
    return qk + gates.unsqueeze(-2)
```

## Critical Hyperparameters & Tuning Advice
- Paper: block size 64, AdamW 1e-3, cosine, backbone frozen. Tight budgets show the largest gap vs SeerAttention-R.
- Eval needs the sglang-blocksparse fork, not stock SGLang.
