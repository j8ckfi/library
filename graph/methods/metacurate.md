---
id: method:metacurate
type: method
title: 'MetaCurate'
category: data-curriculum
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'chat / instruct SFT stack (OLMo-3 Dolci)'
  reason: 'OLMo-3 remains the open instruct stack; MetaCurate evolves SWE trajectory filters'
  use_instead: method:olmo-3
- when: 'agentic automated SFT data research (AutoSFT)'
  reason: 'AutoSFT is general SFT data research; MetaCurate is SWE trajectory filter evolution'
  use_instead: method:autosft
- when: 'scalable SWE issue synthesis from historical bug fixes'
  reason: 'SWE-at-Scale synthesizes issues; MetaCurate filters trajectories'
  use_instead: method:swe-at-scale
assumptions:
- 'Starts from a blank filter. Pairwise LLM judgments revise rules, rubric, and aggregation. Downstream SFT on an uncurated pool and Nemotron v3 SWE.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:metacurate
recipes:
- recipe:metacurate
claims:
- benchmark: 'SWE-Verified SFT vs random selection, hand-authored filters, and a 3.5x-cost training-loop baseline'
  metric: 'mean SWE-Verified'
  value: 'highest mean among compared methods, including hand-authored filters and a 3.5x-cost training-loop baseline'
  baseline: 'random / hand-authored / training-loop filter (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23134'
  notes: 'Does not retarget OLMo-3, AutoSFT, or SWE-at-Scale.'
tags:
- sft
- curation
- swe
- active
---

# MetaCurate

## Method Overview
MetaCurate evolves a curation filter from pairwise LLM judgments: disagreements with the judge rewrite the filter's rules, rubric, and aggregation, then the filter scores trajectories independently at scale.

## When to Use
- Agentic coding SFT from a raw trajectory pool when handwritten filters are the bottleneck.

## When NOT to Use
Open instruct stack → `method:olmo-3`. General SFT data research → `method:autosft`.

## Relation to Existing SOTA
Active plug-in on `task:instruct-sft-alignment` with a mention on `task:coding-agent-rl-environment-construction` (`sota_for: []`). Does **not** replace OLMo-3 or AutoSFT.

## Gotchas & Failure Modes
- Pairwise judgments only during search; scoring is independent afterward.
- SWE-Verified SFT, not CodeMidas env construction.
