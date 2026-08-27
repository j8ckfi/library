---
id: recipe:nemotron-cascade-2
type: recipe
title: "Nemotron-Cascade 2 Industrial SFT Recipe"
method: method:nemotron-cascade-2
task: task:instruct-sft-alignment
target_hardware: "16x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / NeMo-Aligner"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - recipe
  - alignment
  - nemotron-cascade-2
---

# Nemotron-Cascade 2 Industrial SFT Recipe

```python
import torch

print("Nemotron-Cascade 2 industrial SFT pipeline loaded")
```
