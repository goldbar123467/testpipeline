"""
Stage 3 — Deduplication check for MS Geography question bank.
Exact stem match → reject.  Fuzzy match (>0.85) → flag to pending.
"""

import difflib
import json
import os
import glob as globmod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPROVED_DIR = os.path.join(ROOT, "bank", "approved")
FUZZY_THRESHOLD = 0.85


def _load_approved_stems() -> list[dict]:
    """Load id + stem from every approved question."""
    items = []
    for path in globmod.glob(os.path.join(APPROVED_DIR, "*.json")):
        with open(path, "r") as f:
            data = json.load(f)
        items.append({"id": data["id"], "stem": data["stem"], "path": path})
    return items


def check_duplicates(question: dict) -> dict:
    """
    Returns:
        {"status": "clean"}                    — no duplicates found
        {"status": "exact_dup", "match_id": …} — exact stem match
        {"status": "fuzzy_dup", "match_id": …, "ratio": float}
                                                — fuzzy match above threshold
    """
    new_stem = question["stem"].strip()
    approved = _load_approved_stems()

    for item in approved:
        # Skip self (re-ingesting the same file)
        if item["id"] == question["id"]:
            continue

        existing_stem = item["stem"].strip()

        # Exact match
        if new_stem.lower() == existing_stem.lower():
            return {"status": "exact_dup", "match_id": item["id"]}

        # Fuzzy match
        ratio = difflib.SequenceMatcher(None, new_stem.lower(), existing_stem.lower()).ratio()
        if ratio > FUZZY_THRESHOLD:
            return {"status": "fuzzy_dup", "match_id": item["id"], "ratio": round(ratio, 3)}

    return {"status": "clean"}
