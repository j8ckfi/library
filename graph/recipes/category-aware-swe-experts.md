---
id: recipe:category-aware-swe-experts
type: recipe
title: "Category-Aware SWE Expert RL"
method: method:category-aware-swe-experts
task: task:swe-agent-category-expert-rl
target_hardware: "long-horizon SWE sandbox fleet for Agentic-miniRL plus a distillation pass"
framework: "PyTorch / Agentic-miniRL host"
repo_url: "https://github.com/alibaba/AgenticBigBang"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - swe
  - experts
  - mopd
  - agentic
---

# Category-Aware SWE Expert RL

## Hardware & Environment Setup
- Official: `https://github.com/alibaba/AgenticBigBang`.
- Env construction from source stays CodeMidas. Async stays SAO. Issue-to-patch loop stays mini-SWE-agent. Engine stays Miles.

```bash
git clone https://github.com/alibaba/AgenticBigBang.git && cd AgenticBigBang
```

## Quickstart Implementation

```python
from __future__ import annotations


def relu_gate(teacher_return: float, reference_return: float) -> float:
    """Keep only the teacher's improving direction over the reference."""
    return max(0.0, teacher_return - reference_return)


def rre_step(mastery: dict[str, float], verified: list[str], pool: list[str]) -> list[str]:
    """Refresh mastery, Repair SFT on verified successes, Expand the frontier."""
    stale = [i for i, p in mastery.items() if p < 0.5]
    repair = list(verified)
    expand = [i for i in pool if i not in mastery or mastery[i] < 0.8]
    return stale + repair + expand
```

Train one same-origin expert per category with Agentic-miniRL. After each RL phase, refresh instance mastery, Repair-SFT on that expert's verified successes, then reselect tasks. Distill with label-routed MOPD; mask tokens whose ReLU-gated extrapolated advantage is zero.

## Critical Hyperparameters & Tuning Advice
- Track per-category \(\Delta_c\) and \(G_{\mathrm{sim}}\). Do not stop on aggregate resolution alone.
- Do not import external teacher trajectories. Repair uses the expert's own verified rollouts.
- Pro-618 is an audit-filtered Pro subset. Do not mix with locked-mini ranking boards.
