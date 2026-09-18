---
id: method:sol-pi
type: method
title: "SoL-Pi"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "production harness kernel (rewind, sandbox, remote, TUI / journal → session DOM)"
    reason: "omp² remains the architecture spec; SoL-Pi is a token-efficiency extension on Pi"
    use_instead: "method:omp2-harness"
  - when: "SWE-bench start/eval loop or GitHub issue → patch"
    reason: "mini-SWE-agent remains the locked ranking scaffold"
    use_instead: "method:mini-swe-agent"
  - when: "routing-harness RSI post-train of model weights"
    reason: "NeoHorse-1 remains that first hop; SoL-Pi searches harness mechanisms, not a weight curriculum"
    use_instead: "method:neohorse-1"
  - when: "train an async agent policy"
    reason: "this is a harness extension, not SAO"
    use_instead: "method:sao"
assumptions:
  - "You run Pi (`@earendil-works/pi-coding-agent` 0.85.1). SoL-Pi is a standalone extension; every mechanism is opt-in and off by default."
  - "EdgeBench 51 tasks with GPT-5.6 Sol and Opus 5 in the paper. Not a SWE-bench locked-mini number."
  - "Evidence-Preserving Reducer may send logs to a reducer model; review SECURITY.md before enabling."
last_reviewed: "2026-09-18"
papers:
  - paper:sol-pi
recipes:
  - recipe:sol-pi
claims:
  - benchmark: "EdgeBench, 51 tasks, GPT-5.6 Sol and Opus 5"
    metric: "task performance vs Pi / token traffic"
    value: "Pi-comparable quality; token traffic −44.7% to −49.0%"
    baseline: "native Pi; also Codex and Claude Code harnesses for cost"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20519"
    notes: "API cost about −1/3. Hourly savings $8.75–$13.50 vs Codex/Claude Code; $4.36–$5.71 vs Pi. Not an omp2 / mini-SWE-agent / NeoHorse-1 bake-off."
tags:
  - agents
  - agent-harness
  - rsi
  - token-efficiency
  - sol-pi
  - active
---

# SoL-Pi

## Method Overview
SoL-Pi is a Pi extension found by scaling auto-research at the harness layer. Four mechanisms survived: Action Fusion (validation in the same tool call as an edit/write), ObservationPack (large observations as handles with exact paged recall), Evidence-Preserving Reducer (compact log receipts whose quotes match the archive), and Online Context Compact (compact finished plan steps, then continue). They compose through Pi's public extension APIs. No Pi source patches. This is token-efficient harness RSI, not omp²'s journal kernel, not mini-SWE-agent's issue-to-patch loop, and not NeoHorse-1's routing-guided weight update.

## When to Use
- You already run Pi and want opt-in cuts to token traffic without changing the SWE start loop or the production kernel spec.

## When NOT to Use
- Harness kernel architecture → `method:omp2-harness`. Issue → patch → `method:mini-swe-agent`. Routing-harness post-train → `method:neohorse-1`. Policy RL → `method:sao`.

## Relation to Existing SOTA
- Active sibling on `task:agent-harness-runtime`. Mention on `task:agentic-rsi-routing-posttrain`. Does **not** enter `current_sota`. Does **not** supersede `method:omp2-harness`, `method:mini-swe-agent`, or `method:neohorse-1`.

## Gotchas & Failure Modes
- Missing `sol-pi.json` leaves every mechanism disabled.
- Reducer and compact start extra model calls; enable them only after the security and cost notes.
- EdgeBench is not SWE-bench locked mini. Do not retarget mini-SWE-agent from these numbers.
