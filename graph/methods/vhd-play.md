---
id: method:vhd-play
type: method
title: "VHD-Play (Verifiable Hidden Dynamics Play)"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "source code is the only task-specific input for coding RL envs"
    reason: "CodeMidas remains the source-code env factory; VHD-Play starts from solved math mechanisms"
    use_instead: "method:codemidas"
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains the outcome-only first hop; VHD-Play constructs mechanism-grounded envs"
    use_instead: "method:canopy"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL; VHD-Play is env construction, not straggler replay"
    use_instead: "method:sao"
  - when: "GitHub issue to patch / SWE harness"
    reason: "mini-SWE-agent remains the loop"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Sample and solve a mathematical model family first. A setter then renders stateful tools whose dynamics and episode reward inherit from that solution. The player does not see parameters or z_theta."
  - "Paper trains Qwen3.6-35B-A3B on three mechanism families; 3,300 admitted environments at cents each."
  - "No public GitHub as of 2026-09-24."
last_reviewed: "2026-09-24"
papers:
  - paper:vhd-play
recipes:
  - recipe:vhd-play
claims:
  - benchmark: "five-family agentic diagnostic, Qwen3.6-35B-A3B"
    metric: "mean agentic score"
    value: "0.204→0.815"
    baseline: "untrained Qwen3.6-35B-A3B 0.204"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.27321"
    notes: "Train on three families; evaluate five. Does not replace CodeMidas."
  - benchmark: "E-Commerce Bench 365-day storefront"
    metric: "bankruptcy-free completion vs Qwen3.7-Max"
    value: "exceeds Qwen3.7-Max; 3.4× base ending balance; zero bankruptcy"
    baseline: "Qwen3.7-Max; untrained Qwen3.6-35B-A3B"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.27321"
    notes: "External transfer. Learnable gap is stateful interaction, not written-out solving."
tags:
  - post-training
  - agentic
  - environments
  - vhd-play
  - active
---

# VHD-Play (Verifiable Hidden Dynamics Play)

## Method Overview
VHD-Play synthesizes long-horizon agentic RL environments by solving a mathematical mechanism first, then wrapping its executable dynamics as stateful tools. The outcome rule \(\mathcal{R}_\theta\) is fixed from the solver's reference \(z_\theta=(u^*(\theta),u_0(\theta))\) before the setter ever emits an interface. Episode reward is a clipped improvement over the default policy:

\[
r(\pi;\theta)=\operatorname{clip}_{[0,1]}\!\left(\frac{u(\pi;\theta)-u_0(\theta)}{u^*(\theta)-u_0(\theta)}\right).
\]

The player probes and commits under a shared turn budget; parameters stay hidden. CodeMidas remains the source-code coding-env factory. This is the mechanism substrate.

## When to Use
- You need diverse, cheap, verifier-grounded agentic RL environments and the seed is a solved math/OR mechanism rather than an OSS codebase.

## When NOT to Use
- Source-code coding RL envs → `method:codemidas`. AppWorld coverage → `method:canopy`. Async stragglers → `method:sao`. SWE loop → `method:mini-swe-agent`.

## Relation to Existing SOTA
- Active first hop on `task:mechanism-grounded-agentic-rl-env` only (method status active; listed in that task's `current_sota`; `sota_for` stays empty). Does **not** replace `method:codemidas`, `method:canopy`, `method:sao`, `method:miles`, or `method:mini-swe-agent`.

## Gotchas & Failure Modes
- Written-out QA of the same \(M(\theta)\) is the wrong eval. The paper's gap is stateful interaction.
- No public trainer or env GitHub as of 2026-09-24.
- The setter sees \((\theta,c)\); the policy must not. Leaking parameters collapses the task to written-out solving.
