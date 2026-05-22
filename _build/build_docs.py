"""Build script for NVH Source Locator documentation site.

Reads:
- <docs-root>/translations_ui.py (landing page strings)
- <docs-root>/quick_ref_batch1.py (Quick Reference content batch 1)
- Future: quick_ref_batch2.py, user_guide_batchN.py
- <docs-root>/en/*.md (English source)

Produces:
- <docs-root>/index.html (top-level landing with all language links)
- <docs-root>/{locale}/index.html (per-language landing)
- <docs-root>/{locale}/user-guide.html
- <docs-root>/{locale}/quick-reference.html
- <docs-root>/{locale}/*.md (markdown source files)
- <docs-root>/style.css (shared)

Each .html page includes:
- Language switcher with all 30 languages
- "Download as PDF" button (if PDF exists for that locale)
- The translated disclaimer banner
- Footer with EVDiag/support info
"""

import sys
import os
import markdown
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translations_ui import TRANSLATIONS, LANGUAGE_ORDER, RTL_LANGS, ENGLISH_FALLBACK

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Load translation batches dynamically ---
quick_ref_translations = {}

def load_batch(filename, var_name, target_dict):
    """Import a batch file and merge its translations dict into target."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if not os.path.exists(path):
        return
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    batch = getattr(mod, var_name, {})
    target_dict.update(batch)
    print(f"  loaded {len(batch)} translations from {filename}")

print("Loading translation batches...")
for batch_num in range(1, 10):
    load_batch(f'quick_ref_batch{batch_num}.py', 'QUICK_REF_TRANSLATIONS', quick_ref_translations)

user_guide_translations = {}
for batch_num in range(1, 10):
    load_batch(f'user_guide_batch{batch_num}.py', 'USER_GUIDE_TRANSLATIONS', user_guide_translations)

# --- Load English source ---
with open(os.path.join(DOCS_ROOT, 'en', 'quick-reference.md'), 'r', encoding='utf-8') as f:
    quick_ref_translations['en'] = f.read()

with open(os.path.join(DOCS_ROOT, 'en', 'user-guide.md'), 'r', encoding='utf-8') as f:
    user_guide_translations['en'] = f.read()


# --- CSS ---
CSS = """
:root {
  --navy: #0F3460;
  --accent: #00B4D8;
  --text: #222;
  --text-muted: #556;
  --text-faint: #889;
  --border: #E5E7EB;
  --bg: #FFFFFF;
  --surf: #F8FAFC;
  --info-bg: #D1ECF1;
  --info-txt: #0C5460;
  --warn-bg: #FFF8E1;
  --warn-txt: #78350F;
  --warn-border: #F59E0B;
}

* { box-sizing: border-box; }

html[dir="rtl"] body { text-align: right; }
html[dir="rtl"] .lang-switcher { direction: ltr; text-align: left; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  max-width: 900px;
  margin: 0 auto;
  padding: 24px;
  color: var(--text);
  line-height: 1.65;
  background: var(--bg);
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  padding: 14px 0;
  border-bottom: 1px solid var(--border);
  margin-bottom: 24px;
}

.top-nav .home-link {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
}

.top-nav .home-link:hover {
  color: var(--accent);
}

.lang-switcher {
  position: relative;
  display: inline-block;
}

.lang-switcher-button {
  background: var(--surf);
  border: 1px solid var(--border);
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  color: var(--navy);
  font-weight: 500;
}

.lang-switcher-button::after {
  content: " ▾";
  font-size: 10px;
  color: var(--text-faint);
}

.lang-switcher-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 4px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
  padding: 8px 0;
  min-width: 200px;
  max-height: 60vh;
  overflow-y: auto;
  z-index: 100;
  display: none;
}

.lang-switcher.open .lang-switcher-menu { display: block; }

.lang-switcher-menu a {
  display: block;
  padding: 8px 16px;
  color: var(--text);
  text-decoration: none;
  font-size: 14px;
}

.lang-switcher-menu a:hover { background: var(--surf); }
.lang-switcher-menu a.active { background: var(--info-bg); color: var(--info-txt); font-weight: 600; }

