---
id: paper:gmts
type: paper
title: "GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning"
authors:
  - "Outongyi Lv"
  - "Yuanwei Zhang"
  - "Xiaoqun Zhang"
year: 2026
month: 8
arxiv_id: "2608.30632"
url: "https://arxiv.org/abs/2608.30632"
methods:
  - method:gmts
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - token-selection
  - gmts
---

# GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning

## Abstract Summary
Training RLVR on only the top-20% highest-entropy tokens helps, but entropy does not rank token importance consistently across answers whose advantages differ. GMTS scores each token by $\delta_{i,t}=|E_{i,t}\cdot\omega_{i,t}|$, where $E$ is predictive entropy and $\omega$ is the PPO-style coefficient that already includes clipping, advantage, and optional KL. Updating only the top-$\rho$ tokens by $\delta$ outperforms entropy-based token selection (ETS) as a plug-in to GRPO and DAPO, with about 1–3 percentage-point gains on math.

## Key Contributions
1. **Entropy–gradient link**: Within one answer, high entropy tracks large $\|\nabla_\theta\log\pi\|$; across answers, $\omega$ (clip/adv) breaks that ranking.
2. **GMTS score** $|E\cdot\omega|$ approximates gradient-magnitude rank without materializing true parameter gradients.
3. **Drop-in filter** for GRPO/DAPO with negligible overhead (all terms already exist in the RLVR step).

## Empirical Highlights
- Qwen2.5-Math-1.5B avg@16 over five math benches: DAPO 41.06, +ETS 40.01, +GMTS 41.56; GRPO 38.81, +ETS 39.59, +GMTS 40.89.
- Qwen2.5-Math-7B: DAPO+GMTS 50.14 vs DAPO+ETS 48.81 (+1.33); GRPO+GMTS 49.84 vs GRPO+ETS 46.43 (+3.41).
- Qwen3-8B DAPO: GMTS 56.08 vs ETS 54.23 vs DAPO 53.71; AIME2024 39.79 vs ETS 34.58.
- Code-domain 1.5B DAPO/GRPO: +1.87 / +1.90 vs ETS.

## Open Source Repository & Resources
- Code: `https://github.com/outongyiLv/GMTS` (verl-oriented frameworks)
