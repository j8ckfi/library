---
id: recipe:mhc
type: recipe
title: "Manifold-Constrained Hyper-Connections (mHC) Recipe"
method: method:mhc
task: task:llm-pretraining-optimization
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - architecture
  - hyper-connections
  - mhc
---

# Manifold-Constrained Hyper-Connections (mHC) Recipe

## Quickstart Implementation

```python
import torch
import torch.nn as nn

def sinkhorn_knopp(matrix: torch.Tensor, num_iters: int = 20, eps: float = 1e-6) -> torch.Tensor:
    """Projects a square matrix onto the Birkhoff polytope of doubly stochastic matrices."""
    p = torch.exp(matrix)
    for _ in range(num_iters):
        p = p / (p.sum(dim=-1, keepdim=True) + eps)
        p = p / (p.sum(dim=-2, keepdim=True) + eps)
    return p

class ManifoldConstrainedHyperConnections(nn.Module):
    """Manifold-Constrained Hyper-Connections (mHC) module for n-stream residual expansion."""
    def __init__(self, dim: int, stream_expansion: int = 4):
        super().__init__()
        self.dim = dim
        self.n = stream_expansion
        self.raw_res_mix = nn.Parameter(torch.eye(self.n) + 0.01 * torch.randn(self.n, self.n))
        self.h_pre = nn.Parameter(torch.ones(1, self.n) / self.n)
        self.h_post = nn.Parameter(torch.ones(1, self.n) / self.n)

    def forward(self, x_stream: torch.Tensor, layer_fn) -> torch.Tensor:
        # x_stream: [batch, seq_len, n, dim]
        h_res = sinkhorn_knopp(self.raw_res_mix)
        x_mixed = torch.einsum("ij,bsjd->bsid", h_res, x_stream)
        layer_in = torch.einsum("i,bsid->bsd", self.h_pre.squeeze(0), x_stream)
        layer_out = layer_fn(layer_in)
        out_expanded = torch.einsum("i,bsd->bsid", self.h_post.squeeze(0), layer_out)
        return x_mixed + out_expanded
```
