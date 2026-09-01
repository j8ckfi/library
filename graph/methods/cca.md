---
id: method:cca
type: method
title: "Confucius Code Agent (CCA)"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "default first hop for building a SWE agent"
    reason: "mini-SWE-agent is the 2026 winning design and locked harness"
    use_instead: "method:mini-swe-agent"
  - when: "dumped long prompt offload"
    reason: "CCA is a repo harness, not RLM"
    use_instead: "method:rlm"
  - when: "training an agent policy with async RL"
    reason: "CCA is a scaffold, not SAO"
    use_instead: "method:sao"
assumptions:
  - "Equal-model/tools comparisons in 2512.10398. facebookresearch/cca-swebench puts the agent inside the container."
last_reviewed: "2026-09-01"
papers:
  - paper:cca
recipes:
  - recipe:cca-swe
claims:
  - benchmark: "SWE-Bench-Pro public, Claude 4.5 Sonnet, equal model/tools"
    metric: "resolved %"
    value: 52.7
    baseline: "SWE-agent 43.6"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.10398"
    notes: "Paper equal-model/tools vs SWE-agent."
  - benchmark: "SWE-bench Verified, Claude 4 Sonnet"
    metric: "resolved %"
    value: 74.6
    baseline: "OpenHands 72.8 / SWE-agent 66.6"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.10398"
    notes: "Use when notes/context management beyond bash is required."
  - benchmark: "SWE-Bench-Pro, GPT-5.2 CCA"
    metric: "resolved %"
    value: 59.0
    baseline: "OpenAI proprietary 56.0"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.10398"
    notes: "Paper-reported split."
tags:
  - agents
  - agent-harness
  - cca
  - swe-bench
---

# Confucius Code Agent (CCA)

## Method Overview
CCA is a software-engineering scaffold with notes and context management. The public harness (`facebookresearch/cca-swebench`) runs the agent *inside* the Docker container rather than through a host-side runtime abstraction. Active alternative on `task:software-engineering-agent-harness`. Not SOTA; mini-SWE-agent remains the default loop.

## When to Use
- Equal-model work where you need notes/context management beyond bash.
- SWE-Bench-Pro public evals that match the CCA paper protocol.

## When NOT to Use
- Default "build an agent" → `method:mini-swe-agent`.
- Dumped prompt → `method:rlm`. Train policy → `method:sao`.

## Gotchas & Failure Modes
- Do not treat CCA wins over SWE-agent as a reason to replace the locked mini harness on official Verified/Pro model boards.
