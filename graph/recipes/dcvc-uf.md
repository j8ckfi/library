---
id: recipe:dcvc-uf
type: recipe
title: "DCVC-UF GPU Neural Video Codec Recipe"
method: method:dcvc-uf
task: task:learned-video-compression
target_hardware: "1x NVIDIA RTX 4090 24GB (or 1x A100/H100)"
framework: "PyTorch 2.5+ / CUDA"
repo_url: "https://github.com/microsoft/DCVC"
pip_dependencies:
  - "torch>=2.5.0"
  - "compressai>=1.2.4"
tags:
  - recipe
  - video
  - compression
  - dcvc-uf
---

# DCVC-UF GPU Neural Video Codec Recipe

```python
import torch

print("DCVC-UF GPU accelerated video codec initialized")
```
