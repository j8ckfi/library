---
id: method:verpo
type: method
title: "VERPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "VERPO regularizes privileged-evidence corrections; CISPO remains the Pass@1 kernel"
    use_instead: "method:cispo"
  - when: "privileged same-size gold teacher with student-to-teacher adaptation"
    reason: "VISTA adapts the privileged teacher; VERPO keeps the outcome objective and gates evidence as a proposal"
    use_instead: "method:vista"
  - when: "no teacher, no reward, no privileged evidence"
    reason: "OPSA is supervision-free"
    use_instead: "method:opsa"
  - when: "single-teacher matching distillation without privileged replay"
    reason: "OPD remains the matching default"
    use_instead: "method:opd"
assumptions:
  - "Host loop already has an outcome verifier. Privileged evidence (reference solution, tool trace, or environment feedback) is available at train time only."
  - "Paper: five scientific-reasoning / tool-use tasks; Qwen3-4B/8B and Llama-3.2-1B. No official code as of 2026-09-09."
last_reviewed: "2026-09-09"
papers:
  - paper:verpo
recipes:
  - recipe:verpo
claims:
  - benchmark: "Five scientific-reasoning / tool-use tasks, Qwen3-4B average"
    metric: "average score"
    value: 0.6857
    baseline: "strongest compared baseline 0.6826"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06100"
    notes: "Best variant on that backbone. Small lift; 8B and 1B lifts are larger."
  - benchmark: "Same suite, Qwen3-8B average"
    metric: "average score"
    value: 0.7058
    baseline: "strongest compared baseline 0.6895"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06100"
  - benchmark: "Same suite, Llama-3.2-1B average"
    metric: "average score"
    value: 0.5657
    baseline: "strongest compared baseline 0.4751"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06100"
tags:
  - post-training
  - opsd
  - privileged-teacher
  - verpo
  - active
---

# VERPO

## Method Overview
VERPO is **verified-evidence regularization** on top of an outcome RLVR loop. Privileged evidence (gold, tool feedback) is a proposal, not a matching target. Evidence-free restoration and signed token-level corrections are separate. Fisher Evidence Contrast shrinks corrections along an estimated evidence-presence direction. A stopped token-wise ZPD controller scales acceptance by local reward alignment and Fisher movement cost; the reference channel ignores that gate.

Sits beside VISTA (teacher adaptation on privileged OPSD) and FlowBalance (trajectory-balance self-guidance). Does not replace CISPO.

## When to Use
- Outcome RL plus a privileged evidence channel, when naive teacher imitation copies style that does not help the verifier.

## When NOT to Use
- Pass@1 kernel → `method:cispo`. Privileged-teacher OPSD default → `method:vista`. No labels → `method:opsa`.

## Relation to Existing SOTA
- Active on `task:privileged-teacher-opsd` and as a mention on `task:math-code-rl-dense`. Does **not** enter `current_sota`. Does **not** supersede VISTA, CISPO, OPD, or OPSA.

## Gotchas & Failure Modes
- No official GitHub as of 2026-09-09.
- 4B average lift is small (0.6826→0.6857). Do not treat that as a CISPO bake-off.
- Indiscriminate evidence imitation is the failure mode the paper is written against; do not drop the outcome term.
