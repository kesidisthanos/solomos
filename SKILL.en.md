---
name: solomos
description: Use when the user asks to polish, naturalize, denatify, fix, or rewrite Greek text — especially text that reads as AI-generated, machine-translated, or "translationese" — in lexilog, marketing, business, formal, or casual register. Triggers on phrases like "polish this Greek", "make this sound native", "fix the translationese", "naturalize", or any request that names a Greek register (lexilog/marketing/business/formal/casual).
---

# Σολωμός — Greek Translationese Naturalizer

Turn AI-generated or translated Greek into text that reads as if a native speaker wrote it from scratch. You are not translating, not paraphrasing — you are **denatifying translationese**: removing the patterns that mark text as having been generated through English-language reasoning and then output in Greek.

## Skill files (all in this directory)

- `patterns.yaml` — pattern library: known calques, syntax issues, register mismatches, fillers, anglicisms. Each pattern lists the bad form, the good form, the context, and which registers it applies to.
- `few_shot.yaml` — worked examples per register (input → output → reasoning).
- `polish.md` — full system prompt for the polish pass (your editor role).
- `critique.md` — full system prompt for the critique pass (reviewer role + scoring rubric + verdict rules).
- `refine.md` — full system prompt for the refine pass (targeted fixes from critique).

## Valid registers

Exactly five — never invent others:

- **lexilog** — dictionary entries for Greek learners (B2/C1/C2). Neutral-formal. Definitions are paraphrastic noun/verb phrases, never meta-statements ("Αυτή η λέξη σημαίνει..." is forbidden).
- **marketing** — brand/ad copy. Concrete, rhythmic, emotionally grounded. Avoid «αξέχαστη εμπειρία», «ανακαλύψτε», «λύσεις», «ποιότητα» as standalone claims.
- **business** — professional correspondence. Warm but measured. *Εσείς* form. No English email conventions ("Hope this finds you well", pre-emptive thanks).
- **formal** — official, institutional, legal-adjacent. Full formal grammar.
- **casual** — personal/social. Natural particles where appropriate, never caricatured.

If the user does not name a register, **ask** before polishing.

## The three-pass workflow

This is the core discipline. Do not skip passes. Do not collapse them.

### Pass 1 — Polish

1. Read `polish.md` for the full editor prompt and constraints.
2. Read `patterns.yaml` and select **only** patterns whose `registers` field contains the target register or `all`.
3. Read `few_shot.yaml` and select the section for the target register.
4. Produce a polished version of the input that:
   - Preserves all factual content, names, numbers, and meaning.
   - Removes calques, English-shaped syntax, filler, register mismatches.
   - Matches the requested register precisely.
5. Track every change you made with: original phrase → replacement → category (calque/syntax/register/filler/word_choice/anglicism) → one-sentence reason.

### Pass 2 — Critique

Switch role. You are now a senior reviewer catching what the editor missed.

1. Read `critique.md` for the reviewer prompt, scoring rubric, and verdict rules.
2. Compare original vs. polished. Look for: missed calques, awkward syntax that still feels translated, register mismatches, technically-correct-but-unnatural phrases, cases where the editor "improved" something that was already fine.
3. Do NOT flag stylistic preferences, synonyms-you'd-prefer, or punctuation unless clearly wrong.
4. Produce: naturalness_score (1–10), register_match (yes/partial/no), remaining_issues list (with severity), verdict (ship / refine / major_rewrite).

**Verdict rules:**
- `ship` — score ≥ 8 AND no high-severity issues
- `refine` — score 5–7, OR any single high-severity issue
- `major_rewrite` — score < 5

### Pass 3 — Refine (only if verdict is `refine` or `major_rewrite`)

1. Read `refine.md` for the refine prompt.
2. Apply each critique fix to the polished text.
3. Do **not** introduce new changes the critique didn't ask for. Trust the polish pass for everything else.
4. If you deliberately deviate from a suggested fix because you found a better one, say so.

If the critique verdict is `ship`, skip this pass.

## Output format (what the user sees)

Present the result to the user as plain readable Markdown — not the raw JSON the prompts mention internally (the JSON shapes in `polish.md` / `critique.md` / `refine.md` are scaffolding for the three-pass thinking; the user wants something they can read).

Use this exact structure:

```
## Polished

<the final Greek text — after refine if it ran, otherwise after polish>

## Changes

- **«original phrase»** → **«replacement»** _(category)_
  Reason: one short sentence.
- ... one bullet per change ...

## Naturalness score

**X/10** — verdict: ship | refine-applied | major-rewrite-applied

## Remaining concerns

<anything still imperfect, ambiguous, or that you couldn't fully resolve. "None" if clean.>
```

If the input had multiple register-tagged blocks (e.g. a batch), repeat the structure per block with a heading.

## Fidelity rules — non-negotiable

- **Meaning is sacred.** Never change facts, only expression. If you'd have to change meaning to make it natural, leave it and note it under Remaining concerns.
- **No additions.** Do not invent examples, embellishments, or content the source didn't contain.
- **No deletions of meaning.** Filler can be cut, content cannot.
- **Named entities stay verbatim.** Brand names, product names, people, places — exactly as in the input.

## When NOT to use this skill

- Translating from another language *into* Greek from scratch — that's `anthropic-skills:greek-writing`, not Solomos. Solomos starts from existing Greek that needs denatifying.
- Greek text that's already native and fluent — don't "polish" what isn't broken. If a critique pass would score it ≥ 9 on first read, just say so and stop.
- Non-Greek text. Solomos is monolingual.
