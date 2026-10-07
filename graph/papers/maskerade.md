---
id: paper:maskerade
type: paper
title: "MASKerade: Token-Routed Mask Experts for Dense-to-MoE Upcycling"
authors:
  - Mingyuan Zhang
  - Yue Bai
  - Zhongruo Wang
  - Yupin Huang
  - Yiyang Huang
  - Hailing Wang
  - Huimin Zeng
  - Yun Fu
year: 2026
month: 10
arxiv_id: "2610.07809"
url: "https://arxiv.org/abs/2610.07809"
methods:
  - method:maskerade
cites:
  - paper:deepseek-v4
tags:
  - pretraining
  - moe
  - upcycling
  - maskerade
---

# MASKerade: Token-Routed Mask Experts for Dense-to-MoE Upcycling

## Abstract Summary
MASKerade upcycles a dense FFN into routed binary-mask experts over the frozen parent (e.g. four 2:4 experts, top-2). First hop on `task:dense-to-moe-upcycling`. Code Ming-K9/MASKerade. Does not replace DeepSeek-V4 / Kimi-K3.

## Key Contributions
1. **Learned binary-mask experts** over a frozen dense FFN.
2. **Token-routed** 2:4 experts, top-2.
3. **Released code** at Ming-K9/MASKerade.

## Empirical Highlights
- Upcycling, not sparse-from-scratch. Do not retarget V4 / K3.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07809`
- Code: `https://github.com/Ming-K9/MASKerade` (`code_status: released`; HTTP 200 as of 2026-10-07).
