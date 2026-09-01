---
id: method:ui-tars-2
type: method
title: "UI-TARS-2"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "OSWorld 2.0 paper protocol ranking"
    reason: "47.5 is old OSWorld, not 2.0"
    use_instead: "method:claude-computer-use"
  - when: "mobile AndroidWorld default"
    reason: "MAI-UI 76.7 vs UI-TARS-2 73.3"
    use_instead: "method:mai-ui"
assumptions:
  - "Trained GUI policy. Old OSWorld protocol, not 2.0."
last_reviewed: "2026-09-01"
papers:
  - paper:ui-tars-2
claims:
  - benchmark: "OSWorld (old protocol)"
    metric: "success %"
    value: 47.5
    baseline: "prior UI-TARS / GUI RL (paper)"
    date: "2025-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2509.02544"
    notes: "Not OSWorld 2.0. Do not compare 47.5 to 20.6% binary as the same protocol."
  - benchmark: "AndroidWorld"
    metric: "success %"
    value: 73.3
    baseline: "MAI-UI later 76.7"
    date: "2025-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2509.02544"
    notes: "Trained policy. MAI-UI is the active mobile lead."
tags:
  - agents
  - computer-use
  - ui-tars
---

# UI-TARS-2

## Method Overview
UI-TARS-2 (2509.02544) is a trained GUI policy: OSWorld 47.5 / AndroidWorld 73.3 on the **old OSWorld protocol, not 2.0**. Active on `task:computer-use-agent`. Paper-protocol SOTA remains Claude computer-use on OSWorld 2.0.

## When to Use
- Trained GUI policy on the old OSWorld / AndroidWorld numbers.

## When NOT to Use
- OSWorld 2.0 ranking → `method:claude-computer-use`.
- Mobile lead → `method:mai-ui`.
