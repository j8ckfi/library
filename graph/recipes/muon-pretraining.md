---
id: recipe:muon-pretraining
type: recipe
title: "Pretraining LLM Matrix Weights with the Muon Optimizer"
method: method:muon-optimizer
task: task:llm-pretraining-optimization
target_hardware: "1x NVIDIA H100 80GB (or 8x H100 for distributed pretraining)"
framework: "PyTorch 2.5+ (torch.compile recommended)"
repo_url: "https://github.com/KellerJordan/modded-nanogpt"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - optimizer
  - pretraining
  - pytorch
---

# Pretraining LLM Matrix Weights with the Muon Optimizer

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA H100 SXM 80GB (or 8x H100 cluster for DDP/FSDP).
- Minimum GPU Memory: 24GB VRAM (RTX 4090 with batch size reduction).
- PyTorch Version: PyTorch 2.5.0+ with CUDA 12.4+.

## Quickstart Code

```python
import torch
import torch.nn as nn

@torch.compile
def zeropower_via_newtonschulz5(G: torch.Tensor, steps: int = 5, eps: float = 1e-7) -> torch.Tensor:
    """Computes nearest orthogonal matrix via 5th-order Newton-Schulz polynomial iteration."""
    assert G.ndim >= 2
    a, b, c = (3.4445, -4.7750,  2.0315)
    X = G.bfloat16() / (G.norm() + eps)
    if G.size(0) > G.size(1):
        X = X.T
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    if G.size(0) > G.size(1):
        X = X.T
    return X.to(G.dtype)

class Muon(torch.optim.Optimizer):
    """Muon optimizer for 2D internal weight matrices in neural networks."""
    def __init__(self, params, lr: float = 0.02, momentum: float = 0.95, nesterov: bool = True, ns_steps: int = 5):
        defaults = dict(lr=lr, momentum=momentum, nesterov=nesterov, ns_steps=ns_steps)
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self):
        for group in self.param_groups:
            lr = group["lr"]
            momentum = group["momentum"]
            nesterov = group["nesterov"]
            ns_steps = group["ns_steps"]
            for p in group["params"]:
                if p.grad is None:
                    continue
                g = p.grad
                state = self.state[p]
                if "momentum_buffer" not in state:
                    state["momentum_buffer"] = torch.zeros_like(g)
                buf = state["momentum_buffer"]
                buf.mul_(momentum).add_(g)
                u = g + momentum * buf if nesterov else buf
                u = zeropower_via_newtonschulz5(u, steps=ns_steps)
                # Apply update scaled by spectral norm approximation
                p.data.add_(u, alpha=-lr * max(1, p.size(0) / p.size(1))**0.5)

# Example Hybrid Training Loop Setup:
def create_optimizers(model: nn.Module, muon_lr: float = 0.02, adamw_lr: float = 3e-4):
    muon_params = []
    adamw_params = []
    for name, p in model.named_parameters():
        if p.requires_grad:
            # 2D weight matrices (linear projections) go to Muon; 1D (biases, norms, embeddings) to AdamW
            if p.ndim == 2 and "embed" not in name and "head" not in name:
                muon_params.append(p)
            else:
                adamw_params.append(p)

    opt_muon = Muon(muon_params, lr=muon_lr, momentum=0.95)
    opt_adamw = torch.optim.AdamW(adamw_params, lr=adamw_lr, betas=(0.9, 0.95), weight_decay=0.01)
    return [opt_muon, opt_adamw]
```

## Critical Hyperparameters & Guidance
- **Muon Learning Rate**: 0.02 to 0.05 with Cosine Decay Schedule down to 0.002.
- **AdamW Learning Rate**: 3e-4 to 1e-3 (for embeddings and norm layers).
- **Newton-Schulz Iterations**: 5 steps is optimal for FP32/BF16 convergence.
