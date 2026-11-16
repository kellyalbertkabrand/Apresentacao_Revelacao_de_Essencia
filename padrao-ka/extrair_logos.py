# -*- coding: utf-8 -*-
"""Tira os logotipos do arquivo original do cliente, sem vetorizar nada.

    libreoffice --headless --convert-to pdf LOGO-do-cliente.pptx
    pdftoppm -r 600 -png LOGO-do-cliente.pdf pagina
    python3 padrao-ka/extrair_logos.py pagina-07.png:lm-horizontal-ouro.png

Recorta a arte da página renderizada em 600 dpi e transforma o fundo chapado
em transparência.

O fundo é uma cor única; a arte (dourado com degradê, preto ou branco) é
tudo o que se afasta dela. A máscara usa duas soleiras — abaixo da primeira
é fundo, acima da segunda é arte cheia, e no meio a borda ganha o alfa
proporcional. É isso que preserva a serrilha sem comer o degradê do
dourado."""
import os, sys
import numpy as np
from PIL import Image

def recortar(entrada, saida, baixo=10.0, alto=34.0, margem=12, caixa=None):
    im = Image.open(entrada).convert('RGB')
    a = np.asarray(im).astype(np.float32)
    if caixa:
        a = a[caixa[1]:caixa[3], caixa[0]:caixa[2]]
    fundo = np.median(a[:6, :6].reshape(-1, 3), axis=0)
    dist = np.abs(a - fundo).max(axis=2)
    alfa = np.clip((dist - baixo) / (alto - baixo), 0, 1)
    ys, xs = np.where(alfa > 0.25)
    if not len(ys):
        raise SystemExit('nada encontrado em ' + entrada)
    y0, y1 = max(0, ys.min() - margem), min(a.shape[0], ys.max() + margem + 1)
    x0, x1 = max(0, xs.min() - margem), min(a.shape[1], xs.max() + margem + 1)
    rec, al = a[y0:y1, x0:x1], alfa[y0:y1, x0:x1]
    # tira a cor do fundo de dentro da arte (desfaz a composição)
    with np.errstate(divide='ignore', invalid='ignore'):
        cor = np.where(al[..., None] > 0.02,
                       (rec - fundo * (1 - al[..., None])) / np.maximum(al[..., None], 1e-6),
                       rec)
    cor = np.clip(cor, 0, 255)
    rgba = np.dstack([cor, al * 255]).astype(np.uint8)
    Image.fromarray(rgba, 'RGBA').save(saida)
    return saida, (x1 - x0, y1 - y0), fundo.astype(int).tolist()

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        ent, sai = arg.split(':')
        print('%-34s %s  fundo %s' % ((sai,) + recortar(ent, sai)[1:]))
