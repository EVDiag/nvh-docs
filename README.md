# NVH Source Locator — Multilingual Documentation

This bundle contains the complete documentation site for NVH Source Locator, in 30 locales.

## Status of translations (v2, batch 1)

| Status | Quick Reference | User Guide |
|---|---|---|
| ✅ Fully translated | en, de, es, fr, it, pt, pl, ru, zh | en (others pending in next batches) |
| ⏳ Coming in next batches | cs, sk, hu, hr, bg, sv, no, fi, ro, tr, ar, ja, ko, th, vi | de, es, fr, it, pt, pl, ru, zh + others |
| 🔁 English fallback | be, fa, hi, id, ms, tl (native lang name shown in switcher) | same |

When subsequent batches arrive, drop the `quick_ref_batch2.py` and `user_guide_batchN.py` files into the same folder as `build_docs.py` and re-run.

## What's in this bundle

```
nvh-docs/
├── index.html              ← root landing page (all 30 languages)
├── style.css               ← shared stylesheet
├── support.js              ← behaviour of the support form
├── _routes.json            ← tells Cloudflare only /api/* needs a function
├── test-contact.mjs        ← offline test of the support function
├── README.md               ← this file
├── CLOUDFLARE-MIGRATION.md ← how the site is hosted and how the form sends mail
├── HOSTING-SETUP.md        ← superseded: the old GitHub Pages setup
├── functions/
│   └── api/contact.js      ← POST /api/contact → Resend (runs on Cloudflare)
├── support/
│   └── index.html          ← support form + FAQ (English only)
├── media/                  ← the TDOA explainer video, poster and subtitles
├── screenshots/            ← SVG mockups + .png screenshots (add later)
│   ├── 01-home-2sensor.svg
│   ├── 01-home-2sensor.png   ← you replace with real device shot
│   ├── 02-tab-bar.svg
│   └── ...
├── en/
│   ├── index.html          ← per-language landing
│   ├── user-guide.html
│   ├── user-guide.md       ← markdown source
│   ├── user-guide.pdf
│   ├── quick-reference.html
│   ├── quick-reference.md
│   └── quick-reference.pdf
├── de/
│   └── ... (same structure)
├── es/
│   └── ...
... (28 more locales)
```

## How to add real screenshots

The markdown files reference `../screenshots/<name>.png`. Today the folder contains placeholder `.svg` files. Replace with real screenshots:

1. Take a screenshot on your phone (English UI)
2. Save as PNG to `screenshots/` with the matching filename:
   - `01-home-2sensor.png`
   - `02-tab-bar.png`
   - `03-3sensor-tab.png`
   - `04-triangle-result.png`
   - `05-materials-tab.png`
   - `06-settings.png`
   - `07-paywall.png`
   - `08-photo-annotation.png`
   - `09-pdf-report.png`
   - `10-help-tab.png`
   - `11-pro-locked-field.png`
3. Done. All language pages reference the same `.png` files, so one screenshot serves all 30 languages.

Note: screenshots in English are fine. Each language version still uses these same English-UI screenshots — that's a standard practice for technical documentation.

## How it is published

The site runs on **Cloudflare Pages**, from this repository, at
`https://nvh.evdiag.net/`. Push to `main` and it redeploys; push to any other
branch and you get a preview address.

It is on Cloudflare rather than GitHub Pages because `/support/` has a working
contact form, and sending mail needs an API key that must stay on a server
instead of in the browser. `functions/api/contact.js` is that server: one small
function Cloudflare runs beside the static files.

See `CLOUDFLARE-MIGRATION.md` for the project settings, the environment
variables, and how to roll back to GitHub Pages if ever needed.

## How to update the docs

To edit content in English:

1. Edit `en/user-guide.md` or `en/quick-reference.md`
2. Re-run `build_docs.py` (uses Python's `markdown` package)
3. Commit and push

To edit a translation:

1. Edit `<locale>/user-guide.md` or `<locale>/quick-reference.md`
2. Re-run `build_docs.py`
3. Commit and push

To add more translation batches:

1. Drop new translation files (e.g., `quick_ref_batch2.py`) into the build script directory
2. Re-run `build_docs.py` — it auto-detects and loads them

## Disclaimer

Each translated page includes a soft professional disclaimer noting that the English original is authoritative for the most precise technical terminology. This is standard practice for technical product docs and protects against minor translation inaccuracies.

## Support

The support form is at `https://nvh.evdiag.net/support/`, and every page links
to it. It is English only by deliberate choice — one page to keep correct
rather than thirty to keep in step. Messages land at `support@evdiag.net`,
which also still works as a plain address.

The FAQ on that page makes factual claims about the app: what the one-time
purchase unlocks, what the Restore buttons are called, and the two-root
ambiguity in 3-Sensor and 3D. If any of those change in the app, change them
there too.
