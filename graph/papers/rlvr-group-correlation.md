---
id: paper:rlvr-group-correlation
type: paper
title: "Are Verifier Errors Independent Within a GRPO Group? Evidence from Qwen2.5 Rollouts"
authors:
  - "Esther Xin"
year: 2026
month: 9
arxiv_id: "2609.06386"
url: "https://arxiv.org/abs/2609.06386"
methods:
  - method:rlvr-group-correlation
  - method:grpo
  - method:cispo
cites:
  - paper:grpo
tags:
  - post-training
  - rlvr
  - verifier
  - gotcha
  - rlvr-group-correlation
---

# Are Verifier Errors Independent Within a GRPO Group?

## Abstract Summary
Group RLVR scores several completions per prompt with an automatic verifier. Analyses that treat verifier errors as independent miss dependence from shared answer form. On 24,998 groups of eight Qwen2.5-1.5B completions (MATH, GSM8K, DeepMath-103K), pooled within-group verifier-error correlation is 0.530 (95% CI 0.500–0.560), a Kish effective sample size of 1.70 for an eight-completion group. Fractions, radicals, symbolic expressions, and intervals cluster more than unit annotations and percent signs. Replaying group-relative advantages across four rule-based verifier configs finds at least one advantage-sign disagreement in up to 0.83% of groups. This is a hygiene / analysis result, not an optimizer.

## Key Contributions
1. **Within-group ICC**: ρ≈0.53 on real k=8 rollouts; n_eff≈1.70, not 8.
2. **Answer-form dependence**: structurally complex forms cluster; whitespace/punctuation do not drive the headline ρ.
3. **Advantage-sign replay**: verifier-config disagreements flip GRPO signs in <1% of groups in this corpus — still not independence.

## Empirical Highlights
- 24,998 groups, k=8, Qwen2.5-1.5B, MATH / GSM8K / DeepMath-103K.
- ρ = 0.530, 95% CI [0.500, 0.560]; Kish n_eff = 1.70.
- Part 2 of a series; Part 1 is *Where the Verifier Fails* (arXiv:2609.01354), not ingested here.

## Open Source Repository & Resources
- Code: `https://github.com/ethxin0011/rlvr_group_correlation`
