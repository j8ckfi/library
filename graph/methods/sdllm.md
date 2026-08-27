---
id: method:sdllm
type: method
title: "SDLLM (Spiking Diffusion Language Model)"
category: "snn"
status: active
papers:
  - paper:sdllm
recipes:
  - recipe:sdllm
claims:
  - benchmark: "Generative Text Synthesis"
    metric: "generation latency"
    value: "Parallel non-autoregressive spiking generation"
    baseline: "Diffusion LM"
    date: "2026-08-26"
    verified: true
    notes: "Spiking score-based diffusion model."
tags:
  - snn
  - diffusion
  - sdllm
---

# SDLLM (Spiking Diffusion Language Model)

## Method Overview
SDLLM combines non-autoregressive diffusion score matching with spiking temporal dynamics for fast, low-energy text generation.

## When to Use
- Fast parallel generative modeling on neuromorphic hardware.
