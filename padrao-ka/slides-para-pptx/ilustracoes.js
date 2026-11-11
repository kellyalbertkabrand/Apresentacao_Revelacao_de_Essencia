// ilustracoes.js — rasteriza, com fundo transparente, o que no slide e vetor:
// os desenhos em SVG inline e os logos em .svg. Roda depois do extrair.js e
// anota o arquivo de cada um no proprio spec.json.
//
//   node ilustracoes.js <pasta-do-deck>
//
// A resolucao e 4x o tamanho em tela: num slide de 1920px isso da o bastante
// para imprimir sem serrilhar.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const DECK = path.resolve(process.argv[2] || '.');
const EDIT = path.join(DECK, 'edit');
const spec = path.join(EDIT, 'spec.json');
const deck = JSON.parse(fs.readFileSync(spec, 'utf8'));
fs.mkdirSync(path.join(EDIT, 'svg'), {recursive: true});

const pagina = (corpo, w, h) => `<!doctype html><html><head><meta charset="utf-8"><style>
  html,body{margin:0;padding:0;background:transparent}
  #c{width:${w}px;height:${h}px}
  img{width:${w}px;height:${h}px;object-fit:contain;display:block}
  </style></head><body><div id="c">${corpo}</div></body></html>`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 800, height: 800}, deviceScaleFactor: 4});
  const tmp = path.join(EDIT, '_ilustra.html');
  const feitos = {};
  let n = 0;
  for (const s of deck) {
    let i = 0;
    for (const it of s.itens) {
      const vetor = it.tipo === 'svg' || (it.tipo === 'img' && it.src.endsWith('.svg'));
      if (!vetor) continue;
      const w = Math.round(it.b.w), h = Math.round(it.b.h);
      const chave = it.tipo === 'svg' ? `${s.id}-${i++}`
                  : `${path.basename(it.src, '.svg')}-${w}x${h}`;
      if (!feitos[chave]) {
        const corpo = it.tipo === 'svg' ? it.html : `<img src="${it.src}">`;
        fs.writeFileSync(tmp, pagina(corpo, w, h));
        await page.setViewportSize({width: w, height: h});
        await page.goto('file://' + tmp, {waitUntil: 'load'});
        await page.waitForTimeout(120);
        await page.screenshot({path: path.join(EDIT, 'svg', chave + '.png'), omitBackground: true});
        feitos[chave] = 'svg/' + chave + '.png';
        n++;
      }
      it.arquivo = feitos[chave];
    }
  }
  fs.writeFileSync(spec, JSON.stringify(deck, null, 1));
  fs.existsSync(tmp) && fs.unlinkSync(tmp);
  console.log(n, 'ilustracoes rasterizadas');
  await browser.close();
})();
