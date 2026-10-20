---
id: task:outcome-only-long-horizon-agent-rl
type: task
title: "Outcome-Only Long-Horizon Agent RL"
domain: "post-training"
summary: "Train a long-horizon interactive agent from sparse end-of-task verification (or, when no checker exists, from rubric credit) without denser step rewards, SFT priors, or multi-agent scaffolding."
scope: "Policy training for multi-turn agents judged only at episode end, where the failure modes are signal starvation (all-success / all-fail groups) and policy drift on a small revisited task pool. Includes the outcome-blind rubric variant when no programmatic checker exists."
out_of_scope:
  - "Async straggler / tool-latency RL (SAO)"
  - "Folding a long tool/web/SWE trajectory into a small active context (FoldGRPO)"
  - "Single-turn dense math/code RLVR (CISPO)"
  - "Building or choosing a SWE harness rather than training a policy (mini-SWE-agent)"
  - "Production harness kernel (omp2)"
  - "Live-web multi-hop search-agent training (Iris)"
  - "Data/env construction for coding-agent RL from source code (CodeMidas)"
  - "Multi-stage agent continual learning (ACLArena)"
redirects:
  - when: "success-preserving agentic OPD overshoot (SPOD), not AppWorld coverage"
    to: "method:spod"
  - when: "just-in-time rubric training harness (HarnessRL), not CANOPY coverage"
    to: "method:harnessrl"
  - when: "tree-aware posterior self-distillation for long-horizon agent RL (TreeOPSD)"
    to: "method:treeopsd"
  - when: "Lean4 multi-level process rewards for SWE/terminal agent RL (Lean4AgenticRL)"
    to: "method:lean4-agentic-rl"
  - when: "executable oracle continuations from policy-reached states (SERO)"
    to: "method:sero"
  - when: "variable environment latency / async stragglers, not sparse-outcome coverage"
    to: "task:agentic-async-rl"
  - when: "the problem is context folding of a long tool trajectory, not the RL signal"
    to: "task:long-horizon-tool-agent"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "build an agent loop rather than train a policy"
    to: "task:software-engineering-agent-harness"
  - when: "production engine (rewind, sandbox, remote, TUI)"
    to: "task:agent-harness-runtime"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing)"
    to: "task:web-search-agent-rl"
  - when: "production post-train stack rather than sparse-outcome coverage"
    to: "task:frontier-rl-posttrain-stack"
  - when: "agentic RSI / routing-harness post-train, not AppWorld coverage"
    to: "task:agentic-rsi-routing-posttrain"
  - when: "noisy pairwise preference labels (PLC-DPO), not outcome-only agent RL"
    to: "task:direct-preference-alignment"
  - when: "data/env construction for coding-agent RL from source code"
    to: "task:coding-agent-rl-environment-construction"
  - when: "multi-stage agent capability stacking / continual learning"
    to: "task:agent-continual-learning"
  - when: "multi-turn agent OPD at pivotal early mistakes (prevent reverse-KL + recover forward-KL)"
    to: "method:pivotopd"
  - when: "act-first / reason-later multi-turn OPD (inverse dynamics + async full-response distill)"
    to: "method:actfirst-opd"
  - when: "branchy RLVR token cost; hindsight-divergence prefix reuse"
    to: "method:hdl"
  - when: "per-state shrinkage of step-level advantage for agentic RL (GiGPO-style groups)"
    to: "method:adastep"
  - when: "structured planning/subtask credit + local-context distillation for long-horizon agents"
    to: "method:scad"
  - when: "learning rubric rewards for rubric-based RL (vacuous credit)"
    to: "method:metarubric"
  - when: "hierarchical MoE routing control during agentic RL (operation-type experts)"
    to: "method:hierarchical-moe-routing-control"
  - when: "state-grounded on-policy distillation for multi-turn agents (matched interaction state, not student CoT)"
    to: "method:state-opd"
  - when: "matched-context group policy optimization (pairwise credit on sibling agent rollouts)"
    to: "method:mcgpo"
  - when: "hindsight-guided tree exploration and turn-level credit for multi-turn LLM agents"
    to: "method:treehca"
  - when: "branch-and-resample OPD at uncertain / teacher-disagreement tokens (protocol-boundary repair)"
    to: "method:branchopd"
  - when: "protocol-level rubrics so criteria cannot compensate (ProRubric)"
    to: "method:prorubric"
  - when: "Neyman prefix resampling on GiGPO-style agent groups (VSR)"
    to: "method:vsr"
  - when: "fork RL rollouts from the agent's own failure states (ReTerm)"
    to: "method:reterm"
  - when: "privileged representation OPSD after GRPO (PR-OPD / invisible advantage)"
    to: "method:pr-opd"
  - when: "action-level OPD without teacher token probabilities"
    to: "method:actionopd"
  - when: "single-rollout token credit via causal vs hindsight JSD (HP-RLVR)"
    to: "method:hp-rlvr"
  - when: "self-distillation methods vs GRPO on agent benches (no consistent win)"
    to: "paper:agentic-self-distill-reality"
