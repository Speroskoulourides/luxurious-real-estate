from pathlib import Path

p = Path('golden-visa/index.html')
s = p.read_text(encoding='utf-8')

old_link = '<a href="#" class="zh-button" data-lang="zh">中文</a>'
new_link = '<a href="/golden-visa/?lang=zh" class="zh-button" data-lang="zh">中文</a>'
if old_link in s:
    s = s.replace(old_link, new_link, 1)
elif new_link not in s:
    raise SystemExit('Chinese language link not found')

lock_script = '''<script id="snk-golden-visa-zh-lock">
(()=>{
  if(new URLSearchParams(window.location.search).get('lang')!=='zh') return;
  let busy=false;
  const applyZh=()=>{
    if(busy) return;
    busy=true;
    document.documentElement.lang='zh-CN';
    Object.entries(translations).forEach(([selector,text])=>{
      const el=document.querySelector(selector);
      if(el && el.innerHTML!==text[1]) el.innerHTML=text[1];
    });
    busy=false;
  };
  const start=()=>{
    applyZh();
    new MutationObserver(()=>applyZh()).observe(document.body,{subtree:true,childList:true,characterData:true});
  };
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',start,{once:true});
  else start();
})();
</script>
'''

if 'id="snk-golden-visa-zh-lock"' not in s:
    if '</body>' not in s:
        raise SystemExit('Closing body tag not found')
    s = s.replace('</body>', lock_script + '</body>', 1)

p.write_text(s, encoding='utf-8')
