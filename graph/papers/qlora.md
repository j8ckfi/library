---
id: paper:qlora
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
  - qlora
---

# QLoRA: Efficient Finetuning of Quantized LLMs

## Abstract Summary
QLoRA backpropagates gradients through 4-bit quantized base models into 16-bit low-rank adapters (LoRA). Using 4-bit NormalFloat (NF4), Double Quantization, and Paged Optimizers, QLoRA reduces the memory footprint of fine-tuning a 65B model from >780GB to <48GB without sacrificing task performance.

## Open Source Repository
- Implementation: `https://github.com/artidoro/qlora`
