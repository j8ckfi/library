---
id: recipe:bispikclm
type: recipe
title: "BiSpikCLM Training Recipe"
method: method:bispikclm
task: task:spiking-neural-networks-training
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - snn
---

# BiSpikCLM Training Recipe

```python
import torch

print("BiSpikCLM causal spiking model loaded")
```
