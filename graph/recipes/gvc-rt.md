---
id: recipe:gvc-rt
type: recipe
title: "GVC-RT Generative Video Codec Recipe"
method: method:gvc-rt
task: task:learned-video-compression
target_hardware: "1x NVIDIA RTX 4090 24GB"
framework: "PyTorch 2.5+ / GVC-RT"
repo_url: "https://github.com/semcomm/GVC-RT"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - video
  - compression
  - generative
---

# GVC-RT Generative Video Codec Recipe

```python
import torch

print("GVC-RT real-time generative video compression loaded")
```
