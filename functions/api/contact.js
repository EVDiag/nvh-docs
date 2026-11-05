/**
 * POST /api/contact — Cloudflare Pages Function.
 *
 * Takes the support form on /support/ and sends it to the inbox through Resend.
 * Adapted from the same function on clutch.evdiag.net, so both sites behave
 * identically and a fix to one is worth porting to the other.
 *
 * Environment variables (Cloudflare -> Pages project -> Settings -> Environment variables):
 *   RESEND_API_KEY     required — from resend.com/api-keys
 *   CONTACT_TO         required — where messages land, e.g. support@evdiag.net
 *   CONTACT_FROM       optional — must be on a domain verified in Resend.
 *                                 Defaults to "NVH Source Locator <noreply@evdiag.net>"
 *   TURNSTILE_SECRET   optional — if set, the form must send a Turnstile token.
 *                                 Leave it unset and that check is skipped.
 */

const MAX = { name: 120, email: 200, topic: 60, message: 5000, context: 200 };
const TOPICS = new Set([
  'A question', 'Something is wrong / a bug', 'Feature request',
  'A result looks wrong', 'Material or speed-of-sound data',
  'Purchase or restore', 'Something else'
]);

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }
  });

// Strip control characters, then trim and cap the length.
const CONTROL_CHARS = /[\u0000-\u001F\u007F]/g;
const clean = (v, max) =>
  typeof v === 'string' ? v.replace(CONTROL_CHARS, '').trim().slice(0, max) : '';

// Deliberately permissive: rejecting unusual but valid addresses annoys real
// people, and a wrong address only costs us an undeliverable reply.
const emailLooksReal = e => /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(e) && e.length <= MAX.email;

// A header value containing a newline could inject extra mail headers.
const safeHeader = s => s.replace(/[\r\n]+/g, ' ').trim();

async function turnstileOk(env, token, ip) {
  if (!env.TURNSTILE_SECRET) return true;          // not configured, not enforced
  if (!token) return false;
  const form = new FormData();
  form.append('secret', env.TURNSTILE_SECRET);
  form.append('response', token);
  if (ip) form.append('remoteip', ip);
  try {
    const r = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',
      { method: 'POST', body: form });
    const d = await r.json();
    return d.success === true;
  } catch {
    return false;
  }
}

export async function onRequestPost({ request, env }) {
  if (!env.RESEND_API_KEY || !env.CONTACT_TO) {
    return json({ ok: false, error: 'The contact form is not configured yet. Please email us directly.' }, 503);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: 'Could not read that request.' }, 400);
  }

  // Hidden anti-spam field. A person never sees it, so a value here usually
  // means a bot — but browser autofill and password managers fill hidden
  // fields too, which on the clutch site silently threw real messages away
  // until Oct 2026. So a filled field never drops anything: the message is
  // delivered with "[Possible spam]" in the subject and a person decides.
  const trap = clean(body.hp_check, MAX.context);

  const name = clean(body.name, MAX.name);
  const email = clean(body.email, MAX.email);
  const rawTopic = clean(body.topic, MAX.topic);
  const topic = TOPICS.has(rawTopic) ? rawTopic : 'Something else';
  const message = clean(body.message, MAX.message);

  // Optional, and worth having: which page they came from tells us which
  // language the manual was in when they hit the problem.
  const fromPage = clean(body.fromPage, MAX.context);

  if (!name || !email || !message) {
    return json({ ok: false, error: 'Please fill in your name, email and message.' }, 400);
  }
  if (!emailLooksReal(email)) {
    return json({ ok: false, error: 'That email address does not look right.' }, 400);
  }
  if (message.length < 10) {
    return json({ ok: false, error: 'Please add a little more detail so we can help.' }, 400);
  }

  const ip = request.headers.get('CF-Connecting-IP') || '';
  if (!(await turnstileOk(env, body.turnstileToken, ip))) {
    return json({ ok: false, error: 'Spam check failed. Please reload the page and try again.' }, 400);
  }

  const country = request.headers.get('CF-IPCountry') || 'unknown';
  const text = [
    message, '', '---',
    'From:    ' + name + ' <' + email + '>',
    'Topic:   ' + topic,
    'Country: ' + country,
    ...(fromPage ? ['Page:    ' + fromPage] : []),
    'Sent:    ' + new Date().toISOString(),
    'Via:     nvh.evdiag.net support form',
    ...(trap ? ['Note:    the hidden anti-spam field was filled in (' + JSON.stringify(trap) +
                '), so this may be a bot, or browser autofill.'] : [])
  ].join('\n');

  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: 'Bearer ' + env.RESEND_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: env.CONTACT_FROM || 'NVH Source Locator <noreply@evdiag.net>',
        // CONTACT_TO may list several addresses, comma separated.
        to: String(env.CONTACT_TO).split(',').map(a => a.trim()).filter(Boolean),
        reply_to: email,                       // hitting Reply answers the sender
        subject: (trap ? '[Possible spam] ' : '') +
                 '[NVH Source Locator] ' + safeHeader(topic) + ' - ' + safeHeader(name),
        text
      })
    });

    if (!res.ok) {
      console.error('Resend rejected the message:', res.status, await res.text());
      return json({ ok: false, error: 'We could not send that just now. Please email us directly.' }, 502);
    }
    let id = null;
    try { id = (await res.json()).id || null; } catch {}
    console.log('Support message accepted by Resend:', id, trap ? '(flagged: hidden field filled)' : '');
    return json({ ok: true, id });
  } catch (err) {
    console.error('Contact form failed:', err);
    return json({ ok: false, error: 'We could not send that just now. Please email us directly.' }, 502);
  }
}

// Anything that is not a POST
export async function onRequest({ request }) {
  if (request.method === 'POST') return;         // handled by onRequestPost
  return json({ ok: false, error: 'Method not allowed.' }, 405);
}
