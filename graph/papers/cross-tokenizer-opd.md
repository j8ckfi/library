---
id: paper:cross-tokenizer-opd
type: paper
title: "Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability"
authors:
  - Bingxi Hou
  - Guochao Jiang
  - Guofeng Quan
  - Weiqing Li
  - Wenfeng Feng
  - Guohua Liu
  - Yuewei Zhang
year: 2026
month: 10
arxiv_id: "2610.08448"
url: "https://arxiv.org/abs/2610.08448"
methods:
  - method:cross-tokenizer-opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - tokenizer
  - cross-tokenizer-opd
---

# Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability

## Abstract Summary
Cross-tokenizer OPD is usually framed as an alignment problem. Strict 1:1 sequence alignment already covers most student tokens (85.57–96.98%) even when Jaccard overlap is only 39.49–64.87%. The remaining gap is supervision reliability on the shared vocabulary: reverse KL restricted to a student-selected top-16 subset of the shared vocab matches full shared-vocab OPD (≥96% of the gain). Span-level MSE alignment hurts. Beside same-tokenizer OPD. Top HF Daily paper 2026-10-07.

## Key Contributions
1. **Coverage**: strict 1:1 already covers most student tokens despite low Jaccard overlap.
2. **Top-16 shared-vocab reverse-KL** matches full shared-vocab OPD.
3. **Span MSE is the wrong fix** for the leftover tokens.

## Empirical Highlights
- 1:1 coverage 85.57–96.98% at Jaccard 39.49–64.87%.
- k=16 retains ≥96% of full shared-vocab OPD gain.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08448`
- Code: none found as of 2026-10-07 (`code_status: none`).
