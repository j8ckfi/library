---
id: paper:spikingjelly-paper
type: paper
title: "SpikingJelly: An Open-Source Machine Learning Platform for Spiking Neural Networks"
authors:
  - "Wei Fang"
  - "Yanqi Chen"
  - "Jianhao Ding"
  - "Zhaofei Yu"
  - "Timothee Masquelier"
  - "Ding Chen"
  - "Liwei Huang"
  - "Huiwei Zhou"
  - "Guoqi Li"
  - "Yonghong Tian"
year: 2023
month: 12
arxiv_id: "2311.14749"
url: "https://arxiv.org/abs/2311.14749"
methods:
  - method:surrogate-gradient-snn
cites: []
tags:
  - snn
  - neuromorphic
  - framework
---

# SpikingJelly: An Open-Source Machine Learning Platform for Spiking Neural Networks

## Abstract Summary
This comprehensive paper (published in IEEE TPAMI) presents SpikingJelly, the foundational PyTorch framework for deep Spiking Neural Networks. It provides optimized CUDA and C++ backends for Leaky Integrate-and-Fire neurons, multi-step direct surrogate gradient backpropagation, neuromorphic event processing, and hardware export to neuromorphic chips.

## Key Contributions
1. **Surrogate Gradient Engine**: High-performance differentiable surrogate gradient primitives for PyTorch.
2. **Deep SNN Architectures**: Validated direct training of deep Spiking ResNets and Spiking Vision Transformers.
3. **Neuromorphic Dataset Pipelines**: End-to-end event data processing for DVS cameras.
