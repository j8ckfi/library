---
id: task:spiking-neural-networks-training
type: task
title: "Direct Training of Deep Spiking Neural Networks"
domain: "snn"
summary: "Gradient-based end-to-end direct training of deep leaky integrate-and-fire (LIF) neuromorphic networks via surrogate gradient backpropagation."
current_sota:
  - method: method:surrogate-gradient-snn
    as_of: "2024-06"
    benchmark: "Neuromorphic DVS-Gesture / ImageNet-1k"
    metric: "top-1 accuracy"
    value: 81.3
    notes: "Direct backpropagation through time using smooth surrogate threshold derivatives in SpikingJelly."
methods:
  - method:surrogate-gradient-snn
tags:
  - snn
  - neuromorphic
  - event-driven
---

# Direct Training of Deep Spiking Neural Networks

## Problem Definition
Spiking Neural Networks (SNNs) process temporal event streams via discrete all-or-none spike activations \(\{0, 1\}\), offering orders of magnitude lower dynamic energy consumption on event-driven neuromorphic hardware. However, the step-activation threshold function has a Dirac delta derivative (zero almost everywhere, undefined at threshold), preventing standard backpropagation.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: Neuromorphic event datasets (DVS-CIFAR10, DVS-Gesture, N-ImageNet) and static vision benchmarks (ImageNet-1k, CIFAR-100).
- **Efficiency Metrics**: Synaptic operations per sample, simulated spike count per timestep, and temporal latency.

## SOTA Landscape
Modern deep SNNs are trained end-to-end using **Surrogate Gradient Learning**, which replaces non-differentiable Heaviside step gradients during the backward pass with smooth continuous functions (e.g. Arctan, Sigmoid, or FastSigmoid), enabling direct training of deep ResNet and Transformer-like spiking architectures.
