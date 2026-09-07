---
id: recipe:layer-dropout
type: recipe
title: "Layer Dropout Pretrain Recipe"
method: method:layer-dropout
task: task:llm-pretraining-optimization
target_hardware: "Cerebras CS-3 (paper); GPU pretrain boxes for the drop-path kernel"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/meta-pytorch/torchtune/blob/main/torchtune/modules/layer_dropout.py"
pip_dependencies:
  - "torch>=2.5.0"
  - "torchtune>=0.5.0"
tags:
  - recipe
  - layer-dropout
  - pretraining
  - stochastic-depth
---

# Layer Dropout Pretrain Recipe

## Hardware & Environment Setup
- No paper-specific repo. Practical kernels: torchtune `layer_dropout.py` and fairseq `LayerDrop`. Override residual scale to $r_{\mathrm{train}}=1/\rho$, $r_{\mathrm{eval}}=1$ even if those files historically used 1/1.
- Optimizer stays `method:muon2` (+ KL-SOAP if memory allows) for ~7B. This recipe only wraps residual blocks.

## Quickstart Implementation

```python
import torch
import torch.nn as nn


class LayerDropResidual(nn.Module):
    """Stochastic-depth residual with r_train = 1/rho. p_drop is the skip probability."""

    def __init__(self, module: nn.Module, p_drop: float):
        super().__init__()
        self.module = module
        self.p_drop = float(p_drop)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.p_drop <= 0.0:
            return x + self.module(x)
        rho = 1.0 - self.p_drop
        if not self.training:
            return x + self.module(x)
        keep = torch.rand(x.shape[0], device=x.device, dtype=x.dtype) > self.p_drop
        residual = self.module(x) / rho
        mask = keep.view(-1, *([1] * (x.ndim - 1)))
        return x + residual * mask


def ild_drop_probs(n_layers: int, p_max: float) -> list[float]:
    """Increasing layer distribution: p^ℓ = ℓ/(L-1) * p_max."""
    if n_layers <= 1:
        return [0.0]
    return [(i / (n_layers - 1)) * p_max for i in range(n_layers)]


def dts_scale(step: int, total: int) -> float:
    """Decreasing time schedule multiplier in [0, 1]."""
    if total <= 1:
        return 0.0
    return max(0.0, 1.0 - step / (total - 1))
```

## Critical Hyperparameters & Tuning Advice
- $r_{\mathrm{train}}=1/\rho$. This is the paper's transfer-critical scale, not $r_{\mathrm{train}}=1$.
- Large runs: ILD + DTS. Table 5: 1.8B $p_{\max}=0.6$ (~15% FLOP save), 3.9B $0.8$ (~20%), 8.2B $0.99$ (~25%).
- Retune LR, batch, and weight decay at each dropout rate before declaring a loss regression.
- Do not replace Muon2. PEFT-only stacks are out of scope.
