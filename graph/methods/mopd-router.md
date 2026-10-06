---
id: method:mopd-router
type: method
title: "MOPD-Router"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "gap-aware budget / token-share balancing defaults across labeled domain teachers"
    reason: "Open-MOPD remains the multi-teacher default; MOPD-Router is token-level ExpertAlign routing, not budget rebalancing"
    use_instead: "method:open-mopd"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the single-teacher distill default"
    use_instead: "method:opd"
  - when: "Direct-OPD / weak-to-strong policy-shift token selection by teacher–ref JSD"
    reason: "S2D-OPD is a Direct-OPD keep-mask, not multi-teacher routing"
    use_instead: "method:s2d-opd"
  - when: "TSD residual calibration of teacher–student discrepancy during OPD"
    reason: "Cal-OPD calibrates OPD advantage; MOPD-Router allocates among teachers"
    use_instead: "method:cal-opd"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER)"
    reason: "IER-OPD ranks reverse-KL gradient SNR inside one teacher; this method routes a pool"
    use_instead: "method:ier-opd"
  - when: "latent OPD collapse / last-layer crossfade"
    reason: "LastOPD is a latent-then-token schedule, not teacher routing"
    use_instead: "method:lastopd"
  - when: "domain-feedback-scale calibration of labeled MOPD advantages"
    reason: "MOPD-Router routes unlabeled pools per token; DN-MOPD rescales labeled-routing spread"
    use_instead: "method:dn-mopd"
  - when: "multi-teacher OPD subspace protection / task cycling"
    reason: "MOPD-Router is token routing; PMOPD protects sequential block updates"
    use_instead: "method:pmopd"
assumptions:
  - "Sampled-token MOPD host. Teachers share a pre-RL base used by ExpertAlign. Paper: three Qwen3-4B-Non-Thinking RL specialists (math/code/IF); students Qwen3-1.7B and Qwen3-4B non-thinking."
  - "ExpertAlign default: top-k=16, alignment margin δ=1e-6, cosine weighting over the positive-alignment set. Empty set skips OPD at that token."
  - "Official code TURLEing/MOPD-Router (verl + run.sh) released as of 2026-09-28."
last_reviewed: "2026-10-06"
papers:
  - paper:rethink-mopd
  - paper:mopd-router
recipes:
  - recipe:mopd-router
claims:
  - benchmark: "Unlabeled 60K mix, Qwen3-4B-Non-Thinking student, nine-benchmark overall Avg."
    metric: "macro-average of AIME24/25, HMMT Feb/Nov, HumanEval+, MBPP+, LCB-v6, IFEval, IFBench"
    value: "53.76"
    baseline: "Mean aggregation 47.88 (+5.88 / +12.3%); Standard MOPD 48.76; Open-MOPD 49.41"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30837"
    notes: "Table 1. No domain labels. Same-size. Not an Open-MOPD retarget."
  - benchmark: "Labeled MOPD mix, Qwen3-4B-Non-Thinking student, nine-benchmark overall Avg."
    metric: "macro-average of the same nine metrics"
    value: "54.58"
    baseline: "Standard MOPD 50.63 (+3.95 / +7.8%); Open-MOPD 52.37; Mean 48.16"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30837"
    notes: "Table 2. ExpertAlign ignores available domain labels. Strong-to-weak 1.7B labeled 40.19 vs Standard MOPD 37.52."
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - mopd-router
  - active
---

# MOPD-Router

## Method Overview
Sampled-token MOPD writes a per-teacher advantage \(A_t^{(i)}=\mathrm{sg}[\log\pi_{\phi_i}(y_t\mid h_t)-\log\pi_{\theta_{\mathrm{old}}}(y_t\mid h_t)]\) and a routed advantage \(A_t=\sum_i w_{i,t}A_t^{(i)}\). Domain-label hard routing sets \(w_{i,t}=\mathbb{I}[i=d(x)]\). Mean sets \(w_{i,t}=1/M\). MOPD-Router replaces both with a plug-in metric over the full pool at each token, with no domain labels and no separately trained router.

ExpertAlign uses the shared pre-RL base. On the student's top-\(k\) support \(S_t^S\), the expertise vector is \(\mathbf{e}_{i,t}=[\log p_t^i(v)-\log p_t^{\mathrm{base}}(v)]_{v\in S_t^S}\) and the teaching vector is \(\mathbf{d}_{i,t}=[\log p_t^i(v)-\log p_t^S(v)]_{v\in S_t^S}\). Keep teacher \(i\) only when \(\langle\mathbf{e}_{i,t},\mathbf{d}_{i,t}\rangle>\delta\), then cosine-weight the retained set (uniform-over-retained is a weaker ablation). Empty retained set skips OPD at that position.

Entropy (teacher confidence) and Novelty (accessible teacher–student JSD on shared top-\(k\)) are reference metrics in the same interface. Entropy is a weak router in the paper.

Open-MOPD remains gap-aware token-share balancing. OPD remains single-teacher matching.

## When to Use
- Multi-teacher OPD on unlabeled or mixed prompts where you want token-level ExpertAlign routing over the full pool instead of one domain teacher per prompt.

## When NOT to Use
- Token-share / gap-aware budget defaults → `method:open-mopd`. Single-teacher matching → `method:opd`. Direct-OPD JSD keep-mask → `method:s2d-opd`. TSD calibration → `method:cal-opd`. IER sparse reverse-KL → `method:ier-opd`. Latent collapse → `method:lastopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:open-mopd`. Does **not** enter `current_sota`. Does **not** replace `method:open-mopd`, `method:opd`, `method:s2d-opd`, `method:cal-opd`, `method:ier-opd`, or `method:lastopd`.

## Gotchas & Failure Modes
- ExpertAlign needs the teachers' shared pre-RL base at every token. Missing that base is not Mean aggregation; it is a different metric.
- Entropy routing systematically favors the low-entropy math teacher in the paper. Do not treat confidence as a drop-in ExpertAlign.
- Cosine weighting beats uniform-over-retained in all four settings. Do not ship the uniform ablation as the default.
- Gains are overall-Avg. of nine metrics, not a bake-off against Open-MOPD's 83.4% headroom-recovery claim.
