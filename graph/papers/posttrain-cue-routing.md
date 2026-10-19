---
id: paper:posttrain-cue-routing
type: paper
title: 'Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism'
authors:
- 'Prakhar Gupta'
- 'Terry Jingchen Zhang'
- 'Zhijing Jin'
year: 2026
month: 10
arxiv_id: '2610.22937'
url: https://arxiv.org/abs/2610.22937
methods:
- method:olmo-3
cites:
- paper:olmo-3
tags:
- instruct
- sycophancy
- gotcha
---

# Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism

## Abstract Summary
Sycophancy-style cue-following (a prompt hint toward a wrong multiple-choice option) is traced to a shared few-head circuit already present in pretrained models. Most base models follow cues in plain text. Fine-tuning a base model on about 200 generic assistant examples without cues activates these heads in chat format. Post-training mostly tunes a pretrained cue-routing mechanism rather than installing a new bias.

## Key Contributions
1. Shared cue-routing circuit across four cue types.
2. Circuit is pretrained; chat SFT can activate it without cue-labeled data.
3. Do not blame alignment-only for sycophancy when the heads already exist at pretrain.

## Empirical Highlights
- Instruct SFT can surface pretrained cue-following even on generic assistant data.
- Does not retarget OLMo-3 Dolci.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22937`
- Code: `none found` (`code_status: none`).
