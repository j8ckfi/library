---
id: recipe:neohorse-1
type: recipe
title: "NeoHorse-1 Routing-Harness Post-Training"
method: method:neohorse-1
task: task:agentic-rsi-routing-posttrain
target_hardware: "multi-GPU post-train box for 4B/9B (paper eval uses SGLang v0.5.17)"
framework: "PyTorch / SGLang"
repo_url: "https://github.com/TokenRhythm/NeoHorse"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
  - "sglang"
tags:
  - recipe
  - neohorse
  - agentic
  - routing
---

# NeoHorse-1 Routing-Harness Post-Training

## Hardware & Environment Setup
- Code: `https://github.com/TokenRhythm/NeoHorse`. Weights: `https://hf.co/collections/TokenRhythm/neohorse-1`.
- Serve with SGLang v0.5.17 thinking mode: `enable_thinking=true`, `force_nonempty_content=true`. Max output 51200 on IF/code benches, 32768 on harness benches.
- Host distill algorithm stays OPD. Pass@1 stays CISPO. SWE harness stays mini-SWE-agent.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class RoutingRecord:
    demand: float
    tier: str
    valid_structure: bool
    semantic_score: float
    subscene: str


def admit(record: RoutingRecord, semantic_floor: float = 0.5) -> bool:
    """Keep traces that pass structural validation and a six-dimensional semantic floor."""
    return bool(record.valid_structure) and record.semantic_score >= semantic_floor


def curriculum_stage(demand: float) -> int:
    """Three-stage routing curriculum: low / mid / high predicted capability demand."""
    if demand < 1.0 / 3.0:
        return 1
    if demand < 2.0 / 3.0:
        return 2
    return 3
```

## Critical Hyperparameters & Tuning Advice
- Organize SFT by routing demand before routing-guided OPD. Do not skip admission.
- Capability-guided allocation updates the mix from eval, not from raw router confidence alone.
- Do not replace OPD, CISPO, SAO, CANOPY, Iris, or mini-SWE-agent with this recipe.
