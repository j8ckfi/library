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
  - method:opd-one-example
  - method:opd-hard-cot-selection
  - method:ida-opd
  - method:opsa
  - method:rise
  - method:pta
  - method:tgopd
last_reviewed: "2026-09-08"
tags:
  - post-training
  - distillation
  - on-policy
  - opd
---

# Small Local Student Distillation from Strong Teacher

## Problem Definition
Training small local students (1B–8B) from large teacher models (70B–405B) with generalized on-policy divergence matching.

## SOTA Recommendation (as of 2026-09-08)
- **Single-Teacher Distillation Default**: **OPD** (`method:opd`, `paper:opd` `arXiv:2604.13016`). Unchanged.
- **Multi-Teacher Student Distillation Default**: **Open-MOPD** (`method:open-mopd`, `paper:open-mopd` `arXiv:2608.19098`) for token-share balancing, gap-aware dynamic budget allocation, and student reward refresh across specialized teacher models.
- **Related alternative**: Use `method:vista` instead when the teacher is a privileged same-model copy that sees the gold solution (not a larger frozen teacher). OPD remains the student-distillation default.
- **Optional teacher-OPD filter**: `method:ra-opd` (`arXiv:2608.27960`) keeps trajectories with sign-agree teacher return vs outcome reward. Does not replace OPD.
- **Optional sampled-token entropy plug-in**: `method:ida-opd` (`arXiv:2608.29846`) keeps entropy-expanding $A_y$ and shrinks $\mathcal{I}_H<0$ by $|q-p|/(q+p)$. Does not replace OPD or CISPO.
- **Data-efficiency note**: `method:opd-one-example` (`arXiv:2609.04172`) — one query recovers most full-data OPD; ~16 diverse queries ≈ full-data / MOPD. Does not replace OPD.
- **Data-selection sibling**: `method:opd-hard-cot-selection` (`arXiv:2609.05198`) — hard/long-CoT examples drive OPD gains (not high token entropy); 8 hard can match 17K. Does not replace OPD or OPD-II.
- **Related self-extrapolating teacher**: `method:rise` (`arXiv:2609.05295`) synthesizes an OPD teacher from the student's RLVR trajectory. No external teacher. Does not replace OPD, CISPO, or OPSA.
- **Tool-using OPKD**: `method:pta` (`arXiv:2609.04773`, EMNLP 2026 Main) — student-induced but teacher-committed rollouts; tool calls execute only after the teacher verifies the turn. Pre-RL distill for Search-R1 / DeepEyes. Does not replace OPD for text-only distillation.
- **Optional prompt-level teacher gate**: `method:tgopd` (`arXiv:2609.02998`) admits dense OPD only after verifier-scored teacher probes pass; else GRPO. Sibling of RA-OPD / IDA-OPD / VISTA. Does not replace OPD, CISPO, OPSA, or Open-MOPD.
- **No teacher / no labels**: `method:opsa` on `task:teacher-free-on-policy-self-adaptation`. Does not replace OPD when a strong teacher is the goal.
