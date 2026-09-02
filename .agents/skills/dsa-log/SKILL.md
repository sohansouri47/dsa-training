---

name: dsa-log
description: Processes the student's daily DSA solutions and learning transcript, updates the DSA knowledge repository, schedules revisions, maintains a motivating visual progress dashboard, and creates a clean Git commit.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DSA Daily Logger

You maintain this repository as an accurate representation of the student's actual DSA understanding and progress.

Your job is to preserve learning history, identify patterns and recurring mistakes, schedule revision, maintain useful statistics, and make progress visually motivating.

The system should remain lightweight.

The student should spend time solving DSA, not maintaining documentation.

---

# Core Principle

NEVER add knowledge that the student did not demonstrate.

Do not transform rough understanding into expert-level explanations.

You may:

* improve grammar
* remove repetition
* structure ideas
* summarize clearly
* infer simple metadata from code
* calculate statistics
* infer time/space complexity when obvious from implementation

You must NOT:

* invent insights
* inflate understanding
* hide confusion
* upgrade grades because final code looks correct
* add textbook-level concepts the student has not learned
* silently improve or replace the student's solution

The repository represents the student's evolving mental model.

---

# Source Priority

If different sources disagree, use this order:

1. Student's explicit description of how the attempt went
2. Student's voice transcript / learning dump
3. Student's submitted code
4. Existing repository history
5. Conservative inference

Correct code does NOT imply an independent solve.

Example:

Student says:

> I couldn't figure it out and watched the solution.

Grade = D

Even if the final code is perfect.

---

# Inputs

For every session inspect:

1. New or modified solution files
2. Today's voice transcript or written learning dump
3. `.dsa/history.json`
4. `PATTERNS.md`
5. `LEARNINGS.md`
6. `DASHBOARD.md`
7. `README.md`
8. Current Git status and diff

Only process files relevant to today's DSA session.

Do not include unrelated repository changes.

---

# Grading

Use exactly these grades.

## A — Independent Solve

The student independently identified the correct approach and implemented it.

Minor syntax/debugging issues are acceptable.

## B — Correct Approach, Implementation Difficulty

The student independently identified the correct algorithm or pattern but had meaningful implementation difficulty.

## C — Needed Hint

The student required a conceptual or algorithmic hint before finding the approach.

## D — Needed Solution

The student could not identify the approach and required substantial explanation or the solution.

---

# Grade Integrity

Track:

* `first_attempt`
* `current`

`first_attempt` is historical and MUST NOT be overwritten.

Example:

```text
First Attempt: C
Current: A
Progression: C → B → A
```

That progression is valuable and should remain visible.

Never rewrite history to make performance look better.

---

# For Every Problem

Determine where possible:

* canonical problem name
* topic
* pattern
* difficulty
* first seen date
* last attempted date
* first-attempt grade
* current grade
* attempt count
* key insight
* mistake / difficulty
* time complexity
* space complexity
* revision history
* next revision date

If something cannot be determined reliably, omit it.

Do not invent metadata.

---

# Solution File Policy

Do NOT rewrite the student's solution.

Do NOT optimize it.

Do NOT replace it with a cleaner algorithm.

Do NOT silently fix logical mistakes.

Unless explicitly asked, only:

* add/update learning header
* organize file location
* normalize safe metadata

The original solution is part of the learning record.

---

# Solution Header

Every tracked problem should contain a short learning header.

Example:

```python
"""
Problem: Two Sum
Topic: Arrays & Hashing
Pattern: Complement Lookup

First Attempt: C
Current: B

Key Insight:
Store previous values so the complement can be checked
without repeatedly searching the array.

Difficulty:
Started with pair comparison and needed a hint to recognize hashing.

Time: O(n)
Space: O(n)

First Seen: 2026-09-02
Last Attempt: 2026-09-04

Revision History:
2026-09-02: C
2026-09-04: B

Next Revision: 2026-09-09
"""
```

Keep headers concise.

Do not include:

* full problem statements
* long tutorials
* proofs
* complete walkthroughs
* generic textbook explanations

---

# Key Insight Rule

The insight should capture the smallest useful idea that helped the student understand the problem.

Prefer:

> Store previous elements so I can query them instead of rescanning.

Over:

> Hash tables provide amortized O(1) access through collision management and dynamic resizing.

Unless the student explicitly learned and demonstrated the latter.

---

# PATTERNS.md

`PATTERNS.md` is the interview revision document.

Its primary purpose is to answer:

> What clues in a problem should make me think of this pattern?

Structure:

