---
id: recipe:miles
type: recipe
title: "Miles v0.1 Frontier Post-Training Stack"
method: method:miles
task: task:frontier-rl-posttrain-stack
target_hardware: "64x NVIDIA GB300 (paper GLM-5.2 case study: 32 rollout / 32 train); smaller dense/MoE recipes in-repo"
framework: "PyTorch / SGLang / Megatron-LM or FSDP"
repo_url: "https://github.com/radixark/miles"
pip_dependencies:
  - "torch>=2.5.0"
  - "sglang"
tags:
  - recipe
  - miles
  - systems
  - post-training
---

# Miles v0.1 Frontier Post-Training Stack

## Hardware & Environment Setup
- Official code: `https://github.com/radixark/miles`. Website: `https://miles.radixark.com`.
- GLM-5.2 744B-A40B case study: 64 GB300, 32/32 split, Megatron TP2/PP4/CP4/EP8, BF16 train / FP8 serve, optimizer-state streaming to node-local disk, max session 65536, batch 64 trajectories (8 tasks × 8 attempts), fully async. Launch: `examples/experimental/openenv/glm52_tbench2`.
- Host Pass@1 algorithm stays CISPO. Distill default stays OPD. Factory process stays Poolside. Async-straggler algorithm stays SAO.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class MilesAsyncLimits:
    in_flight_trajectories: int = 128
    train_batch_trajectories: int = 64
    group_size: int = 8
    stale_weight_versions: int = 4


def should_drop_group(
    timed_out: bool,
    reward_unique: bool,
    oldest_weight_lag: int,
    limits: MilesAsyncLimits,
) -> str | None:
    """Buffer drop reasons from Miles Table 1. Filter-rejected groups are never retried."""
    if timed_out:
        return "generation_timeout"
    if not reward_unique:
        return "zero_advantage"
    if oldest_weight_lag > limits.stale_weight_versions:
        return "stale"
    return None


def refill_slots(finished_in_group: int, group_size: int, sample_granularity: bool) -> int:
    """Sample granularity frees a slot per finished trajectory; group granularity waits for the whole group."""
    if sample_granularity:
        return int(finished_in_group)
    return group_size if finished_in_group >= group_size else 0
```

## Critical Hyperparameters & Tuning Advice
- Prefer sample-granularity async when trajectory lengths vary by an order of magnitude.
- Enable `--use-rollout-routing-replay` (R3) on shipped MoE recipes that need exact expert replay; leave it off if the GLM-5.2 reference is the template.
- Stream optimizer state to disk when the per-rank Adam state will not fit (GLM-5.2: ~279GB unsharded share even at DP=4).
- Do not treat Miles as a CISPO/SAO/OPD replacement. It runs those objectives; it is not the kernel default.
