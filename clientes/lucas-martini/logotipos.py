#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Folha de logotipos do Lucas Martini, em PDF.

    python3 clientes/lucas-martini/vetorizar.py     # primeiro o vetor
    python3 clientes/lucas-martini/logotipos.py     # depois a folha

Gera dois conjuntos em `assets/marca/pdf/`:

- **Lucas-Martini-Logotipos.pdf** — a folha completa, uma versão por página,
  com o nome, o fundo em que vive e o que ela resolve. É o que se manda para
  um fornecedor que precisa escolher.
- **um PDF por versão** — o arquivo solto, em **vetor**, direto de
  `assets/marca/vetor/`. É o que se manda quando pedem "o logo em PDF", e é
  o que a gráfica quer: escala de um brinde a uma fachada sem perder nada.

Tudo sai de `assets/marca/vetor/`, que é onde o `vetorizar.py` deixa o
logotipo refeito. A folha é raster a 200 dpi só porque é um documento de
leitura; os arquivos soltos são vetor de verdade.
"""
import os
import shutil

from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(AQUI, "assets", "marca")
VETOR = os.path.join(MARCA, "vetor")
SAIDA = os.path.join(MARCA, "pdf")
FONTES = os.path.join(os.path.dirname(os.path.dirname(AQUI)),
                      "padrao-ka", "fontes")

DPI = 200
A4 = (int(11.69 * DPI), int(8.27 * DPI))      # A4 deitado

VERDE = (74, 83, 78)
PAPEL = (246, 244, 239)
AREIA = (206, 195, 181)
GRAFITE = (44, 50, 46)
DOURADO = (174, 140, 78)
SUAVE = (154, 160, 154)

# nome, arquivo em vetor/, fundo da página, cor do texto, legenda
VERSOES = [
    ("Principal", "lm-horizontal-ouro-claro", VERDE, PAPEL,
     "Dourado sobre o verde da marca. É a versão de assinatura."),
    ("Vertical", "lm-vertical-ouro-claro", VERDE, PAPEL,
     "Para espaços estreitos e para a abertura de documentos."),
    ("Dourado sobre papel", "lm-horizontal-ouro", PAPEL, GRAFITE,
     "O mesmo metal, um tom mais fundo, para viver sobre o claro."),
    ("Monocromática", "lm-horizontal-preto", PAPEL, GRAFITE,
     "Preto sobre papel. Documento, contrato, impressão em uma cor."),
    ("Vertical monocromática", "lm-vertical-preto", AREIA, GRAFITE,
     "Sobre a areia da marca: papelaria e aplicações impressas."),
    ("Sobre fundo escuro", "lm-vertical-branco", GRAFITE, PAPEL,
     "Versão clara, só quando o fundo for escuro o bastante."),
    ("Símbolo", "lm-escudo-ouro-claro", VERDE, PAPEL,
     "O escudo sozinho: avatar, carimbo, selo e assinatura de e-mail."),
    ("Símbolo monocromático", "lm-escudo-preto", PAPEL, GRAFITE,
     "Para gravação, relevo, carimbo e aplicação em uma cor."),
]


def fonte(nome, tam):
    return ImageFont.truetype(os.path.join(FONTES, nome), tam)


def logo(arquivo):
    return Image.open(os.path.join(VETOR, arquivo + ".png")).convert("RGBA")


def pagina(nome, arquivo, fundo, tinta, legenda):
    """Uma versão, centrada na página, com o nome e a legenda embaixo."""
    pag = Image.new("RGB", A4, fundo)
    d = ImageDraw.Draw(pag)
    im = logo(arquivo)

    # o logo ocupa no máximo 46% da largura e 34% da altura da página
    esc = min(A4[0] * 0.46 / im.size[0], A4[1] * 0.34 / im.size[1])
    im = im.resize((int(im.size[0] * esc), int(im.size[1] * esc)),
                   Image.LANCZOS)
    x = (A4[0] - im.size[0]) // 2
    y = int(A4[1] * 0.30) - im.size[1] // 2
    pag.paste(im, (x, y), im)

    base = int(A4[1] * 0.62)
    d.line([(A4[0] * 0.5 - 80, base), (A4[0] * 0.5 + 80, base)],
           fill=DOURADO, width=4)
    d.text((A4[0] / 2, base + 60), nome.upper(), font=fonte("Outfit1.ttf", 40),
           fill=tinta, anchor="ma")
    d.text((A4[0] / 2, base + 138), legenda,
           font=fonte("Outfit1Light.ttf", 32), fill=tinta, anchor="ma")
    d.text((A4[0] / 2, A4[1] - 106), "LUCAS MARTINI  ·  PROTEÇÃO & SUCESSÃO",
           font=fonte("Outfit1Light.ttf", 27), fill=tinta, anchor="ma")
    return pag


def capa():
    pag = Image.new("RGB", A4, VERDE)
    d = ImageDraw.Draw(pag)
    im = logo("lm-vertical-ouro-claro")
    esc = A4[0] * 0.44 / im.size[0]
    im = im.resize((int(im.size[0] * esc), int(im.size[1] * esc)),
                   Image.LANCZOS)
    pag.paste(im, ((A4[0] - im.size[0]) // 2, int(A4[1] * 0.28)), im)
    d.text((A4[0] / 2, A4[1] * 0.62), "LOGOTIPOS",
           font=fonte("Outfit1.ttf", 46), fill=PAPEL, anchor="ma")
    d.text((A4[0] / 2, A4[1] * 0.62 + 74), "Proteção & Sucessão",
           font=fonte("Outfit1Light.ttf", 32), fill=SUAVE, anchor="ma")
    return pag


if __name__ == "__main__":
    os.makedirs(SAIDA, exist_ok=True)
    paginas = [capa()] + [pagina(*v) for v in VERSOES]
    folha = os.path.join(SAIDA, "Lucas-Martini-Logotipos.pdf")
    paginas[0].save(folha, "PDF", resolution=DPI, save_all=True,
                    append_images=paginas[1:])
    print(folha)

    # os arquivos soltos são o próprio vetor, copiado — não uma foto dele
    for _, arquivo, _, _, _ in VERSOES:
        origem = os.path.join(VETOR, arquivo + ".pdf")
        destino = os.path.join(SAIDA, arquivo + ".pdf")
        shutil.copyfile(origem, destino)
        print(destino)
