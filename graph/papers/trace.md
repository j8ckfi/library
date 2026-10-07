---
id: paper:trace
type: paper
title: "TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models"
authors:
  - Xin Wang
  - Hao Yu
  - Zhengyang Zhuge
  - Bochao Mao
  - Zheng Li
  - Junda Feng
  - Yuyan Luo
  - Yi Zhang
  - Yizhong Cao
  - Mi Zhang
  - Dayiheng Liu
  - Jianwei Zhang
year: 2026
month: 10
arxiv_id: "2610.07767"
url: "https://arxiv.org/abs/2610.07767"
methods:
  - method:trace
cites:
  - paper:quartet-ii
tags:
  - post-training
  - quantization
  - fp4
  - moe
  - trace
---

# TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models

## Abstract Summary
FP4 RL of MoE LMs fails when train-side rounding disagrees with rollout-side quantization. TRACE is rollout-guided QAT: it aligns train-side FP4 rounding to rollout-side quantization and caches mantissa/scale from the rollout engine. Up to 5.4× rollout speedup on Qwen3.5-35B-A3B / 122B-A10B / Qwen3.8-Flash-Next / 2.4T-A95B. Dual-active with TRIAGE on the FP4 RL train–rollout task. Does not replace Quartet-II.

## Key Contributions
1. **Rollout-guided QAT** for FP4 RL of MoE LMs.
2. **Cache mantissa/scale** from the rollout side into the train grid.
3. **Up to 5.4× rollout speedup** vs unaligned FP4 RL.

## Empirical Highlights
- MoE models Qwen3.5-35B-A3B / 122B-A10B / Qwen3.8-Flash-Next / 2.4T-A95B.
- Up to 5.4× rollout speedup.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07767`
- Code: none found as of 2026-10-07 (`code_status: none`).
