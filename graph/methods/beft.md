---
id: method:beft
type: method
title: "BEFT (Binarized Efficient Fine-Tuning)"
category: "peft"
status: active
papers:
  - paper:beft
recipes:
  - recipe:beft
claims:
  - benchmark: "Ultra-Low Memory PEFT"
    metric: "memory footprint"
    value: "Binarized adapter fine-tuning"
    baseline: "LoRA"
    date: "2026-08-26"
    verified: true
    notes: "1-bit adapter matrices with integer scaling."
tags:
  - peft
  - quantization
  - binarization
  - beft
---

# BEFT (Binarized Efficient Fine-Tuning)

## Method Overview
BEFT optimizes binarized 1-bit low-rank adapter weights with integer scaling factors for ultra-low memory fine-tuning.

## When to Use
- Extreme memory constraints where even 16-bit LoRA adapter weights exceed memory limits.
