---
id: paper:diffgate
type: paper
title: "DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation"
authors:
  - Karn Tiwari
  - Varnith Chordia
  - Prathosh A P
year: 2026
month: 10
arxiv_id: "2610.04596"
url: "https://arxiv.org/abs/2610.04596"
methods:
  - method:diffgate
cites:
  - paper:opd
  - paper:opd-then-rlvr
  - paper:grpo
tags:
  - post-training
  - distillation
  - opd
  - diffgate
---

# DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

## Abstract Summary
OPD is dense but weakly aligned with rollout correctness; GRPO is outcome-aligned but sparse and silent on all-fail groups. DiffGate applies teacher supervision only to failed trajectories, scaled by group difficulty, and smoothly bounded. Verifier chooses which trajectories get a teacher; the teacher supplies token-level directions there. Qwen3-0.6B/1.7B: code avg@8 +1.7/+1.8 and pass@8 +1.6/+5.7 vs matched GRPO. Math avg@8 within 0.5 of GRPO; pass@8 +1.1/+3.9. pass@8 improves in all four model–domain settings. No dedicated repo (verl cited). Beside OPD-then-RLVR.

## Key Contributions
1. **Failure-only teacher**: teacher signal on failed trajectories, scaled by group difficulty.
2. **Bounded mix** so extreme teacher–student gaps do not dominate.
3. **Coverage lift**: pass@8 up in all four Qwen3-0.6B/1.7B × code/math settings.

## Empirical Highlights
- Code avg@8 +1.7 / +1.8 and pass@8 +1.6 / +5.7 vs matched GRPO on 0.6B / 1.7B.
- Math avg@8 within 0.5 of GRPO; pass@8 +1.1 / +3.9.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04596`
- Code: none found as of 2026-10-06 (`code_status: none`). Paper cites verl; no dedicated GitHub.
