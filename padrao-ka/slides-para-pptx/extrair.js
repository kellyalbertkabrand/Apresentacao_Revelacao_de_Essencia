// extrair.js — le os slides HTML de um deck do Padrao KA (artefato do tipo
// Slides) e mede, no proprio navegador, cada texto, filete e imagem.
//
//   node extrair.js <pasta-do-deck> [ids...]
//
// A pasta precisa ter project/deck.json, project/slides/*.html, assets/ e um
// mapa.json ligando o id de cada blob ao arquivo em assets/. Sem ids, roda a
// ordem inteira do deck. Sai em <pasta>/edit/spec.json.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const DECK = path.resolve(process.argv[2] || '.');
const MAP = JSON.parse(fs.readFileSync(path.join(DECK, 'mapa.json'), 'utf8'));
const F = process.env.KA_FONTES || '/home/user/apresentacoes/padrao-ka/fontes';
const face = (w,f) => `@font-face{font-family:Outfit;font-weight:${w};src:url(file://${F}/${f})}`;
const CSS = [face(200,'Outfit1Light.ttf'),face(300,'Outfit1Light.ttf'),face(400,'Outfit1.ttf'),
  face(500,'Outfit1Medium.ttf'),face(600,'Outfit1SemiBold.ttf'),face(700,'Outfit1Bold.ttf'),
  face(800,'Outfit1UltraBold.ttf')].join('\n');

const EXTRA = `html,body{margin:0;padding:0}
aside{display:none}
section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}
h1,h2,h3,p{margin:0}`;

(async () => {
  let ids = process.argv.slice(3);
  if (!ids.length)
    ids = JSON.parse(fs.readFileSync(path.join(DECK,'project/deck.json'),'utf8')).order;
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport:{width:1920,height:1080}, deviceScaleFactor:1});
  const deck = [];
  for (const id of ids) {
    let html = fs.readFileSync(path.join(DECK,'project/slides',id+'.html'),'utf8');
    const nota = (html.match(/<aside>([\s\S]*?)<\/aside>/) || [,''])[1]
      .replace(/<[^>]+>/g,'').replace(/&amp;/g,'&').replace(/&nbsp;/g,' ').trim();
    html = html.replace(/\/_blob\/([0-9a-f]{32})/g, (m,b) =>
      MAP[b] ? 'file://' + path.join(DECK,'assets',MAP[b]) : 'file:///dev/null');
    const doc = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}\n${EXTRA}</style></head><body>${html}</body></html>`;
    const tmp = path.join(DECK,'_x.html');
    fs.writeFileSync(tmp, doc);
    await page.goto('file://'+tmp, {waitUntil:'load'});
    await page.waitForTimeout(200);
    const slide = await page.evaluate(() => {
      const px = v => parseFloat(v) || 0;
      const INLINE = new Set(['B','SPAN','BR','I','STRONG','EM','SUP','U']);
      const out = [];
      const sec = document.querySelector('section');
      const cssec = getComputedStyle(sec);
      const vazio = c => !c || c === 'transparent' || /rgba\(\s*0,\s*0,\s*0,\s*0\s*\)/.test(c);

      const caixa = el => {
        const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
        const bl = px(cs.borderLeftWidth), bt = px(cs.borderTopWidth);
        const brw = px(cs.borderRightWidth), bb = px(cs.borderBottomWidth);
        const pl = px(cs.paddingLeft), pt = px(cs.paddingTop);
        const pr = px(cs.paddingRight), pb = px(cs.paddingBottom);
        return {x:r.left, y:r.top, w:r.width, h:r.height,
                cx:r.left+bl+pl, cy:r.top+bt+pt,
                cw:r.width-bl-brw-pl-pr, ch:r.height-bt-bb-pt-pb};
      };

      const trechos = (el) => {
        const res = [];
        const rec = (no, est) => {
          no.childNodes.forEach(n => {
            if (n.nodeType === 3) {
              if (n.textContent.length) res.push(Object.assign({t:n.textContent}, est));
            } else if (n.tagName === 'BR') {
              res.push({br:true});
            } else {
              const cs = getComputedStyle(n);
              rec(n, {peso:+cs.fontWeight, cor:cs.color, ls:px(cs.letterSpacing), tam:px(cs.fontSize)});
            }
          });
        };
        const cs = getComputedStyle(el);
        rec(el, {peso:+cs.fontWeight, cor:cs.color, ls:px(cs.letterSpacing), tam:px(cs.fontSize)});
        return res;
      };

      const anda = (el) => {
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') return;
        const b = caixa(el);
        if (b.w === 0 && b.h === 0) return;
        const tag = el.tagName.toUpperCase();
        if (tag === 'IMG') {
          out.push({tipo:'img', src:el.getAttribute('src'), b,
                    fit:cs.objectFit, raio:px(cs.borderTopLeftRadius),
                    nw:el.naturalWidth, nh:el.naturalHeight});
          return;
        }
        if (tag === 'SVG') {
          out.push({tipo:'svg', html:el.outerHTML, b});
          return;
        }
        const temFundo = !vazio(cs.backgroundColor);
        const lado = (l) => {
          const w = px(cs['border' + l + 'Width']);
          const e = cs['border' + l + 'Style'];
          return (w > 0 && e !== 'none' && !vazio(cs['border' + l + 'Color']))
                 ? {w, cor: cs['border' + l + 'Color'], estilo: e} : null;
        };
        const bordas = {topo:lado('Top'), direita:lado('Right'),
                        baixo:lado('Bottom'), esquerda:lado('Left')};
        const temBorda = Object.values(bordas).some(Boolean);
        if (temFundo || temBorda) {
          out.push({tipo:'rect', b, fundo: temFundo ? cs.backgroundColor : null,
                    raio: px(cs.borderTopLeftRadius),
                    raios: [px(cs.borderTopLeftRadius), px(cs.borderTopRightRadius),
                            px(cs.borderBottomRightRadius), px(cs.borderBottomLeftRadius)],
                    bordas});
        }
        const filhos = Array.from(el.children);
        const folha = filhos.every(c => INLINE.has(c.tagName.toUpperCase()));
        if (folha && el.textContent.trim()) {
          out.push({tipo:'texto', b,
                    tam:px(cs.fontSize), peso:+cs.fontWeight, cor:cs.color,
                    ls:px(cs.letterSpacing),
                    lh: cs.lineHeight === 'normal' ? px(cs.fontSize)*1.2 : px(cs.lineHeight),
                    align:cs.textAlign, nowrap: cs.whiteSpace === 'nowrap',
                    trechos: trechos(el)});
          return;
        }
        filhos.forEach(anda);
      };
      Array.from(sec.children).forEach(anda);
      return {fundo: cssec.backgroundColor, itens: out};
    });
    slide.id = id; slide.nota = nota;
    deck.push(slide);
    console.log(id, slide.itens.length, 'itens');
  }
  fs.mkdirSync(path.join(DECK,'edit'), {recursive:true});
  fs.writeFileSync(path.join(DECK,'edit/spec.json'), JSON.stringify(deck, null, 1));
  await browser.close();
})();
