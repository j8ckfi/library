---
id: paper:cal-opd
type: paper
title: "Calibrating Teacher--Student Discrepancy for On-Policy Distillation"
authors:
  - "Qiangqiang He"
  - "Jin Li"
  - "MingCai Chen"
year: 2026
month: 9
arxiv_id: "2609.21619"
url: "https://arxiv.org/abs/2609.21619"
methods:
  - method:cal-opd
cites:
  - paper:opd
  - paper:vista
  - paper:retireopd
tags:
  - post-training
  - distillation
  - on-policy
  - opd
  - cal-opd
---

# Calibrating Teacher--Student Discrepancy for On-Policy Distillation

## Abstract Summary
On-policy distillation scores student tokens by teacher–student log-likelihood discrepancy. That discrepancy is not a pure capability gap: teacher likelihood itself moves under contextual interventions even when the evaluated trajectory is held fixed. The paper calls this Teacher Self-Deviation (TSD). Privileged OPD, which conditions the teacher on answers or solutions, amplifies those teacher-side shifts and can transfer them into the student. Cal-OPD probes the teacher with positive and negative privileged interventions, estimates a token-level TSD region, and keeps only the residual discrepancy beyond that region as the optimization advantage. On math reasoning, the retained signal is about 52–65% of the original discrepancy, yet Cal-OPD beats standard OPD and several OPD variants at two Qwen3 scales.

## Key Contributions
1. **Teacher Self-Deviation**: token-level teacher likelihood is not an equally stable reference; privileged context amplifies teacher-side variation.
2. **Calibrated residual**: positive and negative interventions estimate a TSD region; residual discrepancy outside that region is the OPD advantage.
3. **Privileged information as a probe, not a teacher**: interventions calibrate the reference rather than being distilled into the student.

## Empirical Highlights
- Qwen3-4B-Thinking-2507 → Qwen3-1.7B Avg@16: Cal-OPD 53.1 vs student 49.2 / OPD 50.8 / Privileged-OPD 49.3.
- Qwen3-30B-A3B-Thinking-2507 → Qwen3-4B Avg@16: Cal-OPD 69.0 vs student 66.6 / OPD 65.9 / Privileged-OPD 64.0.
- Retained discrepancy under evaluative interventions falls from ~65% to ~52%; Cal-OPD ends shorter than standard OPD (~9.3K vs ~11.8K) and is about 1.26× faster to train.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.21619`
- Implemented in verl (Sheng et al.). No public GitHub as of 2026-09-21 (`recipe:cal-opd` `code_status: none`).
