# NVH Docs — Rebuild, Deploy & Update Guide

Everything you need to keep these docs alive after the initial delivery: how to edit content, regenerate the site, push to git, and host on your own domain.

---

## 1. Prerequisites (one-time setup)

You'll need Python 3.9+ and a couple of packages.

```cmd
:: From any terminal on Windows
python --version
pip install markdown reportlab
```

That's it. The build scripts use only `markdown` (HTML generation) and `reportlab` (PDF generation). Everything else is standard library.

> **Optional**: If you want better-looking PDFs for non-Latin scripts (Chinese, Arabic, Thai, etc.), drop DejaVu fonts into a `fonts/` folder next to `generate_pdfs_all.py`. Otherwise reportlab falls back to Helvetica and CJK glyphs show as boxes in PDFs (HTML is fine either way).

---

## 2. Directory layout

```
nvh-docs-v2/
├── index.html                   ← generated, root landing page
├── style.css                    ← shared CSS
├── README.md                    ← project overview
├── HOSTING-SETUP.md             ← deployment steps
├── REBUILD-GUIDE.md             ← this file
├── _build/                      ← ★ build scripts live here
│   ├── build_docs.py            ← regenerates all HTML + MD
│   ├── generate_pdfs_all.py     ← regenerates all PDFs
│   ├── translations_ui.py       ← landing page strings, language list
│   ├── quick_ref_batch1.py      ← Quick Ref translations (locales 1-8)
│   ├── quick_ref_batch2.py      ← Quick Ref translations (locales 9-16)
│   ├── quick_ref_batch3.py      ← Quick Ref translations (locales 17-23)
│   ├── user_guide_batch1.py     ← User Guide translations (de, es, fr, it)
│   ├── user_guide_batch2.py     ← User Guide translations (pt, pl, ru, zh)
│   ├── user_guide_batch3.py     ← User Guide translations (cs, sk, hu, hr, bg)
│   ├── user_guide_batch4.py     ← User Guide translations (sv, no, fi, ro, tr)
│   └── user_guide_batch5.py     ← User Guide translations (ar, ja, ko, th, vi)
├── screenshots/                 ← all image assets, PNG preferred
│   ├── 01-home-2sensor.png
│   ├── 02-tab-bar.png
│   └── … (11 total)
├── en/                          ← ★ English is the source of truth
│   ├── index.html               ← generated
│   ├── user-guide.html          ← generated
│   ├── user-guide.md            ← ★ EDIT THIS for content changes
│   ├── user-guide.pdf           ← generated
│   ├── quick-reference.html     ← generated
│   ├── quick-reference.md       ← ★ EDIT THIS for content changes
│   └── quick-reference.pdf      ← generated
├── de/ es/ fr/ … (29 more)      ← all generated from translation batches
```

The `★` items are the only ones you ever hand-edit. Everything else is regenerated.

---

## 3. What change triggers what rebuild

