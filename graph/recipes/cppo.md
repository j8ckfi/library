---
id: recipe:cppo
type: recipe
title: "CPPO Cumulative Prefix-Divergence Recipe"
method: method:cppo
task: task:reasoning-rl-alignment
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://hunyuan-cppo.github.io/"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - rl-alignment
  - cppo
---

# CPPO Cumulative Prefix-Divergence Recipe

```python
import torch

print("CPPO recipe loaded")
```
