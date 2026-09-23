---
id: method:aide2
type: method
title: "AIDE2"
category: "agent-recursion"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "production harness kernel (rewind, sandbox, remote, TUI)"
    reason: "omp² remains the kernel spec; AIDE2 is recursive self-rewrite of a research-agent harness"
    use_instead: "method:omp2-harness"
  - when: "regularized harness RSI (annealed edit budget / anti-memorization critic on a frozen backbone)"
    reason: "RRSI searches harness edits around a frozen model; AIDE2 accepts a rewrite as the next incumbent agent"
    use_instead: "method:rrsi"
  - when: "routing-harness RSI post-train of model weights from harness traces"
    reason: "NeoHorse-1 remains that first hop; AIDE2 does not update weights from routing traces"
    use_instead: "method:neohorse-1"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness"
    reason: "Harness-Zero is agent-as-harness SFT; AIDE2 keeps improving the harness code itself"
    use_instead: "method:harness-zero"
assumptions:
  - "The object of optimization is the research agent's own code. Inner-loop agents run at a fixed per-task dollar budget. Outer-loop selection uses a private grade the inner agent never sees."
  - "Paper: 8-day run, 100 nodes, seven accepted rewrites. Outer loop Claude Opus 4.7; inner loop Gemini 3 Flash. Baseline AIDE_human is Weco's production research agent."
  - "No public GitHub as of 2026-09-23."
last_reviewed: "2026-09-23"
papers:
  - paper:aide2
recipes:
  - recipe:aide2
claims:
  - benchmark: "AIDE2 selection-benchmark private grade, 8-day autonomous run"
    metric: "incumbent grade g(a*)"
    value: "0.703 → 0.778 (7 accepted rewrites)"
    baseline: "AIDE_human 0.749 under the same grade"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.26457"
    notes: "Figure 2. Eventually beats AIDE_human on the selection benchmark. Not an omp2 / RRSI / NeoHorse bake-off."
  - benchmark: "Held-out kernel-engineering reward hacking (38 pairs)"
    metric: "reward-hacking rate"
    value: "32% (AIDE_85)"
    baseline: "AIDE_0 55%; AIDE_human 39%"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.26457"
    notes: "Not an explicit training objective. Transfer also reported on ALE / MLE / FML / WeatherBench 2."
tags:
  - agents
  - agent-harness
  - rsi
  - aide2
  - active
---

# AIDE2

## Method Overview
\(\mathrm{AIDE}^{2}\) is recursive self-improvement at the **harness layer** of an AI research agent. The inner loop edits task code against a public metric under a fixed budget. The outer loop rewrites the inner-loop agent's own code. A candidate is kept only if its private held-out grade \(g(a)\) beats the incumbent. That accepted rewrite **is** the next agent.

This is true recursive harness RSI, not RRSI's regularized search around a frozen backbone, not NeoHorse-1's routing-guided weight update, not omp²'s kernel spec, and not Harness-Zero's distillation into weights under a fixed target harness.

## When to Use
- You can grade research-agent harness rewrites on a held-out suite and want the accepted code to become the next incumbent.

## When NOT to Use
- Production kernel → `method:omp2-harness`. Regularized evolve-set anti-memorization search → `method:rrsi`. Weight update from routing traces → `method:neohorse-1`. Weight distillation of harness behaviors → `method:harness-zero`.

## Relation to Existing SOTA
- Active mention on `task:agent-harness-runtime` and `task:agentic-rsi-routing-posttrain`. Does **not** enter `current_sota`. Does **not** replace `method:omp2-harness`, `method:rrsi`, `method:neohorse-1`, `method:sol-pi`, or `method:harness-zero`.

## Gotchas & Failure Modes
- No public GitHub as of 2026-09-23. Reimplement the bi-level loop; do not invent an omp2 or NeoHorse replacement.
- Inner-loop public reward and outer-loop private grade must stay decoupled or the inner agent can optimize the selection signal.
- Gains on the selection benchmark are first-order; the paper's transfer claim is the four external benches, including OOD WeatherBench 2.
- Using a discovered agent as the outer-loop rewriter is noisy; the paper cannot distinguish it from the strong human baseline there.
