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

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN  # noqa: E402
from pptx.oxml.ns import qn  # noqa: E402
from pptx.oxml.xmlchemy import OxmlElement  # noqa: E402

from rostos import foco as foco_cabeca  # noqa: E402
from ka_layout import (  # noqa: E402
    ACENTO, BRANCO, CLARO, CORPO, FIO, PAINEL, TINTA,
    BOLD, LIGHT, SANS, SANS_LIGHT, SANS_SEMI, SEMI,
    T_CAPA, T_CORPO, T_DISPLAY, T_DIVISOR, T_FRASE, T_H1, T_LEAD, T_MEDIO,
    T_MINI, T_RODAPE, T_ROTULO, T_SUMARIO, T_SUBCAPA, T_ASSINATURA,
    T_DATA, MEDIO, REG, ULTRA,
    ALT, LARG, ML, MR, W, Y_EYE, Y_H1, Y_RODAPE,
    LOGO_KA, SIMBOLO_IKIGAI, TRACO,
    Deck,
)

# ------------------------------------------------------------------ medidas
TOPO = 2.00          # primeira linha util dentro do painel
FUNDO = 9.15         # ultima caixa de texto comeca aqui, no maximo
COL, GAP = 3.35, 0.55

# Largura media de caractere, em polegadas por ponto de corpo. So entra em
# cena se a Outfit nao estiver em padrao-ka/fontes/ — contar caractere trata
# "iii" e "MMM" como a mesma coisa e erra ate 15%.
CHAR = 0.0103

# A fonte com que o texto e medido. E a Light porque e a mais estreita da
# familia: medir por ela e errar sempre para o lado seguro.
FONTE_MEDIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fontes", "Outfit1Light.ttf")
FOLGA = 1.03         # o LibreOffice e o PowerPoint quebram um fio antes
_FONTES = {}


def _fonte(tam):
    chave = round(tam, 1)
    if chave not in _FONTES:
        from PIL import ImageFont
        _FONTES[chave] = ImageFont.truetype(FONTE_MEDIDA, int(round(tam * 4)))
    return _FONTES[chave]


def largura_texto(texto, tam):
    """Largura real do texto, em polegadas, medida na propria fonte."""
    return _fonte(tam).getlength(texto) / 4.0 / 72.0 * FOLGA


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
ENTRELINHA = 1.24


