---
id: paper:led
type: paper
title: 'LED: Improving Masked Diffusion Language Models by Lookahead Editing'
authors:
- 'Yuyan Zhou'
- 'Zeyuan Yang'
- 'Yuxuan Song'
- 'Zhicheng Cai'
- 'Hongli Yu'
- 'Weiying Ma'
- 'Hao Zhou'
- 'James Kwok'
year: 2026
month: 10
arxiv_id: '2610.23122'
url: https://arxiv.org/abs/2610.23122
methods:
- method:led
cites:
- paper:a2d
- paper:justopd
tags:
- dllm
- mdm
- sft
- active
---

# LED

## Abstract Summary
Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive language models, enabling non-autoregressive text generation through parallel decoding. Existing dLLMs can be broadly categorized into two families: masked diffusion models (MDMs) and uniform diffusion models (UDMs) In this work, we theoretically show that MDMs are easier to optimize due to their mask-based transition schedule but have lower computational expressivity, whereas UDMs enable iterative state revision and greater expressivity but are substantially harder to train. This trade-off raises a natural question: can we obtain the expressivity of iterative revision without giving up the simp

## Key Contributions
1. Lookahead Editing keeps MDM's mask-based transition schedule and adds a rewritable proposal state: each decode step runs several lookahead updates before committing tokens to the masked sequence.

## Empirical Highlights
- +11.4 (7B) / +7.7 (8B) vs MDM SFT; LED-8B SFT-only beats LLaDA2.1-16B Q-mode (CPT+SFT+RL)

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23122`
- Code: `none found` (`code_status: none`).
