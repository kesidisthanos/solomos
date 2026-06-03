#!/usr/bin/env python3
"""Static check for the Solomos skill.

Catches structural drift, stale files, and regression of past wording fixes.
Does NOT evaluate runtime writing quality, scenario depth, or Greek
naturalness, those are covered by tests/test_prompts.yaml and exemplar-audit.

Run from the skill root:

    python3 tests/static_check.py

Exit code: 0 on PASS, 1 on FAIL.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/generate.md",
    "references/polish.md",
    "references/critique.md",
    "references/refine.md",
    "references/few_shot.yaml",
    "references/patterns.yaml",
    "references/judgment.md",
    "references/positive-patterns.md",
    "scenarios/README.md",
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
    "references/*.yaml",
    "scenarios/*.md",
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

# §10: em-dash (U+2014) and en-dash (U+2013) are banned in Greek prose.
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


def check_scenario_integrity():
    errors = []
    scen_dir = ROOT / "scenarios"
    if not scen_dir.is_dir():
        errors.append("scenarios/ directory missing")
        return errors

    fs_files = {p.name for p in scen_dir.glob("*.md") if p.name != "README.md"}

    readme = scen_dir / "README.md"
    if not readme.is_file():
        errors.append("scenarios/README.md missing")
        return errors
    text = readme.read_text(encoding="utf-8")
    # Match markdown links of the form [`name.md`](name.md).
    ref_files = set(re.findall(r"\[`([a-z][a-z0-9-]*\.md)`\]", text))

    fs_only = fs_files - ref_files
    ref_only = ref_files - fs_files
    for name in sorted(fs_only):
        errors.append(
            f"scenario {name} exists but is not referenced in scenarios/README.md"
        )
    for name in sorted(ref_only):
        errors.append(
            f"scenarios/README.md references {name} but the file does not exist"
        )
    if len(fs_files) != len(ref_files):
        errors.append(
            f"scenario count mismatch: filesystem={len(fs_files)} README={len(ref_files)}"
        )
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
            hits.append(f"{rel}:{lineno}: em/en-dash in Greek prose (§10): {_short(line)}")
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
            # follow-up: allowed only inside scenarios/translation-from-english.md
            if "follow-up" in line and rel != "scenarios/translation-from-english.md":
                followup_hits.append(
                    f"{rel}:{lineno}: follow-up outside translation-from-english.md: {_short(line)}"
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
    sections.append(("Scenario integrity", check_scenario_integrity()))

    bad_term_hits, followup_hits, formatting_hits = check_bad_terms()
    sections.append(("Known bad terms", bad_term_hits))
    sections.append(("follow-up outside allowed scope", followup_hits))
    sections.append(("formatting outside allowed context", formatting_hits))
    sections.append(("Em/en-dash in Greek prose (§10)", check_em_dashes()))

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
