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
      "História, Ikigai e os padrões que existem na origem da Forma e da "
      "My Home.", 18.5, CORPO, LIGHT, espaco=1.45, h=1.4)
s.shapes.add_picture(LOGO, E(ML), E(9.95), E(1.85), E(1.85 * 183 / 777))

# =====================================================================
# 02 — SUMÁRIO
# =====================================================================
SECOES = [("01", "Metodologia"), ("02", "História"),
          ("03", "A linha-mestra da história"), ("04", "Ikigai"),
          ("05", "A essência")]

s = slide()
eyebrow(s, "Sumário")
for i, (n, nome) in enumerate(SECOES):
    y = 2.90 + i * 1.46
    fio(s, ML, y, 13.6)
    bloco(s, ML, y + 0.42, 1.2, n, 13, ACENTO, SEMI, spc=2.4, h=0.3)
    bloco(s, ML + 1.70, y + 0.24, 11.0, nome, 38, TINTA, LIGHT, espaco=1.1)
fio(s, ML, 2.90 + len(SECOES) * 1.46, 13.6)
rodape(s)

# =====================================================================
# 03 — A PERGUNTA QUE NOS GUIA
# =====================================================================
s = slide()
eyebrow(s, "A pergunta que nos guia", ML, 3.60)
bloco(s, ML, 4.35, 15.0,
      ["O que existe em Flávia", "antes mesmo de existirem",
       "a Forma e a My Home?"], 58, TINTA, LIGHT, espaco=1.22)
rodape(s)

# =====================================================================
# 04 — DIVISOR
# =====================================================================
divisor("01", "Metodologia")

# =====================================================================
# 05 — Por que começamos pela essência
# =====================================================================
s = pagina("Conceito", "Por que começamos pela essência")
bloco(s, ML, 4.25, 12.6,
      "Em marcas fortemente ligadas à fundadora, compreender a sua história "
      "ajuda a identificar as crenças, os padrões e os princípios que podem "
      "ter influenciado a criação, a cultura e a expressão das marcas.",
      24, CORPO, LIGHT, espaco=1.5, h=2.6)
fio(s, ML, 7.05, W)
rotulo(s, "O que não é", ML, 7.45)
bloco(s, ML, 7.95, 6.6, "Não estamos fazendo uma análise psicológica.",
      26, CORPO, LIGHT, espaco=1.35, h=1.6)
fio_v(s, 9.80, 7.45, 2.10)
rotulo(s, "O que é", 10.80, 7.45)
bloco(s, 10.80, 7.95, 7.0,
      "Estamos investigando a origem identitária da Forma e da My Home.",
      26, TINTA, LIGHT, espaco=1.35, h=1.6)
rodape(s)

# =====================================================================
# 06 — Como essa etapa contribui para o branding
# =====================================================================
s = pagina("Método", "Como essa etapa contribui para o branding")
etapas = [("01", "História", "Revela as referências e as crenças de origem."),
          ("02", "Ikigai", "Revela as motivações e a razão de ser."),
          ("03", "Padrões", "Revela as formas recorrentes de agir e de decidir."),
          ("04", "Essência", "Sintetiza aquilo que pode estar na raiz das marcas.")]
COL, GAP = 3.45, 0.60
for i, (n, tit, desc) in enumerate(etapas):
    x = ML + i * (COL + GAP)
    fio(s, x, 4.45, COL)
    bloco(s, x, 4.75, COL, n, 54, NUM, LIGHT, h=1.1)
    bloco(s, x, 6.00, COL, tit, 22, TINTA, REG, espaco=1.1, h=0.5)
    bloco(s, x, 6.60, COL, desc, 19, CORPO, LIGHT, espaco=1.45, h=2.0)
fio(s, ML, 8.95, W)
rotulo(s, "Na etapa seguinte", ML, 9.30, cor=ACENTO)
bloco(s, 6.20, 9.22, 11.6,
      "A Base Estratégica determinará o que disso deve se transformar em "
      "estratégia para cada marca.", 19, CORPO, LIGHT, espaco=1.4, h=0.9)
rodape(s)

# =====================================================================
# 07 — Como chegamos à revelação
# =====================================================================
s = slide()
eyebrow(s, "Modelo")
titulo(s, "Como chegamos à revelação")
fio(s, ML, 3.55, W)

tf = caixa(s, ML, 4.90, W, 1.0)
p = par(tf, True, align=PP_ALIGN.CENTER)
for i, palavra in enumerate(["História", "Ikigai", "Padrões recorrentes"]):
    if i:
        txt(p, "     +     ", 34, ACENTO, LIGHT)
    txt(p, palavra, 34, CORPO, LIGHT)
