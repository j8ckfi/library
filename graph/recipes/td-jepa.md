---
id: recipe:td-jepa
type: recipe
title: "TD-JEPA World Model Recipe"
method: method:td-jepa
task: task:continuous-control-world-model
target_hardware: "4x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / TD-JEPA"
repo_url: "https://github.com/HKBU-KnowComp/Temporal-Distance-JEPA"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - control
  - jepa
---

# TD-JEPA World Model Recipe

```python
import torch

print("TD-JEPA temporal distance metric world model initialized")
```
