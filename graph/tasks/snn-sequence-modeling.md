---
id: task:snn-sequence-modeling
type: task
title: "SNN Long-Sequence & SSM Modeling"
domain: "snn"
summary: "Spiking neural network temporal architectures for long-horizon sequence modeling."
current_sota:
  - method: method:longspike
    as_of: "2026-08-26"
    benchmark: "Long Sequence Neuromorphic Suite"
    metric: "context retention"
    value: "Default SOTA SSM-SNN"
    notes: "LongSpike (2606.12895); train with A2SG (2606.11236)."
methods:
  - method:longspike
  - method:a2sg
  - method:silif
  - method:neuronspark
  - method:bispikclm
tags:
  - snn
  - ssm
  - longspike
---

# SNN Long-Sequence & SSM Modeling

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **LongSpike** (`method:longspike`, 2606.12895); train with **A2SG** (`method:a2sg`, 2606.11236).
