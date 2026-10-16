---
id: paper:waypoint-opd
type: paper
title: 'Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation'
authors:
- Bingxi Hou
- Guochao Jiang
- Guofeng Quan
- Weiqing Li
- Wenfeng Feng
- Guohua Liu
- Yuewei Zhang
year: 2026
month: 10
arxiv_id: '2610.21601'
url: https://arxiv.org/abs/2610.21601
methods:
- method:waypoint-opd
cites:
- paper:opd
- paper:rpd-opd
tags:
- distillation
- opd
- policy-shift
---

# Waypoint-OPD

## Abstract Summary
Endpoint RL policy-shift distillation cannot tell whether early and late teacher updates reinforce or cancel. Waypoint-OPD scores an intermediate checkpoint from the same RL run and gates the endpoint log-probability shift by directional agreement at student prefixes.

## Key Contributions
1. Intermediate-checkpoint directional gate on endpoint policy-shift OPD.
2. One extra frozen-teacher scoring pass versus endpoint-only transfer.
3. Qwen3-4B RL teachers into Qwen3-8B / 14B / 30B-A3B math and code students.

## Empirical Highlights
- Highest domain-average among compared student methods in all six settings.
- Math vs Direct-OPD +2.18 / +1.59 / +1.89; code +2.66 / +1.52 / +1.19.
- Qwen3-8B math Avg 56.14 vs no-gate 53.50.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.21601`
- Code: `https://github.com/hhhbxloveai/WaypointOPD` (`code_status: released`).

