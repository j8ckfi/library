---
id: recipe:ace-moe-peft
type: recipe
title: "ACE MoE Adapter Consolidation"
method: method:ace-moe-peft
task: task:parameter-efficient-fine-tuning
target_hardware: "MoE PEFT box (paper: four MoE backbones)"
framework: "PyTorch"
repo_url: "https://github.com/UbiquitousAILab/ACE"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
  - "peft"
tags:
  - recipe
  - peft
  - moe
  - ace-moe-peft
---

# ACE MoE Adapter Consolidation

## Hardware & Environment Setup
- Code: `https://github.com/UbiquitousAILab/ACE`. EMNLP 2026.
- Keep the global PEFT budget fixed. Raise rank inside a group as you merge experts.
- Dense 24GB quality default stays `method:lr-matters-lora`. Do not confuse with `method:ace`.

## Quickstart Implementation

```python
from collections import defaultdict


def group_shared_rank(n_experts: int, per_expert_rank: int, n_groups: int) -> int:
    """Move the same adapter budget into fewer, wider LoRAs."""
    if n_groups <= 0:
        raise ValueError("n_groups must be positive")
    return max(1, (n_experts * per_expert_rank) // n_groups)


def experts_by_group(assignments: list[int]) -> dict[int, list[int]]:
    grouped: dict[int, list[int]] = defaultdict(list)
    for expert_id, group_id in enumerate(assignments):
        grouped[int(group_id)].append(expert_id)
    return dict(grouped)
```

## Critical Hyperparameters & Tuning Advice
- Group by adapter similarity during/after a short expert-wise warmup, then consolidate.
- Measure wall-clock vs expert-wise LoRA; the paper's 1.31×–1.48× is the target band.
