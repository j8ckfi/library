---
id: method:dora
type: method
title: "DoRA (Weight-Decomposed Low-Rank Adaptation)"
category: "peft"
status: superseded
superseded_by: method:lr-matters-lora
sota_for: []
supersedes:
  - method:lora
papers:
  - paper:dora
  - paper:dora-paper
recipes:
  - recipe:dora-finetuning
claims:
  - benchmark: "LLaMA-7B/13B Commonsense Reasoning"
    metric: "mean accuracy"
    value: 78.7
    baseline: "LoRA (77.2), Full Fine-Tuning (78.3)"
    date: "2024-02"
    verified: true
    notes: "Consistently outperforms standard LoRA at identical rank without adding inference latency after weight merging."
tags:
  - peft
  - low-rank
  - fine-tuning
---

# DoRA (Weight-Decomposed Low-Rank Adaptation)

## Method Overview
DoRA decomposes a pre-trained weight matrix into magnitude and directional components.

## Supersession
- Superseded by `method:lr-matters-lora` (2602.04998) as quality default.
