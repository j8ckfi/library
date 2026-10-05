---
id: recipe:opsft
type: recipe
title: "OPSFT On-Policy Update Direction"
method: method:opsft
task: task:instruct-sft-alignment
target_hardware: "SFT box that can compute an on-policy gradient; paper: Qwen3-4B/8B DeepMath"
framework: "PyTorch"
repo_url: "https://github.com/ssfgunner/OPSFT"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - opsft
  - sft
---

# OPSFT On-Policy Update Direction

## Hardware & Environment Setup
- Official: `https://github.com/ssfgunner/OPSFT`. `code_status: released`.
- Instruct default stays OLMo-3. Pass@1 stays CISPO.

```bash
git clone https://github.com/ssfgunner/OPSFT.git && cd OPSFT
```

## Quickstart Implementation

```python
from __future__ import annotations


def project_on_policy(sft_grad: list[float], onpol_grad: list[float]) -> list[float]:
    if len(sft_grad) != len(onpol_grad):
        raise ValueError("gradient shapes must match")
    if not sft_grad:
        raise ValueError("gradients are empty")
    denom = sum(g * g for g in onpol_grad)
    if denom == 0.0:
        raise ValueError("on-policy gradient is zero")
    scale = sum(a * b for a, b in zip(sft_grad, onpol_grad)) / denom
    if scale < 0.0:
        scale = 0.0
    return [scale * g for g in onpol_grad]
```

Compute the usual SFT gradient and an on-policy gradient (current-model NLL on its own samples). Keep the SFT step's projection onto the on-policy direction; drop the opposing component.

## Critical Hyperparameters & Tuning Advice
- Qwen3-4B DeepMath 40.11 vs GRPO 38.96 in 6.4 h vs 16.5 h. Post-GRPO continue, do not vanilla-SFT over it (36.25 drop).
