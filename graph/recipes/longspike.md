---
id: recipe:longspike
type: recipe
title: "LongSpike SSM-SNN Training Recipe"
method: method:longspike
task: task:spiking-neural-networks-training
target_hardware: "8x NVIDIA H100 80GB"
framework: "PyTorch 2.5+ / LongSpike"
repo_url: "https://github.com/xinruihe389-commits/LongSpike"
pip_dependencies:
  - "torch>=2.5.0"
  - "spikingjelly>=0.0.0.0.14"
tags:
  - recipe
  - snn
  - longspike
---

# LongSpike SSM-SNN Training Recipe

```python
import torch

print("LongSpike SSM-SNN sequence model initialized")
```
