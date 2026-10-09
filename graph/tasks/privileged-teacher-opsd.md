---
id: task:privileged-teacher-opsd
type: task
title: "Privileged-Teacher On-Policy Self-Distillation"
domain: "post-training"
summary: "On-policy self-distillation where a same-size teacher is privileged with a gold reference solution and a deterministic outcome verifier, rather than a larger frozen teacher model."
redirects:
  - when: "rollout-free step-aligned privileged distillation of a reference solution (SAPD)"
    to: "method:sapd"
  - when: "hindsight-to-foresight distillation when verifier groups are silent (SRD)"
    to: "method:srd"
  - when: "privileged-context content (demo vs feedback vs rephrase) as OPSD drift, not a trainer"
    to: "method:privileged-context-drift"
  - when: "outcome-guided FKL/RKL OPSD with entropy prefix cutoff"
    to: "method:og-opsd"
  - when: "OPSD entropy overshoot (student entropy past the teacher; exemplar-guided + entropy-aware KL)"
    to: "method:e2-opsd"
  - when: "TSD calibration of teacher–student discrepancy during OPD (not teacher update)"
    to: "method:cal-opd"
  - when: "Adaptive Retirement of a privileged self-OPD teacher then pure agent RL"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "privileged teacher co-evolves with the student (DCE) plus shorter verified rewrites (SRCL)"
    to: "method:dce-srcl"
  - when: "privileged OPSD gains collapse at scale; verified on-policy scaffolds"
    to: "method:oasis"
  - when: "MLLM privileged OPSD with textual spatial guidance from synthetic scenes (not crop-zoom teachers)"
    to: "method:where-opd"
  - when: "neighborhood expert privileged OPSD (frozen local perturbations)"
    to: "method:n-opsd"
  - when: "MCMC projection sampling of expert traces then ordinary SFT (not a privileged-teacher update)"
    to: "method:sampling-sft"
  - when: "adaptive iterative error-to-repair guidance for OPSD"
    to: "method:air-opd"
  - when: "root-cause diagnosis of the student's own failed reasoning then differentiated prefix/error distillation"
    to: "method:rc-opd"
current_sota:
  - method: method:vista
    as_of: "2026-08-31"
    benchmark: "AIME24 / AIME25 / HMMT25 Avg@12 (Qwen3-1.7B/4B/8B instruct)"
    metric: "Avg@12 accuracy"
    value: "VISTA 44.0 / 64.3 / 66.9 vs OPSD 43.4 / 63.6 / 64.8 vs GRPO 37.7 / 62.7 / 64.0"
    notes: "VISTA (2608.28306) keeps the OPSD student update and adapts the privileged teacher on verified rollouts at top-k teacher-first KL positions."
methods:
  - method:sapd
  - method:srd
  - method:privileged-context-drift
  - method:og-opsd
  - method:e2-opsd
  - method:vista
  - method:opd
  - method:opdvr
  - method:u-opsd
  - method:flowbalance
  - method:verpo
  - method:opsd-collapse-review
  - method:nsd
  - method:scope-opsd
  - method:retireopd
  - method:cal-opd
  - method:dce-srcl
  - method:oasis
  - method:where-opd
  - method:n-opsd
  - method:sampling-sft
  - method:air-opd
  - method:rc-opd
last_reviewed: "2026-10-09"
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - vista
---

# Privileged-Teacher On-Policy Self-Distillation

## Problem Definition
Train a problem-only student on its own rollouts using dense token-level targets from a same-size teacher that also sees a gold reference solution. The teacher is a privileged copy of the student, not a larger frozen model. A deterministic outcome verifier is available. Vanilla OPSD treats that privileged distribution as a fixed target at every student prefix; the teacher can then over-support reference-specific tokens or suppress valid student continuations.

## Evaluation Protocol
- **Primary Benchmarks**: AIME 2024, AIME 2025, HMMT 2025 Avg@12 on Qwen3 instruct models.
- **Evaluation Pitfalls**: Do not treat this task as single-teacher student distillation from a frontier model (`task:student-distillation` / `method:opd`) or as OPD+RLVR with an external teacher (`task:distill-reasoner-verifier` / `method:opdvr`).

