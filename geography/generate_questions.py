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

    # PG.1 - Major physical features (oceans)
    {
        "id": "q_pg0006",
        "standard_code": "6-8.PG.1",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Pacific Ocean covers more area than all of Earth's land combined. It stretches from Asia and Australia in the west to North and South America in the east."},
        "stem": "Based on the passage, what makes the Pacific Ocean a significant physical feature of Earth?",
        "choices": [
            {"id": "A", "text": "It covers more area than all land on Earth", "correct": True},
            {"id": "B", "text": "It is the warmest of all the world's oceans", "correct": False},
            {"id": "C", "text": "It separates Europe from North America", "correct": False},
            {"id": "D", "text": "It contains the most islands of any ocean", "correct": False}
        ],
        "answer_explanation": "The passage states that the Pacific Ocean covers more area than all of Earth's land combined, making it the largest ocean and a major physical feature.",
        "difficulty": "easy",
        "tags": ["oceans", "pacific", "physical-features"],
        "generated_at": TIMESTAMP
    },

    # PG.2 - Plate tectonics (earthquakes)
    {
        "id": "q_pg0007",
        "standard_code": "6-8.PG.2",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The San Andreas Fault in California is a place where two tectonic plates slide past each other. This type of boundary is called a transform boundary. Movement along the fault has caused many earthquakes in the region."},
        "stem": "Based on the passage, what causes so many earthquakes in California?",
        "choices": [
            {"id": "A", "text": "Two tectonic plates slide past each other there", "correct": True},
            {"id": "B", "text": "The state is located near an active volcano", "correct": False},
            {"id": "C", "text": "Ocean waves wear down the coastline over time", "correct": False},
            {"id": "D", "text": "Strong winds push against the mountain ranges", "correct": False}
        ],
        "answer_explanation": "The passage explains that California's earthquakes are caused by two tectonic plates sliding past each other along the San Andreas Fault, which is a transform boundary.",
        "difficulty": "medium",
        "tags": ["plate-tectonics", "earthquakes", "transform-boundary"],
        "generated_at": TIMESTAMP
    },

    # PG.2 - Plate tectonics (Ring of Fire)
    {
        "id": "q_pg0008",
        "standard_code": "6-8.PG.2",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Ring of Fire is a horseshoe-shaped zone around the edges of the Pacific Ocean. About 75 percent of the world's active volcanoes are found along this zone. The Ring of Fire is also where about 90 percent of earthquakes happen."},
        "stem": "What is the best explanation for why so many volcanoes and earthquakes occur along the Ring of Fire?",
        "choices": [
            {"id": "A", "text": "Many tectonic plate boundaries are located there", "correct": True},
            {"id": "B", "text": "The Pacific Ocean creates strong ocean currents", "correct": False},
            {"id": "C", "text": "The area receives more rainfall than other zones", "correct": False},
            {"id": "D", "text": "Warm temperatures melt rocks beneath the surface", "correct": False}
        ],
        "answer_explanation": "The Ring of Fire has so many volcanoes and earthquakes because it sits along many tectonic plate boundaries where plates collide, pull apart, or slide past each other.",
        "difficulty": "medium",
        "tags": ["plate-tectonics", "ring-of-fire", "volcanoes"],
        "generated_at": TIMESTAMP
    },

    # PG.3 - Water cycle (condensation)
    {
        "id": "q_pg0009",
        "standard_code": "6-8.PG.3",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "After hiking up a mountain on a warm day, a student notices that clouds are forming near the top. The student remembers learning that warm air rises and cools as it goes higher in the atmosphere."},
        "stem": "Which part of the water cycle explains why clouds form near the mountain top?",
        "choices": [
            {"id": "A", "text": "Evaporation turns water into gas near the peak", "correct": False},
            {"id": "B", "text": "Condensation occurs when rising air cools down", "correct": True},
            {"id": "C", "text": "Precipitation falls from clouds to the ground", "correct": False},
            {"id": "D", "text": "Collection gathers water in lakes and streams", "correct": False}
        ],
        "answer_explanation": "Condensation is the process where water vapor cools and turns back into tiny water droplets, forming clouds. As warm air rises up the mountain and cools, condensation occurs.",
        "difficulty": "medium",
        "tags": ["water-cycle", "condensation", "clouds"],
        "generated_at": TIMESTAMP
    },

    # PG.3 - Water cycle (groundwater/runoff)
    {
        "id": "q_pg0010",
        "standard_code": "6-8.PG.3",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "After a heavy rainstorm, water does not stay in one place. Some water soaks into the ground and becomes groundwater. Other water flows downhill across the land into rivers and streams."},
        "stem": "Which TWO processes describe what happens to rainwater after it reaches the ground?",
        "choices": [
            {"id": "A", "text": "It can soak into the soil as infiltration", "correct": True},
            {"id": "B", "text": "It can flow across land as surface runoff", "correct": True},
            {"id": "C", "text": "It rises back into the air as condensation", "correct": False},
            {"id": "D", "text": "It is absorbed directly by the sun above", "correct": False}
        ],
        "answer_explanation": "After rain falls, water either infiltrates (soaks into) the soil to become groundwater, or flows across the surface as runoff into rivers and streams. Condensation occurs in the air, not on the ground.",
        "difficulty": "medium",
        "tags": ["water-cycle", "groundwater", "runoff", "infiltration"],
        "generated_at": TIMESTAMP
    },

    # PG.4 - Climate zones (latitude)
    {
        "id": "q_pg0011",
        "standard_code": "6-8.PG.4",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A geography class is studying three cities. City A is near the equator. City B is halfway between the equator and the North Pole. City C is near the North Pole."},
        "stem": "Based on their locations, which city most likely has the warmest average temperature all year?",
        "choices": [
            {"id": "A", "text": "City A, because it is closest to the equator", "correct": True},
            {"id": "B", "text": "City B, because it is in the middle latitude", "correct": False},
            {"id": "C", "text": "City C, because it receives the most sunlight", "correct": False},
            {"id": "D", "text": "City B, because middle zones trap the most heat", "correct": False}
        ],
        "answer_explanation": "Places near the equator receive the most direct sunlight year-round, giving them the warmest average temperatures. City C near the pole would be the coldest.",
        "difficulty": "easy",
        "tags": ["climate-zones", "latitude", "temperature"],
        "generated_at": TIMESTAMP
    },

    # PG.4 - Climate zones (ocean currents)
    {
        "id": "q_pg0012",
        "standard_code": "6-8.PG.4",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Norway is located far north in Europe, yet its western coast has milder winters than other places at the same latitude. Scientists explain that a warm ocean current called the North Atlantic Current carries heat from the tropics northward along the coast."},
        "stem": "According to the passage, why does western Norway have milder winters than expected?",
        "choices": [
            {"id": "A", "text": "A warm ocean current brings heat to the coast", "correct": True},
            {"id": "B", "text": "Mountains block cold winds from reaching Norway", "correct": False},
            {"id": "C", "text": "Norway is closer to the equator than it appears", "correct": False},
            {"id": "D", "text": "Thick forests trap heat along the western coast", "correct": False}
        ],
        "answer_explanation": "The passage states that the North Atlantic Current carries warm water from the tropics to Norway's western coast, making winters milder than other places at the same latitude.",
        "difficulty": "medium",
        "tags": ["climate-zones", "ocean-currents", "temperature"],
        "generated_at": TIMESTAMP
    },

    # PG.4 - Climate zones (elevation)
    {
        "id": "q_pg0013",
        "standard_code": "6-8.PG.4",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Two cities in the same country are located at the same latitude. City X is at sea level along the coast. City Y is high in the mountains at 3,000 meters above sea level."},
        "stem": "How would the average temperature of City Y most likely compare to City X?",
        "choices": [
            {"id": "A", "text": "City Y would be warmer due to mountain sunshine", "correct": False},
            {"id": "B", "text": "City Y would be cooler due to higher elevation", "correct": True},
            {"id": "C", "text": "Both cities would have the same temperatures", "correct": False},
            {"id": "D", "text": "City Y would be warmer because of thinner air", "correct": False}
        ],
        "answer_explanation": "Temperature decreases as elevation increases. City Y at 3,000 meters would be significantly cooler than City X at sea level, even though both are at the same latitude.",
        "difficulty": "medium",
        "tags": ["climate-zones", "elevation", "temperature"],
        "generated_at": TIMESTAMP
    },

    # PG.4 - Climate zones (tropical/polar/temperate)
    {
        "id": "q_pg0014",
        "standard_code": "6-8.PG.4",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Earth's surface can be divided into major climate zones based on distance from the equator. The zone nearest the equator is hot and wet. The zones nearest the poles are extremely cold. Between them are zones with moderate temperatures and changing seasons."},
        "stem": "Which TWO statements correctly describe Earth's major climate zones?",
        "choices": [
            {"id": "A", "text": "Tropical zones near the equator are warm and wet", "correct": True},
            {"id": "B", "text": "Polar zones near the poles are extremely cold", "correct": True},
            {"id": "C", "text": "Temperate zones have the hottest temperatures", "correct": False},
            {"id": "D", "text": "Desert zones are always found near the equator", "correct": False}
        ],
        "answer_explanation": "Tropical zones near the equator are warm and wet, and polar zones near the poles are extremely cold. Temperate zones have moderate, not the hottest, temperatures. Deserts can be found at various latitudes.",
        "difficulty": "easy",
        "tags": ["climate-zones", "tropical", "polar", "temperate"],
        "generated_at": TIMESTAMP
    },

    # PG.5 - Biomes (desert)
    {
        "id": "q_pg0015",
        "standard_code": "6-8.PG.5",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Sahara Desert in northern Africa receives less than 25 centimeters of rain per year. Temperatures can reach over 50 degrees Celsius during the day but drop sharply at night. Few plants and animals can survive these harsh conditions."},
        "stem": "Which characteristic of the Sahara makes it difficult for most living things to survive?",
        "choices": [
            {"id": "A", "text": "Very low rainfall and extreme temperature changes", "correct": True},
            {"id": "B", "text": "Heavy flooding that occurs during winter months", "correct": False},
            {"id": "C", "text": "Thick forests that block sunlight from the ground", "correct": False},
            {"id": "D", "text": "Frequent earthquakes that damage the landscape", "correct": False}
        ],
        "answer_explanation": "The Sahara has very little rain and extreme temperature swings between day and night, making survival difficult for most plants and animals.",
        "difficulty": "easy",
        "tags": ["biomes", "desert", "sahara", "climate-vegetation"],
        "generated_at": TIMESTAMP
    },

    # PG.5 - Biomes (tropical rainforest)
    {
        "id": "q_pg0016",
        "standard_code": "6-8.PG.5",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Tropical rainforests are found near the equator where it is warm and rainy throughout the year. These forests have more types of plants and animals than any other biome on Earth. The trees grow so tall and thick that very little sunlight reaches the forest floor."},
        "stem": "Based on the passage, what makes tropical rainforests different from other biomes?",
        "choices": [
            {"id": "A", "text": "They have the greatest variety of living things", "correct": True},
            {"id": "B", "text": "They experience all four seasons during the year", "correct": False},
            {"id": "C", "text": "They are located in the coldest parts of Earth", "correct": False},
            {"id": "D", "text": "They have very few trees due to heavy rainfall", "correct": False}
        ],
        "answer_explanation": "The passage states that tropical rainforests have more types of plants and animals than any other biome, giving them the greatest biodiversity on Earth.",
        "difficulty": "easy",
        "tags": ["biomes", "rainforest", "biodiversity", "climate-vegetation"],
        "generated_at": TIMESTAMP
    },

    # PG.5 - Biomes (tundra)
    {
        "id": "q_pg0017",
        "standard_code": "6-8.PG.5",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The tundra biome is found in the far north near the Arctic. Winters are long and bitterly cold, and the ground stays frozen for most of the year. Only small, low-growing plants like mosses and shrubs can survive because the growing season is very short."},
        "stem": "Why are trees unable to grow in the tundra biome?",
        "choices": [
            {"id": "A", "text": "The soil is too wet from constant rainfall", "correct": False},
            {"id": "B", "text": "The growing season is too short and cold", "correct": True},
            {"id": "C", "text": "Strong ocean waves wash away the topsoil", "correct": False},
            {"id": "D", "text": "There is too much sunlight during the summer", "correct": False}
        ],
        "answer_explanation": "The tundra has a very short growing season and frozen ground most of the year, which prevents trees from establishing roots and growing tall enough to survive.",
        "difficulty": "easy",
        "tags": ["biomes", "tundra", "arctic", "climate-vegetation"],
        "generated_at": TIMESTAMP
    },

    # PG.6 - Weathering and erosion (chemical weathering)
    {
        "id": "q_pg0018",
        "standard_code": "6-8.PG.6",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Over many years, rainwater slowly dissolves limestone rock. This process creates caves, sinkholes, and underground rivers. The rainwater is slightly acidic, which helps break down the minerals in the rock."},
        "stem": "What type of weathering process is described in the passage?",
        "choices": [
            {"id": "A", "text": "Mechanical weathering from freezing water", "correct": False},
            {"id": "B", "text": "Chemical weathering from acidic rainwater", "correct": True},
            {"id": "C", "text": "Erosion caused by strong winds blowing sand", "correct": False},
            {"id": "D", "text": "Physical weathering from plant root growth", "correct": False}
        ],
        "answer_explanation": "The passage describes chemical weathering, where acidic rainwater dissolves limestone rock over time to create caves, sinkholes, and underground rivers.",
        "difficulty": "medium",
        "tags": ["weathering", "chemical-weathering", "erosion", "limestone"],
        "generated_at": TIMESTAMP
    },

    # PG.6 - Weathering and erosion (river erosion)
    {
        "id": "q_pg0019",
        "standard_code": "6-8.PG.6",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Grand Canyon in Arizona was formed over millions of years. The Colorado River slowly cut through layers of rock, carving a canyon that is over 1,600 meters deep in some places."},
        "stem": "Which process was most responsible for forming the Grand Canyon over time?",
        "choices": [
            {"id": "A", "text": "River erosion wearing away layers of rock", "correct": True},
            {"id": "B", "text": "Volcanic eruptions that pushed rock apart", "correct": False},
            {"id": "C", "text": "Glaciers sliding slowly across the desert", "correct": False},
            {"id": "D", "text": "Earthquakes splitting the ground wide open", "correct": False}
        ],
        "answer_explanation": "The Grand Canyon was carved by the Colorado River slowly eroding through layers of rock over millions of years. This is a classic example of river erosion shaping landforms.",
        "difficulty": "easy",
        "tags": ["weathering", "erosion", "river-erosion", "grand-canyon"],
        "generated_at": TIMESTAMP
    },

    # PG.6 - Weathering and erosion (glaciers)
    {
        "id": "q_pg0020",
        "standard_code": "6-8.PG.6",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "During the last Ice Age, massive sheets of ice called glaciers covered much of North America. As these glaciers moved slowly across the land, they scraped away soil and rock. When the glaciers melted, they left behind U-shaped valleys and large lakes."},
        "stem": "How did glaciers change the landscape of North America during the Ice Age?",
        "choices": [
            {"id": "A", "text": "They deposited sand to create new mountain ranges", "correct": False},
            {"id": "B", "text": "They scraped land and carved valleys and lakes", "correct": True},
            {"id": "C", "text": "They blocked rivers and created large waterfalls", "correct": False},
            {"id": "D", "text": "They heated the ground and formed new volcanoes", "correct": False}
        ],
        "answer_explanation": "Glaciers scraped away soil and rock as they moved, carving U-shaped valleys. When they melted, the depressions they left behind filled with water to form large lakes like the Great Lakes.",
        "difficulty": "medium",
        "tags": ["weathering", "erosion", "glaciers", "ice-age"],
        "generated_at": TIMESTAMP
    },

    # PG.7 - Natural disasters (hurricanes)
    {
        "id": "q_pg0021",
        "standard_code": "6-8.PG.7",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Hurricanes form over warm ocean water near the equator. As warm, moist air rises quickly, it creates a spinning storm system. These storms bring heavy rain, strong winds, and can cause flooding when they reach land."},
        "stem": "Based on the passage, what geographic condition is needed for a hurricane to form?",
        "choices": [
            {"id": "A", "text": "Cold air moving quickly across flat plains", "correct": False},
            {"id": "B", "text": "Warm ocean water found near the equator", "correct": True},
            {"id": "C", "text": "Dry conditions found in a desert climate", "correct": False},
            {"id": "D", "text": "Snow melting rapidly in mountain valleys", "correct": False}
        ],
        "answer_explanation": "The passage states that hurricanes form over warm ocean water near the equator. The warm, moist air rising from the ocean surface provides the energy that drives hurricane formation.",
        "difficulty": "easy",
        "tags": ["natural-disasters", "hurricanes", "weather"],
        "generated_at": TIMESTAMP
    },

    # PG.7 - Natural disasters (tsunamis)
    {
        "id": "q_pg0022",
        "standard_code": "6-8.PG.7",
        "standard_essential": False,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In 2011, a powerful earthquake struck the ocean floor near Japan. The earthquake pushed a massive wall of water toward the coast. This giant wave, called a tsunami, flooded cities and caused widespread damage."},
        "stem": "According to the passage, what caused the tsunami that struck Japan in 2011?",
        "choices": [
            {"id": "A", "text": "A powerful earthquake on the ocean floor", "correct": True},
            {"id": "B", "text": "A volcanic eruption on a nearby island", "correct": False},
            {"id": "C", "text": "Strong winds from a tropical hurricane", "correct": False},
            {"id": "D", "text": "Heavy rainfall that overflowed the rivers", "correct": False}
        ],
        "answer_explanation": "The passage explains that a powerful earthquake on the ocean floor near Japan displaced water and created the tsunami that struck the coast.",
        "difficulty": "easy",
        "tags": ["natural-disasters", "tsunamis", "earthquakes"],
        "generated_at": TIMESTAMP
    },

    # PG.8 - Physical geography affects settlement (river valleys)
    {
        "id": "q_pg0023",
        "standard_code": "6-8.PG.8",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Many of the world's earliest civilizations developed along major rivers. The Nile River in Egypt, the Tigris and Euphrates in Mesopotamia, and the Indus River in South Asia all supported large farming communities because the rivers provided water and rich soil."},
        "stem": "Why did early human communities often settle and grow near major rivers?",
        "choices": [
            {"id": "A", "text": "Rivers provided water and fertile soil for farming", "correct": True},
            {"id": "B", "text": "Rivers created natural walls to block enemy armies", "correct": False},
            {"id": "C", "text": "Rivers made the climate cooler and more comfortable", "correct": False},
            {"id": "D", "text": "Rivers kept dangerous animals away from villages", "correct": False}
        ],
        "answer_explanation": "Early civilizations settled near rivers because rivers provided fresh water for drinking and irrigation, and periodic flooding deposited rich soil ideal for farming.",
        "difficulty": "easy",
        "tags": ["settlement-patterns", "rivers", "agriculture", "civilization"],
        "generated_at": TIMESTAMP
    },

    # PG.8 - Physical geography affects settlement (coastal cities/trade)
    {
        "id": "q_pg0024",
        "standard_code": "6-8.PG.8",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Many of the world's largest cities are located along coastlines or near major ports. These locations give people access to fishing, shipping, and trade routes that connect different parts of the world."},
        "stem": "What is the main reason many large cities developed along coastlines?",
        "choices": [
            {"id": "A", "text": "Coastal areas always have the best weather", "correct": False},
            {"id": "B", "text": "Coasts provide access to fishing and trade", "correct": True},
            {"id": "C", "text": "Coastlines are farther from earthquake zones", "correct": False},
            {"id": "D", "text": "Coastal land is the easiest land to farm", "correct": False}
        ],
        "answer_explanation": "Coastal cities developed because coastlines provide access to fishing, shipping, and trade routes. These economic advantages attracted large populations over time.",
        "difficulty": "medium",
        "tags": ["settlement-patterns", "coastal-cities", "trade", "economy"],
        "generated_at": TIMESTAMP
    },

    # PG.8 - Physical geography affects settlement (mountains as barriers)
    {
        "id": "q_pg0025",
        "standard_code": "6-8.PG.8",
        "standard_essential": True,
        "reporting_category": "Physical Geography",
        "domain": "Physical Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Himalaya Mountains in Asia are the tallest mountain range in the world. Throughout history, these mountains have made travel and trade between South Asia and East Asia very difficult. As a result, the cultures on each side developed in different ways."},
        "stem": "How have the Himalaya Mountains affected human settlement and culture in Asia?",
        "choices": [
            {"id": "A", "text": "They served as a barrier that separated cultures", "correct": True},
            {"id": "B", "text": "They created fertile farmland on both sides", "correct": False},
            {"id": "C", "text": "They attracted large populations to the peaks", "correct": False},
            {"id": "D", "text": "They provided easy trade routes across regions", "correct": False}
        ],
        "answer_explanation": "The Himalayas acted as a natural barrier that made travel and trade difficult between South Asia and East Asia, causing cultures on each side to develop independently.",
        "difficulty": "medium",
        "tags": ["settlement-patterns", "mountains", "barriers", "culture"],
        "generated_at": TIMESTAMP
    },

    # ── HUMAN GEOGRAPHY (20 questions) ───────────────────────────────

    # HG.1 - Population distribution (water access)
    {
        "id": "q_hg0001",
        "standard_code": "6-8.HG.1",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A student studies a population map of Africa. The map shows that most people live along rivers, coastlines, and areas with regular rainfall. Large desert areas like the Sahara have very few people."},
        "stem": "Based on the map, what factor has the greatest influence on where people live in Africa?",
        "choices": [
            {"id": "A", "text": "Access to water and fertile land", "correct": True},
            {"id": "B", "text": "Distance from other countries", "correct": False},
            {"id": "C", "text": "The number of roads in each area", "correct": False},
            {"id": "D", "text": "How close an area is to the equator", "correct": False}
        ],
        "answer_explanation": "The map shows population concentrated near water sources and rainfall areas. Access to water for drinking and farming is the main factor influencing settlement in Africa.",
        "difficulty": "easy",
        "tags": ["population-distribution", "water", "settlement-factors"],
        "generated_at": TIMESTAMP
    },

    # HG.1 - Population distribution (climate)
    {
        "id": "q_hg0002",
        "standard_code": "6-8.HG.1",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "More than half of the world's population lives in Asia. Within Asia, people are clustered in river valleys, coastal plains, and areas with mild climates. Mountain regions and dry deserts have far fewer people."},
        "stem": "What pattern does the passage show about where people live in Asia?",
        "choices": [
            {"id": "A", "text": "People spread evenly across the whole continent", "correct": False},
            {"id": "B", "text": "People cluster where land and climate support life", "correct": True},
            {"id": "C", "text": "Most people live in the highest mountain regions", "correct": False},
            {"id": "D", "text": "People prefer dry desert areas over river valleys", "correct": False}
        ],
        "answer_explanation": "The passage shows that people in Asia cluster in areas with favorable conditions like river valleys, coastal plains, and mild climates, rather than spreading evenly.",
        "difficulty": "easy",
        "tags": ["population-distribution", "asia", "settlement-patterns"],
        "generated_at": TIMESTAMP
    },

    # HG.1 - Population distribution (density comparison)
    {
        "id": "q_hg0003",
        "standard_code": "6-8.HG.1",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A table shows population density for four regions:\n\n\u2022 Region A: 5 people per square kilometer (desert)\n\u2022 Region B: 350 people per square kilometer (river delta)\n\u2022 Region C: 2 people per square kilometer (arctic tundra)\n\u2022 Region D: 90 people per square kilometer (grassland)"},
        "stem": "Which region most likely has the highest population density, and why?",
        "choices": [
            {"id": "A", "text": "Region B, because river deltas provide rich farmland", "correct": True},
            {"id": "B", "text": "Region A, because deserts have plenty of open space", "correct": False},
            {"id": "C", "text": "Region C, because cold areas attract many people", "correct": False},
            {"id": "D", "text": "Region D, because grasslands have no other uses", "correct": False}
        ],
        "answer_explanation": "Region B has the highest density at 350 people per square kilometer because river deltas provide fertile soil, fresh water, and flat land ideal for farming and settlement.",
        "difficulty": "medium",
        "tags": ["population-density", "river-delta", "settlement-factors"],
        "generated_at": TIMESTAMP
    },

    # HG.1 - Population distribution (factors)
    {
        "id": "q_hg0004",
        "standard_code": "6-8.HG.1",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Geographers study many factors that explain why some areas have large populations while other areas have very few people."},
        "stem": "Which TWO factors most influence where large numbers of people choose to live?",
        "choices": [
            {"id": "A", "text": "Availability of fresh water and food sources", "correct": True},
            {"id": "B", "text": "A mild climate that supports year-round living", "correct": True},
            {"id": "C", "text": "Being located far from any ocean or coastline", "correct": False},
            {"id": "D", "text": "Having very steep and rocky mountain terrain", "correct": False}
        ],
        "answer_explanation": "Fresh water, food sources, and mild climates are the main factors that attract large populations. Remote inland locations and steep terrain discourage settlement.",
        "difficulty": "easy",
        "tags": ["population-distribution", "settlement-factors"],
        "generated_at": TIMESTAMP
    },

    # HG.2 - Migration (push factors)
    {
        "id": "q_hg0005",
        "standard_code": "6-8.HG.2",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In the 1840s, a disease destroyed most of the potato crop in Ireland. Potatoes were the main food source for millions of Irish people. As a result, over one million people left Ireland and moved to the United States and other countries."},
        "stem": "What type of migration factor caused so many Irish people to leave their country?",
        "choices": [
            {"id": "A", "text": "A push factor caused by a food shortage", "correct": True},
            {"id": "B", "text": "A pull factor from better jobs in Ireland", "correct": False},
            {"id": "C", "text": "A push factor caused by overcrowded cities", "correct": False},
            {"id": "D", "text": "A pull factor from warmer weather elsewhere", "correct": False}
        ],
        "answer_explanation": "The Irish Potato Famine was a push factor, a negative condition that forced people to leave. The food shortage pushed over one million people to migrate to other countries.",
        "difficulty": "easy",
        "tags": ["migration", "push-factors", "famine", "ireland"],
        "generated_at": TIMESTAMP
    },

    # HG.2 - Migration (pull factors)
    {
        "id": "q_hg0006",
        "standard_code": "6-8.HG.2",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "During the California Gold Rush of 1849, thousands of people moved to California from across the United States and around the world. They hoped to find gold and become wealthy."},
        "stem": "What type of migration factor drew people to California during the Gold Rush?",
        "choices": [
            {"id": "A", "text": "A push factor from war in their home regions", "correct": False},
            {"id": "B", "text": "A pull factor from the chance to find wealth", "correct": True},
            {"id": "C", "text": "A push factor from a lack of farmland at home", "correct": False},
            {"id": "D", "text": "A pull factor from California's cold climate", "correct": False}
        ],
        "answer_explanation": "The opportunity to find gold and become wealthy was a pull factor that attracted people to California. Pull factors are positive conditions that draw people to a new place.",
        "difficulty": "easy",
        "tags": ["migration", "pull-factors", "gold-rush", "california"],
        "generated_at": TIMESTAMP
    },

    # HG.2 - Migration (push and pull combined)
    {
        "id": "q_hg0007",
        "standard_code": "6-8.HG.2",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "A family decides to move from a small village to a large city in another country. In their village, there are no jobs and the schools have closed. In the city, there are many factories hiring workers and good schools for children."},
        "stem": "Which TWO statements correctly identify the push and pull factors in this example?",
        "choices": [
            {"id": "A", "text": "No jobs in the village is a push factor", "correct": True},
            {"id": "B", "text": "Factories hiring workers is a pull factor", "correct": True},
            {"id": "C", "text": "Closed schools in the village is a pull factor", "correct": False},
            {"id": "D", "text": "Good schools in the city is a push factor", "correct": False}
        ],
        "answer_explanation": "Push factors are negative conditions in the home area (no jobs), while pull factors are positive conditions in the new area (factories hiring). Closed schools push people away; good schools pull people toward the city.",
        "difficulty": "medium",
        "tags": ["migration", "push-pull-factors", "rural-urban"],
        "generated_at": TIMESTAMP
    },

    # HG.2 - Migration (effects)
    {
        "id": "q_hg0008",
        "standard_code": "6-8.HG.2",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "When large numbers of people migrate to a new country, they bring their language, food, music, and traditions with them. Over time, these customs blend with the culture of their new home."},
        "stem": "What is one important effect of large-scale migration on the receiving country?",
        "choices": [
            {"id": "A", "text": "The country's culture becomes more diverse", "correct": True},
            {"id": "B", "text": "The country's population always decreases", "correct": False},
            {"id": "C", "text": "The country loses all of its original customs", "correct": False},
            {"id": "D", "text": "The country's borders change their location", "correct": False}
        ],
        "answer_explanation": "When migrants bring their customs, food, and language to a new country, the receiving country becomes more culturally diverse as traditions blend together over time.",
        "difficulty": "medium",
        "tags": ["migration", "cultural-effects", "diversity"],
        "generated_at": TIMESTAMP
    },

    # HG.3 - Cultural traits (language)
    {
        "id": "q_hg0009",
        "standard_code": "6-8.HG.3",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Spanish is spoken in Spain and in most countries of Central and South America. This is because Spain established colonies in the Americas during the 1500s and 1600s. Spanish settlers brought their language to these regions."},
        "stem": "What process explains why Spanish is spoken across so many countries today?",
        "choices": [
            {"id": "A", "text": "Cultural diffusion through colonization", "correct": True},
            {"id": "B", "text": "Natural language change over many centuries", "correct": False},
            {"id": "C", "text": "Geographic isolation on different continents", "correct": False},
            {"id": "D", "text": "Similar climates producing similar languages", "correct": False}
        ],
        "answer_explanation": "Spanish spread to the Americas through cultural diffusion during colonization. When Spain established colonies, settlers brought their language, which became the dominant language in many regions.",
        "difficulty": "medium",
        "tags": ["cultural-traits", "language", "cultural-diffusion", "colonization"],
        "generated_at": TIMESTAMP
    },

    # HG.3 - Cultural traits (religion)
    {
        "id": "q_hg0010",
        "standard_code": "6-8.HG.3",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A map of world religions shows that Christianity is common in Europe and the Americas. Islam is the main religion in the Middle East and North Africa. Hinduism is mostly found in South Asia, especially India."},
        "stem": "What does the map reveal about how religions are distributed around the world?",
        "choices": [
            {"id": "A", "text": "Every country practices the same religion", "correct": False},
            {"id": "B", "text": "Religions are concentrated in specific regions", "correct": True},
            {"id": "C", "text": "Religion has no connection to geography at all", "correct": False},
            {"id": "D", "text": "Only one religion exists on each continent", "correct": False}
        ],
        "answer_explanation": "The map shows that major religions are concentrated in specific world regions rather than being evenly spread. This reflects historical patterns of cultural development and diffusion.",
        "difficulty": "easy",
        "tags": ["cultural-traits", "religion", "world-regions"],
        "generated_at": TIMESTAMP
    },

    # HG.3 - Cultural traits (diffusion through trade)
    {
        "id": "q_hg0011",
        "standard_code": "6-8.HG.3",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Silk Road was a network of trade routes that connected China to Europe for hundreds of years. Merchants traveling these routes traded goods like silk, spices, and glass. They also shared ideas, religions, and inventions along the way."},
        "stem": "How did the Silk Road contribute to cultural diffusion between regions?",
        "choices": [
            {"id": "A", "text": "It kept all cultures completely separated", "correct": False},
            {"id": "B", "text": "Traders spread ideas and customs along the routes", "correct": True},
            {"id": "C", "text": "It only moved physical goods and no ideas", "correct": False},
            {"id": "D", "text": "It replaced local cultures with a single culture", "correct": False}
        ],
        "answer_explanation": "The Silk Road promoted cultural diffusion as traders exchanged not just goods but also ideas, religions, and inventions between China, Central Asia, and Europe.",
        "difficulty": "medium",
        "tags": ["cultural-diffusion", "silk-road", "trade", "ideas"],
        "generated_at": TIMESTAMP
    },

    # HG.3 - Cultural traits (customs vary by region)
    {
        "id": "q_hg0012",
        "standard_code": "6-8.HG.3",
        "standard_essential": True,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "People around the world celebrate different holidays, eat different foods, and follow different traditions. These cultural traits often reflect the history, geography, and beliefs of each region."},
        "stem": "Which TWO examples best show how cultural traits vary across regions?",
        "choices": [
            {"id": "A", "text": "People in Japan eat rice daily while Mexicans eat corn tortillas", "correct": True},
            {"id": "B", "text": "Diwali is celebrated in India while Thanksgiving is celebrated in the U.S.", "correct": True},
            {"id": "C", "text": "All countries around the world speak the same language", "correct": False},
            {"id": "D", "text": "Every culture celebrates the exact same holidays", "correct": False}
        ],
        "answer_explanation": "Different food traditions (rice vs. corn tortillas) and different holidays (Diwali vs. Thanksgiving) are clear examples of how cultural traits vary by region based on history and geography.",
        "difficulty": "easy",
        "tags": ["cultural-traits", "customs", "regional-variation"],
        "generated_at": TIMESTAMP
    },

    # HG.4 - Urbanization (definition)
    {
        "id": "q_hg0013",
        "standard_code": "6-8.HG.4",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In 1950, about 30 percent of the world's people lived in cities. Today, more than 55 percent live in urban areas. By 2050, experts predict nearly 70 percent of all people will live in cities."},
        "stem": "What trend does the passage describe about world population over time?",
        "choices": [
            {"id": "A", "text": "More people are moving from cities to farms", "correct": False},
            {"id": "B", "text": "The share of people living in cities is growing", "correct": True},
            {"id": "C", "text": "Rural areas are growing faster than urban areas", "correct": False},
            {"id": "D", "text": "The world population is staying the same size", "correct": False}
        ],
        "answer_explanation": "The passage shows urbanization, the trend of an increasing share of people living in cities, growing from 30 percent in 1950 to a projected 70 percent by 2050.",
        "difficulty": "easy",
        "tags": ["urbanization", "population-trends", "cities"],
        "generated_at": TIMESTAMP
    },

    # HG.4 - Urbanization (urban vs rural)
    {
        "id": "q_hg0014",
        "standard_code": "6-8.HG.4",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Urban areas have many buildings, roads, and businesses close together. They offer jobs in offices, factories, and stores. Rural areas have open land used mostly for farming and ranching. People in rural areas live farther apart from one another."},
        "stem": "What is the main difference between urban and rural areas described in the passage?",
        "choices": [
            {"id": "A", "text": "Urban areas are more crowded with varied jobs", "correct": True},
            {"id": "B", "text": "Rural areas have more factories than urban areas", "correct": False},
            {"id": "C", "text": "Urban areas are used mainly for farming crops", "correct": False},
            {"id": "D", "text": "Rural areas have larger populations than cities", "correct": False}
        ],
        "answer_explanation": "The passage describes urban areas as dense with buildings, roads, and diverse jobs, while rural areas have open land used for farming with people living farther apart.",
        "difficulty": "easy",
        "tags": ["urbanization", "urban-rural", "land-use"],
        "generated_at": TIMESTAMP
    },

    # HG.4 - Urbanization (why people move to cities)
    {
        "id": "q_hg0015",
        "standard_code": "6-8.HG.4",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In many developing countries, young people leave their farming villages and move to large cities. They hope to find better-paying jobs, attend schools, and access hospitals and other services that are not available in rural areas."},
        "stem": "Why do many young people in developing countries move from villages to cities?",
        "choices": [
            {"id": "A", "text": "Cities offer better jobs, schools, and services", "correct": True},
            {"id": "B", "text": "Villages have too many job openings to fill", "correct": False},
            {"id": "C", "text": "Cities have more farmland than rural villages", "correct": False},
            {"id": "D", "text": "Villages are too crowded for young people", "correct": False}
        ],
        "answer_explanation": "Young people move to cities for better economic and social opportunities, including higher-paying jobs, schools, and healthcare services not available in rural areas.",
        "difficulty": "easy",
        "tags": ["urbanization", "rural-to-urban", "developing-countries"],
        "generated_at": TIMESTAMP
    },

    # HG.5 - Human-environment interaction (adapt)
    {
        "id": "q_hg0016",
        "standard_code": "6-8.HG.5",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Inuit people of the Arctic have lived in one of the coldest places on Earth for thousands of years. They traditionally built igloos from snow blocks to stay warm. They wore thick fur clothing and hunted seals and fish for food."},
        "stem": "How did the Inuit people adapt to their harsh physical environment?",
        "choices": [
            {"id": "A", "text": "They used local materials for shelter and clothing", "correct": True},
            {"id": "B", "text": "They changed the climate to make it warmer", "correct": False},
            {"id": "C", "text": "They moved to a tropical region to avoid cold", "correct": False},
            {"id": "D", "text": "They built large stone buildings for protection", "correct": False}
        ],
        "answer_explanation": "The Inuit adapted to Arctic conditions by using available resources: snow for igloos, animal furs for warm clothing, and local wildlife for food. This is an example of humans adapting to their environment.",
        "difficulty": "easy",
        "tags": ["human-environment", "adaptation", "inuit", "arctic"],
        "generated_at": TIMESTAMP
    },

    # HG.5 - Human-environment interaction (modify)
    {
        "id": "q_hg0017",
        "standard_code": "6-8.HG.5",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Netherlands is a country in Europe where much of the land is below sea level. Over hundreds of years, the Dutch people built walls called dikes to hold back the sea. They also pumped water out of low areas to create dry land for farming and building."},
        "stem": "How did the people of the Netherlands modify their physical environment?",
        "choices": [
            {"id": "A", "text": "They moved their entire country to higher ground", "correct": False},
            {"id": "B", "text": "They built dikes and pumped water to create dry land", "correct": True},
            {"id": "C", "text": "They filled the ocean with rocks to raise sea level", "correct": False},
            {"id": "D", "text": "They planted trees to stop the rain from falling", "correct": False}
        ],
        "answer_explanation": "The Dutch modified their environment by building dikes to hold back the sea and pumping water to create dry land. This is a classic example of humans changing the physical environment to meet their needs.",
        "difficulty": "medium",
        "tags": ["human-environment", "modification", "netherlands", "dikes"],
        "generated_at": TIMESTAMP
    },

    # HG.5 - Human-environment interaction (depend)
    {
        "id": "q_hg0018",
        "standard_code": "6-8.HG.5",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "People depend on the physical environment for many of their basic needs. Farmers need soil and rain to grow food. Cities need rivers and lakes for drinking water. Factories need natural resources like oil, coal, and metals."},
        "stem": "Which TWO examples show how humans depend on the physical environment?",
        "choices": [
            {"id": "A", "text": "Farmers need soil and rain to grow their crops", "correct": True},
            {"id": "B", "text": "Factories use oil and metals from the earth", "correct": True},
            {"id": "C", "text": "People build roads to connect two cities together", "correct": False},
            {"id": "D", "text": "Students attend school to learn new subjects", "correct": False}
        ],
        "answer_explanation": "Farming depends on soil and rain from the environment, and factories depend on natural resources like oil and metals. Building roads and attending school are human activities, not examples of depending on the physical environment.",
        "difficulty": "easy",
        "tags": ["human-environment", "dependence", "natural-resources"],
        "generated_at": TIMESTAMP
    },

    # HG.6 - Demographic data (birth/death rate)
    {
        "id": "q_hg0019",
        "standard_code": "6-8.HG.6",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A table shows data for two countries:\n\n\u2022 Country X: Birth rate = 40 per 1,000 people, Death rate = 10 per 1,000\n\u2022 Country Y: Birth rate = 10 per 1,000 people, Death rate = 9 per 1,000"},
        "stem": "Based on the data, which country's population is growing faster, and why?",
        "choices": [
            {"id": "A", "text": "Country X, because more people are being born than dying", "correct": True},
            {"id": "B", "text": "Country Y, because it has a lower death rate overall", "correct": False},
            {"id": "C", "text": "Country X, because it has the fewest total people", "correct": False},
            {"id": "D", "text": "Country Y, because its birth rate is very low", "correct": False}
        ],
        "answer_explanation": "Country X has a much larger gap between births (40) and deaths (10), meaning 30 more people per 1,000 are added each year. Country Y only adds 1 person per 1,000, so it grows much slower.",
        "difficulty": "medium",
        "tags": ["demographics", "birth-rate", "death-rate", "population-growth"],
        "generated_at": TIMESTAMP
    },

    # HG.6 - Demographic data (population density)
    {
        "id": "q_hg0020",
        "standard_code": "6-8.HG.6",
        "standard_essential": False,
        "reporting_category": "Human Geography",
        "domain": "Human Geography",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Population density measures how many people live in a given area. It is calculated by dividing the total population by the total land area. A city with 500,000 people in 100 square kilometers has a density of 5,000 people per square kilometer."},
        "stem": "What does a high population density tell us about a place?",
        "choices": [
            {"id": "A", "text": "Many people are living in a small area of land", "correct": True},
            {"id": "B", "text": "Very few people live anywhere in that country", "correct": False},
            {"id": "C", "text": "The area has more land than it needs for people", "correct": False},
            {"id": "D", "text": "People are spread out evenly across all regions", "correct": False}
        ],
        "answer_explanation": "High population density means many people are concentrated in a small area. The example shows 5,000 people per square kilometer, indicating a crowded urban area.",
        "difficulty": "easy",
        "tags": ["demographics", "population-density", "urban"],
        "generated_at": TIMESTAMP
    },

    # ── MAP SKILLS (20 questions) ────────────────────────────────────

    # MS.1 - Latitude and longitude (reading coordinates)
    {
        "id": "q_ms0001",
        "standard_code": "6-8.MS.1",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A geography teacher tells the class that a city is located at 30 degrees North latitude and 90 degrees West longitude. She explains that latitude lines run east and west, and longitude lines run north and south."},
        "stem": "Based on these coordinates, in which part of the world is this city most likely located?",
        "choices": [
            {"id": "A", "text": "The southeastern United States", "correct": True},
            {"id": "B", "text": "The northern coast of Australia", "correct": False},
            {"id": "C", "text": "The eastern edge of Asia", "correct": False},
            {"id": "D", "text": "The southern tip of South America", "correct": False}
        ],
        "answer_explanation": "30 degrees North and 90 degrees West places the city in the southeastern United States, near the Gulf Coast. This is close to the location of New Orleans, Louisiana.",
        "difficulty": "medium",
        "tags": ["latitude", "longitude", "coordinates", "absolute-location"],
        "generated_at": TIMESTAMP
    },

    # MS.1 - Latitude and longitude (equator/prime meridian)
    {
        "id": "q_ms0002",
        "standard_code": "6-8.MS.1",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The equator is an imaginary line at 0 degrees latitude that divides Earth into the Northern and Southern Hemispheres. The prime meridian is a line at 0 degrees longitude that divides Earth into the Eastern and Western Hemispheres."},
        "stem": "What do the equator and the prime meridian have in common?",
        "choices": [
            {"id": "A", "text": "They both divide Earth into two equal halves", "correct": True},
            {"id": "B", "text": "They both run from the North Pole to the South Pole", "correct": False},
            {"id": "C", "text": "They both measure distance east and west only", "correct": False},
            {"id": "D", "text": "They both pass through the United States", "correct": False}
        ],
        "answer_explanation": "Both the equator and the prime meridian divide Earth into two hemispheres. The equator separates north from south, while the prime meridian separates east from west.",
        "difficulty": "easy",
        "tags": ["latitude", "longitude", "equator", "prime-meridian"],
        "generated_at": TIMESTAMP
    },

    # MS.2 - Map types (political vs physical)
    {
        "id": "q_ms0003",
        "standard_code": "6-8.MS.2",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A student needs to find the borders between countries in Africa. Another student wants to see where the tallest mountains are located on the continent."},
        "stem": "Which types of maps should each student use to find the information they need?",
        "choices": [
            {"id": "A", "text": "A political map for borders, a physical map for mountains", "correct": True},
            {"id": "B", "text": "A physical map for borders, a political map for mountains", "correct": False},
            {"id": "C", "text": "A road map for borders, a weather map for mountains", "correct": False},
            {"id": "D", "text": "A thematic map for both borders and mountains", "correct": False}
        ],
        "answer_explanation": "Political maps show human-made boundaries like country borders. Physical maps show natural features like mountains, rivers, and elevation. Each map type has a different purpose.",
        "difficulty": "easy",
        "tags": ["map-types", "political-map", "physical-map"],
        "generated_at": TIMESTAMP
    },

    # MS.2 - Map types (thematic map)
    {
        "id": "q_ms0004",
        "standard_code": "6-8.MS.2",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A map of the United States uses different colors to show how much rainfall each state receives per year. States with heavy rainfall are dark blue, and states with little rainfall are light yellow."},
        "stem": "What type of map is described in the passage?",
        "choices": [
            {"id": "A", "text": "A political map showing state governments", "correct": False},
            {"id": "B", "text": "A thematic map showing rainfall patterns", "correct": True},
            {"id": "C", "text": "A physical map showing mountains and rivers", "correct": False},
            {"id": "D", "text": "A road map showing highways between cities", "correct": False}
        ],
        "answer_explanation": "A thematic map focuses on a specific topic or theme, such as rainfall, population, or temperature. This map uses color to show rainfall amounts across states.",
        "difficulty": "easy",
        "tags": ["map-types", "thematic-map", "rainfall"],
        "generated_at": TIMESTAMP
    },

    # MS.3 - Map elements (scale)
    {
        "id": "q_ms0005",
        "standard_code": "6-8.MS.3",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A map of Texas has a scale bar that shows 1 centimeter equals 100 kilometers. A student measures the distance between two cities on the map and finds they are 3 centimeters apart."},
        "stem": "Based on the map scale, how far apart are the two cities in real life?",
        "choices": [
            {"id": "A", "text": "100 kilometers apart", "correct": False},
            {"id": "B", "text": "200 kilometers apart", "correct": False},
            {"id": "C", "text": "300 kilometers apart", "correct": True},
            {"id": "D", "text": "400 kilometers apart", "correct": False}
        ],
        "answer_explanation": "If 1 centimeter on the map equals 100 kilometers, then 3 centimeters equals 3 times 100, which is 300 kilometers in real life.",
        "difficulty": "easy",
        "tags": ["map-elements", "scale", "distance"],
        "generated_at": TIMESTAMP
    },

    # MS.3 - Map elements (legend/compass rose)
    {
        "id": "q_ms0006",
        "standard_code": "6-8.MS.3",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "A student is looking at a map that shows parks, schools, and hospitals in a neighborhood. Small symbols are used for each type of building. An arrow on the map points to the top of the page."},
        "stem": "Which TWO map elements would help the student understand the symbols and directions on this map?",
        "choices": [
            {"id": "A", "text": "A legend that explains what each symbol means", "correct": True},
            {"id": "B", "text": "A compass rose that shows north, south, east, and west", "correct": True},
            {"id": "C", "text": "A title that names the type of government", "correct": False},
            {"id": "D", "text": "A graph that shows the population over time", "correct": False}
        ],
        "answer_explanation": "A legend (or key) explains what each symbol on the map represents. A compass rose shows cardinal directions so the reader can tell which way is north, south, east, and west.",
        "difficulty": "easy",
        "tags": ["map-elements", "legend", "compass-rose"],
        "generated_at": TIMESTAMP
    },

    # MS.4 - Map projections (distortions)
    {
        "id": "q_ms0007",
        "standard_code": "6-8.MS.4",
        "standard_essential": False,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "When mapmakers create a flat map of Earth, they must stretch or shrink parts of the round surface to make it fit. This means every flat map has some distortion. On many common maps, land near the poles looks much bigger than it really is."},
        "stem": "Why do all flat maps of Earth contain some form of distortion?",
        "choices": [
            {"id": "A", "text": "Earth's round surface cannot be shown perfectly flat", "correct": True},
            {"id": "B", "text": "Mapmakers always make mistakes when drawing lines", "correct": False},
            {"id": "C", "text": "Flat maps are too small to show the whole planet", "correct": False},
            {"id": "D", "text": "The continents are always moving to new places", "correct": False}
        ],
        "answer_explanation": "A sphere cannot be perfectly represented on a flat surface without stretching or compressing some areas. This is why all map projections have some distortion of size, shape, or distance.",
        "difficulty": "medium",
        "tags": ["map-projections", "distortion", "flat-maps"],
        "generated_at": TIMESTAMP
    },

    # MS.5 - Geographic tools (GPS)
    {
        "id": "q_ms0008",
        "standard_code": "6-8.MS.5",
        "standard_essential": False,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A hiker uses a device that receives signals from satellites orbiting Earth. The device shows her exact location on a digital map and gives her directions to the nearest trail. This technology is called the Global Positioning System."},
        "stem": "How does GPS technology help the hiker in this passage?",
        "choices": [
            {"id": "A", "text": "It uses satellites to find her exact location", "correct": True},
            {"id": "B", "text": "It measures the temperature of the air around her", "correct": False},
            {"id": "C", "text": "It predicts the weather for the next week", "correct": False},
            {"id": "D", "text": "It takes pictures of the trail from space", "correct": False}
        ],
        "answer_explanation": "GPS uses signals from satellites to determine a person's exact location on Earth. The hiker's device receives these signals and displays her position on a digital map.",
        "difficulty": "easy",
        "tags": ["geographic-tools", "gps", "technology"],
        "generated_at": TIMESTAMP
    },

    # MS.6 - Hemispheres, continents, oceans (continents)
    {
        "id": "q_ms0009",
        "standard_code": "6-8.MS.6",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Earth has seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America. Asia is the largest continent by both land area and population."},
        "stem": "According to the passage, what makes Asia different from the other six continents?",
        "choices": [
            {"id": "A", "text": "It is the largest in both area and population", "correct": True},
            {"id": "B", "text": "It is the only continent surrounded by water", "correct": False},
            {"id": "C", "text": "It has the fewest countries of any continent", "correct": False},
            {"id": "D", "text": "It is located entirely in the Southern Hemisphere", "correct": False}
        ],
        "answer_explanation": "The passage states that Asia is the largest continent by both land area and population, making it stand out from the other six continents.",
        "difficulty": "easy",
        "tags": ["continents", "asia", "world-geography"],
        "generated_at": TIMESTAMP
    },

    # MS.6 - Hemispheres, continents, oceans (hemispheres)
    {
        "id": "q_ms0010",
        "standard_code": "6-8.MS.6",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Earth is divided into four hemispheres. The equator divides Earth into the Northern and Southern Hemispheres. The prime meridian divides Earth into the Eastern and Western Hemispheres."},
        "stem": "Which TWO statements about Earth's hemispheres are correct based on the passage?",
        "choices": [
            {"id": "A", "text": "The equator separates the Northern and Southern Hemispheres", "correct": True},
            {"id": "B", "text": "The prime meridian separates the Eastern and Western Hemispheres", "correct": True},
            {"id": "C", "text": "The equator divides Earth into Eastern and Western halves", "correct": False},
            {"id": "D", "text": "The prime meridian runs east to west around Earth", "correct": False}
        ],
        "answer_explanation": "The equator runs east-west and separates the Northern and Southern Hemispheres. The prime meridian runs north-south and separates the Eastern and Western Hemispheres.",
        "difficulty": "easy",
        "tags": ["hemispheres", "equator", "prime-meridian"],
        "generated_at": TIMESTAMP
    },

    # MS.1 - Latitude and longitude (using coordinates to find location)
    {
        "id": "q_ms0011",
        "standard_code": "6-8.MS.1",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A treasure hunt game gives students a set of coordinates: 0 degrees latitude, 30 degrees East longitude. Students must use a world map to find the location. The coordinates point to a spot in the middle of Africa."},
        "stem": "What does 0 degrees latitude tell the students about this location on the map?",
        "choices": [
            {"id": "A", "text": "The location is on the equator", "correct": True},
            {"id": "B", "text": "The location is at the North Pole", "correct": False},
            {"id": "C", "text": "The location is on the prime meridian", "correct": False},
            {"id": "D", "text": "The location is in the Western Hemisphere", "correct": False}
        ],
        "answer_explanation": "Zero degrees latitude is the equator, the imaginary line that circles Earth halfway between the North and South Poles. Zero degrees longitude would be the prime meridian.",
        "difficulty": "easy",
        "tags": ["latitude", "longitude", "equator", "coordinates"],
        "generated_at": TIMESTAMP
    },

    # MS.1 - Latitude and longitude (latitude affects climate)
    {
        "id": "q_ms0012",
        "standard_code": "6-8.MS.1",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "City A is located at 10 degrees North latitude. City B is located at 60 degrees North latitude. Both cities are on the same continent."},
        "stem": "Based on their latitude, how would the climates of these two cities most likely compare?",
        "choices": [
            {"id": "A", "text": "City A would be warmer because it is closer to the equator", "correct": True},
            {"id": "B", "text": "City B would be warmer because it is farther from the equator", "correct": False},
            {"id": "C", "text": "Both cities would have the same climate and temperatures", "correct": False},
            {"id": "D", "text": "City A would be colder because of its lower latitude number", "correct": False}
        ],
        "answer_explanation": "Places closer to the equator (lower latitude numbers) receive more direct sunlight and are generally warmer. City A at 10 degrees North is much closer to the equator than City B at 60 degrees North.",
        "difficulty": "medium",
        "tags": ["latitude", "climate", "temperature", "equator"],
        "generated_at": TIMESTAMP
    },

    # MS.2 - Map types (topographic map)
    {
        "id": "q_ms0013",
        "standard_code": "6-8.MS.2",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A topographic map uses curved lines called contour lines to show the shape and elevation of the land. Lines that are close together mean the land is steep. Lines that are far apart mean the land is flat or gently sloping."},
        "stem": "What can a person learn from studying the contour lines on a topographic map?",
        "choices": [
            {"id": "A", "text": "How steep or flat the land is in an area", "correct": True},
            {"id": "B", "text": "What language the people in the area speak", "correct": False},
            {"id": "C", "text": "How much rain falls in the area each year", "correct": False},
            {"id": "D", "text": "Which countries share a border in the area", "correct": False}
        ],
        "answer_explanation": "Contour lines on a topographic map show elevation and slope. Closely spaced lines indicate steep terrain, while widely spaced lines indicate flat or gentle terrain.",
        "difficulty": "medium",
        "tags": ["map-types", "topographic-map", "contour-lines", "elevation"],
        "generated_at": TIMESTAMP
    },

    # MS.2 - Map types (choosing the right map)
    {
        "id": "q_ms0014",
        "standard_code": "6-8.MS.2",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Different types of maps are designed for different purposes. A physical map shows natural features. A political map shows borders and capitals. A thematic map focuses on a specific topic like climate or population."},
        "stem": "Which TWO tasks would require a student to use a political map?",
        "choices": [
            {"id": "A", "text": "Finding the capital city of a country", "correct": True},
            {"id": "B", "text": "Locating the border between two nations", "correct": True},
            {"id": "C", "text": "Measuring the height of a mountain range", "correct": False},
            {"id": "D", "text": "Comparing annual rainfall across a region", "correct": False}
        ],
        "answer_explanation": "Political maps show human-made features like country borders and capital cities. Mountain heights require a physical map, and rainfall data requires a thematic map.",
        "difficulty": "easy",
        "tags": ["map-types", "political-map", "map-purpose"],
        "generated_at": TIMESTAMP
    },

    # MS.3 - Map elements (title and purpose)
    {
        "id": "q_ms0015",
        "standard_code": "6-8.MS.3",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A student opens a map that has the title \"Population Density of South America.\" The map uses different shades of color, with darker shades showing areas where more people live. A legend on the side explains what each shade means."},
        "stem": "How do the title and legend work together to help the student read this map?",
        "choices": [
            {"id": "A", "text": "The title names the topic, and the legend explains the colors", "correct": True},
            {"id": "B", "text": "The title shows direction, and the legend shows distance", "correct": False},
            {"id": "C", "text": "The title lists all countries, and the legend shows borders", "correct": False},
            {"id": "D", "text": "The title gives the map scale, and the legend shows rivers", "correct": False}
        ],
        "answer_explanation": "The map title tells the reader what the map is about (population density of South America). The legend explains what the different shades of color represent, helping the reader understand the data.",
        "difficulty": "easy",
        "tags": ["map-elements", "title", "legend", "reading-maps"],
        "generated_at": TIMESTAMP
    },

    # MS.3 - Map elements (using scale to compare)
    {
        "id": "q_ms0016",
        "standard_code": "6-8.MS.3",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Two maps show the same city. Map A has a scale of 1 centimeter equals 1 kilometer. Map B has a scale of 1 centimeter equals 10 kilometers. Both maps are printed on paper the same size."},
        "stem": "What is the main difference between what these two maps show?",
        "choices": [
            {"id": "A", "text": "Map A shows a smaller area with more detail", "correct": True},
            {"id": "B", "text": "Map B shows a smaller area with more detail", "correct": False},
            {"id": "C", "text": "Both maps show the same amount of detail", "correct": False},
            {"id": "D", "text": "Map A covers a larger area than Map B does", "correct": False}
        ],
        "answer_explanation": "Map A has a larger scale (1 cm = 1 km), so it shows a smaller area but with more detail. Map B has a smaller scale (1 cm = 10 km), so it covers a larger area but with less detail.",
        "difficulty": "medium",
        "tags": ["map-elements", "scale", "map-detail", "comparison"],
        "generated_at": TIMESTAMP
    },

    # MS.4 - Map projections (Mercator)
    {
        "id": "q_ms0017",
        "standard_code": "6-8.MS.4",
        "standard_essential": False,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Mercator projection is a common flat map used in many classrooms. On this map, Greenland appears to be almost the same size as Africa. In reality, Africa is about 14 times larger than Greenland."},
        "stem": "What does the Greenland and Africa example show about the Mercator projection?",
        "choices": [
            {"id": "A", "text": "It greatly exaggerates the size of land near the poles", "correct": True},
            {"id": "B", "text": "It makes all continents appear exactly the same size", "correct": False},
            {"id": "C", "text": "It shows the correct size of every country on Earth", "correct": False},
            {"id": "D", "text": "It shrinks land near the equator to save space", "correct": False}
        ],
        "answer_explanation": "The Mercator projection stretches areas near the poles, making them appear much larger than they really are. This is why Greenland looks as big as Africa even though Africa is 14 times larger.",
        "difficulty": "medium",
        "tags": ["map-projections", "mercator", "distortion", "size"],
        "generated_at": TIMESTAMP
    },

    # MS.4 - Map projections (why different projections exist)
    {
        "id": "q_ms0018",
        "standard_code": "6-8.MS.4",
        "standard_essential": False,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Mapmakers have created many different map projections over the centuries. Some projections show the correct size of continents but distort their shape. Others keep the shape accurate but change the size. No single projection can show everything perfectly."},
        "stem": "Why have mapmakers created many different types of map projections?",
        "choices": [
            {"id": "A", "text": "No single projection can avoid all types of distortion", "correct": True},
            {"id": "B", "text": "Mapmakers enjoy creating as many maps as possible", "correct": False},
            {"id": "C", "text": "Each country requires its own special map projection", "correct": False},
            {"id": "D", "text": "Older projections were lost and had to be remade", "correct": False}
        ],
        "answer_explanation": "Because a round Earth cannot be shown on a flat surface without distortion, different projections make different trade-offs between size, shape, distance, and direction.",
        "difficulty": "medium",
        "tags": ["map-projections", "distortion", "trade-offs"],
        "generated_at": TIMESTAMP
    },

    # MS.5 - Geographic tools (GIS)
    {
        "id": "q_ms0019",
        "standard_code": "6-8.MS.5",
        "standard_essential": False,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "A city planner uses a computer system to layer different maps on top of each other. One layer shows roads, another shows buildings, and a third shows flood zones. This system is called a Geographic Information System, or GIS."},
        "stem": "How does a GIS help the city planner make better decisions?",
        "choices": [
            {"id": "A", "text": "It combines many types of geographic data in layers", "correct": True},
            {"id": "B", "text": "It replaces the need for any maps or other data", "correct": False},
            {"id": "C", "text": "It automatically fixes all the problems in a city", "correct": False},
            {"id": "D", "text": "It only shows one type of information at a time", "correct": False}
        ],
        "answer_explanation": "GIS layers multiple types of geographic data so users can see how different features relate to each other. The city planner can view roads, buildings, and flood zones together to make informed decisions.",
        "difficulty": "medium",
        "tags": ["geographic-tools", "gis", "technology", "data-layers"],
        "generated_at": TIMESTAMP
    },

    # MS.6 - Hemispheres, continents, oceans (oceans)
    {
        "id": "q_ms0020",
        "standard_code": "6-8.MS.6",
        "standard_essential": True,
        "reporting_category": "Map Skills and Tools",
        "domain": "Map Skills",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Earth has five major oceans: the Pacific, Atlantic, Indian, Southern, and Arctic. The Pacific Ocean is the largest and deepest. The Arctic Ocean is the smallest and is mostly covered by ice."},
        "stem": "Based on the passage, how do the Pacific and Arctic Oceans compare to each other?",
        "choices": [
            {"id": "A", "text": "The Pacific is the largest while the Arctic is the smallest", "correct": True},
            {"id": "B", "text": "The Arctic is larger and deeper than the Pacific Ocean", "correct": False},
            {"id": "C", "text": "Both oceans are the same size but differ in temperature", "correct": False},
            {"id": "D", "text": "The Pacific is covered by ice while the Arctic is not", "correct": False}
        ],
        "answer_explanation": "The passage states that the Pacific is the largest and deepest ocean, while the Arctic is the smallest and mostly covered by ice, making them opposite extremes among Earth's five oceans.",
        "difficulty": "easy",
        "tags": ["oceans", "pacific", "arctic", "world-geography"],
        "generated_at": TIMESTAMP
    },

    # ── WORLD REGIONS (20 questions) ─────────────────────────────────

    # WR.1 - Physical and human characteristics (Africa)
    {
        "id": "q_wr0001",
        "standard_code": "6-8.WR.1",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Africa is the second-largest continent. Its physical features include the Sahara Desert in the north, tropical rainforests near the equator, and the Great Rift Valley in the east. Africa is also home to more than 50 countries and hundreds of languages."},
        "stem": "Based on the passage, what makes Africa a diverse continent in terms of geography?",
        "choices": [
            {"id": "A", "text": "It has deserts, rainforests, and rift valleys", "correct": True},
            {"id": "B", "text": "It is completely covered by tropical rainforest", "correct": False},
            {"id": "C", "text": "It has only one type of climate across the land", "correct": False},
            {"id": "D", "text": "It is the smallest continent with few countries", "correct": False}
        ],
        "answer_explanation": "Africa has a wide variety of physical features, including the Sahara Desert, tropical rainforests, and the Great Rift Valley, making it geographically diverse.",
        "difficulty": "easy",
        "tags": ["world-regions", "africa", "physical-features", "diversity"],
        "generated_at": TIMESTAMP
    },

    # WR.1 - Physical and human characteristics (Asia)
    {
        "id": "q_wr0002",
        "standard_code": "6-8.WR.1",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Asia contains the highest mountain range in the world, the Himalayas. It also has large deserts like the Gobi and fertile river valleys like those along the Ganges and Yangtze rivers. More than four billion people live in Asia."},
        "stem": "What do the physical features of Asia tell us about the continent?",
        "choices": [
            {"id": "A", "text": "It has a wide range of landforms and environments", "correct": True},
            {"id": "B", "text": "It is made up entirely of flat river plains", "correct": False},
            {"id": "C", "text": "It has fewer people than any other continent", "correct": False},
            {"id": "D", "text": "It has no mountains or deserts of any kind", "correct": False}
        ],
        "answer_explanation": "Asia has mountains (Himalayas), deserts (Gobi), and fertile river valleys (Ganges, Yangtze), showing it has a wide range of landforms and environments.",
        "difficulty": "easy",
        "tags": ["world-regions", "asia", "physical-features", "landforms"],
        "generated_at": TIMESTAMP
    },

    # WR.1 - Physical and human characteristics (Europe)
    {
        "id": "q_wr0003",
        "standard_code": "6-8.WR.1",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Europe is a small continent with many different countries, languages, and cultures packed closely together. Its physical features include the Alps mountain range, the Rhine and Danube rivers, and long coastlines along the Atlantic Ocean and Mediterranean Sea."},
        "stem": "Which TWO features describe the physical geography of Europe?",
        "choices": [
            {"id": "A", "text": "The Alps mountain range crosses several countries", "correct": True},
            {"id": "B", "text": "Major rivers like the Rhine and Danube flow through it", "correct": True},
            {"id": "C", "text": "Europe has no coastline on any ocean or sea", "correct": False},
            {"id": "D", "text": "Europe is the largest continent on the planet", "correct": False}
        ],
        "answer_explanation": "Europe's physical geography includes the Alps mountain range and major rivers like the Rhine and Danube. Europe is actually one of the smallest continents and has extensive coastlines.",
        "difficulty": "easy",
        "tags": ["world-regions", "europe", "physical-features", "alps"],
        "generated_at": TIMESTAMP
    },

    # WR.1 - Physical and human characteristics (South America)
    {
        "id": "q_wr0004",
        "standard_code": "6-8.WR.1",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "South America is home to the Amazon River, which carries more water than any other river on Earth. The continent also has the Andes Mountains, the longest mountain range in the world, stretching along the western coast."},
        "stem": "What are two major physical features that define the geography of South America?",
        "choices": [
            {"id": "A", "text": "The Amazon River and the Andes Mountains", "correct": True},
            {"id": "B", "text": "The Nile River and the Rocky Mountains", "correct": False},
            {"id": "C", "text": "The Sahara Desert and the Great Barrier Reef", "correct": False},
            {"id": "D", "text": "The Mississippi River and the Alps Mountains", "correct": False}
        ],
        "answer_explanation": "The passage identifies the Amazon River (largest by water volume) and the Andes Mountains (longest mountain range) as two defining physical features of South America.",
        "difficulty": "easy",
        "tags": ["world-regions", "south-america", "amazon", "andes"],
        "generated_at": TIMESTAMP
    },

    # WR.2 - Compare cultures/governments/economies (democracy vs monarchy)
    {
        "id": "q_wr0005",
        "standard_code": "6-8.WR.2",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In the United States, citizens vote for their leaders in elections. In Saudi Arabia, the country is ruled by a king whose power is passed down through the royal family. Both systems are forms of government, but they work very differently."},
        "stem": "What is the key difference between these two forms of government?",
        "choices": [
            {"id": "A", "text": "One elects leaders while the other has a hereditary ruler", "correct": True},
            {"id": "B", "text": "Both countries choose leaders through popular elections", "correct": False},
            {"id": "C", "text": "Neither country allows citizens to participate in government", "correct": False},
            {"id": "D", "text": "Both countries are ruled by kings from royal families", "correct": False}
        ],
        "answer_explanation": "The U.S. is a democracy where leaders are elected by citizens. Saudi Arabia is a monarchy where power passes through the royal family. The key difference is how leaders gain power.",
        "difficulty": "medium",
        "tags": ["world-regions", "government", "democracy", "monarchy"],
        "generated_at": TIMESTAMP
    },

    # WR.2 - Compare cultures/governments/economies (developed vs developing)
    {
        "id": "q_wr0006",
        "standard_code": "6-8.WR.2",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Japan has a strong economy with advanced technology, high literacy rates, and modern hospitals. Many countries in Sub-Saharan Africa have growing economies but still face challenges with access to clean water, education, and healthcare."},
        "stem": "What does the passage suggest about the difference between these two world regions?",
        "choices": [
            {"id": "A", "text": "They are at different levels of economic development", "correct": True},
            {"id": "B", "text": "Japan has fewer natural resources than Africa does", "correct": False},
            {"id": "C", "text": "African countries have stronger economies than Japan", "correct": False},
            {"id": "D", "text": "Both regions face the exact same challenges today", "correct": False}
        ],
        "answer_explanation": "The passage contrasts Japan's advanced economy and services with the development challenges in Sub-Saharan Africa, showing they are at different levels of economic development.",
        "difficulty": "medium",
        "tags": ["world-regions", "economy", "development", "comparison"],
        "generated_at": TIMESTAMP
    },

    # WR.2 - Compare cultures/governments/economies (cultural comparison)
    {
        "id": "q_wr0007",
        "standard_code": "6-8.WR.2",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "In India, many people practice Hinduism and celebrate festivals like Diwali. In Brazil, most people are Christian and celebrate Carnival. Both countries have rich cultural traditions that reflect their unique histories."},
        "stem": "Which TWO conclusions can be drawn from comparing India and Brazil?",
        "choices": [
            {"id": "A", "text": "Different regions have different dominant religions", "correct": True},
            {"id": "B", "text": "Cultural celebrations reflect a region's history and beliefs", "correct": True},
            {"id": "C", "text": "Every country in the world celebrates the same holidays", "correct": False},
            {"id": "D", "text": "Religion has no influence on culture in either country", "correct": False}
        ],
        "answer_explanation": "India and Brazil show that different regions have different dominant religions and that cultural celebrations like Diwali and Carnival reflect each region's unique history and beliefs.",
        "difficulty": "easy",
        "tags": ["world-regions", "culture", "religion", "comparison"],
        "generated_at": TIMESTAMP
    },

    # WR.2 - Compare cultures/governments/economies (economic systems)
    {
        "id": "q_wr0008",
        "standard_code": "6-8.WR.2",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In a market economy, businesses and individuals make most economic decisions about what to produce and sell. In a command economy, the government controls most production and sets prices. Many countries today have a mix of both systems."},
        "stem": "What is the main difference between a market economy and a command economy?",
        "choices": [
            {"id": "A", "text": "Who decides what goods are produced and sold", "correct": True},
            {"id": "B", "text": "Whether the country has any natural resources", "correct": False},
            {"id": "C", "text": "How large the population of the country is", "correct": False},
            {"id": "D", "text": "What language the people of the country speak", "correct": False}
        ],
        "answer_explanation": "In a market economy, individuals and businesses make economic decisions. In a command economy, the government controls production and prices. The key difference is who makes economic decisions.",
        "difficulty": "medium",
        "tags": ["world-regions", "economy", "market", "command"],
        "generated_at": TIMESTAMP
    },

    # WR.3 - Countries, capitals, features (Africa)
    {
        "id": "q_wr0009",
        "standard_code": "6-8.WR.3",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Egypt is a country in northeastern Africa. Its capital city is Cairo, one of the largest cities on the continent. The Nile River flows through Egypt and has been important to the country for thousands of years."},
        "stem": "Based on the passage, what is the capital of Egypt and what major river flows through it?",
        "choices": [
            {"id": "A", "text": "Cairo is the capital, and the Nile River flows through it", "correct": True},
            {"id": "B", "text": "Alexandria is the capital, and the Congo River flows through it", "correct": False},
            {"id": "C", "text": "Cairo is the capital, and the Amazon River flows through it", "correct": False},
            {"id": "D", "text": "Nairobi is the capital, and the Nile River flows through it", "correct": False}
        ],
        "answer_explanation": "The passage states that Cairo is the capital of Egypt and that the Nile River flows through the country, making it one of the most important geographic features of Egypt.",
        "difficulty": "easy",
        "tags": ["world-regions", "africa", "egypt", "capitals", "nile"],
        "generated_at": TIMESTAMP
    },

    # WR.3 - Countries, capitals, features (Asia)
    {
        "id": "q_wr0010",
        "standard_code": "6-8.WR.3",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "China is the most populous country in the world and is located in East Asia. Its capital is Beijing. China's landscape includes the Gobi Desert in the north, the Himalaya Mountains in the southwest, and the Yangtze River, Asia's longest river."},
        "stem": "Which physical feature described in the passage is the longest river in Asia?",
        "choices": [
            {"id": "A", "text": "The Yangtze River in China", "correct": True},
            {"id": "B", "text": "The Gobi Desert in northern China", "correct": False},
            {"id": "C", "text": "The Himalaya Mountains in the southwest", "correct": False},
            {"id": "D", "text": "The capital city of Beijing in the east", "correct": False}
        ],
        "answer_explanation": "The passage identifies the Yangtze River as Asia's longest river. The Gobi is a desert, the Himalayas are mountains, and Beijing is a city, not a river.",
        "difficulty": "easy",
        "tags": ["world-regions", "asia", "china", "yangtze", "rivers"],
        "generated_at": TIMESTAMP
    },

    # WR.3 - Countries, capitals, features (South America)
    {
        "id": "q_wr0011",
        "standard_code": "6-8.WR.3",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Brazil is the largest country in South America. Its capital is Brasilia, although its largest city is Sao Paulo. The Amazon Rainforest covers a huge part of northern Brazil and is the largest tropical rainforest in the world."},
        "stem": "What is the capital of Brazil, and what major feature covers much of its northern area?",
        "choices": [
            {"id": "A", "text": "Brasilia is the capital, and the Amazon Rainforest covers the north", "correct": True},
            {"id": "B", "text": "Sao Paulo is the capital, and the Sahara Desert covers the north", "correct": False},
            {"id": "C", "text": "Brasilia is the capital, and the Andes Mountains cover the north", "correct": False},
            {"id": "D", "text": "Rio de Janeiro is the capital, and grasslands cover the north", "correct": False}
        ],
        "answer_explanation": "The passage states that Brasilia is Brazil's capital and the Amazon Rainforest covers a huge part of northern Brazil. Sao Paulo is the largest city but not the capital.",
        "difficulty": "easy",
        "tags": ["world-regions", "south-america", "brazil", "capitals", "amazon"],
        "generated_at": TIMESTAMP
    },

    # WR.3 - Countries, capitals, features (Europe)
    {
        "id": "q_wr0012",
        "standard_code": "6-8.WR.3",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multi_select",
        "stimulus": {"type": "text", "content": "Europe has many well-known countries and capitals. France has its capital in Paris. Germany's capital is Berlin. The United Kingdom's capital is London. All three countries are located in Western Europe."},
        "stem": "Which TWO pairings of European countries and their capitals are correct?",
        "choices": [
            {"id": "A", "text": "France and Paris", "correct": True},
            {"id": "B", "text": "Germany and Berlin", "correct": True},
            {"id": "C", "text": "France and London", "correct": False},
            {"id": "D", "text": "Germany and Paris", "correct": False}
        ],
        "answer_explanation": "France's capital is Paris and Germany's capital is Berlin. London is the capital of the United Kingdom, not France. Paris is France's capital, not Germany's.",
        "difficulty": "easy",
        "tags": ["world-regions", "europe", "capitals", "countries"],
        "generated_at": TIMESTAMP
    },

    # WR.4 - Trade and transportation (global trade routes)
    {
        "id": "q_wr0013",
        "standard_code": "6-8.WR.4",
        "standard_essential": False,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Suez Canal in Egypt connects the Mediterranean Sea to the Red Sea. Before the canal was built, ships traveling from Europe to Asia had to sail all the way around the southern tip of Africa, adding thousands of kilometers to the journey."},
        "stem": "How did the Suez Canal change trade between Europe and Asia?",
        "choices": [
            {"id": "A", "text": "It created a much shorter shipping route between them", "correct": True},
            {"id": "B", "text": "It stopped all trade between Europe and Asia completely", "correct": False},
            {"id": "C", "text": "It forced ships to travel a longer route around Africa", "correct": False},
            {"id": "D", "text": "It connected the Pacific Ocean to the Atlantic Ocean", "correct": False}
        ],
        "answer_explanation": "The Suez Canal created a shortcut between Europe and Asia by connecting the Mediterranean and Red Seas, eliminating the long route around Africa.",
        "difficulty": "medium",
        "tags": ["trade", "transportation", "suez-canal", "shipping"],
        "generated_at": TIMESTAMP
    },

    # WR.4 - Trade and transportation (resources and trade)
    {
        "id": "q_wr0014",
        "standard_code": "6-8.WR.4",
        "standard_essential": False,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Countries in the Middle East produce a large share of the world's oil. This oil is shipped by tanker to countries in Europe, Asia, and North America that need fuel for their cars, factories, and power plants."},
        "stem": "What does this example show about how trade connects different world regions?",
        "choices": [
            {"id": "A", "text": "Regions with resources sell to regions that need them", "correct": True},
            {"id": "B", "text": "Every region produces all the resources it needs", "correct": False},
            {"id": "C", "text": "Trade only happens between countries on the same continent", "correct": False},
            {"id": "D", "text": "Oil is not an important product in global trade today", "correct": False}
        ],
        "answer_explanation": "The Middle East has oil that other regions need. This shows how trade connects regions: areas rich in a resource export it to areas that lack that resource.",
        "difficulty": "easy",
        "tags": ["trade", "resources", "oil", "middle-east", "global-trade"],
        "generated_at": TIMESTAMP
    },

    # WR.4 - Trade and transportation (Panama Canal)
    {
        "id": "q_wr0015",
        "standard_code": "6-8.WR.4",
        "standard_essential": False,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Panama Canal is a waterway that cuts through Central America. It allows ships to travel between the Atlantic and Pacific Oceans without sailing around the southern tip of South America, saving weeks of travel time."},
        "stem": "Why is the Panama Canal important to world trade and transportation?",
        "choices": [
            {"id": "A", "text": "It provides a shortcut between the Atlantic and Pacific Oceans", "correct": True},
            {"id": "B", "text": "It blocks ships from crossing between two oceans", "correct": False},
            {"id": "C", "text": "It connects the Mediterranean Sea to the Indian Ocean", "correct": False},
            {"id": "D", "text": "It allows trains to cross from North to South America", "correct": False}
        ],
        "answer_explanation": "The Panama Canal provides a shortcut for ships traveling between the Atlantic and Pacific Oceans, saving thousands of kilometers and weeks of travel compared to going around South America.",
        "difficulty": "easy",
        "tags": ["trade", "transportation", "panama-canal", "shipping"],
        "generated_at": TIMESTAMP
    },

    # WR.5 - Political boundaries (how borders are set)
    {
        "id": "q_wr0016",
        "standard_code": "6-8.WR.5",
        "standard_essential": False,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Some country borders follow natural features like rivers and mountain ranges. For example, the Rhine River forms part of the border between France and Germany. Other borders are straight lines drawn by people, like many borders in Africa that were set by European colonial powers."},
        "stem": "What are two different ways that political borders between countries are established?",
        "choices": [
            {"id": "A", "text": "By following natural features or by being drawn by people", "correct": True},
            {"id": "B", "text": "By measuring population and by counting languages spoken", "correct": False},
            {"id": "C", "text": "By climate zones and by the direction of ocean currents", "correct": False},
            {"id": "D", "text": "By the age of the country and by its total land area", "correct": False}
        ],
        "answer_explanation": "Political borders can follow natural features like rivers and mountains, or they can be straight lines drawn by people, often during colonial periods as seen in Africa.",
        "difficulty": "medium",
        "tags": ["political-boundaries", "borders", "natural-features", "colonialism"],
        "generated_at": TIMESTAMP
    },

    # WR.5 - Political boundaries (borders change over time)
    {
        "id": "q_wr0017",
        "standard_code": "6-8.WR.5",
        "standard_essential": False,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "In 1991, the Soviet Union broke apart into 15 separate countries, including Russia, Ukraine, and Kazakhstan. Before 1991, all of these areas were part of one large country. This shows that political borders can change over time."},
        "stem": "What does the breakup of the Soviet Union show about political borders?",
        "choices": [
            {"id": "A", "text": "Country borders can change due to political events", "correct": True},
            {"id": "B", "text": "Country borders are permanent and never change", "correct": False},
            {"id": "C", "text": "Borders only change when natural disasters strike", "correct": False},
            {"id": "D", "text": "Borders are always decided by geographic features", "correct": False}
        ],
        "answer_explanation": "The Soviet Union splitting into 15 countries in 1991 is a major example of how political borders can change due to political events, wars, or independence movements.",
        "difficulty": "medium",
        "tags": ["political-boundaries", "soviet-union", "border-changes"],
        "generated_at": TIMESTAMP
    },

    # WR.6 - Rivers/mountains shape civilizations (Nile and Egypt)
    {
        "id": "q_wr0018",
        "standard_code": "6-8.WR.6",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "Ancient Egypt developed along the Nile River in northeastern Africa. Each year, the Nile flooded and left behind rich soil on its banks. Egyptian farmers used this soil to grow crops that fed millions of people for thousands of years."},
        "stem": "How did the Nile River help the civilization of ancient Egypt grow and thrive?",
        "choices": [
            {"id": "A", "text": "Annual floods left rich soil for growing crops", "correct": True},
            {"id": "B", "text": "The river kept enemy armies from ever attacking", "correct": False},
            {"id": "C", "text": "The Nile provided gold and silver for trade", "correct": False},
            {"id": "D", "text": "The river created a cold climate good for farming", "correct": False}
        ],
        "answer_explanation": "The Nile's annual floods deposited rich, fertile soil along its banks, allowing Egyptian farmers to grow enough food to support a large civilization for thousands of years.",
        "difficulty": "easy",
        "tags": ["rivers", "nile", "egypt", "civilization", "agriculture"],
        "generated_at": TIMESTAMP
    },

    # WR.6 - Rivers/mountains shape civilizations (mountains as trade barriers)
    {
        "id": "q_wr0019",
        "standard_code": "6-8.WR.6",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Andes Mountains run along the western coast of South America. These tall mountains made it very hard for people on the coast to trade with people living on the plains to the east. Ancient civilizations like the Inca built special roads and bridges to cross the mountains."},
        "stem": "How did the Andes Mountains affect trade and civilization in South America?",
        "choices": [
            {"id": "A", "text": "They created a barrier that made east-west trade difficult", "correct": True},
            {"id": "B", "text": "They provided a flat and easy path for trade wagons", "correct": False},
            {"id": "C", "text": "They blocked all rivers from flowing to the ocean", "correct": False},
            {"id": "D", "text": "They had no effect on how civilizations developed", "correct": False}
        ],
        "answer_explanation": "The Andes acted as a natural barrier between the coast and the interior, making trade difficult. The Inca built roads and bridges to overcome this challenge.",
        "difficulty": "medium",
        "tags": ["mountains", "andes", "trade-barriers", "inca", "civilization"],
        "generated_at": TIMESTAMP
    },

    # WR.6 - Rivers/mountains shape civilizations (Mediterranean Sea and trade)
    {
        "id": "q_wr0020",
        "standard_code": "6-8.WR.6",
        "standard_essential": True,
        "reporting_category": "World Regions",
        "domain": "World Regions",
        "question_type": "multiple_choice",
        "stimulus": {"type": "text", "content": "The Mediterranean Sea is surrounded by parts of Europe, Africa, and Asia. For thousands of years, ancient civilizations like Greece, Rome, and Phoenicia used the sea for trade, fishing, and travel. The sea connected these cultures and helped them share goods and ideas."},
        "stem": "Based on the passage, how did people around the Mediterranean Sea use it long ago?",
        "choices": [
            {"id": "A", "text": "It connected civilizations and helped them trade ideas and goods", "correct": True},
            {"id": "B", "text": "It kept all ancient civilizations completely separated", "correct": False},
            {"id": "C", "text": "It provided farmland for growing crops along its floor", "correct": False},
            {"id": "D", "text": "It blocked travel between Europe, Africa, and Asia", "correct": False}
        ],
        "answer_explanation": "The Mediterranean Sea served as a highway for trade and travel, connecting civilizations in Europe, Africa, and Asia. This allowed them to share goods, ideas, and culture.",
        "difficulty": "medium",
        "tags": ["bodies-of-water", "mediterranean", "trade", "civilization"],
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
