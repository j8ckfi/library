---
id: method:autoqra
type: method
title: "AutoQRA (Automated Quantized Residual Adaptation)"
category: "peft"
status: sota
sota_for:
  - task:4bit-peft-quantization
papers:
  - paper:autoqra
recipes:
  - recipe:autoqra
claims:
  - benchmark: "4-Bit Fine-Tuning"
    metric: "residual error preservation"
    value: "Co-default 4-bit PEFT solution"
    baseline: "QLoRA"
    date: "2026-08-26"
    verified: true
    notes: "Automated layer-wise bit allocation for quantized fine-tuning."
tags:
  - peft
  - quantization
  - autoqra
  - sota
---

# AutoQRA (Automated Quantized Residual Adaptation)

## Method Overview
AutoQRA automatically tunes bit allocations and adapter ranks across individual transformer layers based on gradient sensitivity.

## When to Use
- Co-default alternative to AQLoRA-Q for automated 4-bit quantized adapter fine-tuning.
