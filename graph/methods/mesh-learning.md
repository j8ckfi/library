---
id: method:mesh-learning
type: method
title: "Mesh Learning"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-turn dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; Mesh Learning is a strategy-collapse regularizer (Coach Prompting + balancing) on GRPO-style RLVR"
    use_instead: "method:cispo"
  - when: "all-zero verifier groups"
    reason: "VeriGate gates silent groups; Mesh Learning keeps multiple strategy heads from collapsing"
    use_instead: "method:verigate"
  - when: "Pass@K / coverage / no-backward rather than Pass@1"
    reason: "ES-reasoning remains Pass@K / coverage; Mesh Learning is a Pass@1-family collapse fix"
    use_instead: "method:es-reasoning"
assumptions:
  - "GRPO-style RLVR host. Concurrent strategy heads with a coach prompt and a balancing regularizer. Paper: Qwen3-4B and Qwen2.5-7B, AIME26."
  - "Official code Ayanami-0123/Open-Mesh-Learning released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:mesh-learning
recipes:
  - recipe:mesh-learning
claims:
  - benchmark: "Qwen3-4B Mesh Learning m=4 AIME26"
    metric: "AIME26"
    value: "56.7"
    baseline: "GRPO 43.3"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02835"
    notes: "Table 2. Not a CISPO Pass@1 retarget."
  - benchmark: "Qwen2.5-7B Mesh Learning m=4 AIME26"
    metric: "AIME26"
    value: "13.3"
    baseline: "GRPO 9.2"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02835"
    notes: "Same Table 2 row (m=4)."
tags:
  - post-training
  - rl-alignment
  - rlvr
  - mesh-learning
  - active
---

# Mesh Learning

## Method Overview
Outcome RLVR can keep Pass@1 climbing while the policy's strategy set collapses onto one surviving mode. Mesh Learning runs \(m\) concurrent strategy heads. Coach Prompting keeps the heads semantically distinct; Strategy-Balancing Regularization penalizes mass concentrating on one head. The inner optimizer in the paper is GRPO-style; the library Pass@1 default is still CISPO.

## When to Use
- Dense math RLVR where you observe strategy collapse (diverse traces dying) and you can afford \(m\) heads plus a coach prompt.

## When NOT to Use
- Pass@1 default → `method:cispo`. Silent all-zero groups → `method:verigate`. Pass@K / coverage → `method:es-reasoning`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` beside CISPO (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- Do not cite 56.7 vs GRPO 43.3 as a CISPO bake-off.
- \(m=4\) is the reported AIME26 setting; \(m=3\) is a weaker row in the same table.
