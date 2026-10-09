---
id: paper:onlineqat
type: paper
title: "OnlineQAT: On-Policy Distillation for Ultra-Low-Bit Large Language Models"
authors:
  - "Wenjun Wang"
  - "Heng Li"
  - "Yanggan Gu"
  - "Hongxia Yang"
year: 2026
month: 10
arxiv_id: "2610.09346"
url: "https://arxiv.org/abs/2610.09346"
methods:
  - method:onlineqat
cites:
  - paper:opd
  - paper:gradcodes
tags:
  - quantization
  - qat
  - opd
  - onlineqat
---

# OnlineQAT: On-Policy Distillation for Ultra-Low-Bit Large Language Models

## Abstract Summary
Ultra-low-bit QAT recovery is usually trained on fixed or teacher completions, so the quantized student visits prefixes that never appeared in the recovery set. OnlineQAT first gets a usable low-bit init via block-wise QAT, then runs sampled reverse-KL OPD on student-generated responses against a frozen full-precision teacher. Qwen3-1.7B: 57.28 W3A16 and 32.52 W2A16 average, +2.90 / +0.44 vs ReasoningQAT. Beside GradCodeS. No official GitHub as of 2026-10-09.

## Key Contributions
1. Fixed-completion QAT recovery misses student-visited prefixes under quantization noise.
2. Two-stage: block-wise QAT init, then on-policy reverse-KL against a frozen full-precision teacher.
3. Largest lift at 3 bits; smaller at 2 bits.

## Empirical Highlights
- Qwen3-1.7B average: 57.28 W3A16 and 32.52 W2A16.
- +2.90 / +0.44 vs ReasoningQAT at W3A16 / W2A16.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.09346`
- Code: none found as of 2026-10-09 (`code_status: none`).
