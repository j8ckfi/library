---
id: method:dn-mopd
type: method
title: "DN-MOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "gap-aware budget / token-share balancing defaults across labeled domain teachers"
    reason: "Open-MOPD remains the multi-teacher default; DN-MOPD rescales labeled-routing advantages by domain log-ratio spread, not token-share budget"
    use_instead: "method:open-mopd"
  - when: "token-level ExpertAlign routing over unlabeled multi-teacher pools (no domain labels, no separate router train)"
    reason: "DN-MOPD keeps label routing; MOPD-Router allocates among teachers per token"
    use_instead: "method:mopd-router"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the single-teacher distill default"
    use_instead: "method:opd"
  - when: "multi-teacher OPD subspace protection / task cycling (not feedback-scale)"
    reason: "PMOPD projects gradients and Adafactor updates out of protected task subspaces"
    use_instead: "method:pmopd"
assumptions:
  - "Labeled domain routing (math/code/IF). Host is sampled-token clipped OPD / Uni-OPD. Paper: independently trained Qwen3.5 specialists at 9B/4B/2B."
  - "Per-batch population std of teacher–rollout log-ratios; clip multipliers to [0.25, 4]. w_d=1 if a domain has <2 observations or a std is zero."
  - "Official code LiXin97/DN-MOPD released as of 2026-09-30."
last_reviewed: "2026-10-06"
papers:
  - paper:rethink-mopd
  - paper:dn-mopd
recipes:
  - recipe:dn-mopd
claims:
  - benchmark: "Qwen3.5 9B/4B/2B six-task Total vs label-routed MOPD"
    metric: "six-task average"
    value: "59.6 / 52.5 / 29.0"
    baseline: "Label MOPD 58.4 / 50.3 / 26.6; 16K +1.17–2.36, 8K +2.47–3.08"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.35347"
    notes: "Three seeds +1.12 / +1.97 / +2.34. Mathematics recovery is the largest domain lift. Not an Open-MOPD retarget."
  - benchmark: "First-batch Qwen3.5 4B labeled MOPD gradient share"
    metric: "IF share of combined gradient"
    value: "94%"
    baseline: "IF log-ratio std 2.3–4.4× pooled; math ~0.5× pooled"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.35347"
    notes: "Equal prompt counts. Assignment without scale calibration is the failure mode."
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - dn-mopd
  - active
---

# DN-MOPD

## Method Overview
Label-routed MOPD sets \(A_t=\log p_{T_d}(y_t\mid h_t)-\log\pi_u(y_t\mid h_t)\) from the specialist of prompt domain \(d\). Independently trained RL specialists do not emit those log-ratios on a common scale. DN-MOPD keeps the assignment and rescales advantages from batch spread. For token log-ratios \(r_{i,t}=\ell^T_{i,t}-\ell^{\mathrm{roll}}_{i,t}\), let \(\sigma_d\) be the population std on domain \(d\) and \(\sigma_{\mathrm{all}}\) the pooled std. Then

\[
w_d=\operatorname{clip}\!\left(\frac{\sigma_{\mathrm{all}}}{\sigma_d},\,0.25,\,4\right),\qquad \widetilde{A}_t=\operatorname{stopgrad}(w_d A_t).
\]

The actor uses the usual clipped OPD surrogate on \(\widetilde{A}_t\). Multipliers are positive, so signs (encourage vs discourage) stay. MOPD is \(w_d=1\). This is not token-share / gap-aware budget (`method:open-mopd`) and not per-token ExpertAlign (`method:mopd-router`).

## When to Use
- Labeled multi-teacher OPD where IF (or another concise domain) log-ratios swamp math/code on the shared student.

## When NOT to Use
- Token-share / gap-aware budget defaults → `method:open-mopd`. Unlabeled pool routing → `method:mopd-router`. Single-teacher matching → `method:opd`. Subspace protection / cycling → `method:pmopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:open-mopd` and `method:mopd-router`. Does **not** enter `current_sota`. Does **not** replace Open-MOPD, OPD, MOPD-Router, or PMOPD.

## Gotchas & Failure Modes
- Needs domain labels. Unlabeled mixtures are MOPD-Router's job.
- \(w_d=1\) if a domain has fewer than two tokens or a std is zero; small batches can skip calibration.
- Clip \([0.25,4]\) can leave residual imbalance. Fixed weights near measured multipliers matched 9B/4B in the paper; do not treat the clip bounds as a learned router.
- Gains are six-task Total vs label MOPD, not Open-MOPD's 83.4% headroom-recovery claim.
