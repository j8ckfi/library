---
id: method:carm
type: method
title: "CARM"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "CISPO remains Pass@1; CARM is a sequence-level off-policy mask"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR train–infer engine mismatch (calibrated IS on log-odds displacement)"
    reason: "CIS-RL truncates per-token mismatch ratios; CARM accepts or rejects the whole response"
    use_instead: "method:cis-rl"
  - when: "choosing the frontier post-train engine"
    reason: "Miles is the stack; CARM is a mask inside a GRPO/PPO host"
    use_instead: "method:miles"
  - when: "MoE/VL RLVR loss rather than off-policy masking"
    reason: "SAPO remains the MoE/VL optimizer"
    use_instead: "method:sapo"
assumptions:
  - "Rollout policy and train policy can differ (minibatch staleness, actor-learner delay, vLLM/SGLang vs FSDP/Megatron). Token ratios r_t = pi_theta / pi_rollout on sampled tokens."
  - "Paper: math mean@16 on AIME 2024/2025/2026 + BeyondAIME; four code benches pass@1. GeoMean / DeepSeek-V3.2 signed-log sequence mask is the cancellation baseline."
  - "No public code as of 2026-10-02 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:carm
  - paper:probe-the-harness
recipes:
  - recipe:carm
claims:
  - benchmark: "Math mean@16 averaged over AIME 2024/2025/2026 and BeyondAIME"
    metric: "mean@16 lift vs geometric-mean masking"
    value: "up to +3.13 pp"
    baseline: "GeoMean (length-normalized geometric mean of token ratios / signed log-ratio mean)"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02039"
    notes: "Keeps the token-level PPO/GRPO surrogate. Not a CISPO / CIS-RL / Miles retarget."
  - benchmark: "Four code benchmarks, average pass@1"
    metric: "pass@1 lift vs strongest evaluated baseline"
    value: "+2.88 pp"
    baseline: "strongest sequence- or token-level mask in the paper"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02039"
    notes: "Filtering rate is not monotone in accuracy; match rates when comparing masks."
tags:
  - post-training
  - rl-alignment
  - off-policy
  - carm
  - masking
  - active
---

# CARM

## Method Overview
Sequence-level off-policy masks that average *signed* token log-ratios (GeoMean / DeepSeek-V3.2) let \(r=10\) and \(r=0.1\) cancel to a geometric mean of 1. CARM averages **absolute** log-ratios before the threshold:

\[
d_{\mathrm{CARM}}(y)=\frac{1}{T}\sum_{t=1}^{T}|\log r_t|,\qquad s_{\mathrm{CARM}}(y)=\exp(d_{\mathrm{CARM}}(y)).
\]

Keep the response when \(s_{\mathrm{CARM}}\) is below the band. Accepted responses satisfy a joint bound on the fraction of ratios outside a (possibly asymmetric) band and their mean log-distance beyond it. Token PPO/GRPO clipping is unchanged; CARM only decides whether the response enters the batch.

## When to Use
- Production RLVR where rollout engine ≠ train engine, or stale mini-batches, and GeoMean is accepting bidirectional drift.

## When NOT to Use
- Pass@1 kernel → `method:cispo`. Per-token train–infer IS cap → `method:cis-rl`. Engine choice → `method:miles`. MoE/VL loss → `method:sapo`.

## Relation to Existing SOTA
- Active plug-in on `task:frontier-rl-posttrain-stack` and `task:math-code-rl-dense` / `task:math-code-rl-moe` beside CIS-RL / CISPO / Miles. Does **not** enter those `current_sota` lists.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-02. Reimplement the absolute-log mean; do not invent a CISPO replacement.
- Comparable filtering rates can yield different accuracies. More masking is not uniformly better.
- Complements CIS-RL (token mismatch cap) rather than replacing it.
