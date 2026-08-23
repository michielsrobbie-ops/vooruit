
(function () {
  'use strict';

  /* --- mobiel menu --- */
  var schakel = document.querySelector('[data-nav-schakel]');
  var nav = document.getElementById('hoofdnav');
  if (schakel && nav) {
    schakel.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'ja';
      nav.setAttribute('data-open', open ? 'nee' : 'ja');
      schakel.setAttribute('aria-expanded', String(!open));
      schakel.textContent = open ? 'Menu' : 'Sluit';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.setAttribute('data-open', 'nee');
        schakel.setAttribute('aria-expanded', 'false');
        schakel.textContent = 'Menu';
      }
    });
  }

  /* --- cookiemelding --- */
  var balk = document.querySelector('[data-cookiebalk]');
  var SLEUTEL = 'vooruit-cookies';
  function lees() { try { return localStorage.getItem(SLEUTEL); } catch (e) { return null; } }
  function bewaar(w) { try { localStorage.setItem(SLEUTEL, w); } catch (e) {} }
  function toonBalk() { if (balk) { balk.hidden = false; } }
  function verbergBalk() { if (balk) { balk.hidden = true; } }

  function pasToe(keuze) {
    document.documentElement.setAttribute('data-cookies', keuze);
    /* Analytische scripts horen hier geladen te worden, en alleen bij keuze === 'alles'.
       Zolang Vooruit geen statistiekdienst gebruikt, gebeurt er niets. */
  }

  if (balk) {
    var eerder = lees();
    if (eerder) { pasToe(eerder); } else { toonBalk(); }
    balk.addEventListener('click', function (e) {
      var knop = e.target.closest('[data-cookies]');
      if (!knop) return;
      var keuze = knop.getAttribute('data-cookies');
      bewaar(keuze); pasToe(keuze); verbergBalk();
    });
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cookies-openen]')) { e.preventDefault(); toonBalk(); }
  });

  /* --- doorsnede: kaarten koppelen en op mobiel inzoomen --- */
  var tekening = document.querySelector('[data-doorsnede]');
  if (tekening) {
    var svg = tekening.querySelector('svg');
    if (svg && window.matchMedia) {
      var smal = window.matchMedia('(max-width: 899px)');
      var pasAan = function () {
        svg.setAttribute('viewBox', smal.matches ? '168 44 544 576' : '0 0 880 620');
      };
      pasAan();
      if (smal.addEventListener) smal.addEventListener('change', pasAan);
      else if (smal.addListener) smal.addListener(pasAan);
    }
    var zet = function (zone) {
      if (zone) tekening.setAttribute('data-actief', zone);
      else tekening.removeAttribute('data-actief');
    };
    var koppel = function (el) {
      var z = el.getAttribute('data-zone');
      ['mouseenter', 'focusin'].forEach(function (ev) { el.addEventListener(ev, function () { zet(z); }); });
      ['mouseleave', 'focusout'].forEach(function (ev) { el.addEventListener(ev, function () { zet(null); }); });
    };
    var legenda = document.querySelector('[data-legenda]');
    if (legenda) legenda.querySelectorAll('[data-zone]').forEach(koppel);
    tekening.querySelectorAll('[data-zone]').forEach(koppel);
  }
})();
