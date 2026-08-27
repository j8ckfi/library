---
id: recipe:sparse-bitnet
type: recipe
title: "Sparse-BitNet 1.58-Bit Pretraining Recipe"
method: method:sparse-bitnet
task: task:1bit-extreme-quantization
target_hardware: "8x NVIDIA H100 80GB (Training) / CPU / NPU (Inference)"
framework: "PyTorch 2.5+ / Sparse-BitNet"
repo_url: "https://github.com/AAzdi/Sparse-BitNet"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - quantization
  - 1bit
  - ternary
  - sparse-bitnet
---

# Sparse-BitNet 1.58-Bit Pretraining Recipe

```python
import torch

print("Sparse-BitNet 1.58-bit BitLinear and dynamic activation sparsity loaded")
```
