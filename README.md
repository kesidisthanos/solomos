# Σολωμός

Skill για το [Claude Code](https://claude.com/claude-code) που γράφει, επιμελείται και μεταφράζει ελληνικό κείμενο ώστε να διαβάζεται σαν να το έγραψε Έλληνας. Εντοπίζει δύο ειδών σημάδια: όσα αφήνει κάθε γλωσσικό μοντέλο (αντιθέσεις του τύπου «δεν είναι Χ, είναι Υ», κλεισίματα μιας γραμμής, τριάδες, φουσκωμένη σημασία) και όσα αφήνει η σκέψη που ξεκίνησε στα αγγλικά (calques, αγγλική σύνταξη, αμετάφραστοι όροι, παύλες).

## Εγκατάσταση

### Claude Code

```text
/plugin marketplace add kesidisthanos/solomos
/plugin install solomos@solomos
```

### Codex

```bash
npx skills add kesidisthanos/solomos --global --agent codex
```

### Claude.ai και Claude Desktop

Κατέβασε το αποθετήριο ως ZIP (**Code → Download ZIP**) και ανέβασέ το ως skill στις Ρυθμίσεις.

### Άλλα εργαλεία

```bash
npx skills add kesidisthanos/solomos --global --agent '*'
```

Για εργαλείο που δεν υποστηρίζεται, αντίγραψε το `SKILL.md` και τον φάκελο `references/` στον φάκελο skills του.

## Πώς το καλείς

Ζήτα κάτι στα ελληνικά, ή δώσε κείμενο για επιμέλεια:

- «επιμελήσου αυτό το κείμενο: ...»
- «διόρθωσε τη μηχανική μετάφραση: ...»
- «γράψε email στον λογιστή μου ότι αργώ μια εβδομάδα με τα παραστατικά»
- «μετάφρασε φυσικά στα ελληνικά: ...»

## Παράδειγμα

**Πρωτότυπο:**

> Σας γράφω σήμερα για να ακουμπήσουμε βάση σχετικά με τη νέα στρατηγική. Στο τέλος της ημέρας, εγώ πιστεύω ότι είναι κρίσιμο να κάνουμε focus στην εμπειρία του χρήστη.

**Επιμελημένο:**

> Για τη νέα στρατηγική: τελικά, πρέπει να εστιάσουμε στην εμπειρία του χρήστη.

## Αρχεία

```
solomos/
├── SKILL.md                 # όλες οι οδηγίες: τρόπος δουλειάς και 24 μοτίβα κατά σειρά ισχύος
├── references/
│   └── scenarios.md         # μορφή, μήκος και παγίδες ανά είδος κειμένου
├── .claude-plugin/          # plugin και marketplace για το Claude Code
├── agents/openai.yaml       # όνομα και περιγραφή για Codex
└── tests/                   # στατικός έλεγχος και υλικό δοκιμών
```

Κάθε μοτίβο στο `SKILL.md` έχει την ίδια μορφή: Πρόσεξε (φράσεις), Πρόβλημα (γιατί), Πριν, Μετά. Η δομή ακολουθεί το [humanizer](https://github.com/blader/humanizer), προσαρμοσμένη στα ελληνικά.

Στατικός έλεγχος:

```bash
python3 tests/static_check.py
```

## Συνεισφορά

Νέα μοτίβα και διορθώσεις είναι ευπρόσδεκτα σε [issue](https://github.com/kesidisthanos/solomos/issues) ή pull request. Ένα νέο μοτίβο χρειάζεται Πρόσεξε, Πρόβλημα, Πριν και Μετά, και θέση στην κατάταξη: όσο πιο σπάνια θα το έκανε σκόπιμα ένας προσεκτικός Έλληνας, τόσο πιο ψηλά.

## Άδεια χρήσης

[MIT](LICENSE).

---

## English summary

**Solomos** is a Claude Code skill for writing, editing, and translating Greek so it reads as if a native writer wrote it. It targets two sources of tells: generic language-model habits (not-X-but-Y contrasts, one-line closers, forced triads, inflated significance) and English-first thinking (calques, English word order, untranslated terms, dashes). The whole method lives in one file, `SKILL.md`, with 24 patterns ranked strongest first, each with a before/after example. The structure follows [humanizer](https://github.com/blader/humanizer), adapted for Greek.
