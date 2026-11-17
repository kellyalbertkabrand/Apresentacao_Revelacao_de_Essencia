# -*- coding: utf-8 -*-
"""Prepara a fotografia da capa do brand book: recorta em 16:9, desfoca e
põe o véu por cima.

O desfoque e o véu são feitos aqui, e não dentro do .pptx, porque efeito de
PowerPoint muda conforme o programa que abre o arquivo. Assim a capa é a
mesma em qualquer lugar.

    python3 clientes/lucas-martini/capa_fundo.py --blur 10 --veu 0.45 0.58
"""
import argparse, os
import numpy as np
from PIL import Image, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
CAPA = os.path.join(AQUI, "assets", "capa")
ORIGINAL = os.path.join(CAPA, "capa-original.png")

VERDE_FECHADO = np.array([16, 20, 18], float)
VERDE_ABERTO = np.array([116, 130, 120], float)


def preparar(blur, veu, saida_preto, saida_verde):
    im = Image.open(ORIGINAL).convert("RGB")
    bor = im.filter(ImageFilter.GaussianBlur(radius=blur))
    alt = im.size[1]
    grad = np.linspace(veu[0], veu[1], alt)[:, None, None]

    preto = np.asarray(bor).astype(float) * (1 - grad)
    Image.fromarray(np.clip(preto, 0, 255).astype("uint8")).save(saida_preto)

    # a mesma foto puxada para o verde da marca, mantendo a luz da imagem
    L = np.asarray(bor.convert("L")).astype(float) / 255.0
    verde = VERDE_FECHADO + L[:, :, None] * (VERDE_ABERTO - VERDE_FECHADO)
    verde = verde * (1 - grad * 0.45)
    Image.fromarray(np.clip(verde, 0, 255).astype("uint8")).save(saida_verde)
    print("desfoque %s, véu de %.2f a %.2f" % (blur, veu[0], veu[1]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--blur", type=float, default=10)
    ap.add_argument("--veu", type=float, nargs=2, default=[0.45, 0.58])
    o = ap.parse_args()
    preparar(o.blur, o.veu,
             os.path.join(CAPA, "capa-fundo-preto.png"),
             os.path.join(CAPA, "capa-fundo-verde.png"))
