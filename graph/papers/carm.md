---
id: paper:carm
type: paper
title: "CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning"
authors:
  - "Yafei Zhang"
  - "Songshuo Lu"
  - "Sicong Liao"
  - "Zhi Chen"
  - "Yaohua Tang"
year: 2026
month: 10
arxiv_id: "2610.02039"
url: "https://arxiv.org/abs/2610.02039"
methods:
  - method:carm
cites:
  - paper:grpo
  - paper:cis-rl
  - paper:miles
tags:
  - post-training
  - rl-alignment
  - off-policy
  - carm
  - masking
---

# CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning

## Abstract Summary
Production RLVR is off-policy: stale mini-batches, actor–learner delay, vLLM/SGLang vs FSDP/Megatron. Sequence-level masks that average signed token log-ratios (GeoMean / DeepSeek-V3.2) let \(r=10\) and \(r=0.1\) cancel to a geometric mean of 1. CARM averages absolute log-ratios before the threshold, then keeps the token PPO/GRPO surrogate. Moore Threads AI. No public code as of 2026-10-02.

## Key Contributions
1. **Cancellation diagnosis**: signed-log sequence scores can look on-policy while every token ratio is far from 1.
2. **Absolute-log mask**: \(d_{\mathrm{CARM}}=(1/T)\sum_t|\log r_t|\); accepted responses jointly bound the fraction of out-of-band ratios and their mean log-distance beyond the band.
3. **Complement, not replacement**: token clipping / CIS-RL stay; CARM only admits or rejects the response.

## Empirical Highlights
- Math mean@16 averaged over AIME 2024/2025/2026 and BeyondAIME: up to +3.13 pp vs geometric-mean masking.
- Four code benches, average pass@1: +2.88 pp vs the strongest evaluated baseline. Filtering rate is not monotone in accuracy.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02039`
- Code: none found as of 2026-10-02 (`code_status: none`).
