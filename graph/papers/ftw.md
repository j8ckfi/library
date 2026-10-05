---
id: paper:ftw
type: paper
title: "Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT"
authors:
  - "Joery A. de Vries"
  - "Neil D. Lawrence"
  - "Zhenwen Dai"
year: 2026
month: 10
arxiv_id: "2610.03361"
url: "https://arxiv.org/abs/2610.03361"
methods:
  - method:ftw
cites:
  - paper:sao
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - agentic
  - critic-free
  - ftw
---

# Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT

## Abstract Summary
GRPO needs a group of repeated rollouts from the same initial state. Stateful sandboxes and live services often cannot reconstruct that state. Follow the Winners (FTW) adapts the cross-entropy method: an ordinal filter over a replay buffer replaces the group baseline, giving polynomial concentration in the order statistic of returns. Control-as-inference recovers GRPO as risk-neutral and DPO as a pairwise special case; FTW shares DPO's bounded risk-seeking offset and controls it with selection pressure. NeurIPS 2026. Active plug-in beside SAO. No dedicated GitHub as of 2026-10-05 (verl-agent is only a cited host).

## Key Contributions
1. **CEM-style ordinal filter on replay** instead of GRPO groups or a PPO critic.
2. **Search-R1, Qwen2.5-3B-Instruct**: FTW-K1-C4 35.46 ± 0.15 vs GRPO 33.6 vs PPO 32.5.
3. Sokoban is reported as training curves vs PPO/GRPO, not a single headline number.

## Empirical Highlights
- Matches GRPO/PPO on Sokoban and published Search-R1 baselines without a value model, group rollouts, or environment duplication.
- Diagnostic bandits and Brax are in the paper; they do not retarget SAO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03361`
- Code: none found as of 2026-10-05 (`code_status: none`). verl-agent is a host citation, not an FTW repo.
