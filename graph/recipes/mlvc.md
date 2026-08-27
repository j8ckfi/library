---
id: recipe:mlvc
type: recipe
title: "MLVC Deployable Video Codec Recipe"
method: method:mlvc
task: task:learned-video-compression
target_hardware: "Mobile NPU / Edge CPU / 1x RTX 4090"
framework: "PyTorch 2.5+ / ONNX Runtime"
repo_url: "https://github.com/microsoft/mlvc"
pip_dependencies:
  - "torch>=2.5.0"
  - "onnxruntime>=1.19.0"
tags:
  - recipe
  - video
  - compression
  - mlvc
---

# MLVC Deployable Video Codec Recipe

```python
import torch

print("MLVC edge deployable video codec loaded")
```
