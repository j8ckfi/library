---
id: paper:triage
type: paper
title: "TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning"
authors:
  - Zhen Li
  - Shuai Zhang
  - Yanggan Gu
  - Yiming Zhang
  - Yang Yu
  - Mingfa Feng
  - Congkai Xie
  - Shuang Yu
  - Junjie Lai
  - Hongxia Yang
year: 2026
month: 10
arxiv_id: "2610.07043"
url: "https://arxiv.org/abs/2610.07043"
methods:
  - method:triage
cites:
  - paper:quartet-ii
tags:
  - post-training
  - quantization
  - nvfp4
  - rl-alignment
  - triage
---

# TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning

## Abstract Summary
Native NVFP4 RL is unstable when train–rollout mismatch amplifies negative-advantage / negative-gap updates. TRIAGE diagnoses at segment level and rebalances those amplifying directions. Qwen3-4B / 30B-A3B; up to 2.3× rollout vs BF16; full-precision-level math on five reasoning benches. Dual-active with TRACE. No head-to-head vs TRACE. Does not replace Quartet-II.

## Key Contributions
1. **Direction-aware mismatch** diagnosis at segment level.
2. **Rebalance amplifying negative-advantage / negative-gap** updates.
3. **Up to 2.3× rollout vs BF16** while retaining native NVFP4 W4A4.

## Empirical Highlights
- Qwen3-4B / Qwen3-30B-A3B native NVFP4 RL.
- >34500 GPU-h B300.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07043`
- Code: none found as of 2026-10-07 (`code_status: none`).
