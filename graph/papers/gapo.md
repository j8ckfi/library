---
id: paper:gapo
type: paper
title: "Group Adaptive Clipping Policy Optimization"
authors:
  - "Sheng Jia"
  - "Xiao Wang"
  - "Shiva Prasad Kasiviswanathan"
  - "Rein Houthooft"
year: 2026
month: 9
arxiv_id: "2609.00444"
url: "https://arxiv.org/abs/2609.00444"
methods:
  - method:gapo
cites:
  - paper:grpo
  - paper:gspo
  - paper:dapo
  - paper:minimax-m1
tags:
  - post-training
  - rlvr
  - clipping
  - gapo
---

# Group Adaptive Clipping Policy Optimization

## Abstract Summary
Group-relative RLVR (GRPO / GSPO / DAPO) applies a fixed importance-sampling clip boundary to every rollout. Rare correct traces on hard prompts and abundant correct traces on easy prompts are therefore clipped at comparable rates, even though the scarce traces carry stronger exploration signal. GAPO is a plug-in that adapts the upper clip width to the rollout advantage, motivated by a reverse-KL trust-region argument: larger learning signal should get proportionally more update headroom. The PPO/GSPO surrogate is unchanged; only the clip threshold moves. No reward shaping. Across Qwen and Llama, GAPO improves Pass@1 and Pass@k versus fixed clipping and advantage-shaping baselines on math and coding when base pass rates are low. Accepted to EMNLP 2026 Main.

## Key Contributions
1. **Fixed-clip failure**: IS ratios grow faster on low-$c$ (scarce-correct) groups, so a uniform $[1-\epsilon,1+\epsilon]$ hits hard-problem rollouts first.
2. **Adaptive upper clip**: $\epsilon_{\mathrm{hi}}(c)=\epsilon_{\mathrm{lo}}+(\epsilon_{\mathrm{hi}}^{\max}-\epsilon_{\mathrm{lo}})\cdot(k-c)/(k-1)$ for a correct rollout in a group of size $k$ with $c$ correct; incorrect rollouts keep $\epsilon_{\mathrm{lo}}$.
3. **Drop-in on GRPO/GSPO**: token-IS and sequence-IS (GSPO geometric-mean ratio) both supported; host loss unchanged.
4. **No reward shaping**: advantage-shaping baselines (F-GRPO, DrGRPO) are comparators, not the mechanism.

## Empirical Highlights
- DeepSeek-R1-Distill-Qwen-1.5B / DeepScaleR, Pass@1/Pass@16: GAPO AIME24 44.0/76.7 vs GSPO 41.3/73.3 vs F-GSPO 40.2/73.3; AIME25 30.8/56.7 vs GSPO 29.4/50.0.
- Qwen2.5-1.5B-Math in-domain Pass@1 avg: GAPO-token-IS 37.6 vs GRPO 36.7 vs DrGRPO 33.8; GAPO sequence-IS 37.9 vs GSPO 37.7.
- DeepCoder-1.5B (token-IS $\epsilon_{\mathrm{hi}}^{\max}\in[0.2,0.28]$): LCB-v5 Pass@1 24.8 vs reproduced DeepCoder 22.4 vs base 16.9; HumanEval+ 71.7 vs 68.2 vs 58.3.

## Open Source Repository & Resources
- Code: `https://github.com/Sheng-J/GAPO` (verl plug-in + patch pinned to verl `9bda8b9a`). Full Amazon-internal trainer still under release review as of 2026-09-07.
