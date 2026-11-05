/* Support form on /support/.
 *
 * Posts JSON to /api/contact, which is a Cloudflare Pages Function. The Resend
 * API key lives there as an encrypted environment variable and never reaches
 * the browser — which is the whole reason this site moved off GitHub Pages.
 *
 * Mirrors the handler on clutch.evdiag.net so both sites behave the same.
 */
(function () {
  var form = document.getElementById('contactForm');
  if (!form) return;

  var btn = document.getElementById('submitBtn');
  var msg = document.getElementById('formMsg');

  function say(kind, text) {
    msg.className = 'formmsg show ' + kind;
    msg.textContent = text;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var data = {
      name: form.name.value,
      email: form.email.value,
      topic: form.topic.value,
      message: form.message.value,
      hp_check: form.hp_check.value,
      // Which manual page they came from. Tells us the language they were
      // reading in, which is often the fastest clue to what they mean.
      fromPage: document.referrer || ''
    };

    if (!data.name || !data.email || !data.message) {
      say('bad', 'Please fill in your name, email and message.');
      return;
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(data.email)) {
      say('bad', 'That email address does not look right.');
      return;
    }
    if (data.message.trim().length < 10) {
      say('bad', 'Please add a little more detail so we can help.');
      return;
    }

    btn.disabled = true;
    var label = btn.textContent;
    btn.textContent = 'Sending…';
    msg.className = 'formmsg';

    fetch('/api/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
      .then(function (r) {
        return r.json().then(function (j) { return { ok: r.ok, body: j }; });
      })
      .then(function (res) {
        if (res.ok && res.body.ok) {
          form.reset();
          say('good', 'Thank you — your message is on its way. We usually reply within a working day.');
        } else {
          say('bad', (res.body && res.body.error) ||
            'We could not send that just now. Please email support@evdiag.net directly.');
        }
      })
      .catch(function () {
        say('bad', 'We could not send that just now. Please email support@evdiag.net directly.');
      })
      .then(function () {
        btn.disabled = false;
        btn.textContent = label;
      });
  });
})();
