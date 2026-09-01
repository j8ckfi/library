---
id: method:opsa
type: method
title: "OPSA (On-Policy Self-Adaptation)"
category: "rl-alignment"
status: sota
sota_for:
  - task:teacher-free-on-policy-self-adaptation
supersedes: []
do_not_use_for:
  - when: "verifiable labels exist and the goal is Pass@1 math/code RLVR"
    reason: "OPSA is supervision-free self-adaptation, not labeled RLVR"
    use_instead: "method:cispo"
  - when: "a strong teacher is available and the goal is intentional distillation"
    reason: "OPSA drops the teacher; OPD remains the single-teacher distill default"
    use_instead: "method:opd"
  - when: "unlabeled existing math problems with rollout-consensus pseudo-solutions"
    reason: "u-OPSD distills a majority-vote teacher along disagreeing paths; that is a different signal"
    use_instead: "method:u-opsd"
  - when: "test-time adaptation on unlabeled queries"
    reason: "OPSA is train-time; TTPO is the test-time first-hop"
    use_instead: "method:ttpo"
  - when: "zero external problems including unverifiable domains"
    reason: "J-Zero generates the curriculum; OPSA assumes an existing unlabeled prompt set"
    use_instead: "method:j-zero"
  - when: "flow matching or continuous diffusion post-training"
    reason: "Self-OPD is the teacher-free flow default"
    use_instead: "method:self-opd"
assumptions:
  - "Train-time unlabeled prompt corpus exists (paper: DAPO-17k questions, labels unused)."
  - "Policy can sample long on-policy rollouts; paper trains Qwen3-1.7B/4B and Qwen3.5-9B in non-thinking mode on 8 GPUs via slime."
  - "Does not require shared vocab or white-box teacher logits."
last_reviewed: "2026-09-01"
papers:
  - paper:opsa
recipes:
  - recipe:opsa
claims:
  - benchmark: "AIME24 Avg@32, Qwen3-1.7B non-thinking"
    metric: "Avg@32 accuracy"
    value: 48.85
    baseline: "Base 13.44 / OPD 32.08 / GRPO 33.96 / OPSD 33.33 / TTRL 19.90"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.31046"
    notes: "+35.41 vs base (263% relative). Paper Table 2/3. DAPO-17k questions only."
  - benchmark: "AIME24 / AIME25 / HMMT25 average, Qwen3-1.7B non-thinking"
    metric: "mean Avg@32 / Pass@32"
    value: "35.83 / 65.56"
    baseline: "Best RL baseline +11.04 Avg@32 and +8.89 Pass@32; base 9.62 / 31.11"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.31046"
    notes: "Table 3. Pass@32 more than doubles vs base on each of the three math benches."
  - benchmark: "AIME24 Avg@32, Qwen3.5-9B non-thinking"
    metric: "Avg@32 accuracy"
    value: 87.81
    baseline: "Base 76.35"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.31046"
    notes: "+11.46 on an already strong base; HMMT25 44.48 -> 67.40."
tags:
  - post-training
  - on-policy
  - teacher-free
  - label-free
  - opsa
  - sota
---

# OPSA (On-Policy Self-Adaptation)

## Method Overview
OPSA is train-time token-level RL with no teacher, reward, or hint. It updates only the lowest-20% log-probability response tokens and assigns entropy-adaptive negative advantages:

\[
A_i^{\mathrm{dyn}}=-\frac12-\frac{H_i-H_{\min}}{2(H_{\max}-H_{\min})}\in[-1.0,-0.5]
\]

$H_{\min}$ and $H_{\max}$ are the min/max entropy among those selected tokens in the same response. High-entropy positions get a more negative signal (toward $-1$), which suppresses sampled tails and redistributes mass among competing head tokens. Low-entropy confident tokens are typically excluded from the 20% set.

The paper's diagnosis of OPD: teacher advantages on student prefixes are noisy (30.6% at a 4B teacher, 50.6% at 235B-A22B), students are insensitive to that noise, and a fixed negative advantage on low-logp tokens matches teacher-provided ones. OPSA keeps the useful piece (negative signal on low-logp tokens) and drops the teacher.

## When to Use
- Train-time improvement of a reasoner when there is an unlabeled prompt set and no teacher, verifier, or hint channel.
- When OPD is attractive but teacher logits are unavailable, vocab-mismatched, or known to be noisy on student prefixes.

## When NOT to Use
- Labels exist and Pass@1 RLVR is the goal -> `method:cispo`.
- A strong teacher is available and the goal is to transfer that teacher -> `method:opd` (optionally `method:ra-opd` as a filter).
- Unlabeled math with majority-vote pseudo-solutions -> `method:u-opsd`.
- Test-time only -> `method:ttpo`.
- No problem corpus at all -> `method:j-zero`.
- Flow / diffusion -> `method:self-opd`.

## Relation to Existing SOTA
- First-hop only for `task:teacher-free-on-policy-self-adaptation`. Does **not** replace `method:cispo`, `method:opd`, `method:open-mopd`, `method:opdvr`, `method:u-opsd`, `method:self-opd`, `method:ttpo`, `method:vista`, or `method:j-zero`.
- Paper finding that OPD gains may not be distillation is documented here; it is not a supersession of OPD.

## Gotchas & Failure Modes
- Restricting to the bottom 10% logp over-sharpens and underperforms; 20/30/40% all work. Default 20%.
- Positive advantages on the same token set collapse the policy (length -> 0, gradient explosion). Do not flip the sign.
- TTRL-style self-consistency rewards can raise Avg@1 while hurting Pass@K; OPSA is the coverage-preserving alternative in this shelf, not a labeled-RLVR substitute.
- Paper trains non-thinking; enabling thinking at eval is complementary, not a training default.