current_sota:
  - method: method:canopy
    as_of: "2026-09-04"
    benchmark: "AppWorld Test-Normal / Test-Challenge TGC, Qwen3-14B (Feb 2026 leaderboard)"
    metric: "TGC mean@1"
    value: "86.9 / 67.6"
    notes: "CANOPY (2609.01245). Sparse outcome reward, n=32, KL-anchored on-policy. Does not replace SAO, FoldGRPO, CISPO, mini-swe-agent, or omp2-harness. DRACO is the outcome-blind rubric sibling, not a supersession."
methods:
  - method:spod
  - method:harnessrl
  - method:treeopsd
  - method:lean4-agentic-rl
  - method:sero
  - method:actionopd
  - method:hp-rlvr
  - method:prorubric
  - method:vsr
  - method:reterm
  - method:pr-opd
  - method:branchopd
  - method:state-opd
  - method:mcgpo
  - method:treehca
  - method:canopy
  - method:draco
  - method:sao
  - method:foldgrpo
  - method:cispo
  - method:mini-swe-agent
  - method:iris
  - method:t1-terminal-rl
  - method:evors
  - method:ddo
  - method:retireopd
  - method:actobs
  - method:codemidas
  - method:aclarena
  - method:pivotopd
  - method:actfirst-opd
  - method:hdl
  - method:adastep
  - method:scad
  - method:metarubric
  - method:hierarchical-moe-routing-control
last_reviewed: '2026-10-20'
tags:
  - post-training
  - agentic
  - outcome-only
  - long-horizon
  - canopy
  - draco
---

# Outcome-Only Long-Horizon Agent RL

## Problem Definition
Train a multi-turn interactive policy (AppWorld-style application operation, SWE repair, similar) when the only trustworthy label is end-of-episode verification — or, when no checker exists, a rubric scored once per trajectory. The typical failure of nearby methods is compensating around the policy (dense step rewards, SFT priors, skill libraries, orchestration) instead of restoring coverage and stopping drift.

Two siblings share this task and are not substitutes:
- **CANOPY**: programmatic checker exists; scale same-task exploration and KL-anchor so sparse outcome RL suffices.
- **DRACO**: no programmatic checker; dynamic rubrics plus closed-form step credit redistribution.

## Evaluation Protocol
- **Primary Benchmarks**: AppWorld TGC/SGC (Test-Normal, Test-Challenge); SWE-bench Verified resolve rate when transferring the same design principles; τ-bench for outcome-blind transfer.
- **Evaluation Pitfalls**: Do not mix training-free frontier harness numbers (HCL-GP / ASSAY) with trained-policy TGC. Do not treat AppWorld leaderboard wins as a reason to drop SAO for async training or mini-SWE-agent for the harness.

