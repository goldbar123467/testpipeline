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
