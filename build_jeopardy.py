#!/usr/bin/env python3
"""Build a self-contained Jeopardy HTML game from the approved question bank."""

import json
import os
from collections import defaultdict

APPROVED_DIR = os.path.join(os.path.dirname(__file__), "bank", "approved")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "jeopardy.html")

DIFF_ORDER = {"easy": 0, "medium": 1, "hard": 2}

# Fun Jeopardy-style category names per domain
CATEGORY_NAMES = {
    "Civics": [
        "We the People",
        "Rights & Rules",
        "Leaders & Laws",
        "Civic Duty",
        "Government in Action",
        "Democracy Now",
        "Liberty & Justice",
        "Checks & Balances",
    ],
    "History": [
        "Back in Time",
        "American Story",
        "History Makers",
        "The Past Speaks",
        "Founding Days",
        "Ages & Eras",
    ],
    "Geography": [
        "Map It Out",
        "Where in the World?",
    ],
    "Economics": [
        "Money Matters",
        "Buy & Sell",
        "Dollars & Sense",
    ],
    "Mixed": [
        "Potpourri",
    ],
}


def load_questions():
    questions = []
    for f in sorted(os.listdir(APPROVED_DIR)):
        if f.endswith(".json"):
            with open(os.path.join(APPROVED_DIR, f)) as fh:
                questions.append(json.load(fh))
    return questions


def organize_into_rounds(questions):
    """Organize 100 questions into 4 rounds of 5 categories × 5 questions."""
    by_domain = defaultdict(list)
    for q in questions:
        by_domain[q["domain"]].append(q)

    # Sort each domain by difficulty
    for domain in by_domain:
        by_domain[domain].sort(key=lambda q: DIFF_ORDER.get(q["difficulty"], 1))

    # Split each domain into chunks of 5
    domain_chunks = {}
    for domain, qs in by_domain.items():
        chunks = []
        for i in range(0, len(qs), 5):
            chunk = qs[i : i + 5]
            if len(chunk) == 5:
                chunks.append(chunk)
            else:
                # Leftover questions
                domain_chunks.setdefault("_leftover", []).extend(chunk)
        domain_chunks[domain] = chunks

    # Handle leftovers - combine into Mixed category chunks
    leftovers = domain_chunks.pop("_leftover", [])
    if leftovers:
        # Pad with any available extra or just use what we have
        while len(leftovers) < 5:
            # Steal from largest domain
            largest = max(domain_chunks, key=lambda d: len(domain_chunks[d]))
            if domain_chunks[largest]:
                stolen = domain_chunks[largest].pop()
                leftovers.extend(stolen)
            else:
                break
        # Re-chunk leftovers into groups of 5
        mixed_chunks = []
        for i in range(0, len(leftovers), 5):
            chunk = leftovers[i : i + 5]
            if len(chunk) == 5:
                mixed_chunks.append(chunk)
        domain_chunks["Mixed"] = mixed_chunks

    # Build 4 rounds, each with 5 categories - interleave domains for variety
    rounds = [[] for _ in range(4)]
    name_idx = defaultdict(int)

    # Create a pool of (domain, chunk) pairs
    pool = []
    for domain, chunks in domain_chunks.items():
        for chunk in chunks:
            pool.append((domain, chunk))

    # Sort pool so we interleave domains: cycle through domains round-robin
    domain_order = ["Civics", "History", "Economics", "Geography", "Mixed"]
    sorted_pool = []
    domain_queues = defaultdict(list)
    for domain, chunk in pool:
        domain_queues[domain].append(chunk)

    # Round-robin pick from domains
    while any(domain_queues[d] for d in domain_queues):
        for d in domain_order:
            if domain_queues[d]:
                sorted_pool.append((d, domain_queues[d].pop(0)))

    # Distribute into 4 rounds of 5, now with interleaved domains
    for idx, (domain, chunk) in enumerate(sorted_pool):
        r = idx // 5
        if r >= 4:
            break

        cat_names = CATEGORY_NAMES.get(domain, ["Bonus"])
        ni = name_idx[domain]
        cat_name = cat_names[ni % len(cat_names)]
        name_idx[domain] = ni + 1

        # Sort chunk by difficulty for point value assignment
        chunk.sort(key=lambda q: DIFF_ORDER.get(q["difficulty"], 1))

        rounds[r].append(
            {"name": cat_name, "domain": domain, "questions": chunk}
        )

    return rounds


