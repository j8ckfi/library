---
id: method:resopd
type: method
title: "ResOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "ResOPD is a sparse-payload variance fix, not a new OPD default"
    use_instead: "method:opd"
  - when: "sparse OPD keep-mask by usefulness / 1–2 tokens per trajectory"
    reason: "Sparse OPD supervision drops tokens; ResOPD residualizes the tail under a sparse payload"
    use_instead: "method:sparse-opd-supervision"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER)"
    reason: "IER-OPD ranks SNR; ResOPD is unbiased tail residualization"
    use_instead: "method:ier-opd"
assumptions:
  - Host is reverse-KL OPD with a sparse teacher payload (sampled-token or Top-k).
  - "GitHub InternLM/ResOPD announced, 404 as of 2026-10-06 (`code_status: announced`)."
last_reviewed: "2026-10-06"
papers:
  - paper:resopd
recipes:
  - recipe:resopd
claims:
  - benchmark: "sparse OPD reverse-KL under sampled-token / Top-k payloads"
    metric: "unbiased full-vocab reverse-KL gradient / variance vs sparse payload"
    value: "unbiased full-vocab reverse KL; substantial variance reduction (abstract; no numeric table)"
    baseline: "sampled-token estimator / direct Top-k OPD"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04882"
    notes: "Does not retarget OPD or sparse-opd-supervision. Do not invent 52–75% / +4.40."
tags:
  - post-training
  - distillation
  - resopd
  - active
---

# ResOPD

## Method Overview
ResOPD keeps a sparse teacher payload but recovers an unbiased full-vocabulary reverse-KL gradient by treating the unobserved mass as one tail event, backpropping that exact aggregate, and sampling only the within-tail residual.

## When to Use
- Sparse OPD (Top-k or sampled-token teacher interface) where sampled-token variance or Top-k bias is the complaint.

## When NOT to Use
- Default OPD → `method:opd`. Usefulness keep-mask → `method:sparse-opd-supervision`. IER reliability mask → `method:ier-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:sparse-opd-supervision` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: announced** InternLM/ResOPD 404 as of 2026-10-06.
- Do not invent numeric lifts absent from the abstract.
