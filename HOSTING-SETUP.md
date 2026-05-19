# Hosting setup — custom domain, no "github" in URL, PDF download

You want the docs hosted at a URL like `https://nvh.evdiag.net/user-guide.html` (or similar), with no "github" word visible, and a PDF download button. This is exactly the setup used by sites like https://bloomdays.family/privacy.html — GitHub Pages with a custom domain.

## Total cost

- **$10-15/year** for a domain (or $0 if using a subdomain of evdiag.net which you may already own)
- **$0** for hosting (GitHub Pages is free for public repos)
- **$0** for PDF download (we generate it once and commit it)

---

## Architecture

```
┌─────────────────────────────────┐
│  evdiag-pages repo (PUBLIC)     │
│  on GitHub                       │
│  ┌──────────────────────────┐    │
│  │ /nvh/user-guide.html     │    │
│  │ /nvh/quick-reference.html│    │
│  │ /nvh/user-guide.pdf      │    │
│  │ /nvh/screenshots/*.svg   │    │
│  └──────────────────────────┘    │
└─────────────────────────────────┘
              │
              │ served by GitHub Pages
              ▼
   evdiag.github.io/evdiag-pages/...
              │
              │ DNS CNAME redirect
              ▼
   nvh.evdiag.net/user-guide.html  ← what the user sees
```

The user's URL has no "github" in it. They can download the PDF with one click.

---

## Step-by-step setup

### Step 1: Decide your URL

Pick a subdomain of a domain you already own, or buy a new one:

**Option A — subdomain of evdiag.net** (you probably already own this)
- `nvh.evdiag.net` — clean, branded
- `docs.evdiag.net` — works for multiple products
- `manual.evdiag.net` — descriptive

**Option B — new dedicated domain**
- Buy at any registrar (Namecheap, Cloudflare, Porkbun, GoDaddy)
- Something like `nvh-locator.com` or `evdiag-docs.com`
- ~$10-15/year

I recommend **Option A** with `nvh.evdiag.net` — uses your existing domain, free, professional.

### Step 2: Convert markdown to HTML

The markdown files need to become HTML for browser rendering. Use Pandoc (free tool):

**Install Pandoc** (one-time):
- Windows: download from https://pandoc.org/installing.html
- Or use `winget install pandoc`

**Convert the files**:
```powershell
cd C:\path\to\nvh-docs

# Convert markdown to HTML with embedded CSS
pandoc user-guide.md -o user-guide.html `
  --standalone `
  --metadata title="NVH Source Locator — User Guide" `
  --css=style.css

pandoc quick-reference.md -o quick-reference.html `
  --standalone `
  --metadata title="NVH Source Locator — Quick Reference" `
  --css=style.css
```

You'll also want a small `style.css` for clean appearance — see below.

### Step 3: Generate PDF from markdown

Also using Pandoc, with a LaTeX backend for nice PDFs:

```powershell
# Install MiKTeX once for the LaTeX backend
# https://miktex.org/download

pandoc user-guide.md -o user-guide.pdf `
  --pdf-engine=xelatex `
  --variable=geometry:margin=2cm

pandoc quick-reference.md -o quick-reference.pdf `
  --pdf-engine=xelatex `
  --variable=geometry:margin=2cm
```

The PDFs will include the SVG screenshots inline. Commit them to the repo so users can download.

**Alternative if Pandoc/LaTeX is too heavy**: just print the HTML to PDF from your browser. Open the .html file in Chrome → Ctrl+P → Save as PDF. Less polished but works.

### Step 4: Add download button to the HTML

Edit each `.html` file and add a download button near the top. Look for the `<body>` opening and insert:

```html
<div style="background:#0F3460;color:#FFFFFF;padding:12px;text-align:center;border-radius:8px;margin-bottom:24px;">
  <a href="user-guide.pdf" download style="color:#00B4D8;text-decoration:none;font-weight:600;">
    📥 Download as PDF
  </a>
</div>
```

(Repeat for `quick-reference.html` pointing at `quick-reference.pdf`.)

### Step 5: Create style.css

Create `style.css` in the docs folder with clean styling:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  max-width: 800px;
  margin: 40px auto;
  padding: 0 24px;
  color: #222;
  line-height: 1.65;
}
h1, h2, h3 {
  color: #0F3460;
}
h1 {
  border-bottom: 2px solid #00B4D8;
  padding-bottom: 8px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
}
th, td {
  text-align: left;
  padding: 8px 12px;
  border-bottom: 1px solid #E5E7EB;
}
th {
  background: #F8FAFC;
  font-weight: 600;
}
code, pre {
  font-family: "Courier New", monospace;
  background: #F8FAFC;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 90%;
}
img, svg {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 16px auto;
  border: 1px solid #E5E7EB;
  border-radius: 6px;
}
blockquote {
  border-left: 3px solid #00B4D8;
  margin: 16px 0;
  padding: 8px 16px;
  background: #F8FAFC;
}
a {
  color: #00B4D8;
}
```

### Step 6: Copy files into evdiag-pages repo

You already have `evdiag-pages` repo set up with GitHub Pages working (it hosts `promo.html`). Add the docs alongside:

```powershell
cd C:\Users\rfmot\evdiag-pages

