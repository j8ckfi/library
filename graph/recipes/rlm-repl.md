---
id: recipe:rlm-repl
type: recipe
title: "RLM REPL offload (depth=1)"
method: method:rlm
task: task:long-context-prompt-offload
target_hardware: "API model (GPT-5-class) or local OpenAI-compatible server; REPL on host or Docker"
framework: "Python 3.11+ / rlms"
repo_url: "https://github.com/alexzhang13/rlm"
pip_dependencies:
  - "rlms"
tags:
  - recipe
  - agents
  - rlm
  - long-context
---

# RLM REPL offload (depth=1)

Default depth is **1**. Do not set depth 2.

## Hardware & Environment Setup
- `pip install rlms` (Python 3.11+). `OPENAI_API_KEY` or another supported backend.
- Isolated REPL: `environment="docker"` when the prompt can execute untrusted code.

## Quickstart Implementation

```python
from rlm import RLM

rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-5"},
    verbose=True,
)
print(rlm.completion("Print me the first 100 powers of two, each on a newline.").response)
```

## Critical Hyperparameters & Tuning Advice
- **Depth**: 1. Depth 2 overthinks (3.6s → 344.5s).
- **Not a SWE harness**: do not use this as GitHub-issue-to-patch.
- **Not FoldGRPO**: this slices a dumped prompt, not a tool trajectory.
- **SFT sub-claim**: RLM-Qwen3-8B +28.3% median (1k traj, 48 H100-h) is optional training in `training/`, not a new method.
