---
id: method:magicbeanstalk
type: method
title: MagicBeanStalk
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR algorithm
  reason: CISPO remains Pass@1; MagicBeanStalk synthesizes calibrated problems to escape zero-advantage
    groups
  use_instead: method:cispo
- when: all-zero verifier groups / gated process supervision
  reason: VeriGate gates PRMs; MagicBeanStalk grows new problems from hard seeds
  use_instead: method:verigate
- when: hindsight-to-foresight distillation when verifier groups are silent (SRD)
  reason: SRD distills hindsight; MagicBeanStalk synthesizes new mid-difficulty problems
  use_instead: method:srd
assumptions:
- 'RLVR with a verifiable corpus that is mostly all-success or all-fail for the target policy and budget.
  Paper: 78K pooled math corpus ~88% zero-advantage; gpt-oss-120b and DeepSeek v4Flash; also finance synthesis.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:magicbeanstalk
recipes:
- recipe:magicbeanstalk
claims:
- benchmark: 8 math benches, 16K-token budget, continual RLVR on synthesized families
  metric: mean across 8 math benches vs full 78K source corpus / best filtered subset
  value: gpt-oss-120b 61.2→69.8 (+8.6); DeepSeek v4Flash 72.4→77.9 (+5.4); full corpus +1.1; best filtered
    real subset +5.8
  baseline: full 78K pooled RLVR corpus; best filtered real subset
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12659
  notes: Does not retarget CISPO or VeriGate. Filtering discards hard problems; synthesis keeps their
    blueprints at calibrated difficulty.
tags:
- post-training
- rlvr
- data-synthesis
- magicbeanstalk
- active
---

# MagicBeanStalk

## Method Overview
For each always-fail seed, extract the reasoning blueprint, then grow easier compositional children until the target policy's train-budget pass rate is mixed. Train RLVR on those families, not on the all-fail originals.

## When to Use
- Labeled math RLVR where most corpus items are all-pass or all-fail at your k and max tokens.

## When NOT to Use
Pass@1 algorithm → `method:cispo`. Gated PRM → `method:verigate`. Silent-group hindsight distill → `method:srd`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` with a mention on `task:all-zero-verifier-groups` (`sota_for: []`). Does **not** replace CISPO, VeriGate, or SRD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Filter-only baselines cannot recover discarded hard blueprints.
- Difficulty must be calibrated to the target policy and budget; a generic teacher rewrite is not enough.
