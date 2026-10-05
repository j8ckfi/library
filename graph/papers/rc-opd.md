---
id: paper:rc-opd
type: paper
title: "Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation"
authors:
  - "Chenglei Shen"
  - "Haoyang Yao"
  - "Weijie Yu"
  - "Song Jin"
  - "Xiao Zhang"
  - "Jun Xu"
year: 2026
month: 10
arxiv_id: "2610.03515"
url: "https://arxiv.org/abs/2610.03515"
methods:
  - method:rc-opd
cites:
  - paper:vista
tags:
  - post-training
  - distillation
  - privileged-teacher
  - opsd
  - rc-opd
---

# Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation

## Abstract Summary
Reference-conditioned OPSD can explain a correct solution without fixing why the student's own reasoning fails (reasoning mismatch) and can constrain already-valid prefixes (distillation trap). RC-OPD locates the earliest substantive error, repairs it into an anchor, and tests the repair by student continuation within a budget. Successful chains get root-cause distillation on the erroneous span and anchor-guided distillation on the valid prefix. Failed budgets fall back to reference-conditioned OPSD. Active plug-in beside VISTA / OASIS / N-OPSD / Air-OPD. Code: `https://github.com/Starrylay/RC-OPD`.

## Key Contributions
1. **Diagnose / repair / continue**: Error Stage → Anchor Stage; Failure Reason & Goal vs COT-to-Anchor.
2. **Differentiated distillation** on error vs valid prefix; fallback to reference OPSD if the budget is exhausted.
3. **Table 1 Avg@4**: Qwen3-1.7B / 4B / 8B RC-OPD 44.17 / 66.11 / 66.94 vs OPSD 40.28 / 62.50 / 63.33.

## Empirical Highlights
- Qwen3-8B AIME25 76.67 vs OPSD 64.17.
- ROSD / DASH / PW-OPSD / AVSD / EOPD are paper baselines, not library retargets of VISTA.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03515`
- Code: `https://github.com/Starrylay/RC-OPD` (`code_status: released`; HTTP 200 as of 2026-10-05).
