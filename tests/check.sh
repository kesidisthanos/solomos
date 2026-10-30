#!/usr/bin/env bash
# Solomos QA gate.
# Runs the static check. If it passes, prints short reminders about
# the runtime side of QA. Run from the skill root.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"

cd "$ROOT"
python3 tests/static_check.py

cat <<'EOF'

Reminders:
  - Review tests/test_prompts.yaml for regression prompts.
  - Use tests/runtime_review.md for manual runtime scoring.
  - Do not patch the skill based on one weak output unless the failure
    is severe or recurring across tests.
EOF
