---
id: recipe:recreationworld
type: recipe
title: "RecreationWorld Hybrid CUA Environments"
method: method:recreationworld
task: task:hybrid-computer-use-agent-rl
target_hardware: "platform VM or device under test (Ubuntu / macOS / Windows / Android / Web) plus a model endpoint"
framework: "uv / RecreationWorld harness (`rb run`)"
repo_url: "https://github.com/QwenLM/RecreationWorld"
code_status: released
pip_dependencies:
  - "uv"
tags:
  - recipe
  - recreationworld
  - computer-use
  - hybrid-cua
---

# RecreationWorld Hybrid CUA Environments

## Hardware & Environment Setup
- Official: `https://github.com/QwenLM/RecreationWorld`
- Bench: `https://recreation-bench.cc/`
- Dataset: Hugging Face `Qwen/RecreationBench` (also ModelScope `Qwen/RecreationBench`)
- OSWorld 2.0 ranking stays Claude computer-use. This recipe is hybrid GUI+code recreation.

## Quickstart Implementation

```bash
uv sync
uv run python scripts/release/smoke_providers.py
uv run python scripts/release/smoke_runtime.py
uv run rb run --help
```

A scored run also needs a frozen task bundle, a prepared execution environment, and model plus judge endpoints. Pick a platform:

| Platform | Tasks | Interface |
| --- | ---: | --- |
| Ubuntu | 50 | AT-SPI |
| macOS | 50 | AXUIElement |
| Windows | 50 | UI Automation |
| Android | 50 | UiAutomator |
| Web | 50 | Browser assertions |

Canonical task index: `tasks/`.

## Critical Hyperparameters & Tuning Advice
- Reward is frozen reference-grounded assertions, not source similarity. Candidates may use another language or framework.
- Report programmatic and visual scores separately. Overall 58% can still mean 2.8% full programmatic pass.
- GUI interaction continues after implementation starts. Do not freeze the agent into a code-only second stage.
