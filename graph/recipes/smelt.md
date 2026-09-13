---
id: recipe:smelt
type: recipe
title: "SMELT Compute-Matched Looped MoE Recipe"
method: method:smelt
task: task:compute-matched-moe-looped-pretrain
target_hardware: "paper ladder 100M–1.6B active / up to 54B non-embedding (internal cluster)"
framework: "decoder-only MoE Transformer (paper; AdamW WSD)"
repo_url: none found
code_status: partial
pip_dependencies: []
tags:
  - recipe
  - smelt
  - moe
  - looped-transformer
---

# SMELT Compute-Matched Looped MoE Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-12 (`arXiv:2609.01343`). `repo_url: none found`.
- Paper optimizer: AdamW, WSD, global batch 256 sequences (~1M tokens/step), packed 4096-token contexts.
- Architecture default for frontier MoE stays DeepSeek-V4 / Kimi-K3. This recipe is the looping match, not that template.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class SmeltLayout:
    num_layers: int
    loop_span_frac: float = 0.5
    loop_count: int = 2
    residual_scale: float = 0.5


def looped_layer_ids(layout: SmeltLayout) -> range:
    span = int(round(layout.num_layers * layout.loop_span_frac))
    start = (layout.num_layers - span) // 2
    return range(start, start + span)


def execution_depth(layout: SmeltLayout) -> int:
    span = len(looped_layer_ids(layout))
    return layout.num_layers + (layout.loop_count - 1) * span
```

## Critical Hyperparameters & Tuning Advice
- Loop the middle 50% twice. Scale those residual updates by \(1/2\). Keep physical depth at the unlooped Baseline optimum.
- Pay for extra visits by narrowing \(H\); recover non-embedding params by raising expert count uniformly; restore KV with head size / GQA. Target mismatch: FLOPs <4%, params <1%, KV <4%.
- Two visits beat three or four under the FLOPs cap (thinner model).
- Do not clone unrelated repositories named SMELT.
