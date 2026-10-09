---
id: paper:expdis
type: paper
title: "Decoupling Exploration from Optimization in RLVR"
authors:
  - "Saif Punjwani"
  - "Micah Goldblum"
year: 2026
month: 10
arxiv_id: "2610.10536"
url: "https://arxiv.org/abs/2610.10536"
methods:
  - method:expdis
cites:
  - paper:dapo
  - paper:exppo
tags:
  - post-training
  - rlvr
  - exploration
  - expdis
---

# Decoupling Exploration from Optimization in RLVR

## Abstract Summary
Novelty bonuses inside RLVR often degrade a model that already has a strong prior, because the verifier only covers a thin slice of behavior. ExpDis trains explorer policies with a novelty bonus, filters trajectories for correctness and quality, and distills them into a student that never sees the novelty term. Repeat. Beats DAPO at the same wall-clock; improved pass@k scaling. Code: SaifPunjwani/Exploration-Distillation. Beside CISPO / ExPPO.

## Key Contributions
1. Do not mix novelty into the optimizer of the deployed policy.
2. Explorer(s) with a novelty bonus, then filter correct/quality traces, then distill a student without novelty.
3. Public code and HF checkpoints.

## Empirical Highlights
- Seven math benchmarks, two model families: ExpDis outperforms DAPO at the same wall-clock budget.
- Improved pass@k scaling: more diverse correct solutions than mixing novelty into the deployed reward.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.10536`
- Code: `https://github.com/SaifPunjwani/Exploration-Distillation` (`code_status: released`). Checkpoints: `https://huggingface.co/SaifPunjwani/expdis-checkpoints`.