fio(s, 9.30, 6.35, 1.40)
bloco(s, ML, 6.85, W, "Hipótese de essência", 58, TINTA, LIGHT,
      align=PP_ALIGN.CENTER, espaco=1.1)
bloco(s, 4.00, 8.60, 12.0,
      "A apresentação cruza a trajetória, a razão de ser e o comportamento "
      "recorrente para revelar a raiz que antecede as marcas.",
      19, CLARO, LIGHT, align=PP_ALIGN.CENTER, espaco=1.45, h=1.2)
rodape(s)

# =====================================================================
# 08 — DIVISOR
# =====================================================================
divisor("02", "História")

# =====================================================================
# 09 — Onde essa história começa
# =====================================================================
s = slide()
foto(s, 11.60, 0, 8.40, ALT, FOTO["B"])
eyebrow(s, "História")
titulo(s, "Onde essa história começa", ML, Y_H1, 8.6, 42)
fio(s, ML, 3.45, 8.6)
itens = [("Origem", "Família muito humilde, mudança para Primavera do Leste, "
                    "fé, trabalho e recomeço."),
         ("Contexto", "O pai trabalhando como caseiro/vaqueiro, a mãe "
                      "presente, a rotina de esforço e honestidade."),
         ("Marca inicial", "Desde cedo, a realidade presente nunca pareceu "
                           "definir a realidade que Flávia conseguia imaginar.")]
for i, (rot, desc) in enumerate(itens):
    y = 4.05 + i * 1.92
    rotulo(s, rot, ML, y)
    bloco(s, ML, y + 0.48, 8.4, desc, 19, CORPO, LIGHT, espaco=1.45, h=1.2)
    if i < 2:
        fio(s, ML, y + 1.62, 8.6)
rodape(s, num=False)

# =====================================================================
# 10 — Os primeiros sinais
# =====================================================================
s = slide()
foto(s, 0, 0, 8.60, ALT, FOTO["B"])
X2 = 10.00
eyebrow(s, "Os primeiros sinais", X2, 2.30)
bloco(s, X2, 2.95, 8.0, "“", 92, ACENTO, LIGHT, espaco=1.0, h=1.2)
bloco(s, X2, 3.95, 8.0, ["Pai, eu vou comprar", "isso aqui.”"],
      48, TINTA, LIGHT, espaco=1.18)
fio(s, X2, 6.45, 1.30, ACENTO, esp=0.03)
bloco(s, X2, 6.95, 7.8,
      "Ainda adolescente, Flávia imaginava outra vida antes de ela existir. "
      "O portão e a casa tornaram-se símbolos dessa visão de futuro.",
      19, CORPO, LIGHT, espaco=1.5, h=1.8)
for i, atributo in enumerate(["Desejo de crescer", "Imaginação de futuro",
                              "Inconformismo com a condição dada"]):
    bloco(s, X2, 8.80 + i * 0.42, 7.8, atributo.upper(), 11, CLARO, SEMI,
          spc=2.4, h=0.3)
tf = caixa(s, X2, Y_RODAPE, 8.0, 0.35)
p = par(tf, True)
txt(p, DOC, 10.5, CLARO, SANS, spc=2.4)
txt(p, "   ·   ", 10.5, CLARO, SANS, spc=2.4)
txt(p, MARCA, 10.5, CLARO, SANS, spc=2.4)

# =====================================================================
# 11 — As experiências que a formaram
# =====================================================================
s = slide()
foto(s, 11.60, 0, 8.40, ALT, FOTO["C"])
eyebrow(s, "Profundidade")
titulo(s, "As experiências que a formaram", ML, Y_H1, 8.6, 42)
fio(s, ML, 3.45, 8.6)
exp = [("01", "Trabalho precoce", "Cozinhava com o pai no garimpo e aprendeu "
        "cedo a relação entre esforço e conquista."),
       ("02", "Disciplina", "Bicicleta, trabalho, faculdade e futsal para "
        "conquistar a bolsa e seguir estudando."),
       ("03", "Móveis planejados", "Dez anos de aprendizado técnico, de "
        "conhecimento e de domínio do setor."),
       ("04", "Maternidade e retorno", "Pausa, reconfiguração e volta mais "
        "madura ao empreendedorismo.")]
