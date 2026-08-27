---
id: recipe:efficienttdmpc
type: recipe
title: "EfficientTDMPC Continuous Control Recipe"
method: method:efficienttdmpc
task: task:continuous-control-world-model
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100 40GB)"
framework: "PyTorch 2.5+ / BMPC"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "gymnasium>=1.0.0"
tags:
  - recipe
  - control
  - robotics
  - efficienttdmpc
---

# EfficientTDMPC Continuous Control Recipe

```python
import torch

print("EfficientTDMPC block planning world model loaded")
```
