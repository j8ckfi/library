---
id: recipe:muon-pretraining
type: recipe
title: "Muon Pretraining Recipe"
method: method:muon-scalable
task: task:pretrain-dense-7b
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/MoonshotAI/Moonlight"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - pretraining
  - muon
---

# Muon Pretraining Recipe

```python
import torch

print("Scalable Muon recipe loaded")
```
