---
id: method:silif
type: method
title: "SiLIF / C-SiLIF (SSM-Inspired Leaky Integrate-and-Fire)"
category: "spiking"
status: active
superseded_by: method:longspike
sota_for: []
supersedes:
  - method:surrogate-gradient-snn
papers:
  - paper:silif
recipes:
  - recipe:spikingjelly-snn
claims:
  - benchmark: "Neuromorphic Audio & Event Vision Benchmarks"
    metric: "temporal task accuracy & spike sparsity"
    value: "Speech-Neuron Reference Baseline"
    baseline: "Adaptive LIF (AdLIF)"
    date: "2025-06"
    verified: true
    notes: "SSM-inspired Leaky Integrate-and-Fire dynamics. Maintained as speech-neuron citation."
tags:
  - snn
  - neuromorphic
  - silif
  - audio-event
---

# SiLIF / C-SiLIF (SSM-Inspired Leaky Integrate-and-Fire)

## Method Overview
SiLIF integrates continuous-time linear state-space formulations with spiking thresholds. Retained in the graph as a primary speech-neuron citation.

## Supersession
- Superseded by `method:longspike` (2606.12895) as the default SSM-SNN architecture.
