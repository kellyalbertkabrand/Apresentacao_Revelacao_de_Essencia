#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a trama de pontos do brand book.

    python3 padrao-ka/trama.py

O brand book usa uma retícula de pontos que se desfaz — a mesma ideia do
meio-tom de impressão. Os pontos saem BRANCOS com alfa; a cor de quem está
embaixo é que manda. Três variantes, pela direção em que a trama se desfaz.
"""
import os

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(AQUI, "assets")

LARG, ALT = 2000, 1125     # 100 px por polegada, o tamanho da página
PASSO = 11                 # distância entre centros de ponto
RAIO = 2.1


def desenhar(nome, peso):
    """`peso(x, y)` devolve 0..1 — a opacidade do ponto naquele lugar."""
    im = Image.new("RGBA", (LARG, ALT), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    for y in range(0, ALT + PASSO, PASSO):
        for x in range(0, LARG + PASSO, PASSO):
            p = peso(x / LARG, y / ALT)
            if p <= 0.01:
                continue
            a = int(min(1.0, p) * 255)
            d.ellipse((x - RAIO, y - RAIO, x + RAIO, y + RAIO),
                      fill=(255, 255, 255, a))
    caminho = os.path.join(ASSETS, nome)
    im.save(caminho)
    print(caminho)


if __name__ == "__main__":
    # canto inferior esquerdo: a trama sobe e se desfaz
    desenhar("trama-canto.png",
             lambda x, y: max(0.0, (y - 0.45) * 1.9) * max(0.0, (0.75 - x) * 1.5))
    # faixa à direita: a trama entra pela borda
    desenhar("trama-direita.png",
             lambda x, y: max(0.0, (x - 0.52) * 1.7))
    # rodapé inteiro: a trama assenta o pé da página
    desenhar("trama-pe.png",
             lambda x, y: max(0.0, (y - 0.62) * 1.6))
