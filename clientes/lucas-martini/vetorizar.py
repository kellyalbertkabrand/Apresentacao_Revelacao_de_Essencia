#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Refaz os logotipos do Lucas Martini em vetor.

    python3 clientes/lucas-martini/vetorizar.py

O material de identidade que chegou era uma página de 592 px — foi o que a
API do Canva entregou, e o download em alta está bloqueado pela política de
rede do ambiente. Num logotipo isso aparece de duas formas feias: a borda
serrilhada e a cor "ralada", porque o pixel da borda traz o fundo antigo
misturado dentro dele.

As duas coisas se resolvem na mesma operação: separar a FORMA da COR.

1. **Forma.** A cobertura de tinta é medida em cada pixel (1 no miolo da
   marca, 0 no fundo, a rampa real no meio), ampliada oito vezes e
   **vetorizada** com o potrace. A partir daí a forma não tem mais
   resolução: SVG e PDF escalam de um favicon a um painel.
2. **Cor.** Entra depois, exata: preto, branco, ou o dourado da marca em
   gradiente — medido no próprio material do cliente. Nunca mais uma média
   com o fundo.

O traçado sai sempre da versão de **maior contraste** (preto sobre areia),
que é a única em que os detalhes finos sobrevivem: na dourada sobre verde os
tis de PROTEÇÃO e SUCESSÃO somem de vez, e o escudo prateado se desmancha
porque o degradê cruza a cor do fundo.

Um detalhe que só aparece quando se mede: na origem **o til tem 4 × 1
pixel** — virou uma barra reta. Nenhum traçado inventa de volta o que não
está lá, então esses dois acentos são localizados e **redesenhados** na
proporção certa. É a única parte do logotipo que não vem do traçado, e é
reconstrução de uma informação que se sabe qual é: a palavra é PROTEÇÃO.

Saída em `assets/marca/vetor/`: SVG, PDF e PNG de 4000 px de cada versão.
O PDF é o arquivo que importa — é vetor, e é o que se manda para gráfica.

