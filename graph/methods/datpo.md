---
id: method:datpo
type: method
title: "DATPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "DATPO is a coverage / Pass@k tree-rollout method; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "Pass@K / coverage / no-backward without tree rollouts"
    reason: "ES-reasoning remains the no-backward Pass@K first hop"
    use_instead: "method:es-reasoning"
  - when: "cold-start silent-group prompt selection"
    reason: "ThinkPrior ranks prompts; DATPO changes rollout structure"
    use_instead: "method:thinkprior"
assumptions:
  - "Host is a GRPO-family trainer that can emit tree-structured rollouts. Paper trains Qwen2.5-3B-Base and Qwen3-4B-Base on MATH, 1×A100 per run, based on GRPO-Zero."
  - "Default tree (N, Kmax, Bmax)=(4,3,4) with annealed sibling-diversity α: 0.2→0. gte-large-en-v1.5 embeddings."
  - "Token budget is matched to baselines; wall-clock is not, because branches wait on the base rollout."
last_reviewed: "2026-09-09"
papers:
  - paper:datpo
recipes:
  - recipe:datpo
claims:
  - benchmark: "Qwen2.5-3B-Base MATH500/AIME26/25/24/AMC23"
    metric: "avg@k / pass@k"
    value: "22.4 / 54.9"
    baseline: "GRPO 20.7/48.2; Dr.GRPO 21.7/48.2; TreeRL 21.7/46.1; AttnRL 21.3/53.0"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08650"
    notes: "Table 2. avg@8 on MATH500, avg@64 otherwise. Pass@k averaged over three eval runs."
  - benchmark: "Qwen3-4B-Base same suite"
    metric: "avg@k / pass@k"
    value: "31.3 / 60.4"
    baseline: "GRPO 30.1/58.3; AttnRL 30.7/57.4; TreeRL 30.3/56.7"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08650"
    notes: "Table 2. avg@k lift vs AttnRL is +0.6; pass@k +3.0."
  - benchmark: "Qwen2.5-3B-Base GPQA-Diamond avg@8"
    metric: "avg@8"
    value: 28.5
    baseline: "GRPO 25.3 / AttnRL 25.9 / TreeRL 25.3"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08650"
    notes: "Table 11 OOD. MMLU-Pro 33.1 ties AttnRL 33.2."
tags:
  - post-training
  - rlvr
  - passk
  - datpo
  - active
---

# DATPO

## Method Overview
DATPO expands RLVR **reasoning coverage** by changing train-time rollouts, not the Pass@1 kernel. Difficulty-adaptive trees allocate more leaves to hard prompts. Forking uses sentence entropy (mean token entropy of a sentence) to avoid the localization of top-k token entropy. Block-level PPO uses an advantage that adds an annealed sibling-diversity term from embedding cosine among child blocks.

ES-reasoning remains the Pass@K / no-backward first hop. CISPO remains Pass@1. ThinkPrior is a prompt prior, not a tree.

## When to Use
- Labeled math RLVR where Pass@k / test-time majority vote matters more than a small avg@k bump.
- You can pay tree-rollout wall-clock (≈2× GRPO in the paper).

## When NOT to Use
- Pass@1 default → `method:cispo`.
- No-backward Pass@K → `method:es-reasoning`.
- Silent-group prompt ranking → `method:thinkprior`.

## Relation to Existing SOTA
- Active on `task:passk-reasoning-coverage` and optional on `task:math-code-rl-dense`. Does **not** supersede `method:es-reasoning` or `method:cispo`.
- Distinct from TreeRL (token-entropy + local-global advantages) and AttnRL (attention forking).

## Gotchas & Failure Modes
- No DATPO-named GitHub; stack is GRPO-Zero.
- Wall-clock 60.3h vs GRPO 26.3h on 1×A100 despite matched generated tokens.
- avg@k gains are small; the headline is pass@k. Do not retarget CISPO from Table 2.
- Without the diversity term, AIME26 pass@64 peaks then falls (30.0% at step 200 → 25.6% at 700).
