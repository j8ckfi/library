---
id: method:harness-rsi
type: method
title: 'Harness RSI'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production harness kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the production kernel'
  use_instead: method:omp2-harness
- when: 'regularized harness RSI (annealed edit budget / anti-memorization critic)'
  reason: 'RRSI remains the regularized searcher'
  use_instead: method:rrsi
- when: 'recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)'
  reason: 'AIDE2 is the recursive rewrite loop'
  use_instead: method:aide2
- when: 'harness curriculum as a non-stationary bandit over failure-pattern arms'
  reason: 'ActiveSaddler remains failure-pattern curriculum'
  use_instead: method:activesaddler
assumptions:
- 'Formal harness self-evolution with frozen weights and an admission rule on fresh validation.'
- 'Code: zgcagi/Harness-RSI (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:harness-rsi
recipes:
- recipe:harness-rsi
claims:
- benchmark: 'formal PAC admission / retention bounds; cases from prior harness RSI work'
  metric: 'framework completeness, not a SWE-bench ranking'
  value: 'expected generalization bound; retention bound under regression budgets; high-probability admission on fresh validation'
  baseline: 'RRSI / AIDE2 / ActiveSaddler (related, not a bake-off)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.18813'
  notes: 'Does not replace omp2, RRSI, or AIDE2.'
tags:
- agent-harness
- rsi
- active
---

# Harness RSI

## Method Overview
Keep weights frozen. Propose revisions to prompts, memory, workflows, tools, repo control, or plugins. Admit only on fresh independent validation. Persist accepted revisions across runs.

## When to Use
- Formalizing harness self-evolution and admission, not replacing a production kernel.

## When NOT to Use
Production kernel → `method:omp2-harness`. Annealed edit-budget RSI → `method:rrsi`. Research-agent rewrite incumbent → `method:aide2`. Failure-pattern bandit → `method:activesaddler`.

## Relation to Existing SOTA
Active plug-in on `task:agent-harness-runtime` (`sota_for: []`). Does **not** replace omp2 or RRSI.

## Gotchas & Failure Modes
- Bounds assume explicit validation budgets; they are not a Terminal-Bench ranking.

