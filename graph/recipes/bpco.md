---
id: recipe:bpco
type: recipe
title: "BPCO Critic Optimization Recipe"
method: method:bpco
task: task:token-level-critic-rl
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/QPHutu/golden_critic"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - rl-alignment
  - bpco
---

# BPCO Critic Optimization Recipe

## Hardware & Environment Setup
- Recommended Hardware: 8x NVIDIA H100 80GB GPUs.
- Framework: PyTorch 2.5+ with standard actor-critic pipeline.

## Quickstart Code

```python
import torch
import torch.nn as nn

class BoundedValueHead(nn.Module):
    """Value head bounded to [min_val, max_val] interval."""
    def __init__(self, hidden_dim: int, min_val: float = 0.0, max_val: float = 1.0):
        super().__init__()
        self.linear = nn.Linear(hidden_dim, 1)
        self.min_val = min_val
        self.max_val = max_val

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        raw_val = self.linear(hidden_states).squeeze(-1)
        return self.min_val + (self.max_val - self.min_val) * torch.sigmoid(raw_val)

def compute_dppo_surrogate(
    pi_log_probs: torch.Tensor,
    mu_log_probs: torch.Tensor,
    advantages: torch.Tensor,
    epsilon: float = 0.2,
) -> torch.Tensor:
    """Computes DPPO surrogate objective with probability-bounded clipping."""
    mu_probs = torch.exp(mu_log_probs)
    ratio = torch.exp(pi_log_probs - mu_log_probs)
    
    eps_scaled = epsilon / (mu_probs + 1e-8)
    clipped_ratio = torch.clamp(ratio, 1.0 - eps_scaled, 1.0 + eps_scaled)
    
    surr1 = ratio * advantages
    surr2 = clipped_ratio * advantages
    return torch.min(surr1, surr2).mean()
```

## Critical Hyperparameters
- `epsilon`: 0.2 (DPPO probability threshold scaling).
- `value_bound`: Match minimum and maximum bounds of task reward.
- `normalize_advantages`: `False` (preserve unnormalized advantage scales).
