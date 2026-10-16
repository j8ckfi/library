---
id: method:autosft
type: method
title: 'AutoSFT'
category: data-curriculum
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'open pretrain mix / Dolma-3 recipe rather than SFT data research'
  reason: 'OLMo-3 remains the instruct/pretrain recipe; AutoSFT curates SFT data'
  use_instead: method:olmo-3
- when: 'on-policy parameter update direction SFT (OPSFT)'
  reason: 'OPSFT is a trainer; AutoSFT is a data-research agent'
  use_instead: method:opsft
- when: 'drift-budget instruct FT (DCO)'
  reason: 'DCO is a layer-selective trainer; AutoSFT searches data actions'
  use_instead: method:dco
assumptions:
- 'SFT data research with a fixed model/trainer/budget and a pool that can be proportioned, pruned, repaired, replaced, or synthesized.'
- 'Code: Thinking-Space/AutoSFT (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:autosft
recipes:
- recipe:autosft
claims:
- benchmark: 'IFEval / IFBench / MBPP+ with retrain-from-base each round'
  metric: 'component-wise lifts vs single-agent data loop'
  value: 'analysis +6.5 IFEval; synthesis +3.4 IFEval / +2.9 IFBench; code analysis +3.7 MBPP+'
  baseline: 'single-agent SFT data loop; executor-only (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22194'
  notes: 'Does not retarget OLMo-3. Active SFT data-curation agent.'
tags:
- sft
- data-curriculum
- agentic
- active
---

# AutoSFT

## Method Overview
Treat SFT data research as a multi-action space. A meta agent keeps execution out of analysis context, collects independent proposals, and calls synthesis when the pool cannot cover a capability. Retrain from the base each round.

## When to Use
- Automating SFT mix edits when a human engineer would proportion / prune / repair / replace / synthesize.

## When NOT to Use
Instruct recipe default → `method:olmo-3`. On-policy SFT trainer → `method:opsft`. Drift-budget FT → `method:dco`.

## Relation to Existing SOTA
Active plug-in on `task:instruct-sft-alignment` (`sota_for: []`). Does **not** replace OLMo-3.

## Gotchas & Failure Modes
- Single-agent loops collapse to proportion-only and dump context.
- Gains are attributed because every round retrains from base; do not skip that.

