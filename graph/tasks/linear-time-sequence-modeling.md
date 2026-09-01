---
id: task:linear-time-sequence-modeling
type: task
title: "Linear-Time Sequence Modeling & Recurrent Architectures"
domain: "pretraining"
summary: "Long-sequence autoregressive modeling with sub-quadratic O(N) training and O(1) per-step inference complexity."
current_sota:
  - method: method:mamba-2
    as_of: "2024-05"
    benchmark: "Pile / FineWeb Token Perplexity & Throughput"
    metric: "tokens/sec per H100"
    value: "8x vs standard attention"
    notes: "State Space Duality (SSD) connects structured state spaces with matrix multiplication tensor cores."
methods:
  - method:mamba-2
  - method:qwen38-next
  - method:gated-deltanet-2
last_reviewed: "2026-09-01"
tags:
  - pretraining
  - architecture
  - state-space-models
---

# Linear-Time Sequence Modeling & Recurrent Architectures

## Problem Definition
Standard multi-head attention scales quadratically \(O(N^2)\) with sequence length \(N\) in compute and memory, creating severe bottlenecks for ultra-long context windows (>64k tokens) and real-time streaming inference. Linear-time sequence models aim to achieve sub-quadratic or linear complexity \(O(N)\) during training with constant memory \(O(1)\) state caching during generation.

## Evaluation Protocol & Benchmarks
- **Evaluation Benchmarks**: Long-context associative recall, language modeling perplexity across token budgets (10B–300B), and Needle-In-A-Haystack retrieval at 64k–1M context lengths.
- **Hardware Metrics**: Training tokens per second per GPU, inference latency and memory footprint during continuous generation.

## SOTA Landscape
While original linear attention models suffered from expressive capacity deficits compared to full attention, modern structured state-space models and linear attention variants (specifically Mamba-2 / SSD) close the performance gap while running dramatically faster on GPU matrix engines.
