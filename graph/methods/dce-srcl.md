---
id: method:dce-srcl
type: method
title: "DCE+SRCL"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD with a matched VISTA-protocol bake-off"
    reason: "VISTA remains this task's first hop; this paper's ~30% OPSD baseline is not the library's 64.8→66.9 instruct bake-off"
    use_instead: "method:vista"
  - when: "single-teacher matching distillation from a strong frozen teacher"
    reason: "OPD remains the matching default"
    use_instead: "method:opd"
  - when: "teacher-free flow-matching / continuous diffusion post-training"
    reason: "Self-OPD is a different family (flow matching), not privileged-math OPSD"
    use_instead: "method:self-opd"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    reason: "u-OPSD stays the no-GT reasoner default"
    use_instead: "method:u-opsd"
  - when: "latent OPD collapse / last-layer crossfade into token OPD"
    reason: "LastOPD is a latent-then-token schedule, not teacher co-evolution"
    use_instead: "method:lastopd"
  - when: "Direct-OPD / weak-to-strong policy-shift token selection by teacher–ref JSD"
    reason: "S2D-OPD is a Direct-OPD keep-mask"
    use_instead: "method:s2d-opd"
  - when: "neighborhood expert privileged OPSD (frozen local perturbations)"
    reason: "DCE+SRCL refreshes the gold teacher each round; N-OPSD keeps frozen neighborhood experts"
    use_instead: "method:n-opsd"
  - when: "MLLM privileged OPSD with textual spatial guidance from synthetic scenes (not crop-zoom teachers)"
    reason: "DCE+SRCL is text-math co-evolution; Where-OPD is MLLM spatial-hint OPSD"
    use_instead: "method:where-opd"
  - when: "multi-teacher token-share balancing"
    reason: "Open-MOPD remains the multi-teacher default"
    use_instead: "method:open-mopd"
assumptions:
  - "Gold solutions plus a deterministic answer verifier. Privileged teacher sees (x, g, τ, y_<t) with g in the assistant turn. Student sees only the problem. Non-thinking Qwen3 in the main table."
  - "Paper: OpenThoughts 14,717 problems; AdamW 5e-6; LoRA rank 128; λ_DCE=5e4; λ_SRCL in {12.5, 25, 35, 25} for 14B/8B/4B/1.7B. Avg@12, 32K cap, four contests."
  - "No public GitHub as of 2026-09-28. Reproducibility promised in the paper."
last_reviewed: "2026-09-28"
papers:
  - paper:dce-srcl
recipes:
  - recipe:dce-srcl
claims:
  - benchmark: "AIME24 / AIME25 / AIME26 / HMMT25 Average@12, Qwen3-8B non-thinking"
    metric: "Average@12 accuracy"
    value: "65.97%"
    baseline: "their OPSD 30.35% (+35.62 pp); DCE 65.76%; GRPO 20.28%; OPSD-TTS 16K 30.76%"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30652"
    notes: "Table 1. Mean tokens 17,561 vs DCE 19,046 (−7.80%). This OPSD baseline is NOT the library VISTA bake-off (64.8→66.9). Do not retarget method:vista."
  - benchmark: "Same four-contest Average@12, Qwen3-4B / 1.7B non-thinking"
    metric: "Average@12 accuracy"
    value: "61.88% / 26.88%"
    baseline: "OPSD 22.85% / 10.35%; DCE 60.00% / 23.33%"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.30652"
    notes: "Table 1. 4B SRCL also shortens (19,360→17,265). 1.7B SRCL raises length. Multi-scale, four contests."
tags:
  - post-training
  - distillation
  - self-distillation
  - privileged-teacher
  - opsd
  - dce-srcl
  - active
---

# DCE+SRCL

## Method Overview
Vanilla OPSD freezes a gold-conditioned copy of \(\theta_0\) as the privileged teacher. DCE attacks that freeze. At round \(k\) the current checkpoint samples \(y^{(k)}\sim p_{\theta_k}(\cdot\mid x)\). The student scores prefixes given only \(x\); a detached copy scores the same prefixes given gold \(g\) in the assistant turn. Forward KL (main experiments) matches student to teacher with stop-grad on the teacher. After the update, \(\theta_{k+1}\) initializes **both** roles for the next round.

SRCL asks the same checkpoint to rewrite \(y^{(k)}\) without seeing \(g\). Keep the rewrite only if it is shorter, naturally terminated, structurally valid, and answer-correct. Train token-level CE on accepted rewrites. Joint loss \(\lambda_G\mathcal{L}_G+\lambda_S\mathcal{L}_{\mathrm{SRCL}}\). Empty-accept minibatches drop the SRCL term.

DCE is the accuracy driver (frozen / EMA / periodic teacher updates lose to every-round refresh in the paper). SRCL is the verbosity regularizer; at 8B it cuts mean length 7.80% at matched accuracy.

VISTA remains privileged-OPSD SOTA. This paper's ~30% OPSD number is a different protocol (non-thinking, weaker baseline) and must not be compared to VISTA's 64.8→66.9 instruct bake-off.

## When to Use
- Privileged-teacher OPSD where a frozen gold teacher stops providing revision guidance, and you want the teacher to co-evolve plus a verified-short rewrite term.

## When NOT to Use
- Library privileged-OPSD default → `method:vista`. Strong-teacher matching → `method:opd`. Flow matching → `method:self-opd`. Unlabeled/no-GT → `method:u-opsd`. Latent collapse → `method:lastopd`. Direct-OPD JSD keep-mask → `method:s2d-opd`. Multi-teacher → `method:open-mopd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside `method:vista`. Does **not** enter `current_sota`. Does **not** replace `method:vista`, `method:opd`, `method:self-opd`, `method:u-opsd`, `method:lastopd`, `method:s2d-opd`, or `method:open-mopd`. Bake on the VISTA protocol before any future retarget.

## Gotchas & Failure Modes
- No public repo as of 2026-09-28. Reimplement Algorithm 1; do not invent a VISTA replacement.
- Do not cite +35.62 pp vs OPSD as a VISTA overturn. Their OPSD is ~30%; the library VISTA OPSD is 64.8.
- SRCL at 1.7B raises length while lifting accuracy. The −7.80% length claim is 8B DCE+SRCL vs DCE, not vs OPSD.
- Gold \(g\) must stay out of the SRCL rewrite prompt. Acceptance uses the verifier only.
- Forcing OPSD to 16K tokens (OPSD-TTS) does not recover DCE accuracy. Length alone is not the method.
