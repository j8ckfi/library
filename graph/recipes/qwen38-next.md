---
id: recipe:qwen38-next
type: recipe
title: "Qwen3.8-Next GDN Kernel and Optimizer Split"
method: method:qwen38-next
task: task:pretrain-moe-frontier
target_hardware: "NVIDIA Hopper or Blackwell (SM90+)"
framework: "PyTorch 2.8+ / FlashQLA / TileLang"
repo_url: "https://github.com/QwenLM/FlashQLA"
pip_dependencies:
  - "torch>=2.8.0"
  - "flash-qla"
tags:
  - recipe
  - qwen38-next
  - flashqla
  - gated-deltanet
---

# Qwen3.8-Next GDN Kernel and Optimizer Split

## Hardware & Environment Setup
- Public code is FlashQLA only (`pip install flash-qla`). CUDA 12.8+, PyTorch 2.8+, SM90/SM100/SM103/SM120/SM121.
- Full Qwen3.8-Flash-Next pretrain stack is not released; use this kernel plus the paper's optimizer split.

## Quickstart Implementation

```python
from flash_qla import chunk_gated_delta_rule

o, final_state = chunk_gated_delta_rule(
    q=q,
    k=k,
    v=v,
    g=g,
    beta=beta,
    scale=scale,
    initial_state=initial_state,
    output_final_state=True,
    cu_seqlens=cu_seqlens,
)
```

Muon on 2D linear maps; AdamW on embeddings, n-gram tables, `lm_head`, MoE router, and Gated Residual low-rank projections. Split fused parameters before orthogonalization. Newton–Schulz 8 steps. Do not ramp batch size.

## Critical Hyperparameters & Tuning Advice
- Hybrid schedule: one full-attention (later QSA) layer in every four; remaining token mixers GDN.
- QSA CPT: $K=2048$, $r=4$, 256K sequence, indexer KL then sparse backbone.
- This recipe does not replace Muon2 as the ~7B optimizer default or DeepSeek-V4/Kimi-K3 as MoE architecture defaults.
