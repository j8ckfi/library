---
id: recipe:w2s-opd
type: recipe
title: "W2S-OPD Distillation Recipe"
method: method:w2s-opd
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/Yu-Fangxu/W2S-OPD"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - distillation
  - weak-to-strong
---

# W2S-OPD Distillation Recipe

```python
import torch

print("W2S-OPD weak-to-strong recipe loaded")
```
