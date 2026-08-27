---
id: recipe:htmuon
type: recipe
title: "HTmuon Training Recipe"
method: method:htmuon
task: task:llm-pretraining-optimization
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/TDCSZ327/HTmuon"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - optimizer
  - htmuon
---

# HTmuon Training Recipe

## Quickstart Implementation

```python
import torch

# HTmuon heavy-tailed noise filtering
print("HTmuon recipe loaded")
```
