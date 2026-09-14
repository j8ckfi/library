---
id: paper:ddo
type: paper
title: "Direct Diversity Optimization for Diverse Successful Trajectories in Preference Post-Training"
authors:
  - "Junwon Ko"
  - "Dong-Jae Lee"
  - "Minchan Kwon"
  - "Sunghyun Baek"
  - "Junmo Kim"
year: 2026
month: 9
arxiv_id: "2609.10052"
url: "https://arxiv.org/abs/2609.10052"
methods:
  - method:ddo
cites:
  - paper:dpo-paper
tags:
  - post-training
  - preference-alignment
  - diversity
  - agent
  - ddo
---

# Direct Diversity Optimization for Diverse Successful Trajectories in Preference Post-Training

## Abstract Summary
LLM agents trained from trajectory-level success/failure labels collapse onto one successful branch. Direct Diversity Optimization (DDO) is an offline preference method for successful-strategy coverage under a fixed rollout budget. Divergence-Tree Collection (DTC) builds state-aligned branch sets at shared decision states. The Reference-Relative Target-Odds Objective (RTO) trains the model to match reference-relative targets over successful alternatives. Strongest task success and successful-strategy coverage among compared methods on BabyAI, BabaIsAI, and WebShop.

## Key Contributions
1. **DTC**: state-aligned successful branch sets, not unpaired preference rows.
2. **RTO**: reference-relative target odds over successful alternatives.
3. **Coverage + recovery**: highest recovery after local action replacement vs successful-only imitation and decoding-time diversification.

## Empirical Highlights
- Best task success and successful-strategy coverage on BabyAI, BabaIsAI, and WebShop among the paper's post-training methods (DPO, DivFreq, DivProb, TieDPO variants).
- Code and nine DDO adapters: `https://github.com/koguma00/direct_diverse_optimization`.

## Open Source Repository & Resources
- Official: `https://github.com/koguma00/direct_diverse_optimization`
- Train: `python train.py --config configs/training.yaml` (`method: ddo`).
