# ILEARN 5th Grade Social Studies — Question Bank Pipeline

Generate, validate, and export a balanced practice question bank (~40–80 questions) aligned to the 2023 Indiana Academic Standards and ILEARN blueprint.

## Setup

```bash
pip install jsonschema textstat python-docx
```

## Quick Start

```bash
# 1. Check what the bank needs
python pipeline/balance.py

# 2. Generate a question (use the Claude Code skill)
#    "make a question for 5.G.6 about natural resources and regional economy"

# 3. Export when balanced
python exports/to_gimkit.py        # → exports/gimkit.csv
python exports/to_studyguide.py    # → exports/studyguide.docx
```

## Repo Layout

```
bank/
  approved/        Validated questions (one JSON per item)
  rejected/        Failed validation (includes rejection_reason)
  pending/         Awaiting your review (fuzzy duplicates)
standards/         grade5_ss_2023.json — all 40 standards
blueprint/         ilearn_g5_ss.json — reporting category targets
pipeline/
  schema.json      Question JSON schema
  validate.py      Schema + rules filter
  dedupe.py        Exact + fuzzy duplicate check
  ingest.py        Orchestrator (validate → dedupe → route)
  balance.py       Bank composition vs. blueprint
exports/
  to_gimkit.py     Gimkit CSV export
  to_studyguide.py Printable DOCX study guide
.claude/skills/
  ss-question-gen/ Claude Code generation skill + examples
```

## Pipeline Stages

1. **Schema** — JSON schema check, standard code exists, category matches, choice count correct
2. **Rules** — Flesch-Kincaid ≤ grade 7, stem 8–40 words, choice length balanced, no banned phrases, no answer leakage
3. **Dedup** — exact stem match → reject; fuzzy match (>0.85) → flag for review

## Exports

- **Gimkit** — `Question, Answer, Alt 1, Alt 2, Alt 3` CSV
- **Study Guide** — Word doc grouped by category, essentials starred, answer key at back
