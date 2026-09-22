---
id: method:ier-opd
type: method
title: "IER-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "IER-OPD is a sparse-token reliability plug-in on sampled reverse-KL OPD, not a new distill default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "usefulness keep-mask only (min/max A_t / pctltail) without gradient-estimation SNR"
    reason: "Sparse OPD Supervision is the usefulness keep-mask; IER ranks reliability and fuses with usefulness"
    use_instead: "method:sparse-opd-supervision"
  - when: "sampled-token OPD is flattening pass@k and you need entropy A_y reweight, not a token keep-mask"
    reason: "IDA-OPD shrinks entropy-contracting A_y; IER selects tokens"
    use_instead: "method:ida-opd"
  - when: "TSD calibration of teacher–student discrepancy during OPD"
    reason: "Cal-OPD is residual-advantage calibration, not sparse token selection"
    use_instead: "method:cal-opd"
assumptions:
  - "Host is sampled reverse-KL OPD. Paper: slime + TA-OPD, DAPO-Math-17k or RaR-Medicine, 4 prompts × 16 responses, lr 1e-6, prompt/response/context 2048/8192/16384."
  - "IER is approximated on a top-K candidate set from student and teacher logits plus the sampled token. High IER is reliability, not usefulness."
  - "Code: BruceSheng1202/IER-OPD."
last_reviewed: "2026-09-22"
papers:
  - paper:ier-opd
recipes:
  - recipe:ier-opd
claims:
  - benchmark: "JustRL-Qwen3-4B → Qwen3-1.7B, Bayes@32 at 0.1% token budget"
    metric: "Bayes@32"
    value: "IER 15.8 / 15.2 / 9.5 / 13.0 on AIME25 / AIME26 / HMMT25 / HMMT26"
    baseline: "full OPD 14.4 / 12.5 / 8.7 / 13.4; student 11.6 / 10.3 / 8.4 / 10.4"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24432"
    notes: "Table 2. Exceeds full OPD on three of four benches. TIP+IER-AND at 0.1% also beats full OPD on this pair."
  - benchmark: "JustRL-Nemotron-1.5B → OpenMath-Nemotron-1.5B, Bayes@32 at 0.1% IER / 1% TA-OPD+IER-AND"
    metric: "Bayes@32"
    value: "IER 0.1% AIME26 58.9 / HMMT26 34.1; TA-OPD+IER-AND 1% comparable to full OPD"
    baseline: "full OPD 59.9 / 34.7 (AIME26 / HMMT26)"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24432"
    notes: "Table 2. Sparse 0.1%–1% matches full OPD on the Nemotron pair."
  - benchmark: "HealthBench overall/hard, ClinAlign-4B → Qwen3-4B"
    metric: "overall / hard"
    value: "IER 0.1% 45.25/18.37; TIP+IER-OR 0.1% 46.08/19.61"
    baseline: "full OPD 45.77/19.77; student 38.23/8.78; Prefix 0.1% 38.30/8.68"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24432"
    notes: "Table 1. Prefix+IER-OR 44.98/19.49. Does not replace OPD."
tags:
  - post-training
  - distillation
  - on-policy
  - sparse-supervision
  - opd
  - ier-opd
  - active
---

# IER-OPD

## Method Overview
Keep sampled reverse-KL OPD. Change which tokens receive the loss. At a fixed prefix, the one-sample reverse-KL gradient decomposes into a Fisher-geometry signal and sampling noise under the variance-minimizing scalar baseline \(b^\star\). The information-efficiency ratio is

\[
\operatorname{IER}=\frac{\operatorname{Signal}}{\operatorname{Noise}}=\frac{\operatorname{Var}_p[\rho]}{\mathbb{E}_p[(\rho-b^\star)^2 L]-\operatorname{Var}_p[\rho]}.
\]

Full-vocabulary IER is expensive. Approximate it on a candidate set \(\mathcal{C}\) of top-K student logits, top-K teacher logits, and the sampled token. Rank tokens by \(\widehat{\operatorname{IER}}\), normalize the rank \(r_j\in[0,1]\), and fuse with a usefulness score \(u_j\) by soft OR \(r+u-ru\) or soft AND \(ru\). Keep at least one token per response. This is a plug-in on `method:opd`, beside `method:sparse-opd-supervision` (usefulness keep-mask) and `method:ida-opd` (entropy \(A_y\) reweight).

## When to Use
- Already running sampled-token OPD and you want a 0.1%–1% token budget that accounts for gradient-estimation reliability, not only usefulness.

## When NOT to Use
- Distill default → `method:opd`. Pass@1 → `method:cispo`. Usefulness keep-mask only → `method:sparse-opd-supervision`. Entropy \(A_y\) reweight → `method:ida-opd`. TSD calibration → `method:cal-opd`.

## Relation to Existing SOTA
- Active sparse-OPD plug-in on `task:student-distillation`. Does **not** enter `current_sota`. Does **not** supersede `method:opd`, `method:cispo`, `method:sparse-opd-supervision`, `method:ida-opd`, or `method:cal-opd`.

## Gotchas & Failure Modes
- High IER is not high usefulness. Fuse with a usefulness score; IER alone is a reliability rank.
- Entropy + IER is not a reliable combination in the paper. TIP / TA-OPD / CA-SoftOR fuse more often.
- More tokens are not always better. 1%–5% with usefulness+IER can match or beat full OPD; 10%+ can add noisy updates.
- Thinking-on Qwen3: TIP alone can fall below full OPD and even the student; TIP+IER-AND is the reported fix.
