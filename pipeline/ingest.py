#!/usr/bin/env python3
"""
Orchestrator — runs validate + dedupe on one question file,
then routes it to approved/, rejected/, or pending/.

Usage:
    python pipeline/ingest.py bank/pending/q_abc123.json
"""

import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from pipeline.validate import validate
from pipeline.dedupe import check_duplicates

APPROVED_DIR = os.path.join(ROOT, "bank", "approved")
REJECTED_DIR = os.path.join(ROOT, "bank", "rejected")
PENDING_DIR = os.path.join(ROOT, "bank", "pending")


def ingest(filepath: str) -> dict:
    """
    Validate and route a question file.
    Returns {"result": "approved"|"rejected"|"pending", "details": ...}
    """
    filepath = os.path.abspath(filepath)
    if not os.path.isfile(filepath):
        return {"result": "error", "details": f"File not found: {filepath}"}

    with open(filepath, "r") as f:
        question = json.load(f)

    filename = os.path.basename(filepath)

    # --- Stage 1 + 2: validate ---
    schema_errors, rule_errors = validate(question)

    if schema_errors or rule_errors:
        all_errors = schema_errors + rule_errors
        question["rejection_reason"] = "; ".join(all_errors)
        dest = os.path.join(REJECTED_DIR, filename)
        with open(dest, "w") as f:
            json.dump(question, f, indent=2)
        # Remove from source if it's not already in rejected/
        if os.path.abspath(os.path.dirname(filepath)) != os.path.abspath(REJECTED_DIR):
            os.remove(filepath)
        return {"result": "rejected", "details": all_errors}

    # --- Stage 3: dedupe ---
    dup_result = check_duplicates(question)

    if dup_result["status"] == "exact_dup":
        reason = f"Exact duplicate of {dup_result['match_id']}"
        question["rejection_reason"] = reason
        dest = os.path.join(REJECTED_DIR, filename)
        with open(dest, "w") as f:
            json.dump(question, f, indent=2)
        if os.path.abspath(os.path.dirname(filepath)) != os.path.abspath(REJECTED_DIR):
            os.remove(filepath)
        return {"result": "rejected", "details": [reason]}

    if dup_result["status"] == "fuzzy_dup":
        reason = (
            f"Fuzzy duplicate (ratio={dup_result['ratio']}) of "
            f"{dup_result['match_id']} — needs your review"
        )
        dest = os.path.join(PENDING_DIR, filename)
        if os.path.abspath(filepath) != os.path.abspath(dest):
            shutil.move(filepath, dest)
        return {"result": "pending", "details": [reason]}

    # --- All clear → approved ---
    dest = os.path.join(APPROVED_DIR, filename)
    with open(dest, "w") as f:
        json.dump(question, f, indent=2)
    if os.path.abspath(os.path.dirname(filepath)) != os.path.abspath(APPROVED_DIR):
        if os.path.exists(filepath):
            os.remove(filepath)
    return {"result": "approved", "details": []}


def main():
    if len(sys.argv) < 2:
        print("Usage: python pipeline/ingest.py <question.json>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isabs(filepath):
        filepath = os.path.join(ROOT, filepath)

    result = ingest(filepath)

    status = result["result"].upper()
    if result["result"] == "approved":
        print(f"  ✓ {status}: {os.path.basename(filepath)} → bank/approved/")
    elif result["result"] == "rejected":
        print(f"  ✗ {status}: {os.path.basename(filepath)} → bank/rejected/")
        for d in result["details"]:
            print(f"    - {d}")
    elif result["result"] == "pending":
        print(f"  ⚠ {status}: {os.path.basename(filepath)} → bank/pending/")
        for d in result["details"]:
            print(f"    - {d}")
    else:
        print(f"  ERROR: {result['details']}")

    return result


if __name__ == "__main__":
    main()