def altura(texto, tam, largura, espaco=1.4):
    return linhas(texto, tam, largura) * tam / 72.0 * espaco * ENTRELINHA


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
            self.texto(s, x, y - 0.60, w, spec["eyebrow"].upper(), T_ROTULO,
                       cor_eye, SANS, spc=3.0, h=0.32)
        titulo = spec.get("titulo")
        if not titulo:
            return y
        # Titulo de pagina em CAIXA ALTA. Caixa alta ocupa cerca de 10% mais
        # largura que caixa baixa, entao a conta de linhas usa o texto ja
        # convertido — senao o titulo quebra onde o calculo nao previu.
        titulo = (titulo.upper() if isinstance(titulo, str)
                  else [l.upper() for l in titulo])
        tam = spec.get("tam_titulo", T_H1)
        n = linhas(titulo, tam, w) if isinstance(titulo, str) else len(titulo)
        self.titulo(s, titulo, x, y, w, tam, cor)
        fim = y + n * tam / 72.0 * 1.14 + 0.34
        self.fio(s, x, fim, w, FIO if cor is TINTA else CLARO)
        return fim + 0.42

    def corpo(self, s, spec, x, y, w, fim=FUNDO, cor=CORPO, cor_forte=TINTA):
        """Lead, paragrafos, itens e destaque — o miolo comum a varias
        paginas.

        Mede tudo antes de desenhar. Numa pagina com faixa de fotografia
        sobra pouco mais de um terco da altura, e o mesmo texto que respira
        na pagina inteira estoura ali. Quando nao cabe, o metodo aperta
        primeiro os intervalos e so depois reduz o corpo — nunca deixa
        vazar."""
        tam_lead, tam_corpo = T_LEAD, T_CORPO
        tam_dest = spec.get("tam_destaque", T_MEDIO)
        gap_lead, gap_par, gap_item, gap_dest = 0.30, 0.26, 0.08, 0.48

        def medir(k):
            total, blocos = 0.0, []
            if spec.get("lead"):
                h = altura(spec["lead"], tam_lead * k, w) + 0.12
                blocos.append(("lead", h)); total += h + gap_lead * k
            for par in spec.get("paragrafos", []):
                h = altura(par, tam_corpo * k, w) + 0.10
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
                self.texto(s, x, y, w, b[2], tam_corpo * k, cor, LIGHT, h=b[1])
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
        caminho = self.arquivo(spec.get("foto"))
        if not caminho:
            return self.slide(), Y_H1, FUNDO
        lado = spec.get("lado", "direita")
        nome = os.path.basename(caminho)
        iw, ih = Image.open(caminho).size

        # Retrato nunca entra em faixa horizontal: o corte sobraria um sexto
        # da altura, so a testa.
        if lado in ("cima", "baixo") and iw / ih < 1.15:
            lado = "direita"

        # A faixa horizontal corta a imagem na VERTICAL, e e ai que a cabeca
        # se perde. Se a faixa que o texto permite nao comporta a cabeca
        # inteira, a pagina vira tira vertical — cortar o rosto nao e uma
        # opcao, e a tira corta na horizontal, onde sobra folga de sobra.
        if lado in ("cima", "baixo"):
            pedida = min(self._fatia(spec), self.FAIXA_MAX)
            if not self._faixa_cabe(caminho, pedida):
                precisa = pedida
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

        if lado in ("direita", "esquerda"):
            # a tira cresce ate a cabeca caber, dentro de um limite
            v = max(self.FATIA_V_MIN, spec.get("fatia_v", self.FATIA_V_MIN))
            while v < self.FATIA_V_MAX and \
                    not self._enquadrar(caminho, LARG * v, ALT)[1]:
                v += 0.01
            foco, cabe = self._enquadrar(caminho, LARG * v, ALT,
                                         spec.get("foco", 0.5))
            if not cabe:
                self.avisos.append("%s: cabeca nao cabe nem na tira" % nome)
            corte = LARG * v
            if lado == "direita":
                self.bloco(s, 0, 0, LARG - corte, ALT, PAINEL)
                self.foto(s, LARG - corte, 0, corte, ALT, caminho, foco=foco)
                self._col = (ML, LARG - corte - ML - 0.95)
            else:
                self.foto(s, 0, 0, corte, ALT, caminho, foco=foco)
                self.bloco(s, corte, 0, LARG - corte, ALT, PAINEL)
                self._col = (corte + 0.95, LARG - corte - 1.90)
            return s, Y_H1, FUNDO

        self._col = (ML, W)
        h_foto = ALT * min(spec.get("fatia", 0.42), self.FAIXA_MAX)
        foco, cabe = self._enquadrar(caminho, LARG, h_foto,
                                     spec.get("foco", 0.16))
        if not cabe:
            self.avisos.append("%s: cabeca cortada na faixa" % nome)
        if lado == "cima":
            self.foto(s, 0, 0, LARG, h_foto, caminho, foco=foco)
            self.bloco(s, 0, h_foto, LARG, ALT - h_foto, PAINEL)
            return s, h_foto + 0.95, FUNDO
        self.bloco(s, 0, 0, LARG, ALT - h_foto, PAINEL)
        self.foto(s, 0, ALT - h_foto, LARG, h_foto, caminho, foco=foco)
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
        """Fotografia em tela cheia com veu; texto branco por cima."""
        s = self.slide(painel=False)
        caminho = self.arquivo(spec.get("foto"))
        if caminho:
            foco, _ = self._enquadrar(caminho, LARG, ALT, spec.get("foco", 0.5))
            self.foto(s, 0, 0, LARG, ALT, caminho, foco=foco)
        self.veu(s, 0, 0, LARG, ALT, TINTA, spec.get("veu", 0.58))
        linhas_ = spec.get("linhas") or [spec.get("titulo", "")]
        tam = spec.get("tam") or self._tam_display(linhas_, 15.4)
        # a frase sai com entrelinha 1,26 e a fonte ainda tem a sua propria
        # altura de linha: sem ENTRELINHA o bloco mede 20% a menos do que
        # ocupa, e o filete de acento acaba por cima da segunda linha
        alt_bloco = len(linhas_) * tam / 72.0 * 1.26 * ENTRELINHA
        y = (ALT - alt_bloco) / 2 - 0.30
        if spec.get("eyebrow"):
            self.texto(s, ML, y - 0.85, W, spec["eyebrow"].upper(), T_ROTULO,
                       BRANCO, SANS, spc=3.0, h=0.32)
        self.texto(s, ML, y, 15.4, linhas_, tam, BRANCO, LIGHT, espaco=1.26,
                   h=alt_bloco + 0.30)
        y += alt_bloco + 0.34
        if spec.get("apoio"):
            self.fio(s, ML, y, 1.30, ACENTO, esp=0.03)
            self.texto(s, ML, y + 0.34, 13.0, spec["apoio"], T_CORPO, BRANCO,
                       LIGHT, h=altura(spec["apoio"], T_CORPO, 13.0) + 0.1)
        self.rodape(s, sobre_foto=True)
        return s

    # ---------------------------------------------------- paginas tipograficas
    def _tam_display(self, linhas_, largura, teto=T_DISPLAY, piso=30):
        """Corpo que faz as quebras do autor valerem.

        Numa pagina de frase as linhas sao escritas a mao: cada uma e uma
        unidade de sentido. Se o corpo for grande demais para a largura, a
        linha quebra sozinha no meio e a intencao se perde — por isso o
        tamanho sai da linha mais longa, nao de uma tabela."""
        maior = max((len(l) for l in linhas_), default=1)
        return max(piso, min(teto, largura / (CHAR * max(maior, 1))))

    def pg_declaracao(self, spec):
        """A pagina de silencio: uma frase grande e muito ar."""
        s = self.slide()
        linhas_ = spec.get("linhas", [])
        tam = spec.get("tam") or self._tam_display(linhas_, 15.4)
        # a frase sai com entrelinha 1,26 e a fonte ainda tem a sua propria
        # altura de linha: sem ENTRELINHA o bloco mede 20% a menos do que
        # ocupa, e o filete de acento acaba por cima da segunda linha
        alt_bloco = len(linhas_) * tam / 72.0 * 1.26 * ENTRELINHA
        extra = 0.0
        if spec.get("apoio"):
            extra = 0.90 + altura(spec["apoio"], T_CORPO, 13.0)
        y = (9.60 + 1.10 - alt_bloco - extra) / 2
        if spec.get("eyebrow"):
            self.texto(s, ML, y - 0.90, W, spec["eyebrow"].upper(), T_ROTULO,
                       ACENTO if spec.get("marcar") else CLARO, SEMI if
                       spec.get("marcar") else SANS, spc=3.0, h=0.32)
        self.fio(s, ML, y - 0.46, 1.30, ACENTO, esp=0.03)
        self.texto(s, ML, y, 15.4, linhas_, tam, TINTA, LIGHT, espaco=1.26,
                   h=alt_bloco + 0.30)
        if spec.get("apoio"):
            self.texto(s, ML, y + alt_bloco + 0.55, 13.0, spec["apoio"],
                       T_CORPO, CORPO, LIGHT,
                       h=altura(spec["apoio"], T_CORPO, 13.0) + 0.1)
        self.rodape(s)
        return s

    def pg_texto(self, spec):
        s, y0, fim = self._abrir(spec)
        X, LG = self._col
        y = self.cabeca(s, spec, x=X, w=LG, y=y0)
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
            self.fio(s, cx, y, larg)
            self.texto(s, cx, y + 0.28, larg, rot, T_MEDIO, TINTA, LIGHT,
                       h=altura(rot, T_MEDIO, larg, 1.2) + 0.1)
            dy = y + 0.30 + altura(rot, T_MEDIO, larg, 1.2) + 0.26
            h = altura(desc, T_CORPO, larg) + 0.1
            self.texto(s, cx, dy, larg, desc, T_CORPO, CORPO, LIGHT, h=h)
            fundo = max(fundo, dy + h)
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
            self.texto(s, X, min(fundo + 0.30, FIM), LG, spec["fecho"],
                       T_MINI, CLARO, LIGHT, align=PP_ALIGN.CENTER, h=0.4)
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
        topo = max(y, 5.00)
        fundo = topo
        for i, (rot, itens) in enumerate([spec["esquerda"], spec["direita"]]):
            cx = X + i * (larg + 1.70)
            self.fio(s, cx, topo, larg, ACENTO if i == 0 else FIO,
                     esp=0.03 if i == 0 else 0.012)
            self.rotulo(s, rot, cx, topo + 0.30, larg,
                        ACENTO if i == 0 else CLARO)
            yy = topo + 0.72
            # a coluna mais longa manda no corpo: duas listas de tamanhos
            # diferentes precisam terminar dentro da mesma pagina
            n_max = max(len(spec["esquerda"][1]), len(spec["direita"][1]))
            tam = T_LEAD if (FIM - topo - 0.80) / max(1, n_max) >= 0.52 \
                else T_CORPO
            gap = 0.22 if tam == T_LEAD else 0.14
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
        topo = max(y, 4.20)
        larg = LG - min(5.60, LG * 0.40)
        # Cada degrau tem a altura do seu proprio texto. Dividir o espaco em
        # partes iguais estoura a pagina quando uma das leituras e longa.
        # Quando nao cabe, o corpo desce um degrau ANTES de a linha ser
        # espremida: encolher a caixa abaixo do que o texto ocupa nao faz o
        # texto encolher — faz ele invadir a linha de baixo.
        espaco = FIM + 0.30 - topo
        escala = [T_LEAD, T_CORPO, T_MINI] if larg >= 7.0 else [T_CORPO, T_MINI]
        for tam_desc in escala:
            alturas = [max(0.72, altura(desc, tam_desc, larg, 1.35) + 0.44)
                       for _, desc in itens]
            if sum(alturas) <= espaco:
                break
        folga = espaco - sum(alturas)
        if folga > 0:
            alturas = [a + min(0.42, folga / len(itens)) for a in alturas]
        yy = topo
        for i, (rot, desc) in enumerate(itens):
            ultimo = i == len(itens) - 1
            self.fio(s, X, yy, LG)
            self.rotulo(s, rot, X, yy + 0.26, min(5.20, LG * 0.37),
                        ACENTO if ultimo else CLARO)
            self.texto(s, X + min(5.60, LG * 0.40), yy + 0.18, larg, desc,
                       tam_desc, TINTA, LIGHT, h=alturas[i] - 0.26)
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
            alturas = [max(0.46, altura(i, tam, largura - 0.48, 1.38) + 0.06)
                       for i in itens]
            pior = max(sum(alturas[c * por_col:(c + 1) * por_col])
                       for c in range(colunas))
            return alturas, pior

        for tam in (T_LEAD, T_CORPO, T_MINI):
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
                self.ponto(s, cx + 0.05, yy + 0.16, 0.085,
                           ACENTO if i == len(itens) - 1 and
                           spec.get("marcar_ultimo") else CLARO)
                self.texto(s, cx + 0.48, yy, largura - 0.48, item, tam, TINTA,
                           LIGHT, h=alturas[i])
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
        self.cabeca(s, spec)
        paragrafos = spec["paragrafos"]
        larg = (W - 1.10) / 2
        meio = int(math.ceil(len(paragrafos) / 2))
        topo = 3.30
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
        s = self.slide()
        # o titulo do sumario fica ACIMA do painel, em Ultra-Bold, como no
        # arquivo final da Kelly
        self.texto(s, 1.82, 0.88, 12.0, spec.get("titulo", "Sumário").upper(),
                   T_SUMARIO, TINTA, ULTRA, espaco=1.0, h=T_SUMARIO / 60.0)
        itens = spec["itens"]
        com_desc = any(len(i) > 2 for i in itens)
        topo = 2.95
        passo = (FUNDO + 0.30 - topo) / len(itens)
        # com a escala medida o nome vem a 23pt e a descricao a 15pt: sem
        # folga suficiente o filete seguinte corta os descendentes
        tam_nome = 25 if passo >= 1.00 else T_LEAD
        for i, item in enumerate(itens):
            num, nome = item[0], item[1]
            desc = item[2] if len(item) > 2 else None
            y = topo + i * passo
            self.fio(s, ML, y, W)
            self.texto(s, ML, y + 0.28, 1.1, num, 15.5, ACENTO, SEMI,
                       spc=2.4, h=0.32)
            h_nome = tam_nome / 72.0 * 1.42
            self.texto(s, ML + 1.75, y + 0.16, W - 1.75, nome, tam_nome,
                       TINTA, LIGHT, h=h_nome)
            if desc:
                self.texto(s, ML + 1.75, y + 0.16 + h_nome, W - 1.75, desc,
                           18, CLARO, LIGHT, h=18 / 72.0 * 1.5)
        self.fio(s, ML, topo + len(itens) * passo, W)
        self.rodape(s)
        return s

    def pg_divisor(self, spec):
        s = self.slide()
        self.texto(s, ML, 4.20, 4.0, spec["numero"], T_ROTULO, ACENTO, SEMI,
                   spc=3.0, h=0.3)
        nome = spec["nome"].upper()
        tam = T_DIVISOR if len(nome) <= 16 else 68
        self.texto(s, ML, 4.80, 14.0, nome, tam, TINTA, LIGHT, espaco=1.0,
                   h=tam / 72.0 * 1.3)
        self.fio(s, ML, 6.95, W)
        if spec.get("apoio"):
            self.texto(s, ML, 7.25, 13.0, spec["apoio"], T_CORPO, CLARO,
                       LIGHT, h=altura(spec["apoio"], T_CORPO, 13.0) + 0.1)
        self.rodape(s)
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

    def montar(self, paginas):
        for i, spec in enumerate(paginas, 1):
            tipo = spec["tipo"]
            if tipo not in self.TIPOS:
                raise ValueError("pagina %d: tipo desconhecido %r" % (i, tipo))
            if tipo == "abertura":
                self.abertura()
            elif tipo == "fecho":
                self.fecho(spec.get("frase", "MUITO OBRIGADA!"))
            else:
                getattr(self, self.TIPOS[tipo])(spec)
        return self