def build_html(rounds):
    """Generate the complete Jeopardy HTML game."""
    rounds_json = json.dumps(rounds, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>5th Grade Social Studies Jeopardy!</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: #060CE9;
  color: #fff;
  min-height: 100vh;
}}

/* ── Setup Screen ── */
#setup-screen {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 2rem;
}}

#setup-screen h1 {{
  font-family: 'Impact', 'Arial Black', sans-serif;
  font-size: 3.5rem;
  color: #FFD700;
  text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
  margin-bottom: 0.5rem;
  text-align: center;
  letter-spacing: 2px;
}}

#setup-screen h2 {{
  font-size: 1.3rem;
  color: #ADD8E6;
  margin-bottom: 2rem;
  font-weight: normal;
}}

.setup-box {{
  background: rgba(0,0,0,0.3);
  border-radius: 16px;
  padding: 2rem;
  width: 100%;
  max-width: 500px;
}}

.setup-box label {{
  display: block;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  color: #FFD700;
}}

.setup-box input, .setup-box select {{
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #FFD700;
  border-radius: 8px;
  font-size: 1rem;
  background: #000080;
  color: #fff;
  margin-bottom: 1rem;
}}

.setup-box input::placeholder {{ color: #8888cc; }}

#team-inputs {{ margin-top: 1rem; }}

.team-input-row {{
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}}

.team-color-dot {{
  width: 20px;
  height: 20px;
  border-radius: 50%;
  flex-shrink: 0;
}}

.team-input-row input {{ margin-bottom: 0; }}

#start-btn {{
  display: block;
  width: 100%;
  padding: 1rem;
  margin-top: 1.5rem;
  font-size: 1.4rem;
  font-weight: bold;
  background: #FFD700;
  color: #060CE9;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  letter-spacing: 1px;
  transition: transform 0.1s, box-shadow 0.2s;
}}

#start-btn:hover {{ transform: scale(1.03); box-shadow: 0 4px 20px rgba(255,215,0,0.4); }}

/* ── Game Screen ── */
#game-screen {{ display: none; padding: 1rem; }}

/* Scoreboard */
#scoreboard {{
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
  padding: 0.75rem;
  background: rgba(0,0,0,0.3);
  border-radius: 12px;
}}

.team-score-card {{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 1.5rem;
  border-radius: 10px;
  min-width: 150px;
  border: 3px solid transparent;
  transition: border-color 0.3s;
}}

.team-score-card.active {{ border-color: #FFD700; }}

.team-score-card .team-name {{
  font-weight: bold;
  font-size: 1rem;
  margin-bottom: 0.25rem;
}}

.team-score-card .team-score {{
  font-size: 2rem;
  font-weight: bold;
  color: #FFD700;
}}

.score-buttons {{
  display: flex;
  gap: 0.3rem;
  margin-top: 0.25rem;
}}

.score-buttons button {{
  padding: 0.2rem 0.5rem;
  font-size: 0.75rem;
  border: 1px solid rgba(255,255,255,0.3);
  background: rgba(255,255,255,0.1);
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}}

.score-buttons button:hover {{ background: rgba(255,255,255,0.25); }}

/* Round Navigation */
#round-nav {{
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}}

.round-btn {{
  padding: 0.5rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  border: 2px solid #FFD700;
  background: transparent;
  color: #FFD700;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}}

.round-btn.active, .round-btn:hover {{
  background: #FFD700;
  color: #060CE9;
}}

.round-btn.round-complete {{
  opacity: 0.5;
  text-decoration: line-through;
}}

/* Jeopardy Board */
#board {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 6px;
  max-width: 1100px;
  margin: 0 auto;
}}

.category-header {{
  background: #000080;
  padding: 1rem 0.5rem;
  text-align: center;
  font-weight: bold;
  font-size: 0.95rem;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 1px;
  min-height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}}

.cell {{
  background: #000080;
  padding: 1rem;
  text-align: center;
  font-size: 1.8rem;
  font-weight: bold;
  color: #FFD700;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  min-height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  user-select: none;
}}

.cell:hover {{ background: #0000AA; transform: scale(1.03); }}
.cell.answered {{
  background: #1a1a4e;
  color: #333366;
  cursor: default;
  transform: none;
}}

/* ── Question Modal ── */
#modal-overlay {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.85);
  z-index: 1000;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}}

#modal-overlay.visible {{ display: flex; }}

#modal {{
  background: #060CE9;
  border: 4px solid #FFD700;
  border-radius: 16px;
  padding: 2rem;
  max-width: 750px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}}

