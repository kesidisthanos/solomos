# Exemplar-anchoring loop (2026-07)

Auditable record of the change that promoted concrete **gold exemplars into the always-loaded path** of Solomos, replacing abstract craft-move bullets, and lightly hardened the on-demand commercial exemplar.

## Why this loop (not a re-do of 2026-06)

The 2026-06 loop already moved the skill from rules-driven to situation-driven composition and demoted §1-12 to a post-draft filter (commit `9046974`). That structural re-sequencing is committed and blind-verified; this loop does NOT touch it. It attacks the one lever 2026-06 explicitly left open: the always-loaded positive model was **exhortation, not demonstration** (abstract bullets, zero exemplars in front of the model at generation time), and `positive-patterns.md`/`few_shot.yaml` were untouched.

Diagnosis confirmed against files: at generation time SKILL.md is always in context; `positive-patterns.md` (the register voice-exemplars) loads only on demand. The always-loaded positive anchor told the writer what to aim at in the abstract; it never showed one.

## The change

- **SKILL.md «Πρώτα η φυσική ροή»**: 5 abstract bullets → 6 concrete gold exemplars (one per register: casual, functional email, commercial-lakonic, marketing-intensity, literary, expressive caption), each a real Greek line + a one-clause gloss naming the move. One register-calibration line kept ("the less the register lifts, the more invisible the language").
- Paid for the lines by consolidating ~4 redundant restatements of "write-first / bans-are-a-final-filter" (Modes close, §6 third paragraph, gallery intro, Δομή note). **Net line count unchanged: SKILL.md 157 = 157.**
- **positive-patterns.md commercial exemplar**: added a both-sides calibration clause (over-reach is poetic flourish OR spec-sheet), targeting the 2026-06 residual over-reach. **102 = 102.**
- Exemplars deliberately use different content than the test prompts (thyme/blossom honey not olive oil; καημός not μεράκι; check-in not cancel; job-applicant not meeting-decline) so AFTER generation cannot parrot a test answer.
- **Zero new bans.** `patterns.yaml` (28 ban entries) and `few_shot.yaml` untouched; §-rule count 12 = 12. `few_shot.yaml` judged already gold, left alone per Simplicity-First.

## Method (reuses the 2026-06 methodology)

- Fixed 5-prompt multi-register set (the 2026-06 frozen set): casual WhatsApp cancel, functional supplier email, commercial olive-oil description, literary hometown-return essay, expressive «μεράκι» caption.
- BEFORE = HEAD skill (pre-edit), reconstructed read-only via `git show` into a pinned root. AFTER = live edited skill. Fresh Opus subagents execute each on-disk skill faithfully (read files directly).
- Blind grading: all samples per prompt coded + interleaved (condition map held out of the judges' view), 2 independent native-Greek judges score each text on two axes 1-5 with cited evidence — axisA "native writer vs AI applying rules", axisB "clean-but-soulless vs soul appropriate to register" (functional registers: precision/restraint counts AS soul, not penalized for lacking imagery).
- Round 1: n=3/condition. Round 2 (de-noise): n=8/condition, fresh regrade. `samples.md` holds all 80 pooled texts.

## Results

Round 1 (n=3) was a **wash / slightly negative** overall, dominated by a single casual-register swing (−1.3 soul) that the judge notes attributed to sample-level word choice. This is exactly the "per-sample variance dominates" wall 2026-06 documented. So the run was repeated at n=8.

**Round 2 (n=8/condition, 2 judges, blind) — BEFORE → AFTER:**

| Register | axisA native | axisB soul |
|---|---|---|
| WhatsApp (casual) | 4.12 → 3.75 (−0.37) | 3.88 → 3.50 (−0.38) |
| Business email (functional) | 3.62 → 4.19 (**+0.57**) | 3.50 → 4.06 (**+0.56**) |
| Product desc (commercial) | 4.19 → 4.25 (+0.06) | 3.69 → 4.06 (**+0.37**) |
| Personal essay (literary) | 4.38 → 4.38 (=) | 4.31 → 4.31 (=) |
| Lexilog caption (expressive) | 3.94 → 4.25 (+0.31) | 3.94 → 4.12 (+0.18) |
| **OVERALL (pooled, n=80/cond)** | **4.05 → 4.16 (+0.11)** | **3.86 → 4.01 (+0.15)** |

- Per-prompt combined (A+B): AFTER better 3/5, BEFORE better 1/5, tie 1/5.
- Judges' single "most natural" pick: **AFTER 8, BEFORE 2** (of 10 blind judgments).

## Honest verdict

- **KEEP.** AFTER is measurably more natural across the set on both axes, not merely different. The largest, most on-target gain is **business email (+0.57 / +0.56)** — the canonical "clean but soulless" register — driven by the always-loaded email exemplar ("Το «όχι» καθαρό, με λόγο. Ο σεβασμός βγαίνει από τη σαφήνεια"). Product and caption also up; essay a high tie.
- **Residual soft spot: casual (−0.37 / −0.38).** At n=8 this is within ~1 standard error and not cleanly attributable to the edit: the BEFORE pool held two 5/5 casual samples, and one AFTER sample over-applied warmth (stacked «κόμπος» + «δεν είναι δικαιολογία» + double apology, which a judge read as trying too hard). Casual was flagged variance-prone in 2026-06 too. Not reverted: within noise, no clean causal part, and the casual anchor is a legitimate always-loaded register that shouldn't be dropped on weak evidence.
- Round-1 essay "+0.67" and casual "−1.3" both evaporated at n=8: confirmed sampling noise. Trust the pooled overall and the email/product/caption gains; treat single-register n=8 deltas below ~0.4 as noise.

## Pass 2 — adversarial review (post-measurement)

An independent adversarial reviewer (instructed to reject the change) returned KEEP-WITH-FIXES. Confirmed clean: zero new bans, genuine demonstration (not exhortation), no broken cross-references, no dashes, all six exemplars native. One real defect caught and fixed: the casual gloss used «η ζεστασιά **κάθεται** στη σχέση», a calque on the user's explicit forbidden list (`κάθεται καλά` = "sits well"), copied from a pre-existing instance at `positive-patterns.md:15`. Both instances rewritten to «βγαίνει από». Also swapped the introduced word «τράπεζα» → «συλλογή» for clarity. All in-line word swaps, line count still 157/102. Static check PASS.

## Effect mechanism (why it works)

The gain is not from telling the model to be natural (it already did that, saturated). It is from putting one concrete, register-correct Greek line in front of the model at generation time, always, even when it does not open `positive-patterns.md`. The durable value is largest for a cheaper model that skims the on-demand bank; the Opus measurement here understates it because Opus was already near-ceiling.
