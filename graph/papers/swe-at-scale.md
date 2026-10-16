---
id: paper:swe-at-scale
type: paper
title: 'SWE-at-Scale: Scalable Issue Synthesis from Historical Bug Fixes'
authors:
- Silin Chen
- Zihan Zhang
- Xiaodong Gu
- Jiale Huang
- Yuling Shi
- Han Li
- Zhao Shan
- Chengcheng Wan
- Zhensu Sun
- Haibing Guan
year: 2026
month: 10
arxiv_id: '2610.21359'
url: https://arxiv.org/abs/2610.21359
methods:
- method:swe-at-scale
cites:
- paper:codemidas
tags:
- swe
- data-curriculum
---

# SWE-at-Scale

## Abstract Summary
Real SWE tasks arrive at the rate of issue reports. SWE-at-Scale inverts historical bug fixes into bug-induction supervision, transfers those patterns to novel code contexts, and samples diverse executable issues from a single file.

## Key Contributions
1. Fix inversion as bug-induction supervision.
2. Pattern transfer to novel contexts.
3. Diversity scaling to 200 generations per file.

## Empirical Highlights
- More diverse and harder than current synthesis baselines; distinct bug types from one context.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.21359`
- Code: `https://github.com/cslsolow/SWE-at-scale` (`code_status: released`).
- Models: `https://huggingface.co/SWE-at-Scale`

