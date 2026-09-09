---
id: paper:rpb
type: paper
title: "Router Prior Bias: Preserving Base Routing Structure in MoE Post-Training"
authors:
  - "Jaedeok Lee"
  - "Keonwoo Kim"
  - "Dongyoon Han"
  - "Sangdoo Yun"
  - "Yera Choi"
  - "Haanju Yoo"
year: 2026
month: 9
arxiv_id: "2609.08115"
url: "https://arxiv.org/abs/2609.08115"
methods:
  - method:rpb
cites: []
tags:
  - post-training
  - moe
  - routing
  - rpb
---

# Router Prior Bias: Preserving Base Routing Structure in MoE Post-Training

## Abstract Summary
MoE pretraining uses a load-balancing loss to push expert utilization toward uniformity. Post-training inherits a different situation: the base router already encodes non-uniform expert co-activation, which a re-imposed uniformity objective flattens. Router Prior Bias (RPB) is a training-time bias that pulls router logits toward a prior read from the frozen base router while leaving the router trainable (soft router anchoring). Weight, logit, and output-distribution anchors perform comparably; the effect is the softness of the constraint. Hard assignment of the same prior preserves community structure but drops downstream accuracy.

## Key Contributions
1. **Soft router anchoring** as the post-train principle, vs re-applied LBL or unanchored FT.
2. **RPB**: bias toward a frozen-base prior; router stays trainable.
3. **Community structure is a footprint**, not the mechanism: hard assignment keeps communities and still loses.

## Empirical Highlights
- Moonlight-16B-A3B math post-train: RPB 45.77 in-domain vs re-applied LBL 31.91 vs unanchored FT 29.44; more OOD retained than either.
- Ordering vs LBL reproduces on Qwen3-30B-A3B-Base; LBL gap also on an independently sourced corpus.

## Open Source Repository & Resources
- Claimed code: `https://github.com/naver-ai/rpb` (404 at 2026-09-09 ingest; paper says code will be released).
