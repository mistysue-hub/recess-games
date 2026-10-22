UPDATE 19 Oct 2026 (Susie): Final exam Parts 1 and 3 (M16 Q1-Q2, M18 Q4) are optional; the learner can tell Rocky "skip". Takes Game Theory 3B first.

# Game Theory 4: Play It Again (draft course map)

Segment GameTh4. Folder t4/. Results code GT4-M##. Grades 10-12. Retro arcade look. Take Game Theory 3 first.
Yale ECON 159 (Ben Polak, Fall 2007), Lectures 21-24, Problem Set 10, Practice Problems on Asymmetric Information, and the Final Exam.
20 modules (more than 8 because each lecture over 30 minutes is split into parts of 40 minutes or less, and Yale's problem set, practice set and final are boss modules).

| Module | Yale source | Contents | Minutes |
|---|---|---|---|
| M01 | Lecture 21, Part 1 | Last Round game + clip 0:00-22:44 (class Prisoner's Dilemma, unraveling, lame duck) | 33 |
| M02 | Lecture 21, Part 2 | bet + clip 22:44-53:15 (two-round rewards, renegotiation, bankruptcy) + rematch | 37 |
| M03 | Lecture 22, Part 1 | Strategy Tournament + clip Lecture 21 53:15-end (coin-toss ending, Grim Trigger) | about 29 |
| M04 | Lecture 22, Part 2 | bet + clip 0:00-29:21 (Grim Trigger needs a 1/3 chance) + rematch | 35 |
| M05 | Lecture 22, Part 3 | bet + clip 29:21-53:09 (examples; one-period punishment) + rematch | 30 |
| M06 | Lecture 22, Part 4 | bet + clip 53:09-end (outsourcing to Freedonia; conclusions) + rematch | about 32 |
| M07 | BOSS Problem Set 10, Part 1 (The Cartel) | Q1 a-d, Q2 a-c | 35 |
| M08 | BOSS Problem Set 10, Part 2 | Q3, Q4 a-b (4c optional) | 35 |
| M09 | Lecture 23, Part 1 | Hiring Desk + clip 35:07-59:36 (good and bad workers, MBA signal) | 35 |
| M10 | Lecture 23, Part 2 | bet + clip 59:36-end (conclusions) + rematch | about 20 |
| M11 | Lecture 23, Part 3 | bet + clip 0:00-35:07 (unraveling and examples; rewind) + rematch | 39 |
| M12 | Lecture 24, Part 1 | Jar of Coins + clip 0:00-21:40 (common values, jar auction, winner's curse) | about 32 |
| M13 | Lecture 24, Part 2 | bet + clip 21:40-42:38 (correcting for the curse, second jar) + rematch | 27 |
| M14 | Lecture 24, Part 3 | bet + clip 42:38-end (four auction types, revenue) + rematch | about 26 |
| M15 | BOSS Practice Problems on Asymmetric Information (The Informant) | 4 problems | 35 |
| M16 | BOSS Final, Part 1 (The Final Boss) | Q1 a-d + Q2 a-b (35 points); optional clips Lecture 14 49:25-55:53, Lecture 16 34:04-45:42 | 35 |
| M17 | BOSS Final, Part 2 | Q3 a-e (40 points) | 40 |
| M18 | BOSS Final, Part 3 | Q4 a-b (30 points) | 30 |
| M19 | BOSS Final, Part 4 | Q5 a-d (27 points) | 27 |
| M20 | BOSS Final, Part 5 | Q5 e-f (18 points) | 18 |

Video IDs: L21 zNxVVVk5It0, L22 NBKr-wK-TEQ, L23 RWxTJsTbK2w, L24 pJAhnc8VuDo. Optional: L14 aIq0E3OmNz4, L16 SE7kP7XZuV4.

## Boss sources
- Problem Set 10 (due 5 Dec 2007, on the Lecture 22 page): https://oyc.yale.edu/sites/default/files/problemset10_0_0.pdf (4 questions). Placed after Lecture 22. Q1 uses Template 3 ideas (subgame perfection with investment).
- Practice Problems on Asymmetric Information (Lecture 24 page): https://oyc.yale.edu/sites/default/files/practice_problems_on_asymmetric_information_0.pdf (4 problems). Placed after Lecture 24.
- Final Exam 2007: https://oyc.yale.edu/sites/default/files/final_exam_2007_0.pdf (5 questions, 150 points, 150 minutes plus 30 reading). Split about 1 point = 1 minute. Yale's "Concepts since Midterm" sheet says it covers the second half of the course (Templates 3 and 4), so Q1a, Q1c, Q2 and Q4 lean on Template 3.
- Yale posts solutions for the final and the practice problems. Following the midterm decision, Rocky checks reasoning only and uses no key.
- No problem set was found on the Lecture 21, 23 or 24 pages.

## Games (all tested in node)
- t4-m01-last-round.html (GT4-M01): Polak's payoffs (2,2 / -1,3 / 3,-1 / 0,0). Match 1: 5 known rounds vs Mira (copies you, always cheats in round 5). Match 2: coin-toss ending (3 in 4 to continue, at least 3 rounds) vs Dex (Grim Trigger).
- t4-m03-strategy-tournament.html (GT4-M03): 5 robots round-robin with continuation 20%, 60%, 90% (expected points, exact). Winners: SHARK at 20%; COPYCAT and GRUDGE tie at 60% and 90%.
- t4-m09-hiring-desk.html (GT4-M09): Polak's signaling numbers (50/30, MBA cost 5 vs 10.01). 1 year fools you; 2 years sorts with least school; 4 years Gus exactly even; 5 years nobody signals.
- t4-m12-jar-of-coins.html (GT4-M12): common-value jar auction, guesses within 12 of the truth, 5 rivals (two bid their guess, others shade 3, 6, 10). Naive winners overpay about 9 times in 10 in simulation.

## Cut points and lengths to confirm by watching
- Lecture lengths not confirmed (VideoLectures.net and YouTube blocked from here). Clips that run "to the end": L21 from 53:15 (M03), L22 from 53:09 (M06), L23 from 59:36 (M10), L24 from 42:38 (M14). Minutes for those are estimates.
- L24 cut at 21:40 (1300 s) is inside a chapter, estimated from the transcript line about how to correct for the winner's curse.

## Open questions for Susie
- Final exam is 5 boss modules (150 points). Fine, or trim to the questions Template 4 teaches (Q3 and Q5) and make Q1, Q2, Q4 optional?
- Use Yale's posted keys for the final and practice problems, or keep reasoning-only like the midterm?
- Card headings are "GAME: <name>" without a number, since Template 3's game count isn't known yet.
