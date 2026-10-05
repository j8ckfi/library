---
id: paper:air-opd
type: paper
title: "Learning from Evolving Errors: Adaptive Iterative Repair for On-Policy Distillation"
authors:
  - "Rui Li"
  - "Liyang He"
  - "Zheng Zhang"
  - "Zhenya Huang"
  - "Linbo Zhu"
  - "Qi Liu"
year: 2026
month: 10
arxiv_id: "2610.02700"
url: "https://arxiv.org/abs/2610.02700"
methods:
  - method:air-opd
cites:
  - paper:vista
tags:
  - post-training
  - distillation
  - privileged-teacher
  - opsd
  - air-opd
---

# Learning from Evolving Errors: Adaptive Iterative Repair for On-Policy Distillation

## Abstract Summary
Reference-conditioned OPSD tells the teacher the destination, not how to leave the student's current error. Air-OPD (adaptive iterative repair) synthesizes error-specific repair guidance, retries on-policy, and if the retry fails, writes new guidance for the new error. A fixed teacher sees that guidance as privileged context and supervises an error-aligned span of the latest failed response. Outcome-aware stage weighting favors early repair stages and credits stages whose retry passes verification. Active plug-in beside VISTA / OASIS / N-OPSD. No public code as of 2026-10-05.

## Key Contributions
1. **Error-to-repair privileged context** instead of a static gold solution as the only teacher hint.
2. **Error-aligned region + outcome-aware stage weights** across multi-round retries.
3. **Qwen3-4B Math Avg (Avg@12 of AIME24/AIME25/HMMT25)** External-G 66.7 / Self-G 65.8 vs OPSD 63.1 / GRPO 62.3 / base 61.2.

## Empirical Highlights
- Qwen3-8B Math Avg External-G 67.4 / Self-G 66.9 vs OPSD 64.7 / GRPO 64.0 / base 61.8.
- Self-G already +2.8 / +2.1 Math Avg vs OPSD on 4B / 8B without an external model.
- OOD (MMLU-Pro / GPQA) stays near the base model (4B OOD Avg 56.8 External-G vs base 57.2).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02700`
- Code: none found as of 2026-10-05 (`code_status: none`). TRL is mentioned only as a host, not a release.
