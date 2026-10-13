#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le a saida de `pdftotext -bbox` e aponta o texto que vazou do painel.

Chamado por conferir.sh. O fundo do painel esta em 9,60" (691,2 pt) e o
rodape vive legitimamente abaixo disso, a partir de 10,16" — por isso a
faixa do rodape fica de fora da checagem.

O brand book nao tem painel: a pagina inteira e area util, e o limite passa
a ser 10,30". Nesse caso:

    python3 padrao-ka/conferir.py bb.html --fundo 10.30
"""
import re
import sys

FUNDO = 691.2    # 9,60" em pontos — o fundo do painel
RODAPE = 728.0   # a partir daqui e a faixa do rodape, fora do painel de proposito

PALAVRA = re.compile(
    r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">'
    r'(.*?)</word>')


def main(caminho, fundo=FUNDO, rodape=RODAPE):
    with open(caminho, encoding="utf-8") as f:
        html = f.read()
    limpo = True
    for i, pagina in enumerate(html.split("<page ")[1:], 1):
        fora = [(float(m[4]), m[5]) for m in PALAVRA.finditer(pagina)
                if float(m[4]) > fundo and float(m[2]) < rodape]
        if fora:
            limpo = False
            print("  slide %02d  vaza ate %.2f in  |  %s" % (
                i, max(f[0] for f in fora) / 72,
                " ".join(f[1] for f in fora)[:90]))
    if limpo:
        print("TUDO DENTRO DO PAINEL")
    return 0 if limpo else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    fundo, rodape = FUNDO, RODAPE
    if "--fundo" in args:
        i = args.index("--fundo")
        fundo = float(args[i + 1]) * 72
        rodape = 1e9          # sem painel nao ha faixa de rodape a ignorar
        args = args[:i] + args[i + 2:]
    sys.exit(main(args[0], fundo, rodape))
