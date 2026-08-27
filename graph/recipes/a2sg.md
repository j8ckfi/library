---
id: recipe:a2sg
type: recipe
title: "A2SG Adaptive Surrogate Gradient Recipe"
method: method:a2sg
task: task:spiking-neural-networks-training
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / A2SG"
repo_url: "https://github.com/KIST-NCL/A2SG.git"
pip_dependencies:
  - "torch>=2.5.0"
  - "spikingjelly>=0.0.0.0.14"
tags:
  - recipe
  - snn
  - a2sg
---

# A2SG Adaptive Surrogate Gradient Recipe

```python
import torch

print("A2SG adaptive surrogate gradient loaded")
```
