---
id: method:qlora
type: method
title: "QLoRA (Quantized 4-bit Low-Rank Adaptation)"
category: "peft"
status: superseded
superseded_by: method:aqlora-q
sota_for: []
supersedes: []
papers:
  - paper:qlora
  - paper:qlora-paper
recipes:
  - recipe:qlora-peft
claims:
  - benchmark: "Vicuna Benchmark / MMLU"
    metric: "99.3% recovery of full 16-bit performance"
    value: 99.3
    baseline: "16-bit Full Fine-Tuning"
    date: "2023-05"
    verified: true
    notes: "Utilizes 4-bit NormalFloat (NF4), Double Quantization, and Paged Optimizers."
tags:
  - peft
  - quantization
  - memory-efficient
---

# QLoRA (Quantized 4-bit Low-Rank Adaptation)

## Method Overview
QLoRA reduces the memory footprint of fine-tuning large models to fit onto a single consumer GPU using NF4 quantization.

## Supersession
- Superseded by `method:aqlora-q` as the speed and recipe default on 4-bit stacks.
