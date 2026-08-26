---
id: paper:lora-paper
type: paper
title: "LoRA: Low-Rank Adaptation of Large Language Models"
authors:
  - "Edward J. Hu"
  - "Yelong Shen"
  - "Phillip Wallis"
  - "Zeyuan Allen-Zhu"
  - "Yuanzhi Li"
  - "Shean Wang"
  - "Lu Wang"
  - "Weizhu Chen"
year: 2021
month: 6
arxiv_id: "2106.09685"
url: "https://arxiv.org/abs/2106.09685"
methods:
  - method:lora
cites: []
tags:
  - peft
  - low-rank
  - foundational
---

# LoRA: Low-Rank Adaptation of Large Language Models

## Abstract Summary
LoRA proposes freezing the pre-trained model weights and injecting trainable rank decomposition matrices into each layer of the Transformer architecture, reducing trainable parameter count by 10,000x and GPU memory requirements by 3x without introducing inference latency.

## Key Contributions
1. Formalized low-rank matrix decomposition \(\Delta W = B \cdot A\) for adapter-based parameter-efficient fine-tuning.
2. Established parameter efficiency across GPT-3 and RoBERTa benchmarks.
