---
id: method:nsd
type: method
title: "Negative Self-Distillation (NSD)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "labeled Pass@1 math/code RLVR"
    reason: "NSD is an anti-collapse self-distillation trainer, not the Pass@1 kernel"
    use_instead: "method:cispo"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the matching default"
    use_instead: "method:opd"
  - when: "privileged-teacher OPSD is still desired and working"
    reason: "VISTA remains the privileged-teacher first hop; NSD diverges from a negative condition instead of adapting a gold teacher"
    use_instead: "method:vista"
  - when: "teacher-free entropy-adaptive self-adaptation with no negative teacher"
    reason: "OPSA stays that first hop; NSD still builds a negative condition"
    use_instead: "method:opsa"
assumptions:
  - "Reasoning post-train. Paper: Qwen3-1.7B/4B/8B, 2 epochs, α=0.01. Default negative condition is generated online without gold answers."
  - "Official train/eval: Prongcan/NSD (in-repo verl; scripts/4B_NSD and scripts/eval). Collection: PassionPrc/nsd-negative-self-distillation. Checkpoints: PassionPrc/NSD-Qwen3-{1.7B,4B,8B}."
last_reviewed: "2026-09-11"
papers:
  - paper:nsd
recipes:
  - recipe:nsd
claims:
  - benchmark: "AIME 24/25/26 + HMMT + AMC + OlympiadBench + MATH, Qwen3-1.7B ΔAvg"
    metric: "average accuracy lift vs base"
    value: "+2.3"
    baseline: "OPSD +1.1 / Intuitor −0.5 / TTRL +0.3 (same table)"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11699"
    notes: "Table 1. CI [+0.7, +4.0], p=0.001. Not a CISPO Pass@1 bake-off."
  - benchmark: "Same suite, Qwen3-4B ΔAvg"
    metric: "average accuracy lift vs base"
    value: "+7.5"
    baseline: "OPSD +1.0 / Intuitor +1.3 / TTRL +0.2"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11699"
    notes: "Table 1. Peak AIME24 35.8. Reflection tokens 7.5 vs OPSD 2.2 (Table 2)."
  - benchmark: "Same suite, Qwen3-8B ΔAvg"
    metric: "average accuracy lift vs base"
    value: "+6.0"
    baseline: "OPSD +0.3 / Intuitor +1.9 / TTRL −0.1"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11699"
    notes: "Table 1. Peak AIME24 39.6. CI [+4.0, +7.9]."
tags:
  - post-training
  - distillation
  - opsd
  - nsd
  - anti-collapse
  - active
---

# Negative Self-Distillation (NSD)

## Method Overview
OPSD collapse: a privileged confident teacher forces imitation and kills uncertainty / self-correction. NSD **diverges** from a self-generated negative condition (a "careless reasoner") instead of matching gold. Default: generate the negative prompt online from the student, no gold answers.

Loss (repo):

\[
L = \beta\,\mathrm{KL}(\pi_S \| \pi_{\mathrm{ref}}) + \alpha\,\max(0, \pi_{\mathrm{atk}} - \pi_{\mathrm{ref}})\,\mathrm{unlikelihood}(\pi_S)
\]

A dynamic gate keeps the push on reasoning-critical tokens so ordinary language is not unlearned. Host modes: supervised distillation (forward KL + trust-region clip) or NSD as a negative reward on GRPO.

Actionable anti-collapse trainer next to the `method:opsd-collapse-review` survey. Does not replace VISTA.

## When to Use
- OPSD / privileged imitation is collapsing self-correction and you want a trainer that pushes away from flawed traces.
- Label-free online negative conditions are acceptable.

## When NOT to Use
- Pass@1 labels → `method:cispo`. Frozen teacher matching → `method:opd`. Privileged-teacher OPSD that still works → `method:vista`. No negative teacher at all → `method:opsa`.

## Relation to Existing SOTA
- Active sibling on `task:privileged-teacher-opsd`. Does **not** enter `current_sota`. VISTA remains the privileged-teacher first hop.
- Mention on `task:teacher-free-on-policy-self-adaptation` as the anti-collapse trainer that still uses a negative condition. OPSA remains that task's first hop.
- `method:opsd-collapse-review` stays the niche survey; NSD is the trainer you actually run.

## Gotchas & Failure Modes
- Ungated unlearning of the negative teacher also hits function words. Keep the divergence gate.
- Paper GRPO mode is an inner host, not a revival of GRPO as the library Pass@1 default.
- 1.7B lift is smaller than 4B/8B. Do not treat Table 1 as a CISPO comparison.
