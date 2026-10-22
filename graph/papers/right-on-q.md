---
id: paper:right-on-q
type: paper
title: 'Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories'
authors:
- 'Boyuan Zheng'
- 'Jing Xiong'
- 'Chenwei Wu'
- 'Hui Shen'
- 'Zesen Zhao'
- 'Hei Ting Una Chan'
- 'Xueshen Liu'
- 'Zhen Zhang'
year: 2026
month: 10
arxiv_id: '2610.29378'
url: https://arxiv.org/abs/2610.29378
methods:
- method:right-on-q
cites:
- paper:gradcodes
- paper:onlineqat
tags:
- quantization
- qat
- active
---

# Right On Q

## Abstract Summary
Right On Q (OnQ) drops fixed-response QAT and supervises the quantized student on its own generated prefixes with a dynamic KL, so long-horizon reasoning prefixes match decode.

## Key Contributions
1. Right On Q as an active plug-in on `task:full-lowbit-finetune`.

## Empirical Highlights
- beats every 2-bit baseline on every bench and size; Qwen3-8B average +10.26. Does not retarget `method:gradcodes`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29378`
- Code: `none found` (`code_status: none`).
