---
id: method:mintrl
type: method
title: "MInTRL (Minimal Intervention Reinforcement Learning)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR default"
    reason: "MInTRL is a sparse-intervention plug-in on otherwise on-policy RLVR; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "MoE/VL RLVR loss"
    reason: "SAPO remains the MoE/VL algorithm; MInTRL does not retarget it"
    use_instead: "method:sapo"
  - when: "variable tool latency / async stragglers"
    reason: "Paper lists long-horizon agentic eval as future work; SAO remains async RL"
    use_instead: "method:sao"
  - when: "outcome-only long-horizon coverage / anti-drift"
    reason: "CANOPY / DRACO own that shelf; MInTRL is single-turn math/code interventions"
    use_instead: "method:canopy"
assumptions:
  - "Host is on-policy RLVR with a verifiable outcome. Paper: Qwen3-1.7B/4B non-thinking, judge Qwen3-4B-Instruct-2507, AceReason-Nemotron math + DeepCoder-Preview code."
  - "Advantage-regression objective (no IS). MInTRL-Const outperformed MInTRL-Proxy in the main tables."
  - "No official GitHub as of 2026-09-14."
last_reviewed: "2026-09-14"
papers:
  - paper:mintrl
recipes:
  - recipe:mintrl
claims:
  - benchmark: "Qwen3-1.7B math avg (AIME25 / AIME26 / HMMT25) and code avg (LCB / HE+ / MBPP+)"
    metric: "mean Pass@1 (n=32)"
    value: "35.45 math / 61.95 code"
    baseline: "stronger of GRPO and OPD: +13.61 math / +14.12 code"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12419"
    notes: "MInTRL-Const. Not a CISPO bake-off. Paper also states up to +9.44 pp vs strongest competitor."
  - benchmark: "Qwen3-4B math / code avgs, same protocol"
    metric: "mean Pass@1 (n=32)"
    value: "55.73 math / 72.63 code"
    baseline: "GRPO/OPD pair: +3.02 math / +6.80 code"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.12419"
    notes: "Const generally beats Proxy when the student is weak; Proxy can win under self-intervention (52.29 vs 48.47)."
tags:
  - post-training
  - rl-alignment
  - rlvr
  - mintrl
  - active
---

# MInTRL (Minimal Intervention Reinforcement Learning)

## Method Overview
On-policy RLVR cannot see trajectories the policy never samples. Full off-policy SFT shifts the distribution too far. MInTRL inserts sparse local edits: a judge-intervention policy reviews a chunk, either Keeps it or Revises a short suffix, then returns control to the student. Training is sequence-level advantage regression, so mixed-policy tokens do not need importance sampling. Intensity is a knob: too little does nothing; too much becomes off-policy SFT.

## When to Use
- Dense math/code RLVR where on-policy sampling is stuck and a stronger judge can patch local errors.
- When you can afford extra inference for reviews but want most tokens still on-policy.

## When NOT to Use
- Pass@1 default → `method:cispo`. MoE/VL loss → `method:sapo`. Async tools → `method:sao`. Outcome-only agents → `method:canopy`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense`. Does **not** enter `current_sota`. CISPO / SAPO / SAO unchanged. Agentic long-horizon is explicitly future work in the paper.

## Gotchas & Failure Modes
- Peak at moderate off-policy token fraction. Full expert trajectories regress toward SFT+GRPO.
- Intervention tokens can have tiny student probability; Const anchors were more stable than Proxy in the main tables.
- Review cost vs GRPO is real; paper argues wall-clock can still win via denser signal.
