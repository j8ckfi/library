---
id: paper:opd-failure-problems
type: paper
title: 'Correcting or Continuing? What On-Policy Distillation Learns from Student Errors'
authors:
- Shuo Yang
- Zheyu Zhang
- Mahito Sugiyama
- Gjergji Kasneci
year: 2026
month: 10
arxiv_id: '2610.18011'
url: https://arxiv.org/abs/2610.18011
methods:
- method:opd
cites:
- paper:opd
tags:
- distillation
- opd
- gotcha
---

# Correcting or Continuing? OPD on student-failure problems

## Abstract Summary
Gotcha on student distillation. Five OPD mechanisms degrade accuracy when training is restricted to problems the student fails (8/8 configs, p=0.0078) while KL keeps dropping. The same pipeline is +4.6pp on a non-failure mix. Do not concentrate OPD on all-fail prompts.

## Key Contributions
1. Fail-set OPD: 8/8 configs degrade, binomial p=0.0078.
2. Non-failure mix +4.6pp on Qwen2.5-0.5B GSM8K 43.6→48.2.
3. KL dropping is not a quality signal on fail-only sets.

## Empirical Highlights
- Restricting to student-failure problems reverses the usual OPD sign.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.18011`
- Code: `none found` (`code_status: none`).
