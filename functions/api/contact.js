const APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbwZA8TyuMbwKy2PO7zK1pvycVJf4htzf3umHRy7rMJbVpeOJH6Q4f1IDm066F63XmBFzQ/exec';

const allowedOrigin = (origin) => {
  if (origin === 'https://snkrealestate.com' || origin === 'https://www.snkrealestate.com') return origin;
  try {
    const host = new URL(origin).hostname;
    if (host === 'luxurious-real-estate.pages.dev' || host.endsWith('.luxurious-real-estate.pages.dev')) return origin;
  } catch (_) {}
  return '';
};

const responseHeaders = (request) => {
  const origin = allowedOrigin(request.headers.get('Origin') || '');
  return {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'x-content-type-options': 'nosniff',
    ...(origin ? {
      'access-control-allow-origin': origin,
      'access-control-allow-methods': 'POST, OPTIONS',
      'access-control-allow-headers': 'content-type',
      'vary': 'Origin'
    } : {})
  };
};

const json = (request, body, status = 200) => new Response(JSON.stringify(body), {
  status,
  headers: responseHeaders(request)
});

export function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: responseHeaders(request) });
}

export async function onRequestPost({ request, env }) {
  if (!env.TURNSTILE_SECRET_KEY) return json(request, { ok: false, error: 'server_not_configured' }, 503);

  const form = await request.formData();
  if (String(form.get('website') || '').trim()) return json(request, { ok: true });

  const startedAt = Number(form.get('formStartedAt'));
  if (!Number.isFinite(startedAt) || Date.now() - startedAt < 2500) {
    return json(request, { ok: false, error: 'submission_too_fast' }, 400);
  }

  const token = String(form.get('cf-turnstile-response') || '');
  if (!token) return json(request, { ok: false, error: 'verification_required' }, 400);

  const verifyBody = new FormData();
  verifyBody.set('secret', env.TURNSTILE_SECRET_KEY);
  verifyBody.set('response', token);
  const ip = request.headers.get('CF-Connecting-IP');
  if (ip) verifyBody.set('remoteip', ip);

  
    method: 'POST',
    body: verifyBody
  });
  const verification = await verifyResponse.json();
  if (!verification.success) return json(request, { ok: false, error: 'verification_failed' }, 403);

  form.delete('cf-turnstile-response');
  const upstream = await fetch(APPS_SCRIPT_URL, {
    method: 'POST',
    body: form,
    redirect: 'follow'
  });
  if (!upstream.ok) return json(request, { ok: false, error: 'delivery_failed' }, 502);

  return json(request, { ok: true });
}
