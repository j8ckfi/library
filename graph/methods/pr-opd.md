---
id: method:pr-opd
type: method
title: PR-OPD (Privileged Representation OPSD)
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: privileged-teacher OPSD with a gold solution and outcome verifier
  reason: VISTA remains the privileged-teacher first hop; PR-OPD is hidden-state alignment
    after GRPO
  use_instead: method:vista
- when: outcome-only long-horizon agent RL with a programmatic checker
  reason: CANOPY remains coverage RL; PR-OPD is a distill plug-in after GRPO
  use_instead: method:canopy
assumptions:
- 'Same-size self-teacher conditioned on hindsight skill. Paper: Qwen2.5-3B-Instruct ALFWorld / WebShop after GRPO.'
- Official repo balibata/PR-OPD as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:pr-opd
recipes:
- recipe:pr-opd
claims:
- benchmark: Qwen2.5-3B-Instruct ALFWorld / WebShop after GRPO; WebShop skill swap
  metric: success delta; fraction of tokens vs hidden states that change
  value: +4.7 ALFWorld / +11.7 WebShop; skill 42.2→56.2 with <25% token probs and
    >80% hidden states changing
  baseline: GRPO warm start without PR-OPD (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2609.36642
  notes: PreSO 2610.14001 is related work only (SKIP). Does not retarget VISTA, NSD,
    or CANOPY.
tags:
- distillation
- privileged-opsd
- hidden-states
- active
---

# PR-OPD (Privileged Representation OPSD)

## Method Overview
Warm-start with GRPO, then distill hidden states toward a self-teacher that sees hindsight skill. Token-level probabilities barely move; representations do.

## When to Use
- Agentic GRPO has plateaued and skill is sitting in hidden states rather than token probs.

## When NOT to Use
Gold-solution privileged OPSD → `method:vista`. Negative-condition anti-collapse → `method:nsd`. AppWorld coverage → `method:canopy`. Token OPD → `method:opd`.

## Relation to Existing SOTA
Active plug-in on `task:privileged-teacher-opsd` (`sota_for: []`). Mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace VISTA or NSD.

## Gotchas & Failure Modes
- Related PreSO (2610.14001) is not a library method this sweep.
- +11.7 WebShop is the paper's post-GRPO number, not a CANOPY bake-off.
