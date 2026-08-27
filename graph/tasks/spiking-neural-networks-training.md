---
id: task:spiking-neural-networks-training
type: task
title: "Direct Training of Deep Spiking Neural Networks"
domain: "snn"
summary: "Gradient-based end-to-end direct training of deep leaky integrate-and-fire (LIF) neuromorphic networks via surrogate gradient backpropagation."
current_sota:
  - method: method:longspike
    as_of: "2026-08-26"
    benchmark: "Neuromorphic Long Sequence & Audio Benchmarks"
    metric: "top-1 accuracy & temporal modeling"
    value: "Default SOTA for SNN sequence / SSM"
    notes: "LongSpike (2606.12895); train with A2SG (2606.11236); SiLIF stays as speech-neuron cite."
  - method: method:a2sg
    as_of: "2026-08-26"
    benchmark: "Deep SNN Backpropagation Suite"
    metric: "training stability"
    value: "Recommended SNN training surrogate gradient method"
    notes: "A2SG (2606.11236) for surrogate gradient backprop."
methods:
  - method:longspike
  - method:a2sg
  - method:silif
  - method:ngn
  - method:neuronspark
  - method:bispikclm
  - method:sdllm
  - method:surrogate-gradient-snn
tags:
  - snn
  - neuromorphic
  - longspike
  - a2sg
---

# Direct Training of Deep Spiking Neural Networks

## Problem Definition
Spiking Neural Networks (SNNs) process temporal event streams via discrete all-or-none spike activations.

## SOTA Recommendation (as of 2026-08-26)
- **SNN Sequence / SSM**: **LongSpike** (`method:longspike`, 2606.12895).
- **Training Method**: Train with **A2SG** (`method:a2sg`, 2606.11236) adaptive surrogate gradients.
- **Speech-Neuron Reference**: **SiLIF** (`method:silif`) stays as speech-neuron citation.
