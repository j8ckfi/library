---
id: paper:sf-mopd
type: paper
title: "Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation"
authors:
  - "Xiaofei Yin"
  - "Tong Chu"
  - "Jiyuan Fu"
  - "Jun Lan"
  - "Shuheng Zhou"
  - "Huijia Zhu"
year: 2026
month: 10
arxiv_id: "2610.02324"
url: "https://arxiv.org/abs/2610.02324"
methods:
  - method:sf-mopd
cites:
  - paper:open-mopd
tags:
  - post-training
  - distillation
  - multi-teacher
  - mopd
---

# Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation

## Abstract Summary
Multi-teacher OPD consolidates specialists into one student, but the student drifts from its initialization and general capabilities drop. Constraining the student to the init also blocks specialist learning. SF-MOPD couples a fast student (updated by each teacher) with a slow EMA of that student; the slow copy is the capability reference and the deployable checkpoint. Active plug-in beside Open-MOPD / MOPD-Router / DN-MOPD / PMOPD. No public code as of 2026-10-05.

## Key Contributions
1. **Slow/fast coupling**: EMA slow student absorbs teacher signal gradually; fast student takes the raw specialist update.
2. **Capability preservation**: general skills degrade less as domain expertise is added.
3. **Qwen3-VL All Avg**: 8B 67.7 vs MOPD 65.5 vs Open-MOPD 64.2; 4B 64.8 vs MOPD 63.6; 2B 54.2 vs MOPD 53.3.

## Empirical Highlights
- Table 1 All Avg on Qwen3-VL-8B/4B/2B Instruct. Paper Open-MOPD 64.2 is not the library 83.4% headroom-recovery bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02324`
- Code: none found as of 2026-10-05 (`code_status: none`).
