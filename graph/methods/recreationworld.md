---
id: method:recreationworld
type: method
title: "RecreationWorld"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "desktop/OS GUI ranking on OSWorld 2.0 paper protocol"
    reason: "Claude computer-use remains that ranking SOTA; RecreationWorld is hybrid GUI+code train/eval"
    use_instead: "method:claude-computer-use"
  - when: "GitHub issue to patch / SWE harness"
    reason: "mini-SWE-agent remains the issue-to-patch loop"
    use_instead: "method:mini-swe-agent"
  - when: "programmatic checker AppWorld coverage / anti-drift"
    reason: "CANOPY remains outcome-only agent RL; recreation is a hybrid CUA environment"
    use_instead: "method:canopy"
  - when: "trained mobile-only GUI policy on AndroidWorld"
    reason: "MAI-UI / UI-TARS-2 are trained GUI policies, not hybrid recreation"
    use_instead: "method:mai-ui"
assumptions:
  - "Hybrid CUA: the agent interleaves GUI exploration, implementation, and visual verification of its own artifacts. Five platforms: Ubuntu, macOS, Windows, Android, Web."
  - "Reward is reference-as-oracle: hidden programmatic and visual assertions derived from a running reference, frozen after human review."
  - "Code and RecreationBench released. RecreationBench is 250 tasks, 50 per platform."
last_reviewed: "2026-09-21"
papers:
  - paper:recreationworld
recipes:
  - recipe:recreationworld
claims:
  - benchmark: "RecreationBench overall, GPT-6 Astra"
    metric: "unweighted mean of programmatic and visual scores"
    value: "58.1%"
    baseline: "Claude Opus 5 44.2%; GPT-5.6 Sol 42.1%; Qwen3.8-Max-0902 34.8%"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22000"
    notes: "Prog 58.19 / VLM 57.92. Full programmatic pass on 2.8% of tasks. Ranking bench for hybrid recreation, not OSWorld 2.0."
  - benchmark: "Five OOD coding / hybrid CUA benches after recreation training"
    metric: "gain vs first checkpoint"
    value: "up to +17.9 pp"
    baseline: "first evaluated checkpoint of the same run"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22000"
    notes: "Qwen3.7-Plus +5.8 pp and Qwen-Flash-CPT +12.1 pp on the reported transfer plot. Transfer beyond recreation."
tags:
  - agents
  - computer-use
  - hybrid-cua
  - recreationworld
  - active
---

# RecreationWorld

## Method Overview
RecreationWorld is a train/eval framework for hybrid computer-use agents. Each task gives a running reference application. The agent must discover behavior by operating the reference, then implement, build, run, and visually verify a candidate, with no prescribed stage order. Hidden tests are derived from the reference: programmatic assertions read structured UI state; visual assertions judge rendered properties. Code and data are released.

The OSWorld 2.0 ranking shelf stays Claude computer-use. This method is the hybrid GUI+code training environment.

## When to Use
- Training or evaluating agents that must interleave GUI exploration with code/CLI implementation and visually verify their own artifacts across desktop, mobile, or web.

## When NOT to Use
- OSWorld 2.0 paper-protocol ranking → `method:claude-computer-use`. Issue-to-patch → `method:mini-swe-agent`. AppWorld coverage → `method:canopy`. Mobile GUI-only → `method:mai-ui`.

## Relation to Existing SOTA
- Active first hop on `task:hybrid-computer-use-agent-rl` only (method status active; listed in that task's `current_sota`). Mention on `task:computer-use-agent`. Does **not** demote `method:claude-computer-use`. Does **not** replace `method:mini-swe-agent` or `method:canopy`.

## Gotchas & Failure Modes
- High overall scores can hide near-zero full programmatic pass (2.8% for GPT-6 Astra). Score both axes.
- Static interface structure is easier than interactions and computed outputs. Do not treat a pretty recreation as a behavioral clone.
- Platform-native GUI stacks differ (AT-SPI, AXUIElement, UI Automation, UiAutomator, browser). The unified harness does not erase those.
