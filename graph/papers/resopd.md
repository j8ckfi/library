---
id: paper:resopd
type: paper
title: "ResOPD: Tail Residualization for Sparse On-Policy Distillation"
authors:
  - Penghui Yang
  - Long Xing
  - Xuanlang Dai
  - Ziyu Liu
  - Kai Chen
  - Yuhang Zang
year: 2026
month: 10
arxiv_id: "2610.04882"
url: "https://arxiv.org/abs/2610.04882"
methods:
  - method:resopd
cites:
  - paper:opd
  - paper:sparse-opd-supervision
tags:
  - post-training
  - distillation
  - opd
  - resopd
---

# ResOPD: Tail Residualization for Sparse On-Policy Distillation

## Abstract Summary
Sparse OPD payloads (sampled-token score or Top-k) face unbiased-but-high-variance vs biased Top-k objectives. ResOPD aggregates the unobserved vocabulary into an observable coarse tail event, computes that aggregate gradient exactly, and samples only the fine-grained within-tail residual, with no extra teacher queries. Claims unbiased full-vocabulary reverse-KL gradients under on-policy sampling and substantial variance reduction under the same sparse payload. Announced GitHub InternLM/ResOPD was 404 as of 2026-10-06. Beside sparse-opd-supervision.

## Key Contributions
1. **Tail residualization**: coarse tail event + sampled within-tail residual.
2. **Unbiased full-vocab reverse KL** under the same sparse teacher payload.
3. **No extra teacher forwards** for the residual.

## Empirical Highlights
- Abstract: substantial variance reduction and improved downstream performance in the evaluated settings.
- Do not invent 52–75% or +4.40 figures; they are not in the abstract.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04882`
- Code: announced `https://github.com/InternLM/ResOPD` (HTTP 404 as of 2026-10-06; `code_status: announced`).
