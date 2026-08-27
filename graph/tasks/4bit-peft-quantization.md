---
id: task:4bit-peft-quantization
type: task
title: "4-Bit Quantized PEFT & Adaptation"
domain: "efficiency"
summary: "Fine-tuning quantized foundation models in 4-bit memory constraints with high throughput."
current_sota:
  - method: method:aqlora-q
    as_of: "2026-08-26"
    benchmark: "4-Bit Single GPU PEFT"
    metric: "speed and accuracy retention"
    value: "Default SOTA Speed/Recipe on 4-Bit Stack"
    notes: "AQLoRA-Q (2608.23816) or AutoQRA (2602.22268)."
  - method: method:autoqra
    as_of: "2026-08-26"
    benchmark: "Automated 4-Bit Quantized Adaptation"
    metric: "residual error preservation"
    value: "Co-Default SOTA"
    notes: "AutoQRA (2602.22268) automated bit allocation."
methods:
  - method:aqlora-q
  - method:autoqra
  - method:qlora
  - method:beft
tags:
  - efficiency
  - peft
  - quantization
  - 4bit
---

# 4-Bit Quantized PEFT & Adaptation

## SOTA Recommendation (as of 2026-08-26)
- **Primary Method**: **AQLoRA-Q** (`method:aqlora-q`, 2608.23816) or **AutoQRA** (`method:autoqra`, 2602.22268).
