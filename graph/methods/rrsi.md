---
id: method:rrsi
type: method
title: "RRSI"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "production harness kernel (rewind, sandbox, remote, TUI / journal → session DOM)"
    reason: "omp² remains the architecture spec; RRSI regularizes harness search around a frozen backbone"
    use_instead: "method:omp2-harness"
  - when: "routing-harness RSI post-train of model weights"
    reason: "NeoHorse-1 remains that first hop; RRSI does not update weights"
    use_instead: "method:neohorse-1"
  - when: "token-efficient Pi harness mechanisms from auto-research"
    reason: "SoL-Pi is a Pi extension found by harness RSI; RRSI is regularized search against evolve-set overfitting"
    use_instead: "method:sol-pi"
  - when: "SWE-bench start/eval loop or GitHub issue → patch"
    reason: "mini-SWE-agent remains the locked ranking scaffold"
    use_instead: "method:mini-swe-agent"
  - when: "full expert-trajectory SFT after model-specific harness evolution"
    reason: "That imitation is the harness-onpolicy-correction failure mode"
    use_instead: "method:harness-onpolicy-correction"
assumptions:
  - "Frozen backbone. Search edits prompts, control flow, tools, skills, memory, context, sub-agents. Paper: Claude Opus 4.8 / Gemini 3.5 Flash as search policy; Vertex AI."
  - "One evolve suite per domain; transfer is measured on held-out and OOD benches with the harness frozen."
  - "Code: google-research/rrsi. Candidates live in git worktrees off evolve/<domain>."
last_reviewed: "2026-09-22"
papers:
  - paper:rrsi
recipes:
  - recipe:rrsi
claims:
  - benchmark: "Terminal-Bench 2.1 evolve split, Gemini 3.5 Flash search policy"
    metric: "pass rate"
    value: "78.7"
    baseline: "unevolved harness H0 64.6 (+14.1)"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24972"
    notes: "Table 3. SWE-bench Verified OOD 76.8→79.0. Claude Opus 4.8: TB 74.2→80.2, SWE-Verified 82.0→83.8."
  - benchmark: "Five OOD / held-out splits (SWE-Verified, Harvey LAB ID, JobBench, GDPval, APEX-Agents, Frontier-Eng)"
    metric: "gain vs H0"
    value: "up to +4.7 points on OOD agentic benches; Frontier-Eng +4.3 Medal (24.3% rel)"
    baseline: "unevolved H0; unregularized evolution often below H0 OOD"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24972"
    notes: "Eight benches, three domains. ~30% fewer policy tokens than unregularized evolution. Does not replace omp2 / NeoHorse-1 / SoL-Pi / mini-SWE-agent."
tags:
  - agents
  - agent-harness
  - rsi
  - rrsi
  - active
---

# RRSI

## Method Overview
RRSI is regularized recursive self-improvement of an **agent harness** with a frozen backbone. Unregularized propose-and-select RSI memorizes the evolve split. RRSI keeps every harness component editable and constrains how the search uses finite noisy feedback.

Proposal side: temporally annealed edit budget \(b_t\) (how many independent edits one candidate may bundle), full edit-history conditioning so falsified hypotheses are not redrawn, and stall-triggered exploration of untried components. Selection side: a critic screens benchmark-specific / leaking diffs before they are scored; a noise-adjusted floor, cost rule, and pruner drop tiny, expensive, or obsolete machinery. Accepted candidates fast-forward a git branch; the incumbent is always a commit.

This is harness search, not omp²'s kernel spec, not NeoHorse-1's routing-guided weight update, not SoL-Pi's Pi mechanisms, and not mini-SWE-agent's issue-to-patch loop.

## When to Use
- You are evolving a harness against a finite evolve set and OOD transfer / anti-memorization is the complaint.

## When NOT to Use
- Production kernel → `method:omp2-harness`. Routing-harness weight post-train → `method:neohorse-1`. Pi token-efficiency extension → `method:sol-pi`. Issue → patch → `method:mini-swe-agent`. Evolved-harness full-traj SFT → `method:harness-onpolicy-correction`.

## Relation to Existing SOTA
- Active mention on `task:agent-harness-runtime` and `task:agentic-rsi-routing-posttrain`. Does **not** enter `current_sota`. Does **not** replace `method:omp2-harness`, `method:neohorse-1`, `method:sol-pi`, `method:mini-swe-agent`, or `method:harness-onpolicy-correction`.

## Gotchas & Failure Modes
- Backbone stays frozen. If you need weight updates from routing traces, that is NeoHorse-1.
- Noise band \(\delta\) is instance-specific (`rrsi.json`: 0.017 / 0.004 / 0.020). Recalibrate if the verifier variance changes.
- Critic rejects evolve-set entity names and answers. Generic prompt/tool edits remain valid.