for i, (n, rot, desc) in enumerate(exp):
    y = 3.85 + i * 1.52
    bloco(s, ML, y + 0.02, 0.9, n, 13, ACENTO, SEMI, spc=2.0, h=0.3)
    rotulo(s, rot, ML + 1.10, y, cor=TINTA)
    bloco(s, ML + 1.10, y + 0.45, 7.3, desc, 18.5, CORPO, LIGHT, espaco=1.45,
          h=1.2)
    if i < 3:
        fio(s, ML, y + 1.30, 8.6)
rodape(s, num=False)

# =====================================================================
# 12 — As tensões que a colocaram em movimento
# =====================================================================
s = pagina("Contraste", "As tensões que a colocaram em movimento",
           com_fio=False)
tensoes = [("A condição de vida dizia", "“essa é a realidade disponível.”",
            "Flávia queria outra."),
           ("O cargo dizia", "“até aqui você pode chegar.”",
            "Flávia queria crescer."),
           ("As franquias diziam", "“é assim que deve ser feito.”",
            "Flávia queria fazer do seu jeito."),
           ("As sobras diziam", "“isso terminou aqui.”",
            "Flávia enxergou começo.")]
for i, (rot, fala, resp) in enumerate(tensoes):
    y = 4.45 + i * 1.40
    fio(s, ML, y, W)
    rotulo(s, rot, ML, y + 0.42, 4.6)
    bloco(s, 7.00, y + 0.34, 5.4, fala, 20, CORPO, LIGHT, italic=True, h=0.7)
    fio(s, 12.55, y + 0.60, 0.42, CLARO, esp=0.018)
    bloco(s, 13.45, y + 0.30, 4.4, resp, 23, TINTA, LIGHT, espaco=1.25, h=0.9)
fio(s, ML, 4.45 + len(tensoes) * 1.40, W)
rodape(s)

# =====================================================================
# 13 — As grandes viradas
# =====================================================================
s = pagina("Método", "As grandes viradas")
viradas = [("01", "Monta sua loja", "Sai do papel de funcionária e assume uma "
            "trajetória própria."),
           ("02", "Faz uma pausa", "Escolhe a maternidade, reorganiza a vida e "
            "se fortalece."),
           ("03", "Retorna pela Forma", "Volta ao setor e reencontra o lugar "
            "onde quer construir."),
           ("04", "Cria a My Home", "Transforma o descarte em uma nova "
            "possibilidade de negócio.")]
fio(s, ML, 5.05, W)
for i, (n, rot, desc) in enumerate(viradas):
    x = ML + i * (COL + GAP)
    bloco(s, x, 4.45, COL, n, 13, ACENTO, SEMI, spc=2.4, h=0.3)
    ponto(s, x + 0.06, 5.06, 0.12)
    bloco(s, x, 5.45, COL, rot, 22, TINTA, REG, espaco=1.15, h=1.0)
    bloco(s, x, 6.20, COL, desc, 19, CORPO, LIGHT, espaco=1.45, h=2.2)
rodape(s)

# =====================================================================
# 14 — O padrão invisível
# =====================================================================
s = slide()
foto(s, 12.40, 0, 7.60, ALT, FOTO["D"])
eyebrow(s, "Padrões")
titulo(s, "O padrão invisível", ML, Y_H1, 9.4, 42)
fio(s, ML, 3.45, 9.4)
pares = [("Escassez", "Não aceita a condição como destino."),
         ("Carreira", "Não aceita o cargo como limite final."),
         ("Franquias", "Não aceita o modelo pronto como a única forma."),
         ("Sobras", "Não aceita o descarte como o fim.")]
for i, (rot, desc) in enumerate(pares):
    y = 4.05 + i * 1.18
    rotulo(s, rot, ML, y + 0.14, 2.6)
    bloco(s, ML + 2.90, y, 6.5, desc, 21, CORPO, LIGHT, espaco=1.3, h=0.8)
    if i < 3:
        fio(s, ML, y + 0.92, 9.4)
fio(s, ML, 8.55, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 8.95, 9.2,
      "Em histórias diferentes, aparece o mesmo movimento: a realidade "
      "presente nunca é tratada como a versão final do possível.",
      19, TINTA, LIGHT, espaco=1.4, h=1.1)
rodape(s, num=False)

# =====================================================================
# 15 — O movimento que se repete
# =====================================================================
s = pagina("Modelo", "O movimento que se repete")
passos = [["Percebe", "a condição"], ["Imagina", "algo além"],
          ["Busca", "conhecimento"], ["Mobiliza", "pessoas"],
          ["Constrói", ""], ["Transforma", "em realidade"]]
