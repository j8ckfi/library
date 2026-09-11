---
id: recipe:partial-reasoning-traces
type: recipe
title: "Partial / Truncated Reasoning-Trace SFT"
method: method:partial-reasoning-traces
task: task:instruct-sft-alignment
target_hardware: "same as host SFT (paper: reasoner post-train; code on naver-ai/revisiting-trace)"
framework: "PyTorch / HuggingFace Trainer or host SFT"
repo_url: "https://github.com/naver-ai/revisiting-trace"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - sft
  - reasoning
  - traces
---

# Partial / Truncated Reasoning-Trace SFT

## Hardware & Environment Setup
- Official code: `https://github.com/naver-ai/revisiting-trace` (EMNLP 2026 Findings).
- Instruct defaults stay OLMo-3 Dolci / Nemotron-Cascade 2. Pass@1 stays CISPO.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class TraceKeep:
    prefix_tok: int = 128
    suffix_tok: int = 256


def partial_trace(token_ids: list[int], keep: TraceKeep) -> list[int]:
    """Keep endpoints; drop the redundant middle of a long reasoning trajectory."""
    if len(token_ids) <= keep.prefix_tok + keep.suffix_tok:
        return token_ids
    return token_ids[: keep.prefix_tok] + token_ids[-keep.suffix_tok :]
```

## Critical Hyperparameters & Tuning Advice
- Sweep prefix/suffix; the paper finds heavy truncation still works.
- Do not drop the answer-side endpoint. Intermediate-token removal is the point.
- Apply the same shaping if the host is RL or on-policy distillation, not only SFT.
