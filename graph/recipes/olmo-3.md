---
id: recipe:olmo-3
type: recipe
title: "OLMo-3 Pretraining & Dolci Alignment Recipe"
method: method:olmo-3
task: task:open-data-recipe
target_hardware: "64x NVIDIA H100 SXM5 80GB (Distributed Cluster)"
framework: "PyTorch 2.5+ / OLMo-core"
repo_url: "https://github.com/allenai/OLMo-core"
pip_dependencies:
  - "torch>=2.5.0"
  - "olmo-core"
  - "dolma"
tags:
  - recipe
  - pretraining
  - open-data
  - olmo3
---

# OLMo-3 Pretraining & Dolci Alignment Recipe

## Quickstart Implementation

```python
import torch

# OLMo-3 Dolma-3 data streaming and Dolci instruction training pipeline
print("OLMo-3 training recipe loaded")
```
