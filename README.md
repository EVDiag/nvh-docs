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
├── README.md               ← this file
├── HOSTING-SETUP.md        ← how to publish on custom domain
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

## How to publish

See `HOSTING-SETUP.md` for the step-by-step setup of a custom domain like `https://nvh.evdiag.net/`. Summary:

1. Copy this entire folder into `evdiag-pages/nvh/`
2. Push to GitHub
3. Add CNAME DNS record at your domain registrar
4. Done — accessible at your clean URL within 30 minutes

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

For documentation issues or corrections, contact `support@evdiag.net`.
