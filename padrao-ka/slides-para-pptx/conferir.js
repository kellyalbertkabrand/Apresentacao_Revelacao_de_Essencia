// conferir.js — abre cada slide do deck no Chromium com as fontes do KA,
// salva o PNG em <pasta>/png e acusa o que passa da margem ou estoura a caixa.
//
//   node conferir.js <pasta-do-deck> [ids...]
//
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const DECK = path.resolve(process.argv[2] || '.');
const OUT = path.join(DECK, 'png');
const MAP = JSON.parse(fs.readFileSync(path.join(DECK, 'mapa.json'), 'utf8'));
const F = process.env.KA_FONTES || '/home/user/apresentacoes/padrao-ka/fontes';
const face = (w,f) => `@font-face{font-family:Outfit;font-weight:${w};src:url(file://${F}/${f})}`;
const CSS = [face(200,'Outfit1Light.ttf'),face(300,'Outfit1Light.ttf'),face(400,'Outfit1.ttf'),
  face(500,'Outfit1Medium.ttf'),face(600,'Outfit1SemiBold.ttf'),face(700,'Outfit1Bold.ttf'),
  face(800,'Outfit1UltraBold.ttf')].join('\n');

(async () => {
  fs.mkdirSync(OUT, {recursive: true});
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 1920, height: 1080}, deviceScaleFactor: 2});
  let ids = process.argv.slice(3);
  if (!ids.length)
    ids = JSON.parse(fs.readFileSync(path.join(DECK,'project/deck.json'),'utf8')).order;
  for (const id of ids) {
    let html = fs.readFileSync(path.join(DECK, 'project/slides', id + '.html'), 'utf8');
    html = html.replace(/\/_blob\/([0-9a-f]{32})/g, (m, b) =>
      MAP[b] ? 'file://' + path.join(DECK, 'assets', MAP[b]) : 'file:///dev/null');
    const doc = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}
      html,body{margin:0;padding:0}
      aside{display:none}
      section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}
      h1,h2,h3,p{margin:0}
      </style></head><body>${html}</body></html>`;
    const tmp = path.join(DECK, '_r.html');
    fs.writeFileSync(tmp, doc);
    await page.goto('file://' + tmp, {waitUntil: 'load'});
    await page.waitForTimeout(250);
    await page.screenshot({path: path.join(OUT, id + '.png')});
    const over = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('section *').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) return;
        if (el.scrollWidth > el.clientWidth + 1 && el.clientWidth > 0)
          out.push('LARGURA ' + el.tagName + ' ' + el.clientWidth + '<' + el.scrollWidth +
                   ' :: ' + (el.textContent || '').trim().slice(0, 30));
        if (r.bottom > 1081 || r.right > 1921 || r.top < -1 || r.left < -1)
          out.push(el.tagName + ' ' + Math.round(r.left) + ',' + Math.round(r.top) + ' ' +
                   Math.round(r.width) + 'x' + Math.round(r.height) + ' :: ' +
                   (el.textContent || '').trim().slice(0, 40));
      });
      return out;
    });
    console.log(id, over.length ? 'VAZA -> ' + over.join(' | ') : 'ok');
  }
  await browser.close();
})();
