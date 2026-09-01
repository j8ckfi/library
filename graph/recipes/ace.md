---
id: recipe:ace
type: recipe
title: "ACE playbook loop"
method: method:ace
task: task:agent-memory
target_hardware: "API models (paper: DeepSeek-V3.1 generator/reflector/curator)"
framework: "Python / uv / github.com/ace-agent/ace"
repo_url: "https://github.com/ace-agent/ace"
pip_dependencies:
  - "uv"
tags:
  - recipe
  - agents
  - ace
---

# ACE playbook loop

Incremental bullets, not rewrite. Needs execution feedback.

## Hardware & Environment Setup

```bash
git clone https://github.com/ace-agent/ace.git
cd ace
uv sync
```

## Quickstart Implementation

```python
from ace import ACE

ace_system = ACE(
    api_provider="openai",
    generator_model="DeepSeek-V3.1",
    reflector_model="DeepSeek-V3.1",
    curator_model="DeepSeek-V3.1",
    max_tokens=4096,
)
config = {
    "num_epochs": 1,
    "max_num_rounds": 3,
    "curator_frequency": 1,
    "playbook_token_budget": 80000,
    "task_name": "appworld",
    "no_ground_truth": False,
    "save_dir": "./results",
}
# ace_system.run(mode="offline", train_samples=..., val_samples=..., data_processor=..., config=config)
```

## Critical Hyperparameters & Tuning Advice
- **Updates**: incremental bullets. Do not rewrite the whole playbook (Dynamic Cheatsheet collapse).
- **Feedback**: without it, ACE/DC can degrade.
- **Not RLM**: recursive summary is not this recipe.