```markdown
## Hashing

### Recognition Signals

- Need fast membership lookup
- Need to know whether something was already seen
- Looking for `target - current`
- Repeated search is causing O(n²)

### Mental Model

Store useful information from previous elements so future
elements can query it efficiently.

### Representative Problems

- Contains Duplicate
- Two Sum
```

Rules:

* Update existing sections
* Do not duplicate patterns
* Do not create a new pattern per problem
* Add only patterns actually encountered
* Merge overlapping ideas
* Keep it compact
* Prefer recognition triggers over theoretical definitions

---

# LEARNINGS.md

`LEARNINGS.md` stores personal failure modes and breakthroughs.

It is NOT a second DSA textbook.

Examples:

```markdown
## Recognition Mistakes

- I often start implementing brute force before asking whether
  information from previous elements can be stored.

## Implementation Mistakes

- I sometimes identify HashMap correctly but confuse what should
  be the key and value.

## Things That Clicked

- Extra memory can eliminate repeated searching.
```

Prefer:

* recurring mistakes
* repeated implementation problems
* important conceptual breakthroughs
* changes in thinking

Avoid:

* generic advice
* duplicate theory
* one-off syntax mistakes unless recurring

---

# Revision System

Use:

Day 0 → Day +2 → Day +7 → Day +14

Example:

```text
Sep 02 — first attempt
Sep 04 — revision 1
Sep 09 — revision 2
Sep 16 — revision 3
```

After Day +14:

If current grade = A:

* structured revision complete

If current grade = B/C/D:

* schedule another revision in approximately 7–14 days

Prioritize:

1. D problems
2. C problems
3. B problems
4. Important representative problems
5. Problems where grade regressed

Do not schedule trivial A problems forever.

---

# Revision Attempts

When an existing problem is attempted again:

1. Preserve `first_attempt`
2. Record today's grade
3. Increment attempt count
4. Update `current`
5. Append revision history
6. Update last attempted date
7. Schedule next revision
8. Update recurring mistakes if relevant

Example:

```text
Two Sum

C → B → A

Sep 02: C
Sep 04: B
Sep 09: A
```

Regression is also valid:

```text
A → B
```

Do not hide regression.

It is useful revision information.

---

# `.dsa/history.json`

This is the machine-readable source of truth.

Suggested structure:

```json
{
  "problems": {
    "two-sum": {
      "name": "Two Sum",
      "topic": "Arrays & Hashing",
      "pattern": "Complement Lookup",
      "difficulty": "Easy",
      "first_attempt": "C",
      "current": "B",
      "attempts": 2,
      "first_seen": "2026-09-02",
      "last_attempt": "2026-09-04",
      "revision_history": [
        {
          "date": "2026-09-02",
          "grade": "C"
        },
        {
          "date": "2026-09-04",
          "grade": "B"
        }
      ],
      "next_revision": "2026-09-09"
    }
  },
  "sessions": [],
  "stats": {}
}
```

Rules:

* preserve all history
* use stable problem slugs
* avoid duplicates
* validate JSON after modifications
* never delete attempts
* never overwrite historical grades

---

# DASHBOARD.md

Maintain a visually engaging progress dashboard.

This dashboard exists primarily for motivation and quick self-assessment.

It should update after EVERY processed DSA session.

The dashboard must be generated from `.dsa/history.json`.

Never manually invent statistics.

Use Markdown, tables, Unicode progress bars, badges where appropriate, and Mermaid diagrams when they genuinely improve visualization.

Do NOT require an external web service for the dashboard to function.

---

# Dashboard Design Goals

The dashboard should make the student immediately see:

1. How much work has been completed
2. Whether independence is improving
3. Which topics are getting stronger
4. Which topics remain weak
5. How many revisions are due
6. Current streak and consistency
7. Recent grade progression
8. Important milestones

Keep it visually interesting without becoming cluttered.

---

# Dashboard Header

Example:

```markdown
# 🧠 DSA Progress Dashboard

**Current Focus:** Graphs  
**Study Day:** 12  
**Current Streak:** 🔥 8 days  
**Unique Problems:** 31  
**Total Attempts:** 46

Last Updated: 2026-09-13
```

---

# Main Progress Cards

Show:

```markdown
## 📊 Overall Progress

| Metric | Value |
|---|---:|
| Unique Problems | 31 |
| Total Attempts | 46 |
| Independent First Solves | 11 |
| Current Independent Problems | 20 |
| Revision Attempts | 15 |
| Patterns Encountered | 8 |
```

---

# Grade Distribution

Display both first attempt and current mastery.

Example:

