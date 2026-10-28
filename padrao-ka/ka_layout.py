#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA VISUAL KA — motor de layout para as apresentacoes do
KA · Inteligencia para Marcas.

Este modulo NAO conhece nenhum conteudo. Ele oferece a grade, a tipografia,
os arquetipos de pagina e os assets do padrao. Cada modelo de apresentacao
(Revelacao de Essencia, Base Estrategica, Plano de Comunicacao...) importa
daqui e monta o seu proprio roteiro.

Documentacao do padrao: padrao-ka/SISTEMA-VISUAL.md

Uso minimo:

    from ka_layout import Deck
    d = Deck(documento="REVELAÇÃO DE ESSÊNCIA", marca="NOME DA MARCA")
    s = d.pagina("Conceito", "Por que a essência vem primeiro?")
    d.corpo(s, 4.15, "Texto do slide.")
    d.salvar("saida.pptx")
"""
import os

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Emu, Pt

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")

TEXTURA = os.path.join(ASSETS, "textura-ondas.jpeg")
LOGO_KA = os.path.join(ASSETS, "logo-ka.png")
LOGO_KELLY = os.path.join(ASSETS, "logo-kelly-albert.png")
LOGO_PARCEIRO = os.path.join(ASSETS, "logo-vm-rocks.png")
TRACO = os.path.join(ASSETS, "traco.png")
SIMBOLO_IKIGAI = os.path.join(ASSETS, "simbolo-ikigai.png")

# ------------------------------------------------------------------ paleta
# MEDIDA no arquivo que a Kelly diagramou a mao (outubro/2026) e que passou
# a ser o padrao do Projeto Marca com Essencia. Ver PADRAO-KELLY.md.
PAINEL = RGBColor(0xF8, 0xF7, 0xF2)   # painel claro sobre a textura
TINTA = RGBColor(0x1C, 0x1C, 0x1A)    # titulos, listas e camadas
CORPO = RGBColor(0x6B, 0x6B, 0x66)    # corpo de texto
CLARO = RGBColor(0xA5, 0xA4, 0x9F)    # legenda, rodape — e o filete
FIO = RGBColor(0xA5, 0xA4, 0x9F)      # filetes: o mesmo cinza, nao um mais claro
GRAFITE = RGBColor(0x32, 0x33, 0x30)  # a frase de declaracao
ACENTO = RGBColor(0xCC, 0x75, 0x4E)   # terracota — uso minimo
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)

# ------------------------------------------------- tipografia (so Outfit)
#
# MEDIDO no arquivo final da Kelly: a familia de texto e a OUTFIT 1, nao a
# Outfit 2. No arquivo dela sao 576 trechos em Outfit 1 Light contra 4 em
# Outfit 2 Light. A Outfit 2 sobrou so no eyebrow. A primeira transcricao
# inverteu as duas familias — e e dai que vinha a maior diferenca visual
# entre o que eu gerava e o padrao dela, maior que qualquer tamanho.
LIGHT = "Outfit 1 Light"        # corpo, titulos e frases — o peso padrao
REG = "Outfit 1"                # rodape e texto neutro
SEMI = "Outfit 1 Semi-Bold"     # rotulos e numerais
SANS = "Outfit 2"               # eyebrow — a unica sobrevivente da familia 2
SANS_LIGHT = "Outfit 2 Light"   # assinatura do metodo, na capa
SANS_SEMI = "Outfit 2 Semi-Bold"  # o nome do metodo dentro da assinatura
BOLD = "Outfit 1 Bold"
MEDIO = "Outfit 1 Medium"       # titulo da capa
ULTRA = "Outfit 1 Ultra-Bold"   # titulo do sumario
HEAVY = "Outfit 1 Heavy"

EMU = 914400
LARG, ALT = 20.0, 11.25

# ------------------------------------------------------------------ grade
PAINEL_M = 1.10          # recuo do painel em relacao a borda do slide
ML = 2.20                # margem de texto (esquerda)
MR = 17.80               # limite direito do texto
W = MR - ML              # largura util
Y_EYE, Y_H1 = 1.95, 2.55
Y_RODAPE = 10.32

# Escala tipografica. Nao inventar tamanhos fora desta tabela.
#
# MEDIDA no arquivo final da Kelly, nao estimada: o Canva reporta a pagina
# em 1920 px para 20", ou seja 96 px/in, entao pt = px * 0,75. A primeira
# transcricao deste padrao chutou a escala e saiu pequena demais — o nome
# da secao vinha 34%% menor, o rodape 29%% menor, o corpo 19%% menor.
#
# Lead e corpo ficam no topo da faixa medida (o arquivo dela usa 22/18 numa
# pagina e 24/19 noutra) porque em projecao o corpo menor nao se le.
T_CAPA = 75              # titulo da capa
T_DIVISOR = 143.5        # nome da secao, na virada de tema
T_DIV_APOIO = 65         # a linha de apoio da virada, abaixo do nome
T_DISPLAY = 37           # a frase grande da pagina de declaracao
T_H1 = 42                # titulo de pagina
T_FRASE = 28             # aspas de citacao, no cartao sobre a foto
T_MEDIO = 25             # frase forte, rotulo de coluna
T_LEAD = 25              # linha de abertura — igual ao corpo
T_CORPO = 25             # corpo
T_LISTA = 30             # item de lista: maior que o corpo, e em tinta
T_CAMADA_ROT = 18        # rotulo da camada, Semi-Bold espacejado
T_MINI = 17              # legenda miuda
T_RODAPE = 17            # rodape
T_SUMARIO = 78           # titulo do sumario, acima do painel
T_SUBCAPA = 30           # subtitulo da capa
T_ASSINATURA = 26.8      # assinatura do metodo, na capa
T_DATA = 19.5            # data, na capa
T_FECHO = 95             # o OBRIGADA! da ultima pagina
T_ROTULO = 14            # eyebrow e rotulo miudo em caixa alta


def partes(texto):
    """Quebra o texto nos `**` em pares (trecho, e_forte)."""
    saida, forte = [], False
    for pedaco in texto.split("**"):
        if pedaco:
            saida.append((pedaco, forte))
        forte = not forte
    return saida or [(texto, False)]


def sem_marcas(texto):
    """O mesmo texto sem os `**` — e o que se mede."""
    if isinstance(texto, (list, tuple)):
        return [t.replace("**", "") for t in texto]
    return texto.replace("**", "")


def _modelo_base():
    """O .pptx de referencia existe apenas para herdar tema e as fontes
    Outfit incorporadas — nenhum slide dele e aproveitado."""
    return os.environ.get(
        "MODELO_PPTX",
        os.path.join(os.path.dirname(BASE), "referencia",
                     "PADRAO-KA-revelacao-de-essencia.pptx"))


# Escala anterior, menor. Existe so para o roteiro fixo da Revelacao de
# Essencia, diagramado a mao contra estes valores antes da medicao. Nao usar
# em material novo.
ESCALA_LEGADA = {
    "CAPA": 76, "DIVISOR": 62, "DISPLAY": 46, "H1": 38, "FRASE": 28,
    "MEDIO": 22, "LEAD": 17, "CORPO": 14.5, "MINI": 12, "RODAPE": 12,
    "ROTULO": 9.5, "SUMARIO": 44, "SUBCAPA": 22, "ASSINATURA": 17, "DATA": 12,
    "LISTA": 18, "DIV_APOIO": 28, "CAMADA_ROT": 11, "FECHO": 47,
}
ESCALA_KA = {
    "CAPA": T_CAPA, "DIVISOR": T_DIVISOR, "DISPLAY": T_DISPLAY, "H1": T_H1,
    "FRASE": T_FRASE, "MEDIO": T_MEDIO, "LEAD": T_LEAD, "CORPO": T_CORPO,
    "MINI": T_MINI, "RODAPE": T_RODAPE, "ROTULO": T_ROTULO,
    "SUMARIO": T_SUMARIO, "SUBCAPA": T_SUBCAPA, "ASSINATURA": T_ASSINATURA,
    "DATA": T_DATA, "LISTA": T_LISTA, "DIV_APOIO": T_DIV_APOIO,
    "CAMADA_ROT": T_CAMADA_ROT, "FECHO": T_FECHO,
}


class Deck:
    def __init__(self, documento, marca, modelo=None, escala="ka"):
        self.documento = documento.upper()
        self.marca = marca.upper()
        self.prs = Presentation(modelo or _modelo_base())

        # Limpa os slides do arquivo-modelo preservando tema e fontes. O
        # export do Canva pendura os notesSlides tambem em presentation.xml;
        # sem derrubar essas relacoes os slides antigos continuam
        # alcancaveis e o pacote sai com partes duplicadas.
        parte = self.prs.part
        for rid, rel in list(parte.rels.items()):
            if not rel.is_external and "notesSlide" in str(rel.target_part.partname):
                parte.drop_rel(rid)
        for sldId in list(self.prs.slides._sldIdLst):
            parte.drop_rel(sldId.rId)
            self.prs.slides._sldIdLst.remove(sldId)
        assert not [p for p in parte.package.iter_parts()
                    if "/ppt/slides/" in str(p.partname)], "sobraram slides do modelo"

        self.branco = next(l for l in self.prs.slide_layouts if l.name == "Blank")
        self.T = dict(ESCALA_LEGADA if escala == "legada" else ESCALA_KA)

    # ------------------------------------------------------------ utilidades
    @staticmethod
    def e(v):
        return Emu(int(round(v * EMU)))

    def slide(self, painel=True, textura=True):
        """Pagina do padrao: textura de ondas no fundo e, por cima, o painel
        claro de cantos arredondados onde o conteudo vive. Paginas de
        abertura, fecho e alguns manifestos dispensam o painel."""
        s = self.prs.slides.add_slide(self.branco)
        s.background.fill.solid()
        s.background.fill.fore_color.rgb = PAINEL
        if textura:
            pic = s.shapes.add_picture(TEXTURA, 0, 0, self.e(LARG), self.e(ALT))
            # 32% sobre o fundo claro. Chapada, a textura rouba o contraste
            # do texto e some com a leveza do padrao.
            blip = pic._element.blipFill.find(qn("a:blip"))
            alpha = OxmlElement("a:alphaModFix")
            alpha.set("amt", "32000")
            blip.append(alpha)
        if painel:
            self.bloco(s, PAINEL_M, PAINEL_M, LARG - 2 * PAINEL_M,
                       ALT - 2 * PAINEL_M - 0.55, PAINEL, raio=0.18)
        return s

    def bloco(self, s, x, y, w, h, cor, raio=0.0):
        forma = MSO_SHAPE.ROUNDED_RECTANGLE if raio else MSO_SHAPE.RECTANGLE
        sp = s.shapes.add_shape(forma, self.e(x), self.e(y), self.e(w), self.e(h))
        if raio:
            sp.adjustments[0] = min(0.5, raio / min(w, h))
        sp.fill.solid()
        sp.fill.fore_color.rgb = cor
        sp.line.fill.background()
        sp.shadow.inherit = False
        return sp

    def fio(self, s, x, y, w, cor=FIO, esp=0.012):
        """Filete. No padrao KA e ele, e nao a caixa, que organiza a pagina."""
        return self.bloco(s, x, y, w, esp, cor)

    def fio_v(self, s, x, y, h, cor=FIO, esp=0.012):
        return self.bloco(s, x, y, esp, h, cor)

    def ponto(self, s, cx, cy, d=0.10, cor=ACENTO):
        sp = s.shapes.add_shape(MSO_SHAPE.OVAL, self.e(cx - d / 2),
                                self.e(cy - d / 2), self.e(d), self.e(d))
        sp.fill.solid()
        sp.fill.fore_color.rgb = cor
        sp.line.fill.background()
        sp.shadow.inherit = False
        return sp

    def anel(self, s, cx, cy, d, cor=FIO, esp=0.9):
        """Circulo de contorno fino — no padrao KA, nunca preenchido."""
        sp = s.shapes.add_shape(MSO_SHAPE.OVAL, self.e(cx - d / 2),
                                self.e(cy - d / 2), self.e(d), self.e(d))
        sp.fill.background()
        sp.line.color.rgb = cor
        sp.line.width = Pt(esp)
        sp.shadow.inherit = False
        return sp

    def caixa(self, s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
        tb = s.shapes.add_textbox(self.e(x), self.e(y), self.e(w), self.e(h))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        return tf

    @staticmethod
    def par(tf, primeiro=False, align=PP_ALIGN.LEFT, espaco=1.3):
        p = tf.paragraphs[0] if primeiro else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = espaco
        return p

    @staticmethod
    def txt(p, texto, tam, cor, fonte=LIGHT, italic=False, spc=None):
        r = p.add_run()
        r.text = texto
        r.font.size = Pt(tam)
        r.font.name = fonte
        r.font.italic = italic
        r.font.color.rgb = cor
        # O peso vem do NOME da fonte, nunca de b="1": negrito sintetico
        # sobre a Outfit engrossa as curvas e deixa o texto pastoso.
        r.font.bold = False
        if spc is not None:
            r.font._rPr.set("spc", str(int(spc * 100)))
        return r

    def texto(self, s, x, y, w, itens, tam, cor, fonte=LIGHT,
              align=PP_ALIGN.LEFT, espaco=1.4, h=None, italic=False, spc=None):
        """`espaco` e a entrelinha em MULTIPLOS DO CORPO, gravada EXATA.

        O arquivo que a Kelly diagramou grava entrelinha exata — 35pt para
        corpo de 25, 57,4pt para titulo de 42 — e nao um multiplo da altura
        de linha da fonte. Gravar exato tem duas consequencias boas: a
        composicao bate com a dela ao ponto, e a conta de altura passa a ser
        a propria medida (linhas x corpo x espaco), sem fator de correcao."""
        if isinstance(itens, str):
            itens = [itens]
        tf = self.caixa(s, x, y, w, h or (len(itens) * tam / 72.0 * espaco + 0.3))
        for i, t in enumerate(itens):
            par = self.par(tf, primeiro=(i == 0), align=align, espaco=espaco)
            par.line_spacing = Pt(tam * espaco)
            self.txt(par, t, tam, cor, fonte, italic, spc)
        return tf

    def texto_rico(self, s, x, y, w, itens, tam, cor, fonte=LIGHT,
                   forte=None, align=PP_ALIGN.LEFT, espaco=1.4, h=None,
                   spc=None):
        """Igual ao `texto`, mas o trecho entre ** sai no peso forte.

        E a assinatura do padrao: no titulo, a frase-chave vem em Bold e o
        resto em Light, na MESMA linha e no mesmo corpo. O peso marca o que
        a pagina esta dizendo — nao o tamanho, nao a cor."""
        if isinstance(itens, str):
            itens = [itens]
        forte = forte or BOLD
        tf = self.caixa(s, x, y, w, h or (len(itens) * tam / 72.0 * espaco + 0.3))
        for i, t in enumerate(itens):
            par = self.par(tf, primeiro=(i == 0), align=align, espaco=espaco)
            par.line_spacing = Pt(tam * espaco)
            for pedaco, negrito in partes(t):
                self.txt(par, pedaco, tam, cor, forte if negrito else fonte,
                         spc=spc)
        return tf

    def foto(self, s, x, y, w, h, caminho, raio=None, foco=0.5):
        """Imagem cobrindo a caixa (crop sem distorcer). Quando sangra na
        borda do slide vai sem raio; contida, ganha canto arredondado.

        `foco` diz que parte da imagem sobrevive ao corte: 0.5 e o centro,
        valores menores puxam para o topo. Numa FAIXA horizontal o corte e
        vertical e violento, e centralizar decapita as pessoas — por isso a
        faixa pede foco alto (perto de 0,3)."""
        iw, ih = Image.open(caminho).size
        alvo, orig = w / h, iw / ih
        pic = s.shapes.add_picture(caminho, self.e(x), self.e(y),
                                   self.e(w), self.e(h))
        f = min(max(foco, 0.0), 1.0)
        if orig > alvo:
            c = 1 - alvo / orig
            pic.crop_left, pic.crop_right = c * f, c * (1 - f)
        elif orig < alvo:
            c = 1 - orig / alvo
            pic.crop_top, pic.crop_bottom = c * f, c * (1 - f)
        if raio:
            geom = pic._element.spPr.find(qn("a:prstGeom"))
            if geom is not None:
                geom.set("prst", "roundRect")
                av = geom.find(qn("a:avLst"))
                if av is None:
                    av = OxmlElement("a:avLst")
                    geom.append(av)
                for filho in list(av):
                    av.remove(filho)
                gd = OxmlElement("a:gd")
                gd.set("name", "adj")
                gd.set("fmla", "val %d" % int(min(0.5, raio / min(w, h)) * 100000))
                av.append(gd)
        return pic

    def logo(self, s, caminho, x, y, largura):
        iw, ih = Image.open(caminho).size
        return s.shapes.add_picture(caminho, self.e(x), self.e(y),
                                    self.e(largura), self.e(largura * ih / iw))

    # -------------------------------------------------------- blocos de pagina
    def eyebrow(self, s, texto, x=ML, y=Y_EYE):
        self.texto(s, x, y, 12.0, texto.upper(), self.T["ROTULO"], CLARO, SANS,
                   spc=3.0, h=0.32)

    def rotulo(self, s, texto, x, y, w=6.0, cor=CLARO):
        self.texto(s, x, y, w, texto.upper(), self.T["ROTULO"], cor, SEMI, spc=2.2,
                   h=0.28)

    def titulo(self, s, texto, x=ML, y=Y_H1, w=W, tam=None, cor=TINTA,
               espaco=1.37):
        """H1 em CAIXA ALTA e peso leve, com a frase-chave em Bold.

        O marcador e o `**` no proprio titulo do conteudo:

            "titulo": "A menina que **não aceitou os limites**"

        Sem marcador, o titulo inteiro sai em Light — como sempre foi."""
        tam = self.T["H1"] if tam is None else tam
        itens = [texto] if isinstance(texto, str) else list(texto)
        itens = [t.upper() for t in itens]
        return self.texto_rico(s, x, y, w, itens, tam, cor, LIGHT,
                               espaco=espaco)

    def rodape(self, s):
        """Pilula clara com a identificacao do documento + logo KA a direita."""
        self.bloco(s, 1.55, Y_RODAPE - 0.16, 8.35, 0.58, PAINEL, raio=0.16)
        tf = self.caixa(s, 1.95, Y_RODAPE - 0.16, 7.6, 0.58, MSO_ANCHOR.MIDDLE)
        p = self.par(tf, True)
        self.txt(p, self.documento, self.T["RODAPE"], TINTA, REG, spc=2.2)
        self.txt(p, "   |   ", self.T["RODAPE"], CLARO, REG, spc=2.2)
        self.txt(p, self.marca, self.T["RODAPE"], TINTA, BOLD, spc=2.2)
        self.logo(s, LOGO_KA, 16.55, Y_RODAPE - 0.22, 1.72)

    # ------------------------------------------------------------ arquetipos
    def abertura(self, parceiro=LOGO_PARCEIRO):
        """A1 — logos sobre a textura, sem painel. Abre e fecha o documento."""
        s = self.slide(painel=False)
        self.logo(s, LOGO_KELLY, 3.55, 5.05, 4.30)
        if parceiro:
            self.fio_v(s, 9.85, 4.60, 1.85, CLARO, esp=0.014)
            self.logo(s, parceiro, 10.90, 4.85, 4.40)
        return s

    def capa(self, titulo_linhas, subtitulo, assinatura, data):
        """A2 — capa: titulo em caixa alta sobre a textura, barra de
        assinatura embaixo (logo KA · metodo · data)."""
        s = self.slide(painel=False)
        self.logo(s, TRACO, 16.30, 3.15, 1.45)
        self.texto(s, ML, 3.55, 15.0, titulo_linhas, self.T["CAPA"], TINTA, BOLD,
                   espaco=1.06)
        self.fio(s, ML, 6.55, 1.30, ACENTO, esp=0.03)
        self.texto(s, ML, 7.00, 14.0, subtitulo, self.T["SUBCAPA"], TINTA, LIGHT, h=0.75)
        self.logo(s, LOGO_KA, ML, 8.85, 2.35)
        self.fio_v(s, 5.20, 8.75, 0.85, CLARO, esp=0.012)
        self.texto(s, 5.60, 8.82, 4.2, assinatura, self.T["ASSINATURA"], TINTA, LIGHT,
                   espaco=1.25, h=0.8)
        self.fio_v(s, 10.10, 8.75, 0.85, CLARO, esp=0.012)
        self.texto(s, 10.50, 9.02, 3.2, data.upper(), self.T["DATA"], TINTA, SANS,
                   spc=2.0, h=0.35)
        return s

    def pagina(self, eyebrow, titulo, tam=None, com_fio=True, x=ML, w=W):
        """A3 — pagina de conteudo: eyebrow, titulo e filete."""
        tam = self.T["H1"] if tam is None else tam
        s = self.slide()
        self.eyebrow(s, eyebrow, x)
        n = len(titulo) if isinstance(titulo, list) else 1
        self.titulo(s, titulo, x, Y_H1, w, tam)
        if com_fio:
            self.fio(s, x, Y_H1 + n * tam / 72.0 * 1.14 + 0.34, w)
        self.rodape(s)
        return s

    def divisor(self, numero, nome):
        """A4 — virada de tema: numero da secao, nome em caixa alta leve e um
        filete que atravessa a pagina. Nada alem disso."""
        s = self.slide()
        self.texto(s, ML, 4.30, 4.0, numero, self.T["ROTULO"], ACENTO, SEMI, spc=3.0,
                   h=0.3)
        self.texto(s, ML, 4.80, 12.0, nome, self.T["DIVISOR"], TINTA, LIGHT,
                   espaco=1.0)
        self.fio(s, ML, 6.95, W)
        self.rodape(s)
        return s

    def com_foto(self, eyebrow, titulo, caminho, lado="direita", fatia=0.42,
                 tam=None):
        """A5 — pagina partida: foto sangrando em uma lateral, texto na
        outra. Devolve (slide, x, largura) da coluna de texto."""
        tam = self.T["H1"] if tam is None else tam
        s = self.slide(painel=False)
        corte = LARG * fatia
        if lado == "direita":
            self.bloco(s, 0, 0, LARG - corte, ALT, PAINEL)
            self.foto(s, LARG - corte, 0, corte, ALT, caminho)
            x, larg = ML, LARG - corte - ML - 0.9
        else:
            self.foto(s, 0, 0, corte, ALT, caminho)
            self.bloco(s, corte, 0, LARG - corte, ALT, PAINEL)
            x, larg = corte + 0.9, LARG - corte - 1.8
        self.eyebrow(s, eyebrow, x)
        n = len(titulo) if isinstance(titulo, list) else 1
        self.titulo(s, titulo, x, Y_H1, larg, tam)
        self.fio(s, x, Y_H1 + n * tam / 72.0 * 1.14 + 0.34, larg)
        # o rodape acompanha a coluna de texto
        self.bloco(s, x - 0.4, Y_RODAPE - 0.16, min(8.35, larg + 0.8), 0.58,
                   PAINEL, raio=0.16)
        tf = self.caixa(s, x, Y_RODAPE - 0.16, larg, 0.58, MSO_ANCHOR.MIDDLE)
        p = self.par(tf, True)
        self.txt(p, self.documento, T_MINI, TINTA, SANS, spc=2.2)
        self.txt(p, "   |   ", T_MINI, CLARO, SANS, spc=2.2)
        self.txt(p, self.marca, T_MINI, TINTA, BOLD, spc=2.2)
        return s, x, larg

    def manifesto(self, eyebrow, linhas, apoio=None):
        """A6 — pagina de silencio: uma frase grande e muito espaco."""
        s = self.slide()
        self.eyebrow(s, eyebrow, ML, 3.10)
        if apoio:
            self.texto(s, ML, 3.60, 13.0, apoio, self.T["LEAD"], CLARO, LIGHT, h=0.6)
        self.texto(s, ML, 4.35, 15.2, linhas, self.T["DISPLAY"], TINTA, LIGHT,
                   espaco=1.26)
        self.fio(s, ML, 8.05, 1.30, ACENTO, esp=0.03)
        self.rodape(s)
        return s

    def fecho(self, frase="MUITO OBRIGADA!", parceiro=LOGO_PARCEIRO):
        """A7 — ultima pagina: agradecimento e assinatura, sem painel."""
        s = self.slide(painel=False)
        self.texto(s, ML, 2.90, 15.0, frase, self.T["FECHO"], TINTA, LIGHT,
                   espaco=1.12)
        self.logo(s, LOGO_KELLY, 1.125, 5.75, 4.835)
        if parceiro:
            self.fio_v(s, 6.20, 5.75, 1.25, CLARO, esp=0.014)
            self.logo(s, parceiro, 6.642, 5.81, 3.60)
        return s

    # ---------------------------------------------------------------- saida
    def salvar(self, caminho):
        self.prs.save(caminho)
        return caminho, len(self.prs.slides._sldIdLst)
