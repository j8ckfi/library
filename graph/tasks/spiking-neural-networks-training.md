---
id: task:spiking-neural-networks-training
type: task
title: "Direct Training of Deep Spiking Neural Networks"
domain: "snn"
summary: "Gradient-based end-to-end direct training of deep leaky integrate-and-fire (LIF) neuromorphic networks via surrogate gradient backpropagation."
current_sota:
  - method: method:silif
    as_of: "2026-08-26"
    benchmark: "Neuromorphic Audio & Event Benchmarks"
    metric: "top-1 accuracy & temporal modeling"
    value: "SOTA for Spiking Neural Networks"
    notes: "SSM-inspired Leaky Integrate-and-Fire (SiLIF / C-SiLIF) trained with surrogate-gradient BPTT."
methods:
  - method:silif
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
