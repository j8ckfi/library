---
id: method:n-opsd
type: method
title: "N-OPSD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD with a matched VISTA-protocol bake-off"
    reason: "VISTA remains this task's first hop; N-OPSD densifies supervision with a frozen neighborhood pool"
    use_instead: "method:vista"
  - when: "privileged OPSD gains collapse at scale; verified on-policy scaffolds"
    reason: "OASIS changes the scaffold/context; N-OPSD changes the teacher pool"
    use_instead: "method:oasis"
  - when: "privileged teacher co-evolves with the student (DCE) plus shorter verified rewrites (SRCL)"
    reason: "DCE+SRCL refreshes the gold teacher each round; N-OPSD keeps frozen neighborhood experts"
    use_instead: "method:dce-srcl"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    reason: "u-OPSD remains the no-GT default"
    use_instead: "method:u-opsd"
assumptions:
  - "Privileged OPSD host (gold-conditioned teacher, clipped forward-KL on student prefixes). Offline greedy pool of frozen local parameter perturbations; online MaxPeak + quantile routing."
  - "Paper: Qwen3-1.7B/4B/8B, AIME 2024 / AIME 2025 / HMMT February 2025, Average@12, three independent runs."
  - "No public code as of 2026-10-02 (`code_status: none`). Inference uses only the distilled student."
last_reviewed: "2026-10-02"
papers:
  - paper:n-opsd
recipes:
  - recipe:n-opsd
claims:
  - benchmark: "AIME24 / AIME25 / HMMT Feb 2025 Average@12 vs OPSD, Qwen3-1.7B/4B/8B"
    metric: "Average@12 lift over OPSD"
    value: "+2.75 / +1.67 / +1.94"
    baseline: "standard privileged OPSD (one teacher θ)"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.39687"
    notes: "Three independent runs. Highest-peak expert is not always the training target. Not a VISTA bake-off (64.8→66.9) retarget."
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - n-opsd
  - active
---

# N-OPSD

## Method Overview
Standard privileged OPSD uses one teacher \(\theta\) at every student prefix. Local parameter perturbations yield complementary reference-aligned corrections at different gold positions; a pool covers more of those positions than the unperturbed teacher. N-OPSD (Neighborhood OPSD) builds that pool offline by greedy selection on filtered reference-token gains beyond the pool's current best. Online, MaxPeak picks the anchor token and a quantile rule chooses among experts whose top token matches it. The student matches the chosen expert's full next-token distribution with the usual clipped forward-KL OPSD loss.

## When to Use
- Privileged text-math OPSD where a single gold teacher under-covers reference positions, and you can afford an offline perturbation pool.

## When NOT to Use
- Privileged-OPSD first hop → `method:vista`. Scale-collapse scaffolds → `method:oasis`. Co-evolving gold teacher → `method:dce-srcl`. No labels → `method:u-opsd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside VISTA / OASIS / DCE+SRCL. Does **not** enter `current_sota`. Does **not** replace VISTA.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-02.
- Do not cite +2.75/+1.67/+1.94 vs OPSD as beating the library VISTA bake-off (64.8→66.9).
- Highest-peak expert as a naive target is not the method; routing splits direction from support.
- Pool construction uses reference trajectories; student-prefix continuations are the transfer check.
