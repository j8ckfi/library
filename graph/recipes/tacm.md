---
id: recipe:tacm
type: recipe
title: "TACM Self-Call and Range-Read"
method: method:tacm
task: task:long-context-prompt-offload
target_hardware: "finetune box for Qwen3.6-35B-A3B-class MoE; serve at 8K per-agent context"
framework: "PyTorch SFT over a two-tool harness"
repo_url: "https://github.com/brycesandlund/infinite-context"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - tacm
  - long-context
  - agent-recursion
---

# TACM Self-Call and Range-Read

## Hardware & Environment Setup
- Official: `https://github.com/brycesandlund/infinite-context`. `code_status: released`.
- Dumped-corpus REPL stays RLM.

```bash
git clone https://github.com/brycesandlund/infinite-context.git && cd infinite-context
```

## Quickstart Implementation

```python
from __future__ import annotations


def range_read(doc: str, start: int, end: int) -> str:
    if start < 0 or end < start:
        raise ValueError("need 0 <= start <= end")
    if end > len(doc):
        raise ValueError("end exceeds document length")
    return doc[start:end]


def self_call(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("self-call prompt is empty")
    return prompt
```

Expose `range_read` and `self_call` as the only tools. Finetune on synthetic traces that recurse under an 8K per-call cap. Serve with that cap; do not dump the full document into one window.

## Critical Hyperparameters & Tuning Advice
- OOLONG 80K 0.561 vs GPT-5.4 0.539 is the first length where the 8K harness leads. RULER 0.858 at 320K.
