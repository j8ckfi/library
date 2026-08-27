---
id: method:mhc
type: method
title: "mHC (Multi-Head Convolutions)"
category: "architecture"
status: active
papers:
  - paper:mhc
recipes:
  - recipe:mhc
claims:
  - benchmark: "Sub-quadratic Sequence Modeling"
    metric: "throughput / perplexity"
    value: "Hardware-friendly 1D multi-head depthwise convolution"
    baseline: "Transformer Attention"
    date: "2026-08-26"
    verified: true
    notes: "Dynamic depthwise convolutional sequence processing on GPU tensor cores."
tags:
  - architecture
  - convolution
  - mhc
---

# mHC (Multi-Head Convolutions)

## Method Overview
mHC replaces quadratic attention blocks with channel-independent dynamic 1D depthwise convolutions, running at maximum memory bandwidth on modern GPUs.

## When to Use
- Sub-quadratic sequence modeling where attention memory bandwidth is the primary bottleneck.