## SOTA Recommendation (as of 2026-09-08)
- **Primary Method**: **VISTA** (`method:vista`, `paper:vista` `arXiv:2608.28306`) for verifier-informed student-to-teacher adaptation on privileged-teacher OPSD.
- **Not This Task**: `method:opd` remains the single-teacher student-distillation default; `method:opdvr` remains the OPD+RLVR default; `method:u-opsd` remains the unlabeled/no-GT default.
- **Adjacent inner-loop (not this method)**: `method:flowbalance` uses privileged hindsight as a stopped trajectory-balance feature, not a teacher update. VISTA stays this task's first hop.
- **Optional evidence-regularized sibling**: `method:verpo` (`arXiv:2609.06100`). Treats privileged evidence as a proposal on an outcome objective. Does not replace VISTA or CISPO.
- **Collapse playbook (survey)**: `method:opsd-collapse-review` (`arXiv:2608.25936`). Three levers; no code. Does not replace VISTA.
- **Evidence (privileged-context content vs source)**: `method:privileged-context-drift` (`arXiv:2610.07842`). Content (demo vs feedback vs rephrase) drives KL 5.1× more than source. Niche; not a trainer. Does not replace VISTA.
- **Actionable anti-collapse trainer (not this first hop)**: `method:nsd` (`arXiv:2609.11699`). Diverges from a self-generated negative condition instead of imitating privileged traces. Active sibling. VISTA stays this task's first hop.
- **Optional Fisher-subspace OPSD auxiliary (not this first hop)**: `method:scope-opsd` (`arXiv:2609.12579`). Projects the privileged residual onto a frozen rank-64 Fisher-sensitive subspace; matched Random control. Does not replace VISTA, NSD, OPSA, OPD, or CISPO.
- **Not this task (agent RL retirement)**: `method:retireopd` (`arXiv:2609.20784`) on `task:outcome-only-long-horizon-agent-rl` — Adaptive Retirement of a privileged self-OPD teacher then pure RL on ALFWorld/WebShop. Does not replace VISTA.
- **Optional TSD calibration (not this first hop)**: `method:cal-opd` (`arXiv:2609.21619`) on `task:student-distillation` — residual discrepancy beyond a probed teacher-self-deviation region. Signal calibration during OPD, not a teacher update. Does not replace VISTA or RetireOPD.
- **Optional DCE+SRCL co-evolution (not this first hop)**: `method:dce-srcl` (`arXiv:2609.30652`). Privileged teacher refreshes from the student each round; SRCL adds shorter verified rewrites. Qwen3-8B 65.97% Average@12 vs **their** OPSD ~30%. That baseline is **not** the library VISTA bake-off (64.8→66.9). Status active; bake before any retarget. Does not replace VISTA, OPD, Self-OPD, LastOPD, S2D-OPD, or Open-MOPD.
- **Optional scale-collapse scaffold fix (not this first hop)**: `method:oasis` (`arXiv:2609.37915`). Supervise verified on-policy scaffolds; teacher context is another same-problem rollout (answer labels only). OPSD gains collapse with scale; OASIS stays ~+3 pts and beats OPSD by +3.05 at 8B. Does not replace VISTA or u-OPSD.
- **Optional MLLM spatial-hint OPSD (not this first hop)**: `method:where-opd` (`arXiv:2610.02117`). Teacher gets textual object/coord hints from synthetic scenes; student sees the same image. Real-world avg +3.23 on Qwen3.5-4B. VISTA stays text-math first hop. Mention on `task:mllm-finegrained-perception-rl`. Does not replace VISTA, OASIS, or Vision-RL2.
- **Optional neighborhood-expert OPSD (not this first hop)**: `method:n-opsd` (`arXiv:2609.39687`). Frozen local perturbations → denser supervision; Avg@12 +2.75/+1.67/+1.94 vs OPSD. No public code. Not a VISTA bake-off (64.8→66.9) retarget. Does not replace VISTA, OASIS, or DCE+SRCL.
- **Optional error-to-repair iterative OPSD (not this first hop)**: `method:air-opd` (`arXiv:2610.02700`). Qwen3-4B Math Avg External-G 66.7 / Self-G 65.8 vs OPSD 63.1 / GRPO 62.3. Does not replace VISTA or OASIS.
- **Optional root-cause-guided OPD (not this first hop)**: `method:rc-opd` (`arXiv:2610.03515`). Qwen3-1.7B/4B/8B Avg@4 44.17/66.11/66.94 vs OPSD 40.28/62.50/63.33. Code Starrylay/RC-OPD. Does not replace VISTA or OASIS.
- **See also (SFT data projection, not this first hop)**: `method:sampling-sft` (`arXiv:2610.02140`) on `task:math-code-rl-dense`. MCMC-projects off-policy traces then ordinary SFT. Chemistry (Qwen2.5-7B-Instruct) 0.660 vs OPSD 0.618; medical 0.458 vs OPSD 0.466 with prior avg 0.516 vs 0.501. Not a privileged-teacher update. Does not replace VISTA.
- **Optional rollout-free step-aligned distill (not this first hop)**: `method:sapd` (`arXiv:2610.09665`) privileged reference-solution steps, no live rollouts. ~2× vs on-policy. Code Miaow-Lab/SAPD. Does not replace VISTA or OPD.
- **Optional silent-group hindsight distill (not this first hop)**: `method:srd` (`arXiv:2610.08077`) on `task:math-code-rl-dense`. No gold teacher. Does not replace VISTA or VeriGate.
