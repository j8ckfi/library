---
id: method:dora
type: method
title: "DoRA (Weight-Decomposed Low-Rank Adaptation)"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
supersedes:
  - method:lora
superseded_by: method:delora
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
DoRA (Weight-Decomposed Low-Rank Adaptation) analyzes the difference between full fine-tuning and standard LoRA updates. It discovers that full fine-tuning alters both the magnitude and directional vectors of weight matrices with weak correlation, whereas standard LoRA couples magnitude and direction changes proportionally.

DoRA decomposes a pre-trained weight matrix \(W_0 \in \mathbb{R}^{d \times k}\) into a magnitude vector \(m \in \mathbb{R}^{1 \times k}\) and a normalized directional matrix \(V \in \mathbb{R}^{d \times k}\):
\[
W = m \frac{W_0 + \Delta W}{\|W_0 + \Delta W\|_F} = m \frac{W_0 + \frac{\alpha}{r} B A}{\|W_0 + \frac{\alpha}{r} B A\|_F}
\]
where \(m = \|W_0\|_c\) is initialized to the column-wise norm of \(W_0\), and \(B \in \mathbb{R}^{d \times r}, A \in \mathbb{R}^{r \times k}\) are low-rank adapter matrices.

## When to Use
- **High-Performance Fine-Tuning**: When fine-tuning LLaMA, Mistral, Qwen, or vision models where standard LoRA falls short of full fine-tuning accuracy.
- **Zero Inference Overhead**: The adapted weights can be merged back into \(W_0\) after training, resulting in identical deployment latency to the base model.

## Gotchas & Failure Modes
1. **Training VRAM Overhead**: Normalizing the combined matrix \(\|W_0 + BA\|_F\) introduces slight training memory overhead (10–15% more than vanilla LoRA during backward pass).
2. **Gradient Checkpointing**: Always enable gradient checkpointing when using DoRA on large 70B+ models to avoid memory spikes from the norm computation.
