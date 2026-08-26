---
id: paper:dora-paper
type: paper
title: "DoRA: Weight-Decomposed Low-Rank Adaptation"
authors:
  - "Shih-Yang Liu"
  - "Chien-Yi Wang"
  - "Hongxu Yin"
  - "Pavlo Molchanov"
  - "Yu-Chiang Frank Wang"
  - "Kwang-Ting Cheng"
  - "Min-Hung Chen"
year: 2024
month: 2
arxiv_id: "2402.09353"
url: "https://arxiv.org/abs/2402.09353"
methods:
  - method:dora
cites:
  - paper:lora-paper
tags:
  - peft
  - low-rank
  - parameter-efficient
---

# DoRA: Weight-Decomposed Low-Rank Adaptation

## Abstract Summary
DoRA discovers that full fine-tuning exhibits fundamental differences in magnitude vs directional weight updates compared to standard LoRA. By decomposing pre-trained weights into magnitude vectors and directional matrices, DoRA updates directional components with low-rank adapters while learning magnitude vectors separately, matching full fine-tuning capacity with zero additional inference latency.

## Key Contributions
1. **Magnitude-Direction Analysis**: Formalized the distinct learning dynamics between LoRA and full parameter fine-tuning.
2. **Weight-Decomposed Formulation**: Introduced decoupled directional LoRA with learnable magnitude scaling.
3. **Consistently Higher Accuracy**: Outperformed LoRA across commonsense reasoning, visual instruction tuning, and GLUE tasks.
