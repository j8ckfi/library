---
id: method:terminal-rsi
type: method
title: 'Terminal-RSI'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production harness kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the production kernel; Terminal-RSI is a recursive train recipe'
  use_instead: method:omp2-harness
- when: 'regularized harness RSI (annealed edit budget / anti-memorization critic)'
  reason: 'RRSI remains frozen-backbone harness search'
  use_instead: method:rrsi
- when: 'recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)'
  reason: 'AIDE2 rewrites the harness; Terminal-RSI rewrites trajectories then the policy'
  use_instead: method:aide2
- when: 'variable environment latency / async stragglers'
  reason: 'SAO remains async RL'
  use_instead: method:sao
assumptions:
- 'Terminal-bench agents with a verifier and a critic that can be handed off. Paper: Qwen3.8-27B five-stage RSR/RPR.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-16'
papers:
- paper:terminal-rsi
recipes:
- recipe:terminal-rsi
claims:
- benchmark: 'Terminal-Bench 2.1/3.0/4.0/Hard; LHTB; SWR100; Qwen3.8-27B'
  metric: 'success / process reward / strict completion'
  value: 'TB4.0 19.84%; TB2.1 86.52%; TB3.0 16.95%; TB Hard 79.00%; LHTB 0.21→0.37 and 0/46→5/46; SWR100 3%→6%'
  baseline: 'Qwen3.8-27B base through RSR-1 / RPR-1 / RSR-2 / RPR-2 (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22192'
  notes: 'Does not replace omp2 or RRSI. No public code as of 2026-10-16.'
tags:
- agent-harness
- rsi
- terminal
- active
---

# Terminal-RSI

## Method Overview
Alternate verified-trajectory rewrite (RSR) with critic-inheriting policy refine (RPR). TB-GAE keeps token baselines and decays across turns. FDR calibrates family progress; SPR splits strict success from bounded partial credit.

## When to Use
- Terminal-agent post-train where partial repairs must become strict verification.

## When NOT to Use
Production kernel → `method:omp2-harness`. Frozen-backbone harness RSI → `method:rrsi`. Harness rewrite as the next incumbent → `method:aide2`. Async stragglers → `method:sao`.

## Relation to Existing SOTA
Active plug-in on `task:agent-harness-runtime` (`sota_for: []`). Does **not** replace omp2 or RRSI.

## Gotchas & Failure Modes
- Five-stage 27B recipe; not a drop-in for omp2.
- No public GitHub as of 2026-10-16.

