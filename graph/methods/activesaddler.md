---
id: method:activesaddler
type: method
title: "ActiveSaddler"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "production harness kernel (rewind, sandbox, remote, TUI / journal → session DOM)"
    reason: "omp² remains the kernel spec; ActiveSaddler is a curriculum over failure-pattern arms"
    use_instead: "method:omp2-harness"
  - when: "regularized harness RSI (annealed edit budget / anti-memorization critic)"
    reason: "RRSI searches harness edits around a frozen backbone; ActiveSaddler chooses which scenarios drive those updates"
    use_instead: "method:rrsi"
  - when: "recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)"
    reason: "AIDE2 rewrites the harness codebase; ActiveSaddler schedules training scenarios"
    use_instead: "method:aide2"
  - when: "routing-harness RSI post-train of model weights"
    reason: "NeoHorse-1 updates weights from routing traces; ActiveSaddler does not train weights"
    use_instead: "method:neohorse-1"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness"
    reason: "Harness-Zero maps harness behaviors into weights; ActiveSaddler is curriculum, not distillation"
    use_instead: "method:harness-zero"
assumptions:
  - "Offline learning-based automatic harness optimization (AutoSaddler-style): fixed train/dev/test, harness optimizer O patches prompts/tools/control from execution traces. ActiveSaddler only changes which training scenarios are selected."
  - "Paper: GAIA2 and Terminal-Bench 2.0 vs the same harness optimizer with a scenario order fixed before optimization."
  - "Code host microsoft/AutoSaddler; project https://autosaddler-projectpage.github.io/activesaddler/ (aka.ms/ActiveSaddler-website)."
last_reviewed: "2026-10-02"
papers:
  - paper:activesaddler
recipes:
  - recipe:activesaddler
claims:
  - benchmark: "GAIA2 test Pass@1 vs same harness optimizer, fixed scenario order"
    metric: "Pass@1 lift"
    value: "+4.4 pp"
    baseline: "identical harness optimizer with scenario order fixed before optimization"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.00906"
    notes: "Curriculum dimension, not a new kernel. Does not replace omp2 / RRSI / AIDE2 / Harness-Zero / NeoHorse-1."
  - benchmark: "Terminal-Bench 2.0 test Pass@1 vs same harness optimizer, fixed scenario order"
    metric: "Pass@1 lift"
    value: "+7.5 pp"
    baseline: "identical harness optimizer with scenario order fixed before optimization"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.00906"
    notes: "Ablations: failure-pattern arms, evolving utility, explore-vs-revisit balance are all load-bearing."
tags:
  - agents
  - agent-harness
  - curriculum
  - activesaddler
  - active
---

# ActiveSaddler

## Method Overview
Harness optimizers usually fix the scenario set and only evolve prompts, tools, and control. ActiveSaddler treats the **training curriculum** as a non-stationary bandit. Arms are failure-pattern clusters instantiated from diagnosed traces (not category labels, not one arm per scenario). Each iteration either revisits an arm by estimated remaining learning progress or evaluates unseen scenarios to discover new patterns. Optimization outcomes update arm set and priorities so the curriculum co-evolves with the harness. The harness-update operator \(\mathcal{O}\) is unchanged.

## When to Use
- Budgeted offline harness optimization where a fixed scenario order leaves unresolved failures on the table or wastes rollouts on repaired ones.

## When NOT to Use
- Production kernel → `method:omp2-harness`. Frozen-backbone RSI search → `method:rrsi`. Recursive harness rewrite → `method:aide2`. Weight post-train from routing traces → `method:neohorse-1`. Distill harness into weights → `method:harness-zero`.

## Relation to Existing SOTA
- Active plug-in on `task:agent-harness-runtime` and `task:agentic-rsi-routing-posttrain` beside RRSI / AIDE2 / Harness-Zero. Curriculum dimension, not a new kernel. Does **not** enter omp2 or NeoHorse `current_sota`.

## Gotchas & Failure Modes
- Gains are vs the *same* optimizer with a frozen schedule. Do not cite +4.4 / +7.5 as beating omp² or mini-SWE-agent.
- Category-level arms conflate distinct failures; scenario-level arms fragment recurring ones. Failure-pattern clustering is the method.
- Does not update model weights.