#modal-points {{
  position: absolute;
  top: -18px;
  left: 50%;
  transform: translateX(-50%);
  background: #FFD700;
  color: #060CE9;
  font-weight: bold;
  font-size: 1.2rem;
  padding: 0.3rem 1.5rem;
  border-radius: 20px;
}}

#modal-category {{
  text-align: center;
  font-size: 0.9rem;
  color: #ADD8E6;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}}

#modal-stimulus {{
  background: rgba(0,0,0,0.3);
  border-left: 4px solid #FFD700;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 0 8px 8px 0;
  font-size: 1rem;
  line-height: 1.6;
  white-space: pre-wrap;
}}

#modal-stem {{
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  line-height: 1.4;
  text-align: center;
}}

#modal-choices {{
  list-style: none;
  margin-bottom: 1.5rem;
}}

#modal-choices li {{
  background: rgba(0,0,0,0.25);
  border: 2px solid rgba(255,255,255,0.2);
  border-radius: 10px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  font-size: 1.05rem;
  transition: all 0.3s;
  display: flex;
  gap: 0.75rem;
}}

#modal-choices li .choice-id {{
  font-weight: bold;
  color: #FFD700;
  flex-shrink: 0;
}}

#modal-choices li.correct {{
  border-color: #00C853;
  background: rgba(0,200,83,0.2);
}}

#modal-choices li.incorrect {{
  border-color: #FF1744;
  background: rgba(255,23,68,0.1);
  opacity: 0.6;
}}

#answer-section {{
  display: none;
  margin-top: 1rem;
}}

#modal-explanation {{
  background: rgba(0,200,83,0.15);
  border-left: 4px solid #00C853;
  padding: 1rem;
  border-radius: 0 8px 8px 0;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
  line-height: 1.5;
}}

/* Award Points Section */
#award-section {{
  display: none;
  text-align: center;
  margin-top: 1rem;
}}

#award-section p {{
  font-size: 1rem;
  margin-bottom: 0.75rem;
  color: #ADD8E6;
}}

.award-buttons {{
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  flex-wrap: wrap;
}}

.award-btn {{
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  font-weight: bold;
  border: 2px solid;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}}

.award-btn:hover {{ transform: scale(1.05); }}

.no-award-btn {{
  padding: 0.6rem 1.2rem;
  font-size: 0.9rem;
  border: 2px solid rgba(255,255,255,0.3);
  background: transparent;
  color: #fff;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 0.5rem;
}}

.no-award-btn:hover {{ background: rgba(255,255,255,0.1); }}

/* Modal Buttons */
.modal-btn-row {{
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin-top: 1.5rem;
}}

.modal-btn {{
  padding: 0.7rem 2rem;
  font-size: 1.1rem;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
}}

.modal-btn:hover {{ transform: scale(1.05); }}

#reveal-btn {{
  background: #FFD700;
  color: #060CE9;
}}

#close-btn {{
  background: rgba(255,255,255,0.15);
  color: #fff;
  border: 2px solid rgba(255,255,255,0.3);
}}

/* Multi-select badge */
.multi-badge {{
  display: inline-block;
  background: #FF6D00;
  color: #fff;
  font-size: 0.75rem;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  margin-bottom: 0.5rem;
}}

/* Winner screen */
#winner-screen {{
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 2rem;
  text-align: center;
}}

#winner-screen h1 {{
  font-family: 'Impact', 'Arial Black', sans-serif;
  font-size: 4rem;
  color: #FFD700;
  text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
  margin-bottom: 1rem;
}}

#winner-screen .final-scores {{
  margin: 2rem 0;
}}

.final-score-row {{
  font-size: 1.5rem;
  margin: 0.75rem 0;
  padding: 0.75rem 2rem;
  border-radius: 10px;
}}

.final-score-row.winner {{
  font-size: 2rem;
  font-weight: bold;
  color: #FFD700;
  background: rgba(255,215,0,0.15);
  border: 2px solid #FFD700;
}}

#play-again-btn {{
  padding: 1rem 3rem;
  font-size: 1.3rem;
  font-weight: bold;
  background: #FFD700;
  color: #060CE9;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 2rem;
}}

#play-again-btn:hover {{ transform: scale(1.05); }}

/* Deduct toggle */
.deduct-toggle {{
  margin-top: 0.5rem;
}}

.deduct-toggle label {{
  font-size: 0.85rem;
  color: #ADD8E6;
  cursor: pointer;
}}

.deduct-toggle input {{ margin-right: 0.3rem; }}

