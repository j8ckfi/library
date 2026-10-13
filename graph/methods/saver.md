---
id: method:saver
type: method
title: SAVER
category: multimodal-rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: video annotation-as-rollout / fine-grained video perception RL without sparse-frame
    inference
  reason: OraRL remains the video MLLM RL first hop; SAVER is dense-to-sparse paired-view
    RL
  use_instead: method:orarl
- when: general image/multimodal reasoning RL prompt curriculum
  reason: EPS prompt scaffolding is the image/VL prompt curriculum
  use_instead: method:eps-prompt-scaffolding
assumptions:
- 'Video MLLM RL. Paper: Qwen3.5 0.8B/2B/4B; 1,250 Time-R1 grounding examples; sparse
  fps at test.'
- 'Code: lmsdss/SAVER (code_status: released).'
last_reviewed: '2026-10-13'
papers:
- paper:saver
recipes:
- recipe:saver
claims:
- benchmark: Qwen3.5-2B/4B sparse-fps temporal grounding and video-QA vs Qwen3.5
  metric: avg mIoU / QA avg / VideoMMMU
  value: 2B 0.1fps mIoU 18.4→30.0, QA 45.9→50.8; 4B VideoMMMU 0.1fps 52.4→72.7
  baseline: same-size Qwen3.5 at the same fps
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.10893
  notes: Also 2B 2.0fps QA 51.0→54.6; 4B 60.8→64.4. 1,250 grounding examples, no QA
    labels. Does not retarget OraRL.
tags:
- video-mllm
- post-training
- saver
- active
---

# SAVER

## Method Overview
Sample a dense view and a sparse view of the same video. Optimize both with format + grounding rewards. Add a reliability-gated reference reward so the sparse view copies the dense view only when the dense grounding reward is higher. At test, use sparse frames only.

## When to Use
- Video MLLM RL where inference must run at low fps and you can pair dense training views.

## When NOT to Use
Annotation-as-rollout video perception → `method:orarl`. Image/VL prompt curriculum → `method:eps-prompt-scaffolding`.

## Relation to Existing SOTA
Active plug-in on `task:rl-video-mllm` beside `method:orarl` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OraRL.

## Gotchas & Failure Modes
- **code: released** lmsdss/SAVER as of 2026-10-13.
- Trained only on 1,250 Time-R1 grounding examples; QA gains are transfer.
- Dense fallback at test is an optional appendix, not the default protocol.
