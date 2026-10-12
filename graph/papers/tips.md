---
id: paper:tips
type: paper
title: Inducing Process Supervision from Outcome-Only Reinforcement Learning
authors:
- Shengda Fan
- Xin Cong
- Zhong Zhang
- Haotian Chen
- Yankai Lin
year: 2026
month: 9
arxiv_id: '2609.36641'
url: https://arxiv.org/abs/2609.36641
methods:
- method:tips
cites:
- paper:verigate
- paper:srd
tags:
- post-training
- prm
- rlvr
- tips
---

# Inducing Process Supervision from Outcome-Only Reinforcement Learning

## Abstract Summary
PRMs are expensive to label. TIPS is outcome-only RL for a generative PRM: the model writes CoT, step labels, and an outcome; the reward is whether the predicted outcome matches ground truth; group-relative advantage updates the whole response. Accurate step checks help the outcome judgment, so outcome RL induces process supervision. 85.2 ProcessBench F1 from 3.2K outcome-labeled trajectories.

## Key Contributions
1. Outcome-only RL that induces step labels in a generative PRM.
2. No human spans and no Monte Carlo step estimation.
3. 85.2 ProcessBench F1 at 4B with 3.2K trajectories; beats strong prompt judges, trails o1-mini.

## Empirical Highlights
- See `method:tips` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36641`
- Code: `https://github.com/RUCBM/TIPS` (`code_status: released`).
