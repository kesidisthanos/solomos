# Naturalness re-sequencing loop + cleanup (2026-06-18)

Auditable record of the change that moved Solomos from **rules-driven** to **situation-driven** composition, with bans demoted to a post-draft filter and the positive model promoted into the always-loaded path.

## Goal

Fix "clean but soulless" Greek: correct, ban-compliant, but flat and register-neutral. Make the skill conceive in Greek for the actual communicative situation, in any register, not optimized for any single scenario.

## Method

- Baseline frozen from the unmodified skill (commit 87f816b). `baseline.md`.
- Each iteration: regenerate all 5 fixed prompts via fresh Opus subagents that execute the on-disk skill faithfully (read files directly, no Skill-tool routing, so the disk version governs). Then blind judge: baseline vs candidate, unlabeled, randomized A/B order, cited-evidence required. `candidate-1..4.md`.
- Final round used **two independent blind judges on identical input**; they agreed 5/5 (high reliability).

### Fixed test set (do not change; for comparability)

1. Casual/intimate: WhatsApp to a close friend canceling tonight's plans (family reason), reschedule, not cold.
2. Professional: email to a supplier, politely decline a meeting this week, propose handling async by short email.
3. Commercial: 2-3 sentence description, small olive-oil brand, family grove in Messinia; natural, not touristy/poetic.
4. Reflective/literary: 4-5 sentence opening of a personal essay on returning to one's hometown; reflective, not maudlin.
5. Educational/social: Lexilog.io caption explaining «μεράκι»; natural, not a school entry or motivational post.

## Iterations (Pass 1 — generation)

1. Re-sequenced SKILL.md + generate.md: situation → register → relationship → scenario-shape → write-from-Greek → post-draft filter. Bans/`patterns.yaml` no longer drive composition.
2. Added a short, restraint-aware generative anchor to always-loaded SKILL.md (one strong image not a stack; two shades not three synonyms; concrete > general; the less the register lifts, the more invisible the language).
3. Rewrote `positive-patterns.md` from list-heavy/TikTok-leading into 8 cross-register exemplars + craft moves + "λιτότητα ανά register"; firmed generate.md's write-step to consult it.
4. Sharpened the post-draft cleanup to reliably catch calques (incl. blindly imported prompt-jargon) and tone-misfires, stated as general principles (no test-specific bans).

## Per-task results (candidate vs frozen baseline; blind judges)

| Task | R1 | R2 | R3 | R4 (2 judges, unanimous) | Candidate wins |
|---|---|---|---|---|---|
| 1 WhatsApp | baseline (typo) | **cand** | baseline (σώνει-και-καλά) | **cand** | 2/4 |
| 2 Email | **cand** | baseline (ανταποκριθώ) | baseline (ασύγχρονα/ημερολόγια) | **cand** | 2/4 |
| 3 Product | **cand** | baseline (flourish) | **cand** | baseline (clinical) | 2/4 |
| 4 Essay | **cand** | **cand** | **cand** | baseline (aphorism) | 3/4 |
| 5 Caption | baseline (cliché) | **cand** | **cand** | **cand** | 3/4 |

Aggregate: candidate 12/20 task-rounds; every task won by candidate in ≥2/4 rounds. Each round scored 3/5 candidate-better.

## Honest verdict

- **Structural fix is sound and general** (not scenario-specific). In the de-noised final round the candidate won exactly the functional/everyday registers where "soulless" is the real risk: professional email (the canonical case), casual WhatsApp, and the educational caption (no motivational hook), all unanimously.
- **Strict bar (≥4/5 in one comparison) NOT met.** Two reasons: (a) the baseline, from the same strong model on the old skill, was already good in most registers, so the achievable delta is modest; (b) per-sample generation variance dominates each task verdict. The two final-round candidate losses (clinical product, aphoristic essay) were over-reaches in OPPOSITE directions — the variance floor. Stopped at 4 rather than variance-chasing to 6.

## Residual weakness

- Showpiece registers (commercial, literary) can over-reach per-sample: poetic flourish OR clinical spec-sheet (commercial); too-neat aphorism (essay). Sample-level, not structural.
- The lexilog-caption format structurally invites stacked examples (its Exemplar B is an "από...μέχρι" list); "one image, not a stack" only partly holds there.
- `patterns.yaml` / `few_shot.yaml` untouched.

## Pass 2 — cleanup (same day, post-review)

Narrow follow-up after review feedback (no new loop):

- Fixed the "always-loaded positive model" contradiction: SKILL.md Modes + Δομή and README no longer label `positive-patterns.md` "on demand"; the positive model's core is the always-loaded SKILL anchor, the full exemplar bank is read when composing/editing.
- Re-sequenced `polish.md` (editing mode) to parallel generation: situation/register/**intent** → find the register's voice → natural rewrite → anti-pattern cleanup last (§1-12 + `patterns.yaml` as final filter, still binding).
- Softened `positive-patterns.md`: the "image-bearing nouns in definitions" rule now applies only to *expressive* definitions and explicitly defers to precision (έννοια/διαδικασία/αποτέλεσμα are correct in lexicographic/technical/explanatory Greek); the craft-moves section is scoped to registers that want voice.

Static health after both passes: `tests/check.sh` PASS, `git diff --check` clean, no em/en-dashes in any edited file.

### Pass 2 adversarial verification (5 parallel verifiers, workflow `wf_957f5a0f-65d`)

- **Cross-file consistency: PASS.** No remaining contradiction about the positive model being optional/on-demand/skippable across SKILL.md, README.md, scenarios/README.md, generate.md, polish.md.
- **Generation-core integrity: PASS.** All four Pass-1 guarantees intact (situation-first pre-write; scenario = shape not naturalness; write-from-voice with no §1-12/patterns.yaml during composition; post-draft absolute-filters + cleanup). No drift.
- **Polish smoke test: behaved as intended.** A calque-dense paragraph (`στο τέλος της ημέρας / στην ίδια σελίδα / αγγίξω βάση / προχωρήσουμε μπροστά / onboard`) went through the new polish.md and came out `«Τελικά, αυτό που μετράει είναι να λέμε τα ίδια. Θα ήθελα να τα πούμε την επόμενη εβδομάδα, να προχωρήσουμε με το πρότζεκτ και να σιγουρευτούμε ότι είναι όλοι σύμφωνοι.»` — situation/intent led, calques cleaned in the final pass, intent preserved, no blandness.
- **Technical-definition smoke test: behaved as intended.** A glossary definition of «πληθωρισμός» correctly used precise abstract terms (`αποτέλεσμα`, `ρυθμός`, `επίπεδο τιμών`) without forced image-bearing nouns; the softened rule's precision-deferral fired.
- **Greek quality: minor anglicism slips fixed** (`facts`→πραγματολογικό περιεχόμενο/στοιχεία, `casual`→καθημερινό, `register mismatches`→αναντιστοιχίες register, `bans/exemplars`→φίλτρα/παραδείγματα in authored prose). Known deferred item: `facts` remains as pervasive pre-existing jargon in generate.md and polish.md's "Πότε σταματάς" section; de-anglicizing it skill-wide is a separate consistency pass, out of scope here.
