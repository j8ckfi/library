---
id: task:student-distillation
type: task
title: "Small Local Student Distillation from Strong Teacher"
domain: "post-training"
summary: "Distilling reasoning and conversational capabilities from multi-hundred-billion parameter frontier teachers into small local student models."
current_sota:
  - method: method:opd
    as_of: "2026-08-26"
    benchmark: "GSM8k / HumanEval / MT-Bench Student Evaluation"
    metric: "task accuracy vs teacher parity"
    value: "Default SOTA for single-teacher student distillation"
    notes: "OPD 2604.13016 generalized divergence matching on student rollouts."
  - method: method:open-mopd
    as_of: "2026-08-28"
    benchmark: "Multi-Teacher Capability Integration (SmolLM3-3B Benchmark)"
    metric: "oracle ensemble headroom recovery"
    value: "83.4% headroom recovery in a single deployable student"
    notes: "Open-MOPD (2608.19098) fixes multi-teacher imbalance with token-share balancing and gap-aware dynamic budgeting."
methods:
  - method:opd
  - method:open-mopd
  - method:opdvr
  - method:vista
  - method:tropd
  - method:stable-opd
  - method:opd2
  - method:w2s-opd
  - method:nemotron-cascade-2
  - method:on-policy-distillation
  - method:ra-opd
  - method:opsa
last_reviewed: "2026-09-01"
tags:
  - post-training
  - distillation
  - on-policy
  - opd
---

# Small Local Student Distillation from Strong Teacher

## Problem Definition
Training small local students (1B–8B) from large teacher models (70B–405B) with generalized on-policy divergence matching.

## SOTA Recommendation (as of 2026-09-01)
- **Single-Teacher Distillation Default**: **OPD** (`method:opd`, `paper:opd` `arXiv:2604.13016`). Unchanged.
- **Multi-Teacher Student Distillation Default**: **Open-MOPD** (`method:open-mopd`, `paper:open-mopd` `arXiv:2608.19098`) for token-share balancing, gap-aware dynamic budget allocation, and student reward refresh across specialized teacher models.
- **Related alternative**: Use `method:vista` instead when the teacher is a privileged same-model copy that sees the gold solution (not a larger frozen teacher). OPD remains the student-distillation default.
- **Optional teacher-OPD filter**: `method:ra-opd` (`arXiv:2608.27960`) keeps trajectories with sign-agree teacher return vs outcome reward. Does not replace OPD.
- **No teacher / no labels**: `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. Does not replace OPD when a strong teacher is the goal.
