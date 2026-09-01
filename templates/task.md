---
id: task:template-task
type: task
title: "Task Title"
domain: "pretraining" # pretraining | post-training | efficiency | compression | snn | interpretability | video | control | scientific-ml | systems | algorithms | agents
summary: "High-level summary of the optimization or capability challenge."
scope: "One sentence: exactly what problems this task node owns."
out_of_scope: []
# - "Near-miss problem that looks like this task but is not"
redirects: []
# - when: "condition under which the reader should go elsewhere"
#   to: "task:other-task-slug"
last_reviewed: "2026-01-01" # last date current_sota was re-verified against literature
current_sota:
  - method: method:example-method
    as_of: "2026-01"
    benchmark: "StandardBenchmark"
    metric: "accuracy"
    value: 92.4
    notes: "Evaluated under standard 8x H100 compute budget."
methods:
  - method:example-method
tags:
  - pretraining
  - language-models
---

# Task Title

## Problem Definition
Describe the fundamental machine learning problem, formulation, and objectives.

## Evaluation Protocol & Benchmarks
- **Primary Benchmarks**: List standard evaluation datasets and metrics.
- **Evaluation Hazards**: Data contamination risks, evaluation prompt sensitivities, or metric anomalies.

## SOTA Landscape
Summary of the current state-of-the-art methods and historical paradigm shifts.
