---
id: method:mai-ui
type: method
title: "MAI-UI"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "OSWorld 2.0 desktop protocol"
    reason: "MAI-UI is mobile AndroidWorld"
    use_instead: "method:claude-computer-use"
  - when: "GitHub issue → patch"
    reason: "mobile GUI is not SWE"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Mobile GUI. AndroidWorld 76.7 vs UI-TARS-2 73.3."
last_reviewed: "2026-09-01"
papers:
  - paper:mai-ui
claims:
  - benchmark: "AndroidWorld"
    metric: "success %"
    value: 76.7
    baseline: "UI-TARS-2 73.3"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.22047"
    notes: "Active mobile computer-use. Not OSWorld 2.0."
tags:
  - agents
  - computer-use
  - mobile
  - mai-ui
---

# MAI-UI

## Method Overview
MAI-UI (2512.22047) is the active mobile computer-use agent. AndroidWorld **76.7%** vs UI-TARS-2 73.3. Not desktop OSWorld 2.0 SOTA.

## When to Use
- Mobile / AndroidWorld computer-use.

## When NOT to Use
- OSWorld 2.0 desktop → `method:claude-computer-use`.
- SWE → `method:mini-swe-agent`.
