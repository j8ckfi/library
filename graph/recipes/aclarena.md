---
id: recipe:aclarena
type: recipe
title: "ACLArena Mixture of Low-Rank Experts"
method: method:aclarena
task: task:agent-continual-learning
target_hardware: "slime post-train box able to run sequential stage RL then LoRA-expert RL"
framework: "PyTorch / slime"
repo_url: "https://github.com/WillDreamer/ACLArena"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - aclarena
  - continual-learning
  - lora
  - agentic
---

# ACLArena Mixture of Low-Rank Experts

## Hardware & Environment Setup
- Official: `https://github.com/WillDreamer/ACLArena`. Hugging Face collection `willhx/aclarena`.
- Built on slime. Pass@1 stays CISPO. Async stays SAO. AppWorld stays CANOPY. Engine stays Miles.

```bash
git clone https://github.com/WillDreamer/ACLArena.git && cd ACLArena
```

## Quickstart Implementation

```python
from __future__ import annotations


def route_expert(domain: str, experts: dict[str, object]) -> object:
    if domain not in experts:
        raise KeyError(f"no LoRA expert for domain {domain!r}")
    return experts[domain]


def sdft_then_rl(stage_ids: list[str]) -> list[str]:
    """Offline replay of filtered specialist trajectories, then per-stage LoRA RL."""
    replay = [f"sdft:{k}" for k in stage_ids]
    experts = [f"lora-rl:{k}" for k in stage_ids]
    return replay + experts
```

Filter oracle trajectories on reward, tool format, and protocol, then mix. Attach one LoRA expert per stage and RL each expert; route at serve time by domain tag. Do not average teacher logits across protocols.

## Critical Hyperparameters & Tuning Advice
- Sequential Math → Search → E-commerce → IF is the diagnostic curriculum, not the deployed recipe.
- Balance the SDFT mix. Volume-dominant domains overwrite IF / e-commerce.
- MMOPD / merge are paper baselines. MLE is the proposed consolidator.
