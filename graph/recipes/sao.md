---
id: recipe:sao
type: recipe
title: "SAO Agentic Async RL Recipe"
method: method:sao
task: task:agentic-async-rl
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / Ray"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "ray>=2.40.0"
tags:
  - recipe
  - agentic
  - async-rl
  - sao
---

# SAO Agentic Async RL Recipe

```python
import torch

print("SAO async rollout buffer and actor-critic workers initialized")
```
