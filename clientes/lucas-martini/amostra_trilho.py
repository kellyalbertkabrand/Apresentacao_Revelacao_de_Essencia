# -*- coding: utf-8 -*-
"""Amostra: cabeçalho vertical à esquerda (brasão + nome do documento) e a
paginação no rodapé, à direita."""
import importlib.util, os, subprocess, sys
RAIZ = '/home/user/apresentacoes'
sys.path.insert(0, os.path.join(RAIZ, 'padrao-ka'))
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
import ka_brandbook as kb
from ka_brandbook import Brandbook, ML, MR, Y_CABECA, T_CABECA, SEMI, LIGHT

def carregar(cam, nome):
    spec = importlib.util.spec_from_file_location(nome, cam)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

C = carregar(os.path.join(RAIZ, 'clientes/lucas-martini/brandbook.py'), 'bb')

class ComTrilho(Brandbook):
    """O cabeçalho vira um trilho vertical na margem esquerda."""

    def cabecalho(self, s, tom):
        _, _, acento, _ = self.tinta(tom)
        suave = self.p["suave"] if tom != "escuro" else self.p["corpo_escuro"]
        escudo = self.logos.get("escudo")
        if escudo:
            self.logo(s, escudo, 0.42, 0.52, 0.46)
        if self.cabecalho_documento:
            tf = self.caixa(s, 0.30, 1.18, 0.70, 5.40)
            bodyPr = tf._txBody.find(qn('a:bodyPr'))
            bodyPr.set('vert', 'vert')   # lê de cima para baixo
            p = self.par(tf, primeiro=True, align=PP_ALIGN.LEFT)
            self.txt(p, "%s %s" % (self.documento, self.marca), T_CABECA,
                     suave, SEMI, spc=2.6)
        if tom != "escuro":
            self.texto(s, MR - 4.0, 10.42, 4.0,
                       "%02d / %02d" % (self.n, self.total or self.n),
                       T_CABECA, acento, SEMI, spc=2.6, h=0.30,
                       align=PP_ALIGN.RIGHT)

d = ComTrilho(marca=C.MARCA, documento=C.DOCUMENTO, paleta=C.PALETA,
              logos=C.LOGOS)
# uma página de conteúdo de verdade, para ver o trilho em contexto
amostra = [p for p in C.PAGINAS if p.get("titulo") == "Essência da marca"]
d.n = 6
d.montar(amostra)
# a amostra tem uma página só; a paginação mostra onde ela cairia no manual
for sh in d.prs.slides[0].shapes:
    if sh.has_text_frame and ' / 01' in sh.text_frame.text:
        for par in sh.text_frame.paragraphs:
            for run in par.runs:
                run.text = run.text.replace('/ 01', '/ 29').replace('07', '07')
alvo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'amostra-trilho.pptx')
d.salvar(alvo)
subprocess.run(['soffice', '--headless', '--norestore', '--convert-to', 'pdf',
                '--outdir', os.path.dirname(alvo), alvo], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)
print('ok', alvo)
