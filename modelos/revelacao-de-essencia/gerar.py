#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MODELO — REVELAÇÃO DE ESSÊNCIA
KA · Inteligencia para Marcas · Metodo Marca com Essencia ©

Monta a apresentacao de Revelacao de Essencia de qualquer cliente, no padrao
visual KA. O roteiro (as seis secoes e os arquetipos de cada pagina) esta
aqui; o conteudo vem de um modulo separado, por cliente.

    python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin

O diretorio do cliente precisa conter um `conteudo.py` seguindo a estrutura
documentada em modelos/revelacao-de-essencia/MODELO.md, e uma pasta
`assets/` com as fotos.
"""
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "padrao-ka"))

from ka_layout import (  # noqa: E402
    Deck, ACENTO, CLARO, CORPO, TINTA, LIGHT, REG, SEMI, SANS,
    T_CORPO, T_FRASE, T_LEAD, T_MEDIO, T_MINI, T_DISPLAY, T_ROTULO, ML, W,
    SIMBOLO_IKIGAI,
)
from pptx.enum.text import PP_ALIGN  # noqa: E402

COL, GAP = 3.35, 0.55          # grade de quatro colunas
LADO = ("direita", "esquerda")  # a foto alterna de lado a cada aparicao


def carregar(pasta):
    caminho = os.path.join(pasta, "conteudo.py")
    if not os.path.exists(caminho):
        sys.exit("Falta o arquivo %s" % caminho)
    spec = importlib.util.spec_from_file_location("conteudo", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def montar(C, pasta):
    fotos = os.path.join(pasta, "assets")
    def foto(nome):
        p = os.path.join(fotos, nome + ".jpg")
        return p if os.path.exists(p) else None

    d = Deck(documento="Revelação de Essência", marca=C.MARCA)
    lado = [0]

    def alterna():
        lado[0] += 1
        return LADO[lado[0] % 2]

    # 01 — abertura com as assinaturas
    d.abertura()

    # 02 — capa
    d.capa([C.TITULO_1, C.TITULO_2], C.SUBTITULO, C.ASSINATURA, C.DATA)

    # 03 — sumario
    s = d.slide()
    d.eyebrow(s, "Sumário")
    d.titulo(s, "Sumário", ML, 2.45, W, 44)
    for i, (num, nome, desc) in enumerate(C.SECOES):
        y = 3.55 + i * 0.95
        d.fio(s, ML, y, 13.4)
        d.texto(s, ML, y + 0.34, 1.0, num, T_MINI, ACENTO, SEMI, spc=2.4, h=0.28)
        d.texto(s, ML + 1.55, y + 0.22, 11.6, nome, T_MEDIO, TINTA, LIGHT, h=0.42)
        d.texto(s, ML + 1.55, y + 0.60, 11.6, desc, T_CORPO, CLARO, LIGHT, h=0.30)
    d.fio(s, ML, 3.55 + len(C.SECOES) * 0.95, 13.4)
    d.rodape(s)

    # 04 — por que começamos pela essência
    s, x, lg = d.com_foto("Conceito", C.PORQUE["titulo"],
                          foto("04-metodo"), alterna())
    d.texto(s, x, 4.40, lg, C.PORQUE["lead"], T_LEAD, TINTA, LIGHT, h=1.2)
    d.texto(s, x, 5.75, lg, C.PORQUE["corpo"], T_CORPO, CORPO, LIGHT, h=1.6)
    d.fio(s, x, 7.50, lg)
    d.rotulo(s, "O que não é", x, 7.78, lg)
    d.texto(s, x, 8.08, lg, C.PORQUE["nao_e"], T_CORPO, CORPO, LIGHT, h=0.6)
    d.rotulo(s, "O que é", x, 8.78, lg)
    d.texto(s, x, 9.08, lg, C.PORQUE["e"], T_CORPO, TINTA, LIGHT, h=0.6)

    # 05 — a pergunta que conduz a etapa
    s, x, lg = d.com_foto("A pergunta que conduz esta etapa", "",
                          foto("05-pergunta"), alterna())
    d.texto(s, x, 4.30, lg, C.PERGUNTA, T_DISPLAY * 0.78, TINTA, LIGHT,
            espaco=1.26)

    # 06 — como chegamos à revelação
    s = d.pagina("Método", C.METODO["titulo"])
    d.texto(s, ML, 4.25, 14.0, C.METODO["lead"], T_CORPO, CORPO, LIGHT, h=1.1)
    for i, (nome, desc) in enumerate(C.METODO["dimensoes"]):
        cx = ML + i * (COL + GAP)
        d.fio(s, cx, 5.60, COL)
        d.texto(s, cx, 5.88, COL, nome, T_MEDIO, TINTA, LIGHT, h=0.5)
        d.texto(s, cx, 6.48, COL, desc, T_CORPO, CORPO, LIGHT, h=2.0)
    tf = d.caixa(s, ML, 8.40, W, 0.55)
    p = d.par(tf, True, align=PP_ALIGN.CENTER)
    for i, palavra in enumerate(C.METODO["equacao"]):
        if i:
            d.txt(p, "  +  ", T_MEDIO, ACENTO, LIGHT)
        d.txt(p, palavra, T_MEDIO, CORPO, LIGHT)
    d.txt(p, "  =  ", T_MEDIO, ACENTO, LIGHT)
    d.txt(p, "essência", T_MEDIO, TINTA, SEMI)
    d.texto(s, ML, 9.08, W, C.METODO["nota"], T_MINI, CLARO, LIGHT,
            align=PP_ALIGN.CENTER, h=0.4)

    # ——— 01 A ORIGEM
    d.divisor(*C.SECOES[0][:2])

    s, x, lg = d.com_foto("A origem", C.ORIGEM["titulo"],
                          foto("09-origem"), alterna())
    d.texto(s, x, 4.45, lg, C.ORIGEM["lead"], T_LEAD, TINTA, LIGHT, h=1.2)
    d.texto(s, x, 5.85, lg, C.ORIGEM["corpo"], T_CORPO, CORPO, LIGHT, h=2.0)
    d.texto(s, x, 7.95, lg, C.ORIGEM["marcante"], T_MEDIO, TINTA, LIGHT, h=0.9)
    d.fio(s, x, 8.85, 1.30, ACENTO, esp=0.03)
    d.texto(s, x, 9.10, lg, "   ·   ".join(v.upper() for v in C.ORIGEM["valores"]),
            T_ROTULO, CLARO, SEMI, spc=2.0, h=0.4)

    s, x, lg = d.com_foto("A origem", C.SINAIS["titulo"],
                          foto("10-primeiros-sinais"), alterna())
    d.texto(s, x, 4.40, lg, C.SINAIS["lead"], T_LEAD, TINTA, LIGHT, h=1.15)
    d.texto(s, x, 5.65, lg, C.SINAIS["corpo"], T_CORPO, CORPO, LIGHT, h=1.85)
    y = 7.55
    for contexto, fala in C.SINAIS["falas"]:
        d.texto(s, x, y, lg, contexto, T_MINI, CLARO, LIGHT, h=0.3)
        d.texto(s, x, y + 0.28, 0.6, "“", T_FRASE, ACENTO, LIGHT, h=0.5)
        d.texto(s, x + 0.45, y + 0.34, lg - 0.5, fala, T_MEDIO, TINTA, LIGHT,
                h=0.55)
        y += 1.00

    # experiencias formadoras — duas por pagina, para o "o que isso revela"
    # ter ar suficiente
    for parte in range(0, len(C.EXPERIENCIAS), 2):
        nome_foto = "11-experiencias-1" if parte == 0 else "12-experiencias-2"
        s, x, lg = d.com_foto("A origem", C.EXPERIENCIAS_TITULO,
                              foto(nome_foto), alterna())
        for i, (num, tit, fato, revela) in enumerate(C.EXPERIENCIAS[parte:parte + 2]):
            y = 4.30 + i * 2.75
            d.fio(s, x, y, lg)
            d.texto(s, x, y + 0.30, 0.9, num, T_MINI, ACENTO, SEMI, spc=2.4, h=0.28)
            d.texto(s, x + 1.05, y + 0.20, lg - 1.05, tit, T_MEDIO, TINTA,
                    LIGHT, h=0.5)
            d.texto(s, x + 1.05, y + 0.78, lg - 1.05, fato, T_CORPO, CORPO,
                    LIGHT, h=0.95)
            d.rotulo(s, "O que isso revela", x + 1.05, y + 1.80, lg - 1.05)
            d.texto(s, x + 1.05, y + 2.08, lg - 1.05, revela, T_CORPO, TINTA,
                    LIGHT, h=0.60)

    # ——— 02 AS TENSÕES
    d.divisor(*C.SECOES[1][:2])

    # a tabela de tensoes respira em blocos de tres linhas por pagina; a
    # ultima pagina recebe o fecho da secao
    LINHAS = C.TENSOES["linhas"]
    for parte in range(0, len(LINHAS), 3):
        bloco = LINHAS[parte:parte + 3]
        ultima = parte + 3 >= len(LINHAS)
        s, x, lg = d.com_foto("As tensões", C.TENSOES["titulo"],
                              foto("14-tensoes"), alterna())
        if parte == 0:
            d.texto(s, x, 4.30, lg, C.TENSOES["lead"], T_MINI, CLARO, LIGHT,
                    h=0.35)
        y = 4.85 if parte == 0 else 4.45
        for rot, fala, resp, relato in bloco:
            alt = 1.35 if relato else 1.10
            d.fio(s, x, y, lg)
            d.rotulo(s, rot, x, y + 0.28, lg * 0.42)
            d.texto(s, x, y + 0.60, lg * 0.55, fala, T_CORPO, CORPO, LIGHT,
                    italic=not relato, h=alt - 0.55)
            d.fio(s, x + lg * 0.60, y + 0.64, 0.30, CLARO, esp=0.014)
            d.texto(s, x + lg * 0.68, y + 0.50, lg * 0.32, resp, T_CORPO,
                    TINTA, LIGHT, h=alt - 0.45)
            y += alt
        d.fio(s, x, y, lg)
        if ultima:
            d.texto(s, x, y + 0.32, lg, C.TENSOES["fecho"], T_CORPO, TINTA,
                    LIGHT, h=0.8)

    # ——— 03 OS PADRÕES
    d.divisor(*C.SECOES[2][:2])

    s, x, lg = d.com_foto("Os padrões", C.PADRAO["titulo"],
                          foto("16-padrao-invisivel"), alterna())
    d.texto(s, x, 4.35, lg, C.PADRAO["lead"], T_MINI, CLARO, LIGHT, h=0.5)
    for i, etapa in enumerate(C.PADRAO["etapas"]):
        y = 5.05 + i * 1.12
        d.ponto(s, x + 0.05, y + 0.16, 0.10)
        d.texto(s, x + 0.50, y, lg - 0.5, etapa, T_MEDIO, TINTA, LIGHT, h=0.75)
        if i < len(C.PADRAO["etapas"]) - 1:
            d.fio_v(s, x + 0.05, y + 0.38, 0.55, CLARO, esp=0.016)
    d.fio(s, x, 8.60, 1.30, ACENTO, esp=0.03)
    d.texto(s, x, 8.86, lg, C.PADRAO["fecho"], T_CORPO, CORPO, LIGHT, h=0.6)

    s, x, lg = d.com_foto("Os padrões", C.MOVIMENTO["titulo"],
                          foto("18-movimento"), alterna())
    for i, passo in enumerate(C.MOVIMENTO["passos"]):
        y = 4.25 + i * 0.78
        d.ponto(s, x + 0.05, y + 0.16, 0.09,
                ACENTO if i == len(C.MOVIMENTO["passos"]) - 1 else CLARO)
        d.texto(s, x + 0.50, y, lg - 0.5, passo, T_CORPO, TINTA, LIGHT, h=0.62)
        if i < len(C.MOVIMENTO["passos"]) - 1:
            d.fio_v(s, x + 0.05, y + 0.32, 0.34, CLARO, esp=0.014)
    d.fio(s, x, 8.62, lg)
    tf = d.caixa(s, x, 8.80, lg, 0.55)
    p = d.par(tf, True)
    for i, etapa in enumerate(C.MOVIMENTO["sintese"]):
        if i:
            d.txt(p, "  →  ", T_MEDIO, ACENTO, LIGHT)
        d.txt(p, etapa, T_MEDIO, TINTA, LIGHT)

    d.manifesto("Os padrões", C.LINHA_MESTRA["frase"], C.LINHA_MESTRA["apoio"])

    # ——— 04 O IKIGAI
    d.divisor(*C.SECOES[3][:2])

    s, x, lg = d.com_foto("O Ikigai", C.IKIGAI["titulo"],
                          foto("20-ikigai"), alterna())
    d.texto(s, x, 4.40, lg, C.IKIGAI["lead"], T_CORPO, CORPO, LIGHT, h=1.5)
    for i, q in enumerate(C.IKIGAI["perguntas"]):
        y = 6.05 + i * 0.60
        d.ponto(s, x + 0.05, y + 0.16, 0.09, CLARO)
        d.texto(s, x + 0.50, y, lg - 0.5, q, T_LEAD, TINTA, LIGHT, h=0.45)
    d.fio(s, x, 8.60, 1.30, ACENTO, esp=0.03)
    d.texto(s, x, 8.88, lg, C.IKIGAI["fecho"], T_CORPO, CORPO, LIGHT, h=0.6)

    s = d.pagina("O Ikigai", C.MAPA["titulo"])
    d.logo(s, SIMBOLO_IKIGAI, 16.45, 2.05, 1.30)
    for i, (rot, itens) in enumerate(C.MAPA["quadrantes"]):
        cx = ML + i * (COL + GAP)
        d.fio(s, cx, 4.45, COL)
        d.texto(s, cx, 4.75, COL, rot, T_LEAD, TINTA, LIGHT, h=0.9)
        d.texto(s, cx, 5.80, COL, itens, T_CORPO, CORPO, LIGHT, h=3.4)

    s, x, lg = d.com_foto("O Ikigai", C.CENTRO["titulo"],
                          foto("23-centro-ikigai"), alterna())
    d.texto(s, x, 4.40, lg, C.CENTRO["lead"], T_LEAD, TINTA, LIGHT, h=1.6)
    d.fio(s, x, 6.30, lg)
    for i, ex in enumerate(C.CENTRO["exemplos"]):
        d.texto(s, x, 6.50 + i * 0.42, lg, ex, T_CORPO, CORPO, LIGHT, h=0.35)
    d.texto(s, x, 8.35, lg, C.CENTRO["contexto"], T_MINI, CLARO, LIGHT, h=0.3)
    d.texto(s, x, 8.66, 0.6, "“", T_FRASE, ACENTO, LIGHT, h=0.5)
    d.texto(s, x + 0.45, 8.72, lg - 0.5, C.CENTRO["fala"], T_MEDIO, TINTA,
            LIGHT, h=0.7)

    s = d.slide()
    d.eyebrow(s, "O Ikigai")
    d.texto(s, ML, 2.50, 3.0, "RAZÃO DE SER", T_MINI, ACENTO, SEMI, spc=2.4,
            h=0.3)
    d.texto(s, ML, 3.10, 15.2, C.RAZAO_DE_SER["frase"], T_DISPLAY, TINTA,
            LIGHT, espaco=1.26)
    d.fio(s, ML, 6.60, 1.30, ACENTO, esp=0.03)
    d.texto(s, ML, 6.95, 14.0, C.RAZAO_DE_SER["apoio"], T_CORPO, CORPO, LIGHT,
            h=0.8)
    d.rodape(s)

    # ——— 05 A ESSÊNCIA
    d.divisor(*C.SECOES[4][:2])

    s = d.pagina("A essência", C.ENCONTRO["titulo"])
    d.texto(s, ML, 4.25, 14.0, C.ENCONTRO["lead"], T_CORPO, CORPO, LIGHT, h=1.1)
    for i, (rot, desc) in enumerate(C.ENCONTRO["eixos"]):
        cx = ML + i * (COL + GAP)
        d.fio(s, cx, 5.60, COL)
        d.texto(s, cx, 5.88, COL, rot, T_MEDIO, TINTA, LIGHT, h=0.5)
        d.texto(s, cx, 6.48, COL, desc, T_CORPO, CORPO, LIGHT, h=2.2)
    tf = d.caixa(s, ML, 8.85, W, 0.55)
    p = d.par(tf, True, align=PP_ALIGN.CENTER)
    for i, mov in enumerate(C.ENCONTRO["movimentos"]):
        if i:
            d.txt(p, "  ·  ", T_MEDIO, ACENTO, LIGHT)
        d.txt(p, mov, T_MEDIO, TINTA, LIGHT)

    s = d.slide()
    d.eyebrow(s, C.ESSENCIA["eyebrow"])
    d.texto(s, ML, 2.55, 15.2, C.ESSENCIA["frase"], T_DISPLAY, TINTA, LIGHT,
            espaco=1.24)
    d.fio(s, ML, 5.55, W)
    LC, LG = 4.65, 0.55
    for i, (rot, desc) in enumerate(C.ESSENCIA["camadas"]):
        cx = ML + i * (LC + LG)
        d.rotulo(s, rot, cx, 5.95, LC)
        d.texto(s, cx, 6.35, LC, desc, T_CORPO, CORPO, LIGHT, h=2.2)
    d.fio(s, ML, 8.75, W)
    d.texto(s, ML, 9.10, 15.2, C.ESSENCIA["fecho"], T_CORPO, TINTA, LIGHT, h=0.8)
    d.rodape(s)

    # ——— 06 AS MARCAS
    d.divisor(*C.SECOES[5][:2])

    s, x, lg = d.com_foto("As marcas", C.MARCAS["titulo"],
                          foto("29-marcas"), alterna(), fatia=0.34)
    d.texto(s, x, 3.95, lg, C.MARCAS["lead"], T_MINI, CLARO, LIGHT, h=0.35)
    y = 4.45
    for rot, tit, desc in C.MARCAS["marcas"]:
        d.fio(s, x, y, lg)
        d.rotulo(s, rot, x, y + 0.26, lg, cor=ACENTO)
        d.texto(s, x, y + 0.58, lg, tit, T_MEDIO, TINTA, LIGHT, h=0.5)
        d.texto(s, x, y + 1.15, lg, desc, T_CORPO, CORPO, LIGHT, h=1.25)
        y += 2.22
    d.texto(s, x, y + 0.12, lg, C.MARCAS["fecho"], T_MINI, CLARO, LIGHT, h=0.5)

    s, x, lg = d.com_foto("Próxima etapa", C.PROXIMA["titulo"],
                          foto("30-estrategia"), alterna())
    d.texto(s, x, 4.45, lg, C.PROXIMA["lead"], T_CORPO, CORPO, LIGHT, h=1.5)
    d.fio(s, x, 6.30, lg)
    d.rotulo(s, "O que vem a seguir", x, 6.60, lg)
    d.texto(s, x, 6.98, lg, C.PROXIMA["corpo"], T_CORPO, CORPO, LIGHT, h=1.2)
    d.texto(s, x, 8.35, lg, C.PROXIMA["destaque"], T_LEAD, TINTA, LIGHT, h=1.5)

    # fecho seco + agradecimento
    s = d.slide()
    d.fio(s, ML, 4.55, 1.30, ACENTO, esp=0.03)
    d.texto(s, ML, 5.00, 15.2, C.FECHO, T_DISPLAY, TINTA, LIGHT, espaco=1.3)
    d.rodape(s)
    d.fecho()

    return d


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: gerar.py <pasta-do-cliente>")
    pasta = os.path.abspath(sys.argv[1])
    C = carregar(pasta)
    deck = montar(C, pasta)
    saida = os.path.join(pasta, "Revelacao-de-Essencia-%s.pptx" % C.ARQUIVO)
    caminho, n = deck.salvar(saida)
    print("OK ->", caminho, n, "slides")
