---
id: method:bispikclm
type: method
title: "BiSpikCLM"
category: "snn"
status: active
papers:
  - paper:bispikclm
recipes:
  - recipe:bispikclm
claims:
  - benchmark: "Causal Spiking Language Modeling"
    metric: "perplexity & spike rate"
    value: "Bidirectional membrane state persistence"
    baseline: "Standard Spiking LM"
    date: "2026-08-26"
    verified: true
    notes: "Autoregressive causal language modeling with LIF dynamics."
tags:
  - snn
  - language-models
  - bispikclm
---

# BiSpikCLM

## Method Overview
BiSpikCLM adapts leaky integrate-and-fire dynamics for autoregressive next-token prediction, preserving semantic membrane states across generation steps.

## When to Use
- Neuromorphic on-device language generation.
