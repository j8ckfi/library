---
id: paper:evors
type: paper
title: "EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning"
authors:
  - "Weiyuan Li"
  - "Aili Chen"
  - "Xintao Wang"
  - "Yikai Zhang"
  - "Qingqing Dong"
  - "Jinghan Xu"
  - "Hongru Hou"
  - "Wenxuan Zhao"
  - "Chengkun Lang"
  - "Jun Gao"
  - "Yuanli Guo"
  - "Hongcheng Guo"
  - "Yanghua Xiao"
  - "Deqing Yang"
year: 2026
month: 9
arxiv_id: "2609.12459"
url: "https://arxiv.org/abs/2609.12459"
methods:
  - method:evors
cites:
  - paper:draco
tags:
  - post-training
  - rl-alignment
  - rubrics
  - open-ended
  - evors
---

# EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning

## Abstract Summary
Open-ended RL (writing, roleplay, office agents) cannot rely on a fixed verifier. Static and even dynamic rubrics suffer reward hacking, coverage holes, and collapsing informativeness as the policy adapts. EvoRS treats the whole reward system as an executable Reward-DAG. A designer reads on-policy rollouts, proposes bounded candidate DAG states, and accepts a candidate only if self-validation guards on success, hacking, health, and informativeness pass. Instantiated on writing and roleplay with Qwen3-4B / 8B policies and a Qwen3.5-27B GRM.

## Key Contributions
1. **Reward-DAG as evolving state**, not a frozen rubric or a one-shot dynamic rubric.
2. **On-policy candidate search** with explicit validity / coverage / informativeness guards.
3. **Best reported final quality** under three judges on WritingBench and CoSER vs static (RLAIF, RaR) and dynamic (RLER) rubric baselines; lower HR/CFR.

## Empirical Highlights
- Writing and roleplay: best final benchmark quality under GPT-5.6-Terra, DeepSeek-V4-Pro, and GLM-5.2 judges.
- Evolves every five RL steps from the same single-node continuous reward system as RLAIF.
- Not AppWorld TGC; not a CANOPY or DRACO replacement.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-14.
