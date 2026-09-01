---
id: recipe:mini-swe-agent
type: recipe
title: "mini-SWE-agent bash ReAct loop"
method: method:mini-swe-agent
task: task:software-engineering-agent-harness
target_hardware: "CPU + API model (or local LLM); Docker optional for SWE-bench"
framework: "Python 3.11+ / mini-swe-agent / LiteLLM"
repo_url: "https://github.com/SWE-agent/mini-swe-agent"
pip_dependencies:
  - "mini-swe-agent"
  - "uv"
tags:
  - recipe
  - agents
  - mini-swe-agent
  - swe-bench
---

# mini-SWE-agent bash ReAct loop

Eval SWE-bench Verified with the **locked mini harness**. Do not invent tools.

## Hardware & Environment Setup
- API key for the target model (LiteLLM). Docker for sandboxed SWE-bench.
- `pip install uv && uvx mini-swe-agent` or `pip install mini-swe-agent`.

```bash
pip install mini-swe-agent
mini
```

## Quickstart Implementation

```python
from minisweagent.agents.default import DefaultAgent
from minisweagent.environments.local import LocalEnvironment
from minisweagent.models.litellm_model import LitellmModel

agent = DefaultAgent(
    LitellmModel(model_name="openai/gpt-5"),
    LocalEnvironment(),
)
agent.run("Write a sudoku game")
```

## Critical Hyperparameters & Tuning Advice
- **Tools**: bash only. Do not add a 40-server MCP zoo.
- **History**: linear append. Do not fold or compact unless you have left this task for FoldGRPO/RLM.
- **Eval**: official SWE-bench locked mini harness on Verified. Label the board (official JSON vs vals.ai vs Scale Pro).
- **Depth**: this is not RLM. Do not recurse sub-LMs over a dumped corpus here.
