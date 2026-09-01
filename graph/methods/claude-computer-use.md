---
id: method:claude-computer-use
type: method
title: "Claude Computer Use (OSWorld 2.0 paper protocol)"
category: "agent-harness"
status: sota
sota_for:
  - task:computer-use-agent
supersedes: []
do_not_use_for:
  - when: "GitHub issue → patch"
    reason: "desktop GUI is not a SWE harness"
    use_instead: "method:mini-swe-agent"
  - when: "citing aggregator Opus 5 70.6% or Steel GPT-5.6 Sol 62.6% partial as this method's SOTA"
    reason: "those are different snapshots/protocols; paper protocol is 20.6% binary / 54.8% partial"
    use_instead: "method:claude-computer-use"
  - when: "trained mobile GUI policy"
    reason: "MAI-UI / UI-TARS-2 are trained policies on old protocols"
    use_instead: "method:mai-ui"
assumptions:
  - "OSWorld 2.0 paper protocol (2606.29537). Not OSWorld-Verified (near-saturated)."
last_reviewed: "2026-09-01"
papers:
  - paper:osworld-2
recipes:
  - recipe:claude-computer-use
claims:
  - benchmark: "OSWorld 2.0 (paper protocol), Opus 4.8 max think + batched tools"
    metric: "binary / partial success"
    value: "20.6% binary / 54.8% partial"
    baseline: "GPT-5.5 ~13% binary; humans ~1.6h"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.29537"
    notes: "Do not promote aggregator Opus 5 70.6% or Steel GPT-5.6 Sol 62.6% partial as method SOTA. Failures: lost constraints, skip verify — not GUI grounding."
tags:
  - agents
  - computer-use
  - osworld
  - sota
---

# Claude Computer Use (OSWorld 2.0 paper protocol)

## Method Overview
On OSWorld **2.0** (2606.29537), Claude Opus 4.8 with max thinking and batched tools is the paper-protocol current_sota: **20.6% binary / 54.8% partial**. GPT-5.5 is ~13% binary. Humans ~1.6h. Failures are lost constraints and skipped verification, not GUI grounding.

OSWorld-Verified is near-saturated and is not the ranking bench. Do **not** mix paper 20.6% with aggregator 70.6%.

## When to Use
- Desktop/OS computer-use on the OSWorld 2.0 protocol.

## When NOT to Use
- GitHub issue → patch → `method:mini-swe-agent`.
- Mobile AndroidWorld → `method:mai-ui`.
- Old OSWorld trained policy → `method:ui-tars-2` (not 2.0).

## Gotchas & Failure Modes
- Aggregator boards (Opus 5 70.6%, Steel 62.6% partial) are not this method's SOTA.
