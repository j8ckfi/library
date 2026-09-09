---
id: method:kbbq
type: method
title: "KBBQ"
category: "quantization"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "native FP4 forward/backward hardware training from scratch"
    reason: "KBBQ is a W4A4 noise-law / PTQ-style transform, not Quartet-II NVFP4 training"
    use_instead: "method:quartet-ii"
  - when: "MXFP4 training on MI355X"
    reason: "Different shelf"
    use_instead: "method:mxfp4-mi355x"
  - when: "genuine 1-bit PTQ"
    reason: "That is AF1"
    use_instead: "method:af1"
assumptions:
  - "W4A4 inference / PTQ-style blockwise transforms on existing checkpoints. Not native FP4 training."
last_reviewed: "2026-09-09"
papers:
  - paper:kbbq
recipes:
  - recipe:kbbq
claims:
  - benchmark: "W4A4, four base models × two FP4 formats"
    metric: "quality vs prior flatten SOTA"
    value: "outperforms prior SOTA with no extra deploy-time compute"
    baseline: "prior spectrum-flattening SOTA (κ*)"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08135"
    notes: "Does not retarget Quartet-II / MXFP4 hardware training."
tags:
  - quantization
  - fp4
  - kbbq
  - active
---

# KBBQ

## Method Overview
KBBQ applies a closed-form FP4 noise law (participation factor κ) and brakes blockwise transforms short of the κ* flatten ceiling. Active W4A4 niche. Does not replace Quartet-II or MXFP4 as native FP4 training.

## When to Use
- W4A4 PTQ/inference where spectrum flattening is the baseline.

## When NOT to Use
- Native FP4 train → `method:quartet-ii` / `method:mxfp4-mi355x`. 1-bit PTQ → `method:af1`.

## Relation to Existing SOTA
- Active on `task:fp4-hardware-training` as a related W4A4 note only. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- No official GitHub. Do not cite as a training-from-scratch FP4 kernel.
