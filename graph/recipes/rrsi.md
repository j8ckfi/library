---
id: recipe:rrsi
type: recipe
title: "RRSI Regularized Harness RSI"
method: method:rrsi
task: task:agent-harness-runtime
target_hardware: "CPU host plus Vertex AI (Claude Opus 4.8 / Gemini 3.5 Flash); Harbor for coding"
framework: "Python 3.10+ / harbor for Terminal-Bench"
repo_url: "https://github.com/google-research/rrsi"
code_status: released
pip_dependencies:
  - "anthropic[vertex]>=0.40"
tags:
  - recipe
  - rrsi
  - agent-harness
  - rsi
---

# RRSI Regularized Harness RSI

## Hardware & Environment Setup
- Official: `https://github.com/google-research/rrsi`. Project: `https://regularized-rsi.com/`.
- Search core: `pip install -e ".[dev]"`. Coding instance uses harbor (`domains/coding/.venv`). Workspace / engineering: `pip install -e ".[agentic]"` and `RRSI_AGENT_PYTHON`.
- Production kernel stays omp². Routing-harness post-train stays NeoHorse-1. SWE loop stays mini-SWE-agent.

```bash
git clone https://github.com/google-research/rrsi.git && cd rrsi
pip install -e ".[dev]"
python3 -m pytest tests
```

Set `VERTEX_PROJECT`, `VERTEX_LOCATION=global`, and `RRSI_VERTEX_PROJECTS`. `policy_model` / `ORCHESTRATOR_MODEL` in each domain's `rrsi.json`.

## Quickstart Implementation

```python
from __future__ import annotations


def annealed_edit_budget(round_idx: int, b0: int, b_min: int, decay: float) -> int:
    raw = b0 * (decay ** round_idx)
    return max(b_min, int(round(raw)))


def accept_after_floor(score: float, incumbent: float, delta: float, token_cost: float, token_gain: float) -> bool:
    if score < incumbent + delta:
        return False
    if token_cost > 0 and token_gain <= 0:
        return False
    return True
```

Noise band \(\delta\) is 0.017 / 0.004 / 0.020 per instance, or `null` to recalibrate (`rrsi/calibrate.py`).

## Critical Hyperparameters & Tuning Advice
- Critic runs before evaluation. A leaking candidate must never receive an inflate evolve-set score.
- Stall flag plus reserved slots force untried components (`client_tool`, `skill`, `memory`, `subagent`).
- Do not treat Terminal-Bench lifts as a mini-SWE-agent ranking change.
