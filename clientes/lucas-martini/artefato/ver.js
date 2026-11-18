const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const css = fs.readFileSync('project/deck.css','utf8');
  const blobs = JSON.parse(fs.readFileSync('blobs.json','utf8'));
  const ids = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport:{width:1920,height:1080}, deviceScaleFactor:1});
  let atual = '';
  await p.route('http://ka.local/**', r => {
    const u = new URL(r.request().url());
    if (u.pathname === '/') return r.fulfill({status:200, contentType:'text/html; charset=utf-8', body: atual});
    const id = u.pathname.replace('/_blob/','');
    const f = blobs[id];
    if (!f) { console.log('  ! blob desconhecido', id); return r.abort(); }
    r.fulfill({status:200, contentType:'image/png', body: fs.readFileSync(f)});
  });
  for (const id of ids) {
    const s = fs.readFileSync(`project/slides/${id}.html`,'utf8');
    atual = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400..700&family=DM+Sans:opsz,wght@9..40,300..700&family=Outfit:wght@300..600&display=swap">
<style>html,body{margin:0;padding:0;background:#fff}section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}aside{display:none}
${css}</style></head><body>${s}</body></html>`;
    await p.goto('http://ka.local/', {waitUntil:'networkidle'});
    await p.screenshot({path:`../prev-${id}.png`});
    const fora = await p.evaluate(() => {
      const r=[];
      document.querySelectorAll('section *').forEach(e=>{
        if (e.classList.contains('capa-arte')||e.classList.contains('div-foto')||
            e.classList.contains('trama')||e.classList.contains('agua')||
            e.classList.contains('trilho')||e.closest('.trilho')||e.tagName==='ASIDE') return;
        const x=e.getBoundingClientRect();
        if(x.bottom>971||x.right>1748.5||x.left<109) r.push(`${e.className||e.tagName}(b${x.bottom.toFixed(0)} l${x.left.toFixed(0)} r${x.right.toFixed(0)})`);
      });
      return r;});
    console.log(' ', id, fora.length? 'FORA: '+fora.slice(0,4).join(' ') : 'ok');
  }
  await b.close();
})();
