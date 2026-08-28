---
id: recipe:verigate
type: recipe
title: "VeriGate Step-Level Supervision Recipe"
method: method:verigate
task: task:all-zero-verifier-groups
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/umd-huang-lab/VeriGate"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - reasoning
  - verigate
---

# VeriGate Step-Level Supervision Recipe

```python
import torch

def gated_process_reward(prm_scores: torch.Tensor, outcome_verifier: torch.Tensor) -> torch.Tensor:
    """Gates PRM scores strictly behind trusted outcome verification."""
    return torch.where(outcome_verifier > 0.5, prm_scores, torch.zeros_like(prm_scores))
```
