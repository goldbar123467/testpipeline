# Skill: ILEARN 5th Grade Social Studies Question Generator

## Trigger Phrases
- "make a question about …"
- "generate ILEARN question"
- "/newq 5.C.5"
- "I need a question on …"

## Instructions

When this skill is invoked, follow these steps **in order** every single time. Never skip a read step — the point is to ground every generation in the actual files, not memory.

### Step 1 — Read the Standards
Read `standards/grade5_ss_2023.json` in full. Find the standard code the user requested. Confirm it exists and pull its:
- full text
- essential flag
- reporting category
- domain

If the code doesn't exist, tell the user and stop.

### Step 2 — Read the Blueprint
Read `blueprint/ilearn_g5_ss.json`. Note the reporting category percentages so the question style matches ILEARN weighting.

### Step 3 — Read Example Questions
Read 2–3 example questions from `.claude/skills/ss-question-gen/examples/` that match the requested domain. Use these as style anchors for tone, length, and difficulty calibration.

### Step 4 — Read the Schema
Read `pipeline/schema.json`. The generated question must conform to this schema exactly.

### Step 5 — Generate One Question
Generate a single question as a JSON file. Write it to `bank/pending/q_<short-id>.json` where `<short-id>` is 8 random lowercase hex characters.

**ILEARN Style Rules (always apply):**
- **Stimulus first.** Prefer document-based stimuli (excerpt, quote, short passage, table description). The stimulus gives context; the stem asks about it.
- **Grade 5 reading level.** Keep Flesch-Kincaid at or below grade 7. Use simple sentences. Avoid jargon.
- **4 choices for multiple_choice** — exactly 1 correct. Distractors must be plausible and based on real student misconceptions, not obviously wrong.
- **2+ correct for multi_select** — stem must say "Which TWO…" or "Select TWO…"
- **Never use:** "all of the above", "none of the above", "which is NOT"
- **Choice length:** keep all choices roughly similar length. The correct answer should not be noticeably longer than distractors.
- **No answer leakage:** the correct answer text must not appear verbatim in the stem.
- **Tags:** include 2–4 lowercase kebab-case tags relevant to the content.
- **Difficulty:** easy / medium / hard — match to grade-level expectations.
- **generated_at:** use current ISO 8601 timestamp.

### Step 6 — Run the Ingest Pipeline
Run: `python pipeline/ingest.py bank/pending/q_<short-id>.json`

This validates schema, checks rules, and runs dedup. The file gets routed to:
- `bank/approved/` — all checks passed
- `bank/rejected/` — failed validation (with rejection_reason)
- `bank/pending/` — fuzzy duplicate flagged for your review

### Step 7 — Report
Tell the user the result:
- **Approved:** "✓ Question approved and saved to bank/approved/"
- **Rejected:** "✗ Rejected — [reason]. Want me to fix and retry?"
- **Pending:** "⚠ Flagged as possible duplicate of [match_id]. Review needed."
