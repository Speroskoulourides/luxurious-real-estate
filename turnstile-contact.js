
(() => {
  const form = document.getElementById('snkInvestorForm');
  if (!form) return;

  const button = document.getElementById('snkSubmitButton');
  const status = document.getElementById('snkFormStatus');
  const started = document.getElementById('snkFormStartedAt');
  const frame = document.querySelector('iframe[name="snkHiddenSubmitFrame"]');
  const turnstile = form.querySelector('.cf-turnstile');
  const lang = (document.documentElement.lang || 'en').toLowerCase().split('-')[0];
  const messages = {
    en: {
      sending: 'Sending your enquiry…',
      success: 'Thank you. Your enquiry has been received and SNK Real Estate will contact you shortly.',
      error: 'Your enquiry could not be sent. Please try again or contact investments@snkrealestate.com.'
    },
    el: {
      sending: 'Αποστολή του αιτήματός σας…',
      success: 'Ευχαριστούμε. Το αίτημά σας ελήφθη και η SNK Real Estate θα επικοινωνήσει σύντομα μαζί σας.',
      error: 'Το αίτημα δεν μπόρεσε να αποσταλεί. Παρακαλώ δοκιμάστε ξανά ή επικοινωνήστε στο investments@snkrealestate.com.'
    },
    fr: {
      sending: 'Envoi de votre demande…',
      success: 'Merci. Votre demande a bien été reçue et SNK Real Estate vous contactera prochainement.',
      error: 'La demande n\'a pas pu être envoyée. Veuillez réessayer ou contacter investments@snkrealestate.com.'
    },
    es: {
      sending: 'Enviando su consulta…',
      success: 'Gracias. Hemos recibido su consulta y SNK Real Estate se pondrá en contacto con usted en breve.',
      error: 'No se pudo enviar la consulta. Inténtelo de nuevo o contacte con investments@snkrealestate.com.'
    },
    zh: {
      sending: '正在发送您的咨询…',
      success: '感谢您。我们已收到您的咨询，SNK Real Estate 将很快与您联系。',
      error: '您的咨询未能发送。请重试或联系 investments@snkrealestate.com。'
    }
  };
  const msg = messages[lang] || messages.en;
  const setStarted = () => { if (started) started.value = String(Date.now()); };
  const setStatus = (text) => {
    if (!status) return;
    status.hidden = false;
    status.textContent = text;
  };

  if (turnstile) turnstile.remove();
  form.action = 'https://script.google.com/macros/s/AKfycbzu85eEupba-TbVPBW2ZK4_phDFODMpzcE8t6tP5rmE0IG9bJYSFLvO9KHdreiq2nvePA/exec';
  form.method = 'POST';
  form.target = 'snkHiddenSubmitFrame';
  setStarted();

  form.addEventListener('submit', () => {
    if (button) {
      button.disabled = true;
      button.dataset.originalText = button.dataset.originalText || button.textContent;
    }
    setStatus(msg.sending);
  });

  window.addEventListener('message', (event) => {
    if (frame && event.source !== frame.contentWindow) return;
    const data = event.data || {};
    if (data.source !== 'snk-form') return;

    if (data.ok) {
      setStatus(msg.success);
      form.reset();
    } else {
      setStatus(msg.error);
    }

    if (button) button.disabled = false;
    setStarted();
  });
})();
