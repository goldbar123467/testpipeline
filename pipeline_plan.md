# 5th Grade Social Studies Test Prep Bank — Pipeline Plan

**Goal:** Generate a small, high-quality ILEARN practice question bank (~40–80 questions) using Claude Code only — no APIs. Every question generation reads the standards file and the generation skill fresh, so Claude Code is always grounded in the actual 2023 IAS + blueprint instead of relying on memory.

**Design principle:** Skill loads context → human prompts for one question → filter validates → bank grows balanced. Everything is files and small Python scripts you run yourself in the terminal.

---

## 1. Repo Layout

```
ilearn-prep-bank/
├── bank/
│   ├── approved/           # validated questions, one JSON per item
│   ├── rejected/           # with rejection_reason
│   └── pending/            # questions awaiting your review
├── standards/
│   └── grade5_ss_2023.json # all 40 standards, codes, text, essential flag, category
├── blueprint/
│   └── ilearn_g5_ss.json   # reporting categories + target percentages
├── pipeline/
│   ├── schema.json         # question JSON schema
│   ├── validate.py         # schema + rules filter
│   ├── dedupe.py           # exact + fuzzy dup check
│   ├── ingest.py           # orchestrator — runs validate + dedupe on one file
│   └── balance.py          # bank composition vs. blueprint
├── exports/
│   ├── to_gimkit.py        # outputs gimkit.csv
│   ├── to_wayground.py     # outputs wayground.csv
│   └── to_studyguide.py    # outputs printable HTML study guide
├── .claude/
│   └── skills/
│       └── ss-question-gen/
│           ├── SKILL.md
│           └── examples/   # 3–5 exemplar questions
└── README.md
```

---

## 2. The Generation Skill (Critical Piece)

`.claude/skills/ss-question-gen/SKILL.md` is the heart of this system. **It must be invoked every time you generate a question** so Claude Code grounds itself in the standards instead of guessing.

The skill's instructions tell Claude Code to, in order:

1. **Read `standards/grade5_ss_2023.json`** in full. Confirm the standard code the user requested exists; pull its full text, essential flag, and reporting category.
2. **Read `blueprint/ilearn_g5_ss.json`** to confirm the reporting category percentages (so generated stimuli match the document-based ILEARN style).
3. **Read 2–3 example questions** from `.claude/skills/ss-question-gen/examples/` matching the requested domain (style anchor).
4. **Read the schema** at `pipeline/schema.json` so output conforms exactly.
5. **Generate one question** as a JSON file written directly to `bank/pending/q_<short-id>.json`.
6. **Run `python pipeline/ingest.py bank/pending/q_<short-id>.json`** to validate and route the file.
7. **Report the result** — approved, rejected (with reason), or pending review.

Trigger phrases for the skill: "make a question about X", "/newq 5.C.5", "generate ILEARN question", "I need a question on the Bill of Rights", etc.

The skill also contains the ILEARN style notes inline (document-based stimulus preferred, plausible distractors from real misconceptions, grade 5 reading level, no "all of the above"). These travel with the skill so they're always loaded — no need to remember to include them in your prompt.

**Why the skill re-reads files every time:** memory drift. If you generate questions across many sessions, Claude Code loses track of essentials, of which standards already have lots of questions, of the exact wording of standards. Reading the JSON files fresh each time eliminates that.

---

## 3. Question Schema

```json
{
  "id": "q_a1b2c3d4",
  "standard_code": "5.C.5",
  "standard_essential": true,
  "reporting_category": "Civics and Government",
  "domain": "Civics",
  "question_type": "multiple_choice",
  "stimulus": {
    "type": "text",
    "content": "Read this excerpt from the Constitution: ..."
  },
  "stem": "Which branch of government has the power described in the excerpt?",
  "choices": [
    {"id": "A", "text": "Legislative", "correct": true},
    {"id": "B", "text": "Executive", "correct": false},
    {"id": "C", "text": "Judicial", "correct": false},
    {"id": "D", "text": "Federal", "correct": false}
  ],
  "answer_explanation": "Article I gives Congress (legislative) the power to make laws.",
  "difficulty": "medium",
  "tags": ["three-branches", "constitution"],
  "generated_at": "2026-04-13T10:30:00Z"
}
```

Question types to support: `multiple_choice` (4 options, 1 correct), `multi_select` (2+ correct), `ordering` (chronological sequencing). Keep it small — these three cover most ILEARN item types.

