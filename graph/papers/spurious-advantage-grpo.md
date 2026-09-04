---
id: paper:spurious-advantage-grpo
type: paper
title: "Spurious Advantage Hidden in GRPO"
authors:
  - "Jiamian Wang"
  - "Samyadeep Basu"
  - "Koustava Goswami"
  - "Tong Yu"
  - "Zhiqiang Tao"
year: 2026
month: 9
arxiv_id: "2609.04063"
url: "https://arxiv.org/abs/2609.04063"
methods:
  - method:grpo
  - method:cispo
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - grpo
  - advantage
  - gotcha
---

# Spurious Advantage Hidden in GRPO

## Abstract Summary
GRPO's within-group magnitude $|\hat{A}^+|=\sqrt{n^-/n^+}$ is a function of group composition, not of whether a correct rollout was reasoned or guessed. On bounded-answer tasks (k-way multiple choice), open-answer sets with bounded sub-cases (55.95% of MATH-7.5K by answer shape), and search agents with a large action budget, lucky guesses still receive the rare-success amplification. This is a gotcha on `method:grpo` / CISPO-family group-relative advantages, not a new library default. SignBalance (sign + global scale + stop-gradient per-class balance) is the paper's estimator; it is not ingested as a training method and does not retarget current_sota.

## Key Contributions
1. **Spurious advantage**: $p_q=p_r+(1-p_r)p_g$; the GRPO magnitude acts on $n^+$ that mixes reasoning and guessing.
2. **Three regimes**: bounded-answer; bounded shapes inside nominally open math; multi-turn search with outcome-only exact match.
3. **SignBalance** (documented, not a graph method): $\hat{A}^+=c$, $\hat{A}^-=-c\cdot\mathrm{sg}[n^+/n^-]$. Parameter-free drop-in. Do not promote it over CISPO.

## Empirical Highlights
- Qwen2.5-0.5B-Instruct, MATH-7.5K, Avg-8: SignBalance 36.61 vs GRPO 34.24 vs DAPO 36.27. Lift is concentrated on bounded-answer benches (AQuA 35.43 vs GRPO 29.53; AMC 10.84 vs 6.02); open-answer MATH-500 53.60 vs GRPO 56.60 (GRPO still ahead there).
- MATH-7.5K answer-shape audit: 55.95% of parsable problems in bounded categories (int_small 24.41% with $p_g=4.76\%$, etc.).
- For G=16, a lone correct rollout gets $|\hat{A}^+|=\sqrt{15}\approx 3.87$ vs 1.0 in a balanced group; PPO clip does not bound this magnitude.

## Open Source Repository & Resources
- Code "will be released" as of the preprint; none found 2026-09-04. Use as a gotcha on GRPO/CISPO recipes, not as a new first-hop method.
