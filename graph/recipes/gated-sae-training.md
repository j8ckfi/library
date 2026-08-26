---
id: recipe:gated-sae-training
type: recipe
title: "Training Gated Sparse Autoencoders (Gated SAE) for Circuit Extraction"
method: method:gated-sae
task: task:mechanistic-interpretability-dictionaries
target_hardware: "1x NVIDIA A100 / H100 80GB"
framework: "PyTorch 2.5+ / SAELens / TransformerLens"
repo_url: "https://github.com/jbloomAus/SAELens"
pip_dependencies:
  - "torch>=2.5.0"
  - "sae-lens>=3.0.0"
  - "transformer-lens>=2.0.0"
tags:
  - interpretability
  - mechanistic
  - sae
  - circuits
---

# Training Gated Sparse Autoencoders (Gated SAE) for Circuit Extraction

## Hardware & Environment Setup
- Recommended Hardware: 1x NVIDIA A100 (80GB) or H100 (80GB).
- Python Packages: `sae-lens>=3.0.0`, `transformer-lens`.

## Quickstart Code

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GatedSAE(nn.Module):
    """Gated Sparse Autoencoder eliminating L1 shrinkage bias."""
    def __init__(self, d_in: int = 4096, d_hidden: int = 65536, l1_coeff: float = 5.0):
        super().__init__()
        self.d_in = d_in
        self.d_hidden = d_hidden
        self.l1_coeff = l1_coeff

        self.b_dec = nn.Parameter(torch.zeros(d_in))
        
        # Gating Pathway parameters
        self.W_gate = nn.Parameter(torch.randn(d_in, d_hidden) * (1 / d_in**0.5))
        self.b_gate = nn.Parameter(torch.zeros(d_hidden))
        self.r_mag = nn.Parameter(torch.zeros(d_hidden))  # Learned magnitude bias scaling
        
        # Decoder (normalized dictionary vectors)
        self.W_dec = nn.Parameter(torch.randn(d_hidden, d_in) * (1 / d_hidden**0.5))

    def forward(self, x: torch.Tensor):
        x_cent = x - self.b_dec
        
        # 1. Gating pathway pre-activations
        pi_gate_pre = x_cent @ self.W_gate + self.b_gate
        f_gate = (pi_gate_pre > 0).float()
        
        # 2. Magnitude pathway (shares direction with W_gate via r_mag scaling)
        W_mag = self.W_gate * torch.exp(self.r_mag)
        b_mag = self.b_gate * torch.exp(self.r_mag)
        f_mag = F.relu(x_cent @ W_mag + b_mag)
        
        # 3. Gated feature activations
        f_gated = f_gate * f_mag
        
        # 4. Reconstruction
        x_reconstruct = f_gated @ self.W_dec + self.b_dec
        
        # Loss: Reconstruction MSE + L1 penalty on gating pre-activations only
        mse_loss = F.mse_loss(x_reconstruct, x)
        sparsity_loss = self.l1_coeff * F.relu(pi_gate_pre).sum(dim=-1).mean()
        
        total_loss = mse_loss + sparsity_loss
        l0_sparsity = (f_gated > 0).float().sum(dim=-1).mean()
        
        return total_loss, mse_loss, l0_sparsity, x_reconstruct
```

## Critical Hyperparameters
- **Expansion Factor**: 16x to 32x of model hidden dimension (e.g. \(d_{\text{hidden}} = 65,536\) for \(d_{\text{in}} = 4,096\)).
- **L1 Coefficient**: Tune to achieve target \(L_0\) sparsity between 20 and 100 active features per token.
- **Decoder Weight Normalization**: Normalize decoder column vectors to unit norm after every optimizer step.
