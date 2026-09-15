#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revelacao de Essencia - Flavia Pereira Muccelin

Sistema visual editorial, minimalista:
  - fundo branco, margens largas (11% de cada lado)
  - hierarquia por ESCALA e PESO LEVE (Outfit Light), nao por negrito/caixa alta
  - FILETE no lugar de CAIXA: nada de cartao com borda e sombra
  - fotos SANGRANDO na lateral, tratadas como protagonistas
  - um unico acento quente, tirado das proprias fotos, usado com parcimonia

Base: SABRE_odonto.pptx, so para herdar o tema e as fontes Outfit
incorporadas (o desenho nao vem mais de la).
"""
import os

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

# ---------------------------------------------------------------- caminhos
BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets-revelacao")
MODELO = os.environ.get(
    "MODELO_PPTX",
    "/tmp/claude-0/-home-user-apresentacoes/74909cc6-46cb-52da-9161-fde6cae96c6d/"
    "scratchpad/work/destino-layout.pptx",
)
SAIDA = os.path.join(BASE, "Revelacao-de-Essencia-Flavia-Pereira-Muccelin.pptx")

LOGO = os.path.join(ASSETS, "logo-ka.png")
FOTO = {k: os.path.join(ASSETS, "foto_%s.jpg" % k) for k in "ABCDE"}

# ---------------------------------------------------------------- paleta
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)
TINTA = RGBColor(0x1C, 0x1C, 0x1A)   # titulos e frases
CORPO = RGBColor(0x6B, 0x6B, 0x66)   # corpo de texto
CLARO = RGBColor(0xA5, 0xA4, 0x9F)   # eyebrow, legenda, rodape
FIO = RGBColor(0xE2, 0xE1, 0xDD)     # filetes
NUM = RGBColor(0xD4, 0xD2, 0xCC)     # numeros grandes de apoio
ACENTO = RGBColor(0xA9, 0x72, 0x4A)  # terracota das fotos — uso minimo

# --------------------------------------------- tipografia (familia Outfit)
LIGHT = "Outfit 2 Light"
REG = "Outfit 2"
SEMI = "Outfit 2 Semi-Bold"
SANS = "Outfit 1"

EMU = 914400
LARG, ALT = 20.0, 11.25

# grade
ML, MR = 2.20, 17.80          # margens laterais
W = MR - ML                   # largura util = 15,6"
Y_EYE, Y_H1 = 1.75, 2.35      # topo do eyebrow e do titulo
Y_RODAPE = 10.45

MARCA = "FLÁVIA PEREIRA MUCCELIN"
DOC = "REVELAÇÃO DE ESSÊNCIA"

# ---------------------------------------------------------------- base
prs = Presentation(MODELO)

# Remove os slides do modelo preservando tema e fontes incorporadas. O export
# do Canva pendura os notesSlides tambem em presentation.xml; sem derrubar
# essas relacoes os slides antigos continuam alcancaveis e o pacote duplica.
for _rid, _rel in list(prs.part.rels.items()):
    if not _rel.is_external and "notesSlide" in str(_rel.target_part.partname):
        prs.part.drop_rel(_rid)
for _sldId in list(prs.slides._sldIdLst):
    prs.part.drop_rel(_sldId.rId)
    prs.slides._sldIdLst.remove(_sldId)
assert not [p for p in prs.part.package.iter_parts()
            if "/ppt/slides/" in str(p.partname)], "sobraram slides do modelo"

BLANK = next(l for l in prs.slide_layouts if l.name == "Blank")
_pagina = [0]


def E(v):
    return Emu(int(round(v * EMU)))


def slide():
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BRANCO
    _pagina[0] += 1
    return s


# ------------------------------------------------------------- primitivas
def fio(s, x, y, w, cor=FIO, esp=0.014):
    """Filete horizontal. Substitui a caixa como elemento de organizacao."""
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(esp))
    sp.fill.solid()
    sp.fill.fore_color.rgb = cor
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def fio_v(s, x, y, h, cor=FIO, esp=0.014):
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, E(x), E(y), E(esp), E(h))
    sp.fill.solid()
    sp.fill.fore_color.rgb = cor
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def ponto(s, cx, cy, d=0.11, cor=ACENTO):
    sp = s.shapes.add_shape(MSO_SHAPE.OVAL, E(cx - d / 2), E(cy - d / 2),
                            E(d), E(d))
    sp.fill.solid()
    sp.fill.fore_color.rgb = cor
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def anel(s, cx, cy, d, cor=FIO, esp=0.9):
    """Circulo de contorno fino — nunca preenchido."""
    sp = s.shapes.add_shape(MSO_SHAPE.OVAL, E(cx - d / 2), E(cy - d / 2),
                            E(d), E(d))
    sp.fill.background()
    sp.line.color.rgb = cor
    sp.line.width = Pt(esp)
    sp.shadow.inherit = False
    return sp


def caixa(s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def par(tf, primeiro=False, align=PP_ALIGN.LEFT, espaco=1.25):
    p = tf.paragraphs[0] if primeiro else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = espaco
    return p


def txt(p, texto, tam, cor, fonte=LIGHT, italic=False, spc=None):
    r = p.add_run()
    r.text = texto
    r.font.size = Pt(tam)
    r.font.name = fonte
    r.font.italic = italic
    r.font.color.rgb = cor
    # o peso vem do NOME da fonte (Light / Regular / Semi-Bold), nunca do
    # b="1" — negrito sintetico sobre a Outfit fica pastoso
    r.font.bold = False
    if spc is not None:
        r.font._rPr.set("spc", str(int(spc * 100)))
    return r


def bloco(s, x, y, w, itens, tam, cor, fonte=LIGHT, align=PP_ALIGN.LEFT,
          espaco=1.35, h=None, italic=False, spc=None):
    if isinstance(itens, str):
        itens = [itens]
    tf = caixa(s, x, y, w, h or (len(itens) * tam / 72.0 * espaco + 0.3))
    for i, t in enumerate(itens):
        txt(par(tf, primeiro=(i == 0), align=align, espaco=espaco),
            t, tam, cor, fonte, italic, spc)
    return tf


def foto(s, x, y, w, h, caminho):
    """Imagem cobrindo a caixa (center-crop). Sem canto arredondado: quase
    sempre ela sangra na borda do slide."""
    iw, ih = Image.open(caminho).size
    alvo, orig = w / h, iw / ih
    pic = s.shapes.add_picture(caminho, E(x), E(y), E(w), E(h))
    if orig > alvo:
        c = (1 - alvo / orig) / 2
        pic.crop_left = pic.crop_right = c
    elif orig < alvo:
        c = (1 - orig / alvo) / 2
        pic.crop_top = pic.crop_bottom = c
    return pic


# --------------------------------------------------------- blocos de pagina
def eyebrow(s, texto, x=ML, y=Y_EYE):
    bloco(s, x, y, 12.0, texto.upper(), 12.5, CLARO, SANS, spc=3.0, h=0.35)


def titulo(s, texto, x=ML, y=Y_H1, w=W, tam=46, cor=TINTA):
    """H1 em caixa baixa e peso leve. A forca vem do tamanho e do ar em volta."""
    return bloco(s, x, y, w, texto, tam, cor, LIGHT, espaco=1.12)


def rotulo(s, texto, x, y, w=6.0, cor=CLARO, tam=12.5):
    bloco(s, x, y, w, texto.upper(), tam, cor, SEMI, spc=2.2, h=0.30)


def rodape(s, x=ML, num=True):
    tf = caixa(s, x, Y_RODAPE, 11.0, 0.35)
    p = par(tf, True)
    txt(p, DOC, 10.5, CLARO, SANS, spc=2.4)
    txt(p, "   ·   ", 10.5, CLARO, SANS, spc=2.4)
    txt(p, MARCA, 10.5, CLARO, SANS, spc=2.4)
    if num:
        tf = caixa(s, 15.80, Y_RODAPE, 2.00, 0.35)
        txt(par(tf, True, align=PP_ALIGN.RIGHT), "%02d" % _pagina[0], 10.5,
            CLARO, SANS, spc=1.6)


def pagina(rot, tit, tam=46, x=ML, w=W, y_eye=Y_EYE, y_tit=Y_H1, com_fio=True):
    s = slide()
    eyebrow(s, rot, x, y_eye)
    n = len(tit) if isinstance(tit, list) else 1
    titulo(s, tit, x, y_tit, w, tam)
    if com_fio:
        fio(s, x, y_tit + n * tam / 72.0 * 1.12 + 0.42, w)
    return s


def divisor(numero, nome):
    """Pagina de virada de tema: quase vazia, nome em caixa baixa e peso leve."""
    s = slide()
    bloco(s, ML, 4.35, 4.0, numero, 13, ACENTO, SEMI, spc=3.0, h=0.35)
    bloco(s, ML, 4.95, W, nome, 94, TINTA, LIGHT, espaco=1.0)
    fio(s, ML, 7.35, W)
    rodape(s)
    return s



def seta(s, cx, y, h=0.42):
    """Descida vertical entre etapas, no lugar da flecha."""
    fio_v(s, cx, y, h, FIO, esp=0.018)


def citacao(s, x, y, w, texto, rot=None, tam=28):
    """Fala da Flavia: aspas em acento + frase em caixa baixa."""
    if rot:
        bloco(s, x, y, w, rot, 17, CLARO, LIGHT, h=0.35)
        y += 0.45
    bloco(s, x, y, 1.0, "“", 56, ACENTO, LIGHT, h=0.7)
    bloco(s, x + 0.62, y + 0.12, w - 0.7, texto, tam, TINTA, LIGHT,
          espaco=1.25, h=0.9)


# =====================================================================
# 01 — CAPA
# =====================================================================
s = slide()
foto(s, 9.60, 0, 10.40, ALT, FOTO["A"])
eyebrow(s, "Método Marca com Essência ©", ML, 1.95)
bloco(s, ML, 3.85, 7.4, ["Revelação", "de Essência"], 82, TINTA, LIGHT,
      espaco=1.04)
fio(s, ML, 6.95, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 7.45, 7.0, "Flávia Pereira Muccelin", 20, TINTA, SEMI, spc=2.4,
      h=0.4)
bloco(s, ML, 8.10, 6.9,
      "A essência da Flávia como fundadora e os padrões que estão na origem "
      "da Forma e da My Home.", 18.5, CORPO, LIGHT, espaco=1.45, h=1.6)
s.shapes.add_picture(LOGO, E(ML), E(9.95), E(1.85), E(1.85 * 183 / 777))

# =====================================================================
# 02 — SUMÁRIO
# =====================================================================
SECOES = [
    ("01", "A origem",
     "As experiências que formaram a visão de mundo da Flávia."),
    ("02", "As tensões", "Os momentos que a colocaram em movimento."),
    ("03", "Os padrões", "A lógica que se repete ao longo da trajetória."),
    ("04", "O Ikigai", "O que gera sentido e realização para a Flávia."),
    ("05", "A essência", "O princípio que conecta a sua história."),
    ("06", "As marcas",
     "Como essa essência se manifesta na origem da Forma e da My Home."),
]

s = slide()
eyebrow(s, "Sumário")
for i, (n, nome, desc) in enumerate(SECOES):
    y = 2.45 + i * 1.24
    fio(s, ML, y, 13.6)
    bloco(s, ML, y + 0.40, 1.2, n, 13, ACENTO, SEMI, spc=2.4, h=0.3)
    bloco(s, ML + 1.70, y + 0.28, 11.6, nome, 30, TINTA, LIGHT, espaco=1.1,
          h=0.6)
    bloco(s, ML + 1.70, y + 0.86, 11.6, desc, 17, CLARO, LIGHT, h=0.4)
fio(s, ML, 2.45 + len(SECOES) * 1.24, 13.6)
rodape(s)

# =====================================================================
# 03 — Por que começamos pela essência?
# =====================================================================
s = pagina("Conceito", "Por que começamos pela essência?")
bloco(s, ML, 4.15, 13.4,
      "A Forma e a My Home são negócios distintos, mas nasceram e se "
      "desenvolveram a partir da visão de uma mesma fundadora.",
      24, TINTA, LIGHT, espaco=1.45, h=1.3)
bloco(s, ML, 5.65, 13.4,
      "Em marcas fortemente ligadas à fundadora, compreender a história de "
      "quem as criou ajuda a identificar crenças, princípios e formas de "
      "pensar e agir que influenciaram a construção dos negócios.",
      19, CORPO, LIGHT, espaco=1.5, h=1.6)
fio(s, ML, 7.60, W)
rotulo(s, "O que não é", ML, 8.00)
bloco(s, ML, 8.50, 6.8,
      "Uma análise psicológica da Flávia.", 23, CORPO, LIGHT, espaco=1.35,
      h=1.2)
fio_v(s, 9.80, 8.00, 1.70)
rotulo(s, "O que é", 10.80, 8.00)
bloco(s, 10.80, 8.50, 7.0,
      "A investigação da origem identitária das marcas a partir da fundadora.",
      23, TINTA, LIGHT, espaco=1.35, h=1.2)
rodape(s)

# =====================================================================
# 04 — A pergunta que conduz esta etapa
# =====================================================================
s = slide()
eyebrow(s, "A pergunta que conduz esta etapa", ML, 3.90)
bloco(s, ML, 4.60, 15.2,
      ["O que já fazia parte de quem a Flávia é",
       "antes da Forma e da My Home?"], 56, TINTA, LIGHT, espaco=1.24)
rodape(s)

# =====================================================================
# 05 — Como chegamos à revelação
# =====================================================================
s = pagina("Método", "Como chegamos à revelação")
bloco(s, ML, 4.05, 13.6,
      "A essência não é definida por uma característica isolada. Ela se "
      "revela quando diferentes momentos da trajetória apresentam uma mesma "
      "lógica.", 21, CORPO, LIGHT, espaco=1.45, h=1.3)

dimensoes = [
    ("História", "Mostra as experiências e as referências que formaram a "
                 "visão de mundo da Flávia."),
    ("Tensões", "Mostram os momentos em que aquilo que existia entrou em "
                "conflito com aquilo que ela desejava ou conseguia enxergar."),
    ("Padrões", "Revelam como a Flávia responde, repetidamente, a essas "
                "situações."),
    ("Ikigai", "Revela o que gera sentido, realização e vontade de "
               "contribuir."),
]
COL, GAP = 3.45, 0.60
for i, (tit, desc) in enumerate(dimensoes):
    x = ML + i * (COL + GAP)
    fio(s, x, 5.60, COL)
    bloco(s, x, 5.90, COL, tit, 24, TINTA, LIGHT, espaco=1.1, h=0.6)
    bloco(s, x, 6.60, COL, desc, 17, CORPO, LIGHT, espaco=1.45, h=2.0)

tf = caixa(s, ML, 8.80, W, 0.7)
p = par(tf, True, align=PP_ALIGN.CENTER)
for i, palavra in enumerate(["História", "tensões", "padrões", "Ikigai"]):
    if i:
        txt(p, "  +  ", 26, ACENTO, LIGHT)
    txt(p, palavra, 26, CORPO, LIGHT)
txt(p, "  =  ", 26, ACENTO, LIGHT)
txt(p, "essência", 26, TINTA, SEMI)
bloco(s, ML, 9.50, W,
      "A essência é o princípio central que conecta essas dimensões e revela "
      "a lógica que orienta a forma como a Flávia enxerga, age e transforma.",
      16, CLARO, LIGHT, align=PP_ALIGN.CENTER, h=0.5)
rodape(s)

# =====================================================================
# 06 — DIVISOR
# =====================================================================
divisor("01", "A origem")

# =====================================================================
# 07 — Onde essa história começa
# =====================================================================
s = slide()
foto(s, 11.60, 0, 8.40, ALT, FOTO["B"])
eyebrow(s, "A origem")
titulo(s, "Onde essa história começa", ML, Y_H1, 8.6, 42)
fio(s, ML, 3.45, 8.6)
bloco(s, ML, 3.85, 8.4,
      "A história familiar da Flávia é marcada por escassez, trabalho, fé e "
      "recomeços.", 22, TINTA, LIGHT, espaco=1.4, h=1.3)
bloco(s, ML, 5.30, 8.4,
      "A família deixou Guiratinga e foi para Primavera do Leste em busca de "
      "uma vida melhor. O pai da Flávia passou a trabalhar como caseiro "
      "justamente na propriedade onde, décadas depois, ela viveria como "
      "proprietária.", 18, CORPO, LIGHT, espaco=1.5, h=2.2)
bloco(s, ML, 7.70, 8.4,
      "A Flávia chegou àquele lugar como “a filha do peão”.",
      22, TINTA, LIGHT, espaco=1.35, h=0.9)
fio(s, ML, 9.10, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 9.45, 8.4,
      "TRABALHO   ·   FAMÍLIA   ·   FÉ   ·   HONESTIDADE   ·   GRATIDÃO",
      11.5, CLARO, SEMI, spc=2.0, h=0.4)
rodape(s, num=False)

# =====================================================================
# 08 — Os primeiros sinais
# =====================================================================
s = slide()
foto(s, 0, 0, 8.60, ALT, FOTO["C"])
X2 = 10.00
eyebrow(s, "A origem", X2, 1.75)
titulo(s, "Os primeiros sinais", X2, 2.35, 8.0, 42)
fio(s, X2, 3.45, 8.0)
bloco(s, X2, 3.85, 7.9,
      "A vontade de construir uma realidade diferente aparece muito antes da "
      "criação das empresas.", 20, TINTA, LIGHT, espaco=1.4, h=1.2)
bloco(s, X2, 5.05, 7.9,
      "Ainda criança, a Flávia acompanhava o pai no garimpo e chegou a "
      "cozinhar para os trabalhadores. Mais tarde, ia de bicicleta da chácara "
      "até o centro para trabalhar. Também estudava e jogava futsal para "
      "conquistar uma bolsa que ajudasse a manter a faculdade.",
      17.5, CORPO, LIGHT, espaco=1.5, h=2.1)
citacao(s, X2, 7.05, 7.9, "Eu não quero isso para mim.",
        rot="Ela mesma diz:", tam=25)
citacao(s, X2, 8.35, 7.9, "Eu queria mais.",
        rot="E, mais tarde, ao perceber que o cargo limitaria o seu "
            "crescimento:", tam=25)
rodape(s, x=X2, num=False)

# =====================================================================
# 09 — As experiências que a formaram
# =====================================================================
FORMACAO = [
    ("01", "A escassez",
     "A Flávia cresceu em uma realidade de poucos recursos.",
     "A vontade de ampliar possibilidades e não aceitar a condição presente "
     "como limite."),
    ("02", "O portão",
     "Ainda adolescente, a Flávia entrava escondida na casa dos donos da "
     "fazenda onde o pai trabalhava e se imaginava vivendo aquela realidade. "
     "Anos depois, tornou-se proprietária daquele mesmo lugar.",
     "A capacidade de se enxergar dentro de uma realidade antes de ela "
     "existir concretamente."),
    ("03", "O trabalho e o estudo",
     "Trabalho, faculdade, bicicleta e futsal como caminho para conquistar "
     "uma bolsa de estudos.",
     "Para a Flávia, enxergar uma possibilidade exige movimento para "
     "torná-la real."),
    ("04", "A trajetória dos pais",
     "A Flávia cresceu vendo os pais recomeçarem sem abandonar a honestidade, "
     "a fé, o trabalho e a família.",
     "A forma de construir importa tanto quanto aquilo que é conquistado."),
]

# Duas experiencias por pagina: com quatro no mesmo slide o bloco "o que isso
# revela" nao tinha ar e a leitura virava parede de texto.
for parte in (0, 1):
    s = pagina("A origem", "As experiências que a formaram")
    for i, (n, tit, fato, revela) in enumerate(FORMACAO[parte * 2:parte * 2 + 2]):
        x = ML + i * 8.20
        fio(s, x, 4.30, 7.40)
        bloco(s, x, 4.62, 1.0, n, 13, ACENTO, SEMI, spc=2.4, h=0.3)
        bloco(s, x + 1.20, 4.50, 6.2, tit, 26, TINTA, LIGHT, espaco=1.1, h=0.6)
        bloco(s, x + 1.20, 5.35, 6.2, fato, 18.5, CORPO, LIGHT, espaco=1.5,
              h=2.2)
        fio(s, x + 1.20, 7.75, 1.10, ACENTO, esp=0.03)
        rotulo(s, "O que isso revela", x + 1.20, 8.10, 6.2)
        bloco(s, x + 1.20, 8.60, 6.2, revela, 19, TINTA, LIGHT, espaco=1.5,
              h=1.4)
    rodape(s)

# =====================================================================
# 10 — DIVISOR
# =====================================================================
divisor("02", "As tensões")

# =====================================================================
# 11 — As tensões que a colocaram em movimento
# =====================================================================
s = pagina("As tensões", "As tensões que a colocaram em movimento",
           com_fio=False)
bloco(s, ML, 3.40, 13.0,
      "Existe uma lógica recorrente na trajetória da Flávia.", 19, CLARO,
      LIGHT, h=0.45)
tensoes = [
    ("A realidade dizia", "“Essa é a sua condição.”",
     "A Flávia enxergava outra."),
    ("O cargo dizia", "“Até aqui você pode chegar.”", "A Flávia queria mais."),
    ("As marcas prontas diziam", "“É assim que deve ser feito.”",
     "A Flávia queria fazer do seu jeito."),
    ("A maternidade exigiu uma escolha",
     "Conciliar a maternidade e o empreendedorismo não era possível como "
     "ela desejava naquele momento.",
     "Ela parou e, anos depois, construiu um caminho de volta."),
    ("As sobras tinham um destino", "“O descarte.”",
     "A Flávia enxergou matéria para uma nova criação."),
]
# a linha da maternidade traz um relato, nao uma fala: precisa de mais altura
ALTURAS = [1.00, 1.00, 1.00, 1.30, 1.00]
y = 4.00
for i, (rot, fala, resp) in enumerate(tensoes):
    fio(s, ML, y, W)
    rotulo(s, rot, ML, y + 0.34, 4.6)
    bloco(s, 7.00, y + 0.24, 5.4, fala, 17.5, CORPO, LIGHT,
          italic=(i != 3), espaco=1.4, h=1.2)
    fio(s, 12.60, y + 0.48, 0.42, CLARO, esp=0.018)
    bloco(s, 13.35, y + 0.22, 4.5, resp, 20, TINTA, LIGHT, espaco=1.3, h=0.9)
    y += ALTURAS[i]
fio(s, ML, y, W)
bloco(s, ML, y + 0.38, 15.0,
      "Quando aquilo que está dado não corresponde ao que a Flávia enxerga "
      "como possível, ela entra em movimento.", 19, TINTA, LIGHT, h=0.5)
rodape(s)

# =====================================================================
# 12 — DIVISOR
# =====================================================================
divisor("03", "Os padrões")

# =====================================================================
# 13 — O padrão invisível
# =====================================================================
s = slide()
foto(s, 11.60, 0, 8.40, ALT, FOTO["D"])
eyebrow(s, "Os padrões")
titulo(s, "O padrão invisível", ML, Y_H1, 8.6, 42)
fio(s, ML, 3.45, 8.6)
bloco(s, ML, 3.85, 8.4,
      "As situações são diferentes. A resposta da Flávia segue a mesma "
      "lógica.", 20, CLARO, LIGHT, espaco=1.4, h=1.1)
etapas = ["Ela encontra uma realidade ou um limite.",
          "Enxerga que aquilo pode ser diferente.",
          "Constrói um caminho para transformar essa possibilidade em "
          "realidade."]
for i, e in enumerate(etapas):
    y = 5.05 + i * 1.32
    ponto(s, ML + 0.06, y + 0.20, 0.11)
    bloco(s, ML + 0.60, y, 7.8, e, 21, TINTA, LIGHT, espaco=1.3, h=0.9)
    if i < 2:
        seta(s, ML + 0.06, y + 0.46, 0.60)
fio(s, ML, 9.10, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 9.45, 8.4,
      "O padrão está na forma como a Flávia responde quando percebe que "
      "existe uma possibilidade além daquilo que está dado.",
      17, CORPO, LIGHT, espaco=1.4, h=0.9)
rodape(s, num=False)

# =====================================================================
# 14 — O movimento que se repete
# =====================================================================
s = pagina("Os padrões", "O movimento que se repete")
passos = [["Enxerga a realidade", "como ela é"],
          ["Percebe que aquilo", "não precisa", "ser definitivo"],
          ["Enxerga outra", "possibilidade"],
          ["Procura", "um caminho"],
          ["Busca conhecimento,", "mobiliza pessoas", "e recursos"],
          ["Transforma a", "possibilidade", "em realidade"]]
X0, PASSO = 3.20, 2.72
fio(s, X0, 5.35, PASSO * 5)
for i, blk in enumerate(passos):
    cx = X0 + i * PASSO
    ponto(s, cx, 5.35, 0.13, ACENTO if i == 5 else CLARO)
    bloco(s, cx - 1.25, 5.80, 2.50, blk, 17,
          TINTA if i == 5 else CORPO, LIGHT if i < 5 else REG,
          align=PP_ALIGN.CENTER, espaco=1.35, h=1.6)
fio(s, ML, 8.10, 1.30, ACENTO, esp=0.03)
tf = caixa(s, ML, 8.55, W, 0.8)
p = par(tf, True, espaco=1.3)
txt(p, "Enxergar além", 30, TINTA, LIGHT)
txt(p, "   →   ", 30, ACENTO, LIGHT)
txt(p, "colocar em movimento", 30, TINTA, LIGHT)
txt(p, "   →   ", 30, ACENTO, LIGHT)
txt(p, "fazer existir", 30, TINTA, LIGHT)
rodape(s)

# =====================================================================
# 15 — A linha mestra da história
# =====================================================================
s = slide()
eyebrow(s, "Os padrões", ML, 2.05)
bloco(s, ML, 2.55, 13.0,
      "Ao longo da sua trajetória, a Flávia repete um mesmo movimento:",
      19, CLARO, LIGHT, h=0.45)
bloco(s, ML, 3.35, 15.4,
      ["A Flávia não aceita que aquilo que existe",
       "determine aquilo que pode existir."], 52, TINTA, LIGHT, espaco=1.24)
fio(s, ML, 6.15, W)
bloco(s, ML, 6.60, 8.0,
      "Essa lógica aparece em contextos completamente diferentes da sua vida.",
      18, CORPO, LIGHT, espaco=1.45, h=1.0)
for i, t in enumerate(["Muda a situação.", "Muda o desafio.",
                       "Muda o que precisa ser construído."]):
    bloco(s, 10.60, 6.60 + i * 0.46, 7.2, t, 18, CLARO, LIGHT, h=0.4)
fio(s, ML, 8.55, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 8.95, 15.0,
      "A Flávia vê aquilo que existe, mas também enxerga o que aquilo ainda "
      "pode se tornar.", 26, TINTA, LIGHT, espaco=1.35, h=1.0)
rodape(s)

# =====================================================================
# 16 — DIVISOR
# =====================================================================
divisor("04", "O Ikigai")

# =====================================================================
# 17 — O que move a Flávia?
# =====================================================================
s = slide()
foto(s, 0, 0, 8.60, ALT, FOTO["A"])
eyebrow(s, "O Ikigai", X2, 1.85)
titulo(s, "O que move a Flávia?", X2, 2.45, 8.0, 44)
fio(s, X2, 3.60, 8.0)
bloco(s, X2, 4.00, 7.9,
      "Até aqui, a história revelou como a Flávia responde à realidade e "
      "entra em movimento. O Ikigai acrescenta outra dimensão: o que faz "
      "esse movimento ter sentido para ela.", 18, CORPO, LIGHT, espaco=1.5,
      h=1.8)
for i, q in enumerate(["O que a Flávia ama?",
                       "No que reconhece as suas forças?",
                       "Onde encontra realização?",
                       "Como deseja contribuir para outras pessoas?"]):
    y = 6.05 + i * 0.62
    ponto(s, X2 + 0.06, y + 0.14, 0.10, CLARO)
    bloco(s, X2 + 0.55, y, 7.3, q, 20, TINTA, LIGHT, h=0.45)
fio(s, X2, 8.85, 1.30, ACENTO, esp=0.03)
bloco(s, X2, 9.25, 7.9,
      "Não buscamos apenas aquilo que ela gosta de fazer, e sim o que faz uma "
      "realização ter significado para a Flávia.", 17, CORPO, LIGHT,
      espaco=1.45, h=0.9)
rodape(s, x=X2, num=False)

# =====================================================================
# 18 — O mapa do Ikigai
# =====================================================================
s = pagina("O Ikigai", "O mapa do Ikigai")
mapa = [
    ("O que a Flávia ama",
     "A família. As pessoas. Os momentos de qualidade. As conversas e as "
     "trocas verdadeiras. As conexões."),
    ("No que a Flávia é boa",
     "No conhecimento que construiu. Na persuasão. Na seriedade. Na "
     "persistência. No domínio daquilo que vende. Na capacidade de envolver "
     "pessoas."),
    ("Como a Flávia gosta de contribuir",
     "Sendo útil. Compartilhando conhecimentos e experiências. Ajudando "
     "pessoas e empresários. Criando oportunidades. Fazendo diferença na vida "
     "das pessoas."),
    ("Onde a Flávia encontra realização",
     "Ao ver algo ganhar forma. Ao transformar matéria em algo de valor. Ao "
     "perceber a alegria do cliente. Ao ver o sonho de outra pessoa se tornar "
     "concreto. Ao saber que aquilo que construiu também ampliou as "
     "possibilidades de alguém."),
]
for i, (rot, itens) in enumerate(mapa):
    x = ML + i * (COL + GAP)
    fio(s, x, 4.55, COL)
    bloco(s, x, 4.88, COL, rot, 20, TINTA, LIGHT, espaco=1.15, h=1.0)
    bloco(s, x, 6.00, COL, itens, 17, CORPO, LIGHT, espaco=1.5, h=3.4)
rodape(s)

# =====================================================================
# 19 — O centro do Ikigai
# =====================================================================
s = pagina("O Ikigai", "O centro do Ikigai")
bloco(s, ML, 4.15, 13.4,
      "A Flávia não se realiza apenas conquistando para si. Ela encontra "
      "realização quando vê uma possibilidade se tornar concreta e produzir "
      "algo na vida de outras pessoas.", 22, TINTA, LIGHT, espaco=1.45, h=1.8)
fio(s, ML, 6.25, W)
for i, ex in enumerate(["Um cliente realiza um sonho.", "Uma equipe cresce.",
                        "Uma ideia sai do papel.",
                        "Uma pessoa recebe uma oportunidade."]):
    x = ML + i * (COL + GAP)
    bloco(s, x, 6.65, COL, ex, 18, CORPO, LIGHT, espaco=1.4, h=1.0)
citacao(s, ML, 8.05, 9.0, "Fazer diferença na vida das pessoas.",
        rot="Sobre o legado que deseja deixar, a própria Flávia resume:",
        tam=26)
bloco(s, 11.40, 8.55, 6.4,
      "A Flávia também deseja criar uma fundação para oferecer uma profissão "
      "a crianças.", 17, CLARO, LIGHT, espaco=1.45, h=1.0)
rodape(s)

# =====================================================================
# 20 — A razão de ser
# =====================================================================
s = slide()
eyebrow(s, "O Ikigai")
bloco(s, ML, 2.35, 3.0, "RAZÃO DE SER", 12.5, ACENTO, SEMI, spc=2.4, h=0.3)
bloco(s, ML, 3.05, 15.2,
      ["Transformar possibilidades em realizações",
       "concretas que também ampliem a vida",
       "de outras pessoas."], 44, TINTA, LIGHT, espaco=1.24)
fio(s, ML, 6.35, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 6.75, 14.0,
      "A realização ganha sentido quando aquilo que a Flávia constrói também "
      "amplia possibilidades para outras pessoas.", 19, CORPO, LIGHT,
      espaco=1.45, h=0.7)
foto(s, 0, 7.70, LARG, ALT - 7.70, FOTO["E"])

# =====================================================================
# 21 — DIVISOR
# =====================================================================
divisor("05", "A essência")

# =====================================================================
# 22 — Onde a história e o Ikigai se encontram
# =====================================================================
s = pagina("A essência", "Onde a história e o Ikigai se encontram")
bloco(s, ML, 4.05, 13.6,
      "A história revela como a Flávia se movimenta. O Ikigai revela o que dá "
      "sentido a esse movimento. Lado a lado, a mesma lógica aparece.",
      20, CORPO, LIGHT, espaco=1.45, h=1.2)
encontro = [
    ("Visão", "A Flávia enxerga além da condição presente."),
    ("Movimento", "A distância entre aquilo que existe e aquilo que ela "
                  "enxerga como possível a leva a buscar caminhos, "
                  "conhecimento, pessoas e recursos."),
    ("Pessoas", "A família, a equipe, os clientes e as relações fazem parte "
                "daquilo que dá significado às suas realizações."),
    ("Impacto", "A conquista ganha mais sentido quando aquilo que ela "
                "constrói também amplia possibilidades para outras pessoas."),
]
for i, (rot, desc) in enumerate(encontro):
    x = ML + i * (COL + GAP)
    fio(s, x, 5.60, COL)
    bloco(s, x, 5.92, COL, rot, 22, TINTA, LIGHT, espaco=1.1, h=0.5)
    bloco(s, x, 6.55, COL, desc, 17, CORPO, LIGHT, espaco=1.5, h=2.4)
tf = caixa(s, ML, 9.15, W, 0.7)
p = par(tf, True, align=PP_ALIGN.CENTER)
txt(p, "Enxergar além.", 26, TINTA, LIGHT)
txt(p, "   ·   ", 26, ACENTO, LIGHT)
txt(p, "Colocar em movimento.", 26, TINTA, LIGHT)
txt(p, "   ·   ", 26, ACENTO, LIGHT)
txt(p, "Fazer existir.", 26, TINTA, LIGHT)
rodape(s)

# =====================================================================
# 23 — A essência da Flávia como fundadora
# =====================================================================
s = slide()
eyebrow(s, "A essência da Flávia como fundadora")
bloco(s, ML, 2.35, 15.4,
      ["Enxergar além do que está posto e fazer",
       "existir o que ainda é possibilidade."], 52, TINTA, LIGHT, espaco=1.2)
fio(s, ML, 5.55, W)
camadas = [
    ("Enxergar além", "A Flávia não considera a realidade presente como a "
                      "única possibilidade. Ela consegue enxergar aquilo que "
                      "ainda pode existir."),
    ("Fazer existir", "Ela não permanece apenas no campo da imaginação. "
                      "Procura caminhos e transforma a possibilidade em "
                      "realidade."),
    ("Ampliar possibilidades", "A realização ganha sentido quando aquilo que "
                               "ela constrói também cria valor, oportunidade "
                               "ou transformação para outras pessoas."),
]
LC, LG = 4.80, 0.60
for i, (rot, desc) in enumerate(camadas):
    x = ML + i * (LC + LG)
    rotulo(s, rot, x, 6.00, LC)
    bloco(s, x, 6.50, LC, desc, 18, CORPO, LIGHT, espaco=1.5, h=2.2)
fio(s, ML, 8.75, W)
bloco(s, ML, 9.15, 15.2,
      "Forte, determinada, criativa, sonhadora e visionária são "
      "características da Flávia. Mas são manifestações de uma lógica mais "
      "profunda: enxergar além e fazer existir.", 18, TINTA, LIGHT,
      espaco=1.45, h=0.9)
rodape(s)

# =====================================================================
# 24 — DIVISOR
# =====================================================================
divisor("06", "As marcas")

# =====================================================================
# 25 — Como essa essência se manifesta nas marcas
# =====================================================================
s = pagina("As marcas", "Como essa essência se manifesta nas marcas")
bloco(s, ML, 4.05, 13.0,
      "Uma mesma essência. Duas manifestações diferentes.", 22, CLARO, LIGHT,
      h=0.6)
fio(s, ML, 4.95, W)
rotulo(s, "A Forma", ML, 5.35, 7.0, cor=ACENTO)
bloco(s, ML, 5.85, 7.0, "Dar forma ao que ainda é ideia.", 27, TINTA, LIGHT,
      espaco=1.2, h=0.8)
bloco(s, ML, 6.85, 7.0,
      "A empresa representa o espaço que a Flávia buscava para criar, "
      "personalizar e construir segundo a sua própria visão. Esse mesmo "
      "movimento está na natureza do negócio: uma necessidade, uma ideia ou "
      "um sonho se transformam em projeto e ganham forma concreta.",
      17, CORPO, LIGHT, espaco=1.5, h=2.6)
fio_v(s, 9.80, 5.35, 3.80)
rotulo(s, "A My Home", 10.80, 5.35, 7.0, cor=ACENTO)
bloco(s, 10.80, 5.85, 7.0, "Reabrir possibilidades.", 27, TINTA, LIGHT,
      espaco=1.2, h=0.8)
bloco(s, 10.80, 6.85, 7.0,
      "A marca nasce quando a Flávia questiona o destino dado às sobras da "
      "marcenaria. Onde havia descarte, ela enxergou matéria. Onde havia fim, "
      "ela enxergou um novo começo. Aquilo que havia encerrado a sua função "
      "ganhou uma nova possibilidade de existir.",
      17, CORPO, LIGHT, espaco=1.5, h=2.6)
bloco(s, ML, 9.30, 15.2,
      "A Forma e a My Home são marcas diferentes e terão estratégias "
      "próprias. Mas as duas carregam, na origem, uma mesma forma de enxergar "
      "e transformar a realidade.", 17, CLARO, LIGHT, espaco=1.45, h=0.6)
rodape(s)

# =====================================================================
# 26 — Da essência à estratégia
# =====================================================================
s = pagina("Próxima etapa", "Da essência à estratégia")
bloco(s, ML, 4.15, 13.4,
      "Esta etapa revelou a essência da Flávia como fundadora: uma forma "
      "própria de enxergar e transformar a realidade que já existia antes da "
      "Forma e da My Home.", 21, CORPO, LIGHT, espaco=1.5, h=1.6)
fio(s, ML, 6.10, W)
rotulo(s, "O que vem a seguir", ML, 6.50)
bloco(s, ML, 7.00, 15.2,
      "Essa essência ajuda a compreender de onde as duas marcas vêm, mas não "
      "define, sozinha, quem cada marca precisa ser.", 20, CORPO, LIGHT,
      espaco=1.45, h=1.2)
bloco(s, ML, 8.35, 15.2,
      "A Base Estratégica vai definir como essa origem se traduz em uma "
      "direção própria, relevante e diferenciada para a Forma e para a "
      "My Home.", 24, TINTA, LIGHT, espaco=1.4, h=1.6)
rodape(s)

# =====================================================================
# 27 — FECHO
# =====================================================================
s = slide()
fio(s, ML, 4.55, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 5.05, 15.2,
      ["A essência revela a origem.", "A estratégia define a direção."],
      54, TINTA, LIGHT, espaco=1.3)
s.shapes.add_picture(LOGO, E(ML), E(9.90), E(1.85), E(1.85 * 183 / 777))

# ---------------------------------------------------------------- salvar
prs.save(SAIDA)
print("OK ->", SAIDA, len(prs.slides._sldIdLst), "slides")
