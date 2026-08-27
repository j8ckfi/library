---
id: method:neuronspark
type: method
title: "NeuronSpark Spiking Transformer"
category: "snn"
status: active
papers:
  - paper:neuronspark
recipes:
  - recipe:neuronspark
claims:
  - benchmark: "Spiking Transformer Benchmarks"
    metric: "dynamic energy consumption"
    value: "Multi-fold dynamic energy reduction"
    baseline: "Standard Transformer"
    date: "2026-08-26"
    verified: true
    notes: "Spike coincidence-driven self-attention."
tags:
  - snn
  - transformer
  - neuronspark
---

# NeuronSpark Spiking Transformer

## Method Overview
NeuronSpark replaces floating-point attention operations with thresholded spike coincidence detection, matching transformer accuracy with neuromorphic power efficiency.

## When to Use
- Deploying transformer-like models to ultra-low-power neuromorphic processors.
