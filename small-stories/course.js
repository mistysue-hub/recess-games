// Small Stories, Big Moves — shared course data for the hosted pages.
// One entry per week (Recess module). Used by index.html, desk.html, notebook.html, journal.html, portfolio.html.
// Weeks 4–33 carry titles, blocks and MIT mapping now; their desk tasks are added as those weeks are built.
window.SSBM = (function () {
  const BLOCKS = {
    t1: "Toolkit I", s1: "Story 1", w1: "Workshop 1", r1: "Revise Story 1",
    t2: "Toolkit II", s2: "Story 2", w2: "Workshop 2", r2: "Revise Story 2",
    s3: "Story 3", life: "The Life of the Writer", port: "Portfolio"
  };
  // MIT assignment numbers follow the course plan: 1 reading & analysis, 2 character exercises, 3 POV exercises,
  // 4 writing journal, 5 story 1, 6 story 2, 7 critiques, 8 revise story 1, 9 story 3, 10 revise story 2, 11 portfolio.
  const W = [
    {n:1,  block:"t1", title:"Want and Obstacle", story:"Chekhov, The Lottery Ticket", mit:"Read published stories and analyze craft; character exercises (1, 2, 4)", you:"Reading notebook on the story; a 100–150 word want-and-wall piece", mins:"2 sittings, about 75 min",
      notebook:true, words:[100,150],
      task:["Write 100 to 150 words. Somebody wants one concrete thing. Say the want in your first two sentences, as a positive. Put something in the way. Stop before we know whether they get it. No ending, no moral."],
      checks:[{id:"want",text:"The want is named in my first two sentences, as a positive (\"she wants…\")."},
              {id:"wall",text:"Something stands in the way, and I named it."},
              {id:"stop",text:"I stopped before we find out if they get it."}]},
    {n:2,  block:"t1", title:"The Sort of Person Who", story:"Mansfield, Miss Brill", mit:"Character exercises: practice characterization (1, 2, 4)", you:"Reading notebook; a 120–180 word character built from one object and one habit", mins:"2 sittings, about 75 min",
      notebook:true, words:[120,180],
      task:["Write 120 to 180 words that introduce one person through two things only: one object they own and one habit they have. No list of personality words. End with your own \"sort of person who…\" sentence, finished with a habit."],
      checks:[{id:"obj",text:"One object the person owns is in the draft."},
              {id:"habit",text:"One habit they have is shown, not stated."},
              {id:"nolist",text:"No personality words (kind, funny, brave…) describe them directly."},
              {id:"sort",text:"It ends with a \"sort of person who…\" sentence, finished with a habit."}]},
    {n:3,  block:"t1", title:"The Now Moment", story:"Chopin, The Story of an Hour", mit:"Read and analyze: the moment of change; exercise journal (1, 4)", you:"Reading notebook; a 150–200 word before / turn / after built on a feeling you've had", mins:"2 sittings, about 70 min",
      notebook:true, words:[150,200],
      task:["First line: one word, a feeling you have actually had.","Then 150 to 200 words with a before, a turn, and an after. The turn is one sentence, on its own line. The situation can be invented; the feeling can't."],
      checks:[{id:"feel",text:"One feeling-word is on the first line, and that word doesn't appear in the body."},
              {id:"turn",text:"The turn is a single sentence on its own line."},
              {id:"ba",text:"There is text before the turn and text after it."}]},
    {n:4,  block:"t1", title:"Seeds: Emotional Truth", story:"Chekhov, Misery", mit:"Exercise in developing story from incident and life (1, 4)", you:"Reading notebook; a memory sketch, then the same sketch with one thing changed", mins:"2 sittings, about 75 min", notebook:true},
    {n:5,  block:"t1", title:"Two Wants in One Room", story:"Saki, The Open Window", mit:"Plot: what the character wants, what stands in the way (1, 2, 4)", you:"Reading notebook; a 150–200 word scene with two opposed wants", mins:"2 sittings, about 75 min", notebook:true},
    {n:6,  block:"t1", title:"Whose Eyes?", story:"Poe, The Tell-Tale Heart", mit:"Point-of-view exercises (1, 3, 4)", you:"Reading notebook; the Week 5 scene retold as \"I\" by the other person", mins:"2 sittings, about 75 min", notebook:true},
    {n:7,  block:"t1", title:"Count the Cold", story:"London, To Build a Fire (first half)", mit:"Description as a central element; the five senses (1, 4)", you:"Reading notebook; a 150–200 word place through what a body notices", mins:"2 sittings, about 80 min", notebook:true},
    {n:8,  block:"t1", title:"Feeding the Reader", story:"Poe, The Cask of Amontillado", mit:"The forms and methods of revelation: pacing information (1, 4)", you:"Reading notebook; a 200-word scene that plants one thing and pays it off", mins:"2 sittings, about 75 min", notebook:true},
    {n:9,  block:"t1", title:"Where to Start", story:"O. Henry, The Gift of the Magi", mit:"Making the decision where to begin (1, 4)", you:"Reading notebook; the same opening three ways, one chosen", mins:"2 sittings, about 70 min", notebook:true},
    {n:10, block:"t1", title:"Meeting to Parting", story:"Chekhov, The Bet", mit:"Point of view and the scene as a unit; 3 × 200-word exercise (3, 4)", you:"Reading notebook; one scene in two viewpoints, 200 words each", mins:"2 sittings, about 80 min", notebook:true},
    {n:11, block:"s1", title:"Story 1: Seeds and Plan", story:"", mit:"Short Story 1, first draft begun (5)", you:"The six questions answered for your own story; the first 300 words", mins:"2 sittings, about 90 min"},
    {n:12, block:"s1", title:"Story 1: The Middle", story:"", mit:"Short Story 1 in progress (5)", you:"Draft to about 700 words", mins:"2 sittings, about 90 min"},
    {n:13, block:"s1", title:"Story 1: To the End", story:"", mit:"Short Story 1 complete, 800–1,500 words (5)", you:"A finished first draft", mins:"2 sittings, about 90 min"},
    {n:14, block:"w1", title:"Workshop 1", story:"Two course sample stories", mit:"Prepare written critiques for workshop stories (7)", you:"Two written critiques; your story at the reading table", mins:"2 sittings, about 90 min"},
    {n:15, block:"r1", title:"Revise Story 1: Red Lines", story:"", mit:"Substantial rewrite of Story 1 (8)", you:"Chosen notes; the three rewrite moves applied", mins:"2 sittings, about 90 min"},
    {n:16, block:"r1", title:"Revise Story 1: Passes", story:"", mit:"Substantial rewrite of Story 1, submitted (8)", you:"Two focused passes; the revised story with a header note", mins:"2 sittings, about 90 min"},
    {n:17, block:"t2", title:"Every Story Has an Address", story:"Chekhov, Vanka", mit:"Place as both reality and metaphor (1, 4)", you:"Reading notebook; a 150–220 word letter from a place you can't leave", mins:"2 sittings, about 75 min", notebook:true},
    {n:18, block:"t2", title:"One Impossible Thing", story:"Irving, Rip Van Winkle (excerpt)", mit:"The real as the basis for the unreal (1, 4)", you:"Reading notebook; 200 words of ordinary life after one changed rule", mins:"2 sittings, about 80 min", notebook:true},
    {n:19, block:"t2", title:"Voice Is Not the Camera", story:"Saki, The Storyteller", mit:"Description II: authorial voice vs point of view (1, 4)", you:"Reading notebook; the same paragraph in two voices", mins:"2 sittings, about 75 min", notebook:true},
    {n:20, block:"t2", title:"Landing One Beat Early", story:"O. Henry, The Last Leaf", mit:"Endings that feel earned; planting and payoff (1, 4)", you:"Reading notebook; a new last paragraph for Story 1 that stops earlier", mins:"2 sittings, about 70 min", notebook:true},
    {n:21, block:"s2", title:"Story 2: A Different Camera", story:"", mit:"Short Story 2 begun (6)", you:"A plan in a POV you haven't used; the first 400 words", mins:"2 sittings, about 90 min"},
    {n:22, block:"s2", title:"Story 2: The Middle", story:"", mit:"Short Story 2 in progress (6)", you:"Draft to about 1,000 words", mins:"2 sittings, about 90 min"},
    {n:23, block:"s2", title:"Story 2: To the End", story:"", mit:"Short Story 2 complete, 1,000–2,000 words (6)", you:"A finished first draft", mins:"2 sittings, about 90 min"},
    {n:24, block:"w2", title:"Workshop 2", story:"Two course sample stories", mit:"Written critiques (7)", you:"Two more critiques; Story 2 at the reading table", mins:"2 sittings, about 90 min"},
    {n:25, block:"r2", title:"Revise Story 2: Red Lines", story:"", mit:"Revise Story 2 (10)", you:"Chosen notes; the three rewrite moves applied", mins:"2 sittings, about 90 min"},
    {n:26, block:"r2", title:"Revise Story 2: Passes", story:"", mit:"Revised Story 2 submitted (10)", you:"Two focused passes; the revised story with a header note", mins:"2 sittings, about 90 min"},
    {n:27, block:"s3", title:"Story 3: The Outline", story:"", mit:"Short Story 3 planned (9)", you:"Seeds, the six questions, and a scene list for your most ambitious story", mins:"2 sittings, about 80 min"},
    {n:28, block:"s3", title:"Story 3: Opening Scenes", story:"", mit:"Short Story 3 in progress (9)", you:"The first 700 words", mins:"2 sittings, about 90 min"},
    {n:29, block:"s3", title:"Story 3: The Middle", story:"", mit:"Short Story 3 in progress (9)", you:"Draft to about 1,500 words", mins:"2 sittings, about 90 min"},
    {n:30, block:"s3", title:"Story 3: To the End", story:"", mit:"Short Story 3 complete, 1,500–2,500 words (9)", you:"A finished draft, with a self-review", mins:"2 sittings, about 90 min"},
    {n:31, block:"life", title:"The Life of the Writer", story:"", mit:"The way a professional writer works in the world", you:"A half-page writer's letter: your process, what blocks you, what you'd submit", mins:"2 sittings, about 70 min"},
    {n:32, block:"port", title:"Portfolio: Gather", story:"", mit:"Final portfolio: collect the semester's writing (11)", you:"Everything in one place: three stories, two revisions, journal, four critiques", mins:"2 sittings, about 80 min"},
    {n:33, block:"port", title:"Portfolio: Reflect", story:"", mit:"Final portfolio submitted (11)", you:"A reflection on your three stories; the finished portfolio downloaded", mins:"2 sittings, about 70 min"}
  ];
  const byN = {}; W.forEach(w => byN[w.n] = w);
  return { BLOCKS, WEEKS: W, week: n => byN[n], base: "https://mistysue-hub.github.io/recess-games/small-stories/" };
})();

