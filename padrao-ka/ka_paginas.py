#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROTEIRO DECLARATIVO — KA · Inteligencia para Marcas

Extensao do motor de layout (ka_layout.py) para apresentacoes cujo roteiro
nao e fixo: em vez de um contrato de campos, o conteudo do cliente declara
uma LISTA DE PAGINAS, cada uma dizendo o seu arquetipo e o que diz.

    PAGINAS = [
        {"tipo": "divisor", "numero": "01", "nome": "A origem"},
        {"tipo": "declaracao", "linhas": ["Uma frase", "em duas linhas."]},
        {"tipo": "texto", "titulo": "...", "paragrafos": [...]},
    ]

    from ka_paginas import DeckNarrativo
    d = DeckNarrativo(documento="Revelação de Essência", marca="Lucas Martini")
    d.montar(PAGINAS, pasta_assets)

A aparencia continua sendo a do SISTEMA-VISUAL.md: mesma grade, mesma
paleta, mesma escala tipografica, mesmos filetes. O que muda e so a
liberdade de ordenar as paginas.

Fotografia na horizontal
------------------------
O modelo da Revelacao de Essencia sangra a foto numa FAIXA VERTICAL, que
pede imagem em retrato. Quando o material do cliente vem em 16:9, essa
faixa recortaria a foto a um quarto da largura. Por isso aqui a fotografia
entra em FAIXA HORIZONTAL (`foto` + `lado` em "cima"/"baixo") ou em tela
cheia com veu (`foto_cheia`), que respeitam o enquadramento original.
"""
import json
import math
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.shapes import MSO_SHAPE_TYPE  # noqa: E402
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN  # noqa: E402
from pptx.oxml.ns import qn  # noqa: E402
from pptx.oxml.xmlchemy import OxmlElement  # noqa: E402

from rostos import foco as foco_cabeca  # noqa: E402
from ka_layout import (  # noqa: E402
    EMU,
    ACENTO, BRANCO, CLARO, CORPO, FIO, GRAFITE, PAINEL, TINTA,
    BOLD, LIGHT, SANS, SANS_LIGHT, SANS_SEMI, SEMI,
    T_CAPA, T_CORPO, T_DISPLAY, T_DIVISOR, T_DIV_APOIO, T_FRASE, T_H1,
    T_LEAD, T_LISTA, T_CAMADA_ROT, T_MEDIO,
    T_MINI, T_RODAPE, T_ROTULO, T_SUMARIO, T_SUBCAPA, T_ASSINATURA,
    T_DATA, T_FECHO, MEDIO, REG, ULTRA,
    ALT, LARG, ML, MR, PAINEL_M, W, Y_EYE, Y_H1, Y_RODAPE,
    LOGO_KA, SIMBOLO_IKIGAI, TRACO,
    Deck, partes, sem_marcas,
)

# ------------------------------------------------------------------ medidas
TOPO = 2.00          # primeira linha util dentro do painel
FUNDO = 9.15         # ultima caixa de texto comeca aqui, no maximo
COL, GAP = 3.35, 0.55

# MARCACAO DE IMAGEM. Quando a pagina pede fotografia e o arquivo ainda nao
# existe, o motor nao finge que a pagina nao tem foto: ele reserva a area
# EXATA que a imagem vai ocupar e a identifica. O layout aprovado e o mesmo
# layout que recebe a foto depois — quando o arquivo entra em `assets/` com
# o nome declarado em `foto`, a marcacao desaparece e nada se move.
MARCA_FUNDO = RGBColor(0xE9, 0xE5, 0xDC)    # area reservada sobre o claro
MARCA_ESCURO = RGBColor(0x32, 0x33, 0x30)   # area reservada em tela cheia
MARCA_SOBRE_ESCURO = RGBColor(0xC9, 0xC7, 0xC0)
MARCA_ACENTO_ESCURO = RGBColor(0xC6, 0x98, 0x6E)

# Largura media de caractere, em polegadas por ponto de corpo. So entra em
# cena se a Outfit nao estiver em padrao-ka/fontes/ — contar caractere trata
# "iii" e "MMM" como a mesma coisa e erra ate 15%.
CHAR = 0.0103

# A fonte com que o texto e medido. E a Light porque e a mais estreita da
# familia: medir por ela e errar sempre para o lado seguro.
FONTE_MEDIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fontes", "Outfit1Light.ttf")
# A Bold e visivelmente mais larga que a Light. No unico lugar em que o
# display sai em Bold — o nome da secao na virada —, medir pela Light faz a
# conta de caber errar para menos e a linha quebra sozinha no meio do nome.
FONTE_BOLD = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "fontes", "Outfit1Bold.ttf")
FONTE_SEMI = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "fontes", "Outfit1SemiBold.ttf")
FOLGA = 1.03         # o LibreOffice e o PowerPoint quebram um fio antes
_FONTES = {}


def _fonte(tam, arquivo=None):
    chave = (round(tam, 1), arquivo or FONTE_MEDIDA)
    if chave not in _FONTES:
        from PIL import ImageFont
        _FONTES[chave] = ImageFont.truetype(chave[1], int(round(tam * 4)))
    return _FONTES[chave]


def largura_texto(texto, tam, arquivo=None):
    """Largura real do texto, em polegadas, medida na propria fonte."""
    return _fonte(tam, arquivo).getlength(texto) / 4.0 / 72.0 * FOLGA


def linhas_rotulo(texto, tam, largura, spc):
    """Quantas linhas o rotulo espacejado ocupa.

    O espacejamento nao e detalhe: 2,82pt por caractere num rotulo de 27
    letras somam mais de uma polegada, e era por isso que "PROXIMIDADE COM A
    FUNDADORA" quebrava em duas linhas sem que a conta percebesse."""
    n, atual = 1, ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        larg = (largura_texto(teste, tam, FONTE_SEMI)
                + len(teste) * spc / 72.0)
        if not atual or larg <= largura:
            atual = teste
        else:
            n += 1
            atual = palavra
    return n


def linhas(texto, tam, largura):
    """Quantas linhas um texto ocupa nessa largura — medido, nao estimado.

    Repete a quebra por palavra que o PowerPoint faz. Sem a fonte no disco
    cai na conta por caractere, que e grosseira mas nunca subestima."""
    if not texto:
        return 0
    if not os.path.exists(FONTE_MEDIDA):
        por_linha = max(8, largura / (CHAR * tam))
        return max(1, int(math.ceil(len(texto) / por_linha)))
    n, atual = 1, ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if not atual or largura_texto(teste, tam) <= largura:
            atual = teste
        else:
            n += 1
            atual = palavra
    return n


# A entrelinha do PowerPoint multiplica a ALTURA DE LINHA da fonte, nao o
# corpo: a Outfit declara 1,26 em e o LibreOffice usa 1,20. Medir pelo corpo
# puro subestimava toda caixa em ~20% — era por isso que o filete de acento
# cortava a ultima linha do paragrafo mesmo com a contagem de linhas certa.
# A entrelinha e gravada EXATA (ver Deck.texto): 1,40 do corpo no texto,
# 1,37 no titulo. Nao ha mais fator de correcao da altura de linha da fonte —
# o que se escreve e o que o PowerPoint compoe, e por isso a medida fecha.
ENTRELINHA = 1.0


def altura(texto, tam, largura, espaco=1.4):
    return linhas(texto, tam, largura) * tam / 72.0 * espaco * ENTRELINHA


# Sobra de entrelinha embaixo da ultima linha, em ems. A caixa de texto mede
# n linhas inteiras, mas a ultima deixa esse respiro vazio por baixo. Quem
# vai encostar um filete ou uma frase no texto desconta isso — senao abre um
# vao que parece descuido.
SOBRA = 0.30


def pe(y, n, tam, espaco=1.4):
    """Onde a ultima linha de um bloco de texto termina, de verdade."""
    return y + n * tam / 72.0 * espaco * ENTRELINHA - tam / 72.0 * SOBRA


