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
      var done = function () { btn.textContent = "copied"; btn.classList.add("ok"); setTimeout(function () { btn.textContent = "copy"; btn.classList.remove("ok"); }, 1400); };
      if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, done); else done();
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
})();