/* Responsive */
@media (max-width: 768px) {{
  #board {{ gap: 3px; }}
  .cell {{ font-size: 1.2rem; min-height: 55px; padding: 0.5rem; }}
  .category-header {{ font-size: 0.7rem; min-height: 55px; padding: 0.5rem; }}
  #setup-screen h1 {{ font-size: 2.2rem; }}
  .team-score-card {{ min-width: 100px; padding: 0.4rem 0.75rem; }}
  .team-score-card .team-score {{ font-size: 1.5rem; }}
}}
</style>
</head>
<body>

<!-- ════════ SETUP SCREEN ════════ -->
<div id="setup-screen">
  <h1>JEOPARDY!</h1>
  <h2>5th Grade Social Studies Edition</h2>
  <div class="setup-box">
    <label for="num-teams">Number of Teams</label>
    <select id="num-teams" onchange="updateTeamInputs()">
      <option value="2">2 Teams</option>
      <option value="3">3 Teams</option>
      <option value="4">4 Teams</option>
    </select>
    <div id="team-inputs"></div>
    <button id="start-btn" onclick="startGame()">LET'S PLAY!</button>
  </div>
</div>

<!-- ════════ GAME SCREEN ════════ -->
<div id="game-screen">
  <div id="scoreboard"></div>
  <div id="round-nav"></div>
  <div id="board"></div>
  <div style="text-align:center; margin-top:1.5rem;">
    <button onclick="endGame()" style="padding:0.5rem 1.5rem; font-size:1rem; background:#FF1744; color:#fff; border:none; border-radius:8px; cursor:pointer; font-weight:bold;">End Game</button>
  </div>
</div>

<!-- ════════ QUESTION MODAL ════════ -->
<div id="modal-overlay">
  <div id="modal">
    <div id="modal-points"></div>
    <div id="modal-category"></div>
    <div id="modal-stimulus"></div>
    <div id="modal-multi-badge"></div>
    <div id="modal-stem"></div>
    <ul id="modal-choices"></ul>
    <div class="modal-btn-row">
      <button id="reveal-btn" class="modal-btn" onclick="revealAnswer()">Show Answer</button>
    </div>
    <div id="answer-section">
      <div id="modal-explanation"></div>
      <div id="award-section">
        <p>Award points to:</p>
        <div class="award-buttons" id="award-buttons"></div>
        <div class="deduct-toggle">
          <label><input type="checkbox" id="deduct-check"> Deduct from wrong answers</label>
        </div>
        <br>
        <button class="no-award-btn" onclick="closeModal()">No One &mdash; Close</button>
      </div>
    </div>
  </div>
</div>

<!-- ════════ WINNER SCREEN ════════ -->
<div id="winner-screen">
  <h1>GAME OVER!</h1>
  <div class="final-scores" id="final-scores"></div>
  <button id="play-again-btn" onclick="location.reload()">Play Again</button>
</div>

<script>
// ══════════════════════════════════════
//  GAME DATA (auto-generated from question bank)
// ══════════════════════════════════════
const ROUNDS = {rounds_json};

// ══════════════════════════════════════
//  TEAM COLORS
// ══════════════════════════════════════
const TEAM_COLORS = ['#FF6D00', '#00BFA5', '#AA00FF', '#FF1744'];

// ══════════════════════════════════════
//  GAME STATE
// ══════════════════════════════════════
let teams = [];
let currentRound = 0;
let answered = {{}}; // "round-col-row" => true
let currentQuestion = null;
let currentPoints = 0;

const POINT_VALUES = [200, 400, 600, 800, 1000];

// ══════════════════════════════════════
//  SETUP
// ══════════════════════════════════════
function updateTeamInputs() {{
  const n = parseInt(document.getElementById('num-teams').value);
  const container = document.getElementById('team-inputs');
  container.innerHTML = '';
  for (let i = 0; i < n; i++) {{
    const row = document.createElement('div');
    row.className = 'team-input-row';
    row.innerHTML = `
      <span class="team-color-dot" style="background:${{TEAM_COLORS[i]}}"></span>
      <input type="text" id="team-name-${{i}}" placeholder="Team ${{i+1}} Name" value="Team ${{i+1}}">
    `;
    container.appendChild(row);
  }}
}}

