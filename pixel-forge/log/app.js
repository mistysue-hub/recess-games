// Pixel Forge Build Log: Lua highlighting, copy buttons, step progress saved per build.
(function () {
  var KW = /\b(function|end|if|then|elseif|else|for|do|while|repeat|until|return|local|and|or|not|in|break|true|false|nil)\b/g;

  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  function highlight(src) {
    // Tokenise in one pass so strings/comments are never re-highlighted.
    var out = "", i = 0, n = src.length;
    while (i < n) {
      var c = src[i];
      if (c === "-" && src[i + 1] === "-") {            // comment to end of line
        var j = src.indexOf("\n", i); if (j < 0) j = n;
        out += '<span class="tok-cm">' + esc(src.slice(i, j)) + "</span>"; i = j; continue;
      }
      if (c === '"' || c === "'") {                     // string
        var q = c, j2 = i + 1;
        while (j2 < n && src[j2] !== q) { if (src[j2] === "\\") j2++; j2++; }
        out += '<span class="tok-str">' + esc(src.slice(i, j2 + 1)) + "</span>"; i = j2 + 1; continue;
      }
      if (/[A-Za-z_]/.test(c)) {                        // word
        var j3 = i; while (j3 < n && /[\w.:]/.test(src[j3])) j3++;
        var w = src.slice(i, j3);
        if (/^love\./.test(w)) out += '<span class="tok-love">' + esc(w) + "</span>";
        else if (/^(math|table|string)\./.test(w)) out += '<span class="tok-fn">' + esc(w) + "</span>";
        else {
          // split on dots/colons so keywords inside identifiers aren't matched
          out += esc(w).replace(KW, '<span class="tok-kw">$1</span>');
        }
        i = j3; continue;
      }
      if (/[0-9]/.test(c)) {
        var j4 = i; while (j4 < n && /[0-9.]/.test(src[j4])) j4++;
        out += '<span class="tok-num">' + src.slice(i, j4) + "</span>"; i = j4; continue;
      }
      out += esc(c); i++;
    }
    return out;
  }

  document.querySelectorAll("code.lua").forEach(function (el) {
    el.innerHTML = highlight(el.textContent);
  });

  document.querySelectorAll(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var code = btn.parentNode.querySelector("code").textContent;
      var flash = function (label, cls) { btn.textContent = label; if (cls) btn.classList.add(cls); setTimeout(function () { btn.textContent = "copy"; btn.classList.remove("ok"); btn.classList.remove("fail"); }, 1800); };
      var legacy = function () {
        var ok = false, t = document.createElement("textarea");
        t.value = code; t.setAttribute("readonly", ""); t.style.cssText = "position:fixed;top:0;left:0;opacity:0";
        document.body.appendChild(t); t.focus(); t.select();
        try { ok = document.execCommand("copy") === true; } catch (e) { ok = false; }
        t.remove();
        if (ok) flash("copied", "ok"); else flash("copy failed: select the code and copy it", "fail");
      };
      if (navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) {
        navigator.clipboard.writeText(code).then(function () { flash("copied", "ok"); }, legacy);
      } else legacy();
    });
  });

  // progress, saved per build in this browser only
  var build = document.body.getAttribute("data-build");
  if (!build) return;
  var key = "pixelforge:" + build;
  var state = {};
  try { state = JSON.parse(localStorage.getItem(key) || "{}"); } catch (e) { state = {}; }
  function save() { try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) {} }

  var stepBoxes = Array.prototype.slice.call(document.querySelectorAll("input[data-step]"));
  var shipBoxes = Array.prototype.slice.call(document.querySelectorAll("input[data-ship]"));
  var bar = document.querySelector(".bar i"), pct = document.querySelector(".pct");

  function paint() {
    var done = 0;
    stepBoxes.forEach(function (b) {
      var on = !!state["s" + b.dataset.step]; b.checked = on; if (on) done++;
      b.closest("li").classList.toggle("done", on);
    });
    shipBoxes.forEach(function (b) {
      var on = !!state["ship" + b.dataset.ship]; b.checked = on;
      b.closest("li").classList.toggle("done", on);
    });
    if (bar) bar.style.width = (stepBoxes.length ? (100 * done / stepBoxes.length) : 0) + "%";
    if (pct) pct.textContent = done + " of " + stepBoxes.length + " steps";
  }
  stepBoxes.forEach(function (b) {
    b.addEventListener("click", function (e) { e.stopPropagation(); });
    b.addEventListener("change", function () { state["s" + b.dataset.step] = b.checked; save(); paint(); });
  });
  shipBoxes.forEach(function (b) {
    b.addEventListener("change", function () { state["ship" + b.dataset.ship] = b.checked; save(); paint(); });
  });
  paint();

  // ---- Ship-It Check: answers checked on this page; a finish screen is the proof ----
  var check = document.getElementById("check");
  if (!check) return;
  var answers = window.PF_ANSWERS || {};
  var dev = document.getElementById("devname");
  try { dev.value = localStorage.getItem("pixelforge:dev") || ""; } catch (e) {}
  dev.addEventListener("input", function () { try { localStorage.setItem("pixelforge:dev", dev.value); } catch (e) {} });

  var ck = state.check || (state.check = {});
  // restore
  check.querySelectorAll("fieldset.q").forEach(function (fs) {
    var v = ck[fs.dataset.q]; if (v != null) { var r = fs.querySelector('input[value="' + v + '"]'); if (r) r.checked = true; }
    fs.addEventListener("change", function () { ck[fs.dataset.q] = fs.querySelector("input:checked").value; fs.querySelector(".verdict").textContent = ""; fs.classList.remove("bad", "good"); save(); });
  });
  check.querySelectorAll(".task").forEach(function (t) {
    var ta = t.querySelector("textarea"); ta.value = ck["t_" + t.dataset.task] || "";
    ta.addEventListener("input", function () { ck["t_" + t.dataset.task] = ta.value; t.querySelector(".verdict").textContent = ""; t.classList.remove("bad", "good"); save(); });
  });
  var ran = document.getElementById("ran"); ran.checked = !!ck.ran;
  ran.addEventListener("change", function () { ck.ran = ran.checked; save(); });

  function hash(str) { var h = 5381; for (var i = 0; i < str.length; i++) h = ((h << 5) + h + str.charCodeAt(i)) >>> 0; return h; }
  function shipCode(name, date) {
    var h = hash(build + "|" + name.trim().toLowerCase() + "|" + date), A = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789", out = "";
    for (var i = 0; i < 4; i++) { out += A[h % A.length]; h = Math.floor(h / A.length); }
    return "PF-" + build.replace("build", "") + "-" + out;
  }
  function looksLikeCode(s) { return /\b(function|if|for|while|local|end|then|do)\b/.test(s) || /=/.test(s); }
  function hasAny(s, groups) {
    for (var g = 0; g < groups.length; g++) {
      var ok = false; for (var k = 0; k < groups[g].length; k++) if (s.indexOf(groups[g][k]) >= 0) ok = true;
      if (!ok) return groups[g];
    }
    return null;
  }

  function showFinish() {
    var f = document.getElementById("finish"), sh = ck.shipped;
    document.getElementById("fwho").textContent = sh.name;
    document.getElementById("fwhen").textContent = sh.date;
    document.getElementById("fcode").textContent = sh.code;
    f.hidden = false; document.body.classList.add("finished"); window.scrollTo(0, 0);
  }
  document.getElementById("finishclose").addEventListener("click", function () { document.getElementById("finish").hidden = true; document.body.classList.remove("finished"); });
  document.getElementById("copycode").addEventListener("click", function () {
    var btn = this, code = document.getElementById("fcode").textContent;
    var done = function () { btn.textContent = "copied"; setTimeout(function () { btn.textContent = "Copy ship code"; }, 1400); };
    if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, done); else done();
  });

  document.getElementById("checkbtn").addEventListener("click", function () {
    var allOk = true, first = null, verdict = document.getElementById("checkverdict");
    function fail(el, msg) { allOk = false; el.classList.add("bad"); el.classList.remove("good"); el.querySelector(".verdict").textContent = msg; if (!first) first = el; }
    function pass(el, msg) { el.classList.add("good"); el.classList.remove("bad"); el.querySelector(".verdict").textContent = msg || "✓"; }
    if (!dev.value.trim()) { allOk = false; first = dev; dev.classList.add("bad"); } else dev.classList.remove("bad");
    check.querySelectorAll("fieldset.q").forEach(function (fs) {
      var picked = fs.querySelector("input:checked"), key = fs.dataset.q, a = answers[key];
      if (!picked) return fail(fs, "Pick one.");
      if (!a) return pass(fs);
      if (String(picked.value) === String(a.answer)) pass(fs, "✓ " + (a.why || ""));
      else fail(fs, a.nudge || "Not that one. Reread the step it points at and try again.");
    });
    check.querySelectorAll(".task").forEach(function (t) {
      var s = t.querySelector("textarea").value, min = +t.dataset.min || 40;
      if (s.trim().length < min) return fail(t, "That's too short to be the whole thing.");
      var groups = []; try { groups = JSON.parse(t.dataset.any || "[]"); } catch (e) {}
      if (t.dataset.task !== "proud" && groups.length && !looksLikeCode(s)) return fail(t, "That doesn't look like Lua. Paste the code itself.");
      var missing = hasAny(s, groups);
      if (missing) return fail(t, "This task needs " + missing.join(" or ") + " somewhere in it. Is the whole task pasted?");
      pass(t);
    });
    if (!ran.checked) { allOk = false; ran.parentNode.classList.add("bad"); if (!first) first = ran; } else ran.parentNode.classList.remove("bad");
    save();
    if (!allOk) { verdict.textContent = "Not shipped yet. Fix the marked parts and check again."; verdict.className = "verdict bad"; if (first && first.scrollIntoView) first.scrollIntoView({ behavior: "smooth", block: "center" }); return; }
    var date = new Date().toISOString().slice(0, 10);
    ck.shipped = { name: dev.value.trim(), date: date, code: shipCode(dev.value, date) };
    save(); verdict.textContent = "Shipped."; verdict.className = "verdict good"; showFinish();
  });

  if (ck.shipped) {
    var again = document.createElement("button"); again.type = "button"; again.className = "btn ghost shipped-btn"; again.textContent = "Shipped ✓ — show finish screen";
    again.addEventListener("click", showFinish); document.querySelector(".checkrow").appendChild(again);
    var railA = document.querySelector('.rail a[href="#check"]'); if (railA) railA.closest("li").classList.add("done");
  }
})();
