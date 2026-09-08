---
id: method:sparse-opd-supervision
type: method
title: "Sparse OPD Supervision"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "This is a keep-mask on OPD tokens, not a new distill default"
    use_instead: "method:opd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "sampled-token OPD is flattening pass@k and you need entropy-aware reweight, not a 1-token mask"
    reason: "IDA-OPD shrinks entropy-contracting A_y; this card drops tokens"
    use_instead: "method:ida-opd"
  - when: "selecting hard/long-CoT prompts rather than tokens inside a trajectory"
    reason: "That is OPD hard-CoT selection"
    use_instead: "method:opd-hard-cot-selection"
  - when: "shrinking the query set, not the token mask"
    reason: "OPD-II is one/16 diverse queries"
    use_instead: "method:opd-one-example"
assumptions:
  - "Host is reverse-KL / sampled-token OPD with per-token A_t = log π_T(y_t|h_t) − log π_θ(y_t|h_t). Paper: veRL 0.8.0, DAPO-Math-17K, n=1 OPD rollout, max response 8192, lr 1e-6, clip 0.2, Qwen3 no-think."
  - "Table 2 names: mintok = highest-reward token; maxtok = lowest-reward token. Figure 1 caption swaps those adjectives — follow Table 2."
  - "No official code as of 2026-09-08."
last_reviewed: "2026-09-08"
papers:
  - paper:sparse-opd-supervision
recipes:
  - recipe:sparse-opd-supervision
claims:
  - benchmark: "Family 8 Qwen3-1.7B ← Qwen3-30B-A3B-Instruct-2507, AIME24/AIME25/HMMT-Feb avg@8 mean"
    metric: "avg@8 mean"
    value: "pctltail 0.05% 30.1 / minmaxtok 28.9 / maxtok 29.0"
    baseline: "plain OPD 27.5 / student 8.7 / teacher 59.0 / rand1tok 15.6"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04565"
    notes: "Table 3. keep_frac 0.138% / 0.0409% / 0.0176% vs plain 100%."
  - benchmark: "Family 9 Qwen3-8B ← Qwen3-4B-Instruct-2507, AIME24/AIME25/HMMT-Feb avg@8 mean"
    metric: "avg@8 mean"
    value: "minmaxtok 49.3 / maxtok 48.1"
    baseline: "plain OPD 47.5 / teacher 46.8 / student 19.3"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04565"
    notes: "Table 5. maxtok revKL 1.116 vs plain 0.184 — better avg@8 with larger reverse KL."
  - benchmark: "Family 4 Qwen3-4B-Base ← Qwen3-4B-GRPO-5ep, AIME24/AIME25/HMMT-Feb avg@8 mean"
    metric: "avg@8 mean"
    value: 16.4
    baseline: "plain OPD 16.1 / teacher 15.8 / student 6.1 (maxtok)"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04565"
    notes: "Table 4. Same-scale. mintok 14.3. Large-teacher/tiny-base families can see maxtok collapse (Family 1 mean 1.7 vs plain 4.6)."
tags:
  - post-training
  - distillation
  - on-policy
  - sparse-supervision
  - opd
  - active
---

# Sparse OPD Supervision

## Method Overview
Keep the OPD token loss, drop almost every token. With mask $m_t \in \{0,1\}$,

\[
\mathcal{L}_{\mathrm{SOPD}}=\mathbb{E}\Big[\frac{1}{|y|}\sum_t \ell_t(\theta)\,m_t\Big],
\]

where $\ell_t$ is the usual PPO-clipped reverse-KL token loss and $A_t=\log\pi_T(y_t|h_t)-\log\pi_\theta(y_t|h_t)$. Practical masks: one random token; the max and/or min $A_t$; or the top and bottom 0.05% of $A_t$ (`pctltail`). This is a plug-in on `method:opd`, not a new distill algorithm and not CISPO.

`mintok` / `maxtok` follow Table 2 (highest / lowest reward). Do not trust Figure 1's swapped adjectives.

## When to Use
- Already running sampled-token OPD and token-level backward cost or teacher-noise is the complaint.
- Diagnosing whether dense reverse-KL is doing the work (often it is not).

## When NOT to Use
- Distill default → `method:opd`.
- Pass@1 labeled RLVR → `method:cispo`.
- Entropy collapse on sampled-token OPD → `method:ida-opd`.
- Prompt-set size → `method:opd-one-example` / `method:opd-hard-cot-selection`.

## Relation to Existing SOTA
- Active token-budget plug-in on `task:student-distillation`, beside `method:opd-hard-cot-selection`, `method:opd-one-example`, `method:ida-opd`, `method:tgopd`. Does **not** supersede `method:opd` or `method:cispo`.

## Gotchas & Failure Modes
- `maxtok` (lowest-reward token) can underperform plain OPD on large-teacher / small-base students (Family 1 mean 1.7 vs 4.6). Prefer `mintok` / `minmaxtok` / `pctltail` there.
- Best sparse runs often *increase* reverse KL. Do not early-stop on teacher match.
- Paper eval is avg@8 / pass@k with n=256, Qwen3 no-think, DAPO-Math-17K — not a CISPO bake-off.
