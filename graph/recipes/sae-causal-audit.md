---
id: recipe:sae-causal-audit
type: recipe
title: "SAE Causal Audit Suite Recipe"
method: method:sae-causal-audit
task: task:mechanistic-interpretability-dictionaries
target_hardware: "1x NVIDIA RTX 4090 24GB"
framework: "PyTorch 2.5+ / SAE-Audit"
repo_url: "https://github.com/mohamed-bal/sae-causal-audit"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - interpretability
  - sae
  - audit
---

# SAE Causal Audit Suite Recipe

```python
import torch

print("SAE causal auditing benchmark suite loaded")
```
