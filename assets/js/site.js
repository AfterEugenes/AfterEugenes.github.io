// TL;DR — site behaviors: nav, writeup filters, TOC, code copy, lightbox

(function () {
  "use strict";

  // -------------------------------------------------------- language toggle
  var LANG_KEY = "lang";
  var lang = null;
  try { lang = localStorage.getItem(LANG_KEY); } catch (e) {}
  if (!lang) {
    lang = (navigator.language || "en").toLowerCase().indexOf("fr") === 0 ? "fr" : "en";
  }

  var applyLang = function (code) {
    document.documentElement.setAttribute("lang", code);
    Array.prototype.forEach.call(document.querySelectorAll(".i18n"), function (el) {
      if (el.dataset.en === undefined) el.dataset.en = el.textContent;
      el.textContent = code === "fr" && el.dataset.fr ? el.dataset.fr : el.dataset.en;
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-fr-ph]"), function (el) {
      if (el.dataset.enPh === undefined) el.dataset.enPh = el.placeholder || "";
      el.placeholder = code === "fr" ? el.dataset.frPh : el.dataset.enPh;
    });
    var btn = document.querySelector(".lang-toggle");
    if (btn) btn.textContent = code === "fr" ? "FR" : "EN";
  };

  applyLang(lang);

  var langBtn = document.querySelector(".lang-toggle");
  if (langBtn) {
    langBtn.addEventListener("click", function () {
      lang = lang === "fr" ? "en" : "fr";
      try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
      applyLang(lang);
    });
  }

  // ------------------------------------------------------------ mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // ------------------------------------------------------- writeup filters
  var filterRoot = document.querySelector("[data-filters]");
  if (filterRoot) {
    var cards = Array.prototype.slice.call(
      document.querySelectorAll(".writeup-card[data-type]")
    );
    var empty = document.querySelector(".filter-empty");
    var search = document.querySelector("#writeup-search");

    var apply = function () {
      var q = (search && search.value ? search.value : "").trim().toLowerCase();
      var shown = 0;
      cards.forEach(function (card) {
        var type = card.getAttribute("data-type");
        var toggleEl = document.getElementById(type + "-toggle");
        var typeOk = toggleEl ? toggleEl.checked : true;
        var text = (card.getAttribute("data-search") || "") + " " + card.textContent.toLowerCase();
        var searchOk = !q || text.toLowerCase().indexOf(q) !== -1;
        var visible = typeOk && searchOk;
        card.classList.toggle("is-hidden", !visible);
        if (visible) shown++;
      });
      if (empty) empty.classList.toggle("is-hidden", shown > 0);
    };

    Array.prototype.forEach.call(
      filterRoot.querySelectorAll(".filter-toggle"),
      function (el) {
        el.addEventListener("change", apply);
      }
    );
    if (search) search.addEventListener("input", apply);
    apply();
  }

  // ------------------------------------------------------------------ TOC
  var toc = document.querySelector("[data-toc]");
  if (toc) {
    var prose = document.querySelector(".prose");
    if (prose) {
      var heads = prose.querySelectorAll("h1, h2, h3");
      if (heads.length > 1) {
        var ul = toc.querySelector("ul");
        Array.prototype.forEach.call(heads, function (h) {
          if (!h.id) {
            h.id = h.textContent.trim().toLowerCase().replace(/[^\w]+/g, "-");
          }
          var li = document.createElement("li");
          li.className = h.tagName.toLowerCase();
          var a = document.createElement("a");
          a.href = "#" + h.id;
          a.textContent = h.textContent;
          li.appendChild(a);
          ul.appendChild(li);
        });
      } else {
        toc.style.display = "none";
      }
    }
  }

  // ------------------------------------------------- code copy buttons
  Array.prototype.forEach.call(document.querySelectorAll(".highlight"), function (block) {
    var pre = block.querySelector("pre");
    if (!pre) return;
    var btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "copy";
    btn.addEventListener("click", function () {
      navigator.clipboard.writeText(pre.innerText).then(function () {
        btn.textContent = "copied!";
        setTimeout(function () { btn.textContent = "copy"; }, 1400);
      });
    });
    block.appendChild(btn);
  });

  // ---------------------------------------------------------- image lightbox
  var lightbox = document.createElement("div");
  lightbox.className = "lightbox is-hidden";
  document.body.appendChild(lightbox);

  Array.prototype.forEach.call(document.querySelectorAll("img.content-image"), function (img) {
    img.addEventListener("click", function () {
      lightbox.innerHTML = "";
      var big = document.createElement("img");
      big.src = img.src;
      big.alt = img.alt;
      lightbox.appendChild(big);
      lightbox.classList.remove("is-hidden");
    });
  });

  lightbox.addEventListener("click", function () {
    lightbox.classList.add("is-hidden");
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") lightbox.classList.add("is-hidden");
  });
})();
