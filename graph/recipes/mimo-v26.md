---
id: recipe:mimo-v26
type: recipe
title: "MiMo-V2.6 Scaled RL Playbook"
method: method:mimo-v26
task: task:frontier-rl-posttrain-stack
target_hardware: "Frontier MoE RL; paper: up to 1M context, 1568-sample async steps"
framework: "Paper-announced MiMo RL framework"
repo_url: none found
code_status: announced
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - mimo-v26
---

# MiMo-V2.6 Scaled RL Playbook

## Hardware & Environment Setup
- Paper announces open-sourced training dynamics, RL environments, and RL framework.
- No dedicated GitHub URL confirmed as of 2026-10-09. `code_status: announced`.

## Quickstart Implementation

```python
from __future__ import annotations

def freeze_router(named_params, train_router: bool = False):
    frozen = []
    for name, p in named_params:
        if (not train_router) and ("router" in name.lower()):
            p.requires_grad = False
            frozen.append(name)
    return frozen
```

Freeze the MoE router during RL. Miles remains the engine.
