# Computer Care 101 Jr & Sr: source notes

The Python generators that built these games were lost with a cloud container in Nov 2026.
Each game's `index.html` embeds the whole story as JSON (`const STORY=...`) plus the player, so
edits are now made with `patch_story.py`, which rewrites passages in place and re-injects them.

Run: `python3 source/patch_story.py <path to index.html>` (it is safe to run twice).

Nov 24, 2026 patch: Jr Day 5 mini-game moved after the Trackballs lesson; mini-game misses now
tracked and reported in the "Copy my results for Rocky" line; the shift bar shows the Final Exam;
Jr exam Q6 says "grandson Ollie" instead of "little sister".
