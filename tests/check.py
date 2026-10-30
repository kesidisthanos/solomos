#!/usr/bin/env python3
"""Έλεγχος του SKILL.md του Σολωμού.

Βεβαιώνει ότι το αρχείο έχει σωστή κεφαλίδα και ότι το κείμενό του
δεν έχει λατινικούς χαρακτήρες, εικονίδια ή παύλες. Η μόνη παύλα που
επιτρέπεται είναι στη γραμμή του σημαδιού 12, που τις ονομάζει.

Τρέχει από τον φάκελο του Σολωμού:

    python3 tests/check.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"

LATIN = re.compile(r"[A-Za-z]")
ICONS = re.compile("[\U0001F300-\U0001FAFF☀-➿←-⇿]")
DASHES = ("—", "–")
DASH_RULE_MARKER = "μεγάλη παύλα"
MAX_DESCRIPTION = 1024


def main():
    errors = []
    text = SKILL.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        print("ΑΠΟΤΥΧΙΑ: λείπει η κεφαλίδα ανάμεσα σε ---")
        return 1
    header, body = parts[1], parts[2]

    if not re.search(r"^name:\s*solomos\s*$", header, re.M):
        errors.append("κεφαλίδα: λείπει το name: solomos")
    desc = re.search(r"^description:\s*(.+)$", header, re.M)
    if not desc:
        errors.append("κεφαλίδα: λείπει η περιγραφή")
    else:
        d = desc.group(1)
        if len(d) > MAX_DESCRIPTION:
            errors.append(f"κεφαλίδα: η περιγραφή έχει {len(d)} χαρακτήρες, το όριο είναι {MAX_DESCRIPTION}")
        if "<" in d or ">" in d:
            errors.append("κεφαλίδα: η περιγραφή δεν επιτρέπεται να έχει < ή >")
        if LATIN.search(d):
            errors.append("κεφαλίδα: η περιγραφή έχει λατινικούς χαρακτήρες")

    for n, line in enumerate(body.splitlines(), start=1):
        if LATIN.search(line):
            errors.append(f"γραμμή {n}: λατινικοί χαρακτήρες: {line.strip()[:80]}")
        if ICONS.search(line):
            errors.append(f"γραμμή {n}: εικονίδιο ή βελάκι: {line.strip()[:80]}")
        if any(d in line for d in DASHES) and DASH_RULE_MARKER not in line:
            errors.append(f"γραμμή {n}: παύλα: {line.strip()[:80]}")

    if errors:
        for e in errors:
            print(e)
        print(f"\nΑΠΟΤΥΧΙΑ: {len(errors)} προβλήματα")
        return 1
    print("ΕΝΤΑΞΕΙ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
