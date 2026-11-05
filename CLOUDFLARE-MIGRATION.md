# Moving nvh.evdiag.net from GitHub Pages to Cloudflare Pages

This replaces `HOSTING-SETUP.md`, which describes the original GitHub Pages
setup and is kept only for history.

Nothing in this repository changes shape. The same files stay in the same
places, GitHub Pages keeps working while you set Cloudflare up, and the
switch-over is one DNS change you can undo in a minute.

---

## Why

The support form at `/support/` sends mail through Resend, and Resend needs an
API key. A key in the browser is a key anybody can read and use to send mail
as `evdiag.net`, so the send has to happen on a server. GitHub Pages serves
static files and nothing else — there is no server to put the key on.

Cloudflare Pages serves the same static files *and* runs small functions
beside them. `functions/api/contact.js` becomes `POST /api/contact`
automatically, the key lives there as an encrypted environment variable, and
the browser only ever sees the form.

This is exactly how clutch.evdiag.net already works, so after this there is one
setup to remember instead of two, and a fix to one contact form is worth
porting to the other.

---

## What is already in the repository

| Path | What it is |
|---|---|
| `functions/api/contact.js` | the function. Reads the form, sends it through Resend |
| `_routes.json` | tells Cloudflare only `/api/*` needs the function. Every other request is served as a plain file, which is faster and cheaper |
| `support/index.html` | the support page: form plus FAQ |
| `support.js` | the form's behaviour. Posts JSON to `/api/contact` |
| `style.css` | gained a `.contact` block at the end. Nothing else in it changed |
| `test-contact.mjs` | offline test of the function. `node test-contact.mjs` |

Every page footer now links to `/support/` as well as the support address.

---

## Setting it up

### 1. Create the Pages project

Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** →
**Connect to Git** → pick `EVDiag/nvh-docs`.

| Setting | Value |
|---|---|
| Production branch | `main` |
| Framework preset | **None** |
| Build command | *leave empty* |
| Build output directory | `/` |
| Root directory | `/` |

The build output is the repository root because the HTML is committed, not
generated — there is no build step. Cloudflare finds `functions/` by itself.

It will deploy and give you an address like
`https://nvh-docs.pages.dev`. **Open it and check the site before going
further.** The DNS still points at GitHub at this stage, so nothing is live yet
and nothing is at risk.

### 2. Resend

The domain `evdiag.net` is already verified in Resend from the clutch site, so
there is nothing to add there. You only need a key:

**API Keys → Create API Key**, sending permission only. Copy it once — it is
not shown again. You can reuse the clutch key instead if you prefer one key for
both sites; a separate key is tidier if you ever want to revoke one.

### 3. Environment variables

Pages project → **Settings → Environment variables** → **Production**:

| Variable | Value | Secret |
|---|---|---|
| `RESEND_API_KEY` | the key from step 2 | **yes** — use the Encrypt button |
| `CONTACT_TO` | `support@evdiag.net` | no |
| `CONTACT_FROM` | optional. Defaults to `NVH Source Locator <noreply@evdiag.net>`. Must be on a domain verified in Resend | no |

Add them to **Preview** too if you want the form to work on preview branches.

**Redeploy after adding them.** Pages reads environment variables at build
time, so variables added after a deployment are not in it.

Until `RESEND_API_KEY` and `CONTACT_TO` both exist, the form answers "The
contact form is not configured yet. Please email us directly." It never fails
silently.

### 4. Test the form before the cutover

On the `pages.dev` address, send yourself a message through `/support/`. It
should arrive at `support@evdiag.net` with the subject
`[NVH Source Locator] <topic> - <name>`, and hitting Reply should answer the
sender, not you.

If it does not arrive and the page still said "Thank you", look at
[resend.com/emails](https://resend.com/emails) first: an address that bounced
once goes on Resend's suppression list, and every later send to it is skipped
while the API still reports success.

### 5. The cutover

Pages project → **Custom domains** → **Set up a custom domain** →
`nvh.evdiag.net`.

`evdiag.net` is on Cloudflare DNS, so Cloudflare rewrites the record itself:
the `nvh` CNAME stops pointing at `evdiag.github.io` and starts pointing at the
Pages project. HTTPS is issued automatically, usually within a couple of
minutes.

Then in GitHub → `EVDiag/nvh-docs` → **Settings → Pages**, set Source to
**None** so the two are not both claiming the name. Do this after the custom
domain is working, not before.

The `CNAME` file in the repository root is GitHub's. Cloudflare ignores it, and
it will simply be served as a text file at `/CNAME`. Leaving it costs nothing
and is what makes the rollback below a one-step job; delete it later if you
want to be tidy.

### 6. Check

- `https://nvh.evdiag.net/` — the language picker, with the video
- `https://nvh.evdiag.net/en/user-guide.html` — a manual page
- `https://nvh.evdiag.net/support/` — the form, sent for real this time
- `https://nvh.evdiag.net/media/nvh-tdoa.mp4` — the video file itself

The app's in-app manual links and the store listings all point at
`nvh.evdiag.net`, so they keep working: the address is unchanged, only what
answers it is different.

---

## Rolling back

Nothing in the repository was restructured, so GitHub Pages can serve it again
exactly as it is:

1. GitHub → **Settings → Pages** → Source: **Deploy from a branch**, `main`, `/`
2. Cloudflare → the Pages project → **Custom domains** → remove
   `nvh.evdiag.net`
3. Cloudflare → **DNS** for `evdiag.net` → the `nvh` CNAME back to
   `evdiag.github.io`, DNS only (grey cloud)

The site is back within DNS propagation, a few minutes. You lose the support
form, which GitHub Pages cannot run, and nothing else.

---

## Working on it afterwards

Push to `main` and Cloudflare redeploys, same as GitHub Pages did. Push to any
other branch and you get a preview at
`https://<branch>.<project>.pages.dev`, listed under the project's Deployments.

```bash
node test-contact.mjs              # the function, offline. Prints CONTACT FUNCTION OK
npx wrangler pages dev .           # the whole site and the function, locally
```

For `wrangler pages dev` to actually send, put the two variables in a
`.dev.vars` file at the repository root:

```
RESEND_API_KEY=re_...
CONTACT_TO=support@evdiag.net
```

`.dev.vars` is in `.gitignore`. Never commit it.

---

## Spam

The form has a hidden field a person never sees. A bot that fills it in gets
`[Possible spam]` in the subject — the message still arrives, because browser
password managers fill hidden fields too, and silently binning a real message
is much worse than reading one marked message.

If real spam starts arriving, switch on
[Turnstile](https://dash.cloudflare.com/?to=/:account/turnstile): create a
widget for `nvh.evdiag.net`, put its secret in the Pages project as
`TURNSTILE_SECRET` (encrypted), and add its site key to the form. The function
checks the token only when `TURNSTILE_SECRET` is set, so until then it is
switched off and out of the way. Add the site key and the secret together: with
only the secret set, every message is refused.

---

## One thing worth knowing

Cloudflare now points new projects at Workers Static Assets rather than Pages,
and says Pages "continues to work" while new features go to Workers. Pages is
still the right choice here: clutch.evdiag.net is already on it, the function
file layout is identical, and keeping one setup for both sites is worth more
than being on the newer product. If that ever changes, Cloudflare has a
migration path from Pages to Workers and the function moves across largely
unchanged.
