---
id: recipe:nemotron-3-ultra
type: recipe
title: "Nemotron-3-Ultra MoE Recipe"
method: method:nemotron-3-ultra
task: task:pretrain-moe-frontier
target_hardware: "64x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / Megatron-LM"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - moe
---

# Nemotron-3-Ultra MoE Recipe

```python
import torch

print("Nemotron-3-Ultra MoE recipe loaded")
```
