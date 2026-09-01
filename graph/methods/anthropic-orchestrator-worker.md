---
id: method:anthropic-orchestrator-worker
type: method
title: "Anthropic orchestrator-worker"
category: "agent-harness"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "SWE patches, τ-bench, or sequential one-context work"
    reason: "MAS exception is internal breadth research, not patches"
    use_instead: "method:single-agent-plus-tools"
assumptions:
  - "High-value parallel research only. +90.2% vs single Opus 4, ~15× tokens. June 2025."
last_reviewed: "2026-09-01"
papers:
  - paper:mas-hybrid-gao
claims:
  - benchmark: "Anthropic internal breadth research (Jun 2025)"
    metric: "relative quality vs single Opus 4"
    value: "+90.2%"
    baseline: "single Opus 4; ~15× tokens"
    date: "2025-06"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://www.anthropic.com/engineering/built-multi-agent-research-system"
    notes: "Niche. Default remains single-agent+tools. Gao cascade is the other documented MAS win (+1.1–12pp)."
tags:
  - agents
  - multi-agent
  - orchestrator-worker
  - niche
---

# Anthropic orchestrator-worker

## Method Overview
Niche MAS pattern: orchestrator-worker for **high-value parallel research**. Anthropic June 2025: **+90.2%** vs single Opus 4 on internal breadth research, ~15× tokens. Default is still `method:single-agent-plus-tools`.

## When to Use
- High-value parallel breadth research with token budget to match.

## When NOT to Use
- SWE, τ-bench, sequential work → `method:single-agent-plus-tools`.
