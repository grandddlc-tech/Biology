# IMAT Biology Planner

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

## Android app (offline)
Download the latest APK: https://github.com/grandddlc-tech/Biology/releases/latest/download/BiologyPlanner.apk

- Works fully offline: the page and fonts are bundled in the app, and it asks for no internet permission.
- Progress, test scores and the mistake notebook are saved on the phone.
- Every push that changes `src/`, `android/` or `scripts/` builds a new APK with GitHub Actions
  (`.github/workflows/android.yml`) and publishes it as the latest release.
- Signing: the key is never stored in the repo. Add two repository secrets, `KEYSTORE_BASE64` (a base64 `.jks` with alias `planner`)
  and `KEYSTORE_PASSWORD`, so every build is signed with the same key and updates install over the old version.
  Without them, CI signs each build with a one-off key, and installing a newer build needs an uninstall first (which clears saved progress).

Build locally: `python3 scripts/build_android_assets.py && cd android && KEYSTORE_PASSWORD=... ./gradlew assembleRelease`
(with your own keystore at `android/keystore/release.jks`).
