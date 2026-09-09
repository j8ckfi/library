---
id: paper:circuitlens
type: paper
title: "CircuitLens: Reasoning Circuits as Data Selection Signals for Reinforcement Learning with Verifiable Rewards"
authors:
  - "Zhuofan Chen"
  - "Ziqian Jiao"
  - "Yikai Cui"
  - "Zhixin Cai"
  - "Jun Bai"
  - "Wenge Rong"
year: 2026
month: 9
arxiv_id: "2609.07183"
url: "https://arxiv.org/abs/2609.07183"
methods:
  - method:circuitlens
cites:
  - paper:grpo
tags:
  - post-training
  - rlvr
  - interpretability
  - circuitlens
---

# CircuitLens: Reasoning Circuits as Data Selection Signals for Reinforcement Learning with Verifiable Rewards

## Abstract Summary
RLVR data selection usually scores problems as intrinsically easy/hard. CircuitLens instead computes a Circuit Reasoning Score (CRS) from 46 reasoning-sensitive attention heads found by contrastive ablation, in one frozen-base forward pass, with no reward labels or rollouts. On Qwen2.5-Math-7B the *lowest*-engagement decile beats random on GSM8K (+2.0), OlympiadBench (+1.6), and Minerva (+2.9); the highest-engagement decile is indistinguishable from the middle. Boundary conditions: domain-curated pools do not separate; 1.5B scale reverses the useful direction; lowest-reward training generalizes best. EMNLP 2026 Findings. Regime-dependent, not a static ranking of problem quality. Beside ThinkPrior (difficulty prior) and DataFlex-RL (uniform often wins).

## Key Contributions
1. **CRS** from identified reasoning heads, one forward, no rollouts.
2. **Counterintuitive low-engagement win** on medium math at 7B.
3. **Regime dependence**: scale, pool curation, and reward quartile all flip the ranking.

## Empirical Highlights
- Qwen2.5-Math-7B lowest CRS decile vs random: GSM8K +2.0, OlympiadBench +1.6, Minerva +2.9.
- Highest-engagement decile ≈ middle decile.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
