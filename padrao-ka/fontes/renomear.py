# -*- coding: utf-8 -*-
"""Da a cada variante da Outfit o nome de familia que o Canva usa.

O arquivo da Kelly pede "Outfit 1 Light", "Outfit 1 Medium" e por ai. No
disco, essas variantes se apresentam todas como a familia "Outfit 1" em
estilos diferentes, e o LibreOffice nao casa o nome composto: cai na mesma
face para todos os pesos. A previa entao mente — mostra tudo no mesmo peso e
mede a largura errada.

Aqui cada arquivo passa a se chamar, na propria tabela de nomes, exatamente
como o Canva o chama. Feito uma vez; o resultado e o que vai no repositorio.

    python3 padrao-ka/fontes/renomear.py
"""
import glob
import os

from fontTools.ttLib import TTFont

AQUI = os.path.dirname(os.path.abspath(__file__))

NOMES = {
    "Outfit1": "Outfit 1",
    "Outfit1Light": "Outfit 1 Light",
    "Outfit1Medium": "Outfit 1 Medium",
    "Outfit1SemiBold": "Outfit 1 Semi-Bold",
    "Outfit1Bold": "Outfit 1 Bold",
    "Outfit1UltraBold": "Outfit 1 Ultra-Bold",
    "Outfit2": "Outfit 2",
    "Outfit2Light": "Outfit 2 Light",
    "Outfit2Medium": "Outfit 2 Medium",
    "Outfit2SemiBold": "Outfit 2 Semi-Bold",
}


def renomear(caminho, familia):
    f = TTFont(caminho)
    nome = f["name"]
    for reg in list(nome.names):
        if reg.nameID in (1, 3, 4, 6, 16, 17):
            texto = familia if reg.nameID in (1, 4, 16) else None
            if reg.nameID == 17:          # estilo tipografico
                texto = "Regular"
            elif reg.nameID == 6:         # PostScript
                texto = familia.replace(" ", "").replace("-", "")
            elif reg.nameID == 3:         # identificador unico
                texto = familia + " KA"
            if texto:
                reg.string = texto
    # peso e largura declarados: sem isso o fontconfig ainda agrupa por estilo
    f["name"].setName("Regular", 2, 3, 1, 0x409)
    f["name"].setName("Regular", 2, 1, 0, 0)
    f.save(caminho)


if __name__ == "__main__":
    for caminho in sorted(glob.glob(os.path.join(AQUI, "*.ttf"))):
        base = os.path.splitext(os.path.basename(caminho))[0]
        if base in NOMES:
            renomear(caminho, NOMES[base])
            print("%-22s -> %s" % (base, NOMES[base]))