| You change… | Run | What regenerates |
|---|---|---|
| A screenshot in `screenshots/` | nothing | HTML already references the file by name — just commit the new image |
| `style.css` | nothing | Already linked relatively — refresh browser |
| `en/user-guide.md` or `en/quick-reference.md` | `python _build/build_docs.py` | English HTML + MD for all locales (translations don't auto-update) |
| Anything in `_build/translations_ui.py` (footer, language list) | `python _build/build_docs.py` | Every locale's HTML |
| A translation in a `_build/*batch*.py` file | `python _build/build_docs.py` | Just that locale's HTML + MD |
| Want fresh PDFs | `python _build/generate_pdfs_all.py` | All PDFs from current MD files |

> **Important nuance**: If you edit the English source (`en/user-guide.md`), the translations DON'T auto-update — they're still locked at the old content. The structure-checker just verifies line counts match. So expect translations to drift if you change English without updating them. For minor English-only edits (typos, link fixes), this is fine; for major content changes, plan to retranslate.

---

## 4. Typical workflows

### A) Replacing a screenshot

```cmd
:: Just drop the new PNG into screenshots/ with the exact same filename
:: No rebuild needed. Just commit:
cd C:\path\to\evdiag-pages\nvh
git add screenshots/01-home-2sensor.png
git commit -m "Update home screen screenshot"
git push
```

GitHub Pages picks it up within ~1 minute. Browser cache may need a hard-refresh (Ctrl+F5).

### B) Fixing a typo in English

```cmd
:: 1. Edit the English source
notepad en\user-guide.md

:: 2. Regenerate
python _build\build_docs.py

:: 3. Optionally regenerate PDFs
python _build\generate_pdfs_all.py

:: 4. Commit and push
git add en/ index.html
git commit -m "Fix typo in user guide intro"
git push
```

### C) Updating a single translation

```cmd
:: 1. Find which batch file contains the locale
:: User Guide:  user_guide_batch1.py (de,es,fr,it), batch2 (pt,pl,ru,zh), etc.
:: Quick Ref:   quick_ref_batch1.py (de,es,fr,it,pt,pl,ru,zh), batch2 (cs,sk,hu,hr,bg,sv,no,fi), batch3 (ro,tr,ar,ja,ko,th,vi)

:: 2. Edit the dict entry inside that file (it's just a Python string)
notepad _build\user_guide_batch1.py

:: 3. Regenerate
python _build\build_docs.py
python _build\generate_pdfs_all.py

:: 4. Commit
git add de/ _build/user_guide_batch1.py
git commit -m "Improve German translation phrasing"
git push
```

### D) Updating the version number or links in the footer

Edit `_build/translations_ui.py` — the `TRANSLATIONS` dict near the top has `footer_*` keys. Change them, run `build_docs.py`, push.

---

## 5. First-time git upload

You already have the `evdiag-pages` repo. I recommend putting the docs in a subdirectory so they coexist with whatever else is in there (currently `promo.html`).

```cmd
:: From the directory where you unzipped the docs:
cd C:\Users\rfmot\evdiag-pages

:: Create a subdirectory for the docs (recommended name: nvh)
mkdir nvh
xcopy /E /I C:\path\to\unzipped\nvh-docs-v2\* nvh\

:: Verify the structure
dir nvh

:: Commit
git add nvh/
git commit -m "Add multilingual user documentation (24 locales)"
git push origin main
```

After the push, the docs are live at:
- `https://evdiag.github.io/evdiag-pages/nvh/` (default GitHub Pages URL)
- `https://nvh.evdiag.net/` if you set up a custom subdomain (see §6)

---

## 6. Use your own domain — recommended

**Yes, use your own domain.** Three reasons:

1. **Brand**: `nvh.evdiag.net` looks far more professional in App Store / Play Store listings than `evdiag.github.io/evdiag-pages/nvh/`.
2. **Portability**: If you ever migrate off GitHub Pages (Cloudflare Pages, Netlify, your own server), the link in your store listings doesn't break — you just point DNS somewhere else.
3. **Reviewer trust**: Apple and Google reviewers do click through external links. A vanity domain reads as "real company"; a github.io URL can read as "indie project."

### Recommended setup: subdomain `nvh.evdiag.net`

**Step 1 — At your DNS registrar** (whoever sold you `evdiag.net`):

Add a CNAME record:
```
Type:   CNAME
Name:   nvh
Value:  evdiag.github.io
TTL:    3600 (or default)
```

**Step 2 — In the repo**, add a `CNAME` file (no extension) inside `nvh/`:
```
nvh.evdiag.net
```

**Step 3 — In the GitHub repo settings**:
- Go to `https://github.com/EVDiag/evdiag-pages/settings/pages`
- Under "Custom domain", enter `nvh.evdiag.net`, save
- Wait a few minutes for DNS check to pass
- Tick "Enforce HTTPS" once it becomes available

Done. The site is now live at `https://nvh.evdiag.net/`.

> **Heads up**: A repo can only have one CNAME file at a time. If you also use `evdiag.github.io/evdiag-pages/` for the existing `promo.html` content, putting a CNAME inside `nvh/` won't conflict — GitHub only reads the CNAME from the root of what it's serving. Test this on a low-stakes path first.

---

## 7. Screenshot format and resolution

### PNG, not SVG

You asked about converting to SVG. **Don't.** SVG describes vector shapes (lines, curves, fills). Screenshots are pixels. Converting a screenshot to SVG either:

- Embeds the raw bitmap as a base64 string inside the SVG (defeats the purpose — same data, bigger file, slower render), or
- Auto-traces it into vector paths (produces ugly, lossy garbage that looks nothing like the original UI).

**The placeholder mockups I generated are SVG because they're synthetic diagrams** (rectangles, text, simple icons drawn from scratch). Real screenshots from your phone must stay PNG.

If you want vector for something specific — say, an architecture diagram or a flowchart in the User Guide — that's a good SVG use case. Hand-author it or use a tool like Figma → export SVG. But camera-style screenshots: always PNG.

### Resolution targets

| Source | Target file | Notes |
|---|---|---|
| iPhone 15/16 Pro Max screenshot | ~1290×2796 px native | Keep native; CSS scales it down responsively |
| Android (Pixel, Samsung) | ~1080×2400 px native | Keep native |
| If you must downscale | 800–1200 px wide | Anything below 800 looks blurry on retina displays |
| Hard cap | 2500 px on the long edge | Beyond this you're wasting bytes |
| File size goal | 100–400 KB each | After optimization |

**Practical workflow:**

1. Capture on the device with the native screenshot function (don't photograph the screen)
2. Transfer the PNG to your computer (AirDrop, USB, email, whatever)
3. Open in any image tool. If file is over 500 KB, run it through an optimizer:
   - **Free GUI tools**: TinyPNG (web), ImageOptim (Mac), FileOptimizer (Windows)
   - **CLI**: `pngcrush input.png output.png` or `oxipng -o 4 input.png`
4. Save with the **exact filename** the docs expect (see §8 below)
5. Drop into `screenshots/` folder
6. Commit and push

### Filename map (don't rename)

The HTML files reference these exact paths:

```
screenshots/01-home-2sensor.png         ← Home screen with 2-Sensor tab active
screenshots/02-tab-bar.png              ← Close-up of the top tab bar
screenshots/03-3sensor-tab.png          ← 3-Sensor tab showing triangle inputs
screenshots/04-triangle-result.png      ← Triangle result with source location
screenshots/05-materials-tab.png        ← Materials picker showing the list
screenshots/06-settings.png             ← Settings panel
screenshots/07-paywall.png              ← The paywall modal
screenshots/08-photo-annotation.png     ← Photo with sensor markers overlaid
screenshots/09-pdf-report.png           ← Example generated PDF report
screenshots/10-help-tab.png             ← Help/tutorials tab
screenshots/11-pro-locked-field.png     ← Locked input field with gold padlock badge
```

> **All locales reuse the same English-UI screenshots by default.** This is the right call for the first round — translating UI screenshots for 24 locales is enormous extra work for marginal gain when the docs themselves are translated. If a specific market complains, you can add locale-specific overrides later.

---

## 8. Updating a screenshot later — the quick path

```cmd
:: 1. Drop the new PNG into screenshots/ with the same filename
copy new-screenshot.png C:\Users\rfmot\evdiag-pages\nvh\screenshots\01-home-2sensor.png

:: 2. No rebuild needed — HTML already references the filename
:: 3. Commit and push
cd C:\Users\rfmot\evdiag-pages
git add nvh/screenshots/01-home-2sensor.png
git commit -m "Update home screen screenshot"
git push
```

If you've also edited content somewhere, do a full rebuild first:

```cmd
cd C:\Users\rfmot\evdiag-pages\nvh
python _build\build_docs.py
python _build\generate_pdfs_all.py
git add .
git commit -m "Refresh docs and screenshots"
git push
```

---

## 9. Common pitfalls

**"My PDF shows boxes instead of Chinese/Arabic/Thai characters"**
Reportlab is using its Helvetica fallback because no Unicode font is installed. Either ignore (HTML versions work fine), or drop a DejaVu font file into a `fonts/` folder next to `generate_pdfs_all.py`.

**"The browser shows the old version after my push"**
Browser cache. Hard-refresh with Ctrl+F5 (Windows) or Cmd+Shift+R (Mac). On mobile, force-quit and reopen the browser. GitHub Pages itself updates within ~60 seconds of a push.

**"build_docs.py says 'module not found'"**
You're not running it from the right place, or you don't have `markdown` installed. Run `pip install markdown reportlab` first, and run the script either as `python _build/build_docs.py` from the docs root, or `cd _build && python build_docs.py`.

**"I edited a translation but the HTML didn't update"**
Did you run `python _build/build_docs.py` after editing? The HTML is generated, not live-loaded from the batch files.

**"The line counts no longer match across locales"**
You probably added or removed content in the English source without updating translations. This is fine functionally — the docs still work — but means translations are now slightly out of sync with the English version. Plan to update translations when you do significant English edits.

---

## 10. Adding a new locale later

If a customer base in, say, Dutch or Greek emerges later, here's the path:

1. Open `_build/translations_ui.py` and add the locale code to `LANGUAGE_ORDER` (e.g. `'nl'`)
2. Add a row to the `TRANSLATIONS` dict with all the UI strings translated to that language
3. Create a new translation batch file `_build/user_guide_batch6.py` and `_build/quick_ref_batch4.py` with the locale's translations
4. Run `python _build/build_docs.py`
5. Done — the new locale appears in the language switcher automatically

The `LANGUAGE_ORDER` list is the single source of truth for which locales exist; everything else flows from it.

---

*Maintained by Roman / EVDiag. For questions: support@evdiag.net.*
