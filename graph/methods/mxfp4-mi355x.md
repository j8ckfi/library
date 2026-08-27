---
id: method:mxfp4-mi355x
type: method
title: "MXFP4 (Microscaling FP4 Training)"
category: "quantization"
status: sota
sota_for:
  - task:fp4-hardware-training
papers:
  - paper:mxfp4-mi355x
recipes:
  - recipe:mxfp4-mi355x
claims:
  - benchmark: "Microscaled FP4 Benchmark"
    metric: "numerical stability & hardware utilization"
    value: "Co-default microscaling FP4 hardware training format"
    baseline: "FP8"
    date: "2026-08-26"
    verified: true
    notes: "OCP Microscaling FP4 format specifications for modern accelerators."
tags:
  - quantization
  - fp4
  - mxfp4
  - hardware-training
  - sota
---

# MXFP4 (Microscaling FP4 Training)

## Method Overview
MXFP4 implements the OCP Microscaling FP4 format for high-throughput hardware training, sharing block-level exponents across 32 elements to prevent underflow.

## When to Use
- Microscaled FP4 hardware training across multi-vendor accelerator hardware (e.g. AMD MI355X).
