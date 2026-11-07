# IMAT Planners

Six offline study planners for IMAT: **Biology** (`src/planner.html`, green), **Chemistry** (`src/chemistry.html`, blue), **Physics** (`src/physics.html`, black), **Math** (`src/math.html`, white), **Logic** (`src/logic.html`, pink) and **Reading** (`src/reading.html`, red).

## Biology

A clean study planner for IMAT biology, from **8 Nov 2026** to **20 Mar 2027** (29 Esfand 1405, the day before Nowruz).

Open `index.html` in a browser. English only, with an iPhone-style font (San Francisco on Apple devices, Inter elsewhere).

## Weekly rhythm
| Day | Plan |
|---|---|
| Sat – Tue | Study this week's chapter (one chapter per week, in 4 parts) |
| Wed | Rest / catch up |
| Thu | Timed cumulative test of every chapter studied so far |
| Fri | Active recall of the week + write mistakes in the notebook |

19 chapters over 19 weeks, then a final full-course review day on 20 March.

## Features
- **Today**: tasks for the day with checkboxes, week strip, test score entry on Thursdays
- **Schedule**: every week and day, with progress and missed days
- **Tests**: score table and trend chart
- **Mistake notebook**: log mistakes by chapter, mark them resolved
- **Chapters**: rename chapters to match your textbook

Progress is saved in the browser (or to your account when opened as a Claude artifact).
`src/planner.html` is the source; `index.html` wraps it as a standalone page.

## Chemistry
Two chapters a week, 38 chapters, same dates (8 Nov 2026 → 20 Mar 2027).

| Day | Plan |
|---|---|
| Sat – Sun | First chapter of the week (2 parts) |
| Mon | Rest |
| Tue – Wed | Second chapter of the week (2 parts) |
| Thu | Timed cumulative test of every chapter studied so far |
| Fri | Active recall of the week + write mistakes in the notebook |

Week 1 starts on Sunday: Sunday covers chapter 1, Tue–Wed chapter 2. The chemistry app uses a blue theme.

## Physics
Two chapters a week, 38 chapters, same dates. Black theme.

| Day | Plan |
|---|---|
| Sat | Rest |
| Sun – Mon | First chapter of the week (2 parts) |
| Tue – Wed | Second chapter of the week (2 parts) |
| Thu | Timed cumulative test of every chapter studied so far |
| Fri | Active recall of the week + write mistakes in the notebook |

## Math
One chapter a week, 19 chapters, same dates. Always white (also in dark mode).

| Day | Plan |
|---|---|
| Sat, Mon, Wed | Study this week's chapter (3 parts) |
| Sun, Tue | Rest |
| Thu | Timed cumulative test of every chapter studied so far |
| Fri | Active recall of the week + write mistakes in the notebook |

Week 1 starts on Sunday, so its chapter is covered on Monday and Wednesday.

## Logic
One chapter every two weeks, 10 chapters, same dates. Pink theme.

| Day | Plan |
|---|---|
| Sat, Mon, Wed | Study the current chapter (6 parts over two weeks) |
| Sun, Tue | Rest |
| Thu | Timed cumulative test of every chapter studied so far |
| Fri | Active recall + write mistakes in the notebook |

Chapter 1 has 5 parts (week 1 starts on Sunday); chapter 10 gets the last single week (3 parts).

## Reading
Red theme. Three reading days a week, the other days are free.

| Day | Plan |
|---|---|
| Sun | Read one 600–800-word article (BBC Future, Scientific American, The Guardian); from memory write the main idea in one sentence and the author's view (for / against / neutral); add new words to the vocabulary notebook |
| Tue | One reading passage with its questions (past IMAT first, then IELTS Academic Reading); after marking, find the sentence that proves each right answer |
| Thu | Review the week's words |

Instead of chapters it has a **Vocabulary** notebook (words by week, mark learned) and an **Articles** log (title, source, main idea, author's view). Tuesday tests record the source (IMAT / IELTS) and score.

## Android apps (offline)
- Biology: https://github.com/grandddlc-tech/Biology/releases/latest/download/BiologyPlanner.apk
- Chemistry: https://github.com/grandddlc-tech/Biology/releases/latest/download/ChemistryPlanner.apk
- Physics: https://github.com/grandddlc-tech/Biology/releases/latest/download/PhysicsPlanner.apk
- Math: https://github.com/grandddlc-tech/Biology/releases/latest/download/MathPlanner.apk
- Logic: https://github.com/grandddlc-tech/Biology/releases/latest/download/LogicPlanner.apk
- Reading: https://github.com/grandddlc-tech/Biology/releases/latest/download/ReadingPlanner.apk

Both come from one Android project (`android/`) as six product flavors (`bio`, `chem`, `phys`, `math`, `logic`, `reading`) and install side by side.

- Works fully offline: the page and fonts are bundled in the app, and it asks for no internet permission.
- Progress, test scores and the mistake notebook are saved on the phone.
- Every push that changes `src/`, `android/` or `scripts/` builds a new APK with GitHub Actions
  (`.github/workflows/android.yml`) and publishes all six APKs as the latest release.
- Signing: the key is never stored in the repo. Add two repository secrets, `KEYSTORE_BASE64` (a base64 `.jks` with alias `planner`)
  and `KEYSTORE_PASSWORD`, so every build is signed with the same key and updates install over the old version.
  Without them, CI signs each build with a one-off key, and installing a newer build needs an uninstall first (which clears saved progress).

Build locally: `python3 scripts/build_android_assets.py && cd android && KEYSTORE_PASSWORD=... ./gradlew assembleRelease`
(with your own keystore at `android/keystore/release.jks`).
