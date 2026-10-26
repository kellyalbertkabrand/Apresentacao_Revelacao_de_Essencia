#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Acusa primeira pessoa do plural no texto das apresentações.

    python3 padrao-ka/conferir_voz.py                      # tudo
    python3 padrao-ka/conferir_voz.py clientes/flavia-muccelin

A Kelly pediu em outubro/2026: **nada de "nosso", "nossa", "assumimos",
"mudar nossa essência"**. A razão é prática — na primeira pessoa o documento
só funciona lido de dentro, e o mesmo arquivo precisa apresentar a marca a um
sócio, a um candidato ou ao mercado. Em terceira pessoa ele afirma; na
primeira, ele desabafa.

A conferência lê o conteúdo como CÓDIGO, não como texto: percorre a árvore
sintática e examina só as strings que chegam ao slide. Assim um comentário
ou uma docstring explicando a regra não vira falso positivo — que foi
exatamente o que aconteceu na primeira versão feita com `grep`.

Duas exceções ficam fora da varredura, declaradas em EXCECOES: o manifesto
(gênero em que a marca fala, e o "nós" ali costuma ser o universal) e a fala
de exemplo numa página de tom de voz (citação de discurso, não afirmação
sobre a marca).
"""
import ast
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# "nós" leva acento; sem ele a classe [óo] casava também com a
# preposicao "nos" e acusava todo "nos materiais" da vida
PRONOME = re.compile(r"\b(noss[oa]s?|nós|conosco)\b", re.I)
# -amos/-emos/-imos sao as desinencias de primeira pessoa do plural
DESINENCIA = re.compile(r"\b\w{3,}(?:amos|emos|imos|ramos|ssemos)\b", re.I)
IRREGULAR = re.compile(r"\b(somos|temos|vamos|estamos|fomos|seremos|podemos|"
                       r"devemos|queremos|fazemos|vimos|pomos)\b", re.I)
# "nos" e quase sempre a preposicao em+os ("nos materiais", "nos produtos"):
# tentar separar verbo de substantivo pela desinencia da falso positivo em
# todo plural terminado em -os. Por isso a regra e uma LISTA FECHADA dos
# verbos que de fato aparecem com o pronome ("o que nos torna", "que nos
# definem") — precisa, em vez de esperta.
NOS_PRONOME = re.compile(
    r"\bnos\s+(torna\w*|define\w*|definiu|conecta\w*|une|unem|uniu|"
    r"move\w*|leva\w*|faz|fazem|fez|guia\w*|limita\w*|impede\w*|"
    r"ensina\w*|diferencia\w*|representa\w*|trouxe\w*|formou|formaram)\b",
    re.I)

# Trechos que PODEM falar na primeira pessoa, por genero. A chave e o arquivo
# e o valor e o comeco do texto.
EXCECOES = {
    "clientes/lucas-martini/brandbook.py": (
        "dependente daquilo que não podemos controlar",
        "Enquanto podemos escolher",
        "Antes do produto, precisamos entender o impacto financeiro",
    ),
}


def liberado(caminho, texto):
    rel = os.path.relpath(caminho, RAIZ).replace(os.sep, "/")
    for inicio in EXCECOES.get(rel, ()):
        if texto.strip().startswith(inicio):
            return True
    return False


def falas(caminho):
    """So as strings que viram texto de slide — nada de docstring."""
    fonte = open(caminho, encoding="utf-8").read()
    arvore = ast.parse(fonte, caminho)
    documentos = set()
    for no in ast.walk(arvore):
        if isinstance(no, (ast.Module, ast.ClassDef, ast.FunctionDef,
                           ast.AsyncFunctionDef)):
            doc = ast.get_docstring(no, clean=False)
            if doc:
                documentos.add(doc)
    for no in ast.walk(arvore):
        if isinstance(no, ast.Constant) and isinstance(no.value, str):
            if no.value in documentos or len(no.value) < 3:
                continue
            yield no.lineno, no.value


def acusa(texto):
    for regra in (PRONOME, DESINENCIA, IRREGULAR, NOS_PRONOME):
        achado = regra.search(texto)
        if achado:
            return achado.group(0)
    return None


def conferir(alvos):
    arquivos = []
    for alvo in alvos:
        if os.path.isdir(alvo):
            arquivos += sorted(glob.glob(os.path.join(alvo, "*.py")))
        else:
            arquivos.append(alvo)
    pulos = ("gerar.py", "vetorizar.py", "logotipos.py", "rostos.py")
    total = 0
    for caminho in arquivos:
        if os.path.basename(caminho) in pulos:
            continue
        for linha, texto in falas(caminho):
            if liberado(caminho, texto):
                continue
            marca = acusa(texto)
            if marca:
                total += 1
                print("%s:%d  [%s]  %s"
                      % (os.path.relpath(caminho, RAIZ), linha, marca,
                         texto.strip()[:92]))
    if total:
        print("\n%d trecho(s) em primeira pessoa. A regra esta em CLAUDE.md."
              % total)
    else:
        print("VOZ EM TERCEIRA PESSOA EM TODAS AS APRESENTACOES")
    return total


if __name__ == "__main__":
    alvos = sys.argv[1:]
    if not alvos:
        alvos = (sorted(glob.glob(os.path.join(RAIZ, "clientes", "*")))
                 + sorted(glob.glob(os.path.join(RAIZ, "modelos", "*"))))
        alvos = [a for a in alvos if os.path.isdir(a)]
    sys.exit(1 if conferir(alvos) else 0)
