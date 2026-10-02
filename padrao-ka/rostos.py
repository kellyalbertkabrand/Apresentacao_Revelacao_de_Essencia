#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAPA DE ROSTOS — onde esta a cabeca em cada fotografia.

    python3 padrao-ka/rostos.py clientes/<cliente>/assets

Detecta os rostos de uma pasta de fotos e grava `rostos.json` ao lado
delas. O motor de layout le esse arquivo na hora de montar o deck e
escolhe o recorte que mantem a cabeca INTEIRA dentro da faixa — sem isso
o corte e cego e decapita as pessoas.

Por que um arquivo e nao deteccao em tempo de build: a geracao do .pptx
nao deve depender de OpenCV instalado, e o mapa e estavel — muda so
quando as fotos mudam. Rodar de novo depois de trocar qualquer imagem.

Regra de escolha: a MAIOR deteccao de cada foto e a pessoa em foco. O
detector tambem acha gravata, mao e logotipo, sempre em caixas pequenas.

A caixa gravada nao e a do rosto, e a da CABECA: o detector marca da
testa ao queixo, entao ela e esticada para cima (cabelo), para baixo
(queixo e pescoco) e para os lados (orelhas), em fracao da propria
altura. Recortar na caixa crua corta o cabelo.
"""
import glob
import json
import os
import sys

# Margens em fracao da altura da caixa detectada.
ACIMA, ABAIXO, LADOS = 0.62, 0.38, 0.28

# Folga extra, em fracao da altura da cabeca, entre a cabeca e a borda do
# recorte. Cabeca encostada na borda le como decapitada mesmo sem cortar.
RESPIRO = 0.28


def cabeca(caminho, cv2):
    """Caixa da cabeca da pessoa em foco, em fracao da imagem."""
    base = os.path.join(os.path.dirname(cv2.__file__), "data")
    cascatas = [cv2.CascadeClassifier(os.path.join(base, n)) for n in (
        "haarcascade_frontalface_default.xml",
        "haarcascade_frontalface_alt2.xml",
        "haarcascade_profileface.xml")]
    img = cv2.imread(caminho)
    if img is None:
        return None
    cinza = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    altura, largura = cinza.shape
    achados = []
    for c in cascatas:
        achados += list(c.detectMultiScale(cinza, 1.07, 5, minSize=(70, 70)))
    espelho = cv2.flip(cinza, 1)
    for (x, y, w, h) in cascatas[2].detectMultiScale(espelho, 1.07, 5,
                                                     minSize=(70, 70)):
        achados.append((largura - x - w, y, w, h))
    if not achados:
        return None
    x, y, w, h = max(achados, key=lambda r: r[2] * r[3])
    return {
        "esq": max(0.0, (x - LADOS * h) / largura),
        "dir": min(1.0, (x + w + LADOS * h) / largura),
        "topo": max(0.0, (y - ACIMA * h) / altura),
        "base": min(1.0, (y + h + ABAIXO * h) / altura),
    }


def foco(caixa, origem, alvo, eixo):
    """Foco (0 a 1) que mantem a cabeca inteira dentro do recorte.

    `origem` e `alvo` sao as proporcoes largura/altura da imagem e da
    caixa de destino. `eixo` e "v" quando o corte e vertical (faixa
    horizontal) e "h" quando e horizontal (tira vertical).

    Devolve (foco, cabe). Quando nao cabe, o foco centra a cabeca e o
    chamador precisa dar mais espaco ao recorte.
    """
    if eixo == "v":
        visivel = min(1.0, origem / alvo)
        a, b = caixa["topo"], caixa["base"]
    else:
        visivel = min(1.0, alvo / origem)
        a, b = caixa["esq"], caixa["dir"]
    corte = 1.0 - visivel
    if corte <= 1e-6:
        return 0.5, True
    folga = RESPIRO * (b - a)
    centro = min(max(((a + b) / 2 - visivel / 2) / corte, 0.0), 1.0)
    if (b - a) + 2 * folga > visivel:
        return centro, False
    lo = max(0.0, (b + folga - visivel) / corte)
    hi = min(1.0, (a - folga) / corte)
    if lo > hi:
        return centro, True
    return min(max(centro, lo), hi), True


def mapear(pasta):
    import cv2
    mapa = {}
    for f in sorted(glob.glob(os.path.join(pasta, "*.*"))):
        if f.lower().endswith((".json", ".txt", ".md")):
            continue
        c = cabeca(f, cv2)
        nome = os.path.basename(f)
        if c:
            mapa[nome] = c
            print("%-48s cabeca y %.2f–%.2f  x %.2f–%.2f"
                  % (nome, c["topo"], c["base"], c["esq"], c["dir"]))
        else:
            print("%-48s sem rosto detectado" % nome)
    alvo = os.path.join(pasta, "rostos.json")
    with open(alvo, "w", encoding="utf-8") as fp:
        json.dump(mapa, fp, indent=1, sort_keys=True)
    print("\n%d de %d fotos mapeadas -> %s"
          % (len(mapa), len(glob.glob(os.path.join(pasta, "*.*"))) - 1, alvo))
    return mapa


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: rostos.py <pasta-de-assets>")
    mapear(os.path.abspath(sys.argv[1]))