# Create nvh subfolder
mkdir nvh
mkdir nvh\screenshots

# Copy files
copy C:\path\to\nvh-docs\user-guide.html nvh\
copy C:\path\to\nvh-docs\quick-reference.html nvh\
copy C:\path\to\nvh-docs\user-guide.pdf nvh\
copy C:\path\to\nvh-docs\quick-reference.pdf nvh\
copy C:\path\to\nvh-docs\style.css nvh\
copy C:\path\to\nvh-docs\screenshots\*.svg nvh\screenshots\

# Commit and push
git add nvh/
git commit -m "feat: add NVH Source Locator user guide and quick reference"
git push origin main
```

After ~1-2 minutes, GitHub Pages will rebuild and the docs will be live at:
`https://evdiag.github.io/evdiag-pages/nvh/user-guide.html`

But that has "github" in the URL. Next step fixes that.

### Step 7: Set up custom domain (DNS CNAME)

This is the step that removes "github" from the URL.

**A. Add CNAME file to the repo**

In `evdiag-pages` repo root, create a file called `CNAME` (no extension, all caps):

```
nvh.evdiag.net
```

That's the entire file content — just your chosen subdomain. Commit and push.

**B. Configure DNS at your domain registrar**

Go to wherever `evdiag.net` is registered. Add a CNAME record:

| Type | Name | Value | TTL |
|---|---|---|---|
| CNAME | `nvh` | `evdiag.github.io.` | 3600 |

(The trailing dot in `evdiag.github.io.` is sometimes required, sometimes not — depends on registrar interface.)

DNS propagation usually takes 5-30 minutes. Sometimes a few hours.

**C. Enable HTTPS in GitHub Pages settings**

After DNS propagates:

1. Go to your repo → Settings → Pages
2. Custom domain should auto-populate with `nvh.evdiag.net`
3. Check **"Enforce HTTPS"** (may take 5-30 min to provision SSL certificate)

### Step 8: Verify

Visit `https://nvh.evdiag.net/nvh/user-guide.html` in an incognito browser.

You should see:
- Clean URL with no "github" word
- The user guide rendered with your CSS
- Working **Download as PDF** button
- All screenshots showing as SVG

---

## Sharing the link

For the app stores:

**Google Play Console** → app listing → set "User support URL" or "Support email" with `https://nvh.evdiag.net/nvh/user-guide.html`

**Apple App Store Connect** → app information → "Marketing URL" or "Support URL" with the same.

For in-app linking, you could add a Help button in the app that opens this URL. But that's a future enhancement — not needed today.

---

## Maintenance workflow

When you want to update the docs:

1. Edit the markdown files
2. Run pandoc to regenerate HTML and PDF
3. Copy updated files to `evdiag-pages/nvh/`
4. Git commit + push
5. GitHub Pages auto-deploys within 1-2 minutes
6. The URL stays the same — users always get the latest version

You can also use tags (like we did for promo.html versions) to snapshot known-good states.

---

## Simpler alternative (no pandoc, manual conversion)

If installing Pandoc feels like too much, here's a simpler path:

1. Open each markdown file in **GitHub** (yes, on the github.com UI)
2. View the rendered output
3. Right-click → Print → Save as PDF
4. Use a tool like `pandoc.online` (browser-based) or `marked2` to generate HTML

You lose some polish but it works without installing anything. Then you only commit the .md, .html, and .pdf files.

---

## Decision tree

**Want the simplest possible setup?**
→ Skip custom domain. Just commit the .md files to evdiag-pages, share the github.io URL. Users see "github" in URL but it works.

**Want clean URL but minimal effort?**
→ Set up CNAME (Step 7) only. Skip pandoc, just commit .md files. GitHub renders markdown automatically. URL becomes `nvh.evdiag.net/nvh/user-guide.md`.

**Want full polish (recommended)?**
→ All 8 steps above. Best result, maintainable, ~1 hour to set up initially, ~5 min per update afterward.

---

## What I can do for you now

I've created the screenshots and markdown files. The remaining steps (Pandoc installation, DNS configuration, custom domain setup) need to be done on YOUR machine and through YOUR domain registrar — I can't reach those.

If you want, I can:
- Generate the HTML files now (using a basic Python-based markdown→HTML converter that doesn't need Pandoc)
- Generate a basic CSS file
- Provide the exact commands to copy/paste

Or I can stop here and you take it from this point.

Tell me which:
- **Continue to HTML/CSS now** — I generate ready-to-host files
- **Stop at markdown** — you handle the rest manually with your preferred tools