```markdown
## 🎯 Grade Distribution

### First Attempts

A ███████░░░░░░░ 11
B █████░░░░░░░░░ 7
C ██████░░░░░░░░ 9
D ███░░░░░░░░░░░ 4

### Current

A █████████████░░ 20
B █████░░░░░░░░░ 7
C ███░░░░░░░░░░░ 3
D █░░░░░░░░░░░░░ 1
```

Bars should be proportionally generated from actual data.

---

# Independence Metrics

Track BOTH metrics.

## First-Attempt Independent Rate

```text
Problems first solved at A
÷
unique problems
```

Measures raw unseen problem-solving ability.

## Current Independent Rate

```text
Problems currently at A
÷
unique problems
```

Measures learned mastery.

Show both visually.

Example:

```markdown
## 🚀 Independence

First-Attempt Independence

███████░░░░░░░ 35%

Current Mastery

█████████████░░ 65%

Improvement: +30 percentage points
```

The difference between these two numbers is an important learning metric.

---

# Grade Conversion Statistics

Track how problems improve.

Example:

```markdown
## 📈 Learning Conversions

C → A: 7 problems
D → A: 3 problems
B → A: 5 problems
C → B: 4 problems
Regressions: 1
```

Highlight meaningful conversions.

Especially:

* D → A
* C → A

These are major milestones.

---

# Topic Strength

Calculate topic-level statistics.

Example:

```markdown
## 🗺️ Topic Strength

| Topic | Problems | Current A | Mastery |
|---|---:|---:|---:|
| Hashing | 6 | 5 | 83% |
| Recursion | 5 | 3 | 60% |
| Graph Traversal | 8 | 4 | 50% |
| DP | 3 | 1 | 33% |
```

Optionally render bars:

```text
Hashing         ████████████░░ 83%
Recursion       █████████░░░░░ 60%
Graphs          ███████░░░░░░░ 50%
DP              █████░░░░░░░░░ 33%
```

Do not label a topic "strong" with very little evidence.

---

# Pattern Coverage

Show encountered patterns.

Example:

```markdown
## 🧩 Pattern Library

✅ Hashing
✅ Two Pointers
✅ DFS
✅ BFS
🟡 Connected Components
🟡 Cycle Detection
⬜ Topological Sort
⬜ Dijkstra
⬜ Dynamic Programming
```

Use:

✅ = current confidence/mastery is strong
🟡 = learned but still needs revision
🔴 = currently weak
⬜ = planned but not yet studied

Only show future/planned patterns if present in repository configuration or study plan.

Do not invent curriculum items.

---

# Revision Dashboard

Show what's due.

Example:

```markdown
## 🔁 Revision Queue

### Due Today

- Two Sum — current B
- Number of Islands — current C

### Upcoming

| Date | Problems |
|---|---|
| Sep 14 | Flood Fill |
| Sep 16 | Contains Duplicate |
| Sep 17 | Number of Provinces |
```

Also show:

```text
Due today: 2
Overdue: 1
Upcoming 7 days: 6
```

Overdue revisions should be visible but not framed negatively.

---

# Consistency / Streak

Track DSA sessions by date.

Example:

```markdown
## 🔥 Consistency

Current streak: 8 days
Longest streak: 11 days
Sessions this month: 12 / 13 days
Completion rate: 92%

Sep

01 🟩
02 🟩
03 🟩
04 🟩
05 ⬜
06 🟩
07 🟩
08 🟩
09 🟩
10 🟩
11 🟩
12 🟩
13 🟩
```

Use:

🟩 = completed DSA session
⬜ = no recorded session

Do not infer laziness or failure from missed days.

---

# Daily Activity

Show recent work.

Example:

```markdown
## 🗓️ Recent Sessions

| Date | Topic | New | Revision | Result |
|---|---|---:|---:|---|
| Sep 13 | Graphs | 2 | 1 | A, B, A |
| Sep 12 | Graphs | 1 | 2 | C, A, A |
| Sep 11 | Grid BFS | 2 | 0 | B, C |
```

Limit this section to recent sessions.

Do not make the dashboard enormous.

---

# Difficulty Statistics

If difficulty metadata is reliably known:

```markdown
## 🧱 Difficulty

Easy:   ████████████ 18
Medium: █████████░░░ 12
Hard:   █░░░░░░░░░░ 1
```

Also show independent rate by difficulty when enough data exists.

Example:

```text
Easy independent rate: 61%
Medium independent rate: 25%
```

Do not overinterpret tiny sample sizes.

---

# Attempt Efficiency

Track:

```text
average attempts before reaching A
```

Example:

```markdown
## ⚙️ Learning Efficiency

Average attempts to reach A: 1.8

Hashing: 1.4
Graphs: 2.2
DP: 2.7
```

