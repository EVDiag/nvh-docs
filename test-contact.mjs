/* Offline test of functions/api/contact.js — no network, no Cloudflare.
   Stubs global fetch so the Resend request can be inspected. */
import { onRequestPost, onRequest } from './functions/api/contact.js';

let fail = 0, sent = null;
const ok = (c, m, x) => { console.log((c ? '  PASS  ' : '  FAIL  ') + m + (x ? '   [' + x + ']' : '')); if (!c) fail++; };

const ENV = { RESEND_API_KEY: 're_TESTKEY_should_never_leak', CONTACT_TO: 'support@evdiag.net' };

globalThis.fetch = async (url, init) => {
  sent = { url, init, body: JSON.parse(init.body) };
  return { ok: true, status: 200, json: async () => ({ id: 'msg_123' }), text: async () => '' };
};

const req = (body, headers = {}) => ({
  method: 'POST',
  json: async () => body,
  headers: { get: k => headers[k] ?? null }
});

const GOOD = {
  name: 'Jan Novak', email: 'jan@example.com',
  topic: 'A result looks wrong',
  message: '3-Sensor, 100/90/80 cm, result mirrored across the A-B line.'
};

const call = async (body, headers, env = ENV) => {
  sent = null;
  const res = await onRequestPost({ request: req(body, headers), env });
  return { status: res.status, body: JSON.parse(await res.text()) };
};

console.log('— rejects bad input —');
let r = await call({ ...GOOD, name: '' });
ok(r.status === 400 && !r.body.ok, 'missing name rejected', r.status);
r = await call({ ...GOOD, email: 'not-an-email' });
ok(r.status === 400, 'malformed email rejected', r.body.error);
r = await call({ ...GOOD, message: 'too short' });
ok(r.status === 400, 'message under 10 chars rejected', r.body.error);
ok(sent === null, 'nothing was sent to Resend for any rejected input');

console.log('\n— refuses to pretend when unconfigured —');
r = await call(GOOD, {}, { CONTACT_TO: 'x@y.z' });
ok(r.status === 503 && /not configured/i.test(r.body.error),
   'no API key gives 503 and says so, rather than a silent success');

console.log('\n— happy path —');
r = await call(GOOD, { 'CF-IPCountry': 'CZ', 'CF-Connecting-IP': '1.2.3.4' });
ok(r.status === 200 && r.body.ok === true, 'accepted', 'id ' + r.body.id);
ok(sent.url === 'https://api.resend.com/emails', 'posted to Resend');
ok(sent.init.headers.Authorization === 'Bearer ' + ENV.RESEND_API_KEY, 'key sent as a Bearer header');
ok(!JSON.stringify(sent.body).includes(ENV.RESEND_API_KEY), 'API key is NOT in the message body');
ok(sent.body.reply_to === GOOD.email, 'reply_to is the sender, so Reply answers them');
ok(Array.isArray(sent.body.to) && sent.body.to[0] === 'support@evdiag.net', 'to: support@evdiag.net');
ok(sent.body.from.includes('noreply@evdiag.net'), 'from: a verified evdiag.net address', sent.body.from);
ok(sent.body.subject === '[NVH Source Locator] A result looks wrong - Jan Novak', 'subject', sent.body.subject);
ok(sent.body.text.includes(GOOD.message), 'message body carried through');
ok(sent.body.text.includes('Country: CZ'), 'country recorded');
ok(sent.body.text.includes('nvh.evdiag.net support form'), 'tagged as coming from the NVH site');

console.log('\n— honeypot never silently drops a real message —');
r = await call({ ...GOOD, hp_check: 'Acme Ltd' });
ok(r.status === 200 && r.body.ok === true, 'still delivered');
ok(sent.body.subject.startsWith('[Possible spam] '), 'flagged in the subject', sent.body.subject);
ok(/hidden anti-spam field was filled/.test(sent.body.text), 'and explained in the body');

console.log('\n— hardening —');
r = await call({ ...GOOD, topic: 'Free money!!' });
ok(sent.body.subject.includes('Something else'), 'unknown topic coerced to a known one', sent.body.subject);
r = await call({ ...GOOD, name: 'Jan\r\nBcc: evil@example.com' });
ok(!/[\r\n]/.test(sent.body.subject), 'CRLF in the name cannot inject a mail header', JSON.stringify(sent.body.subject));
r = await call({ ...GOOD, message: 'x'.repeat(9000) });
ok(sent.body.text.indexOf('x'.repeat(5001)) === -1, 'over-long message truncated to 5000');
r = await call({ ...GOOD, fromPage: 'https://nvh.evdiag.net/de/user-guide.html' });
ok(sent.body.text.includes('/de/user-guide.html'), 'referring page recorded, so we know their language');

console.log('\n— method —');
const g = await onRequest({ request: { method: 'GET' } });
ok(g.status === 405, 'GET is refused', g.status);
ok((await onRequest({ request: { method: 'POST' } })) === undefined, 'POST falls through to the real handler');

console.log(fail ? '\n' + fail + ' FAILURE(S)' : '\nCONTACT FUNCTION OK');
process.exit(fail ? 1 : 0);
