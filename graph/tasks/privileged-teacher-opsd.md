---
id: task:privileged-teacher-opsd
type: task
title: "Privileged-Teacher On-Policy Self-Distillation"
domain: "post-training"
summary: "On-policy self-distillation where a same-size teacher is privileged with a gold reference solution and a deterministic outcome verifier, rather than a larger frozen teacher model."
current_sota:
  - method: method:vista
    as_of: "2026-08-31"
    benchmark: "AIME24 / AIME25 / HMMT25 Avg@12 (Qwen3-1.7B/4B/8B instruct)"
    metric: "Avg@12 accuracy"
    value: "VISTA 44.0 / 64.3 / 66.9 vs OPSD 43.4 / 63.6 / 64.8 vs GRPO 37.7 / 62.7 / 64.0"
    notes: "VISTA (2608.28306) keeps the OPSD student update and adapts the privileged teacher on verified rollouts at top-k teacher-first KL positions."
methods:
  - method:vista
  - method:opd
  - method:opdvr
  - method:u-opsd
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - vista
---

# Privileged-Teacher On-Policy Self-Distillation

## Problem Definition
Train a problem-only student on its own rollouts using dense token-level targets from a same-size teacher that also sees a gold reference solution. The teacher is a privileged copy of the student, not a larger frozen model. A deterministic outcome verifier is available. Vanilla OPSD treats that privileged distribution as a fixed target at every student prefix; the teacher can then over-support reference-specific tokens or suppress valid student continuations.

## Evaluation Protocol
- **Primary Benchmarks**: AIME 2024, AIME 2025, HMMT 2025 Avg@12 on Qwen3 instruct models.
- **Evaluation Pitfalls**: Do not treat this task as single-teacher student distillation from a frontier model (`task:student-distillation` / `method:opd`) or as OPD+RLVR with an external teacher (`task:distill-reasoner-verifier` / `method:opdvr`).

## SOTA Recommendation (as of 2026-08-31)
- **Primary Method**: **VISTA** (`method:vista`, `paper:vista` `arXiv:2608.28306`) for verifier-informed student-to-teacher adaptation on privileged-teacher OPSD.
- **Not This Task**: `method:opd` remains the single-teacher student-distillation default; `method:opdvr` remains the OPD+RLVR default; `method:u-opsd` remains the unlabeled/no-GT default.
