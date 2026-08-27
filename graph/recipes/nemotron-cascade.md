---
id: recipe:nemotron-cascade
type: recipe
title: "Nemotron-Cascade Alignment Recipe"
method: method:nemotron-cascade
task: task:instruct-sft-alignment
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / NeMo-Aligner"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - alignment
---

# Nemotron-Cascade Alignment Recipe

```python
import torch

print("Nemotron-Cascade recipe loaded")
```