## SOTA Recommendation (as of 2026-09-04)
- **Primary Method (checker exists)**: **CANOPY** (`method:canopy`, `paper:canopy` `arXiv:2609.01245`).
- **Outcome-blind / no checker**: **DRACO** (`method:draco`, `paper:draco` `arXiv:2609.04094`). Active, does not replace CANOPY when a verifier exists.
- **Not This Task**: `method:sao` remains async-straggler RL; `method:foldgrpo` remains trajectory folding; `method:cispo` remains dense Pass@1; `method:mini-swe-agent` remains the harness; `method:omp2-harness` remains the production engine; `method:iris` remains live-web search-agent training; `method:miles` remains the frontier post-train stack; `method:neohorse-1` remains routing-harness RSI.
- **Optional 122B terminal-MoE recipe (not this first hop)**: `method:t1-terminal-rl` (`arXiv:2609.11042`) on slime. Terminal-Bench 2.1 43.8%→64.0%. Does not replace CANOPY, SAO, or Miles.
- **Active open-ended reward-system evolution (not this first hop)**: `method:evors` (`arXiv:2609.12459`) co-evolves a reward model from on-policy traces. Does not replace CANOPY or DRACO.
- **Active successful-strategy coverage regularizer (not this first hop)**: `method:ddo` (`arXiv:2609.10052`). Preference-pair primary; mention here for open-ended coverage. Does not replace CANOPY or DRACO.
- **Active privileged self-OPD then retirement (not this first hop)**: `method:retireopd` (`arXiv:2609.20784`). Adaptive Retirement drops the privileged teacher when discrepancy stops shrinking and the student hits a fraction of teacher success, then pure RL. ALFWorld +14.1–18.8% SR vs RL; WebShop +11.8–19.0%. Does not replace CANOPY, SAO, OPD, or VISTA.
- **Related SFT init (not this first hop)**: `method:actobs` (`arXiv:2609.20715`) on `task:agentic-async-rl` — observation-token SFT before GRPO. Does not replace CANOPY.
- **Not this task (coding-agent RL env construction)**: `method:codemidas` (`arXiv:2609.22068`) on `task:coding-agent-rl-environment-construction` — source-code-only env factory then GRPO. Does not replace CANOPY.
- **Not this task (multi-stage agent continual learning)**: `method:aclarena` (`arXiv:2609.23989`) on `task:agent-continual-learning`. Sequential capability stacking, not AppWorld TGC.
- **Optional multi-turn agent OPD at pivotal mistakes (not this first hop)**: `method:pivotopd` (`arXiv:2609.40285`). Reverse-KL prevent + forward-KL recovery. Strongest average on ALFWorld/WebShop/Search-QA; +3.2 SWE-Bench Verified. Does not replace CANOPY or OPD.
- **Optional act-first multi-turn OPD (not this first hop)**: `method:actfirst-opd` (`arXiv:2609.36608`). Inverse dynamics + async full-response distill. 2.3× / 1.8× / 4.9× wall-clock vs Vanilla OPD on ALFWorld/WebShop/ScienceWorld. Does not replace CANOPY or OPD.
- **Optional per-state step-advantage shrinkage (not this first hop)**: `method:adastep` (`arXiv:2610.03223`) on `task:tool-agent-segment-credit`. Mention here for long-horizon agent RL. Does not replace CANOPY or SLCA-GRPO.
- **Optional structured planning/subtask credit (not this first hop)**: `method:scad` (`arXiv:2610.03372`). Qwen3-4B text Avg 46.10 vs ATOD 41.62 / FoldGRPO 39.60. Does not replace CANOPY or PivotOPD.
- **Optional learned rubric rewards (not this first hop)**: `method:metarubric` (`arXiv:2610.02824`). Qwen3-4B PubMedQA 78.40 vs GRPO 72.40. Code metarubric/metarubric. Does not replace CANOPY or DRACO.
- **Related branchy RLVR token-cost plug-in (not this first hop)**: `method:hdl` (`arXiv:2609.36864`) on `task:math-code-rl-dense`. Hindsight-divergence prefix reuse; ScienceWorld-style agent gains. Does not replace CANOPY.
- **Optional state-grounded multi-turn OPD (not this first hop)**: `method:state-opd` (`arXiv:2610.13238`) matches teacher continuations on the objective interaction state. Qwen3-4B macro 31.74 vs 26.07. No public code. Does not replace CANOPY, OPD, PivotOPD, or ActFirst-OPD.
- **Optional matched-context GPO (not this first hop)**: `method:mcgpo` (`arXiv:2610.13755`) pairwise credit on matched sibling supports. +3.96 / +5.16pp WebShop Qwen3-4B/8B vs GraphGPO. No public code. Does not replace CANOPY or SAO.
- **Optional hindsight-guided tree credit (not this first hop)**: `method:treehca` (`arXiv:2610.12828`) branches on reference-answer likelihood jumps and backups turn advantages. GitHub TheBlackCat22/TreeHCA 404. Does not replace CANOPY or PACT.
- **Optional branch-and-resample OPD (not this first hop)**: `method:branchopd` (`arXiv:2610.13481`) on `task:student-distillation`. Protocol-boundary repair on ALFWorld/WebShop. +13.8pp ALFWorld vs vanilla OPD. Does not replace CANOPY or OPD.
- **Optional protocol-level rubrics (not this first hop)**: `method:prorubric` (`arXiv:2609.38847`). HealthBench 4B appropriateness 36.8 vs Rubric-RL 26.0. Code Estrellajer/ProRubric. HF Daily 2026-10-14. Does not replace CANOPY, DRACO, or MetaRubric.
- **Related Neyman prefix resampling (not this first hop)**: `method:vsr` (`arXiv:2610.15888`) on `task:math-code-rl-dense`. GiGPO+VSR BabyAI 47.6 vs 30.4. Does not replace CANOPY.
- **Related recovery-fork terminal RL (not this first hop)**: `method:reterm` (`arXiv:2610.18484`) on `task:coding-agent-rl-environment-construction`. Does not replace CANOPY or CodeMidas.
- **Related privileged representation OPSD (not this first hop)**: `method:pr-opd` (`arXiv:2609.36642`) on `task:privileged-teacher-opsd`. +4.7 ALFWorld / +11.7 WebShop after GRPO. Does not replace CANOPY or VISTA.
- **Optional action-level OPD (not this first hop)**: `method:actionopd` (`arXiv:2610.19820`) on `task:student-distillation`. Black-box teacher, no token logp. Qwen3-4B/8B +3.3–6.9pp OOD. Code thu-nics/ActionOPD. Does not replace CANOPY or OPD.
- **Related single-rollout hindsight token credit (not this first hop)**: `method:hp-rlvr` (`arXiv:2610.20497`) on `task:math-code-rl-dense`. G=1 causal vs hindsight JSD. ALFWorld GRPO zero-grad 43.2%/49.0% vs none. Distinct from HDL. Does not replace CANOPY or CISPO.
- **Gotcha (self-distillation vs GRPO on agent benches)**: `paper:agentic-self-distill-reality` (`arXiv:2610.19789`). 10 methods, 132 runs, 12124.4 H800-h; no method consistently beats GRPO. Does not retarget CANOPY.

- **Optional executable oracle continuations**: `method:sero` (`arXiv:2610.19397`). 1.5B GraphGPO ALFWorld 90.63/88.02→95.83/91.67. No public code. Does not replace CANOPY.
- **Optional tree-aware posterior self-distill**: `method:treeopsd` (`arXiv:2610.23181`). Qwen3-30B-A3B Deep Research +4.97 vs GRPO. Does not replace CANOPY.
- **Optional Lean4 process-reward agent RL**: `method:lean4-agentic-rl` (`arXiv:2610.22448`). LAR-27B TB2.1 77.3%. Does not replace CANOPY or Terminal-RSI.
- **Related success-preserving agentic OPD (not this coverage default)**: `method:spod` (`arXiv:2610.25034`) on `task:student-distillation`. ALFWorld overshoot then erosion without SPOD. Does not replace CANOPY.
- **Related JIT rubric harness (not this coverage default)**: `method:harnessrl` (`arXiv:2610.26426`) on `task:agent-harness-runtime`. Does not replace CANOPY or DRACO.
