---
id: recipe:bitnet-b158
type: recipe
title: "Training 1.58-Bit Ternary Networks with BitLinear Layers"
method: method:bitnet-b158
task: task:1bit-extreme-quantization
target_hardware: "1x NVIDIA A100 / H100 80GB (or multi-GPU cluster)"
framework: "PyTorch 2.5+ / Straight-Through Estimator (STE)"
repo_url: "https://github.com/microsoft/BitNet"
pip_dependencies:
  - "torch>=2.5.0"
  - "einops>=0.8.0"
tags:
  - quantization
  - 1bit
  - ternary
  - bitnet
---

# Training 1.58-Bit Ternary Networks with BitLinear Layers

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA H100 SXM 80GB.
- Software: PyTorch 2.5.0+.

## Quickstart Code

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def weight_quant(w: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """Ternary weight quantization: w_quant in {-1, 0, +1} using Straight-Through Estimator (STE)."""
    gamma = torch.mean(torch.abs(w)).clamp(min=eps)
    w_scaled = w / gamma
    w_quant = torch.clamp(torch.round(w_scaled), -1.0, 1.0)
    # STE: detach gradient during backward pass
    return w + (w_quant * gamma - w).detach()

def activation_quant(x: torch.Tensor, eps: float = 1e-5, q_b: int = 127) -> torch.Tensor:
    """8-bit symmetric activation quantization for BitLinear."""
    gamma = torch.max(torch.abs(x), dim=-1, keepdim=True)[0].clamp(min=eps)
    x_scaled = x * (q_b / gamma)
    x_quant = torch.clamp(torch.round(x_scaled), -q_b, q_b)
    return x + (x_quant * (gamma / q_b) - x).detach()

class BitLinear(nn.Linear):
    """BitLinear layer replacing FP16 nn.Linear in BitNet b1.58."""
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # RMSNorm activation preprocessing
        variance = x.pow(2).mean(-1, keepdim=True)
        x_norm = x * torch.rsqrt(variance + 1e-5)
        
        # Quantize activations (8-bit) and weights (ternary {-1, 0, 1})
        x_q = activation_quant(x_norm)
        w_q = weight_quant(self.weight)
        
        return F.linear(x_q, w_q, self.bias)

# Example Transformer MLP block with BitLinear:
class BitNetMLP(nn.Module):
    def __init__(self, d_model: int = 2048, d_ff: int = 5632):
        super().__init__()
        self.gate_proj = BitLinear(d_model, d_ff, bias=False)
        self.up_proj = BitLinear(d_model, d_ff, bias=False)
        self.down_proj = BitLinear(d_ff, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.down_proj(F.silu(self.gate_proj(x)) * self.up_proj(x))
```

## Critical Hyperparameters
- **Learning Rate**: 1.5e-3 (higher than standard FP16 transformers to facilitate integer threshold crossings).
- **Optimizer**: AdamW with \(\beta_1=0.9, \beta_2=0.95\) and weight decay 0.01.
- **Activation Precision**: 8-bit quantization is required for activation stability.
