---
id: paper:qlora-paper
type: paper
title: "QLoRA: Efficient Finetuning of Quantized LLMs"
authors:
  - "Tim Dettmers"
  - "Artidoro Pagnoni"
  - "Ari Holtzman"
  - "Luke Zettlemoyer"
year: 2023
month: 5
arxiv_id: "2305.14314"
url: "https://arxiv.org/abs/2305.14314"
methods:
  - method:qlora
cites:
  - paper:lora-paper
tags:
  - peft
  - quantization
  - memory-efficiency
---

# QLoRA: Efficient Finetuning of Quantized LLMs

## Abstract Summary
QLoRA demonstrates that 65B parameter language models can be fine-tuned on a single 48GB GPU without performance degradation. It introduces 4-bit NormalFloat (NF4), Double Quantization (DQ) to compress quantization constants, and Paged Optimizers to eliminate memory fragmentation spikes.

## Key Contributions
1. **NF4 Quantization**: Information-theoretically optimal quantile format for Gaussian distributed model weights.
2. **Double Quantization**: Compresses quantization scale factors.
3. **Paged Optimizers**: Prevents OOM errors via CUDA Unified Memory paging.
