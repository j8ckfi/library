---
id: method:codemidas
type: method
title: "CodeMidas"
category: "training-systems"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains the outcome-only first hop; CodeMidas constructs coding RL environments from source code"
    use_instead: "method:canopy"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains async RL; CodeMidas is env construction, not straggler replay"
    use_instead: "method:sao"
  - when: "GitHub issue to patch / SWE harness"
    reason: "mini-SWE-agent remains the loop; CodeMidas is data/env construction for coding-agent RL"
    use_instead: "method:mini-swe-agent"
  - when: "production post-train engine (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the frontier stack; CodeMidas is not a trainer"
    use_instead: "method:miles"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "category see-saw on heterogeneous SWE RL (already-executable tasks)"
    reason: "CodeMidas constructs environments from source; Category-Aware SWE Experts train on already-executable SWE tasks"
    use_instead: "task:swe-agent-category-expert-rl"
  - when: "mechanism-first stateful tool envs (not OSS source)"
    reason: "CodeMidas is source-code coding RL env construction; VHD-Play starts from solved math mechanisms"
    use_instead: "task:mechanism-grounded-agentic-rl-env"
assumptions:
  - "Source code is the only task-specific input. Agents explore implemented functionality, write behavioral specs, build execution-grounded tests, then filter."
  - "Paper trains MiMo-V2.5 with GRPO, binary execution rewards, batch 32, 32 rollouts per task, on 5,545 tasks / 3,185 repos / 23 languages."
  - "Project page https://mimo.xiaomi.com/rl/ is a live MiMo RL dashboard as of 2026-09-21. No public GitHub found."
last_reviewed: "2026-09-24"
papers:
  - paper:codemidas
recipes:
  - recipe:codemidas
claims:
  - benchmark: "DeepSWE v1.1 pass rate, MiMo-V2.5 GRPO"
    metric: "pass rate"
    value: "21.7"
    baseline: "initial MiMo-V2.5 10.0"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22068"
    notes: "+11.7 pp. Figure 5. Not an AppWorld / CANOPY bake-off."
  - benchmark: "ProgramBench Almost Solved, MiMo-V2.5 GRPO"
    metric: "Almost Solved (≥95% tests)"
    value: 21.5
    baseline: "initial MiMo-V2.5 4.5"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22068"
    notes: "+17.0 pp whole-program construction."
  - benchmark: "Terminal-Bench v2.1 pass rate, MiMo-V2.5 GRPO"
    metric: "pass rate"
    value: "72.2"
    baseline: "initial MiMo-V2.5 63.7"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22068"
    notes: "+8.5 pp. SWE-bench Pro 50.3→54.4; RepoZero C2Rust 40.5→51.8."
tags:
  - post-training
  - agentic
  - coding-rl
  - environments
  - codemidas
  - active
---

# CodeMidas

## Method Overview
CodeMidas turns implemented OSS functionality into executable coding-agent RL environments using source code as the only task-specific input. Four stages:

1. **Task design**: explore public entry points, remove the core implementation, write a behavioral statement, keep a reference solution.
2. **Test construction**: map statement requirements to tests whose expected values come from executing the original code.
3. **Execution consistency**: starting codebase must fail twice; reference must pass four times.
4. **Post-rollout filtering**: adversarial leakage, solution-audit of verifier verdicts, keep only tasks with both successful and failed screening rollouts.

The paper then trains MiMo-V2.5 with GRPO and binary execution rewards. The host loss is GRPO; CodeMidas is the environment factory.

## When to Use
- You need a large, execution-verified coding-agent RL task pool and you have OSS codebases rather than issues/PRs/tests as the seed.

## When NOT to Use
- AppWorld coverage → `method:canopy`. Async stragglers → `method:sao`. SWE loop → `method:mini-swe-agent`. Production engine → `method:miles`. Pass@1 → `method:cispo`. Category-aware SWE expert RL → `method:category-aware-swe-experts`. Mechanism-first tool envs → `method:vhd-play`.

## Relation to Existing SOTA
- Active first hop on `task:coding-agent-rl-environment-construction` only (method status active; listed in that task's `current_sota`). Mentions on `task:outcome-only-long-horizon-agent-rl`, `task:agentic-async-rl`, and `task:software-engineering-agent-harness`. Does **not** replace `method:canopy`, `method:sao`, `method:miles`, or `method:mini-swe-agent`. Mechanism-grounded tool envs are `method:vhd-play` on `task:mechanism-grounded-agentic-rl-env`.

## Gotchas & Failure Modes
- Unfiltered scale loses to a smaller cleaned pool: high-quality 3k beats vanilla 8k on SWE-bench Pro, DeepSWE, and CodeMidas Val.
- The verifier stays outside the solver environment until grading. Residual leakage (compiled artifacts, caches) is a construction bug, not a training hyperparameter.
- No public trainer or dataset GitHub as of 2026-09-21.
