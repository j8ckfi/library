---
id: method:eapo
type: method
title: "EAPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "EAPO redistributes an existing group advantage; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "first-mistake process credit from an off-the-shelf teacher"
    reason: "Cliff locates a Pitfall Step; EAPO uses policy entropy × advantage sign with no teacher"
    use_instead: "method:cliff"
  - when: "gating a trained PRM behind outcome verification on all-zero groups"
    reason: "EAPO is not a PRM; VeriGate remains the process-supervision default"
    use_instead: "method:verigate"
  - when: "single-teacher distillation is the goal"
    reason: "EAPO does not match a teacher token distribution"
    use_instead: "method:opd"
assumptions:
  - "Host already samples a GRPO-family group with a verifier. Token entropy from π_old on completion tokens. Paper: Qwen3-4B/8B-Base, Qwen3-4B, Olmo-3-7B-Think-DPO, Reasoning Gym."
  - "Batch 10th/90th percentile entropy normalization; κ≥0 (κ→0 recovers uniform credit). No auxiliary model."
  - "Official code wgcyeo/EAPO released as of 2026-09-30."
last_reviewed: "2026-09-30"
papers:
  - paper:eapo
recipes:
  - recipe:eapo
claims:
  - benchmark: "Qwen3-4B-Base six math benches (AIME24/25/26, HMMT26, AMC23, MATH500-H)"
    metric: "mean Avg@32"
    value: "31.0"
    baseline: "EntropyAdv +5.6; also best vs GRPO / HAPO / 80-20 / RLRT"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.33781"
    notes: "Qwen3-8B-Base mean Avg@32 34.0 (+4.3 vs 80/20). Not a CISPO bake-off."
  - benchmark: "Qwen3-4B / Olmo-3-7B-Think-DPO reasoning backbones"
    metric: "reported overall"
    value: "72.4 / 74.3"
    baseline: "best overall vs the same exploration set; Reasoning Gym 34.89 / 43.02"
    date: "2026-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.33781"
    notes: "Project https://eapo-explore.github.io."
tags:
  - post-training
  - rlvr
  - exploration
  - credit-assignment
  - eapo
  - active
---

# EAPO

## Method Overview
GRPO shares \(\hat{A}^i\) across every token of response \(i\). Methods that always prefer high entropy therefore dump the strongest *penalties* onto uncertain tokens in failed traces. EAPO couples batch-normalized entropy \(h_{i,t}\in[0,1]\) with \(\mathrm{sign}(\hat{A}^i)\):

\[
w_{i,t}=\frac{\exp(\kappa\,\mathrm{sign}(\hat{A}^i)\,h_{i,t})}{\frac{1}{T_i}\sum_u\exp(\kappa\,\mathrm{sign}(\hat{A}^i)\,h_{i,u})},\qquad \hat{A}_t^{i,\mathrm{E}}=\hat{A}^i w_{i,t}.
\]

\(h_{i,t}\) is stop-grad clipped min-max of \(H_{i,t}\) between the batch 10th and 90th entropy percentiles. For \(\kappa>0\) this reinforces high-entropy tokens on success and low-entropy tokens on failure, and mean-normalization redistributes rather than rescales the response. Plug into the existing PPO/GRPO surrogate. CISPO stays the Pass@1 default.

## When to Use
- Dense math RLVR where exploration credit is the bottleneck and you will not add a teacher, PRM, or extra samples.

## When NOT to Use
- Pass@1 default → `method:cispo`. First-mistake teacher locator → `method:cliff`. All-zero PRM gating → `method:verigate`. Distillation → `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` beside `method:cispo` and `method:cliff`. Does **not** enter `current_sota`. Does **not** replace CISPO, Cliff, VeriGate, or OPD.

## Gotchas & Failure Modes
- Shared entropy preference (EntropyAdv / 80-20 high-entropy keep) is the wrong ablation; the sign flip is the method.
- \(\kappa\to 0\) is vanilla GRPO. Do not ship \(\kappa=0\) as EAPO.
- Entropy is from \(\pi_{\mathrm{old}}\) and detached. Differentiating through \(w_{i,t}\) is not the paper.
- All-zero groups still have \(\hat{A}^i=0\); EAPO does not salvage them (see `method:graft` / `method:verigate`).
