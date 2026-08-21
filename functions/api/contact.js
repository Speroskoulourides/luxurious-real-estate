const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwZA8TyuMbwKy2PO7zK1pvycVJf4htzf3umHRy7rMJbVpeOJH6Q4f1IDm066F63XmBFzQ/exec';

const json = (body, status = 200) => new Response(JSON.stringify(body), {
  status,
  headers: {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'x-content-type-options': 'nosniff'
  }
});

export async function onRequestPost({ request, env }) {
  if (!env.TURNSTILE_SECRET_KEY) return json({ ok: false, error: 'server_not_configured' }, 503);

  const form = await request.formData();
  if (String(form.get('website') || '').trim()) return json({ ok: true });

  const startedAt = Number(form.get('formStartedAt'));
  if (!Number.isFinite(startedAt) || Date.now() - startedAt < 2500) {
    return json({ ok: false, error: 'submission_too_fast' }, 400);
  }

  const token = String(form.get('cf-turnstile-response') || '');
  if (!token) return json({ ok: false, error: 'verification_required' }, 400);

  const verifyBody = new FormData();
  verifyBody.set('secret', env.TURNSTILE_SECRET_KEY);
  verifyBody.set('response', token);
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) verifyBody.set('remoteip', ip);

  const verifyResponse = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST',
    body: verifyBody
  });
  const verification = await verifyResponse.json();
  if (!verification.success) return json({ ok: false, error: 'verification_failed' }, 403);

  form.delete('cf-turnstile-response');
  const upstream = await fetch(APPS_SCRIPT_URL, {
    method: 'POST',
    body: form,
    redirect: 'follow'
  });
  if (!upstream.ok) return json({ ok: false, error: 'delivery_failed' }, 502);

  return json({ ok: true });
}
