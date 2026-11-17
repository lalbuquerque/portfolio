(() => {
  'use strict';
  const supported = ['en', 'pt', 'es'];
  const basePath = new URL('.', document.currentScript.src).pathname;
  const key = 'portfolio-language';
  const normalize = value => typeof value === 'string' ? value.toLowerCase().split(/[-_]/)[0] : '';
  let saved;
  try { saved = localStorage.getItem(key); } catch (_) { /* Storage may be disabled. */ }

  // Explicit language URLs are always respected, including shared links.
  if (location.pathname === basePath || location.pathname === basePath + 'index.html') {
    const preferred = Array.from(navigator.languages || []);
    if (!preferred.length && navigator.language) preferred.push(navigator.language);
    const language = supported.includes(saved) ? saved :
      preferred.map(normalize).find(value => supported.includes(value)) || 'en';
    location.replace(basePath + language + '/' + location.search + location.hash);
  }

  // Only an intentional selector choice changes the saved preference.
  document.addEventListener('click', event => {
    const link = event.target.closest?.('.language-switch a');
    if (!link) return;
    const language = normalize(link.getAttribute('lang'));
    if (supported.includes(language)) {
      try { localStorage.setItem(key, language); } catch (_) { /* Navigation still works. */ }
    }
  });
})();
