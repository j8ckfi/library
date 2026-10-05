---
id: paper:opd-gains-collapse
type: paper
title: "Gains and Collapse in On-Policy Distillation: A Reinforcement Learning Perspective"
authors:
  - "Han Cui"
  - "Jianhao Yan"
  - "Yun Luo"
  - "Hongbo Zhang"
  - "Zhizhang Fu"
  - "Yue Zhang"
year: 2026
month: 10
arxiv_id: "2610.03185"
url: "https://arxiv.org/abs/2610.03185"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - collapse
  - gotcha
---

# Gains and Collapse in On-Policy Distillation: A Reinforcement Learning Perspective

## Abstract Summary
OPD can raise Pass@1 or collapse into long repetitive output. The paper treats the teacher as an implicit reward model over student rollouts: it reweights behaviors the student already samples, and does not expand the solvable set. When that implicit RM is misaligned, the student reward-hacks into overlong repetition even though the teacher rarely emits that text. Masking unhealthy responses and SFT initialization each mitigate collapse. Claim note on `method:opd`. Masking is documented, not ingested as a library method. Code: `https://github.com/HancCui/opd_hacking`.

## Key Contributions
1. **Teacher as implicit RM**: OPD amplifies student behaviors the teacher prefers, including ones the teacher does not generate.
2. **No capability expansion**: Pass@1 gains shrink with Pass@K; solved problems after OPD were already in the init student's sample set.
3. **Collapse mitigation (documented, not a graph method)**: masking unhealthy responses; Table 3 4B→Base avg 10.16 → 13.24 with mask.

## Empirical Highlights
- 8B→Base avg 10.41 in the same table; +mask is a sibling row.
- Do not retarget OPD, OPSA, or VISTA. Masking is a gotcha fix, not a new first hop.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03185`
- Project: `https://hanccui.github.io/opd_hacking`
- Code: `https://github.com/HancCui/opd_hacking` (`code_status: released`; HTTP 200 as of 2026-10-05).
