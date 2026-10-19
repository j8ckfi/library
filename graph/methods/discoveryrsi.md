---
id: method:discoveryrsi
type: method
title: 'DiscoveryRSI'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production harness kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the kernel; DiscoveryRSI is scientific hypothesis RSI'
  use_instead: method:omp2-harness
- when: 'terminal-agent RSR + RPR recursive self-improve'
  reason: 'Terminal-RSI is TB-GAE terminal RSI; DiscoveryRSI is hypothesis-tree science'
  use_instead: method:terminal-rsi
- when: 'formal Harness RSI + PAC admission (frozen weights)'
  reason: 'Harness-RSI is PAC admission; DiscoveryRSI scores hypothesis trees'
  use_instead: method:harness-rsi
assumptions:
- 'Multi-agent evolutionary hypothesis trees compiled into Harbor tasks. Code: Gen-Verse/DiscoveryRSI.'
- 'Life-science domains in the paper; DFM-Bench for hypothesis quality.'
last_reviewed: '2026-10-19'
papers:
- paper:discoveryrsi
recipes:
- recipe:discoveryrsi
claims:
- benchmark: 'DFM-Bench hypothesis quality after two self-improve rounds; post-cutoff correspondence vs GPT-6 Luna / Claude Opus 5'
  metric: 'hypothesis quality; post-cutoff correspondence'
  value: '4.86→5.39 after two rounds; DiscoveryRSI-27B 6.3% vs GPT-6 2.5% / Opus 5 2.3%'
  baseline: 'base model / GPT-6 Luna / Claude Opus 5 (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23839'
  notes: 'Does not retarget omp2, Terminal-RSI, or Harness-RSI. Code released.'
tags:
- harness
- rsi
- science
- active
---

# DiscoveryRSI

## Method Overview
DiscoveryRSI grows hypothesis trees with multi-agent evolutionary search, compiles selected investigations into Harbor tasks, and learns via hypothesis credit, harness replay, and rediscovery of accepted improvements.

## When to Use
- Scientific-discovery agents that must turn evidence-grounded hypotheses into executable investigations and learn from that loop.

## When NOT to Use
Production kernel → `method:omp2-harness`. Terminal-bench RSI → `method:terminal-rsi`.

## Relation to Existing SOTA
Active plug-in on `task:agent-harness-runtime` (`sota_for: []`). Does **not** replace omp2 or Terminal-RSI.

## Gotchas & Failure Modes
- Life-science domains and DFM-Bench; not SWE-bench.
- Human-rated correspondence is not a locked harness ranking.
