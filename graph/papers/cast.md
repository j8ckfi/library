---
id: paper:cast
type: paper
title: 'CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation'
authors:
- Jingru Yang
- Jinhang Wu
- Minjing Shi
- Shengfeng He
- Xuyan Li
- Man Tan
- Biye Li
year: 2026
month: 10
arxiv_id: '2610.13257'
url: https://arxiv.org/abs/2610.13257
methods:
- method:cast
cites:
- paper:cross-tokenizer-opd
- paper:opd
tags:
- post-training
- distillation
- opd
- cross-tokenizer
- cast
---

# CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation

## Abstract Summary
Decoded-text alignment gives chunk correspondence for cross-tokenizer OPD but not credit: how to split a chunk-level signal across student tokens, and what to do at unaligned positions. CAST redistributes each aligned chunk's advantage by predictive uncertainty and local teacher-signal smoothness (exact KL-regularized allocation that preserves the chunk total) and KL-anchors unaligned tokens to the initial student policy.

## Key Contributions
1. Separates chunk construction from credit assignment; also applies to punctuation or fixed-length shared-tokenizer chunks.
2. Unaligned-token stay via selective initial-policy KL.
3. Cross-tokenizer and shared-tokenizer gains vs the paper's strongest OPD baselines.

## Empirical Highlights
- See `method:cast` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13257`
- Code: `none found` (`code_status: none`).
