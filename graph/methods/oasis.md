---
id: method:oasis
type: method
title: "OASIS"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD with gold solutions is still the first hop"
    reason: "VISTA remains privileged-OPSD SOTA; OASIS is a scale-collapse scaffold fix, not a teacher-update recipe"
    use_instead: "method:vista"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    reason: "u-OPSD remains the no-GT default; OASIS needs final-answer labels"
    use_instead: "method:u-opsd"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the student-distillation default"
    use_instead: "method:opd"
  - when: "privileged teacher co-evolves with the student (DCE) plus shorter verified rewrites (SRCL)"
    reason: "DCE+SRCL co-evolves the gold teacher; OASIS keeps the OPSD objective and changes the scaffold/context"
    use_instead: "method:dce-srcl"
assumptions:
  - "Answer labels / a deterministic verifier. Sample K on-policy rollouts; supervise the shortest verified scaffold. Teacher context is another same-problem rollout, not a written gold solution."
  - "Paper: Qwen3-1.7B/4B/8B, AIME 2024/2025 and HMMT 2025, Avg@12."
  - "No public GitHub as of 2026-10-01."
last_reviewed: "2026-10-01"
papers:
  - paper:oasis
recipes:
  - recipe:oasis
claims:
  - benchmark: "AIME24 / AIME25 / HMMT25 Avg@12 vs base, Qwen3-1.7B/4B/8B"
    metric: "mean lift over base"
    value: "+3.2 to +3.8"
    baseline: "OPSD vs base +3.05 / +1.98 / +0.14 (collapses with scale)"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37915"
    notes: "Verified on-policy scaffolds. Not a VISTA bake-off retarget."
  - benchmark: "Same suite, Qwen3-8B vs OPSD"
    metric: "mean Avg@12 lift"
    value: "+3.05"
    baseline: "OPSD (gold-context unverified scaffolds)"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.37915"
    notes: "OASIS vs OPSD +0.59 / +1.86 / +3.05 at 1.7B / 4B / 8B. Extra rollout cost vs vanilla OPSD."
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - oasis
  - active
---

# OASIS

## Method Overview
OASIS (On-policy Alignment via Scaffold-Isolated Supervision) keeps the OPSD loss. Sample \(K\) student rollouts, verify final answers, and apply the loss along the shortest verified trajectory. Problems with no verified rollout contribute no signal. Teacher context is a distinct same-problem rollout (usually an unverified attempt, else another verified one), not a written gold solution. Scaffold correctness, not gold-context correctness, is the scale-stable ingredient.

## When to Use
- Privileged OPSD whose gains collapse as the student scales, when you have answer labels but not necessarily gold traces.

## When NOT to Use
- Privileged-OPSD first hop → `method:vista`. No labels → `method:u-opsd`. Frozen larger teacher → `method:opd`. Co-evolving gold teacher → `method:dce-srcl`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside `method:vista` and `method:u-opsd`. Does **not** enter `current_sota`. Does **not** replace VISTA, u-OPSD, or OPD.

## Gotchas & Failure Modes
- No public code as of 2026-10-01.
- Needs a verified scaffold. All-fail problems are skipped.
- Rollout generation cost is higher than vanilla OPSD (K samples per problem).
- Do not cite the 8B +3.05 vs OPSD as beating the library VISTA bake-off (64.8→66.9).
