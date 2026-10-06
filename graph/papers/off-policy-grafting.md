---
id: paper:off-policy-grafting
type: paper
title: "Off-Policy Merging Beats On-Policy Self-Distillation for Continual Learning"
authors:
  - Chen Henry Wu
  - Thomas Zhang
  - Aditi Raghunathan
year: 2026
month: 10
arxiv_id: "2610.05872"
url: "https://arxiv.org/abs/2610.05872"
methods:
  - method:off-policy-grafting
cites:
  - paper:aclarena
tags:
  - post-training
  - continual-learning
  - off-policy-grafting
---

# Off-Policy Merging Beats On-Policy Self-Distillation for Continual Learning

## Abstract Summary
SFT on new data forgets; OPSD has been used to convert off-policy data into on-policy signal but can collapse reasoning. The paper argues SFT already extracts a useful signal; interference is the problem. Grafting changes where the update is applied (donor-checkpoint SFT) then scaled-merges back. Off-policy merging beats OPSD for continual learning in the paper. Distinct from method:graft (GRAFT all-fail GRPO salvage). Active caveat on task:agent-continual-learning; does not retarget ACLArena. No public code as of 2026-10-06.

## Key Contributions
1. **Caveat vs OPSD for CL**: on-policy conversion is not a prerequisite.
2. **Grafting**: SFT a donor checkpoint, then scaled merge, to cut interference.
3. **Slug `off-policy-grafting`**: not `method:graft` (GRAFT all-fail salvage).

## Empirical Highlights
- Abstract: off-policy merging beats OPSD for continual learning.
- No numeric table in the abstract; do not invent one.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05872`
- Code: none found as of 2026-10-06 (`code_status: none`).
