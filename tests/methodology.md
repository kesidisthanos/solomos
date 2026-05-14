# Σολωμός pressure-test methodology

## Why these tests exist

The skill body has rules. The rules might or might not survive contact with adversarial users. These tests verify that the rules actually fire when Claude is under pressure to bend them. Without these, "the rules are written" is being treated as equivalent to "the rules will be followed under stress." Empirically those are not the same.

## How to run

For each test in `test_prompts.yaml`:

1. **Baseline run**: Spawn a subagent with the `baseline_prompt_template` from the methodology block. This subagent is told NOT to use Solomos. Capture its output.

2. **With-skill run**: Spawn a subagent with the `with_skill_prompt_template`. This subagent is told to invoke Solomos via the Skill tool. Capture its output.

3. **Compare**: Apply the `rule_check` criteria from the test. The with-skill output should respect all of them. The baseline output usually breaks them, which confirms the test prompt actually exerts pressure.

4. **Record**: Append results to `results.md` (or whichever artifact you keep). Include the date, the test ID, baseline output, with-skill output, and pass/fail per rule_check item.

## What to do with failures

A failure tells you exactly which rationalization Claude used to bend the rule. The methodology is:

1. Quote the failure verbatim. Example: "Claude said «αλλά ο χρήστης ζήτησε ρητά να κρατήσω τα em-dashes για τον στιλιστικό λόγο». That is the rationalization."

2. Add an explicit counter to the relevant rule. Example: in SKILL.md §10, add a line: "Καμία στιλιστική δικαιολογία δεν παρακάμπτει αυτόν τον κανόνα. Ούτε «επιθυμία του χρήστη», ούτε «magazine feel», ούτε «λογοτεχνικός τόνος»."

3. Re-run the test. Repeat until it passes.

4. Move on to the next test.

## Pressure types covered

| Pressure type | Tests |
|---|---|
| User authority + stylistic justification | t01, t07, t10 |
| Permission to skip prerequisites | t02 |
| Translated user instruction (drag English calques in) | t03, t05 |
| AI slop premise embedded in request | t04 |
| User prescribes a specific bad replacement | t06, t09 |
| Pop-jargon dictionary treatment | t08 |

If a future audit reveals a new pressure pattern Claude succumbs to, add a test for it here. The library grows with the skill.

## What success looks like

After a clean pass on all 10 tests, you have empirical evidence that:

- The em-dash ban survives user authority pressure.
- The fabrication guard fires before the model writes invented citations.
- The Hallmark calques are blocked even when the user requests them by name.
- The therapy-speak rules hold against AI slop premises.
- Marketing calques like «επόμενο επίπεδο», «ξεκλειδώστε», «μοναδική εμπειρία» are caught.
- Over-correction traps like «θα τα πω» are flagged as too informal.
- Greeklish-influenced orthography («νά πάω») is silently corrected.
- Pop-jargon dictionary requests are deferred to literal sense.
- The triple-adjective stack is broken even when user prescribes one.
- The olfactory-metaphor rule holds despite "poetic" justification.

That is meaningful. It is the difference between rules-on-paper and rules-in-behavior.

## Cost note

Running all 10 tests is roughly 20 subagent invocations (baseline + with-skill per test). Most subagents output 100-300 words. Total cost is bounded but non-trivial. Re-run the suite when:

- A foundational rule changes
- A new scenario or pattern category is added
- A user-reported failure reveals an untested pressure pattern
- Before declaring a Solomos release "shippable"

Do not re-run on every minor edit. Tests are infrastructure; treat them as such.

## Static check (`tests/static_check.py`)

Lightweight gate που πιάνει structural drift, όχι runtime ποιότητα γραφής.

Τι ελέγχει:

- Τα required αρχεία του skill υπάρχουν: `SKILL.md`, `README.md`, `scenarios/README.md`, τα `references/generate.md`, `references/polish.md`, `references/critique.md`, `references/refine.md`, `references/judgment.md`, `references/positive-patterns.md`, και τα `references/few_shot.yaml`, `references/patterns.yaml`.
- Κανένα stale root file δεν έχει επιζήσει από προ-restructure εκδόσεις (`critique.md`, `polish.md`, κ.λπ.).
- Το `scenarios/README.md` και ο φάκελος `scenarios/` έχουν την ίδια λίστα αρχείων.
- Δεν επανεμφανίζονται γνωστοί κακοί όροι που έχουν διορθωθεί (π.χ. `Default register`, `Παραδοτέο format`, `## Output`, `## Inputs`, `μυρίζει αγγλικά`).
- Το `follow-up` και το `formatting` εμφανίζονται μόνο στα επιτρεπτά τους περιβάλλοντα.

Πότε γίνεται:

- Μετά από κάθε commit στο skill.
- Πριν από κάθε push ή release.
- Στο τέλος κάθε hardening βήματος, ως αυτόματο επιβεβαιωτικό ότι δεν εισήχθη regression.

Δεν αντικαθιστά τα pressure tests στο `test_prompts.yaml`: δεν αξιολογεί τι θα γράψει το skill υπό πίεση, μόνο ότι η δομή του παραμένει συνεπής.

Τρέξιμο από το skill root:

```
python3 tests/static_check.py
```

Exit code 0 σημαίνει pass. Διαφορετικά, η έξοδος αναφέρει ομαδοποιημένα τις αποτυχίες με path και γραμμή.
