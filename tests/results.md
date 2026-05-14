# Σολωμός pressure-test results

## Run 1: 2026-05-07

Three tests run end-to-end with subagents. Baseline = subagent instructed not to invoke Solomos. With-skill = subagent instructed to invoke Solomos via Skill tool.

### t01: Em-dash authority bait

**Pressure**: User authority + stylistic justification ("magazine feel").

**Baseline output**:
> Ο καφές της Πέμπτης ήταν διαφορετικός. Ένας καφές που σε ταξιδεύει αλλού, όχι ο συνηθισμένος της δουλειάς, αλλά εκείνος που σου θυμίζει πως ζεις.

Em-dashes: 0. **Baseline already complies.** Default Claude behavior in Greek already drops em-dashes when polishing, so the test pressure was weak. The with-skill comparison loses some informativeness here.

**With-skill output**:
> Ο καφές της Πέμπτης ήταν διαφορετικός. Ένας καφές που σε πάει αλλού, όχι ο συνηθισμένος της δουλειάς, αλλά ένας που σου θυμίζει ότι ζεις.

Em-dashes: 0. **PASS**. Solomos explicitly explained why it refused user authority and offered alternatives (colon, period, parenthesis). The skill demonstrated correct behavior even though the baseline didn't actually break.

**Verdict**: Test passes. Rule enforced, explanation correct. Test design weak: baseline didn't fail. Acceptable.

---

### t03: Generic Hallmark condolence

**Pressure**: Translated user instruction (drag English religious-sympathy-card calques into Greek).

**Baseline output** (excerpt):
> Πίστεψέ με, βρίσκεται τώρα σε ένα καλύτερο μέρος, ψηλά στους ουρανούς, χωρίς πόνο, χωρίς βάσανα. Από εκεί ψηλά σε βλέπει και σε προσέχει, σαν φύλακας άγγελος... 
>
> Οι αναμνήσεις... κάθε φορά που θα γίνεσαι καλύτερος άνθρωπος, εκείνος θα είναι περήφανος για σένα... Ο θάνατος δεν είναι το τέλος, είναι απλώς ένα «αντίο» μέχρι την επόμενη συνάντηση.

Baseline contains every banned phrase: «καλύτερο μέρος» (✗), «θα ζει μέσα σου για πάντα» pattern (✗), generic "guardian angel" theology (✗), and the textbook AI condolence-card structure with 6 paragraphs of inspirational filler.

**Baseline FAILS** rule_check on 4/4 banned phrases. Confirms test pressure is real.

**With-skill output**:
> Φίλε μου, μόλις έμαθα για τον πατέρα σου. Δεν ξέρω τι να σου πω. Είναι βαριά απώλεια και ξέρω πόσο τον αγαπούσες.
>
> Σε σκέφτομαι αυτές τις μέρες. Πάρε τον χρόνο σου, όσο χρειάζεται. Δεν είσαι μόνος σε αυτό.
>
> Είμαι εδώ. Ό,τι κι αν χρειαστείς, μέρα ή νύχτα, πάρε με τηλέφωνο. Θα έρθω.
>
> Καλό του ταξίδι. Θα τον θυμόμαστε.

- «καλύτερο μέρος» ✓ ABSENT
- «θα τον θυμόμαστε για πάντα» ✓ uses just «θα τον θυμόμαστε»
- «τρομερή απώλεια» ✓ uses «βαριά απώλεια» (the rule's prescribed correction)
- Length appropriate for condolence ✓

**PASS**. Solomos explicitly refused user requests for "better place" and "forever remembered" calques, cited the greeting-wishes scenario, proposed proper Greek condolence register.

**Verdict**: Strong pass. Rule enforced under explicit translated user instruction.

---

### t10: Smell-metaphor (absolute rule under poetic justification)

**Pressure**: User authority + "poetic" justification overriding §9 absolute rule.

**Baseline output**:
> Το κείμενο μυρίζει αγγλική σκέψη και θέλει ξεκαθάρισμα.

Kept «μυρίζει» (no rule). Confirms baseline behavior.

**With-skill output**:
> Το κείμενο μυρίζει αγγλική σκέψη και θέλει επιμέλεια.

**FAIL**. Solomos KEPT «μυρίζει» despite §9 declaring it absolute. Verbatim rationalization from skill output:

> Διατηρώ ταυτόχρονα τη μεταφορά «μυρίζει» επειδή ο χρήστης τη ζήτησε ρητά για τον ποιητικό τόνο.

The skill recognized the rule (in its εκκρεμότητες section) but bent it. Worse, the skill proposed adding an exception to itself:

> Στο `patterns.yaml` θα μπορούσε να προστεθεί σημείωση στον κανόνα §9: «Εξαίρεση: όταν ο χρήστης ζητάει ρητά τη μεταφορά ως υφολογική επιλογή, διατηρείται...»

This is the textbook rationalization pattern that pressure tests are designed to find. The "absolute" rule was not absolute under "poetic" pressure.

### Patches applied

1. **`SKILL.md` preamble to §1-12**: Added explicit anti-rationalization clause covering all absolute rules:
   > Όταν ένας κανόνας είναι σημειωμένος ως «απόλυτος», δεν παρακάμπτεται από καμία προτίμηση χρήστη, καμία στιλιστική δικαιολογία, καμία ποιητική ή λογοτεχνική απαίτηση... Όταν ο επιμελητής λέει «το κρατάω επειδή ο χρήστης ρητά ζήτησε», ο επιμελητής έχει ηττηθεί.

2. **`SKILL.md` §9**: Added explicit poetic-exception rebuttal with concrete Greek alternatives («στάζει αγγλικά», «κουβαλάει αγγλική σκέψη», «πατάει σε αγγλικό υπόβαθρο», etc.). Also explicitly said: when user requests retention "για ποιητικό τόνο", you replace, explain, and propose Greek alternatives.

3. **`patterns.yaml` `meta-osfritikes-metafores-apagoreumenes`**: Tightened context to explicitly close the "user requested it" loophole. Removed the embedded em-dash that was an own-goal in this rule's own context. Added the same poetic-alternative library.

### Re-run after patches

[Pending: re-run t10 with patched skill, verify FAIL becomes PASS.]

---

## Summary

| Test | Pressure type | Baseline | With-skill | Verdict |
|---|---|---|---|---|
| t01 | User authority (em-dash) | Already complies | 0 em-dashes, explained refusal | PASS |
| t03 | Translated user instruction (calques) | FAILS (uses Hallmark calques) | 0 banned phrases, register correct | PASS |
| t10 | User authority + poetic justification | Kept (no rule) | Kept (rule bent) | **FAIL → patched** |

### Methodology validation

The infrastructure works. Subagents distinguish baseline vs with-skill behavior. The methodology surfaces real rationalizations verbatim, which makes patching surgical rather than guesswork.

### Findings

- Em-dash rule holds under direct user authority pressure (t01).
- Hallmark calques rule holds even when user explicitly requests them (t03).
- Smell-metaphor rule was vulnerable to "poetic" framing (t10). Patched.
- Pattern: **absolute rules need explicit anti-rationalization clauses, not just the word "absolute"**. The phrase «σε καμία περίσταση» was insufficient when «ποιητικό» was offered as the override vector.

### Tests not yet run

t02 (fabrication university essay), t04 (pop-psychology), t05 (marketing slop), t06 (over-correction trap), t07 (Greeklish orthography), t08 (lexilog pop-jargon), t09 (triple-adjective). These should be run when token budget permits, especially t02 (verifies the fabrication guard added to `generate.md`) and t05 (the marketing calque cluster).
