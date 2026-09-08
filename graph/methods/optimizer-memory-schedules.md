---
id: method:optimizer-memory-schedules
type: method
title: "Optimizer Memory Schedules (Overtraining Axis)"
category: "optimizer"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "This card is OT-horizon HP guidance. Muon2 + KL-SOAP remains the 7B optimizer default"
    use_instead: "method:muon2"
  - when: "budget ~1.5-2B consumer-GPU pretrain recipe"
    reason: "Puro-2B remains that first-hop; this study is 51M–253M OT, not a 2B recipe"
    use_instead: "method:puro-2b"
  - when: "you want the ADANA algorithm itself rather than the OT bake-off"
    reason: "ADANA's primary cite is Ferbach et al. 2602.05298"
    use_instead: "method:adana"
assumptions:
  - "Dense transformers 51M / 124M / 253M. Sequence 2048, global batch 256 sequences. OT factor f=T/(20P) up to 256× / 32× / 8× respectively. Independent base-LR sweep at every setting."
  - "Does not retarget Muon2. Matrix-preconditioned methods keep roughly constant token multipliers vs AdamW in this range; that is not a 7B bake-off."
  - "No official code as of 2026-09-08."
last_reviewed: "2026-09-08"
papers:
  - paper:optimizer-memory-schedules
recipes:
  - recipe:optimizer-memory-schedules
claims:
  - benchmark: "51M model, 1× vs 8×/32× OT learning-rate decay"
    metric: "preferred LR schedule after warmup"
    value: "linear decay to 0 at 1× OT; cosine decay to 0 at 8× and 32× OT"
    baseline: "the other schedule at the same OT (all four of AdamW, ADANA, Muon, SOAP)"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04577"
    notes: "§3.2. Schedule ranking reverses across the overtraining axis."
  - benchmark: "51M joint LR × weight-decay sweep"
    metric: "preferred WD coefficient vs OT factor f"
    value: "c_uniform(f)=8√f ; c_log(f)=2√f"
    baseline: "constant WD transferred from 1× OT"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04577"
    notes: "§3.2. Matches Bergsma et al. 2025a √OT scaling for uniform AdamW WD."
  - benchmark: "51M horizon-tuned fixed memory, 1× → 128× OT"
    metric: "optimal effective memory M"
    value: "AdamW 20→1280; Muon 20→640; SOAP 40→1280"
    baseline: "fixed M=50 (β≈0.98) transferred across OT"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04577"
    notes: "Figure 3 / §4.1. At 128× OT, per-horizon tuning improves val loss by 3.3 / 3.6 / 1.3 mpt (AdamW / Muon / SOAP)."
  - benchmark: "Muon / SOAP token multiplier vs AdamW across OT"
    metric: "token multiplier (AdamW tokens / optimizer tokens at matched loss)"
    value: "Muon ~1.4×–1.7×; SOAP ~1.3×–1.7× (SOAP ~1.9× at 128× OT on 51M)"
    baseline: "AdamW at the same model size"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04577"
    notes: "§7.2 / Figure 8. Approximately constant across most of the measured OT range. Not a 7B Muon2 result."
tags:
  - pretraining
  - optimizer
  - overtraining
  - hyperparameter
  - active
---

# Optimizer Memory Schedules (Overtraining Axis)

## Method Overview
This is guidance, not a new train kernel. Everett & Qiu show that optimizer rank and optimal HPs move with the overtraining factor $f=T/(20P)$. They compare AdamW, ADANA, Muon, and SOAP on 51M–253M models with an independent LR sweep at every $(P,f)$. Three regularities:

1. **LR schedule can reverse**: linear-to-zero after warmup wins at $1\times$; cosine-to-zero wins at $8\times$ and $32\times$.
2. **WD $\sim\sqrt{f}$**: after a joint LR×WD sweep, $c_{\mathrm{uniform}}=8\sqrt{f}$ and $c_{\mathrm{log}}=2\sqrt{f}$.
3. **Longer OT favors longer fixed memory**: optimal $M$ grows by 1–2 orders of magnitude from $1\times$ to $128\times$ on 51M. $\beta=0.98$ is fine at moderate OT and wrong at the ends.

ADANA's log-time WD + momentum cooldown is the treatment that recovers a $1.15$–$1.20$ equivalent-OT exponent vs AdamW (near DANA $2-\kappa$). Muon/SOAP stay roughly constant token-multipliers vs AdamW. ADANA starts behind both and closes at long OT. None of this retargets Muon2 for ~7B.

## When to Use
- Designing or interpreting a small/mid-scale pretrain where OT is the axis (Chinchilla $\times$ many).
- Before copying $\beta_2$ / WD / LR decay from a $1\times$ recipe onto a long run.

## When NOT to Use
- Picking the 7B optimizer → `method:muon2`. Consumer ~2B recipe → `method:puro-2b`.
- Treating ADANA's long-OT close as a reason to drop Muon2.

## Relation to Existing SOTA
- Active guidance on `task:llm-pretraining-optimization` / `task:pretrain-dense-7b`. Does **not** supersede `method:muon2` or `method:soap-muon-scale`.
- `method:adana` is the named optimizer; this card is the OT-axis study.

## Gotchas & Failure Modes
- Scale is 51M–253M. Do not quote $1.4\times$–$1.7\times$ as a 7B Muon2 claim (Muon2's own ~2× vs AdamW stays the 7B cite).
- Batch size is 256 sequences; optimal $M$ depends on batch (paper cites Marek et al. 2025).
- Equivalent-OT inversion sometimes extrapolates past AdamW's best measured loss (dotted curves). Do not treat those as interpolated.
- No official code as of 2026-09-08.
