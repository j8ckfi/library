---
id: recipe:onepo
type: recipe
title: "OnePO RL-Only Domain Adaptation"
method: method:onepo
task: task:instruct-sft-alignment
target_hardware: "base-model RL box; paper: medical 20K / HuatuoGPT-3 27B"
framework: "PyTorch RL host; official HuatuoGPT-3"
repo_url: "https://github.com/FreedomIntelligence/HuatuoGPT-3"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - onepo
  - rl-alignment
---

# OnePO RL-Only Domain Adaptation

## Hardware & Environment Setup
- Official: `https://github.com/FreedomIntelligence/HuatuoGPT-3`. `code_status: released` as of 2026-10-06.
- Instruct default stays OLMo-3.

## Quickstart Implementation

```python
from __future__ import annotations

def retire_teacher(student_score: float, teacher_score: float) -> bool:
    return student_score > teacher_score
```

Clone HuatuoGPT-3. Start from the base checkpoint. Treat teacher traces as transient; retire them with `retire_teacher` once the policy wins. Do not SFT first.

## Critical Hyperparameters & Tuning Advice
- HealthBench Total 67.2 / 20K; 27B 70.1 / 71.4 Professional. Do not retarget OLMo-3.
