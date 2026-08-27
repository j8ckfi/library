---
id: paper:a2sg
type: paper
title: "A2SG: Adaptive Surrogate Gradient Backpropagation for Deep Spiking Networks"
authors:
  - "KIST NCL Authors"
year: 2026
month: 6
arxiv_id: "2606.11236"
url: "https://arxiv.org/abs/2606.11236"
methods:
  - method:a2sg
cites:
  - paper:spikingjelly-paper
tags:
  - snn
  - surrogate-gradients
  - neuromorphic
  - a2sg
---

# A2SG: Adaptive Surrogate Gradient Backpropagation for Deep Spiking Networks

## Abstract Summary
A2SG develops an adaptive surrogate gradient formulation that dynamically adjusts smoothing width and slope across training epochs, eliminating dead-neuron regimes during direct SNN backpropagation.

## Key Contributions
1. **Adaptive Surrogate Gradient**: Dynamically modulated surrogate gradient functions preventing gradient stagnation.
2. **Deep SNN Training**: Enables stable end-to-end backpropagation through time in deep spiking networks.

## Open Source Repository
- Implementation: `https://github.com/KIST-NCL/A2SG.git`