.download-banner {
  background: var(--navy);
  color: #FFFFFF;
  padding: 14px 20px;
  text-align: center;
  border-radius: 10px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.download-banner span {
  font-weight: 600;
}

.download-banner a {
  background: var(--accent);
  color: #FFFFFF;
  padding: 8px 16px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
}

.download-banner a:hover { background: #0099BB; }

.download-banner .alt-link {
  background: transparent;
  border: 1px solid rgba(255,255,255,0.3);
  font-size: 13px;
  font-weight: 500;
  padding: 7px 14px;
}

.disclaimer-note {
  background: var(--surf);
  border-left: 4px solid var(--accent);
  padding: 10px 14px;
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 24px;
  border-radius: 0 6px 6px 0;
  font-style: italic;
}

h1, h2, h3, h4 {
  color: var(--navy);
  line-height: 1.3;
}

h1 {
  border-bottom: 2px solid var(--accent);
  padding-bottom: 12px;
  margin-top: 24px;
  font-size: 28px;
}

h2 {
  margin-top: 36px;
  font-size: 22px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
}

h3 { margin-top: 28px; font-size: 17px; }
h4 { margin-top: 20px; font-size: 15px; color: var(--text); }

p { margin: 12px 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 14px;
}

th, td {
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

th {
  background: var(--surf);
  font-weight: 600;
  color: var(--navy);
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

tr:last-child td { border-bottom: none; }

code {
  font-family: "SF Mono", Menlo, Consolas, "Courier New", monospace;
  background: var(--surf);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 90%;
  color: var(--navy);
}

pre {
  background: var(--surf);
  padding: 14px 16px;
  border-radius: 6px;
  border: 1px solid var(--border);
  overflow-x: auto;
  font-size: 13px;
  line-height: 1.5;
}

pre code { background: none; padding: 0; color: var(--text); }

img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 20px auto;
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

blockquote {
  border-left: 4px solid var(--accent);
  margin: 16px 0;
  padding: 12px 18px;
  background: var(--surf);
  color: var(--text-muted);
  font-size: 14px;
  border-radius: 0 6px 6px 0;
}

blockquote p { margin: 6px 0; }

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

hr { border: none; border-top: 1px solid var(--border); margin: 36px 0; }

ul, ol { padding-left: 24px; }
li { margin: 6px 0; }

.docs-footer {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  font-size: 13px;
  color: var(--text-faint);
  text-align: center;
}

.docs-footer a { color: var(--text-muted); }

.doc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 32px;
}

.doc-card {
  background: #FFFFFF;
  padding: 24px;
  border-radius: 10px;
  border: 1px solid var(--border);
  text-decoration: none;
  color: inherit;
  display: block;
  transition: transform 0.15s, box-shadow 0.15s;
}

.doc-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  border-color: var(--accent);
}

.doc-card h2 {
  color: var(--navy);
  margin: 0 0 8px;
  font-size: 18px;
  border-bottom: none;
  padding-bottom: 0;
}

.doc-card p {
  color: var(--text-muted);
  font-size: 14px;
  margin: 8px 0;
}

.doc-card .badge {
  display: inline-block;
  background: var(--info-bg);
  color: var(--info-txt);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  margin-top: 8px;
}

@media print {
  body { max-width: none; padding: 0; }
  .download-banner, .lang-switcher, .top-nav { display: none; }
  .disclaimer-note { background: none; border: none; padding: 0; }
  h1, h2, h3 { page-break-after: avoid; }
  img { page-break-inside: avoid; max-width: 80%; }
}

@media (max-width: 700px) {
  body { padding: 16px; }
  h1 { font-size: 24px; }
  h2 { font-size: 20px; }
  table { font-size: 13px; }
  th, td { padding: 8px 10px; }
  .doc-grid { grid-template-columns: 1fr; }
}
"""


def lang_switcher_html(current_locale, locale_paths):
    """Build the language switcher dropdown HTML.

    current_locale: e.g. 'de'
    locale_paths: dict mapping locale → relative path (from current page) to that locale's same-doc page
    """
    items = []
    for loc in LANGUAGE_ORDER:
        ui = TRANSLATIONS.get(loc) or TRANSLATIONS['en']
        active = ' class="active"' if loc == current_locale else ''
        href = locale_paths.get(loc, f'../{loc}/index.html')
        items.append(f'      <a href="{href}"{active}>{ui["lang_name"]}</a>')
    items_html = '\n'.join(items)

    ui = TRANSLATIONS.get(current_locale) or TRANSLATIONS['en']
    current_name = ui['lang_name']

    return f'''<div class="lang-switcher" id="langSwitcher">
    <button class="lang-switcher-button" onclick="document.getElementById('langSwitcher').classList.toggle('open')">🌐 {current_name}</button>
    <div class="lang-switcher-menu">
{items_html}
    </div>
  </div>'''


def get_ui_strings(locale):
    """Return UI strings for a locale, falling back to English if needed.
    
    If the locale has _fallback: True, merge its lang_name (native script)
    with the English UI strings — so the switcher shows native name but
    UI text is English."""
    entry = TRANSLATIONS.get(locale)
    if entry is None:
        return TRANSLATIONS['en']
    if entry.get('_fallback'):
        merged = dict(TRANSLATIONS['en'])
        merged['lang_name'] = entry['lang_name']
        return merged
    return entry


def get_locale_doc_content(locale, doc_type):
    """Return the markdown content for a doc in a locale, with fallback."""
    if doc_type == 'quick-reference':
        return quick_ref_translations.get(locale) or quick_ref_translations['en']
    elif doc_type == 'user-guide':
        return user_guide_translations.get(locale) or user_guide_translations['en']
    return None


def render_doc_page(locale, doc_type, title_key, pdf_filename, other_doc_key, other_doc_link):
    """Render a documentation HTML page for a given locale and doc type."""
    ui = get_ui_strings(locale)
    is_rtl = locale in RTL_LANGS
    direction = 'rtl' if is_rtl else 'ltr'

    md_content = get_locale_doc_content(locale, doc_type)
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'attr_list'])
    html_body = md.convert(md_content)

    # Language switcher — each locale link points at the same doc in its folder
    locale_paths = {loc: f'../{loc}/{doc_type}.html' for loc in LANGUAGE_ORDER}
    switcher = lang_switcher_html(locale, locale_paths)

    title = ui[title_key]
    page_title = f"NVH Source Locator — {title}"

    other_title = ui[other_doc_key]

    html = f'''<!DOCTYPE html>
<html lang="{locale}" dir="{direction}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>

  <div class="top-nav">
    <a href="index.html" class="home-link">📘 {ui["doc_section_title"]}</a>
    {switcher}
  </div>

  <div class="download-banner">
    <span>{title}</span>
    <a href="{pdf_filename}" download>📥 {ui["download_pdf"]}</a>
    <a href="{other_doc_link}" class="alt-link">{other_title} →</a>
  </div>

  <div class="disclaimer-note">
    {ui["disclaimer"]}
  </div>

  {html_body}

  <div class="docs-footer">
    <p>
      {ui["footer_dev"]} — <a href="https://evdiag.net">evdiag.net</a><br>
      {ui["footer_questions"]} <a href="mailto:support@evdiag.net">support@evdiag.net</a>
    </p>
  </div>

  <script>
    document.addEventListener('click', function(e) {{
      var sw = document.getElementById('langSwitcher');
      if (sw && !sw.contains(e.target)) sw.classList.remove('open');
    }});
  </script>

</body>
</html>
'''
    return html


def render_locale_index(locale):
    """Render the per-language landing page (e.g. en/index.html)."""
    ui = get_ui_strings(locale)
    is_rtl = locale in RTL_LANGS
    direction = 'rtl' if is_rtl else 'ltr'

    locale_paths = {loc: f'../{loc}/index.html' for loc in LANGUAGE_ORDER}
    switcher = lang_switcher_html(locale, locale_paths)

    html = f'''<!DOCTYPE html>
<html lang="{locale}" dir="{direction}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NVH Source Locator — {ui["doc_section_title"]}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>

  <div class="top-nav">
    <a href="../index.html" class="home-link">🌐 {ui["back_to_home"]}</a>
    {switcher}
  </div>

  <h1>NVH Source Locator</h1>
  <p>{ui["intro"]}</p>

  <div class="disclaimer-note">
    {ui["disclaimer"]}
  </div>

  <div class="doc-grid">
    <a href="user-guide.html" class="doc-card">
      <h2>📘 {ui["user_guide_title"]}</h2>
      <p>{ui["user_guide_desc"]}</p>
      <span class="badge">{ui["user_guide_badge"]}</span>
    </a>

    <a href="quick-reference.html" class="doc-card">
      <h2>📋 {ui["quick_ref_title"]}</h2>
      <p>{ui["quick_ref_desc"]}</p>
      <span class="badge">{ui["quick_ref_badge"]}</span>
    </a>
  </div>

  <div class="docs-footer">
    <p>
      {ui["footer_dev"]} — <a href="https://evdiag.net">evdiag.net</a><br>
      {ui["footer_questions"]} <a href="mailto:support@evdiag.net">support@evdiag.net</a>
    </p>
  </div>

  <script>
    document.addEventListener('click', function(e) {{
      var sw = document.getElementById('langSwitcher');
      if (sw && !sw.contains(e.target)) sw.classList.remove('open');
    }});
  </script>

</body>
</html>
'''
    return html


def render_root_index():
    """Render the top-level landing page that lists all languages."""
    # Build list of all 30 locales with their landing page links
    items = []
    for loc in LANGUAGE_ORDER:
        ui = TRANSLATIONS.get(loc) or TRANSLATIONS['en']
        items.append(f'    <a href="{loc}/index.html" class="lang-card"><span class="lang-name">{ui["lang_name"]}</span><span class="lang-code">{loc.upper()}</span></a>')
    items_html = '\n'.join(items)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NVH Source Locator — Documentation</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      max-width: 900px;
      margin: 40px auto;
      padding: 24px;
      color: #222;
      background: #F5F7FA;
      line-height: 1.6;
    }}
    h1 {{
      color: #0F3460;
      border-bottom: 2px solid #00B4D8;
      padding-bottom: 12px;
    }}
    p.intro {{ color: #556; font-size: 15px; }}
    .lang-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 32px;
    }}
    .lang-card {{
      background: #FFFFFF;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #E5E7EB;
      text-decoration: none;
      color: inherit;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
    }}
    .lang-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      border-color: #00B4D8;
    }}
    .lang-name {{
      font-size: 15px;
      color: #0F3460;
      font-weight: 500;
    }}
    .lang-code {{
      font-size: 11px;
      color: #889;
      font-family: monospace;
      background: #F8FAFC;
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .footer {{
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid #E5E7EB;
      text-align: center;
      font-size: 13px;
      color: #889;
    }}
    .footer a {{ color: #556; }}
  </style>
</head>
<body>

  <h1>NVH Source Locator — Documentation</h1>
  <p class="intro">Choose your language to read the user guide and quick reference:</p>

  <div class="lang-grid">
{items_html}
  </div>

  <div class="footer">
    <p>
      Developed by <a href="https://evdiag.net">EVDiag</a> · Support:
      <a href="mailto:support@evdiag.net">support@evdiag.net</a>
    </p>
  </div>

</body>
</html>
'''


def write_file(path, content):
    """Write a file, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    print("\nWriting style.css...")
    write_file(os.path.join(DOCS_ROOT, 'style.css'), CSS)

    print("Writing root index.html...")
    write_file(os.path.join(DOCS_ROOT, 'index.html'), render_root_index())

    print("Generating per-locale pages:")
    for locale in LANGUAGE_ORDER:
        locale_dir = os.path.join(DOCS_ROOT, locale)
        os.makedirs(locale_dir, exist_ok=True)

        # Per-language landing
        write_file(os.path.join(locale_dir, 'index.html'),
                   render_locale_index(locale))

        # Quick Reference markdown source
        qr_md = get_locale_doc_content(locale, 'quick-reference')
        write_file(os.path.join(locale_dir, 'quick-reference.md'), qr_md)

        # User Guide markdown source
        ug_md = get_locale_doc_content(locale, 'user-guide')
        write_file(os.path.join(locale_dir, 'user-guide.md'), ug_md)

        # Quick Reference HTML
        qr_html = render_doc_page(
            locale, 'quick-reference',
            title_key='quick_ref_title',
            pdf_filename='quick-reference.pdf',
            other_doc_key='user_guide_title',
            other_doc_link='user-guide.html'
        )
        write_file(os.path.join(locale_dir, 'quick-reference.html'), qr_html)

        # User Guide HTML
        ug_html = render_doc_page(
            locale, 'user-guide',
            title_key='user_guide_title',
            pdf_filename='user-guide.pdf',
            other_doc_key='quick_ref_title',
            other_doc_link='quick-reference.html'
        )
        write_file(os.path.join(locale_dir, 'user-guide.html'), ug_html)

        # Status flag
        qr_status = "translated" if locale in quick_ref_translations and locale != 'en' else \
                    "english source" if locale == 'en' else "english fallback"
        ug_status = "translated" if locale in user_guide_translations and locale != 'en' else \
                    "english source" if locale == 'en' else "english fallback"
        print(f"  {locale}: QR={qr_status}, UG={ug_status}")

    print(f"\nGenerated docs in {DOCS_ROOT}")


if __name__ == '__main__':
    main()