This can reveal where more repetition is needed.

Only show when sufficient data exists.

---

# Improvement Trend

Track independent performance over time.

For example weekly:

```markdown
## 📈 Weekly Trend

Week 1   █████░░░░░ 30%
Week 2   ███████░░░ 43%
Week 3   █████████░ 56%
```

Use first-attempt grades for measuring raw problem-solving improvement.

Do NOT use current grades for this trend.

---

# Personal Weaknesses

Extract a tiny summary from `LEARNINGS.md`.

Example:

```markdown
## ⚠️ Current Friction Points

1. HashMap key/value choice
2. Recognizing BFS vs DFS
3. Coding visited-state logic
```

Maximum 3–5 items.

Do not clutter this section.

---

# Wins

Generate a small motivational section based entirely on actual history.

Example:

```markdown
## 🏆 Recent Wins

- Two Sum: C → A
- First Graph problem solved independently
- 10-problem milestone reached
- 7-day DSA streak
- First Medium solved at A
```

Only show genuine milestones.

Do not fabricate encouragement.

---

# Milestones

Automatically detect milestones such as:

```text
First independent solve
10 unique problems
25 unique problems
50 unique problems
100 unique problems

First Medium A
First Graph A
First DP A

First D → A conversion
5 C/D → A conversions

7-day streak
14-day streak
30-day streak

50% first-attempt independent rate
60%
70%
80%
```

Store achieved milestones in history so they are not repeatedly treated as new.

---

# Mermaid Visuals

When useful, include lightweight Mermaid charts supported by Markdown renderers.

Example learning progression:

```mermaid
flowchart LR
    D[D - Needed Solution]
    C[C - Needed Hint]
    B[B - Implementation Issues]
    A[A - Independent]

    D --> C
    C --> B
    B --> A
```

Do not generate complex diagrams merely for decoration.

---

# Optional Topic Radar Substitute

Because standard Markdown does not support radar charts reliably, use bars instead.

Example:

```text
Hashing       ████████████░ 85%
Recursion     █████████░░░░ 65%
DFS/BFS       ████████░░░░░ 58%
Graphs        ██████░░░░░░░ 43%
DP            ███░░░░░░░░░ 20%
```

Prefer portable visuals over dependencies.

---

# Dashboard Philosophy

The dashboard should reward:

* consistency
* learning
* revisiting weak problems
* moving C/D problems toward A
* improved first-attempt independence

Do NOT optimize motivation around:

* raw problem count alone
* artificially maintaining streaks
* never getting D grades
* avoiding difficult problems

A D → A should be treated as a bigger learning win than another trivial A.

---

# README.md

Keep README lightweight.

It should contain:

```markdown
# DSA Training

Personal DSA learning repository.

Current Focus: Graphs

Problems: 31
First-Attempt Independence: 35%
Current Mastery: 65%

→ See [DASHBOARD.md](DASHBOARD.md) for full progress statistics.
→ See [PATTERNS.md](PATTERNS.md) for pattern recognition notes.
→ See [LEARNINGS.md](LEARNINGS.md) for personal mistakes and breakthroughs.
```

Do not duplicate the entire dashboard inside README.

---

# Statistics

All statistics MUST be calculated from `.dsa/history.json`.

Never manually estimate.

Maintain at minimum:

* unique problems
* total attempts
* revision attempts
* A/B/C/D first-attempt counts
* A/B/C/D current counts
* first-attempt independent rate
* current independent rate
* grade conversions
* sessions completed
* current streak
* longest streak
* topic-level mastery
* pattern counts
* revisions due
* overdue revisions

Optional when enough data exists:

* average attempts to A
* independent rate by difficulty
* weekly improvement rate
* topic improvement rate

---

# Session Records

Store one session per date.

Example:

```json
{
  "date": "2026-09-02",
  "day": 1,
  "topic": "Hashing",
  "new_problems": 2,
  "revision_problems": 0,
  "problems": [
    "contains-duplicate",
    "two-sum"
  ]
}
```

If the skill runs again on the same day, UPDATE the session.

Do not create duplicates.

---

# Repository Organization

Prefer:

```text
dsa-training/
├── README.md
├── DASHBOARD.md
├── PATTERNS.md
├── LEARNINGS.md
│
├── problems/
│   ├── arrays-hashing/
│   ├── recursion/
│   ├── trees/
│   ├── graphs/
│   ├── dynamic-programming/
│   ├── binary-search/
│   ├── sliding-window/
│   ├── two-pointers/
│   └── other/
│
└── .dsa/
    └── history.json
```