X0, PASSO = 3.20, 2.72
fio(s, X0, 5.35, PASSO * 5)
for i, blk in enumerate(passos):
    cx = X0 + i * PASSO
    ponto(s, cx, 5.35, 0.13, ACENTO if i == 5 else CLARO)
    bloco(s, cx - 1.25, 5.75, 2.50, [t for t in blk if t], 19,
          TINTA if i == 5 else CORPO, LIGHT if i < 5 else REG,
          align=PP_ALIGN.CENTER, espaco=1.3, h=1.4)
fio(s, ML, 7.85, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 8.30, 13.0,
      "A mudança não nasce de um impulso isolado. Ela segue uma sequência "
      "reconhecível de visão, aprendizado e realização.",
      22, TINTA, LIGHT, espaco=1.45, h=1.4)
rodape(s)

# =====================================================================
# 16 — DIVISOR
# =====================================================================
divisor("03", "A linha-mestra da história")

# =====================================================================
# 17 — O manifesto
# =====================================================================
s = slide()
eyebrow(s, "A linha-mestra da história", ML, 2.60)
bloco(s, ML, 3.20, 13.0,
      "Ao longo da trajetória, Flávia parece repetir um mesmo movimento:",
      20, CLARO, LIGHT, h=0.6)
bloco(s, ML, 4.55, 15.4,
      ["Ela não aceita que o que existe", "determine o que pode existir."],
      62, TINTA, LIGHT, espaco=1.24)
fio(s, ML, 8.15, 1.30, ACENTO, esp=0.03)
rodape(s)

# =====================================================================
# 18 — DIVISOR
# =====================================================================
divisor("04", "Ikigai")

# =====================================================================
# 19 — O que move a trajetória
# =====================================================================
s = slide()
foto(s, 0, 0, 8.60, ALT, FOTO["C"])
eyebrow(s, "Ikigai", X2, 2.60)
bloco(s, X2, 3.20, 7.8, ["O que move", "a trajetória"], 52, TINTA, LIGHT,
      espaco=1.14)
fio(s, X2, 5.55, 7.8)
bloco(s, X2, 6.00, 7.6,
      "A história mostra como Flávia se formou e como age diante da vida.",
      21, CORPO, LIGHT, espaco=1.45, h=1.4)
bloco(s, X2, 7.55, 7.6,
      "O Ikigai entra para revelar o que gera sentido, realização e vontade "
      "de contribuir.", 21, TINTA, REG, espaco=1.45, h=1.8)
tf = caixa(s, X2, Y_RODAPE, 8.0, 0.35)
p = par(tf, True)
txt(p, DOC, 10.5, CLARO, SANS, spc=2.4)
txt(p, "   ·   ", 10.5, CLARO, SANS, spc=2.4)
txt(p, MARCA, 10.5, CLARO, SANS, spc=2.4)

# =====================================================================
# 20 — O mapa do Ikigai
# =====================================================================
s = pagina("Modelo", "O mapa do Ikigai")
quad = [("O que ama", "Família, pessoas, trocas, proximidade.",
         PP_ALIGN.RIGHT, 2.20, 4.45),
        ("No que é boa", "Conhecimento, persuasão, liderança, persistência.",
         PP_ALIGN.LEFT, 12.60, 4.45),
        ("Como contribui", "Ajuda, compartilha, gera crescimento.",
         PP_ALIGN.RIGHT, 2.20, 7.25),
        ("Onde se realiza", "Ver os sonhos tomando forma e as pessoas felizes.",
         PP_ALIGN.LEFT, 12.60, 7.25)]
for rot, desc, al, x, y in quad:
    bloco(s, x, y, 5.20, rot.upper(), 12.5, CLARO, SEMI, spc=2.2, align=al,
          h=0.3)
    bloco(s, x, y + 0.50, 5.20, desc, 21, TINTA, LIGHT, align=al, espaco=1.4,
          h=1.5)
anel(s, 10.00, 6.55, 3.60)
bloco(s, 8.30, 6.05, 3.40, ["Sentido", "e realização"], 21, TINTA, LIGHT,
      align=PP_ALIGN.CENTER, espaco=1.3)
rodape(s)

# =====================================================================
# 21 — Razão de ser
# =====================================================================
s = slide()
eyebrow(s, "O centro do Ikigai")
bloco(s, ML, 2.35, 3.0, "RAZÃO DE SER", 12.5, ACENTO, SEMI, spc=2.4, h=0.3)
bloco(s, ML, 3.05, 15.2,
      ["Transformar possibilidades", "em realizações concretas que façam",
       "diferença na vida das pessoas."], 44, TINTA, LIGHT, espaco=1.24)
