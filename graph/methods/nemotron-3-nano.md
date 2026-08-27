---
id: method:nemotron-3-nano
type: method
title: "Nemotron-3-Nano Architecture"
category: "architecture"
status: active
papers:
  - paper:nemotron-3-nano
recipes:
  - recipe:nemotron-3-nano
claims:
  - benchmark: "On-Device & Small LM Benchmarks"
    metric: "throughput & task accuracy"
    value: "High throughput small model Pareto frontier"
    baseline: "Standard Transformer"
    date: "2026-08-26"
    verified: true
    notes: "Optimized small model architecture for low-latency local execution."
tags:
  - architecture
  - pretraining
  - small-lm
  - nemotron
---

# Nemotron-3-Nano Architecture

## Method Overview
Nemotron-3-Nano optimizes transformer layer dimensions and KV-cache heads specifically for memory-constrained edge hardware and low-latency on-device generation.

## When to Use
- Deploying compact (<3B) models to local edge devices and laptops.
