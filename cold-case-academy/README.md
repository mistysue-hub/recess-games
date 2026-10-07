# Cold Case Academy

A Recess course on real heists, escapes and disappearances from history, for ages 10–13.

## Play
- **The Missing Smile** (M01 training case, the 1911 Mona Lisa theft):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/the-missing-smile/

- **Flight 305** (M02, D.B. Cooper Part 1):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/flight-305/
- **The Tena Bar Riddle** (M03, D.B. Cooper Part 2):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/tena-bar-riddle/
- **Count at Dawn** (M04, Alcatraz Part 1):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/count-at-dawn/
- **The Marshals' File** (M05, Alcatraz Part 2):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/marshals-file/

- **The Sensor Log** (M06, Gardner heist Part 1):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/sensor-log/
- **Frame by Frame** (M07, Gardner heist Part 2):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/frame-by-frame/
- **The Tower Ledger** (M08, Princes in the Tower, optional):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/tower-ledger/
- **The Apollo Gallery** (M09, the 2025 Louvre crown-jewels theft):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/apollo-gallery/
- **The Final Report** (M10, capstone report builder; works for any of the five cases):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/final-report/

Evidence locker: Part 1 of each case saves the player's notebook in the browser, and Part 2 reads it (same device, same browser). If storage is blocked, Part 2 still works on its own.

## Folders
- `the-missing-smile/`: the playable game (`index.html`), its Twine source (`source/the-missing-smile.twee`, import into Twine 2), a cover image, and screenshots of the finish screens used as Recess completion references (`reference/`).
- `flight-305/`, `tena-bar-riddle/`, `count-at-dawn/`, `marshals-file/`: the same layout for the D.B. Cooper and Alcatraz games.
- `common-source/common.twee`: shared engine and styles for every game except The Missing Smile (compile each game's `.twee` together with this file).
- `course/recess-workspace/`: the files loaded into the Recess goal template (`AGENTS.md`, `first-message.md`, `modules/`, `resources/`).
- `course/course-outline.md`: the 10-module plan.
- `course/design-M02-M05.md`: designs and fact-check log for the D.B. Cooper and Alcatraz modules.
- `course/reading-list.md`: further reading for every module.
- `cover.png`: course cover image.

## Updating a game
- The Missing Smile: edit `the-missing-smile/source/the-missing-smile.twee` in Twine 2, publish to file, and replace `the-missing-smile/index.html`.
- The other games: import the game's `.twee` and `common-source/common.twee` into the same Twine 2 story (or compile both with Tweego), then replace the game's `index.html`.
