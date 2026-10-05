---
id: paper:on-policy-or-off-policy
type: paper
title: "On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics"
authors:
  - "Julianna Piskorz"
  - "Antonin Berthon"
  - "Mihaela van der Schaar"
year: 2026
month: 9
arxiv_id: "2609.35259"
url: "https://arxiv.org/abs/2609.35259"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - on-policy
  - kl
  - gotcha
---

# On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics

## Abstract Summary
SFT vs RL comparisons confound rollout policy with the objective. This study holds the distillation pipeline fixed and varies rollout policy, token-level KL direction, and learning rate on Llama 3 and Qwen2.5. Rollout policy is not the central driver of in-distribution accuracy, forgetting, or update sparsity. KL direction shapes task performance and coverage; learning rate governs forgetting and sparsity. Forward KL is robust to rollout policy; reverse KL is sensitive and prefers student-generated rollouts. On-policy data still helps harder Countdown variants, but that edge does not reliably survive later RLVR. Claim note on `method:opd` / `task:student-distillation`. No dedicated code.

## Key Contributions
1. **Controlled strong-to-weak distillation**: rollout policy, KL direction, and LR are unconfounded.
2. **Forward KL vs reverse KL**: forward is rollout-robust; reverse favors on-policy student rollouts.
3. **On-policy is not inherently preferable** for ID accuracy / forgetting / sparsity.

## Empirical Highlights
- HF Daily top paper 2026-10-02. No library retarget of OPD.
- No dedicated GitHub as of 2026-10-05.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.35259`
- Code: none found as of 2026-10-05 (`code_status: none`).
