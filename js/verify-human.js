document.addEventListener("DOMContentLoaded", function(){
  const lang = document.documentElement.lang || 'en';
  let text = "Verify you are human";
  if(lang.startsWith('el')) text = "Επιβεβαιώστε ότι είστε άνθρωπος";
  if(lang.startsWith('es')) text = "Verifica que eres humano";
  if(lang.startsWith('fr')) text = "Vérifiez que vous êtes humain";

  document.querySelectorAll('form').forEach(form => {
    const box = document.createElement('div');
    box.innerHTML = `
      <div style="border:1px solid #D4AF37; padding:12px; margin:15px 0; border-radius:6px; background:#faf8f5; display:flex; gap:8px; align-items:center; font-family:Montserrat,sans-serif;">
        <input type="checkbox" required style="width:18px;height:18px; accent-color:#1E3A8A;">
        <span>${text}</span>
      </div>
      <input type="text" name="_gotcha" style="display:none">
    `;
    const btn = form.querySelector('button[type=submit], button');
    if(btn) form.insertBefore(box, btn);
    else form.appendChild(box);
  });
});