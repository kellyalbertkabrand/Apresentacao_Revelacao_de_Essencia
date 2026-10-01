#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta as duas apresentacoes do Lucas Martini no padrao KA.

    python3 clientes/lucas-martini/gerar.py            # as duas
    python3 clientes/lucas-martini/gerar.py revelacao  # so uma

Cada deck e um modulo de conteudo com uma lista PAGINAS; os arquetipos de
pagina estao em padrao-ka/ka_paginas.py.
"""
import importlib.util
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "padrao-ka"))

from ka_paginas import DeckNarrativo  # noqa: E402

DECKS = ("revelacao", "base-estrategica")


def carregar(nome):
    caminho = os.path.join(AQUI, nome.replace("-", "_") + ".py")
    spec = importlib.util.spec_from_file_location("conteudo_" + nome, caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def pdf(caminho):
    """Converte o .pptx entregue para PDF, no mesmo diretorio."""
    saida = os.path.dirname(caminho)
    subprocess.run(
        ["soffice", "--headless", "--norestore", "--convert-to", "pdf",
         "--outdir", saida, caminho],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        timeout=600)
    return caminho[:-5] + ".pdf"


def montar(nome):
    C = carregar(nome)
    d = DeckNarrativo(documento=C.DOCUMENTO, marca=C.MARCA,
                      assets=os.path.join(AQUI, "assets"))
    d.montar(C.PAGINAS)
    alvo = os.path.join(AQUI, C.ARQUIVO + ".pptx")
    caminho, n = d.salvar(alvo)
    print("OK -> %s  (%d slides)" % (caminho, n))
    print("     %s" % pdf(caminho))
    return caminho


if __name__ == "__main__":
    alvos = sys.argv[1:] or list(DECKS)
    for nome in alvos:
        montar(nome)
