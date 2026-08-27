---
id: method:sherry
type: method
title: "Sherry (AngelSlim Structured Quantization)"
category: "quantization"
status: active
papers:
  - paper:sherry
recipes:
  - recipe:sherry
claims:
  - benchmark: "LLM Structured Compression Suite"
    metric: "compression ratio & latency"
    value: "Production structured low-bitweight compression"
    baseline: "AWQ"
    date: "2026-08-26"
    verified: true
    notes: "Structured low-bitweight model compression in Tencent AngelSlim."
tags:
  - quantization
  - compression
  - angelslim
  - sherry
---

# Sherry (AngelSlim Structured Quantization)

## Method Overview
Sherry provides structured low-bitweight model compression and kernel compilation for high-throughput enterprise serving.

## When to Use
- Production compression pipelines targeting sub-4-bit deployment.
