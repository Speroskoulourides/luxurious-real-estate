// SNK contact form: Cloudflare Turnstile verification and Pages Function submission.
(() => {
  const form = document.getElementById('snkInvestorForm');
  if (!form) return;

  const button = document.getElementById('snkSubmitButton');
  const status = document.getElementById('snkFormStatus');
  const started = document.getElementById('snkFormStartedAt');
  const lang = document.documentElement.lang || 'en';
  const messages = {
    en: {
      verify: 'Please complete the human verification.',
      sending: 'Sending your enquiry…',
      success: 'Thank you. Your enquiry has been received and SNK Real Estate will contact you shortly.',
      error: 'Your enquiry could not be sent. Please try again or contact investments@snkrealestate.com.'
    },
    el: {
      verify: 'Παρακαλώ ολοκληρώστε την επιβεβαίωση ανθρώπου.',
      sending: 'Αποστολή του αιτήματός σας…',
      success: 'Ευχαριστούμε. Το αίτημά σας ελήφθη και η SNK Real Estate θα επικοινωνήσει σύντομα μαζί σας.',
      error: 'Το αίτημα δεν μπόρεσε να αποσταλεί. Παρακαλώ δοκιμάστε ξανά ή επικοινωνήστε στο investments@snkrealestate.com.'
    },
    fr: {
      verify: 'Veuillez terminer la vérification humaine.',
      sending: 'Envoi de votre demande…',
      success: 'Merci. Votre demande a bien été reçue et SNK Real Estate vous contactera prochainement.',
      error: 'La demande n\'a pas pu être envoyée. Veuillez réessayer ou contacter investments@snkrealestate.com.'
    },
    es: {
      verify: 'Complete la verificación humana.',
      sending: 'Enviando su consulta…',
      success: 'Gracias. Hemos recibido su consulta y SNK Real Estate se pondrá en contacto con usted en breve.',
      error: 'No se pudo enviar la consulta. Inténtelo de nuevo o contacte con investments@snkrealestate.com.'
    }
  };
  const msg = messages[lang] || messages.en;
  const setStarted = () => { if (started) started.value = String(Date.now()); };
  const setStatus = (text) => {
    if (!status) return;
    status.hidden = false;
    status.textContent = text;
  };

  setStarted();
  form.removeAttribute('target');
  form.action = '/api/contact';

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    if (!data.get('cf-turnstile-response')) {
      setStatus(msg.verify);
      return;
    }

    if (button) button.disabled = true;
    setStatus(msg.sending);

    try {
      const endpoint = window.location.hostname.endsWith('.pages.dev')
        ? '/api/contact'
        : 'https://luxurious-real-estate.pages.dev/api/contact';
      const response = await fetch(endpoint, { method: 'POST', body: data });
      const result = await response.json();
      if (!response.ok || !result.ok) throw new Error(result.error || 'submission_failed');
      setStatus(msg.success);
      form.reset();
    } catch (_) {
      setStatus(msg.error);
    } finally {
      if (window.turnstile) window.turnstile.reset();
      if (button) button.disabled = false;
      setStarted();
    }
  });
})();
