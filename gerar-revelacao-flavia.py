#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Revelacao de Essencia - Flavia Pereira Muccelin
Conteudo e imagens da apresentacao original, rediagramados no layout
"Revelacao de Essencia - SABRE odonto" (20 x 11,25 / Outfit / KA).

Base: SABRE_odonto.pptx (para herdar tema + fontes Outfit incorporadas).
"""
import copy
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

TEXTURA = os.path.join(ASSETS, "textura.jpeg")
TRACO = os.path.join(ASSETS, "traco.png")
LOGO = os.path.join(ASSETS, "logo-ka.png")
FOTO = {k: os.path.join(ASSETS, "foto_%s.jpg" % k) for k in "ABCDE"}

# ---------------------------------------------------------------- paleta
FUNDO = RGBColor(0xF8, 0xF7, 0xF2)      # gelo dos slides de conteudo
FUNDO_DIV = RGBColor(0xF6, 0xF5, 0xF0)  # gelo dos divisores/capa
TINTA = RGBColor(0x1A, 0x1A, 0x1A)      # titulos
PRETO = RGBColor(0x00, 0x00, 0x00)      # capa / divisores
NEUTRO = RGBColor(0xB5, 0xB5, 0xAD)     # corpo secundario e eyebrow
GRAFITE = RGBColor(0x2E, 0x2E, 0x2A)    # numeros, filetes, rotulos fortes
CARD_B = RGBColor(0xFF, 0xFF, 0xFF)     # cartao claro
CARD_G = RGBColor(0xED, 0xED, 0xDD)     # cartao alternado
BORDA = RGBColor(0xE5, 0xE4, 0xDF)      # hairline dos cartoes / faixa
FILETE = RGBColor(0xDC, 0xDB, 0xD5)     # divisores finos
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)

# ---------------------------------------------------------------- fontes
F1 = "Outfit 1"
F1B = "Outfit 1 Bold"
F1H = "Outfit 1 Heavy"
F2 = "Outfit 2"
F2L = "Outfit 2 Light"
F2SB = "Outfit 2 Semi-Bold"
FPLEX = "IBM Plex Sans Thai"
FPLAY = "Playfair Display"

EMU = 914400
LARG, ALT = 20.0, 11.25
MARCA = "FLÁVIA PEREIRA MUCCELIN"
DOC = "REVELAÇÃO DE ESSÊNCIA"

# ---------------------------------------------------------------- base
prs = Presentation(MODELO)

# remove os slides do modelo, preservando tema, layouts e fontes incorporadas.
# O export do Canva pendura os notesSlides tambem em presentation.xml; sem
# derrubar essas relacoes os slides antigos continuam alcancaveis e o pacote
# sai com partes duplicadas.
for _rid, _rel in list(prs.part.rels.items()):
    if not _rel.is_external and "notesSlide" in str(_rel.target_part.partname):
        prs.part.drop_rel(_rid)

sldIdLst = prs.slides._sldIdLst
for sldId in list(sldIdLst):
    prs.part.drop_rel(sldId.rId)
    sldIdLst.remove(sldId)

assert not [p for p in prs.part.package.iter_parts()
            if "/ppt/slides/" in str(p.partname)], "sobraram slides do modelo"

BLANK = next(l for l in prs.slide_layouts if l.name == "Blank")


def E(v):
    return Emu(int(round(v * EMU)))


def slide(textura=False):
    s = prs.slides.add_slide(BLANK)
    fill = s.background.fill
    fill.solid()
    fill.fore_color.rgb = FUNDO_DIV if textura else FUNDO
    if textura:
        s.shapes.add_picture(TEXTURA, 0, 0, E(LARG), E(ALT))
    return s


def rect(s, x, y, w, h, cor, linha=None):
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(h))
    sp.fill.solid()
    sp.fill.fore_color.rgb = cor
    if linha is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = linha
        sp.line.width = Pt(0.75)
    sp.shadow.inherit = False
    return sp


def oval(s, x, y, d, cor):
    sp = s.shapes.add_shape(MSO_SHAPE.OVAL, E(x), E(y), E(d), E(d))
    sp.fill.solid()
    sp.fill.fore_color.rgb = cor
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def card(s, x, y, w, h, cor=CARD_B):
    """Cartao do padrao SABRE: hairline BORDA atras + preenchimento."""
    rect(s, x, y, w, h, BORDA)
    return rect(s, x + 0.012, y + 0.012, w - 0.024, h - 0.024, cor)


def caixa(s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def par(tf, primeiro=False, align=PP_ALIGN.LEFT, espaco=1.15, antes=0):
    p = tf.paragraphs[0] if primeiro else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = espaco
    if antes:
        p.space_before = Pt(antes)
    return p


def txt(p, texto, tam, cor, fonte=F1, bold=False, italic=False, spc=None):
    r = p.add_run()
    r.text = texto
    r.font.size = Pt(tam)
    r.font.name = fonte
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = cor
    if spc is not None:
        r.font._rPr.set("spc", str(int(spc * 100)))
    return r


def linhas(s, x, y, w, itens, tam, cor, fonte=F1, bold=False, italic=False,
           align=PP_ALIGN.LEFT, espaco=1.18, h=None):
    """Bloco de texto com uma ou varias linhas/paragrafos."""
    if isinstance(itens, str):
        itens = [itens]
    tf = caixa(s, x, y, w, h or (len(itens) * tam / 72.0 * espaco + 0.2))
    for i, t in enumerate(itens):
        p = par(tf, primeiro=(i == 0), align=align, espaco=espaco)
        txt(p, t, tam, cor, fonte, bold, italic)
    return tf


def foto(s, x, y, w, h, caminho):
    """Insere a imagem cobrindo a caixa (center-crop, sem distorcer)."""
    iw, ih = Image.open(caminho).size
    alvo, orig = w / h, iw / ih
    pic = s.shapes.add_picture(caminho, E(x), E(y), E(w), E(h))
    if orig > alvo:                       # imagem mais larga: corta laterais
        corte = (1 - alvo / orig) / 2
        pic.crop_left = pic.crop_right = corte
    elif orig < alvo:                     # imagem mais alta: corta topo/base
        corte = (1 - orig / alvo) / 2
        pic.crop_top = pic.crop_bottom = corte
    return pic


def eyebrow(s, texto, x=1.40, y=1.45):
    tf = caixa(s, x, y, 14.0, 0.45)
    txt(par(tf, True), texto.upper(), 17, NEUTRO, F1B, bold=True, spc=1.2)


def h1(s, texto, x=1.40, y=1.78, w=17.2, tam=48, cor=TINTA):
    if isinstance(texto, str):
        texto = [texto]
    tf = caixa(s, x, y, w, len(texto) * tam / 72.0 * 1.12 + 0.2)
    for i, t in enumerate(texto):
        txt(par(tf, primeiro=(i == 0), espaco=1.05), t, tam, cor, F1B, bold=True)
    return tf


def faixa(s, x, y, w, h, texto, tam=26, cor=TINTA, italic=True, fundo=BORDA):
    rect(s, x, y, w, h, fundo)
    tf = caixa(s, x + 0.4, y, w - 0.8, h, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True, align=PP_ALIGN.CENTER, espaco=1.12),
        texto, tam, cor, F1B, bold=True, italic=italic)


def barra(s, x, y, w, h, rotulo, texto, cor_fundo=CARD_B, tam_rot=18, tam=24,
          largura_rot=5.7, align_txt=PP_ALIGN.CENTER):
    """Linha da 'cadeia': fundo + filete escuro a esquerda + rotulo + texto."""
    rect(s, x, y, w, h, cor_fundo)
    rect(s, x, y, 0.09, h, GRAFITE)
    tf = caixa(s, x + 0.53, y, largura_rot, h, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True), rotulo, tam_rot, GRAFITE, F1B, bold=True, spc=1.0)
    if isinstance(texto, str):
        texto = [texto]
    tf2 = caixa(s, x + largura_rot + 0.9, y, w - largura_rot - 1.4, h,
                MSO_ANCHOR.MIDDLE)
    for i, t in enumerate(texto):
        txt(par(tf2, primeiro=(i == 0), align=align_txt, espaco=1.2),
            t, tam, NEUTRO, F1)


def rodape(s):
    tf = caixa(s, 1.90, 10.36, 11.5, 0.4)
    p = par(tf, True)
    txt(p, DOC, 17, PRETO, F1)
    txt(p, "   |    ", 17, PRETO, F1)
    txt(p, MARCA, 17, PRETO, F1, bold=True)
    s.shapes.add_picture(LOGO, E(16.72), E(10.34), E(2.00), E(2.00 * 183 / 777))


def conteudo(rot, titulo, tam_tit=48, y_eye=1.45, y_tit=1.78, x=1.40, w=17.2):
    s = slide()
    eyebrow(s, rot, x, y_eye)
    h1(s, titulo, x, y_tit, w, tam_tit)
    return s


def divisor(titulo_linhas, tam=100):
    s = slide(textura=True)
    tf = caixa(s, 3.78, 4.31, 15.10, len(titulo_linhas) * tam / 72.0 * 1.1 + 0.3)
    for i, t in enumerate(titulo_linhas):
        txt(par(tf, primeiro=(i == 0), align=PP_ALIGN.RIGHT, espaco=1.02),
            t, tam, PRETO, F1B, bold=True)
    rodape(s)
    return s


# =====================================================================
# 01 — CAPA
# =====================================================================
s = slide(textura=True)
s.shapes.add_picture(TRACO, E(16.85), E(6.60), E(1.55), E(1.85))

tf = caixa(s, 1.68, 3.15, 17.20, 1.40)
txt(par(tf, True, espaco=1.0), "REVELAÇÃO DE ESSÊNCIA", 75, PRETO, F1H, bold=True)

tf = caixa(s, 1.68, 4.85, 14.0, 0.95)
txt(par(tf, True), "Flávia Pereira Muccelin", 37, PRETO, F2SB, bold=True)

tf = caixa(s, 1.68, 6.05, 13.6, 1.6)
p = par(tf, True, espaco=1.3)
txt(p, "História, Ikigai e os padrões que existem na origem da ", 28, TINTA, F2)
txt(p, "Forma", 28, TINTA, F2SB, bold=True)
txt(p, " e da ", 28, TINTA, F2)
txt(p, "My Home", 28, TINTA, F2SB, bold=True)
txt(p, ".", 28, TINTA, F2)

rect(s, 1.68, 8.52, 0.02, 1.30, GRAFITE)
tf = caixa(s, 2.05, 8.62, 4.2, 1.15)
p = par(tf, True, espaco=1.12)
txt(p, "Método ", 26.8, PRETO, F2L)
txt(p, "Marca", 26.8, PRETO, F2SB, bold=True)
p = par(tf, espaco=1.12)
txt(p, "com Essência", 26.8, PRETO, F2SB, bold=True)
txt(p, " ©", 14.7, PRETO, FPLAY, bold=True)

rect(s, 6.90, 8.52, 0.02, 1.30, GRAFITE)
tf = caixa(s, 7.30, 8.52, 5.0, 1.30, MSO_ANCHOR.MIDDLE)
txt(par(tf, True), "FORMA  ·  MY HOME", 19.5, PRETO, FPLEX, spc=2.0)

s.shapes.add_picture(LOGO, E(16.72), E(10.34), E(2.00), E(2.00 * 183 / 777))

# =====================================================================
# 02 — Por que começamos pela essência
# =====================================================================
s = conteudo("CONCEITO", "POR QUE COMEÇAMOS PELA ESSÊNCIA", 52, 1.60, 1.95)
linhas(s, 1.40, 3.35, 15.6,
       ["Em marcas fortemente ligadas à fundadora, compreender sua história "
        "ajuda a identificar crenças, padrões e princípios que podem ter "
        "influenciado a criação, a cultura e a expressão das marcas."],
       30, NEUTRO, F1, espaco=1.3, h=2.2)

card(s, 1.40, 5.70, 17.20, 1.55)
rect(s, 1.40, 5.70, 0.10, 1.55, GRAFITE)
tf = caixa(s, 2.05, 5.70, 16.0, 1.55, MSO_ANCHOR.MIDDLE)
txt(par(tf, True), "Não estamos fazendo uma análise psicológica.",
    30, NEUTRO, F1, italic=True)

faixa(s, 1.40, 7.75, 17.20, 1.55,
      "ESTAMOS INVESTIGANDO A ORIGEM IDENTITÁRIA DA FORMA E DA MY HOME.", 25)
rodape(s)

# =====================================================================
# 03 — Como essa etapa contribui para o branding
# =====================================================================
s = conteudo("MÉTODO", "COMO ESSA ETAPA CONTRIBUI PARA O BRANDING", 44, 1.60, 1.95)
etapas = [
    ("01", "HISTÓRIA", "Revela referências e crenças de origem."),
    ("02", "IKIGAI", "Revela motivações e razão de ser."),
    ("03", "PADRÕES", "Revela formas recorrentes de agir e decidir."),
    ("04", "ESSÊNCIA", "Sintetiza aquilo que pode estar na raiz das marcas."),
]
x0, largura, gap = 1.40, 4.03, 0.29
for i, (num, tit, desc) in enumerate(etapas):
    x = x0 + i * (largura + gap)
    card(s, x, 3.65, largura, 4.05, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, 3.65, largura, 0.08, GRAFITE)
    linhas(s, x + 0.45, 4.05, largura - 0.9, num, 48, GRAFITE, F1B, bold=True)
    linhas(s, x + 0.45, 5.05, largura - 0.9, tit, 22, TINTA, F1B, bold=True)
    linhas(s, x + 0.45, 5.70, largura - 0.9, desc, 25, NEUTRO, F1, espaco=1.25,
           h=1.8)

rect(s, 1.40, 8.30, 17.20, 1.30, BORDA)
tf = caixa(s, 2.00, 8.30, 3.6, 1.30, MSO_ANCHOR.MIDDLE)
txt(par(tf, True), "NA ETAPA SEGUINTE", 18, GRAFITE, F1B, bold=True, spc=1.0)
tf = caixa(s, 5.80, 8.30, 12.2, 1.30, MSO_ANCHOR.MIDDLE)
txt(par(tf, True, espaco=1.2),
    "A Base Estratégica determinará o que disso deve se transformar em "
    "estratégia para cada marca.", 26, TINTA, F1)
rodape(s)

# =====================================================================
# 04 — Como chegamos à revelação
# =====================================================================
s = conteudo("MODELO", "COMO CHEGAMOS À REVELAÇÃO", 52, 1.60, 1.95)
blocos = ["HISTÓRIA", "IKIGAI", ["PADRÕES", "RECORRENTES"]]
bx, bl = 1.40, 3.75
for i, b in enumerate(blocos):
    x = bx + i * (bl + 1.30)
    card(s, x, 4.20, bl, 2.60, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, 4.20, bl, 0.08, GRAFITE)
    tf = caixa(s, x + 0.22, 4.28, bl - 0.44, 2.52, MSO_ANCHOR.MIDDLE)
    for j, t in enumerate(b if isinstance(b, list) else [b]):
        txt(par(tf, primeiro=(j == 0), align=PP_ALIGN.CENTER, espaco=1.12),
            t, 23, TINTA, F1B, bold=True)
    sinal = "+" if i < 2 else "="
    tf = caixa(s, x + bl + 0.25, 4.20, 0.80, 2.60, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True, align=PP_ALIGN.CENTER), sinal, 44, GRAFITE, F1B, bold=True)

rect(s, 15.85, 4.20, 2.75, 2.60, GRAFITE)
tf = caixa(s, 15.95, 4.20, 2.55, 2.60, MSO_ANCHOR.MIDDLE)
for j, t in enumerate(["HIPÓTESE", "DE ESSÊNCIA"]):
    txt(par(tf, primeiro=(j == 0), align=PP_ALIGN.CENTER, espaco=1.15),
        t, 23, BRANCO, F1B, bold=True)

faixa(s, 1.40, 8.05, 17.20, 1.45,
      "A APRESENTAÇÃO CRUZA TRAJETÓRIA, RAZÃO DE SER E COMPORTAMENTO "
      "RECORRENTE PARA REVELAR A RAIZ QUE ANTECEDE AS MARCAS.", 26)
rodape(s)

# =====================================================================
# 05 — Onde essa história começa
# =====================================================================
s = conteudo("HISTÓRIA", "ONDE ESSA HISTÓRIA COMEÇA", 52, 1.60, 1.95)
foto(s, 11.40, 3.30, 7.20, 6.30, FOTO["B"])
itens = [
    ("ORIGEM", "Família muito humilde, mudança para Primavera do Leste, fé, "
               "trabalho e recomeço."),
    ("CONTEXTO", "Pai trabalhando como caseiro/vaqueiro, mãe presente, rotina "
                 "de esforço e honestidade."),
    ("MARCA INICIAL", "Desde cedo, a realidade presente nunca pareceu definir "
                      "a realidade que Flávia conseguia imaginar."),
]
for i, (rot, desc) in enumerate(itens):
    y = 3.30 + i * 2.20
    card(s, 1.40, y, 9.60, 2.00, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, 1.40, y, 0.09, 2.00, GRAFITE)
    linhas(s, 1.95, y + 0.32, 8.6, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, 1.95, y + 0.76, 8.6, desc, 24, NEUTRO, F1, espaco=1.25, h=1.1)
rodape(s)

# =====================================================================
# 06 — Os primeiros sinais
# =====================================================================
s = slide()
foto(s, 11.40, 1.45, 7.20, 8.15, FOTO["B"])
eyebrow(s, "OS PRIMEIROS SINAIS", 1.40, 1.60)
tf = caixa(s, 1.40, 2.10, 9.40, 3.6)
for i, t in enumerate(["“PAI, EU VOU", "COMPRAR", "ISSO AQUI.”"]):
    txt(par(tf, primeiro=(i == 0), espaco=1.06), t, 56, TINTA, F1B, bold=True)
rect(s, 1.40, 5.90, 1.60, 0.07, GRAFITE)
linhas(s, 1.40, 6.35, 9.40,
       ["Ainda adolescente, Flávia imaginava outra vida antes de ela existir. "
        "O portão e a casa tornaram-se símbolos dessa visão de futuro."],
       27, NEUTRO, F1, espaco=1.3, h=2.0)
for i, t in enumerate(["DESEJO DE CRESCER", "IMAGINAÇÃO DE FUTURO",
                       "INCONFORMISMO COM A CONDIÇÃO DADA"]):
    y = 8.35 + i * 0.52
    rect(s, 1.40, y + 0.09, 0.30, 0.05, GRAFITE)
    linhas(s, 1.95, y, 8.80, t, 17, GRAFITE, F1B, bold=True)
rodape(s)

# =====================================================================
# 07 — As experiências que a formaram
# =====================================================================
s = conteudo("PROFUNDIDADE", "AS EXPERIÊNCIAS QUE A FORMARAM", 52, 1.60, 1.95)
foto(s, 12.60, 3.30, 6.00, 6.20, FOTO["C"])
exp = [
    ("01", "TRABALHO PRECOCE",
     "Cozinhava com o pai no garimpo e aprendeu cedo a relação entre esforço "
     "e conquista."),
    ("02", "DISCIPLINA",
     "Bicicleta, trabalho, faculdade e futsal para conquistar bolsa e seguir "
     "estudando."),
    ("03", "MÓVEIS PLANEJADOS",
     "Dez anos de aprendizado técnico, conhecimento e domínio do setor."),
    ("04", "MATERNIDADE E RETORNO",
     "Pausa, reconfiguração e volta mais madura ao empreendedorismo."),
]
rect(s, 2.04, 3.55, 0.03, 5.85, FILETE)
for i, (num, rot, desc) in enumerate(exp):
    y = 3.25 + i * 1.64
    oval(s, 1.72, y + 0.05, 0.66, GRAFITE if i == 3 else BORDA)
    tf = caixa(s, 1.72, y + 0.05, 0.66, 0.66, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True, align=PP_ALIGN.CENTER), num, 17,
        BRANCO if i == 3 else GRAFITE, F1B, bold=True)
    linhas(s, 2.85, y, 8.9, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, 2.85, y + 0.42, 8.9, desc, 25, NEUTRO, F1, espaco=1.25, h=1.1)
rodape(s)

# =====================================================================
# 08 — As tensões que a colocaram em movimento
# =====================================================================
s = conteudo("CONTRASTE", "AS TENSÕES QUE A COLOCARAM EM MOVIMENTO", 44, 1.60,
             1.95)
tensoes = [
    ("A CONDIÇÃO DE VIDA DIZIA", "“essa é a realidade disponível.”",
     "Flávia queria outra."),
    ("O CARGO DIZIA", "“até aqui você pode chegar.”",
     "Flávia queria crescer."),
    ("AS FRANQUIAS DIZIAM", "“é assim que deve ser feito.”",
     "Flávia queria fazer do seu jeito."),
    ("AS SOBRAS DIZIAM", "“isso terminou aqui.”",
     "Flávia enxergou começo."),
]
for i, (rot, fala, resp) in enumerate(tensoes):
    y = 3.60 + i * 1.55
    rect(s, 1.40, y, 17.20, 1.32, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, 1.40, y, 0.09, 1.32, GRAFITE)
    tf = caixa(s, 1.95, y, 5.4, 1.32, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True), rot, 18, GRAFITE, F1B, bold=True, spc=0.8)
    tf = caixa(s, 7.55, y, 5.5, 1.32, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True), fala, 24, NEUTRO, F1, italic=True)
    rect(s, 13.25, y + 0.62, 0.55, 0.05, GRAFITE)
    tf = caixa(s, 14.10, y, 4.3, 1.32, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True), resp, 24, TINTA, F1B, bold=True)
rodape(s)

# =====================================================================
# 09 — As grandes viradas
# =====================================================================
s = conteudo("MÉTODO", "AS GRANDES VIRADAS", 52, 1.60, 1.95)
viradas = [
    ("01", "MONTA SUA LOJA",
     "Sai do papel de funcionária e assume uma trajetória própria."),
    ("02", "FAZ UMA PAUSA",
     "Escolhe a maternidade, reorganiza a vida e se fortalece."),
    ("03", "RETORNA PELA FORMA",
     "Volta ao setor e reencontra o lugar onde quer construir."),
    ("04", "CRIA A MY HOME",
     "Transforma o descarte em nova possibilidade de negócio."),
]
for i, (num, rot, desc) in enumerate(viradas):
    x = 1.40 + i * (4.03 + 0.29)
    card(s, x, 3.90, 4.03, 5.10, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, 3.90, 4.03, 0.08, GRAFITE)
    oval(s, x + 1.65, 4.50, 0.72, GRAFITE if i == 3 else BORDA)
    tf = caixa(s, x + 1.65, 4.50, 0.72, 0.72, MSO_ANCHOR.MIDDLE)
    txt(par(tf, True, align=PP_ALIGN.CENTER), num, 18,
        BRANCO if i == 3 else GRAFITE, F1B, bold=True)
    linhas(s, x + 0.30, 5.70, 3.43, rot, 20, TINTA, F1B, bold=True,
           align=PP_ALIGN.CENTER)
    linhas(s, x + 0.30, 6.55, 3.43, desc, 24, NEUTRO, F1,
           align=PP_ALIGN.CENTER, espaco=1.25, h=2.2)
    if i < 3:
        rect(s, x + 4.09, 6.42, 0.17, 0.05, GRAFITE)
rodape(s)

# =====================================================================
# 10 — O padrão invisível
# =====================================================================
s = conteudo("PADRÕES", "O PADRÃO INVISÍVEL", 52, 1.60, 1.95)
foto(s, 12.10, 3.35, 6.50, 4.60, FOTO["D"])
pares = [
    ("ESCASSEZ", "Não aceita a condição como destino."),
    ("CARREIRA", "Não aceita o cargo como limite final."),
    ("FRANQUIAS", "Não aceita o modelo pronto como única forma."),
    ("SOBRAS", "Não aceita o descarte como fim."),
]
for i, (rot, desc) in enumerate(pares):
    x = 1.40 + (i % 2) * 5.25
    y = 3.35 + (i // 2) * 2.40
    card(s, x, y, 4.95, 2.20, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, y, 4.95, 0.08, GRAFITE)
    linhas(s, x + 0.40, y + 0.48, 4.15, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, x + 0.40, y + 0.95, 4.15, desc, 24, NEUTRO, F1, espaco=1.25, h=1.1)

faixa(s, 1.40, 8.20, 17.20, 1.40,
      "EM HISTÓRIAS DIFERENTES, APARECE O MESMO MOVIMENTO: A REALIDADE "
      "PRESENTE NUNCA É TRATADA COMO A VERSÃO FINAL DO POSSÍVEL.", 26)
rodape(s)

# =====================================================================
# 11 — O movimento que se repete
# =====================================================================
s = conteudo("MODELO", "O MOVIMENTO QUE SE REPETE", 52, 1.60, 1.95)
passos = [["PERCEBE A", "CONDIÇÃO"], ["IMAGINA", "ALGO ALÉM"],
          ["BUSCA", "CONHECIMENTO"], ["MOBILIZA", "PESSOAS"],
          ["CONSTRÓI"], ["TRANSFORMA", "EM REALIDADE"]]
lp, gp = 2.60, 0.44
for i, blk in enumerate(passos):
    x = 1.40 + i * (lp + gp)
    ultimo = (i == len(passos) - 1)
    if ultimo:
        rect(s, x, 4.10, lp, 2.60, GRAFITE)
    else:
        card(s, x, 4.10, lp, 2.60, CARD_B if i % 2 == 0 else CARD_G)
        rect(s, x, 4.10, lp, 0.08, GRAFITE)
    tf = caixa(s, x + 0.12, 4.18, lp - 0.24, 2.52, MSO_ANCHOR.MIDDLE)
    for j, t in enumerate(blk):
        txt(par(tf, primeiro=(j == 0), align=PP_ALIGN.CENTER, espaco=1.15),
            t, 18, BRANCO if ultimo else TINTA, F1B, bold=True)
    if not ultimo:
        rect(s, x + lp + 0.10, 5.37, 0.24, 0.05, GRAFITE)

faixa(s, 1.40, 7.60, 17.20, 1.50,
      "A MUDANÇA NÃO NASCE DE UM IMPULSO ISOLADO. ELA SEGUE UMA SEQUÊNCIA "
      "RECONHECÍVEL DE VISÃO, APRENDIZADO E REALIZAÇÃO.", 26)
rodape(s)

# =====================================================================
# 12 — A linha-mestra da história
# =====================================================================
s = slide(textura=True)
s.shapes.add_picture(TRACO, E(16.60), E(7.70), E(1.35), E(1.61))
eyebrow(s, "A LINHA-MESTRA DA HISTÓRIA", 1.68, 2.05)
linhas(s, 1.68, 2.70, 14.0,
       "Ao longo da trajetória, Flávia parece repetir um mesmo movimento:",
       30, NEUTRO, F1, h=0.8)
rect(s, 1.68, 3.85, 1.85, 0.08, GRAFITE)
tf = caixa(s, 1.68, 4.40, 16.0, 4.6)
for i, t in enumerate(["ELA NÃO ACEITA QUE", "O QUE EXISTE DETERMINE",
                       "O QUE PODE EXISTIR."]):
    txt(par(tf, primeiro=(i == 0), espaco=1.08), t, 68, PRETO, F1B, bold=True)
rodape(s)

# =====================================================================
# 13 — Ikigai: o que move a trajetória
# =====================================================================
s = slide(textura=True)
eyebrow(s, "IKIGAI", 1.40, 1.85)
h1(s, ["O QUE MOVE", "A TRAJETÓRIA"], 1.40, 2.25, 10.0, 60)
rect(s, 1.40, 5.05, 1.60, 0.07, GRAFITE)
foto(s, 10.60, 1.85, 8.00, 7.60, FOTO["C"])
card(s, 1.40, 5.60, 8.60, 3.85, CARD_B)
rect(s, 1.40, 5.60, 0.09, 3.85, GRAFITE)
linhas(s, 2.00, 6.05, 7.55,
       ["A história mostra como Flávia se formou e como age diante da vida."],
       27, NEUTRO, F1, espaco=1.28, h=1.6)
linhas(s, 2.00, 7.55, 7.55,
       ["O Ikigai entra para revelar o que gera sentido, realização e vontade "
        "de contribuir."],
       27, TINTA, F1B, bold=True, espaco=1.28, h=1.7)
rodape(s)

# =====================================================================
# 14 — O mapa do Ikigai
# =====================================================================
s = conteudo("MODELO", "O MAPA DO IKIGAI", 52, 1.60, 1.95)
foto(s, 13.60, 3.35, 5.00, 6.15, FOTO["E"])
quad = [
    ("O QUE AMA", "Família, pessoas, trocas, proximidade."),
    ("NO QUE É BOA", "Conhecimento, persuasão, liderança, persistência."),
    ("COMO CONTRIBUI", "Ajuda, compartilha, gera crescimento."),
    ("ONDE SE REALIZA", "Ver sonhos tomando forma e gente feliz."),
]
for i, (rot, desc) in enumerate(quad):
    x = 1.40 + (i % 2) * 7.60
    y = 3.35 + (i // 2) * 3.25
    card(s, x, y, 4.10, 2.90, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, y, 4.10, 0.08, GRAFITE)
    linhas(s, x + 0.30, y + 0.50, 3.50, rot, 18, GRAFITE, F1B, bold=True,
           align=PP_ALIGN.CENTER)
    linhas(s, x + 0.30, y + 1.10, 3.50, desc, 23, NEUTRO, F1,
           align=PP_ALIGN.CENTER, espaco=1.25, h=1.6)

rect(s, 5.90, 4.85, 2.70, 2.90, GRAFITE)
tf = caixa(s, 6.00, 4.85, 2.50, 2.90, MSO_ANCHOR.MIDDLE)
for j, t in enumerate(["SENTIDO", "E", "REALIZAÇÃO"]):
    txt(par(tf, primeiro=(j == 0), align=PP_ALIGN.CENTER, espaco=1.15),
        t, 19, BRANCO, F1B, bold=True)
rodape(s)

# =====================================================================
# 15 — O centro do Ikigai / razão de ser
# =====================================================================
s = slide()
eyebrow(s, "O CENTRO DO IKIGAI", 1.40, 1.45)
tf = caixa(s, 1.40, 1.78, 17.2, 0.6)
txt(par(tf, True), "RAZÃO DE SER", 22, GRAFITE, F1B, bold=True, spc=1.5)
tf = caixa(s, 1.40, 2.60, 17.2, 2.6)
for i, t in enumerate(["TRANSFORMAR POSSIBILIDADES EM",
                       "REALIZAÇÕES CONCRETAS QUE FAÇAM",
                       "DIFERENÇA NA VIDA DAS PESSOAS."]):
    txt(par(tf, primeiro=(i == 0), espaco=1.08), t, 48, TINTA, F1B, bold=True)
foto(s, 1.40, 5.65, 17.20, 2.65, FOTO["E"])
card(s, 1.40, 8.55, 17.20, 1.35, CARD_G)
rect(s, 1.40, 8.55, 0.09, 1.35, GRAFITE)
tf = caixa(s, 2.05, 8.55, 16.0, 1.35, MSO_ANCHOR.MIDDLE)
txt(par(tf, True),
    "A satisfação não termina nela: ganha força quando o que constrói também "
    "amplia algo para o outro.", 26, TINTA, F1, italic=True)
rodape(s)

# =====================================================================
# 16 — Onde história e Ikigai se encontram
# =====================================================================
s = conteudo("SÍNTESE", "ONDE HISTÓRIA E IKIGAI SE ENCONTRAM", 52, 1.60, 1.95)
enc = [
    ("VISÃO", "Enxerga além da condição presente.", 1.40, 3.35),
    ("IMPULSO", "Não se conforma com limites dados.", 13.65, 3.35),
    ("MODO DE AGIR", "Aprende, organiza, mobiliza e executa.", 1.40, 6.20),
    ("IMPACTO", "Quer realizar e gerar transformação para outras pessoas.",
     13.65, 6.20),
]
for i, (rot, desc, x, y) in enumerate(enc):
    card(s, x, y, 4.95, 2.55, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, y, 4.95, 0.08, GRAFITE)
    linhas(s, x + 0.40, y + 0.48, 4.15, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, x + 0.40, y + 0.98, 4.15, desc, 23, NEUTRO, F1, espaco=1.25, h=1.5)

rect(s, 7.35, 4.30, 5.30, 3.55, GRAFITE)
tf = caixa(s, 7.55, 4.30, 4.90, 3.55, MSO_ANCHOR.MIDDLE)
txt(par(tf, True, align=PP_ALIGN.CENTER), "CONVERGÊNCIA", 26, BRANCO, F1B,
    bold=True)
for x1, x2, y in [(6.35, 7.35, 4.60), (12.65, 13.65, 4.60),
                  (6.35, 7.35, 7.45), (12.65, 13.65, 7.45)]:
    rect(s, x1, y, x2 - x1, 0.04, FILETE)

faixa(s, 1.40, 9.00, 17.20, 1.05,
      "HISTÓRIA MOSTRA O MOVIMENTO. IKIGAI REVELA O SENTIDO. "
      "JUNTOS, APONTAM A RAIZ.", 26)
rodape(s)

# =====================================================================
# 17 — A revelação da essência
# =====================================================================
s = conteudo("SÍNTESE", "A REVELAÇÃO DA ESSÊNCIA", 48, 1.45, 1.75)
rect(s, 1.40, 3.05, 17.20, 2.35, BORDA)
tf = caixa(s, 2.00, 3.05, 16.0, 2.35, MSO_ANCHOR.MIDDLE)
for i, t in enumerate(["ENXERGAR ALÉM DO QUE ESTÁ POSTO",
                       "E FAZER EXISTIR O QUE AINDA É POSSIBILIDADE."]):
    txt(par(tf, primeiro=(i == 0), espaco=1.1), t, 40, TINTA, F1B, bold=True)

cols = [
    ("COMO ENXERGA", "O presente não precisa ser a versão final."),
    ("O QUE A MOVE", "A distância entre o que existe e o que ela imagina."),
    ("COMO AGE", "Aprende, trabalha, cria, reorganiza e materializa."),
    ("O QUE TRANSFORMA", "Realidades, inclusive a de outras pessoas."),
]
for i, (rot, desc) in enumerate(cols):
    x = 1.40 + i * (4.03 + 0.29)
    card(s, x, 5.90, 4.03, 3.65, CARD_B if i % 2 == 0 else CARD_G)
    rect(s, x, 5.90, 4.03, 0.08, GRAFITE)
    linhas(s, x + 0.40, 6.35, 3.23, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, x + 0.40, 6.95, 3.23, desc, 25, NEUTRO, F1, espaco=1.25, h=2.3)
rodape(s)

# =====================================================================
# 18 — Como essa essência pode transbordar para as marcas
# =====================================================================
s = conteudo("SÍNTESE", ["COMO ESSA ESSÊNCIA PODE TRANSBORDAR",
                         "PARA AS MARCAS"], 42, 1.45, 1.75)
rect(s, 1.40, 3.55, 17.20, 1.55, GRAFITE)
tf = caixa(s, 2.00, 3.55, 2.6, 1.55, MSO_ANCHOR.MIDDLE)
txt(par(tf, True), "FLÁVIA", 18, BORDA, F1B, bold=True, spc=1.2)
tf = caixa(s, 4.90, 3.55, 13.1, 1.55, MSO_ANCHOR.MIDDLE)
txt(par(tf, True),
    "Enxerga além do que está posto e faz existir o que ainda é possibilidade.",
    28, BRANCO, F1B, bold=True)

rect(s, 9.98, 5.10, 0.04, 0.35, GRAFITE)
rect(s, 5.45, 5.45, 9.10, 0.04, GRAFITE)
rect(s, 5.45, 5.45, 0.04, 0.35, GRAFITE)
rect(s, 14.51, 5.45, 0.04, 0.35, GRAFITE)

marcas = [
    ("FORMA", "Dar forma a possibilidades.",
     "Partir de matéria, técnica e projeto para construir algo que antes "
     "existia apenas como ideia ou sonho.", 1.40, CARD_B),
    ("MY HOME", "Reabrir possibilidades.",
     "Onde o processo enxergava sobra, Flávia viu matéria para criar outra "
     "coisa.", 10.20, CARD_G),
]
for rot, tit, desc, x, cor in marcas:
    card(s, x, 5.95, 8.40, 2.75, cor)
    rect(s, x, 5.95, 8.40, 0.08, GRAFITE)
    linhas(s, x + 0.45, 6.30, 7.5, rot, 18, GRAFITE, F1B, bold=True)
    linhas(s, x + 0.45, 6.75, 7.5, tit, 28, TINTA, F1B, bold=True)
    linhas(s, x + 0.45, 7.45, 7.5, desc, 23, NEUTRO, F1, espaco=1.25, h=1.2)

faixa(s, 1.40, 9.00, 17.20, 1.10,
      "A REVELAÇÃO IDENTIFICA A RAIZ. A BASE ESTRATÉGICA DETERMINARÁ COMO ESSA "
      "RAIZ DEVE, OU NÃO, SE TRANSFORMAR EM ESTRATÉGIA PARA CADA MARCA.", 23)
rodape(s)

# ---------------------------------------------------------------- salvar
prs.save(SAIDA)
print("OK ->", SAIDA, len(prs.slides.__iter__.__self__._sldIdLst), "slides")
