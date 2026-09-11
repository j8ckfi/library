---
id: recipe:t1-terminal-rl
type: recipe
title: "T1 Terminal Agent RL on slime"
method: method:t1-terminal-rl
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "122B-total MoE; paper uses slime rollout/train split with SGLang 0.5.12.post1 + Megatron-Core"
framework: "slime v0.3.0 / Megatron-Core / SGLang"
repo_url: "https://github.com/THUDM/slime"
pip_dependencies:
  - "sglang==0.5.12.post1"
tags:
  - recipe
  - t1
  - terminal
  - slime
  - moe
---

# T1 Terminal Agent RL on slime

## Hardware & Environment Setup
- Project: `https://jyyang26.github.io/t1`. Weights: `https://huggingface.co/collections/TberiusJunyao/t1`.
- Train host: slime v0.3.0 (`https://github.com/THUDM/slime`, paper commit bf14dc21). No dedicated T1 trainer repo as of 2026-09-11.
- Production stack first hop stays Miles. Async algorithm stays SAO. AppWorld coverage stays CANOPY.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class TitoR3:
    replay_expert_ids: bool = True
    repair_turn_boundary_drift: bool = True
    process_reward: str = "n_passing_verifiers"


def r3_train_forward(rollout_expert_ids, router_logits, replay: bool) -> None:
    """Replay sampler expert choices so train MoE routing matches rollout."""
    if replay and rollout_expert_ids is None:
        raise ValueError("R3 requires recorded expert ids from the sampler")
    _ = router_logits
```

## Critical Hyperparameters & Tuning Advice
- TITO: token-in keeps prefixes; token-out stitches under loss masks; repair drift at turn boundaries.
- R3 is load-bearing on MoE; dropping expert replay reopens the 0.021 logp gap.
- Train data must stay disjoint from Terminal-Bench 2.1 if you want the paper's transfer claim.
