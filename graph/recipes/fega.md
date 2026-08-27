---
id: recipe:fega
type: recipe
title: "FEGA Effect Geometry Recipe"
method: method:fega
task: task:mechanistic-interpretability-dictionaries
target_hardware: "1x NVIDIA RTX 4090 24GB"
framework: "PyTorch 2.5+ / FEGA"
repo_url: "https://github.com/UKPLab/FEGA"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - interpretability
  - geometry
  - fega
---

# FEGA Effect Geometry Recipe

```python
import torch

print("FEGA feature effect geometry analyzer initialized")
```
