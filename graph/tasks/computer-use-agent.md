---
id: task:computer-use-agent
type: task
title: "Computer-Use Agent"
domain: "agents"
summary: "Desktop/OS or mobile GUI agents. Paper-protocol ranking is OSWorld 2.0, not aggregator boards and not OSWorld-Verified."
scope: "GUI computer-use. Paper protocol OSWorld 2.0 for desktop. Not GitHub-issue-to-patch."
out_of_scope:
  - "GitHub issue → patch (SWE harness)"
  - "OSWorld-Verified as the ranking bench (near-saturated)"
  - "Aggregator 70.6% / Steel 62.6% as method SOTA"
redirects:
  - when: "GitHub issue to patch"
    to: "task:software-engineering-agent-harness"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:claude-computer-use
    as_of: "2026-06"
    benchmark: "OSWorld 2.0 paper protocol"
    metric: "binary / partial success"
    value: "Opus 4.8 max think + batched tools 20.6% binary / 54.8% partial; GPT-5.5 ~13% binary"
    notes: "Do not promote aggregator Opus 5 70.6% or Steel GPT-5.6 Sol 62.6% partial. Humans ~1.6h. Failures: lost constraints, skip verify."
methods:
  - method:claude-computer-use
  - method:ui-tars-2
  - method:mai-ui
tags:
  - agents
  - computer-use
  - osworld
  - gui
---

# Computer-Use Agent

## Problem Definition
Operate a desktop OS or mobile GUI. Different from a software-engineering agent harness.

## Evaluation Protocol & Benchmarks
- **Ranking (desktop)**: OSWorld 2.0 paper protocol (2606.29537).
- **Not ranking**: OSWorld-Verified (near-saturated); aggregator 70.6%.
- **Mobile**: AndroidWorld (MAI-UI 76.7 vs UI-TARS-2 73.3).
- **Trained policy (old OSWorld)**: UI-TARS-2 47.5 — not comparable to 2.0 20.6% binary.

## SOTA Landscape
- **current_sota (paper protocol)**: Claude computer-use on OSWorld 2.0.
- **Active trained**: UI-TARS-2 (old protocol).
- **Active mobile**: MAI-UI.
