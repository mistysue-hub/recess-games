# Cold Case Academy

A Recess course on real heists, escapes and disappearances from history, for ages 10–13.

## Play
- **The Missing Smile** (M01 training case, the 1911 Mona Lisa theft):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/the-missing-smile/

- **Flight 305** (M02, D.B. Cooper Part 1):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/flight-305/
- **The Tena Bar Riddle** (M03, D.B. Cooper Part 2):
  https://mistysue-hub.github.io/recess-games/cold-case-academy/tena-bar-riddle/

## Folders
- `the-missing-smile/`: the playable game (`index.html`), its Twine source (`source/the-missing-smile.twee`, import into Twine 2), a cover image, and screenshots of the finish screens used as Recess completion references (`reference/`).
- `flight-305/`, `tena-bar-riddle/`: the same layout for the D.B. Cooper games.
- `common-source/common.twee`: shared engine and styles for Flight 305 and The Tena Bar Riddle (compile each game's `.twee` together with this file).
- `course/recess-workspace/`: the files loaded into the Recess goal template (`AGENTS.md`, `first-message.md`, `modules/`, `resources/`).
- `course/course-outline.md`: the 10-module plan.
- `course/design-M02-M05.md`: designs and fact-check log for the D.B. Cooper and Alcatraz modules.
- `course/reading-list.md`: further reading for every module.
- `cover.png`: course cover image.

## Updating a game
- The Missing Smile: edit `the-missing-smile/source/the-missing-smile.twee` in Twine 2, publish to file, and replace `the-missing-smile/index.html`.
- Flight 305 and The Tena Bar Riddle: import the game's `.twee` and `common-source/common.twee` into the same Twine 2 story (or compile both with Tweego), then replace the game's `index.html`.
