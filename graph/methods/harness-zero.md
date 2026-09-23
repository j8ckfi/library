---
id: method:harness-zero
type: method
title: "Harness-Zero"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "production harness kernel (rewind, sandbox, remote, TUI)"
    reason: "omp² remains the kernel spec; Harness-Zero distills harness behaviors into weights"
    use_instead: "method:omp2-harness"
  - when: "routing-harness RSI post-train of model weights from harness traces"
    reason: "NeoHorse-1 remains that first hop; Harness-Zero is agent-as-harness SFT under a fixed target harness"
    use_instead: "method:neohorse-1"
  - when: "single-teacher text distillation without a harness action-space mismatch"
    reason: "OPD remains the distill default; this is harness-behavior transfer, not token reverse-KL"
    use_instead: "method:opd"
  - when: "multi-teacher student distillation"
    reason: "Open-MOPD remains multi-teacher distill"
    use_instead: "method:open-mopd"
  - when: "GitHub issue to patch / SWE harness"
    reason: "mini-SWE-agent remains the loop; the paper uses it as the *target* harness, not a ranking default"
    use_instead: "method:mini-swe-agent"
  - when: "variable environment latency / async stragglers"
    reason: "SAO remains async RL"
    use_instead: "method:sao"
  - when: "programmatic checker AppWorld coverage / anti-drift"
    reason: "CANOPY remains outcome-only agent RL; AppWorld here is a distillation eval, not TGC protocol"
    use_instead: "method:canopy"
  - when: "recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)"
    reason: "Harness-Zero distills harness behaviors into weights under a fixed target; AIDE2 rewrites the harness"
    use_instead: "method:aide2"
assumptions:
  - "Target harness h is a fixed mini-SWE-agent-style bash loop. Evolved student harness h* is adapted into a private reference K for the harnessing agent. Review discussion is not visible to the student."
  - "Paper: Qwen3.5-9B SFT student; SpreadsheetBench Verified / AppWorld / USPTO Retrosynthesis. Harbor Docker sandboxes. Tinker SFT recipe."
  - "Code: metaevo-ai/harness-zero. Weights: Hugging Face metaevo-ai."
last_reviewed: "2026-09-23"
papers:
  - paper:harness-zero
recipes:
  - recipe:harness-zero
claims:
  - benchmark: "Qwen3.5-9B macro task success, specialized harness removed at deploy"
    metric: "macro-average success"
    value: "44.3%"
    baseline: "mini-SWE-agent target h 23.3%; base + evolved h* 41.7%"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24974"
    notes: "SpreadsheetBench 44.0 / AppWorld 58.9 / USPTO 30.0. +21.0 pp vs h-only base. Not an omp2 / OPD / NeoHorse bake-off."
  - benchmark: "Frontier LLMs, same evolved harness, six benchmark–model settings"
    metric: "average success"
    value: "agent-as-harness 81.1%"
    baseline: "code-as-harness / meta-harness 78.1%; mini-SWE-agent 68.6%"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24974"
    notes: "No training. Agent-as-harness outperforms mounting the evolved code harness."
  - benchmark: "Harness-exclusive behavior recovery, 28 patterns, three domains"
    metric: "average recovery"
    value: "82.3%"
    baseline: "behaviors present under h* and absent from the base under h"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.24974"
    notes: "Memory, skill, tool, and middleware patterns."
tags:
  - agents
  - agent-harness
  - distillation
  - harness-zero
  - active
---

# Harness-Zero

## Method Overview
Harness-Zero distills behaviors induced by an optimized harness into model weights so the gains survive under a **fixed target harness**. Three stages:

1. Evolve a student-side harness \(h^\star\) on training tasks; adapt it into a private reference harness \(K\) for a separate harnessing agent (middleware rules become review-time warnings).
2. The student proposes under the target harness \(h\) (mini-SWE-agent, one bash tool). The harnessing agent PASS/REPLACE-corrects the reply in \(h\)'s action space before execution. Review stays private.
3. SFT on reviewed trajectories (mask reviewer-perspective reasoning). Deploy under \(h\) alone: drop \(h^\star\), \(K\), and the harnessing agent.

Agent-as-harness is the mapping across mismatched action spaces. Code-as-harness (mounting \(h^\star\) directly) is the paper's weaker alternative. This is **not** OPD, not NeoHorse-1 routing-guided OPD, not omp², not SAO, and not CANOPY.

## When to Use
- An optimized harness helps at train time but you must ship one fixed target harness, and source/target action spaces do not match.

## When NOT to Use
- Kernel spec → `method:omp2-harness`. Routing RSI post-train → `method:neohorse-1`. Plain text OPD → `method:opd`. Multi-teacher → `method:open-mopd`. Issue → patch → `method:mini-swe-agent`. Async stragglers → `method:sao`. AppWorld TGC → `method:canopy`. Recursive harness self-rewrite → `method:aide2`.

## Relation to Existing SOTA
- Active first hop on `task:harness-distillation` only (method status active; listed in that task's `current_sota`; `sota_for` stays empty). Does **not** retarget `method:omp2-harness`, `method:neohorse-1`, `method:opd`, `method:open-mopd`, `method:sao`, or `method:canopy`. Recursive self-rewrite of the harness codebase is `method:aide2`.

## Gotchas & Failure Modes
- Trajectories collected under \(h^\star\) are not valid SFT targets under \(h\). That action-space mismatch is the reason for agent-as-harness.
- Direct stronger-model traces, \(h^\star\) traces, review without \(K\), and answer-only review are weaker supervision (30% vs 3–15% in the paper ablation).
- AppWorld numbers here are distillation eval, not CANOPY TGC protocol.
