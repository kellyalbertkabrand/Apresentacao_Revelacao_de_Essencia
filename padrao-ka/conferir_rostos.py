#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONFERE OS ROSTOS — nenhuma cabeca cortada no arquivo final.

    python3 padrao-ka/conferir_rostos.py <arquivo.pptx> <pasta-de-assets>

Abre o .pptx pronto, le o recorte REAL de cada fotografia (os valores de
crop que o PowerPoint vai aplicar) e confere contra o mapa de cabecas em
`rostos.json`. Nao e inspecao visual nem confianca no gerador: e a conta
feita sobre o que foi gravado no arquivo.

Sai 1 se alguma cabeca ficou cortada.
"""
import glob
import hashlib
import json
import os
import sys

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE


def visivel(pic):
    """Janela da imagem que sobrevive ao recorte, em fracao (0 a 1)."""
    return {
        "esq": pic.crop_left,
        "dir": 1.0 - pic.crop_right,
        "topo": pic.crop_top,
        "base": 1.0 - pic.crop_bottom,
    }


def por_conteudo(assets):
    """sha1 do arquivo -> nome original.

    O python-pptx grava as imagens embutidas como image1.png, image2.jpg
    e por ai: o nome original se perde no caminho. Casar por conteudo e o
    unico jeito honesto de saber qual foto esta em qual slide."""
    tabela = {}
    for f in glob.glob(os.path.join(assets, "*.*")):
        if f.lower().endswith((".json", ".txt", ".md")):
            continue
        with open(f, "rb") as fp:
            tabela[hashlib.sha1(fp.read()).hexdigest()] = os.path.basename(f)
    return tabela


def conferir(caminho, assets):
    mapa_arq = os.path.join(assets, "rostos.json")
    if not os.path.exists(mapa_arq):
        sys.exit("falta o mapa de rostos: %s\n"
                 "rode antes: python3 padrao-ka/rostos.py %s"
                 % (mapa_arq, assets))
    with open(mapa_arq, encoding="utf-8") as fp:
        cabecas = json.load(fp)

    tabela = por_conteudo(assets)
    prs = Presentation(caminho)
    cortadas, conferidas, sem_mapa = [], 0, set()
    for n, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if sh.shape_type != MSO_SHAPE_TYPE.PICTURE:
                continue
            nome = tabela.get(hashlib.sha1(sh.image.blob).hexdigest(), "")
            if nome not in cabecas:
                if nome:
                    sem_mapa.add(nome)
                continue
            c, v = cabecas[nome], visivel(sh)
            conferidas += 1
            folga = min(c["topo"] - v["topo"], v["base"] - c["base"],
                        c["esq"] - v["esq"], v["dir"] - c["dir"])
            if folga < -0.005:
                cortadas.append((n, nome, folga))

    for nome, _ in sorted((n, 1) for n in sem_mapa):
        print("  aviso: %s sem cabeca mapeada (nao conferida)" % nome)
    if cortadas:
        for n, nome, folga in cortadas:
            print("  slide %02d  CABECA CORTADA em %s (invade %.1f%% da "
                  "cabeca)" % (n, nome, abs(folga) * 100))
        return 1
    print("NENHUMA CABECA CORTADA  (%d fotografias conferidas)" % conferidas)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("uso: conferir_rostos.py <arquivo.pptx> <pasta-de-assets>")
    sys.exit(conferir(sys.argv[1], sys.argv[2]))
