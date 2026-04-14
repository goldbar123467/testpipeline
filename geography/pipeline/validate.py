"""
Stage 1 (schema) + Stage 2 (rules) validation for MS Geography question bank.
Pure Python, no API calls.
"""

import json
import os

import jsonschema
import textstat

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(ROOT, "pipeline", "schema.json")
STANDARDS_PATH = os.path.join(ROOT, "standards", "ms_geography_2023.json")

BANNED_PHRASES = [
    "all of the above",
    "none of the above",
    "which is not",
    "which is NOT",
]

MAX_READING_GRADE = 12.0
STEM_MIN_WORDS = 8
STEM_MAX_WORDS = 40
CHOICE_LENGTH_RATIO = 2.0


def _load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def _build_standards_lookup():
    """Return dict: code -> {text, domain, reporting_category, essential}."""
    data = _load_json(STANDARDS_PATH)
    return {s["code"]: s for s in data["standards"]}


# ---------------------------------------------------------------------------
# Stage 1 — Schema validation
# ---------------------------------------------------------------------------

def validate_schema(question: dict) -> list[str]:
    """Run JSON-schema check + cross-reference against standards file."""
    errors = []

    schema = _load_json(SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema)
    for err in validator.iter_errors(question):
        errors.append(f"Schema: {err.message}")

    if errors:
        return errors  # bail early; rest depends on valid structure

    standards = _build_standards_lookup()
    code = question["standard_code"]

    if code not in standards:
        errors.append(f"Standard code '{code}' not found in standards file.")
        return errors

    std = standards[code]
    if question["reporting_category"] != std["reporting_category"]:
        errors.append(
            f"Reporting category mismatch: question says '{question['reporting_category']}' "
            f"but standards file says '{std['reporting_category']}' for {code}."
        )

    if question["standard_essential"] != std["essential"]:
        errors.append(
            f"Essential flag mismatch: question says {question['standard_essential']} "
            f"but standards file says {std['essential']} for {code}."
        )

    # multiple_choice must have exactly 4 choices, exactly 1 correct
    if question["question_type"] == "multiple_choice":
        if len(question["choices"]) != 4:
            errors.append(f"multiple_choice must have exactly 4 choices, got {len(question['choices'])}.")
        correct_count = sum(1 for c in question["choices"] if c["correct"])
        if correct_count != 1:
            errors.append(f"multiple_choice must have exactly 1 correct answer, got {correct_count}.")

    # multi_select must have 2+ correct
    if question["question_type"] == "multi_select":
        correct_count = sum(1 for c in question["choices"] if c["correct"])
        if correct_count < 2:
            errors.append(f"multi_select must have 2+ correct answers, got {correct_count}.")

    # No empty text fields
    for field in ("stem", "answer_explanation"):
        if not question.get(field, "").strip():
            errors.append(f"'{field}' must not be empty.")
    if not question.get("stimulus", {}).get("content", "").strip():
        errors.append("'stimulus.content' must not be empty.")
    for c in question.get("choices", []):
        if not c.get("text", "").strip():
            errors.append(f"Choice '{c.get('id', '?')}' text must not be empty.")

    return errors


# ---------------------------------------------------------------------------
# Stage 2 — Rules filter (catches common LLM tells)
# ---------------------------------------------------------------------------

def validate_rules(question: dict) -> list[str]:
    """Heuristic rules to catch low-quality generations."""
    errors = []

    # --- Reading level (stem only) ---
    grade = round(textstat.flesch_kincaid_grade(question["stem"]), 1)
    if grade > MAX_READING_GRADE:
        errors.append(
            f"Reading level too high: Flesch-Kincaid grade {grade:.1f} "
            f"(max {MAX_READING_GRADE})."
        )

    # --- Stem length ---
    word_count = len(question["stem"].split())
    if word_count < STEM_MIN_WORDS:
        errors.append(f"Stem too short: {word_count} words (min {STEM_MIN_WORDS}).")
    if word_count > STEM_MAX_WORDS:
        errors.append(f"Stem too long: {word_count} words (max {STEM_MAX_WORDS}).")

    # --- Choice length variance ---
    lengths = [len(c["text"]) for c in question["choices"]]
    if lengths:
        shortest = min(lengths)
        longest = max(lengths)
        if shortest > 0 and longest / shortest > CHOICE_LENGTH_RATIO:
            errors.append(
                f"Choice length variance too high: longest ({longest} chars) > "
                f"{CHOICE_LENGTH_RATIO}x shortest ({shortest} chars)."
            )

    # --- Banned phrases ---
    stem_lower = question["stem"].lower()
    for phrase in BANNED_PHRASES:
        if phrase.lower() in stem_lower:
            errors.append(f"Banned phrase in stem: '{phrase}'.")
    for c in question["choices"]:
        text_lower = c["text"].lower()
        for phrase in BANNED_PHRASES:
            if phrase.lower() in text_lower:
                errors.append(f"Banned phrase in choice {c['id']}: '{phrase}'.")

    # --- Answer leakage ---
    correct_texts = [c["text"].lower().strip() for c in question["choices"] if c["correct"]]
    for ct in correct_texts:
        if ct and ct in stem_lower:
            errors.append(
                f"Answer leakage: correct answer text appears verbatim in stem."
            )

    return errors


# ---------------------------------------------------------------------------
# Combined entry point
# ---------------------------------------------------------------------------

def validate(question: dict) -> tuple[list[str], list[str]]:
    """Run all validation. Returns (schema_errors, rule_errors)."""
    schema_errors = validate_schema(question)
    if schema_errors:
        return schema_errors, []
    rule_errors = validate_rules(question)
    return schema_errors, rule_errors
