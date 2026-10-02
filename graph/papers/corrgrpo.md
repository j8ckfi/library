---
id: paper:corrgrpo
type: paper
title: "CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning"
authors:
  - "Wenbin Hu"
  - "Huihao Jing"
  - "Haochen Shi"
  - "Yuxuan Liu"
  - "Haoran Li"
  - "Yangqiu Song"
year: 2026
month: 9
arxiv_id: "2609.36820"
url: "https://arxiv.org/abs/2609.36820"
methods:
  - method:corrgrpo
cites:
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - multi-reward
  - grpo
  - corrgrpo
---

# CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning

## Abstract Summary
Multi-reward GRPO sums reward components then std-normalizes the total. That variance is the sum of all pairwise covariances, so large-scale correlated rewards dominate the denominator and suppress smaller signals. CorrGRPO keeps the centered total reward and replaces covariances with Pearson correlations. Advantage magnitudes still adapt to reward dependence; scale no longer weights the pairwise terms. HKUST KnowComp. Code: `https://github.com/HKUST-KnowComp/CorrGRPO`.

## Key Contributions
1. **Covariance identity**: multi-reward GRPO's denominator is \(\sum_{l,m}\widehat{\mathrm{Cov}}(R_l,R_m)\); large \(\sigma\) dominates both diagonal and off-diagonal terms.
2. **Pearson denominator**: \(\hat\rho_{lm}=\widehat{\mathrm{Cov}}(R_l,R_m)/(\sigma_l\sigma_m)\); zero-variance rows/columns are zeroed.
3. **Three-domain bake-off**: coding (Pass@1 + efficiency), tool calling, agent utility vs security on 0.5B–8B models vs GRPO and GDPO-style variants.

## Empirical Highlights
- Qwen2.5-Coder-7B-Instruct coding Avg Pass@1 51.49 vs GRPO 47.28 / GDPO 48.88 / base 47.64. LeetCodeDataset Pass@1 24.12 vs GDPO 16.23 / GRPO 15.79.
- Qwen2.5-Coder-3B-Instruct coding Avg Pass@1 45.56 vs GRPO 43.29 / GDPO 43.41 / base 41.93.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36820`
- Code: `https://github.com/HKUST-KnowComp/CorrGRPO` (`code_status: released`).
