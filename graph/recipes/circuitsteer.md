---
id: recipe:circuitsteer
type: recipe
title: "CircuitSteer SAE Steering Recipe"
method: method:circuitsteer
task: task:mechanistic-interpretability-dictionaries
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100 80GB)"
framework: "PyTorch 2.5+ / CircuitSteer"
repo_url: "https://github.com/mehrshad-sdtn/CircuitSteer"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformer-lens>=2.10.0"
tags:
  - recipe
  - interpretability
  - circuits
  - circuitsteer
---

# CircuitSteer SAE Steering Recipe

```python
import torch

print("CircuitSteer subspace projection steering initialized")
```
