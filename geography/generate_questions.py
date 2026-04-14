#!/usr/bin/env python3
"""
Generate Middle School Geography questions and write to bank/pending/.
Then ingest each through the pipeline.

Usage:
    python geography/generate_questions.py
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PENDING_DIR = os.path.join(ROOT, "bank", "pending")
sys.path.insert(0, ROOT)

from pipeline.ingest import ingest

TIMESTAMP = "2026-04-14T10:00:00Z"


def write_and_ingest(question):
    """Write question to pending/, then run through pipeline."""
    path = os.path.join(PENDING_DIR, f"{question['id']}.json")
    with open(path, "w") as f:
        json.dump(question, f, indent=2)
    result = ingest(path)
    status = result["result"].upper()
    if result["result"] == "approved":
        print(f"  \u2713 {status}: {question['id']}")
    elif result["result"] == "rejected":
        print(f"  \u2717 {status}: {question['id']}")
        for d in result["details"]:
            print(f"      {d}")
    else:
        print(f"  \u26a0 {status}: {question['id']}")
        for d in result["details"]:
            print(f"      {d}")
    return result


# ══════════════════════════════════════════════════════════════════════
#  ALL QUESTIONS
# ══════════════════════════════════════════════════════════════════════

ALL_QUESTIONS = [

    # ── PHYSICAL GEOGRAPHY (25 questions) ─────────────────────────────

    # PG.1 - Major physical features
    {
        "id": "q_pg0001",
        "standard_code": "6-8.PG.1",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Read the description below:\n\nThis landform is a large, flat area of land that is raised above the surrounding land on at least one side. It is sometimes called a tableland. The Colorado Plateau in the southwestern United States is one example."},
        "stem": "Based on the description, which type of landform is being described?",
        "choices": [
            {"id": "A", "text": "A plateau", "correct": True},
            {"id": "B", "text": "A valley", "correct": False},
            {"id": "C", "text": "A peninsula", "correct": False},
            {"id": "D", "text": "A delta", "correct": False}
        ],
        "answer_explanation": "A plateau is a flat, elevated landform sometimes called a tableland. A valley is low-lying land between hills, a peninsula extends into water, and a delta forms where a river meets the sea.",
        "difficulty": "easy",
        "tags": ["landforms", "plateau", "physical-features"],
        "generated_at": TIMESTAMP
    },
    {
        "id": "q_pg0002",
        "standard_code": "6-8.PG.1",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Study the following facts:\n\n\u2022 The Nile River is the longest river in Africa.\n\u2022 The Amazon River carries more water than any other river.\n\u2022 The Mississippi River drains most of the central United States."},
        "stem": "What do these three rivers have in common as physical features?",
        "choices": [
            {"id": "A", "text": "They all flow into the Atlantic Ocean", "correct": False},
            {"id": "B", "text": "They are all major drainage systems for large land areas", "correct": True},
            {"id": "C", "text": "They are all located on the same continent", "correct": False},
            {"id": "D", "text": "They all begin in mountain ranges above 5,000 meters", "correct": False}
        ],
        "answer_explanation": "All three rivers are major drainage systems that collect water from large land areas called drainage basins. They are on different continents and flow into different bodies of water.",
        "difficulty": "medium",
        "tags": ["rivers", "drainage-systems", "physical-features"],
        "generated_at": TIMESTAMP
    },
    {
        "id": "q_pg0003",
        "standard_code": "6-8.PG.1",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "A geography teacher asks students to list examples of major physical features found on Earth's surface."},
        "stem": "Which TWO of the following are examples of major physical landforms?",
        "choices": [
            {"id": "A", "text": "The Rocky Mountains", "correct": True},
            {"id": "B", "text": "The Great Plains", "correct": True},
            {"id": "C", "text": "The Panama Canal", "correct": False},
            {"id": "D", "text": "The Hoover Dam", "correct": False}
        ],
        "answer_explanation": "The Rocky Mountains and the Great Plains are natural physical landforms. The Panama Canal and the Hoover Dam are human-made structures, not natural physical features.",
        "difficulty": "easy",
        "tags": ["landforms", "physical-features", "human-vs-natural"],
        "generated_at": TIMESTAMP
    },

    # PG.2 - Plate tectonics
    {
        "id": "q_pg0004",
        "standard_code": "6-8.PG.2",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Read the passage below:\n\nEarth's outer layer is broken into large pieces called tectonic plates. These plates float on top of a layer of hot, soft rock deep below the surface. When two plates push against each other, the land can be forced upward over millions of years."},
        "stem": "According to the passage, what happens when two tectonic plates push against each other?",
        "choices": [
            {"id": "A", "text": "Oceans begin to dry up", "correct": False},
            {"id": "B", "text": "Mountains can form over time", "correct": True},
            {"id": "C", "text": "Rivers change their direction", "correct": False},
            {"id": "D", "text": "Deserts spread to new areas", "correct": False}
        ],
        "answer_explanation": "When tectonic plates collide, land is forced upward, forming mountains over millions of years. This process does not directly cause oceans to dry up, rivers to change direction, or deserts to spread.",
        "difficulty": "easy",
        "tags": ["plate-tectonics", "mountains", "convergent-boundary"],
        "generated_at": TIMESTAMP
    },

    # PG.3 - Water cycle
    {
        "id": "q_pg0005",
        "standard_code": "6-8.PG.3",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A student drew a diagram of the water cycle. The diagram shows the sun heating a lake. Water rises as vapor into the air, forms clouds, and then falls back to Earth as rain. The rain flows into streams and rivers and eventually returns to the lake."},
        "stem": "In the student's diagram, what process causes water to rise from the lake into the air?",
        "choices": [
            {"id": "A", "text": "Condensation", "correct": False},
            {"id": "B", "text": "Precipitation", "correct": False},
            {"id": "C", "text": "Evaporation", "correct": True},
            {"id": "D", "text": "Collection", "correct": False}
        ],
        "answer_explanation": "Evaporation is the process where the sun heats liquid water and turns it into water vapor that rises into the air. Condensation forms clouds, precipitation is rain or snow falling, and collection is water gathering in bodies of water.",
        "difficulty": "easy",
        "tags": ["water-cycle", "evaporation", "earth-systems"],
        "generated_at": TIMESTAMP
    },
]


def main():
    print(f"Generating {len(ALL_QUESTIONS)} questions...\n")
    results = {"approved": 0, "rejected": 0, "pending": 0, "error": 0}
    for q in ALL_QUESTIONS:
        r = write_and_ingest(q)
        results[r["result"]] = results.get(r["result"], 0) + 1

    print(f"\n{'='*40}")
    print(f"Total: {len(ALL_QUESTIONS)}")
    print(f"  Approved: {results['approved']}")
    print(f"  Rejected: {results['rejected']}")
    print(f"  Pending:  {results['pending']}")
    if results.get("error"):
        print(f"  Errors:   {results['error']}")


if __name__ == "__main__":
    main()
