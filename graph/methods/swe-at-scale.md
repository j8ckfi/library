---
id: method:swe-at-scale
type: method
title: 'SWE-at-Scale'
category: data-curriculum
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'source-code-only env factory then GRPO (CodeMidas)'
  reason: 'CodeMidas remains OSS-functionality env construction; SWE-at-Scale synthesizes issues from fixes'
  use_instead: method:codemidas
- when: 'GitHub issue to patch / SWE harness loop'
  reason: 'mini-SWE-agent remains the loop; this is training-data synthesis'
  use_instead: method:mini-swe-agent
- when: 'from-scratch program reproduction envs / Program-Agent'
  reason: 'ProgramGym is reproduction, not fix inversion'
  use_instead: method:programgym
assumptions:
- 'Need more verifiable SWE tasks than natural issue frequency. Historical fixes required.'
- 'Code: cslsolow/SWE-at-scale (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:swe-at-scale
recipes:
- recipe:swe-at-scale
claims:
- benchmark: 'synthesized SWE tasks vs current synthesis baselines; diversity up to 200 gens/file'
  metric: 'diversity / difficulty vs SOTA coding agents'
  value: 'more diverse and realistic than compared synthesizers; distinct bug types from one file; harder for SOTA agents'
  baseline: 'heuristic LLM issue synthesis (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.21359'
  notes: 'Does not replace CodeMidas or mini-SWE-agent.'
tags:
- swe
- data-curriculum
- active
---

# SWE-at-Scale

## Method Overview
Invert a historical fix into a bug-induction operator, transfer the pattern to a new context, and sample executable issues with tests. One file can yield many bug types.

## When to Use
- Scaling SWE training data beyond the natural issue stream.

## When NOT to Use
OSS env factory → `method:codemidas`. Issue-to-patch loop → `method:mini-swe-agent`. From-scratch reproduction → `method:programgym`.

## Relation to Existing SOTA
Active plug-in on `task:coding-agent-rl-environment-construction` with a mention on `task:software-engineering-agent-harness` (`sota_for: []`). Does **not** replace CodeMidas.

## Gotchas & Failure Modes
- Quality still depends on the historical-fix distribution.

