---
id: method:silif
type: method
title: "SiLIF / C-SiLIF (SSM-Inspired Leaky Integrate-and-Fire)"
category: "spiking"
status: sota
sota_for:
  - task:spiking-neural-networks-training
supersedes:
  - method:surrogate-gradient-snn
papers:
  - paper:silif
recipes:
  - recipe:spikingjelly-snn
claims:
  - benchmark: "Neuromorphic Audio & Event Vision Benchmarks"
    metric: "temporal task accuracy & spike sparsity"
    value: "SOTA for Spiking Neural Networks"
    baseline: "Adaptive LIF (AdLIF)"
    date: "2025-06"
    verified: true
    notes: "SSM-inspired Leaky Integrate-and-Fire dynamics with surrogate gradient BPTT."
tags:
  - snn
  - neuromorphic
  - silif
  - audio-event
---

# SiLIF / C-SiLIF (SSM-Inspired Leaky Integrate-and-Fire)

## Method Overview
SiLIF (State-Space Model-inspired Leaky Integrate-and-Fire) integrates continuous-time linear state-space formulations with spiking thresholds, yielding highly expressive multi-scale temporal dynamics while maintaining discrete spike communication.

## When to Use
- Spiking neural networks for audio processing, event cameras, and temporal neuromorphic streams.

## Supersession
- Supersedes classical Adaptive LIF (AdLIF) and standard LIF models.