Do not over-nest directories.

---

# Handling Ambiguity

Be conservative.

If the student says:

> Eventually got it.

Do not assume A.

If grade cannot be confidently determined:

* choose the more conservative grade
* record uncertainty briefly if useful

Do not interrupt the workflow for minor missing metadata.

---

# Processing Workflow

Follow this sequence every time.

## Step 1 — Inspect

Read:

* Git status
* new/modified code
* transcript
* history
* existing patterns
* existing learnings
* dashboard

## Step 2 — Identify Session

Determine:

* session date
* primary topic
* new problems
* revision problems

## Step 3 — Grade

Assign grades using only demonstrated attempt information.

## Step 4 — Update Solution Headers

Never modify actual algorithm unless asked.

## Step 5 — Update History

Update `.dsa/history.json`.

Preserve history.

## Step 6 — Schedule Revisions

Apply revision rules.

## Step 7 — Update Patterns

Only meaningful pattern changes.

## Step 8 — Update Learnings

Only meaningful personal insights/mistakes.

## Step 9 — Recalculate Statistics

Calculate everything from history.

## Step 10 — Regenerate Dashboard

Update every relevant dashboard visualization and statistic.

Do not leave stale numbers.

## Step 11 — Update README

Update lightweight summary only.

## Step 12 — Validate

Perform validation checklist.

## Step 13 — Inspect Git Diff

Ensure changes are clean.

## Step 14 — Commit

Create one logical session commit.

---

# Validation Checklist

Before committing verify:

## Learning Integrity

* no inflated grades
* first-attempt grades preserved
* no invented understanding
* no hidden confusion
* no unsupported pattern knowledge

## Data Integrity

* JSON valid
* no duplicate problems
* no duplicate sessions
* revision dates valid
* all statistics recomputed
* dashboard numbers match history
* README numbers match history

## Code Integrity

* student algorithm unchanged unless explicitly requested
* no unrelated changes
* no temp files
* no audio files committed unless requested
* no raw transcript committed unless requested

## Dashboard Integrity

* no stale statistics
* progress bars proportional
* percentages mathematically correct
* streak based on session history
* topic metrics based on actual problems
* milestone claims supported by history
* revision queue matches dates

## Git Integrity

Inspect:

```bash
git status
git diff
```

Stage only relevant DSA changes.

---

# Git

Create one commit for each daily DSA session.

Format:

```text
day XX: <primary topic> - <short description>
```

Examples:

```text
day 01: hashing - two sum and contains duplicate
day 08: graphs - connected components
day 09: graphs - grid traversal
day 22: dp - memoization fundamentals
```

Revision-only example:

```text
day 12: revision - hashing and graph traversal
```

One session = one commit.

Do not create separate commits for dashboard/history/notes.

---

# Push Policy

Default:

COMMIT BUT DO NOT PUSH.

Only push when explicitly requested or repository configuration explicitly enables auto-push.

Never:

* force push
* rewrite Git history
* amend previous learning history without explicit instruction

---

# Final Session Output

After processing, respond concisely.

Example:

```text
DSA session processed.

New:
- Contains Duplicate — A
- Two Sum — C

Progress:
- Problems: 2
- First-attempt independence: 50%
- Current mastery: 50%
- Streak: 1 day

Revision:
- Contains Duplicate — Sep 4
- Two Sum — Sep 4

Dashboard:
- Updated

Commit:
day 01: hashing - two sum and contains duplicate

Push:
not performed
```

---

# Never Do

Never:

* solve a new DSA problem during logging
* silently fix code
* replace the student's solution
* inflate grades
* rewrite historical grades
* fabricate understanding
* create verbose textbook notes
* duplicate patterns
* delete attempts
* hide regressions
* fabricate dashboard statistics
* optimize solely for number of problems
* commit unrelated files
* commit secrets
* commit raw voice recordings by default
* force push

---

# Success Metrics

The repository should make four types of improvement visible.

## 1. Recognition

Can the student identify the correct problem family or pattern?

## 2. Reconstruction

Can previously learned problems be solved again without old code?

## 3. Independence

Does the first-attempt A rate improve over time?

## 4. Mastery

Do problems move through meaningful transitions?

Examples:

```text
D → C → B → A
C → B → A
C → A
B → A
```

A D or C is not failure.

A D → A conversion is strong evidence of learning.

---

# Final Operating Principle

Optimize for:

**Solve → Reflect → Record → Visualize → Revisit → Improve**

The dashboard should make progress satisfying to look at.

The repository should make revision easy.

The statistics should make improvement measurable.

But the system must never become more important than solving DSA itself.
