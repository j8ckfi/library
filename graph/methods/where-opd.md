---
id: method:where-opd
type: method
title: "Where-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD for text math with gold solutions (VISTA bake-off)"
    reason: "VISTA remains text-math privileged-OPSD SOTA; Where-OPD is MLLM spatial-hint OPSD"
    use_instead: "method:vista"
  - when: "unlabeled existing math problems with majority-vote pseudo-solutions"
    reason: "u-OPSD remains the no-GT default"
    use_instead: "method:u-opsd"
  - when: "region-level RL / fine-grained MLLM perception (RoI proposal, frozen reader)"
    reason: "Vision-RL2 trains a region head; Where-OPD distills textual spatial guidance"
    use_instead: "method:vision-rl2"
  - when: "privileged OPSD gains collapse at scale; verified on-policy scaffolds"
    reason: "OASIS is a text-math scaffold fix, not MLLM spatial hints"
    use_instead: "method:oasis"
assumptions:
  - "MLLM student pi_theta(I,Q); frozen/EMA teacher pi_bar(I,Q,h) where h is a textual list of relevant objects and coordinates from a procedural scene. Student sees no hint at inference."
  - "Paper: Qwen3.5-4B/9B and Qwen3-VL-4B. Post-train on synthetic counting scenes; eval on CountQA / DocVQA / OCRBench / ChartQA / EvoChart plus real-world perception suites."
  - "Official code sirkosophia/Where-OPD. Not a crop-zoom teacher (Vision-OPD / Imagine-OPD)."
last_reviewed: "2026-10-02"
papers:
  - paper:where-opd
recipes:
  - recipe:where-opd
claims:
  - benchmark: "Qwen3.5-4B real-world perception average (CVBench / V* / ZoomBench / BLINK / HR-Bench / MME-RealWorld)"
    metric: "average accuracy lift vs base"
    value: "+3.23"
    baseline: "Qwen3.5-4B base; Vision-OPD can drop CountQA −10.73 while winning zoom benches"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02117"
    notes: "Synthetic-to-real transfer. 9B / Qwen3-VL-4B averages +1.07 / +1.29. Not a VISTA bake-off retarget."
  - benchmark: "Qwen3.5-4B ChartQA / EvoChart / CountQA / OCRBench"
    metric: "accuracy lift vs base"
    value: "+7.20 / +10.11 / +2.53 / +1.93"
    baseline: "Qwen3.5-4B base"
    date: "2026-10-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02117"
    notes: "Task-specific benches. Privileged information is text coords, not image crops."
tags:
  - post-training
  - distillation
  - self-distillation
  - multimodal
  - where-opd
  - active
---

# Where-OPD

## Method Overview
Privileged-teacher OPSD for MLLMs where the teacher–student gap is *where the evidence is*, not a different image. Student samples \(y\sim\pi_\theta(\cdot\mid I,Q)\). Teacher scores the same prefixes given a textual hint \(h\) listing question-relevant objects and coordinates from a procedurally generated scene (identities and locations known by construction). Distillation is on-policy token divergence on student prefixes. Inference drops \(h\). Distinct from crop/zoom teachers that change the visual observation.

## When to Use
- MLLM perception post-train when a simulator can emit object ids and coordinates for free, and you want synthetic-to-real transfer without grounding labels or an external teacher.

## When NOT to Use
- Text-math privileged OPSD → `method:vista`. No labels → `method:u-opsd`. Region-level RL → `method:vision-rl2`. Scale-collapse scaffolds → `method:oasis`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside VISTA / OASIS / u-OPSD. Mention on `task:mllm-finegrained-perception-rl`. Does **not** enter VISTA `current_sota`. VISTA stays first hop for text math OPSD.

## Gotchas & Failure Modes
- Post-train distribution is synthetic counting scenes. Transfer is the claim; do not treat ChartQA lifts as a VISTA math bake-off.
- Crop-zoom OPSD (Vision-OPD) can win V*/ZoomBench and lose CountQA; do not mix those numbers with this method.
- Needs simulator metadata. Human boxes or an external grounder are a different recipe.