// Copy helper: tries the clipboard, then a hidden-textarea copy, and always shows a selected text box as a last resort
// (some embedded panels block clipboard access).
window.SSBM.copyText = async function (text, statusEl) {
  let ok = false;
  try { await navigator.clipboard.writeText(text); ok = true; } catch (e) {}
  if (!ok) {
    try {
      const t = document.createElement("textarea");
      t.value = text; t.setAttribute("readonly", ""); t.style.cssText = "position:fixed;top:0;left:0;opacity:0";
      document.body.appendChild(t); t.focus(); t.select(); t.setSelectionRange(0, text.length);
      ok = document.execCommand("copy") === true; t.remove();
    } catch (e) {}
  }
  let box = document.getElementById("ssbm-copybox");
  if (!box) {
    box = document.createElement("div"); box.id = "ssbm-copybox";
    box.style.cssText = "margin:14px 0;padding:12px;background:#f6e9a6;border:1px solid #c9b45a;border-radius:4px";
    box.innerHTML = '<p style="margin:0 0 8px;font-family:Courier Prime,monospace" id="ssbm-copymsg"></p><textarea readonly id="ssbm-copyta" style="width:100%;height:160px;font:14px Courier Prime,monospace;box-sizing:border-box"></textarea>';
    (statusEl && statusEl.parentNode ? statusEl.parentNode : document.body).appendChild(box);
  }
  const ta = document.getElementById("ssbm-copyta"); ta.value = text;
  document.getElementById("ssbm-copymsg").textContent = ok
    ? "Copied. If pasting into Rocky shows nothing, copy from this box instead:"
    : "Copy didn't work here. Select the text in the box, copy it (Ctrl+C, or Cmd+C on a Mac), then paste it into your chat with Rocky:";
  box.style.display = "block"; ta.focus(); ta.select();
  if (statusEl) statusEl.textContent = ok ? "Copied. Now paste it to Rocky." : "Copy didn't work here. Copy the text from the box below.";
  return ok;
};
