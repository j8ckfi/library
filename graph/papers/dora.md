---
id: paper:dora
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
  - dora
---

# DoRA: Weight-Decomposed Low-Rank Adaptation

## Abstract Summary
DoRA decomposes pre-trained weights into magnitude vectors and directional matrices, updating directional components via low-rank adapters while optimizing magnitude vectors independently.

## Open Source Repository
- Implementation: `https://github.com/NVlabs/DoRA` (Hugging Face PEFT `use_dora=True`)
