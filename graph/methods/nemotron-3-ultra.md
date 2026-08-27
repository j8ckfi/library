---
id: method:nemotron-3-ultra
type: method
title: "Nemotron-3-Ultra MoE Architecture"
category: "architecture"
status: active
papers:
  - paper:nemotron-3-ultra
recipes:
  - recipe:nemotron-3-ultra
claims:
  - benchmark: "Frontier MoE Benchmarks"
    metric: "cluster throughput & loss"
    value: "Topology-aware MoE scaling"
    baseline: "Dense Baseline"
    date: "2026-08-26"
    verified: true
    notes: "Multi-node NVLink/InfiniBand-aligned expert routing."
tags:
  - architecture
  - moe
  - frontier
  - nemotron
---

# Nemotron-3-Ultra MoE Architecture

## Method Overview
Nemotron-3-Ultra structures large Mixture-of-Experts architectures around hardware network topologies, minimizing cross-node all-to-all communication bottlenecks.

## When to Use
- Pretraining multi-hundred-billion parameter MoE models across large GPU clusters.
