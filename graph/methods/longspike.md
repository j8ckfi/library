---
id: method:longspike
type: method
title: "LongSpike (SSM-SNN Sequence Modeling)"
category: "snn"
status: sota
sota_for:
  - task:spiking-neural-networks-training
  - task:snn-sequence-modeling
supersedes:
  - method:silif
papers:
  - paper:longspike
recipes:
  - recipe:longspike
claims:
  - benchmark: "Neuromorphic Long Sequence Benchmarks"
    metric: "temporal task accuracy & context length"
    value: "Default SOTA for SSM-SNN sequence modeling"
    baseline: "SiLIF / AdLIF"
    date: "2026-08-26"
    verified: true
    notes: "Continuous-state state-space transitions integrated with discrete spiking thresholds."
tags:
  - snn
  - neuromorphic
  - ssm
  - longspike
  - sota
---

# LongSpike (SSM-SNN Sequence Modeling)

## Method Overview
LongSpike bridges State Space Model (SSM) recurrence with discrete spiking neural dynamics:
1. **SSM State Transitions**: Continuous linear state recurrence prevents membrane potential saturation across extended temporal sequences.
2. **Spiking Threshold Dynamics**: Discrete all-or-none spike activations enabling neuromorphic hardware execution.

## When to Use
- Default SOTA architecture for spiking neural network sequence modeling and neuromorphic temporal streams (SiLIF remains as a speech-neuron reference).

## Supersession
- Supersedes `method:silif` as the primary SSM-SNN default.