function startGame() {{
  const n = parseInt(document.getElementById('num-teams').value);
  teams = [];
  for (let i = 0; i < n; i++) {{
    const name = document.getElementById(`team-name-${{i}}`).value.trim() || `Team ${{i+1}}`;
    teams.push({{ name, score: 0, color: TEAM_COLORS[i] }});
  }}
  document.getElementById('setup-screen').style.display = 'none';
  document.getElementById('game-screen').style.display = 'block';
  renderScoreboard();
  renderRoundNav();
  renderBoard();
}}

// ══════════════════════════════════════
//  SCOREBOARD
// ══════════════════════════════════════
function renderScoreboard() {{
  const sb = document.getElementById('scoreboard');
  sb.innerHTML = teams.map((t, i) => `
    <div class="team-score-card" id="team-card-${{i}}" style="background:${{t.color}}22">
      <span class="team-name" style="color:${{t.color}}">${{t.name}}</span>
      <span class="team-score" id="score-${{i}}">$${{t.score.toLocaleString()}}</span>
      <div class="score-buttons">
        <button onclick="manualScore(${{i}}, -100)">-100</button>
        <button onclick="manualScore(${{i}}, 100)">+100</button>
      </div>
    </div>
  `).join('');
}}

function updateScores() {{
  teams.forEach((t, i) => {{
    document.getElementById(`score-${{i}}`).textContent = `$${{t.score.toLocaleString()}}`;
  }});
}}

function manualScore(teamIdx, amount) {{
  teams[teamIdx].score += amount;
  updateScores();
}}

// ══════════════════════════════════════
//  ROUND NAV
// ══════════════════════════════════════
function renderRoundNav() {{
  const nav = document.getElementById('round-nav');
  nav.innerHTML = ROUNDS.map((_, i) => `
    <button class="round-btn ${{i === currentRound ? 'active' : ''}}"
            id="round-btn-${{i}}" onclick="switchRound(${{i}})">
      Round ${{i+1}}
    </button>
  `).join('');
}}

function switchRound(r) {{
  currentRound = r;
  document.querySelectorAll('.round-btn').forEach((btn, i) => {{
    btn.classList.toggle('active', i === r);
  }});
  renderBoard();
  checkRoundComplete();
}}

function checkRoundComplete() {{
  ROUNDS.forEach((round, ri) => {{
    let total = round.length * 5;
    let done = 0;
    for (let c = 0; c < round.length; c++) {{
      for (let row = 0; row < 5; row++) {{
        if (answered[`${{ri}}-${{c}}-${{row}}`]) done++;
      }}
    }}
    const btn = document.getElementById(`round-btn-${{ri}}`);
    if (btn) btn.classList.toggle('round-complete', done === total && total > 0);
  }});
}}

// ══════════════════════════════════════
//  BOARD
// ══════════════════════════════════════
function renderBoard() {{
  const board = document.getElementById('board');
  const round = ROUNDS[currentRound];
  if (!round) return;

  let html = '';
  // Category headers
  round.forEach(cat => {{
    html += `<div class="category-header">${{cat.name}}</div>`;
  }});

  // Question cells (5 rows)
  for (let row = 0; row < 5; row++) {{
    round.forEach((cat, col) => {{
      const key = `${{currentRound}}-${{col}}-${{row}}`;
      const isAnswered = answered[key];
      const points = POINT_VALUES[row];
      html += `<div class="cell ${{isAnswered ? 'answered' : ''}}"
                    onclick="openQuestion(${{col}}, ${{row}})"
                    id="cell-${{key}}">
                ${{isAnswered ? '' : '&#36;' + points}}
              </div>`;
    }});
  }}
  board.innerHTML = html;
}}

// ══════════════════════════════════════
//  QUESTION MODAL
// ══════════════════════════════════════
function openQuestion(col, row) {{
  const key = `${{currentRound}}-${{col}}-${{row}}`;
  if (answered[key]) return;

  const round = ROUNDS[currentRound];
  const cat = round[col];
  const q = cat.questions[row];
  if (!q) return;

  currentQuestion = {{ col, row, key, question: q }};
  currentPoints = POINT_VALUES[row];

  // Populate modal
  document.getElementById('modal-points').textContent = `$${{currentPoints}}`;
  document.getElementById('modal-category').textContent = cat.name + ' \u2014 ' + cat.domain;

  // Stimulus
  const stimEl = document.getElementById('modal-stimulus');
  if (q.stimulus && q.stimulus.content) {{
    stimEl.textContent = q.stimulus.content;
    stimEl.style.display = 'block';
  }} else {{
    stimEl.style.display = 'none';
  }}

  // Multi-select badge
  const badgeEl = document.getElementById('modal-multi-badge');
  if (q.question_type === 'multi_select') {{
    const correctCount = q.choices.filter(c => c.correct).length;
    badgeEl.innerHTML = `<span class="multi-badge">Select ${{correctCount}} answers</span>`;
  }} else {{
    badgeEl.innerHTML = '';
  }}

  // Stem
  document.getElementById('modal-stem').textContent = q.stem;

  // Choices (hidden answer state)
  const choicesEl = document.getElementById('modal-choices');
  choicesEl.innerHTML = q.choices.map(c => `
    <li id="choice-${{c.id}}" data-correct="${{c.correct}}">
      <span class="choice-id">${{c.id}}.</span>
      <span>${{c.text}}</span>
    </li>
  `).join('');

  // Reset states
  document.getElementById('answer-section').style.display = 'none';
  document.getElementById('award-section').style.display = 'none';
  document.getElementById('reveal-btn').style.display = 'inline-block';
  document.getElementById('modal-explanation').textContent = '';

  // Show modal
  document.getElementById('modal-overlay').classList.add('visible');
}}

