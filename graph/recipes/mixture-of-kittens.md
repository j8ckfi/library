---
id: recipe:mixture-of-kittens
type: recipe
title: "Mixture-of-Kittens (MoK) Training Recipe"
method: method:mixture-of-kittens
task: task:train-moe-nvl72
target_hardware: "NVIDIA GB300 NVL72 / GB200 NVL72 (Blackwell SM100/SM103)"
framework: "PyTorch 2.10+, CUDA 13.0+"
repo_url: "https://github.com/cursor/mixture-of-kittens"
pip_dependencies:
  - "torch>=2.10.0"
  - "thunderkittens"
tags:
  - recipe
  - systems
  - moe
  - megakernel
  - nvl72
  - mxfp8
  - bf16
---

# Mixture-of-Kittens (MoK) Training Recipe

## Hardware & Environment Requirements
- **Target Hardware**: NVIDIA Blackwell NVL72 racks (GB200 NVL72 or GB300 NVL72 with SM100/SM103 GPUs).
- **Software Dependencies**: PyTorch 2.10+, CUDA Toolkit 13.0+, ThunderKittens.

## Quickstart Implementation

```python
import torch

try:
    import mok.functional as mok_fn
    import mok.ops as mok_ops
except ImportError:
    mok_fn = None
    mok_ops = None

def run_mok_moe_step(
    x: torch.Tensor,
    router_weights: torch.Tensor,
    shared_gate: torch.Tensor,
    shared_up: torch.Tensor,
    shared_down: torch.Tensor,
    routed_gate_fp8: torch.Tensor,
    routed_gate_sc: torch.Tensor,
    routed_up_fp8: torch.Tensor,
    routed_up_sc: torch.Tensor,
    routed_down_fp8: torch.Tensor,
    routed_down_sc: torch.Tensor,
    config=None,
    group=None,
    topk: int = 8,
    num_local_experts: int = 8,
):
    """Executes a fused MoE forward pass with Mixture-of-Kittens on Blackwell NVL72."""
    if mok_fn is None:
        raise RuntimeError("Mixture-of-Kittens (mok) requires Blackwell SM100/SM103 with PyTorch 2.10+ and CUDA 13+.")

    num_local_tokens, hidden_size = x.shape[0], x.shape[1]
    workspace = mok_fn.get_workspace(
        config,
        group,
        device=x.device,
        num_local_tokens=num_local_tokens,
        hidden_size=hidden_size,
        topk=topk,
    )

    topk_experts = torch.topk(router_weights, k=topk, dim=-1).indices
    schedule = mok_fn.build_schedule(
        workspace,
        config,
        topk_experts,
        num_local_experts=num_local_experts,
    )

    output, ctx = mok_fn.forward(
        config,
        workspace,
        schedule,
        x,
        router_weights,
        shared_gate,
        shared_up,
        shared_down,
        (routed_gate_fp8, routed_gate_sc),
        (routed_up_fp8, routed_up_sc),
        (routed_down_fp8, routed_down_sc),
    )
    return output, ctx
```
