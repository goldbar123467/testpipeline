#!/usr/bin/env python3
"""
Export approved questions to Gimkit CSV format.

Gimkit import expects columns:
    Question, Answer, Alt 1, Alt 2, Alt 3

For multi_select questions we join correct answers with " & ".

Usage:
    python exports/to_gimkit.py
    → writes exports/gimkit.csv
"""

import csv
import json
import os
import glob as globmod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPROVED_DIR = os.path.join(ROOT, "bank", "approved")
OUTPUT_PATH = os.path.join(ROOT, "exports", "gimkit.csv")


def load_approved():
    questions = []
    for path in sorted(globmod.glob(os.path.join(APPROVED_DIR, "*.json"))):
        with open(path, "r") as f:
            questions.append(json.load(f))
    return questions


def export():
    questions = load_approved()
    if not questions:
        print("No approved questions to export.")
        return

    rows = []
    for q in questions:
        correct = [c["text"] for c in q["choices"] if c["correct"]]
        incorrect = [c["text"] for c in q["choices"] if not c["correct"]]

        # Gimkit: Question, Answer, then up to 3 wrong answers
        stem = q["stem"]
        if q.get("stimulus", {}).get("content"):
            stem = q["stimulus"]["content"] + "\n\n" + q["stem"]

        answer = " & ".join(correct)
        # Pad incorrect to always have 3 columns
        while len(incorrect) < 3:
            incorrect.append("")

        rows.append([stem, answer, incorrect[0], incorrect[1], incorrect[2]])

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Question", "Answer", "Alt 1", "Alt 2", "Alt 3"])
        writer.writerows(rows)

    print(f"Exported {len(rows)} questions → {OUTPUT_PATH}")


if __name__ == "__main__":
    export()