fio(s, ML, 6.10, 1.30, ACENTO, esp=0.03)
bloco(s, ML, 6.50, 14.0,
      "A satisfação não termina nela: ganha força quando o que constrói "
      "também amplia algo para o outro.", 19, CORPO, LIGHT, espaco=1.45, h=0.7)
foto(s, 0, 7.55, LARG, ALT - 7.55, FOTO["E"])

# =====================================================================
# 22 — Onde história e Ikigai se encontram
# =====================================================================
s = pagina("Síntese", "Onde história e Ikigai se encontram")
enc = [("Visão", "Enxerga além da condição presente.", PP_ALIGN.RIGHT,
        2.20, 4.45),
       ("Impulso", "Não se conforma com os limites dados.", PP_ALIGN.LEFT,
        12.60, 4.45),
       ("Modo de agir", "Aprende, organiza, mobiliza e executa.",
        PP_ALIGN.RIGHT, 2.20, 7.05),
       ("Impacto", "Quer realizar e gerar transformação para outras pessoas.",
        PP_ALIGN.LEFT, 12.60, 7.05)]
for rot, desc, al, x, y in enc:
    bloco(s, x, y, 5.20, rot.upper(), 12.5, CLARO, SEMI, spc=2.2, align=al,
          h=0.3)
    bloco(s, x, y + 0.50, 5.20, desc, 21, TINTA, LIGHT, align=al, espaco=1.4,
          h=1.5)
anel(s, 10.00, 6.35, 3.60)
bloco(s, 8.45, 6.10, 3.10, "Convergência", 21, TINTA, LIGHT,
      align=PP_ALIGN.CENTER, espaco=1.3)
bloco(s, ML, 9.35, 15.0,
      "A história mostra o movimento. O Ikigai revela o sentido. "
      "Juntos, apontam a raiz.", 19, CLARO, LIGHT, align=PP_ALIGN.CENTER,
      h=0.6)
rodape(s)

# =====================================================================
# 23 — DIVISOR
# =====================================================================
divisor("05", "A essência")

# =====================================================================
# 24 — A revelação da essência
# =====================================================================
s = slide()
eyebrow(s, "Síntese")
bloco(s, ML, 2.35, 15.4,
      ["Enxergar além do que está posto e fazer",
       "existir o que ainda é possibilidade."], 52, TINTA, LIGHT, espaco=1.2)
fio(s, ML, 5.85, W)
cols = [("Como enxerga", "O presente não precisa ser a versão final."),
        ("O que a move", "A distância entre o que existe e o que ela imagina."),
        ("Como age", "Aprende, trabalha, cria, reorganiza e materializa."),
        ("O que transforma", "Realidades, inclusive a de outras pessoas.")]
for i, (rot, desc) in enumerate(cols):
    x = ML + i * (COL + GAP)
    rotulo(s, rot, x, 6.30, COL)
    bloco(s, x, 6.80, COL, desc, 19, CORPO, LIGHT, espaco=1.45, h=2.2)
rodape(s)

# =====================================================================
# 25 — Como essa essência transborda para as marcas
# =====================================================================
s = pagina("Síntese", "Como essa essência transborda para as marcas", 42)
rotulo(s, "Flávia", ML, 4.20, cor=ACENTO)
bloco(s, ML, 4.70, 15.0,
      "Enxerga além do que está posto e faz existir o que ainda é "
      "possibilidade.", 32, TINTA, LIGHT, espaco=1.3, h=1.1)
fio(s, ML, 6.25, W)
marcas = [("Forma", "Dar forma às possibilidades.",
           "Partir da matéria, da técnica e do projeto para construir algo "
           "que antes existia apenas como ideia ou sonho.", ML),
          ("My Home", "Reabrir possibilidades.",
           "Onde o processo enxergava sobra, Flávia viu matéria para criar "
           "outra coisa.", 10.60)]
for rot, tit, desc, x in marcas:
    rotulo(s, rot, x, 6.70, 6.8)
    bloco(s, x, 7.20, 7.0, tit, 30, TINTA, LIGHT, espaco=1.2, h=0.8)
    bloco(s, x, 8.20, 6.8, desc, 19, CORPO, LIGHT, espaco=1.45, h=1.6)
fio_v(s, 9.80, 6.70, 3.00)
bloco(s, ML, 9.60, 15.0,
      "A Revelação identifica a raiz. A Base Estratégica determinará como "
      "essa raiz deve, ou não, se transformar em estratégia para cada marca.",
      15, CLARO, LIGHT, h=0.5)
rodape(s)

# ---------------------------------------------------------------- salvar
prs.save(SAIDA)
print("OK ->", SAIDA, len(prs.slides._sldIdLst), "slides")
