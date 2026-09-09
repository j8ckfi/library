---
id: recipe:online-draft-cotrain
type: recipe
title: "Online Draft Co-Training (NeMo RL)"
method: method:online-draft-cotrain
task: task:frontier-rl-posttrain-stack
target_hardware: "multi-node CP+PP (paper up to 122B, 256K)"
framework: "PyTorch / NVIDIA NeMo RL"
repo_url: "https://github.com/NVIDIA-NeMo/RL/issues/3698"
pip_dependencies:
  - "torch>=2.5.0"
  - "nemo-rl"
tags:
  - recipe
  - systems
  - speculative-decoding
  - online-draft-cotrain
---

# Online Draft Co-Training (NeMo RL)

## Hardware & Environment Setup
- Track `https://github.com/NVIDIA-NeMo/RL/issues/3698`. Needs context-parallel zigzag ring attention plus TapChannel.
- Host RL algorithm unchanged. This is rollout acceleration.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class DraftCoTrainFlags:
    branch_attention_cp: bool = True
    tapchannel_pp: bool = True
    online_update_draft: bool = True
```

## Critical Hyperparameters & Tuning Advice
- Enable branch attention under CP before trusting long-context drafts.
- TapChannel must not enter the pipeline critical path (paper: separate transport).