Uma ressalva honesta: isto é a melhor reconstrução possível a partir do que
existe. O arquivo definitivo é o vetor original do designer; no próprio
Canva, "Compartilhar › Baixar › PDF para impressão" entrega esse vetor.
"""
import math
import os
import subprocess

import numpy as np
import potrace
from PIL import Image, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(AQUI, "assets", "marca")
ORIGEM = os.path.join(MARCA, "origem")
SAIDA = os.path.join(MARCA, "vetor")

ESCALA = 8          # a cobertura e ampliada antes de tracar: curva mais limpa
LIMIAR = 0.50       # meia cobertura e a borda real da letra
SUAVE = 0.5         # desfoque leve antes de ampliar: tira o ruido do pixel
TURD = 80           # some com sujeira menor que ~1,25 px da origem
ONDA = 0.105        # amplitude do til redesenhado, em larguras de til
ESPESSURA = 0.17    # espessura do traco do til, em larguras de til
LARGURA_PNG = 4000

# As cores, medidas no material do cliente.
PRETO = "#101010"
BRANCO = "#FFFFFF"
# O dourado nao e uma cor so: e um metal, e metal tem sombra, meio-tom e
# luz. Estes valores saem das paginas 07 e 12 da identidade.
OURO_CLARO = ("#D9B978", "#F3DCA2", "#E8CA8E")   # sobre fundo escuro
OURO = ("#8F6B2F", "#C9A14E", "#A9802F")         # sobre fundo claro

CORES = (("preto", PRETO),
         ("branco", BRANCO),
         ("ouro", OURO),
         ("ouro-claro", OURO_CLARO))

# nome, pagina de origem, caixa de recorte (x0, y0, x1, y1) ou None
ELEMENTOS = (
    ("horizontal", "p15-horizontal-preto.png", None),
    ("vertical", "p14-vertical-preto.png", None),
    ("escudo", "p15-horizontal-preto.png", (0, 0, 224, 338)),
)


def cobertura(caminho):
    """Quanto de tinta tem cada pixel: 1 no miolo da marca, 0 no fundo.

    O fundo e medido na borda da pagina; a tinta cheia, no percentil 99,5 da
    distancia ate ele — assim um pixel solitario de ruido nao define a
    escala."""
    a = np.asarray(Image.open(caminho).convert("RGB")).astype(np.float32)
    borda = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
    fundo = np.median(borda, axis=0)
    d = np.sqrt(((a - fundo) ** 2).sum(2))
    return np.clip(d / max(1.0, np.percentile(d, 99.5)), 0, 1)


def aparar(m, caixa=None):
    """Corta na caixa pedida e depois no que tem tinta."""
    if caixa:
        x0, y0, x1, y1 = caixa
        m = m[y0:y1, x0:x1]
    ys, xs = np.where(m > 0.25)
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def tracar(m):
    """Cobertura -> curvas de Bezier.

    Uma inversao a acertar, invisivel ate olhar o resultado: o potrace trata
    o valor ALTO como fundo, nao como tinta. Por isso a comparacao e `<=`.
    O eixo y, esse, ja bate com o do SVG — nao se inverte nada."""
    im = Image.fromarray((m * 255).astype(np.uint8))
    if SUAVE:
        im = im.filter(ImageFilter.GaussianBlur(SUAVE))
    g = im.resize((im.size[0] * ESCALA, im.size[1] * ESCALA), Image.BICUBIC)
    bits = (np.asarray(g).astype(np.float32) / 255.0) <= LIMIAR
    return potrace.Bitmap(bits).trace(
        turdsize=TURD, alphamax=1.0, opttolerance=0.2), g.size


def rotular(b):
    """Componentes conexos (8 vizinhos), para achar as peças soltas."""
    h, w = b.shape
    rot = np.zeros((h, w), np.int32)
    n = 0
    for y in range(h):
        for x in range(w):
            if b[y, x] and rot[y, x] == 0:
                n += 1
                rot[y, x] = n
                pilha = [(y, x)]
                while pilha:
                    cy, cx = pilha.pop()
                    for ny in (cy - 1, cy, cy + 1):
                        for nx in (cx - 1, cx, cx + 1):
                            if (0 <= ny < h and 0 <= nx < w
                                    and b[ny, nx] and rot[ny, nx] == 0):
                                rot[ny, nx] = n
                                pilha.append((ny, nx))
    return rot, n


def acentos(m):
    """Onde estão os tis de PROTEÇÃO e SUCESSÃO.

    São as únicas peças soltas minúsculas do desenho — 4 × 1 pixel, contra
    14 × 3 dos filetes que fecham a linha. É por aí que se separam."""
    rot, n = rotular(m > 0.35)
    caixas = []
    for i in range(1, n + 1):
        ys, xs = np.where(rot == i)
        if len(ys) <= 10 and ys.max() - ys.min() <= 1:
            caixas.append((xs.min(), ys.min(), xs.max() + 1.0, ys.max() + 1.0))
    return sorted(caixas)


def til(caixa, escala=ESCALA):
    """Redesenha o til dentro da caixa onde a barra estava.

    Um til é um traço em onda: a linha de centro é uma senóide, e o contorno
    sai dela deslocado meia espessura para cada lado, afinando nas pontas
    como faz qualquer tipo de qualidade."""
    x0, y0, x1, y1 = [v * escala for v in caixa]
    larg = x1 - x0
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    amp = larg * ONDA
    esp = larg * ESPESSURA
    n = 24
    cima, baixo = [], []
    for i in range(n + 1):
        t = i / float(n)
        x = x0 + t * larg
        y = cy - amp * math.sin(2 * math.pi * t)
        dx = larg / n
        dy = -amp * 2 * math.pi * math.cos(2 * math.pi * t) / n
        c = math.hypot(dx, dy)
        nx, ny = -dy / c, dx / c
        # as pontas afinam: meia espessura nas bordas, cheia no miolo
        f = 0.55 + 0.45 * math.sin(math.pi * min(1.0, t * 3)) if t < 1 / 3.0 \
            else (0.55 + 0.45 * math.sin(math.pi * min(1.0, (1 - t) * 3))
                  if t > 2 / 3.0 else 1.0)
        h = esp * f / 2.0
        cima.append((x + nx * h, y + ny * h))
        baixo.append((x - nx * h, y - ny * h))
    pts = cima + baixo[::-1]
    d = "M%.2f %.2f " % pts[0]
    d += " ".join("L%.2f %.2f" % p for p in pts[1:])
    return d + " Z"


def fora(curva, caixas, escala=ESCALA, folga=2.0):
    """A curva traçada cai em cima de um dos acentos?"""
    xs = [curva.start_point.x]
    ys = [curva.start_point.y]
    for s in curva:
        xs.append(s.end_point.x)
        ys.append(s.end_point.y)
    for x0, y0, x1, y1 in caixas:
        if (min(xs) >= x0 * escala - folga and max(xs) <= x1 * escala + folga
                and min(ys) >= y0 * escala - folga
                and max(ys) <= y1 * escala + folga):
            return False
    return True


def caminho_svg(path, caixas=()):
    """Curvas do potrace -> atributo d de um <path> SVG."""
    partes = []
    for curva in path:
        if not fora(curva, caixas):
            continue
        partes.append("M%.2f %.2f" % (curva.start_point.x,
                                      curva.start_point.y))
        for s in curva:
            if s.is_corner:
                partes.append("L%.2f %.2f L%.2f %.2f" % (
                    s.c.x, s.c.y, s.end_point.x, s.end_point.y))
            else:
                partes.append("C%.2f %.2f %.2f %.2f %.2f %.2f" % (
                    s.c1.x, s.c1.y, s.c2.x, s.c2.y,
                    s.end_point.x, s.end_point.y))
        partes.append("Z")
    for caixa in caixas:
        partes.append(til(caixa))
    return " ".join(partes)


def svg(d, tam, cor):
    """Uma cor chapada, ou o degrade do metal quando `cor` sao tres tons."""
    larg, alt = tam
    if isinstance(cor, tuple):
        pintura = "url(#ouro)"
        defs = ("<defs><linearGradient id='ouro' x1='0' y1='0' x2='0.4' "
                "y2='1'><stop offset='0%%' stop-color='%s'/>"
                "<stop offset='45%%' stop-color='%s'/>"
                "<stop offset='100%%' stop-color='%s'/>"
                "</linearGradient></defs>" % cor)
    else:
        pintura, defs = cor, ""
    return ("<?xml version='1.0' encoding='UTF-8'?>\n"
            "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' "
            "width='%d' height='%d'>%s"
            "<path d='%s' fill='%s' fill-rule='evenodd'/></svg>"
            % (larg, alt, larg, alt, defs, d, pintura))


def converter(caminho_svg_arq):
    """SVG -> PDF (svglib) -> PNG transparente de 4000 px (pdftocairo)."""
    from reportlab.graphics import renderPDF
    from svglib.svglib import svg2rlg

    desenho = svg2rlg(caminho_svg_arq)
    pdf = caminho_svg_arq[:-4] + ".pdf"
    renderPDF.drawToFile(desenho, pdf)
    dpi = int(round(LARGURA_PNG / (desenho.width / 72.0)))
    subprocess.run(["pdftocairo", "-png", "-transp", "-singlefile",
                    "-r", str(dpi), pdf, caminho_svg_arq[:-4]], check=True)


def gerar(nome, pagina, caixa):
    m = aparar(cobertura(os.path.join(ORIGEM, pagina)), caixa)
    tis = acentos(m)
    path, tam = tracar(m)
    d = caminho_svg(path, tis)
    print("%-11s %4d x %-4d  ->  %d x %d%s" % (
        nome, m.shape[1], m.shape[0], tam[0], tam[1],
        "   (%d til redesenhado)" % len(tis) if tis else ""))
    for rotulo, cor in CORES:
        base = os.path.join(SAIDA, "lm-%s-%s" % (nome, rotulo))
        with open(base + ".svg", "w", encoding="utf-8") as f:
            f.write(svg(d, tam, cor))
        converter(base + ".svg")
        print("            %s" % os.path.basename(base))


if __name__ == "__main__":
    os.makedirs(SAIDA, exist_ok=True)
    for nome, pagina, caixa in ELEMENTOS:
        gerar(nome, pagina, caixa)
