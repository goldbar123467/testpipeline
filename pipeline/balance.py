#!/usr/bin/env python3
"""
Bank composition vs. blueprint balance checker.
Shows category distribution, essential standard coverage,
and suggests what to generate next.

Usage:
    python pipeline/balance.py
"""

import json
import os
import glob as globmod
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPROVED_DIR = os.path.join(ROOT, "bank", "approved")
BLUEPRINT_PATH = os.path.join(ROOT, "blueprint", "ilearn_g5_ss.json")
STANDARDS_PATH = os.path.join(ROOT, "standards", "grade5_ss_2023.json")


def load_approved():
    """Load all approved questions."""
    questions = []
    for path in globmod.glob(os.path.join(APPROVED_DIR, "*.json")):
        with open(path, "r") as f:
            questions.append(json.load(f))
    return questions


def load_blueprint():
    with open(BLUEPRINT_PATH, "r") as f:
        return json.load(f)


def load_standards():
    with open(STANDARDS_PATH, "r") as f:
        data = json.load(f)
    return {s["code"]: s for s in data["standards"]}


def analyze():
    questions = load_approved()
    blueprint = load_blueprint()
    standards = load_standards()
    total = len(questions)

    # --- Category distribution ---
    cat_counts = {}
    for cat in blueprint["reporting_categories"]:
        cat_counts[cat["name"]] = 0
    for q in questions:
        rc = q.get("reporting_category", "Unknown")
        cat_counts[rc] = cat_counts.get(rc, 0) + 1

    # --- Essential coverage ---
    essential_codes = [code for code, s in standards.items() if s["essential"]]
    covered_codes = set()
    for q in questions:
        if q.get("standard_essential"):
            covered_codes.add(q["standard_code"])
    missing_essentials = [c for c in essential_codes if c not in covered_codes]

    # --- Standard coverage (all) ---
    all_covered = set(q["standard_code"] for q in questions)
    uncovered_standards = [c for c in standards if c not in all_covered]

    return {
        "total": total,
        "categories": cat_counts,
        "blueprint": blueprint["reporting_categories"],
        "essential_total": len(essential_codes),
        "essential_covered": len(covered_codes),
        "missing_essentials": sorted(missing_essentials),
        "uncovered_standards": sorted(uncovered_standards),
    }


def print_report():
    data = analyze()
    standards = load_standards()
    total = data["total"]

    print(f"\nBank: {total} approved questions\n")

    # Category breakdown
    for cat_info in data["blueprint"]:
        name = cat_info["name"]
        count = data["categories"].get(name, 0)
        pct = (count / total * 100) if total > 0 else 0
        target = f"{cat_info['target_min_pct']}–{cat_info['target_max_pct']}%"

        if total > 0 and cat_info["target_min_pct"] <= pct <= cat_info["target_max_pct"]:
            status = "✓"
        elif total == 0:
            status = "—"
        elif pct < cat_info["target_min_pct"]:
            status = "⚠ under"
        else:
            status = "⚠ over"

        label = f"{name}:"
        print(f"  {label:<30} {count:>3} ({pct:>5.1f}%)  target {target:<10} {status}")

    # Essential coverage
    print(
        f"\nEssential standard coverage: "
        f"{data['essential_covered']} of {data['essential_total']} essentials covered"
    )
    if data["missing_essentials"]:
        print(f"  Missing essentials: {', '.join(data['missing_essentials'])}")
    else:
        print("  All essentials covered!")

    # Suggestions
    if data["missing_essentials"] or data["uncovered_standards"]:
        print()
        # Find the most underrepresented category
        suggestions = []
        if total > 0:
            for cat_info in data["blueprint"]:
                name = cat_info["name"]
                count = data["categories"].get(name, 0)
                pct = count / total * 100
                if pct < cat_info["target_min_pct"]:
                    deficit = cat_info["target_min_pct"] - pct
                    suggestions.append((deficit, name))
            suggestions.sort(reverse=True)

        if suggestions:
            top_cat = suggestions[0][1]
            n = min(5, len(data["missing_essentials"]) + len(data["uncovered_standards"]))
            # Prioritize missing essentials in the under-represented category
            priority = [c for c in data["missing_essentials"]
                        if standards[c]["reporting_category"] == top_cat]
            if not priority:
                priority = data["missing_essentials"][:n]
            print(
                f"Suggestion: next {n} questions should target {top_cat}, "
                f"prioritizing: {', '.join(priority[:n])}"
            )
        elif data["missing_essentials"]:
            print(
                f"Suggestion: cover these missing essentials next: "
                f"{', '.join(data['missing_essentials'][:5])}"
            )
    elif total > 0:
        print("\n✓ Bank looks well-balanced!")

    print()


if __name__ == "__main__":
    print_report()
