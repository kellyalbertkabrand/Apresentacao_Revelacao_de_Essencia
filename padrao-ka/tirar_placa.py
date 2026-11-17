# -*- coding: utf-8 -*-
"""Tira a placa de fundo que vem grudada em algumas versões do logotipo.

O arquivo que o cliente exporta às vezes traz, atrás da linha de atuação,
um retângulo da cor do slide em que a marca foi desenhada. Sobre aquele
fundo ele some; sobre qualquer outro vira um tarjão. Aqui a placa é
desfeita: o que era tinta sobre a placa volta a ser tinta sobre nada.

    python3 padrao-ka/tirar_placa.py arquivo.png --placa CEC3B5 --tinta 000000
"""
import argparse, sys
import numpy as np
from PIL import Image


def hexa(s):
    s = s.lstrip("#")
    return np.array([int(s[i:i + 2], 16) for i in (0, 2, 4)], dtype=float)


def tirar(caminho, saida, cor_placa, cor_tinta, x_min=0, x_max=None,
          tolerancia=30, piso=0.15, folga=4):
    im = Image.open(caminho).convert("RGBA")
    a = np.array(im).astype(float)
    alt, larg = a.shape[:2]
    x_max = larg if x_max is None else x_max
    opaco = a[:, :, 3] > 200
    faixa = np.zeros((alt, larg), bool)
    faixa[:, x_min:x_max] = True
    placa = (opaco & faixa &
             (np.abs(a[:, :, :3] - cor_placa).max(axis=2) < tolerancia))
    if not placa.any():
        print("sem placa em", caminho)
        return
    ys, xs = np.where(placa)
    # a borda da placa fica meio transparente e escapa do teste: por isso a
    # area tratada cresce alguns pixels para cada lado
    y0, y1 = max(0, ys.min() - folga), min(alt, ys.max() + 1 + folga)
    x0, x1 = max(0, xs.min() - folga), min(larg, xs.max() + 1 + folga)
    rec = a[y0:y1, x0:x1]
    # desfaz a composição: quanto o pixel se afastou da placa na direção
    # da tinta é exatamente a opacidade que a tinta tinha ali
    alcance = cor_tinta - cor_placa
    eixo = int(np.argmax(np.abs(alcance)))
    t = (rec[:, :, eixo] - cor_placa[eixo]) / alcance[eixo]
    # o contorno da placa deixa um fiapo de tinta quase transparente: é ele
    # que vira o fantasma do tarjão sobre outro fundo. O piso corta o fiapo
    # e o que sobra e reescalado, para a tinta nao perder corpo
    t = (t - piso) / (1.0 - piso)
    novo_alfa = np.clip(t, 0, 1) * (rec[:, :, 3] / 255.0)
    dentro = rec[:, :, 3] > 8
    for c in range(3):
        rec[:, :, c] = np.where(dentro, cor_tinta[c], rec[:, :, c])
    rec[:, :, 3] = np.where(dentro, novo_alfa * 255, rec[:, :, 3])
    a[y0:y1, x0:x1] = rec
    Image.fromarray(a.astype(np.uint8), "RGBA").save(saida)
    print("placa de %dx%d tirada em %s" % (x1 - x0, y1 - y0, saida))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivo")
    ap.add_argument("--saida")
    ap.add_argument("--placa", required=True)
    ap.add_argument("--tinta", required=True)
    ap.add_argument("--x-min", type=int, default=0)
    ap.add_argument("--x-max", type=int)
    ap.add_argument("--tolerancia", type=int, default=30)
    ap.add_argument("--piso", type=float, default=0.15)
    ap.add_argument("--folga", type=int, default=4)
    o = ap.parse_args()
    tirar(o.arquivo, o.saida or o.arquivo, hexa(o.placa), hexa(o.tinta),
          o.x_min, o.x_max, o.tolerancia, o.piso, o.folga)
