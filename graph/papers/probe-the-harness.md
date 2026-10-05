---
id: paper:probe-the-harness
type: paper
title: "Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models"
authors:
  - "Taiheng Pan"
year: 2026
month: 10
arxiv_id: "2610.02911"
url: "https://arxiv.org/abs/2610.02911"
methods:
  - method:cis-rl
  - method:carm
  - method:sao
cites:
  - paper:cis-rl
  - paper:carm
  - paper:sao
tags:
  - post-training
  - rl-alignment
  - off-policy
  - harness
  - gotcha
---

# Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models

## Abstract Summary
Stale-data RL rankings can reverse because of harness details that standard logs hide. PTH (Probe The Harness) is a four-layer checklist: the policy used in the PPO/IS ratio, the data seed each arm actually received, the identity of the replay batch (not just its age), and whether the implemented loss matches the written equation. On verl, SAN first beat TIS; after the checks, TIS matches SAN (76–79% at refresh 96). In a single-GPU trainer, TIS learns once each update draws a new batch and SAN keeps a 7–10 point margin. Claim note on CIS-RL / CARM / SAO. SAN is **not** ingested as a library method.

## Key Contributions
1. **Four harness layers** whose logged quantity can look healthy while the defining quantity is wrong.
2. **TIS vs SAN ranking reversals** in verl (ratio against recomputed learner probs; seed not reaching TIS; replay first-batch reuse for 33 updates; loss-normaliser drift).
3. **PTH checklist** for stale-data RL comparisons. Do not promote SAN over CIS-RL, CARM, or SAO.

## Empirical Highlights
- PPO-clip arm on verl peaked 73–74% GSM8K then fell below 30% with clip fraction exactly zero — the ratio was against the learner, so the arm was uncorrected GRPO.
- With the harness checked, TIS ends 76–79% at refresh 96, level with SAN+.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02911`
- Code: none found as of 2026-10-05 (`code_status: none`). SAN is documented, not a graph method.
