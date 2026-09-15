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
    s = d.pagina("Conceito", "Por que começamos pela essência?")
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
PAINEL = RGBColor(0xF7, 0xF5, 0xF0)   # painel claro sobre a textura
TINTA = RGBColor(0x1C, 0x1C, 0x1A)    # titulos e frases
CORPO = RGBColor(0x6B, 0x6B, 0x66)    # corpo de texto
CLARO = RGBColor(0xA5, 0xA4, 0x9F)    # eyebrow, legenda, rodape
FIO = RGBColor(0xDF, 0xDD, 0xD7)      # filetes
ACENTO = RGBColor(0xA9, 0x72, 0x4A)   # terracota — uso minimo
BRANCO = RGBColor(0xFF, 0xFF, 0xFF)

# ------------------------------------------------- tipografia (so Outfit)
LIGHT = "Outfit 2 Light"
REG = "Outfit 2"
SEMI = "Outfit 2 Semi-Bold"
SANS = "Outfit 1"
BOLD = "Outfit 1 Bold"
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
T_CAPA = 76
T_DIVISOR = 62
T_DISPLAY = 46
T_H1 = 38
T_FRASE = 28
T_MEDIO = 22
T_LEAD = 17
T_CORPO = 14.5
T_MINI = 12
T_ROTULO = 9.5


def _modelo_base():
    """O .pptx de referencia existe apenas para herdar tema e as fontes
    Outfit incorporadas — nenhum slide dele e aproveitado."""
    return os.environ.get(
        "MODELO_PPTX",
        os.path.join(os.path.dirname(BASE), "referencia",
                     "PADRAO-KA-revelacao-de-essencia.pptx"))


class Deck:
    def __init__(self, documento, marca, modelo=None):
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
            s.shapes.add_picture(TEXTURA, 0, 0, self.e(LARG), self.e(ALT))
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
        if isinstance(itens, str):
            itens = [itens]
        tf = self.caixa(s, x, y, w, h or (len(itens) * tam / 72.0 * espaco + 0.3))
        for i, t in enumerate(itens):
            self.txt(self.par(tf, primeiro=(i == 0), align=align, espaco=espaco),
                     t, tam, cor, fonte, italic, spc)
        return tf

    def foto(self, s, x, y, w, h, caminho, raio=None):
        """Imagem cobrindo a caixa (center-crop, sem distorcer). Quando sangra
        na borda do slide vai sem raio; contida, ganha canto arredondado."""
        iw, ih = Image.open(caminho).size
        alvo, orig = w / h, iw / ih
        pic = s.shapes.add_picture(caminho, self.e(x), self.e(y),
                                   self.e(w), self.e(h))
        if orig > alvo:
            c = (1 - alvo / orig) / 2
            pic.crop_left = pic.crop_right = c
        elif orig < alvo:
            c = (1 - orig / alvo) / 2
            pic.crop_top = pic.crop_bottom = c
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
        self.texto(s, x, y, 12.0, texto.upper(), T_ROTULO, CLARO, SANS,
                   spc=3.0, h=0.32)

    def rotulo(self, s, texto, x, y, w=6.0, cor=CLARO):
        self.texto(s, x, y, w, texto.upper(), T_ROTULO, cor, SEMI, spc=2.2,
                   h=0.28)

    def titulo(self, s, texto, x=ML, y=Y_H1, w=W, tam=T_H1, cor=TINTA):
        """H1 em caixa baixa e peso leve: a forca vem do tamanho e do ar."""
        return self.texto(s, x, y, w, texto, tam, cor, LIGHT, espaco=1.14)

    def rodape(self, s):
        """Pilula clara com a identificacao do documento + logo KA a direita."""
        self.bloco(s, 1.55, Y_RODAPE - 0.16, 8.35, 0.58, PAINEL, raio=0.16)
        tf = self.caixa(s, 1.95, Y_RODAPE - 0.16, 7.6, 0.58, MSO_ANCHOR.MIDDLE)
        p = self.par(tf, True)
        self.txt(p, self.documento, T_MINI, TINTA, SANS, spc=2.2)
        self.txt(p, "   |   ", T_MINI, CLARO, SANS, spc=2.2)
        self.txt(p, self.marca, T_MINI, TINTA, BOLD, spc=2.2)
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
        self.texto(s, ML, 3.55, 15.0, titulo_linhas, T_CAPA, TINTA, BOLD,
                   espaco=1.06)
        self.fio(s, ML, 6.55, 1.30, ACENTO, esp=0.03)
        self.texto(s, ML, 7.00, 14.0, subtitulo, T_MEDIO, TINTA, LIGHT, h=0.6)
        self.logo(s, LOGO_KA, ML, 8.85, 2.35)
        self.fio_v(s, 5.20, 8.75, 0.85, CLARO, esp=0.012)
        self.texto(s, 5.60, 8.82, 4.2, assinatura, T_LEAD, TINTA, LIGHT,
                   espaco=1.25, h=0.8)
        self.fio_v(s, 10.10, 8.75, 0.85, CLARO, esp=0.012)
        self.texto(s, 10.50, 9.02, 3.2, data.upper(), T_MINI, TINTA, SANS,
                   spc=2.0, h=0.35)
        return s

    def pagina(self, eyebrow, titulo, tam=T_H1, com_fio=True, x=ML, w=W):
        """A3 — pagina de conteudo: eyebrow, titulo e filete."""
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
        self.texto(s, ML, 4.30, 4.0, numero, T_MINI, ACENTO, SEMI, spc=3.0,
                   h=0.3)
        self.texto(s, ML, 4.80, 12.0, nome.upper(), T_DIVISOR, TINTA, LIGHT,
                   espaco=1.0)
        self.fio(s, ML, 6.95, W)
        self.rodape(s)
        return s

    def com_foto(self, eyebrow, titulo, caminho, lado="direita", fatia=0.42,
                 tam=T_H1):
        """A5 — pagina partida: foto sangrando em uma lateral, texto na
        outra. Devolve (slide, x, largura) da coluna de texto."""
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
            self.texto(s, ML, 3.60, 13.0, apoio, T_LEAD, CLARO, LIGHT, h=0.5)
        self.texto(s, ML, 4.35, 15.2, linhas, T_DISPLAY, TINTA, LIGHT,
                   espaco=1.26)
        self.fio(s, ML, 8.05, 1.30, ACENTO, esp=0.03)
        self.rodape(s)
        return s

    def fecho(self, frase="MUITO OBRIGADA!", parceiro=LOGO_PARCEIRO):
        """A7 — ultima pagina: agradecimento e assinatura, sem painel."""
        s = self.slide(painel=False)
        self.texto(s, ML, 4.05, 15.0, frase, T_CAPA * 0.62, TINTA, LIGHT,
                   espaco=1.1)
        self.logo(s, LOGO_KELLY, ML, 5.95, 3.55)
        if parceiro:
            self.fio_v(s, 6.20, 5.75, 1.25, CLARO, esp=0.014)
            self.logo(s, parceiro, 6.95, 5.90, 3.60)
        return s

    # ---------------------------------------------------------------- saida
    def salvar(self, caminho):
        self.prs.save(caminho)
        return caminho, len(self.prs.slides._sldIdLst)
