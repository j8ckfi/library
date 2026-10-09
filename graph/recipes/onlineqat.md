---
id: recipe:onlineqat
type: recipe
title: "OnlineQAT Blockwise QAT then On-Policy Reverse-KL"
method: method:onlineqat
task: task:full-lowbit-finetune
target_hardware: "QAT host plus a frozen full-precision teacher; paper: Qwen3-1.7B W3/W2"
framework: "PyTorch QAT + OPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - onlineqat
---

# OnlineQAT Blockwise QAT then On-Policy Reverse-KL

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def recovery_stage(init_ready: bool) -> str:
    return "opd" if init_ready else "block_qat" 
```

Block-wise QAT first, then on-policy reverse-KL. Do not retarget GradCodeS.
