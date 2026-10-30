#!/usr/bin/env python3
"""Static check for the Solomos skill.

Catches structural drift, stale files, and regression of past wording fixes.
Does NOT evaluate runtime writing quality, scenario depth, or Greek
naturalness, those are covered by tests/test_prompts.yaml and exemplar-audit.

Run from the skill root:

    python3 tests/static_check.py

Exit code: 0 on PASS, 1 on FAIL.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/scenarios.md",
]

STALE_ROOT_FILES = [
    "critique.md",
    "polish.md",
    "refine.md",
    "few_shot.yaml",
    "patterns.yaml",
    "SKILL.en.md",
    "critique.en.md",
    "polish.en.md",
    "refine.en.md",
    # Removed in the single-file restructure; must not come back.
    "references/generate.md",
    "references/polish.md",
    "references/critique.md",
    "references/refine.md",
    "references/judgment.md",
    "references/patterns.yaml",
    "references/few_shot.yaml",
    "references/positive-patterns.md",
    "scenarios/README.md",
]

BAD_TERMS = [
    "μυρίζει αγγλικά",
    "τρέχει checks",
    "prompt+context",
    "Default register",
    "Παραδοτέο format",
    "## Output",
    "## Inputs",
    "Final check",
]

# Product files. Tests/* and the script itself are excluded on purpose.
SCAN_GLOBS = [
    "SKILL.md",
    "README.md",
    "references/*.md",
]

# Substrings on the same line that justify keeping `formatting` (English noun).
FORMATTING_CONTEXT_HINTS = (
    "markdown",
    "latex",
    "word",
    "rendering",
    "επιπλέον",
    "example",
)

# §9: em-dash (U+2014) and en-dash (U+2013) are banned in Greek prose.
# A line containing one is allowed ONLY when it is documenting the rule or
# the single literary-dialogue exception. If a real dialogue/screenplay
# scenario is ever added, extend this allowlist accordingly.
DASH_CHARS = ("—", "–")
DASH_EXCEPTION_MARKERS = (
    "em-dash",
    "en-dash",
    "λογοτεχνικός διάλογος",
    "Καλημέρα, είπε",
)


def scan_files():
    files = []
    for pattern in SCAN_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return files


def check_required_files():
    errors = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    return errors


def check_stale_root_files():
    errors = []
    for rel in STALE_ROOT_FILES:
        if (ROOT / rel).is_file():
            errors.append(f"stale root file present: {rel}")
    return errors


def _short(line):
    line = line.strip()
    return line if len(line) <= 120 else line[:117] + "..."


def check_em_dashes():
    hits = []
    for path in scan_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(lines, start=1):
            if not any(d in line for d in DASH_CHARS):
                continue
            if any(marker in line for marker in DASH_EXCEPTION_MARKERS):
                continue
            hits.append(f"{rel}:{lineno}: em/en-dash in Greek prose (§9): {_short(line)}")
    return hits


def check_bad_terms():
    bad_term_hits = []
    followup_hits = []
    formatting_hits = []

    for path in scan_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for lineno, line in enumerate(lines, start=1):
            for term in BAD_TERMS:
                if term in line:
                    bad_term_hits.append(
                        f"{rel}:{lineno}: [{term}] {_short(line)}"
                    )
            if "follow-up" in line:
                followup_hits.append(
                    f"{rel}:{lineno}: untranslated follow-up: {_short(line)}"
                )
            # formatting: allowed only with a legitimate context hint on the same line
            if "formatting" in line.lower():
                lower = line.lower()
                if not any(hint in lower for hint in FORMATTING_CONTEXT_HINTS):
                    formatting_hits.append(
                        f"{rel}:{lineno}: formatting without Markdown/LaTeX/Word/rendering/example context: {_short(line)}"
                    )
    return bad_term_hits, followup_hits, formatting_hits


def main():
    sections = []

    sections.append(("Required files", check_required_files()))
    sections.append(("Stale root files", check_stale_root_files()))

    bad_term_hits, followup_hits, formatting_hits = check_bad_terms()
    sections.append(("Known bad terms", bad_term_hits))
    sections.append(("Untranslated follow-up", followup_hits))
    sections.append(("formatting outside allowed context", formatting_hits))
    sections.append(("Em/en-dash in Greek prose (§9)", check_em_dashes()))

    total = 0
    for name, errs in sections:
        if errs:
            total += len(errs)
            print(f"FAIL {name}: {len(errs)} issue(s)")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS {name}")

    print()
    if total == 0:
        print("OVERALL: PASS")
        return 0
    print(f"OVERALL: FAIL ({total} issue(s))")
    return 1


if __name__ == "__main__":
    sys.exit(main())
