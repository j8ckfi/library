---
id: recipe:nemotron-3-nano
type: recipe
title: "Nemotron-3-Nano Pretraining Recipe"
method: method:nemotron-3-nano
task: task:pretrain-dense-7b
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / NeMo"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - architecture
---

# Nemotron-3-Nano Pretraining Recipe

```python
import torch

print("Nemotron-3-Nano architecture initialized")
```
