---
id: method:pmopd
type: method
title: "PMOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "gap-aware budget / token-share balancing defaults across labeled domain teachers"
    reason: "Open-MOPD remains the multi-teacher default; PMOPD protects update subspaces, it does not rebalance token share"
    use_instead: "method:open-mopd"
  - when: "domain-feedback-scale calibration of labeled MOPD advantages"
    reason: "DN-MOPD rescales log-ratio spread; PMOPD projects interfering update directions"
    use_instead: "method:dn-mopd"
  - when: "token-level ExpertAlign routing over unlabeled multi-teacher pools"
    reason: "MOPD-Router allocates teachers per token; PMOPD is sequential block training with projection"
    use_instead: "method:mopd-router"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the single-teacher distill default"
    use_instead: "method:opd"
  - when: "multi-task OPD and teacher can be wrong on some tasks"
    reason: "PMOPD protects multi-teacher subspaces; DuoOPD gates one teacher's weights by joint outcomes"
    use_instead: "method:duoopd"
assumptions:
  - "Sequential (cycled) multi-teacher OPD on shared full-parameter students. Paper: Code/Reason/Math teachers, Qwen2.5-7B and Llama-3.1-8B, Adafactor, K=16 SVD, four cycles, probe order Code→Reason→Math."
  - "Subspace memory from cumulative block ΔW per weight matrix; project gradient then the preconditioned update. Rebuild memory each cycle."
  - "No public GitHub as of 2026-09-30. Paper Open-MOPD 63.54 is not the library 83.4% headroom-recovery bake-off."
last_reviewed: "2026-10-01"
papers:
  - paper:pmopd
recipes:
  - recipe:pmopd
claims:
  - benchmark: "Qwen2.5-7B Code/Reason/Math average vs MOPD"
    metric: "three-task average"
    value: "66.97"
    baseline: "MOPD 64.43 (+2.54); paper Open-MOPD 63.54"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.34605"
    notes: "Every task improves. Do not retarget library Open-MOPD (83.4% headroom recovery)."
  - benchmark: "Llama-3.1-8B Code/Reason/Math average vs MOPD"
    metric: "three-task average"
    value: "41.04"
    baseline: "MOPD 38.95 (+2.09)"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.34605"
    notes: "Same geometry-aware recipe transfers across families."
tags:
  - post-training
  - distillation
  - multi-teacher
  - pmopd
  - active
---

# PMOPD

## Method Overview
OPD block displacements \(\Delta W^t=W^{\mathrm{after}}-W^{\mathrm{before}}\) concentrate in low-dimensional, task-consistent subspaces. PMOPD stores the top-\(K\) SVD factors of each completed task block and, on later tasks, removes those directions from both the raw gradient and the Adafactor-preconditioned update (elementwise adaptive scaling can rotate a projected gradient back into the protected span). Memories rebuild each cycle. A pairwise conflict probe ranks tasks before the first cycle; the paper's probe picks Code→Reason→Math with four cycles. This is not Open-MOPD token-share, not DN-MOPD scale calibration, and not MOPD-Router.

## When to Use
- Labeled multi-teacher OPD on shared full weights where mixing or sequential blocks seesaw capabilities, and you can afford SVD memories per matrix.

## When NOT to Use
- Token-share / gap-aware budget → `method:open-mopd`. Domain log-ratio scale → `method:dn-mopd`. Unlabeled token routing → `method:mopd-router`. Single-teacher matching → `method:opd`. Joint-outcome multi-task gating → `method:duoopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:open-mopd` and `method:dn-mopd`. Does **not** enter `current_sota`. Does **not** replace Open-MOPD, DN-MOPD, MOPD-Router, OPD, or DuoOPD.

## Gotchas & Failure Modes
- Gradient-only projection is incomplete under Adafactor/Adam-style preconditioning. Dual projection is the method.
- Unbounded archive of old bases is not the paper; rebuild each cycle.
- Instantaneous PCGrad on mini-batch gradients is a different algorithm (no block \(\Delta W\)).
- Do not cite 66.97 vs 63.54 as beating library Open-MOPD.
