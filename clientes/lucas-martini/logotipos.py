#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Folha de logotipos do Lucas Martini, em PDF.

    python3 clientes/lucas-martini/logotipos.py

Gera dois conjuntos em `assets/marca/pdf/`:

- **Lucas-Martini-Logotipos.pdf** — a folha completa, uma versão por página,
  com o nome, o fundo em que vive e o arquivo de origem. É o que se manda
  para um fornecedor que precisa escolher.
- **um PDF por versão** — a página cortada no tamanho do próprio logo, com
  respiro. É o que se manda quando pedem "o logo em PDF".

Os PNGs de origem foram recortados do material de identidade do cliente e
têm 592 px de largura — foi o que a API do Canva entregou. Serve para tela,
para apresentação e para impressão pequena; para impressão grande, trocar os
PNGs em `assets/marca/` pelos arquivos originais e rodar isto de novo.
"""
import os

from PIL import Image, ImageDraw, ImageFont

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA = os.path.join(AQUI, "assets", "marca")
SAIDA = os.path.join(MARCA, "pdf")
FONTES = os.path.join(os.path.dirname(os.path.dirname(AQUI)),
                      "padrao-ka", "fontes")

DPI = 150
A4 = (int(11.69 * DPI), int(8.27 * DPI))      # A4 deitado

VERDE = (74, 83, 78)
PAPEL = (246, 244, 239)
AREIA = (206, 195, 181)
GRAFITE = (44, 50, 46)
DOURADO = (174, 140, 78)
SUAVE = (154, 160, 154)

# nome, arquivo, fundo da página, cor do texto, legenda
VERSOES = [
    ("Principal", "lm-horizontal-dourado.png", VERDE, PAPEL,
     "Dourado sobre o verde da marca. É a versão de assinatura."),
    ("Vertical", "lm-vertical-dourado-escuro.png", VERDE, PAPEL,
     "Para espaços estreitos e para a abertura de documentos."),
    ("Monocromática", "lm-horizontal-preto.png", PAPEL, GRAFITE,
     "Preto sobre papel. Documento, contrato, impressão em uma cor."),
    ("Vertical monocromática", "lm-vertical-preto.png", AREIA, GRAFITE,
     "Sobre a areia da marca: papelaria e aplicações impressas."),
    ("Sobre fundo escuro", "lm-vertical-claro.png", GRAFITE, PAPEL,
     "Versão clara, só quando o fundo for escuro o bastante."),
    ("Símbolo", "lm-escudo-dourado.png", VERDE, PAPEL,
     "O escudo sozinho: avatar, carimbo, selo e assinatura de e-mail."),
]


def fonte(nome, tam):
    return ImageFont.truetype(os.path.join(FONTES, nome), tam)


def pagina(nome, arquivo, fundo, tinta, legenda):
    """Uma versão, centrada na página, com o nome e a legenda embaixo."""
    pag = Image.new("RGB", A4, fundo)
    d = ImageDraw.Draw(pag)
    logo = Image.open(os.path.join(MARCA, arquivo)).convert("RGBA")

    # o logo ocupa no máximo 46% da largura e 34% da altura da página
    esc = min(A4[0] * 0.46 / logo.size[0], A4[1] * 0.34 / logo.size[1])
    logo = logo.resize((int(logo.size[0] * esc), int(logo.size[1] * esc)),
                       Image.LANCZOS)
    x = (A4[0] - logo.size[0]) // 2
    y = int(A4[1] * 0.30) - logo.size[1] // 2
    pag.paste(logo, (x, y), logo)

    base = int(A4[1] * 0.62)
    d.line([(A4[0] * 0.5 - 60, base), (A4[0] * 0.5 + 60, base)],
           fill=DOURADO, width=3)
    d.text((A4[0] / 2, base + 46), nome.upper(), font=fonte("Outfit1.ttf", 30),
           fill=tinta, anchor="ma")
    d.text((A4[0] / 2, base + 104), legenda,
           font=fonte("Outfit1Light.ttf", 24), fill=tinta, anchor="ma")
    d.text((A4[0] / 2, A4[1] - 80), "LUCAS MARTINI  ·  PROTEÇÃO & SUCESSÃO",
           font=fonte("Outfit1Light.ttf", 20), fill=tinta, anchor="ma")
    return pag


def capa():
    pag = Image.new("RGB", A4, VERDE)
    d = ImageDraw.Draw(pag)
    logo = Image.open(os.path.join(MARCA, "lm-vertical-dourado-escuro.png"))
    logo = logo.convert("RGBA")
    esc = A4[0] * 0.44 / logo.size[0]
    logo = logo.resize((int(logo.size[0] * esc), int(logo.size[1] * esc)),
                       Image.LANCZOS)
    pag.paste(logo, ((A4[0] - logo.size[0]) // 2, int(A4[1] * 0.30)), logo)
    d.text((A4[0] / 2, A4[1] * 0.62), "LOGOTIPOS",
           font=fonte("Outfit1.ttf", 34), fill=PAPEL, anchor="ma")
    d.text((A4[0] / 2, A4[1] * 0.62 + 56), "Proteção & Sucessão",
           font=fonte("Outfit1Light.ttf", 24), fill=SUAVE, anchor="ma")
    return pag


def solto(nome, arquivo, fundo):
    """O PDF de uma versão só: a página é o próprio logo, com respiro."""
    logo = Image.open(os.path.join(MARCA, arquivo)).convert("RGBA")
    esc = 1200.0 / logo.size[0]
    logo = logo.resize((int(logo.size[0] * esc), int(logo.size[1] * esc)),
                       Image.LANCZOS)
    margem = int(logo.size[1] * 0.45)
    pag = Image.new("RGB", (logo.size[0] + 2 * margem,
                            logo.size[1] + 2 * margem), fundo)
    pag.paste(logo, (margem, margem), logo)
    return pag


if __name__ == "__main__":
    os.makedirs(SAIDA, exist_ok=True)
    paginas = [capa()] + [pagina(*v) for v in VERSOES]
    folha = os.path.join(SAIDA, "Lucas-Martini-Logotipos.pdf")
    paginas[0].save(folha, "PDF", resolution=DPI, save_all=True,
                    append_images=paginas[1:])
    print(folha)

    for nome, arquivo, fundo, _, _ in VERSOES:
        p = solto(nome, arquivo, fundo)
        caminho = os.path.join(SAIDA, arquivo.replace(".png", ".pdf"))
        p.save(caminho, "PDF", resolution=DPI)
        print(caminho)