class DeckNarrativo(Deck):
    """Deck montado a partir de uma lista de paginas declaradas."""

    FATIA_V_MIN, FATIA_V_MAX = 0.38, 0.46
    FAIXA_MAX = 0.60          # alem disso a faixa nao deixa pagina para texto

    def __init__(self, documento, marca, assets=None, modelo=None,
                 escala="ka", rodape=True):
        super().__init__(documento, marca, modelo, escala)
        self.com_rodape = rodape
        self.assets = assets
        self.rostos = {}
        self.avisos = []
        self._areas = []
        if assets:
            mapa = os.path.join(assets, "rostos.json")
            if os.path.exists(mapa):
                with open(mapa, encoding="utf-8") as fp:
                    self.rostos = json.load(fp)

    def _enquadrar(self, caminho, w, h, padrao=0.5):
        """Foco que mantem a cabeca inteira dentro de uma caixa w x h.

        Devolve (foco, cabe). Sem mapa de rostos para a imagem, devolve o
        foco pedido e assume que cabe — e por isso que o rostos.json
        precisa existir."""
        c = self.rostos.get(os.path.basename(caminho))
        if not c:
            return padrao, True
        iw, ih = Image.open(caminho).size
        origem, alvo = iw / ih, w / h
        if abs(alvo - origem) < 1e-6:
            return 0.5, True
        eixo = "v" if alvo > origem else "h"
        return foco_cabeca(c, origem, alvo, eixo)

    # ------------------------------------------------ marcacao de imagem
    def marcacao(self, s, x, y, w, h, spec, escuro=False, baixo=False,
                 piso=None, fundo=True, raio=None):
        """A area reservada para uma fotografia que ainda nao existe.

        Nao e um lugar vazio: e a fotografia desenhada em negativo. Ocupa a
        medida exata que a imagem vai ocupar, diz que imagem e aquela, e sai
        de cena sozinha no dia em que o arquivo chegar.

        Em tela cheia (`baixo`) o rotulo e uma nota de producao no pe, e
        `piso` diz onde o texto da pagina terminou — sem isso o rotulo sobe
        por cima da frase."""
        if fundo:
            self.bloco(s, x, y, w, h,
                       MARCA_ESCURO if escuro else MARCA_FUNDO, raio=raio)
        cor_rot = MARCA_ACENTO_ESCURO if escuro else ACENTO
        cor_txt = MARCA_SOBRE_ESCURO if escuro else CORPO
        larg = min(w - 1.30, 12.60 if baixo else 8.60)
        if larg < 1.60:
            return
        nota = spec.get("imagem") or ""

        if baixo:
            # Em tela cheia a marcacao e NOTA DE PRODUCAO, nao composicao:
            # rotulo e briefing na MESMA linha, corpo miudo, encostados no pe
            # do padrao. Empilhar os dois nao cabe quando o nome da secao
            # ocupa duas linhas — e era ai que a nota atravessava o fundo.
            cx = x + ML
            larg_n = larg - 1.05      # o espaco que o rotulo come na 1a linha
            h_nota = altura(nota, T_MINI, larg_n) if nota else 0.0
            cy = 9.40 - (h_nota if nota else 0.40)
            if piso is not None:
                cy = max(cy, piso)
            tf = self.caixa(s, cx, cy, larg, h_nota + 0.12)
            par = self.par(tf, primeiro=True)
            self.txt(par, "IMAGEM   ", T_ROTULO, cor_rot, SEMI, spc=3.0)
            if nota:
                self.txt(par, nota, T_MINI, cor_txt, LIGHT)
            self._areas.append((cx - 0.2, cy - 0.2, larg + 0.4, h_nota + 0.5))
            return

        h_nota = altura(nota, T_CORPO, larg) if nota else 0.0
        bloco = 0.34 + 0.32 + (h_nota + 0.30 if nota else 0.0)
        cx = x + (w - larg) / 2.0
        cy = y + (h - bloco) / 2.0
        self.fio(s, cx, cy, 1.30, cor_rot, esp=0.03)
        self.texto(s, cx, cy + 0.34, larg, "IMAGEM", T_ROTULO, cor_rot, SEMI,
                   spc=3.0, h=0.32)
        if nota:
            self.texto(s, cx, cy + 0.96, larg, nota, T_CORPO, cor_txt, LIGHT,
                       h=h_nota + 0.1)
        # o rotulo pertence a area da foto: a centragem vertical da pagina
        # move o texto do conteudo, nunca a marcacao
        self._areas.append((cx - 0.2, cy - 0.2, larg + 0.4, bloco + 0.4))

    def _por_foto(self, s, x, y, w, h, caminho, foco, spec, escuro=False,
                  baixo=False, piso=None, raio=None):
        """A fotografia — ou, enquanto ela nao existe, a marcacao dela."""
        if caminho:
            return self.foto(s, x, y, w, h, caminho, foco=foco, raio=raio)
        return self.marcacao(s, x, y, w, h, spec, escuro, baixo, piso,
                             raio=raio)

    def _faixa_cabe(self, caminho, fatia):
        """A cabeca sobrevive a uma faixa horizontal dessa altura?"""
        return self._enquadrar(caminho, LARG, ALT * fatia)[1]

    # ------------------------------------------------------------ utilidades
    def arquivo(self, nome):
        if not nome or not self.assets:
            return None
        caminho = os.path.join(self.assets, nome)
        return caminho if os.path.exists(caminho) else None

    def veu(self, s, x, y, w, h, cor=TINTA, opacidade=0.52):
        """Veu sobre a fotografia, para o texto branco ter contraste."""
        sp = self.bloco(s, x, y, w, h, cor)
        solido = sp.fill._xPr.find(qn("a:solidFill"))
        clr = solido.find(qn("a:srgbClr"))
        alpha = OxmlElement("a:alpha")
        alpha.set("val", str(int(opacidade * 100000)))
        clr.append(alpha)
        return sp

    def rodape(self, s, sobre_foto=False, x=1.55, y=None,
               sobre_painel=False):
        """Pilula de identificacao. Sobre fotografia ela some e o texto vai
        direto em branco — pilula clara sobre foto suja a composicao."""
        if not getattr(self, "com_rodape", True):
            return
        y = Y_RODAPE if y is None else y
        if sobre_foto:
            tf = self.caixa(s, ML, y - 0.10, 10.0, 0.46)
            p = self.par(tf, True)
            self.txt(p, self.documento, T_RODAPE, BRANCO, SANS, spc=2.2)
            self.txt(p, "   |   ", T_RODAPE, BRANCO, SANS, spc=2.2)
            self.txt(p, self.marca, T_RODAPE, BRANCO, BOLD, spc=2.2)
            return
        self.bloco(s, x, y - 0.20, 9.30, 0.66, PAINEL, raio=0.18)
        tf = self.caixa(s, x + 0.45, y - 0.20, 8.4, 0.66, MSO_ANCHOR.MIDDLE)
        p = self.par(tf, True)
        self.txt(p, self.documento, T_RODAPE, TINTA, SANS, spc=2.2)
        self.txt(p, "   |   ", T_RODAPE, CLARO, SANS, spc=2.2)
        self.txt(p, self.marca, T_RODAPE, TINTA, BOLD, spc=2.2)
        # O logo-ka.png e uma tela QUADRADA com a marca no meio (a tinta
        # ocupa so 41%–60% da altura). Ancorar pelo topo da tela joga a
        # marca 0,7" abaixo do ponto pedido — foi assim que ela atravessou
        # a borda da faixa de fotografia. Aqui a conta e feita pela tinta.
        TINTA_TOPO, TINTA_BASE = 0.409, 0.597
        lg = 1.72
        if sobre_painel:
            # na faixa, a marca centra na mesma linha optica da pilula
            alvo = y + 0.13 - (TINTA_TOPO + TINTA_BASE) / 2 * lg
        else:
            alvo = y + 0.48 - TINTA_TOPO * lg
        self.logo(s, LOGO_KA, 16.55, alvo, lg)

    def cabeca(self, s, spec, x=ML, w=W, cor=TINTA, cor_eye=CLARO, y=Y_H1):
        """Eyebrow + titulo + filete. Devolve o y onde o corpo pode comecar."""
        if spec.get("eyebrow"):
            self.texto(s, x, y - 0.52, w, spec["eyebrow"].upper(), T_ROTULO,
                       cor_eye, SANS, spc=3.0, h=0.32)
        titulo = spec.get("titulo")
        if not titulo:
            return y
        # Titulo de pagina em CAIXA ALTA, com a frase-chave em Bold (o `**`
        # do conteudo). Caixa alta ocupa cerca de 10% mais largura que caixa
        # baixa, entao a conta de linhas usa o texto ja convertido — e sem os
        # marcadores, que nao se imprimem. Bold e mais largo que Light, e a
        # FOLGA da medida cobre essa diferenca.
        titulo = (titulo.upper() if isinstance(titulo, str)
                  else [l.upper() for l in titulo])
        tam = spec.get("tam_titulo", T_H1)
        nu = sem_marcas(titulo)
        n = linhas(nu, tam, w) if isinstance(titulo, str) else len(titulo)
        self.titulo(s, titulo, x, y, w, tam, cor)
        # O filete sai da altura REAL do titulo, nao de uma estimativa: num
        # titulo de duas linhas a conta antiga encostava o filete no texto, e
        # num de uma linha sobrava um vao.
        fim = y + n * tam / 72.0 * 1.37 + 0.20
        self.fio(s, x, fim, w, FIO if cor is TINTA else CLARO)
        return fim + 0.38

    def corpo(self, s, spec, x, y, w, fim=FUNDO, cor=CORPO, cor_forte=TINTA):
        """Lead, paragrafos, itens e destaque — o miolo comum a varias
        paginas.

        Mede tudo antes de desenhar. Numa pagina com faixa de fotografia
        sobra pouco mais de um terco da altura, e o mesmo texto que respira
        na pagina inteira estoura ali. Quando nao cabe, o metodo aperta
        primeiro os intervalos e so depois reduz o corpo — nunca deixa
        vazar."""
        tam_lead, tam_corpo = T_LEAD, spec.get("tam_corpo", T_CORPO)
        tam_dest = spec.get("tam_destaque", T_MEDIO)
        gap_lead, gap_par, gap_item, gap_dest = 0.30, 0.26, 0.08, 0.48

        def medir(k):
            total, blocos = 0.0, []
            if spec.get("lead"):
                h = altura(spec["lead"], tam_lead * k, w) + 0.12
                blocos.append(("lead", h)); total += h + gap_lead * k
            for par in spec.get("paragrafos", []):
                h = altura(sem_marcas(par), tam_corpo * k, w) + 0.10
                blocos.append(("par", h, par)); total += h + gap_par * k
            for item in spec.get("itens", []):
                h = max(0.40, altura(item, tam_corpo * k, w - 0.5) + 0.06)
                blocos.append(("item", h, item)); total += h + gap_item * k
            if spec.get("destaque"):
                h = altura(spec["destaque"], tam_dest * k, w, 1.25) + 0.14
                blocos.append(("dest", h)); total += h + gap_dest * k
            return total, blocos

        disponivel = fim - y - 0.14
        k = 1.0
        total, _ = medir(k)
        if total > disponivel:
            gap_lead, gap_par, gap_item, gap_dest = 0.20, 0.18, 0.04, 0.38
            total, _ = medir(k)
        while total > disponivel and k > 0.92:
            k -= 0.04
            total, _ = medir(k)
        if total > disponivel:
            # O corpo nao desce mais: abaixo de 92% o texto deixa de ser
            # legivel de longe. Quem precisa ceder e o texto — avisa no build
            # para que a pagina seja cortada ou quebrada em duas.
            self.avisos.append(
                "texto nao cabe em \"%s\": sobram %.2f\" para cortar"
                % (spec.get("titulo") or spec.get("eyebrow") or "?",
                   total - disponivel))
        _, blocos = medir(k)

        for b in blocos:
            if b[0] == "lead":
                self.texto(s, x, y, w, spec["lead"], tam_lead * k, cor_forte,
                           LIGHT, h=b[1])
                y += b[1] + gap_lead * k
            elif b[0] == "par":
                self.texto_rico(s, x, y, w, b[2], tam_corpo * k, cor, LIGHT,
                                h=b[1])
                y += b[1] + gap_par * k
            elif b[0] == "item":
                self.ponto(s, x + 0.05, y + 0.17, 0.085, CLARO)
                self.texto(s, x + 0.48, y, w - 0.48, b[2], tam_corpo * k,
                           cor_forte, LIGHT, h=b[1])
                y += b[1] + gap_item * k
            else:
                y += 0.14
                self.fio(s, x, y, 1.30, ACENTO, esp=0.03)
                y += 0.34
                self.texto(s, x, y, w, spec["destaque"], tam_dest * k,
                           cor_forte, LIGHT, espaco=1.25, h=b[1])
                y += b[1]
        return y

    # ------------------------------------------------------- paginas de foto
    def _abrir(self, spec):
        """Abre a pagina. Quando ha fotografia ela entra como FAIXA
        horizontal sangrando no topo ou no pe, e o painel claro ocupa o
        resto; sem fotografia, e o painel de sempre.

        Devolve (slide, y do primeiro elemento, y limite do conteudo).
        """
        self._col, self._h_foto = (ML, W), 0
        pedida = spec.get("foto")
        if not pedida:
            return self.slide(), Y_H1, FUNDO
        caminho = self.arquivo(pedida)
        # O arquivo ainda nao existe: a pagina sai com a MARCACAO da imagem,
        # na medida exata que a fotografia vai ocupar.
        marcar = caminho is None
        lado = spec.get("lado", "direita")
        nome = os.path.basename(pedida)

        if not marcar:
            iw, ih = Image.open(caminho).size
            # Retrato nunca entra em faixa horizontal: o corte sobraria um
            # sexto da altura, so a testa.
            if lado in ("cima", "baixo") and iw / ih < 1.15:
                lado = "direita"

        # A faixa horizontal corta a imagem na VERTICAL, e e ai que a cabeca
        # se perde. Se a faixa que o texto permite nao comporta a cabeca
        # inteira, a pagina vira tira vertical — cortar o rosto nao e uma
        # opcao, e a tira corta na horizontal, onde sobra folga de sobra.
        if not marcar and lado in ("cima", "baixo"):
            faixa = min(self._fatia(spec), self.FAIXA_MAX)
            if not self._faixa_cabe(caminho, faixa):
                precisa = faixa
                while precisa <= self.FAIXA_MAX and \
                        not self._faixa_cabe(caminho, precisa):
                    precisa += 0.02
                if precisa > self.FAIXA_MAX:
                    self.avisos.append(
                        "%s: faixa horizontal cortaria a cabeca; virou tira "
                        "vertical" % nome)
                    lado = spec.get("virar", "direita")
                elif FUNDO - (ALT * precisa + 0.95) < \
                        self._altura_texto(spec) * 0.92:
                    # A faixa que o rosto exige nao deixa pagina para o
                    # texto. O miolo ainda aperta um pouco (dai o 0,92),
                    # mas espremer alem disso e trocar um problema por
                    # outro: a pagina vai para a tira vertical
                    self.avisos.append(
                        "%s: a faixa que o rosto exige nao deixa espaco "
                        "para o texto; virou tira vertical" % nome)
                    lado = spec.get("virar", "esquerda")
                else:
                    spec = dict(spec, fatia=precisa)

        s = self.slide(painel=False)

        if lado == "solta":
            # A imagem SOLTA: um retangulo de cantos arredondados pousado
            # sobre o painel, a direita, sem sangrar. E o tratamento que a
            # Kelly mais usou — a foto convive com o painel em vez de
            # substituir metade dele.
            self.bloco(s, PAINEL_M, PAINEL_M, LARG - 2 * PAINEL_M,
                       ALT - 2 * PAINEL_M - 0.55, PAINEL, raio=0.18)
            x_img = spec.get("x_imagem", 11.95)
            w_img = spec.get("larg_imagem", 6.95)
            h_img = spec.get("alt_imagem", 7.85)
            y_img = (ALT - 0.55) / 2.0 - h_img / 2.0
            self._por_foto(s, x_img, y_img, w_img, h_img, caminho,
                           spec.get("foco", 0.5), spec, raio=0.18)
            self._col = (ML, x_img - ML - 0.50)
            return s, Y_H1, FUNDO

        if lado in ("direita", "esquerda"):
            v = max(self.FATIA_V_MIN, spec.get("fatia_v", self.FATIA_V_MIN))
            foco = spec.get("foco", 0.5)
            if not marcar:
                # a tira cresce ate a cabeca caber, dentro de um limite
                while v < self.FATIA_V_MAX and \
                        not self._enquadrar(caminho, LARG * v, ALT)[1]:
                    v += 0.01
                foco, cabe = self._enquadrar(caminho, LARG * v, ALT, foco)
                if not cabe:
                    self.avisos.append(
                        "%s: cabeca nao cabe nem na tira" % nome)
            corte = LARG * v
            if lado == "direita":
                self.bloco(s, 0, 0, LARG - corte, ALT, PAINEL)
                self._por_foto(s, LARG - corte, 0, corte, ALT, caminho, foco,
                               spec)
                self._col = (ML, LARG - corte - ML - 0.95)
            else:
                self._por_foto(s, 0, 0, corte, ALT, caminho, foco, spec)
                self.bloco(s, corte, 0, LARG - corte, ALT, PAINEL)
                self._col = (corte + 0.95, LARG - corte - 1.90)
            return s, Y_H1, FUNDO

        self._col = (ML, W)
        h_foto = ALT * min(spec.get("fatia", 0.42), self.FAIXA_MAX)
        foco = spec.get("foco", 0.16)
        if not marcar:
            foco, cabe = self._enquadrar(caminho, LARG, h_foto, foco)
            if not cabe:
                self.avisos.append("%s: cabeca cortada na faixa" % nome)
        if lado == "cima":
            self._por_foto(s, 0, 0, LARG, h_foto, caminho, foco, spec)
            self.bloco(s, 0, h_foto, LARG, ALT - h_foto, PAINEL)
            return s, h_foto + 0.95, FUNDO
        self.bloco(s, 0, 0, LARG, ALT - h_foto, PAINEL)
        self._por_foto(s, 0, ALT - h_foto, LARG, h_foto, caminho, foco, spec)
        self._h_foto = h_foto
        return s, 1.70, ALT - h_foto - 1.25

    def _altura_texto(self, spec):
        """Altura que o miolo da pagina pede, em polegadas."""
        w = spec.get("largura", 13.4)
        preciso = 1.30  # cabeca: eyebrow, titulo e filete
        if spec.get("lead"):
            preciso += altura(spec["lead"], T_LEAD, w) + 0.50
        for par in spec.get("paragrafos", []):
            preciso += altura(par, T_CORPO, w) + 0.36
        for item in spec.get("itens", []):
            preciso += max(0.58, altura(item, T_CORPO, w - 0.5) + 0.18)
        if spec.get("destaque"):
            preciso += altura(spec["destaque"],
                              spec.get("tam_destaque", T_MEDIO), w, 1.25) + 0.62
        return preciso

    def _fatia(self, spec):
        """Quanto da pagina a fotografia pode tomar.

        A faixa e generosa por padrao, mas cede altura quando o texto
        precisa: uma faixa de 42%% com lead, paragrafo e destaque embaixo
        obriga a reduzir o corpo ate o texto ficar ilegivel. Melhor a foto
        perder dois centimetros do que a leitura perder dois pontos."""
        # espaco util abaixo da faixa: comeca 0,95" depois dela e termina
        # no fundo do painel — nao e ALT menos a faixa
        sobra = FUNDO - 0.95 - self._altura_texto(spec)
        return max(0.24, min(spec.get("fatia", 0.42), sobra / ALT))

    def _fechar(self, s, spec):
        x, _ = getattr(self, "_col", (ML, W))
        baixo = (bool(self.arquivo(spec.get("foto")))
                 and spec.get("lado", "cima") == "baixo"
                 and getattr(self, "_h_foto", 0))
        if baixo:
            # dentro do painel, logo acima da faixa: o rodape em branco sobre
            # uma fotografia clara simplesmente desaparece
            self.rodape(s, x=min(x - 0.65, 11.0),
                        y=ALT - self._h_foto - 0.52, sobre_painel=True)
        else:
            self.rodape(s, x=min(x - 0.65, 11.0))

    def pg_foto(self, spec):
        """Pagina de fotografia com texto corrido — mesmo corpo da pagina de
        texto, so que aberta com a faixa."""
        return self.pg_texto(spec)

    def pg_foto_cheia(self, spec):
        """Fotografia em tela cheia com um CARTAO claro por cima.

        No arquivo da Kelly a frase sobre a foto nao vem em branco com veu:
        vem num cartao do mesmo claro do painel, encostado no alto a direita.
        O veu escurece a imagem inteira para salvar o texto; o cartao
        preserva a fotografia e ainda assim garante leitura."""
        s = self.slide(painel=False)
        caminho = self.arquivo(spec.get("foto"))
        if caminho:
            foco, _ = self._enquadrar(caminho, LARG, ALT, spec.get("foco", 0.5))
            self.foto(s, 0, 0, LARG, ALT, caminho, foco=foco)
        elif spec.get("foto"):
            self.bloco(s, 0, 0, LARG, ALT, MARCA_ESCURO)
        else:
            self.veu(s, 0, 0, LARG, ALT, TINTA, spec.get("veu", 0.58))

        linhas_ = spec.get("linhas") or [spec.get("titulo", "")]
        larg = spec.get("larg_cartao", 8.54)
        recuo = 0.62
        lg = larg - 2 * recuo
        tam = spec.get("tam", T_FRASE)
        while tam > 18 and max(linhas(l, tam, lg)
                               for l in sem_marcas(linhas_)) > 1:
            tam -= 1
        alt_frase = len(linhas_) * tam / 72.0 * 1.34
        h_apoio = (altura(sem_marcas(spec["apoio"]), T_MINI, lg)
                   if spec.get("apoio") else 0.0)
        alt = recuo + alt_frase + (0.18 + h_apoio if h_apoio else 0.0) + recuo
        x = spec.get("x_cartao", LARG - larg - 0.0)
        y = spec.get("y_cartao", 1.125)
        self.bloco(s, x, y, larg, alt, PAINEL, raio=0.18)
        self.texto_rico(s, x + recuo, y + recuo, lg, linhas_, tam, TINTA,
                        LIGHT, espaco=1.34, h=alt_frase + 0.12)
        if h_apoio:
            self.texto(s, x + recuo, y + recuo + alt_frase + 0.18, lg,
                       spec["apoio"], T_MINI, CORPO, LIGHT, h=h_apoio + 0.1)
        if not caminho and spec.get("foto"):
            self.marcacao(s, 0, 0, LARG, ALT, spec, escuro=True, baixo=True,
                          piso=y + alt + 0.50, fundo=False)
        self.rodape(s, sobre_foto=True)
        return s

    # ---------------------------------------------------- paginas tipograficas
    def _tam_display(self, linhas_, largura, teto=T_DISPLAY, piso=24):
        """Corpo que faz as quebras do autor valerem.

        Numa pagina de frase as linhas sao escritas a mao: cada uma e uma
        unidade de sentido. Se o corpo for grande demais para a largura, a
        linha quebra sozinha no meio e a intencao se perde — por isso o
        tamanho sai da linha mais longa, nao de uma tabela.

        A linha mais longa e MEDIDA na propria Outfit. Contar caractere
        tratava "iii" e "MMM" como a mesma coisa e errava para menos: numa
        frase de 28 caracteres sobravam cinco polegadas de painel vazio e a
        pagina de silencio entrava um terco menor do que podia."""
        maior = max(linhas_, key=len, default="")
        if not maior:
            return teto
        tam = teto
        while tam > piso and largura_texto(maior, tam) > largura:
            tam -= 1
        return max(piso, tam)

    def pg_declaracao(self, spec):
        """A pagina de silencio: uma frase grande e muito ar."""
        s = self.slide()
        linhas_ = spec.get("linhas", [])
        tam = spec.get("tam") or self._tam_display(sem_marcas(linhas_), 15.4)
        # a frase sai com entrelinha 1,26 e a fonte ainda tem a sua propria
        # altura de linha: sem ENTRELINHA o bloco mede 20% a menos do que
        # ocupa, e o filete de acento acaba por cima da segunda linha
        alt_bloco = len(linhas_) * tam / 72.0 * 1.40
        extra = 0.0
        if spec.get("apoio"):
            extra = 0.90 + altura(sem_marcas(spec["apoio"]), T_CORPO, 13.0)
        y = (9.60 + 1.10 - alt_bloco - extra) / 2
        if spec.get("eyebrow"):
            # o eyebrow sobe um pouco: colado, o filete de acento parecia
            # sublinhar o rotulo em vez de abrir a frase
            self.texto(s, ML, y - 0.98, W, spec["eyebrow"].upper(), T_ROTULO,
                       ACENTO if spec.get("marcar") else CLARO, SEMI if
                       spec.get("marcar") else SANS, spc=3.0, h=0.32)
        self.fio(s, ML, y - 0.44, 1.30, ACENTO, esp=0.03)
        self.texto_rico(s, ML, y, 15.4, linhas_, tam, GRAFITE, LIGHT,
                        espaco=1.40, h=alt_bloco + 0.30)
        if spec.get("apoio"):
            self.texto_rico(s, ML, pe(y, len(linhas_), tam, 1.40) + 0.42, 13.0,
                            spec["apoio"], T_CORPO, CORPO, LIGHT,
                            h=altura(sem_marcas(spec["apoio"]), T_CORPO, 13.0)
                            + 0.1)
        self.rodape(s)
        return s

    def pg_texto(self, spec):
        s, y0, fim = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        # Um titulo e um bloco de texto: como o bloco e o unico texto da
        # pagina, ele le num corpo maior. Quando a pagina tem lead, itens ou
        # destaque, a escala volta ao normal para a hierarquia nao sumir.
        if (spec.get("paragrafos") and not spec.get("lead")
                and not spec.get("itens") and not spec.get("destaque")):
            spec = dict(spec, tam_corpo=spec.get("tam_corpo", T_LEAD))
        self.corpo(s, spec, X, y, spec.get("largura", min(13.4, LG)), fim)
        self._fechar(s, spec)
        return s

    def pg_colunas(self, spec):
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        if spec.get("lead"):
            h = altura(spec["lead"], T_CORPO, min(14.0, LG)) + 0.1
            self.texto(s, X, y, min(14.0, LG), spec["lead"], T_CORPO, CORPO, LIGHT, h=h)
            y += h + 0.46
        cols = spec["colunas"]
        n = len(cols)
        larg = (LG - GAP * (n - 1)) / n
        fundo = y
        for i, (rot, desc) in enumerate(cols):
            cx = X + i * (larg + GAP)
            # o filete da coluna e GROSSO e de ACENTO: e ele que abre o
            # campo. O da camada e fino e cinza; sao dois papeis diferentes
            self.bloco(s, cx, y, larg, 0.062, ACENTO)
            h_rot = altura(sem_marcas(rot), T_MEDIO, larg, 1.40) + 0.1
            self.texto_rico(s, cx, y + 0.30, larg, rot, T_MEDIO, TINTA, LIGHT,
                            h=h_rot)
            dy = y + 0.30 + h_rot + 0.22
            h = altura(sem_marcas(desc), T_CORPO, larg) + 0.1
            self.texto_rico(s, cx, dy, larg, desc, T_CORPO, CORPO, LIGHT, h=h)
            fundo = max(fundo, dy + h)
        # o divisor vertical entre duas colunas, no mesmo acento
        if n == 2:
            self.bloco(s, X + larg + GAP / 2 - 0.011, y + 0.34, 0.021,
                       max(0.6, fundo - y - 0.50), ACENTO)
        if spec.get("equacao"):
            tf = self.caixa(s, X, min(fundo + 0.45, 8.45), LG, 0.55)
            p = self.par(tf, True, align=PP_ALIGN.CENTER)
            for i, palavra in enumerate(spec["equacao"][:-1]):
                if i:
                    self.txt(p, "  +  ", T_MEDIO, ACENTO, LIGHT)
                self.txt(p, palavra, T_MEDIO, CORPO, LIGHT)
            self.txt(p, "  =  ", T_MEDIO, ACENTO, LIGHT)
            self.txt(p, spec["equacao"][-1], T_MEDIO, TINTA, SEMI)
            fundo = min(fundo + 0.45, 8.45) + 0.55
        if spec.get("fecho"):
            # centrado, e nao alinhado a esquerda: no arquivo dela o fecho de
            # uma pagina de colunas fica no eixo, costurando as duas
            lg = min(11.28, LG)
            h = altura(sem_marcas(spec["fecho"]), T_CORPO, lg) + 0.1
            base = fundo + 0.62
            if base > FIM - h + 0.3:
                # nao ha pagina para o fecho. Empurrar para cima e pior que
                # nao ter fecho: ele entra POR CIMA da coluna mais longa. O
                # texto e que precisa ceder — avisa no build.
                self.avisos.append(
                    "o fecho nao cabe em \"%s\": a coluna mais longa precisa "
                    "de %.2f\" a menos"
                    % (sem_marcas(spec.get("titulo") or "?"),
                       base - (FIM - h + 0.3)))
                base = FIM - h + 0.3
            self.texto_rico(s, X + (LG - lg) / 2.0, base, lg,
                            spec["fecho"], T_CORPO, CORPO, LIGHT,
                            align=PP_ALIGN.CENTER, h=h)
        self._fechar(s, spec)
        return s

    def pg_palavras(self, spec):
        """Palavras soltas como composicao — Casa. Renda. Patrimonio."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        if spec.get("lead"):
            h = altura(spec["lead"], T_CORPO, min(13.4, LG)) + 0.1
            self.texto(s, X, y, min(13.4, LG), spec["lead"], T_CORPO, CORPO, LIGHT, h=h)
            y += h + 0.40
        palavras = spec["palavras"]
        n = len(palavras)
        colunas = spec.get("grade", 2 if n > 4 else 1)
        por_col = int(math.ceil(n / colunas))
        larg = (LG - GAP * (colunas - 1)) / colunas
        tam = spec.get("tam", T_FRASE if n <= 6 else T_MEDIO)
        passo = tam / 72.0 * 1.9
        for i, palavra in enumerate(palavras):
            c, r = i // por_col, i % por_col
            cx = X + c * (larg + GAP)
            cy = y + r * passo
            self.fio(s, cx, cy + passo - 0.22, larg)
            self.texto(s, cx, cy, larg, palavra, tam, TINTA, LIGHT,
                       h=passo - 0.18)
        fundo = y + por_col * passo + 0.35
        if spec.get("destaque"):
            self.fio(s, X, min(fundo, FIM - 0.55), 1.30, ACENTO, esp=0.03)
            h = altura(spec["destaque"], T_MEDIO, LG, 1.25) + 0.14
            self.texto(s, X, min(fundo + 0.34, FIM), LG, spec["destaque"],
                       T_MEDIO, TINTA, LIGHT, espaco=1.25, h=h)
        self._fechar(s, spec)
        return s

    def pg_fluxo(self, spec):
        """Passos encadeados na horizontal, com seta de acento."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        passos = spec["passos"]
        n = len(passos)
        larg = (LG - 0.55 * (n - 1)) / n
        topo = max(y + 0.70, 4.80)
        for i, passo in enumerate(passos):
            cx = X + i * (larg + 0.55)
            self.fio(s, cx, topo, larg, ACENTO if i == n - 1 else FIO,
                     esp=0.03 if i == n - 1 else 0.012)
            self.texto(s, cx, topo + 0.34, larg, passo, T_LEAD, TINTA, LIGHT,
                       h=altura(passo, T_LEAD, larg, 1.25) + 0.12)
            if i < n - 1:
                self.texto(s, cx + larg + 0.06, topo + 0.26, 0.45, "→",
                           T_MEDIO, ACENTO, LIGHT, h=0.42)
        fundo = topo + 0.40 + max(
            altura(p, T_LEAD, larg, 1.25) for p in passos)
        if spec.get("sintese"):
            tf = self.caixa(s, X, min(fundo + 0.65, FIM - 0.3), LG, 0.55)
            p = self.par(tf, True, align=PP_ALIGN.CENTER)
            for i, etapa in enumerate(spec["sintese"]):
                if i:
                    self.txt(p, "   ·   ", T_MEDIO, ACENTO, LIGHT)
                self.txt(p, etapa, T_MEDIO, TINTA, LIGHT)
        self._fechar(s, spec)
        return s

    def pg_contraste(self, spec):
        """Dois campos em oposicao, separados por um filete vertical."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        if spec.get("lead"):
            h = altura(spec["lead"], T_CORPO, min(13.4, LG)) + 0.1
            self.texto(s, X, y, min(13.4, LG), spec["lead"], T_CORPO, CORPO, LIGHT, h=h)
            y += h + 0.50
        larg = (LG - 1.70) / 2
        meio = X + larg + 0.85
        # A coluna mais longa manda, e ela e medida pela altura REAL do
        # texto, nao pela contagem de itens: quatro itens que quebram em duas
        # linhas ocupam o dobro do que a conta por item previa, e era por ai
        # que a ultima linha saia do painel. Antes de reduzir o corpo, o
        # bloco sobe — perder ar no topo custa menos que perder dois pontos.
        for tam in (T_LEAD, T_CORPO, T_MINI):
            gap = 0.22 if tam == T_LEAD else 0.14
            pior = max(sum(altura(i, tam, larg, 1.3) + 0.08 + gap
                           for i in lado[1])
                       for lado in (spec["esquerda"], spec["direita"])) - gap
            topo = min(max(y, 5.00), FIM + 0.30 - 0.72 - pior)
            if topo >= y:
                break
        topo = max(topo, y)
        fundo = topo
        for i, (rot, itens) in enumerate([spec["esquerda"], spec["direita"]]):
            cx = X + i * (larg + 1.70)
            self.fio(s, cx, topo, larg, ACENTO if i == 0 else FIO,
                     esp=0.03 if i == 0 else 0.012)
            self.rotulo(s, rot, cx, topo + 0.30, larg,
                        ACENTO if i == 0 else CLARO)
            yy = topo + 0.72
            for item in itens:
                h = altura(item, tam, larg, 1.3) + 0.08
                self.texto(s, cx, yy, larg, item, tam, TINTA, LIGHT, h=h)
                yy += h + gap
            fundo = max(fundo, yy)
        self.fio_v(s, meio - 0.02, topo, fundo - topo - 0.2, FIO, esp=0.014)
        self.texto(s, meio - 0.22, (topo + fundo) / 2 - 0.30, 0.5, "×",
                   T_FRASE, CLARO, LIGHT, h=0.5)
        if spec.get("destaque"):
            h = altura(spec["destaque"], T_MEDIO, LG, 1.25) + 0.14
            self.fio(s, X, min(fundo + 0.30, FIM - 0.5), 1.30, ACENTO,
                     esp=0.03)
            self.texto(s, X, min(fundo + 0.64, FIM), LG, spec["destaque"],
                       T_MEDIO, TINTA, LIGHT, espaco=1.25, h=h)
        self._fechar(s, spec)
        return s

    def pg_camadas(self, spec):
        """Rotulo + leitura, empilhados: a escada de significado."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        itens = spec["camadas"]
        cab = spec.get("cabecalhos")
        larg = LG - min(5.60, LG * 0.40)
        larg_rot = min(5.20, LG * 0.37)
        # o degrau tem a altura do maior dos dois lados: um rotulo que quebra
        # em duas linhas precisa de espaco tanto quanto uma leitura longa
        n_rot = [linhas_rotulo(rot.upper(), T_CAMADA_ROT, larg_rot, 2.82)
                 for rot, _ in itens]
        alt_rot = [n * T_CAMADA_ROT / 72.0 * 1.30 for n in n_rot]
        # Cada degrau tem a altura do seu proprio texto. Dividir o espaco em
        # partes iguais estoura a pagina quando uma das leituras e longa.
        # Antes de reduzir o corpo, a escada SOBE: perder ar no topo custa
        # menos que perder oito pontos de corpo — com seis degraus, o piso
        # de 4,20" sozinho jogava a leitura inteira para 17pt. So depois de
        # a escada encostar no titulo e que o corpo desce um degrau, porque
        # encolher a caixa abaixo do que o texto ocupa nao faz o texto
        # encolher: faz ele invadir a linha de baixo.
        piso = y + (0.56 if cab else 0.0)
        teto = max(piso, 4.20 + (0.56 if cab else 0.0))
        # A ordem das tentativas: primeiro o corpo do padrao com o ar de
        # sempre; depois o mesmo corpo com o ar apertado (0,38" = os 0,30 do
        # alinhamento do rotulo mais um respiro, o minimo que nao encosta); so
        # entao o corpo menor. Com seis degraus a escada passava do limite por
        # tres centesimos de polegada — e perdia oito pontos de corpo por
        # causa deles.
        for tam_desc, ar in ((T_CORPO, 0.44), (T_CORPO, 0.38), (T_MINI, 0.44)):
            alturas = [max(0.72, altura(sem_marcas(desc), tam_desc, larg, 1.40)
                           + ar, alt_rot[i] + 0.52)
                       for i, (_, desc) in enumerate(itens)]
            topo = min(teto, max(piso, FIM + 0.30 - sum(alturas)))
            # a tolerancia de um centesimo de polegada nao e folga: e que o
            # topo sai de FIM - soma, e comparar soma com FIM - topo depois
            # disso e comparar um float consigo mesmo. Sem ela, a escada que
            # cabe EXATO (seis degraus, o caso comum) era reprovada por um
            # erro de arredondamento e caia oito pontos de corpo.
            if sum(alturas) <= FIM + 0.30 - topo + 0.01:
                break
        espaco = FIM + 0.30 - topo
        if cab:
            # os dois titulos de coluna, escritos uma vez so acima da
            # escada. E o que transforma a camada em tabela de duas colunas
            # sem encher a pagina de cartoes
            self.rotulo(s, cab[0], X, topo - 0.56, larg_rot, CLARO)
            self.rotulo(s, cab[1], X + min(5.60, LG * 0.40), topo - 0.56,
                        larg, ACENTO)
        folga = espaco - sum(alturas)
        if folga > 0:
            alturas = [a + min(0.42, folga / len(itens)) for a in alturas]
        yy = topo
        for i, (rot, desc) in enumerate(itens):
            ultimo = i == len(itens) - 1
            self.fio(s, X, yy, LG)
            # O rotulo e Semi-Bold de 18pt, espacejado, em TINTA — so o
            # ultimo degrau recebe o acento, para fechar a escada.
            self.texto(s, X, yy + 0.30, larg_rot, rot.upper(),
                       T_CAMADA_ROT, ACENTO if ultimo else TINTA, SEMI,
                       spc=2.82, h=max(0.40, alt_rot[i] + 0.10))
            self.texto_rico(s, X + min(5.60, LG * 0.40), yy + 0.22, larg, desc,
                            tam_desc, TINTA, LIGHT, h=alturas[i] - 0.30)
            yy += alturas[i]
        # o acento fecha a escada por baixo. Em cima da ultima linha ele
        # parece sublinhar a penultima, que e justamente a que nao importa
        self.fio(s, X, min(yy, FIM + 0.30), 1.30, ACENTO, esp=0.03)
        self._fechar(s, spec)
        return s

    def pg_lista(self, spec):
        """Itens com ponto. Lista curta respira numa coluna; lista longa de
        itens curtos vai para duas, em vez de espremer a entrelinha."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        if spec.get("lead"):
            h = altura(spec["lead"], T_CORPO, min(13.4, LG)) + 0.1
            self.texto(s, X, y, min(13.4, LG), spec["lead"], T_CORPO, CORPO, LIGHT, h=h)
            y += h + 0.42
        itens = spec.get("itens") or []
        if not itens:                      # lista vazia e, na pratica, texto
            self.corpo(s, spec, X, y, spec.get("largura", min(13.4, LG)), FIM)
            self._fechar(s, spec)
            return s
        reservado = 0.0
        if spec.get("destaque"):
            reservado = 0.95 + altura(spec["destaque"], T_MEDIO, LG, 1.25)
        if spec.get("fecho"):
            reservado += 0.52 + altura(spec["fecho"], T_CORPO, min(13.4, LG))
        disponivel = FIM - y - reservado

        colunas = spec.get("grade", 1)
        if colunas == 1 and len(itens) >= 6 and disponivel / len(itens) < 0.50 \
                and max(len(i) for i in itens) <= 56 and LG >= 12.0:
            colunas = 2
        por_col = int(math.ceil(len(itens) / colunas))
        largura = spec.get("largura", (min(13.0, LG) if colunas == 1
                                       else (LG - 0.90) / 2))
        # 18pt de corpo pede 0,45" de entrelinha; abaixo disso as linhas
        # encostam. Em vez de espremer, a lista vai para duas colunas
        if colunas == 1 and len(itens) >= 4 and LG >= 12.0 \
                and disponivel / por_col < 0.46:
            colunas, por_col = 2, int(math.ceil(len(itens) / 2))
            largura = (LG - 0.90) / 2

        # Cada item tem a altura do SEU proprio texto. Distribuir o espaco em
        # passos iguais subestima o item que quebra em duas linhas, e era por
        # isso que o filete de acento do fecho atravessava a ultima linha.
        def medir(tam):
            alturas = [max(0.46, altura(sem_marcas(i), tam, largura - 0.576,
                                       1.40) + 0.06)
                       for i in itens]
            pior = max(sum(alturas[c * por_col:(c + 1) * por_col])
                       for c in range(colunas))
            return alturas, pior

        # O item de lista le em 30pt — maior que o corpo, e em tinta cheia.
        # A lista nao e texto corrido: cada linha e uma afirmacao.
        for tam in (T_LISTA, T_CORPO, T_MINI):
            alturas, pior = medir(tam)
            if pior <= disponivel:
                break
        # o que sobra vira ar entre os itens, ate o limite de respiro do padrao
        folga = min(0.26, max(0.0, (disponivel - pior) / max(1, por_col)))

        fundo = y
        for c in range(colunas):
            cx = X + c * (largura + 0.90)
            yy = y
            for i in range(c * por_col, min(len(itens), (c + 1) * por_col)):
                item = itens[i]
                # O marcador e um QUADRADO de acento, nao um ponto cinza: no
                # arquivo da Kelly ele tem 0,112" e e a unica cor da pagina.
                self.bloco(s, cx + 0.004, yy + 0.19, 0.112, 0.112, ACENTO)
                self.texto_rico(s, cx + 0.576, yy, largura - 0.576, item, tam,
                                TINTA, LIGHT, h=alturas[i])
                yy += alturas[i] + folga
            fundo = max(fundo, yy - folga)
        if spec.get("destaque"):
            # o fecho nao desce alem do painel, mesmo quando a lista
            # cresceu mais do que a reserva previa
            h = altura(spec["destaque"], T_MEDIO, LG, 1.25) + 0.14
            base = min(fundo + 0.58, FIM + 0.28 - h)
            self.fio(s, X, base - 0.34, 1.30, ACENTO, esp=0.03)
            self.texto(s, X, base, LG, spec["destaque"], T_MEDIO, TINTA,
                       LIGHT, espaco=1.25, h=h)
            fundo = base + h
        if spec.get("fecho"):
            # o fecho e a conclusao da lista: mesmo corpo, mesma cor, sem
            # filete. Nao e um destaque — e a ultima frase do mesmo bloco.
            lg = min(13.4, LG)
            h = altura(spec["fecho"], T_CORPO, lg) + 0.1
            self.texto(s, X, min(fundo + 0.52, FIM + 0.28 - h), lg,
                       spec["fecho"], T_CORPO, CORPO, LIGHT, h=h)
        self._fechar(s, spec)
        return s

    def pg_ficha(self, spec):
        """A prancha-resumo: rotulo pequeno e valor, em duas colunas.

        Cada coluna e uma pilha independente, e cada linha tem a altura do
        seu proprio texto — o posicionamento ocupa cinco linhas, a
        personalidade ocupa uma. Distribuir o espaco em partes iguais faz o
        filete seguinte atravessar o texto mais longo."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        campos = spec["campos"]
        colunas = spec.get("grade", 2)
        por_col = int(math.ceil(len(campos) / colunas))
        larg = (LG - 0.90 * (colunas - 1)) / colunas
        topo = max(y, 3.90)

        def alturas(bloco, tam):
            return [max(0.76, altura(v, tam, larg, 1.35) + 0.62)
                    for _, v in bloco]

        pilhas = [campos[c * por_col:(c + 1) * por_col]
                  for c in range(colunas)]
        disponivel = FIM + 0.35 - topo
        # o valor desce um degrau de corpo antes de a linha ser espremida:
        # encolher a caixa abaixo do texto nao encolhe o texto
        for tam_valor in (T_CORPO, T_MINI):
            alts = [alturas(b, tam_valor) for b in pilhas]
            maior = max((sum(a) for a in alts), default=0)
            if maior <= disponivel:
                break
        fator = min(1.0, disponivel / maior) if maior else 1.0
        for c, bloco in enumerate(pilhas):
            cx = X + c * (larg + 0.90)
            yy = topo
            for k, (rot, valor) in enumerate(bloco):
                h = alts[c][k] * fator
                self.fio(s, cx, yy, larg)
                self.rotulo(s, rot, cx, yy + 0.22, larg, ACENTO)
                self.texto(s, cx, yy + 0.54, larg, valor, tam_valor, TINTA,
                           LIGHT, h=h - 0.60)
                yy += h
        self._fechar(s, spec)
        return s

    def pg_alternativas(self, spec):
        """Em vez de / preferir — a troca de linguagem, lado a lado."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
        pares = spec["pares"]
        larg_e = 5.40
        larg_d = LG - larg_e - 1.10
        topo = max(y, 4.10)
        passo = min(1.85, (FIM + 0.30 - topo) / len(pares))
        for i, (evitar, preferir) in enumerate(pares):
            yy = topo + i * passo
            self.fio(s, X, yy, LG)
            self.rotulo(s, spec.get("rot_evitar", "Em vez de"), X, yy + 0.24,
                        larg_e, CLARO)
            self.texto(s, X, yy + 0.56, larg_e, "“%s”" % evitar, T_CORPO,
                       CLARO, LIGHT, italic=True, h=passo - 0.62)
            self.rotulo(s, spec.get("rot_preferir", "Preferir"),
                        X + larg_e + 1.10, yy + 0.24, larg_d, ACENTO)
            self.texto(s, X + larg_e + 1.10, yy + 0.56, larg_d,
                       "“%s”" % preferir, T_CORPO, TINTA, LIGHT,
                       h=passo - 0.62)
        self._fechar(s, spec)
        return s

    def pg_ikigai(self, spec):
        """Os quatro circulos — aneis de contorno, nunca preenchidos.

        Cada leitura tem a altura do seu proprio texto: dividir a coluna em
        quatro partes iguais faz a leitura mais longa invadir a seguinte."""
        s, y0, FIM = self._abrir(spec)
        X, LG = self._col
        self.cabeca(s, spec, x=X, w=LG, y=y0)
        cx, cy, d = 16.55, 2.95, 2.30
        desloc = d * 0.28
        for ddx, ddy in ((0, -desloc), (desloc, 0), (0, desloc), (-desloc, 0)):
            self.anel(s, cx + ddx, cy + ddy, d, FIO, esp=1.1)
        self.ponto(s, cx, cy, 0.13, ACENTO)
        larg = 13.6
        campos = spec["campos"]
        topo = 3.40
        reservado = 0.0
        if spec.get("centro"):
            reservado = 0.55 + altura(spec["centro"], T_MINI, larg, 1.35)
        espaco = FIM + 0.25 - topo - reservado
        # O corpo desce um degrau ANTES de a linha ser espremida: encolher a
        # caixa abaixo do que o texto ocupa nao encolhe o texto — faz o filete
        # da leitura seguinte passar por cima da ultima linha.
        for tam in (T_CORPO, T_MINI):
            alturas = [max(0.80, altura(desc, tam, larg, 1.45) + 0.52)
                       for _, desc in campos]
            if sum(alturas) <= espaco:
                break
        folga = espaco - sum(alturas)
        if folga > 0:
            alturas = [a + min(0.30, folga / len(campos)) for a in alturas]
        else:
            self.avisos.append(
                "ikigai nao cabe em \"%s\": sobram %.2f\" para cortar"
                % (spec.get("titulo", "?"), -folga))
        yy = topo
        for i, (rot, desc) in enumerate(campos):
            self.fio(s, X, yy, larg)
            self.rotulo(s, rot, X, yy + 0.22, larg, ACENTO)
            self.texto(s, X, yy + 0.54, larg, desc, tam, CORPO, LIGHT,
                       h=alturas[i] - 0.60)
            yy += alturas[i]
        if spec.get("centro"):
            self.fio(s, X, yy + 0.08, 1.30, ACENTO, esp=0.03)
            self.texto(s, X, yy + 0.34, larg, spec["centro"], T_MINI, CLARO,
                       SEMI, spc=1.4,
                       h=altura(spec["centro"], T_MINI, larg, 1.35) + 0.12)
        self._fechar(s, spec)
        return s

    def pg_manifesto(self, spec):
        """Texto longo em duas colunas, com muito ar. O manifesto."""
        s = self.slide()
        # o corpo comeca abaixo do titulo e do filete, nao num 3,30 fixo: com
        # titulo de uma linha o 3,30 caia EM CIMA do filete, e a primeira
        # linha da coluna da esquerda cobria a regua da pagina
        y = self.cabeca(s, spec)
        paragrafos = spec["paragrafos"]
        larg = (W - 1.10) / 2
        meio = int(math.ceil(len(paragrafos) / 2))
        topo = max(3.30, y + 0.10)
        reservado = 0.75 if spec.get("assinatura") else 0.0
        espaco = FUNDO + 0.25 - topo - reservado
        colunas = (paragrafos[:meio], paragrafos[meio:])
        for tam_par in (T_LEAD, T_CORPO):
            altos = [sum(altura(p, tam_par, larg, 1.45) + 0.40 for p in b)
                     for b in colunas]
            if max(altos) <= espaco:
                break
        fundo = topo
        for c, bloco in enumerate(colunas):
            cx = ML + c * (larg + 1.10)
            yy = topo
            for par in bloco:
                h = altura(par, tam_par, larg, 1.45) + 0.10
                self.texto(s, cx, yy, larg, par, tam_par, TINTA, LIGHT,
                           espaco=1.45, h=h)
                yy += h + 0.30
            fundo = max(fundo, yy)
        if spec.get("assinatura"):
            # a assinatura segue a coluna mais alta, nunca uma altura fixa
            base = min(fundo + 0.12, FUNDO - 0.05)
            self.fio(s, ML, base - 0.30, 1.30, ACENTO, esp=0.03)
            self.texto(s, ML, base, W, spec["assinatura"], T_MINI, CLARO,
                       SANS, spc=2.2, h=0.35)
        self.rodape(s)
        return s

    def pg_sumario(self, spec):
        """Indice. Ate oito temas cabem numa coluna; acima disso vai para
        duas, senao o filete de um item corta o nome do seguinte."""
        s = self.slide()
        # O titulo do sumario fica ACIMA do painel, em Ultra-Bold, como no
        # arquivo final da Kelly. Ele tem UMA linha de espaco: em duas, o
        # texto transborda a caixa e cai por cima do primeiro item. Por isso
        # o corpo cede ate caber — e so o titulo do sumario cede assim,
        # porque aqui a alternativa e a colisao.
        titulo_s = spec.get("titulo", "Sumário").upper()
        tam_s = T_SUMARIO
        while tam_s > 46 and largura_texto(titulo_s, tam_s) > 15.4:
            tam_s -= 2
        self.texto(s, 1.82, 0.88 + (T_SUMARIO - tam_s) / 150.0, 15.6,
                   titulo_s, tam_s, TINTA, ULTRA, espaco=1.0,
                   h=tam_s / 60.0)
        itens = spec["itens"]
        colunas = spec.get("grade", 1 if len(itens) <= 8 else 2)
        por_col = int(math.ceil(len(itens) / colunas))
        larg = (W - 0.90) / colunas if colunas > 1 else W
        topo = 2.95
        passo = (FUNDO + 0.30 - topo) / por_col
        # com a escala medida o nome vem a 23pt e a descricao a 15pt: sem
        # folga suficiente o filete seguinte corta os descendentes
        tam_nome = 25 if passo >= 1.00 else T_LEAD
        for i, item in enumerate(itens):
            num, nome = item[0], item[1]
            desc = item[2] if len(item) > 2 else None
            c, r = i // por_col, i % por_col
            x = ML + c * (larg + 0.90)
            y = topo + r * passo
            self.fio(s, x, y, larg)
            self.texto(s, x, y + 0.28, 1.1, num, 15.5, ACENTO, SEMI,
                       spc=2.4, h=0.32)
            h_nome = tam_nome / 72.0 * 1.42
            self.texto(s, x + 1.75, y + 0.16, larg - 1.75, nome, tam_nome,
                       TINTA, LIGHT, h=h_nome)
            if desc:
                self.texto(s, x + 1.75, y + 0.16 + h_nome, larg - 1.75, desc,
                           18, CLARO, LIGHT, h=18 / 72.0 * 1.5)
        for c in range(colunas):
            x = ML + c * (larg + 0.90)
            n = min(por_col, len(itens) - c * por_col)
            self.fio(s, x, topo + n * passo, larg)
        self.rodape(s)
        return s

    def pg_divisor(self, spec):
        """A virada de tema, no formato que a Kelly diagramou: o nome da
        secao GIGANTE em Bold, alinhado a direita, e a linha de apoio logo
        abaixo, no mesmo eixo. Sem painel — a textura corre de borda a borda.

        O nome cede corpo ate caber na largura: 143,5pt e o teto, nao uma
        obrigacao, e "CULTURA ORGANIZACIONAL" nao cabe em 143,5pt nenhum.

        Com `foto`, a mesma composicao entra em branco sobre a imagem."""
        caminho = self.arquivo(spec.get("foto"))
        cheia = bool(spec.get("foto"))
        s = self.slide(painel=False)
        if cheia:
            if caminho:
                foco, _ = self._enquadrar(caminho, LARG, ALT,
                                          spec.get("foco", 0.5))
                self.foto(s, 0, 0, LARG, ALT, caminho, foco=foco)
                self.veu(s, 0, 0, LARG, ALT, TINTA, spec.get("veu", 0.52))
            else:
                self.bloco(s, 0, 0, LARG, ALT, MARCA_ESCURO)
            cor_nome = BRANCO
            cor_apoio = BRANCO
            cor_num = MARCA_ACENTO_ESCURO if not caminho else ACENTO
        else:
            cor_nome, cor_apoio, cor_num = TINTA, TINTA, ACENTO

        DIR = 18.875          # a borda direita, medida no arquivo dela
        larg = DIR - ML
        nome = spec["nome"].upper()
        tam = spec.get("tam_nome", T_DIVISOR)
        while tam > 46 and largura_texto(nome, tam, FONTE_BOLD) > larg:
            tam -= 2.5
        alt_nome = tam / 72.0 * 1.10

        apoio = spec.get("apoio")
        tam_ap = spec.get("tam_apoio", T_DIV_APOIO)
        n_ap = 0
        if apoio:
            while tam_ap > 24 and largura_texto(apoio, tam_ap) > larg:
                tam_ap -= 2
            n_ap = linhas(apoio, tam_ap, larg)
        alt_ap = n_ap * tam_ap / 72.0 * 1.16 if apoio else 0.0

        # o bloco inteiro centrado na altura da pagina
        bloco = alt_nome + (0.28 + alt_ap if apoio else 0.0)
        y = (ALT - bloco) / 2.0 - 0.25
        if spec.get("numero"):
            self.texto(s, ML, y - 0.52, larg, spec["numero"], T_ROTULO,
                       cor_num, SEMI, spc=3.0, align=PP_ALIGN.RIGHT, h=0.32)
        self.texto(s, ML, y, larg, nome, tam, cor_nome, BOLD, espaco=1.10,
                   align=PP_ALIGN.RIGHT, h=alt_nome + 0.20)
        fim = y + alt_nome
        if apoio:
            self.texto(s, ML, fim + 0.28, larg, apoio, tam_ap, cor_apoio,
                       LIGHT, espaco=1.16, align=PP_ALIGN.RIGHT,
                       h=alt_ap + 0.15)
            fim = fim + 0.28 + alt_ap
        if cheia and not caminho:
            self.marcacao(s, 0, 0, LARG, ALT, spec, escuro=True, baixo=True,
                          piso=fim + 0.40, fundo=False)
        self.rodape(s, sobre_foto=cheia)
        return s

    def pg_capa(self, spec):
        """Capa no formato do arquivo final da Kelly — medida nele, nao
        estimada.

        A capa nao leva painel: a textura corre de borda a borda e o texto
        assenta direto sobre ela. O titulo entra em 75pt, o subtitulo tem o
        nome em Bold e o resto em regular, e a barra de assinatura embaixo e
        quatro filetes separando logo, metodo e data.

        `foto` so entra se for pedida explicitamente — a capa dela nao tem.
        """
        s = self.slide(painel=False)
        caminho = self.arquivo(spec.get("foto"))
        corte = spec.get("corte", 7.60) if caminho else 0.0
        if caminho:
            foco, _ = self._enquadrar(caminho, corte, ALT,
                                      spec.get("foco", 0.5))
            self.foto(s, LARG - corte, 0, corte, ALT, caminho, foco=foco)
        if TRACO and not caminho:
            self.logo(s, TRACO, 16.17, 3.68, 1.63)

        x = 1.68
        # a caixa do titulo para antes do traco, no canto superior direito
        larg = (LARG - corte - x - 1.10) if caminho else 14.82
        titulo = spec["titulo"]
        if isinstance(titulo, str):
            titulo = [titulo]
        tam = spec.get("tam_titulo", T_CAPA)
        n = len(titulo)
        # No arquivo dela o titulo da capa e Outfit 1 Medium com negrito
        # sintetico por cima. Aqui o peso vem da Bold, que e a mesma cor de
        # traco sem engrossar as curvas — e os 3pt de espacejamento, que sao
        # o que da o ar da capa, ficam.
        self.texto(s, x, 3.93, larg, titulo, tam, TINTA, BOLD, espaco=1.14,
                   spc=3.0, h=n * tam / 72.0 * 1.30)

        # subtitulo: o nome em Bold, a descricao em regular, na mesma linha
        y = 3.93 + n * tam / 72.0 * 1.30 + 0.12
        sub = spec["subtitulo"]
        if isinstance(sub, str):
            sub = [sub]
        tf = self.caixa(s, x, y, larg, 0.55)
        p = self.par(tf, primeiro=True, espaco=1.2)
        self.txt(p, sub[0], T_SUBCAPA, TINTA, BOLD)
        if len(sub) > 1:
            self.txt(p, "  |  " + "  |  ".join(sub[1:]), T_SUBCAPA, TINTA, REG)

        # barra de assinatura: quatro filetes, logo, metodo e data
        for fx in (1.69, 5.21, 8.19, 10.60):
            self.fio_v(s, fx, 8.52, 0.98, CLARO, esp=0.012)
        # a marca mede 3,11" de tinta comecando em 8,65", como no arquivo
        # dela. A tela do PNG e quadrada e a tinta ocupa so a faixa do meio,
        # entao a conta e feita pela tinta — ancorar pelo topo da tela joga a
        # marca 1,5" abaixo da barra.
        TINTA_TOPO, TINTA_ESQ, TINTA_LARG = 0.409, 0.081, 0.822
        tela = 3.11 / TINTA_LARG
        self.logo(s, LOGO_KA, 1.90 - TINTA_ESQ * tela,
                  8.65 - TINTA_TOPO * tela, tela)
        assin = spec["assinatura"]
        if isinstance(assin, str):
            assin = [assin]
        tf = self.caixa(s, 5.45, 8.71, 2.60, 0.80)
        for i, linha in enumerate(assin):
            p = self.par(tf, primeiro=(i == 0), espaco=0.95)
            # "Metodo" leve, o nome do metodo em semibold — como no arquivo
            # dela, onde o peso marca o nome e nao a palavra de servico
            marca = linha.endswith("©")
            if marca:
                linha = linha[:-1].rstrip()
            if i == 0 and " " in linha:
                servico, nome = linha.split(" ", 1)
                self.txt(p, servico + " ", T_ASSINATURA, TINTA, SANS_LIGHT)
                self.txt(p, nome, T_ASSINATURA, TINTA, SANS_SEMI)
            else:
                self.txt(p, linha, T_ASSINATURA, TINTA, SANS_SEMI)
            # o © entra miudo, como no arquivo dela: no corpo da assinatura
            # ele vira um caractere do tamanho de uma palavra
            if marca:
                self.txt(p, "©", 14.7, TINTA, SANS)
        self.texto(s, 8.25, 8.92, 2.30, spec["data"].upper(), T_DATA, TINTA,
                   REG, align=PP_ALIGN.CENTER, h=0.40)
        return s

    # ---------------------------------------------------------------- montagem
    TIPOS = {
        "abertura": None, "fecho": None,
        "capa": "pg_capa", "sumario": "pg_sumario", "divisor": "pg_divisor",
        "declaracao": "pg_declaracao", "texto": "pg_texto",
        "colunas": "pg_colunas", "palavras": "pg_palavras",
        "fluxo": "pg_fluxo", "contraste": "pg_contraste",
        "camadas": "pg_camadas", "lista": "pg_lista", "ficha": "pg_ficha",
        "alternativas": "pg_alternativas", "ikigai": "pg_ikigai",
        "manifesto": "pg_manifesto", "foto": "pg_foto",
        "foto_cheia": "pg_foto_cheia",
    }

    # Paginas cuja posicao e desenhada a mao e nao deve ser recentrada: a
    # capa tem a barra de assinatura presa embaixo, a abertura e o fecho sao
    # composicao de logos, e o sumario nasce preenchendo o painel inteiro.
    SEM_CENTRAR = ("capa", "abertura", "fecho", "sumario",
                   "divisor", "foto_cheia")

    def centrar(self, s, tipo):
        """Centra verticalmente o bloco de conteudo da pagina.

        O motor monta de cima para baixo a partir de uma linha fixa, e numa
        pagina de pouco texto — que e o caso agora, com uma ideia por pagina —
        o conteudo fica colado no cabecalho e o pe sobra vazio. Aqui o bloco
        inteiro desce (ou sobe) de uma vez, para o olho encontrar o texto no
        meio da pagina.

        Fotografia, painel, veu e textura nao se mexem: so o texto e os
        filetes que o acompanham."""
        if tipo in self.SEM_CENTRAR:
            return
        moveis, painel = [], False
        for sh in s.shapes:
            larg = sh.width / float(EMU)
            alt = sh.height / float(EMU)
            if larg >= 17.0 and 8.4 <= alt <= 9.6:
                painel = True
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                continue
            # painel, faixa de fotografia, veu e fundo ficam onde estao
            if larg >= 17.0 or alt >= 8.0:
                continue
            # o rotulo da marcacao pertence a area da imagem, nao ao texto
            cx = (sh.left + sh.width / 2.0) / float(EMU)
            cy = (sh.top + sh.height / 2.0) / float(EMU)
            if any(ax <= cx <= ax + aw and ay <= cy <= ay + ah
                   for ax, ay, aw, ah in self._areas):
                continue
            moveis.append(sh)
        if not moveis:
            return
        topo = min(sh.top for sh in moveis) / float(EMU)
        base = max(sh.top + sh.height for sh in moveis) / float(EMU)
        if painel:
            limite_alto, limite_baixo, meio = 1.62, 9.30, 5.35
        else:
            limite_alto, limite_baixo, meio = 1.10, 10.15, 5.50
        delta = meio - (topo + base) / 2.0
        delta = min(delta, limite_baixo - base)
        delta = max(delta, limite_alto - topo)
        if abs(delta) < 0.02:
            return
        for sh in moveis:
            sh.top = sh.top + self.e(delta)

    def montar(self, paginas):
        for i, spec in enumerate(paginas, 1):
            self._areas = []
            tipo = spec["tipo"]
            if tipo not in self.TIPOS:
                raise ValueError("pagina %d: tipo desconhecido %r" % (i, tipo))
            if tipo == "abertura":
                self.abertura()
            elif tipo == "fecho":
                self.fecho(spec.get("frase", "MUITO OBRIGADA!"))
            else:
                getattr(self, self.TIPOS[tipo])(spec)
            self.centrar(self.prs.slides[-1], tipo)
        return self