function revealAnswer() {{
  if (!currentQuestion) return;
  const q = currentQuestion.question;

  // Highlight correct/incorrect
  q.choices.forEach(c => {{
    const li = document.getElementById(`choice-${{c.id}}`);
    li.classList.add(c.correct ? 'correct' : 'incorrect');
  }});

  // Show explanation
  document.getElementById('modal-explanation').textContent = q.answer_explanation;
  document.getElementById('answer-section').style.display = 'block';

  // Show award buttons
  const awardDiv = document.getElementById('award-buttons');
  awardDiv.innerHTML = teams.map((t, i) => `
    <button class="award-btn"
            style="background:${{t.color}}33; border-color:${{t.color}}; color:${{t.color}}"
            onclick="awardPoints(${{i}})">
      ${{t.name}}
    </button>
  `).join('');
  document.getElementById('award-section').style.display = 'block';

  // Hide reveal button
  document.getElementById('reveal-btn').style.display = 'none';
}}

function awardPoints(teamIdx) {{
  teams[teamIdx].score += currentPoints;

  // Optional deduction for others
  if (document.getElementById('deduct-check').checked) {{
    teams.forEach((t, i) => {{
      if (i !== teamIdx) t.score -= currentPoints;
    }});
  }}

  updateScores();
  closeModal();
}}

function closeModal() {{
  if (currentQuestion) {{
    answered[currentQuestion.key] = true;
    renderBoard();
    checkRoundComplete();
  }}
  document.getElementById('modal-overlay').classList.remove('visible');
  currentQuestion = null;
}}

// Close modal on overlay click
document.getElementById('modal-overlay').addEventListener('click', function(e) {{
  if (e.target === this) {{
    // Don't close without marking answered if question was opened
    if (currentQuestion) closeModal();
  }}
}});

// Keyboard: Escape to close
document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape' && currentQuestion) closeModal();
}});

// ══════════════════════════════════════
//  END GAME
// ══════════════════════════════════════
function endGame() {{
  document.getElementById('game-screen').style.display = 'none';
  const ws = document.getElementById('winner-screen');
  ws.style.display = 'flex';

  // Sort teams by score descending
  const sorted = [...teams].sort((a, b) => b.score - a.score);
  const topScore = sorted[0].score;

  document.getElementById('final-scores').innerHTML = sorted.map((t, i) => `
    <div class="final-score-row ${{t.score === topScore ? 'winner' : ''}}"
         style="color:${{t.color}}; background:${{t.color}}11; border:2px solid ${{t.color}}33">
      ${{t.score === topScore ? '&#127942; ' : ''}}${{t.name}}: $${{t.score.toLocaleString()}}
    </div>
  `).join('');
}}

// ══════════════════════════════════════
//  INIT
// ══════════════════════════════════════
updateTeamInputs();
</script>

</body>
</html>"""
    return html


def main():
    questions = load_questions()
    print(f"Loaded {len(questions)} questions")

    rounds = organize_into_rounds(questions)
    for i, r in enumerate(rounds):
        cats = ", ".join(f"{c['name']} ({c['domain']})" for c in r)
        total = sum(len(c["questions"]) for c in r)
        print(f"Round {i+1} [{total} Qs]: {cats}")

    html = build_html(rounds)
    with open(OUTPUT_FILE, "w") as f:
        f.write(html)
    print(f"\nGenerated: {OUTPUT_FILE}")
    print(f"File size: {len(html):,} bytes")


if __name__ == "__main__":
    main()