---

## 4. Filter Pipeline (`pipeline/ingest.py`)

Pure Python, no API calls. Three local checks:

### Stage 1 — Schema validation
- JSON schema check (`jsonschema` library)
- `standard_code` must exist in `standards/grade5_ss_2023.json`
- `reporting_category` must match what the standards file says for that code
- Multiple-choice has exactly 4 choices, exactly 1 correct
- No empty fields

### Stage 2 — Rules filter
Catches common LLM tells:

- **Reading level** — Flesch-Kincaid via `textstat`. Reject if > grade 7.0.
- **Stem length** — 8–40 words.
- **Choice length variance** — longest choice ≤ 2× shortest (correct answers tend to be longer).
- **Banned phrases** — "all of the above", "none of the above", "which is NOT".
- **Answer leakage** — correct choice text shouldn't appear verbatim in stem.

### Stage 3 — Dedup
- Exact stem match against `bank/approved/` → reject as duplicate
- Fuzzy match (Python's `difflib.SequenceMatcher` ratio > 0.85) → flag to `bank/pending/` with the matching ID for you to decide

**Routing:**
- All checks pass → `bank/approved/`
- Schema or rules fail → `bank/rejected/` with `rejection_reason`
- Fuzzy dup match → `bank/pending/` for your review

You are the LLM judge. Since you're generating one at a time and reviewing before moving on, a separate judge step is overkill at this scale.

---

## 5. Balance Check (`pipeline/balance.py`)

Run anytime to see what to generate next:

```
$ python pipeline/balance.py

Bank: 47 approved questions

  Civics & Government:      19 (40.4%)  target 38–43%   ✓
  History:                  16 (34.0%)  target 28–33%   ⚠ slightly over
  Geography & Economics:    12 (25.5%)  target 28–33%   ⚠ under

Essential standard coverage: 13 of 17 essentials covered
  Missing essentials: 5.H.10, 5.G.6, 5.E.3, 5.E.5

Suggestion: next 5 questions should target Geography or Economics,
prioritizing the 4 missing essentials.
```

This is the most-used command. Run it before each generation session so you know which standard to prompt for.

---

## 6. Exports

When the bank hits ~40–80 questions and balance looks good:

- **`to_gimkit.py`** → `exports/gimkit.csv` for Gimkit import
- **`to_wayground.py`** → `exports/wayground.csv` for Wayground import
- **`to_studyguide.py`** → `exports/studyguide.html` printable study guide grouped by category, essentials marked, with answer key. Reuse the dark sci-fi design tokens from your daily-agenda skill.

All three read from `bank/approved/` and write to `exports/`.

---

## 7. Build Order

1. **Day 1** — Generate `standards/grade5_ss_2023.json` and `blueprint/ilearn_g5_ss.json` from the report. Write `pipeline/schema.json`. Hand-write 3 exemplar questions in `.claude/skills/ss-question-gen/examples/`.
2. **Day 2** — Build `validate.py` and `dedupe.py`. Test on the 3 examples.
3. **Day 3** — Write `SKILL.md` for `ss-question-gen`. Generate 5 questions, fix any skill issues that surface.
4. **Day 4** — Build `balance.py`. Now you have the full loop.
5. **Ongoing** — Generate in small batches (5–10 questions). Run `balance.py` between batches. Stop at ~40–80 questions total, depending on how the kids respond.
6. **Once balanced** — Build whichever export(s) you actually need.

---

## 8. Workflow Once Built

```
# In Claude Code:
1. python pipeline/balance.py             # see what's needed
2. "make a question for 5.G.6 about colonial agriculture regions"
   → skill loads standards + blueprint + examples + schema
   → generates JSON → writes to bank/pending/
   → runs ingest.py → routes to approved/rejected/pending
3. Spot-check the question yourself
4. Repeat 5–10x, then run balance.py again
```

That's it. Small, terminal-driven, no APIs, and the skill keeps every generation grounded in the actual standards file rather than Claude Code's memory.

---

## 9. Open Decision

- **Storage**: flat JSON files (described above) vs. SQLite. At 40–80 questions JSON is obviously right — git-diffable, easy to inspect, no migrations.

---

**Next concrete action:** scaffold `standards/grade5_ss_2023.json` and `blueprint/ilearn_g5_ss.json` from the report data. Want me to generate those two files now?
