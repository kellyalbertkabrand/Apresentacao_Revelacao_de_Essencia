# -*- coding: utf-8 -*-
"""montar.py — fecha o PPTX nativo a partir do spec.json medido pelo extrair.js.

    python3 montar.py <pasta-do-deck> [saida.pptx] [ids...]

Texto vira caixa de texto na Outfit certa, filete e pilula viram forma, foto
vira imagem ja cortada e com os cantos do layout. Nada de slide-imagem: o
arquivo abre no PowerPoint e cada palavra pode ser editada."""
import json, os, re, sys
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

DECK = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
EDIT = os.path.join(DECK, 'edit')
IMG = os.path.join(EDIT, 'img')
os.makedirs(IMG, exist_ok=True)

LARG, ALT = 1920, 1080
ALTURA_LINHA = 1.122      # altura da caixa de texto da Outfit, em ems
EMU_W = 12192000
K = EMU_W / LARG                      # 6350 EMU por px
def E(v): return Emu(int(round(v * K)))
def P(v): return Pt(v / 2.0)          # 1920px = 960pt

PESOS = {100:'Outfit 1 Light', 200:'Outfit 1 Light', 300:'Outfit 1 Light',
         400:'Outfit 1', 500:'Outfit 1 Medium', 600:'Outfit 1 Semi-Bold',
         700:'Outfit 1 Bold', 800:'Outfit 1 Ultra-Bold', 900:'Outfit 1 Ultra-Bold'}

ALIN = {'left':PP_ALIGN.LEFT, 'start':PP_ALIGN.LEFT, 'center':PP_ALIGN.CENTER,
        'right':PP_ALIGN.RIGHT, 'end':PP_ALIGN.RIGHT, 'justify':PP_ALIGN.JUSTIFY}

def cor(css):
    m = re.match(r'rgba?\(([^)]+)\)', css or '')
    if not m: return RGBColor(0,0,0), 1.0
    p = [x.strip() for x in m.group(1).replace('/', ' ').split(',')]
    if len(p) == 1: p = m.group(1).split()
    r, g, b = (int(round(float(x))) for x in p[:3])
    a = float(p[3]) if len(p) > 3 else 1.0
    return RGBColor(r, g, b), a

def alpha_na_forma(forma, a):
    """Transparencia do preenchimento solido (alpha CSS -> alpha OOXML)."""
    if a >= 0.999: return
    srgb = forma.fill._xPr.find(qn('a:solidFill')).find(qn('a:srgbClr'))
    el = srgb.makeelement(qn('a:alpha'), {'val': str(int(round(a * 100000)))})
    srgb.append(el)

def espacamento(run, ls_px):
    if abs(ls_px) < 0.01: return
    run.font._rPr.set('spc', str(int(round(ls_px / 2.0 * 100))))

def sem_estilo(forma):
    """Tira o estilo de tema da forma (sombra e contorno herdados) e some
    com qualquer efeito: a pilula do rodape e um filete, nao um botao."""
    el = forma._element
    st = el.find(qn('p:style'))
    if st is not None: el.remove(st)
    spPr = el.spPr
    if spPr.find(qn('a:effectLst')) is None:
        spPr.append(spPr.makeelement(qn('a:effectLst'), {}))


def sem_autofit(tf):
    bodyPr = tf._txBody.find(qn('a:bodyPr'))
    for t in ('a:normAutofit', 'a:spAutoFit'):
        e = bodyPr.find(qn(t))
        if e is not None: bodyPr.remove(e)
    bodyPr.append(bodyPr.makeelement(qn('a:noAutofit'), {}))

# ---------------------------------------------------------------- imagens
def cantos(im, raio, escala):
    if raio <= 0: return im
    r = int(round(raio * escala))
    r = min(r, im.size[0]//2, im.size[1]//2)
    masc = Image.new('L', im.size, 0)
    ImageDraw.Draw(masc).rounded_rectangle([0, 0, im.size[0]-1, im.size[1]-1],
                                           radius=r, fill=255)
    fora = im.convert('RGBA')
    fora.putalpha(masc)
    return fora

def preparar(src, b, fit, raio, cache={}):
    """Devolve (arquivo, x, y, w, h) ja com corte e cantos aplicados."""
    chave = (src, round(b['w']), round(b['h']), fit, raio)
    if chave in cache: return cache[chave]
    cam = src.replace('file://', '')
    im = Image.open(cam)
    bw, bh = b['w'], b['h']
    if fit == 'contain':
        s = min(bw / im.width, bh / im.height)
        dw, dh = im.width * s, im.height * s
        dest = (cam, b['x'] + (bw - dw) / 2, b['y'] + (bh - dh) / 2, dw, dh)
        if raio <= 0 and im.mode in ('RGB', 'RGBA', 'P', 'L'):
            cache[chave] = dest; return dest
    # cover: corta no centro para a proporcao da caixa
    alvo = bw / bh
    w, h = im.size
    if w / h > alvo:
        nw = int(round(h * alvo)); x0 = (w - nw) // 2
        im = im.crop((x0, 0, x0 + nw, h))
    else:
        nh = int(round(w / alvo)); y0 = (h - nh) // 2
        im = im.crop((0, y0, w, y0 + nh))
    escala = min(3.0, max(1.0, im.width / bw))
    larg = int(round(bw * escala)); altu = int(round(bh * escala))
    im = im.resize((larg, altu), Image.LANCZOS)
    im = cantos(im, raio, escala)
    nome = re.sub(r'[^a-zA-Z0-9]+', '-', os.path.basename(cam))[:40]
    base = os.path.join(IMG, '%s-%dx%d-%d' % (nome, larg, altu, raio))
    if im.mode == 'RGBA':                      # cantos redondos: precisa de alfa
        saida = base + '.png'
        im.save(saida)
    else:                                      # foto cheia: JPEG segura o arquivo
        saida = base + '.jpg'
        im.convert('RGB').save(saida, 'JPEG', quality=90, optimize=True)
    dest = (saida, b['x'], b['y'], bw, bh)
    cache[chave] = dest
    return dest

# ---------------------------------------------------------------- montagem
def forma_retangulo(slide, it):
    b = it['b']
    raios = it.get('raios') or [it.get('raio', 0)] * 4
    raio = max(raios)
    menor = max(1.0, min(b['w'], b['h']))
    if raio > 0:
        f = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                   E(b['x']), E(b['y']), E(b['w']), E(b['h']))
        f.adjustments[0] = min(raio / menor, 0.5)
    else:
        f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                   E(b['x']), E(b['y']), E(b['w']), E(b['h']))
    sem_estilo(f)
    if it.get('fundo'):
        c, a = cor(it['fundo'])
        f.fill.solid(); f.fill.fore_color.rgb = c; alpha_na_forma(f, a)
    else:
        f.fill.background()
    bordas = it.get('bordas') or {}
    lados = {k: v for k, v in bordas.items() if v}
    todas = len(lados) == 4 and len({(v['w'], v['cor'], v['estilo']) for v in lados.values()}) == 1
    if todas:
        bd = next(iter(lados.values()))
        c, a = cor(bd['cor'])
        f.line.color.rgb = c; f.line.width = P(bd['w'])
        if bd['estilo'] == 'dashed':
            ln = f.line._get_or_add_ln()
            ln.append(ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))
    else:
        f.line.fill.background()
        for nome, bd in lados.items():     # filete de um lado so: barra fina
            w = bd['w']
            cx, cy, cw, ch = b['x'], b['y'], b['w'], b['h']
            if nome == 'topo':    cy, ch = b['y'], w
            elif nome == 'baixo': cy, ch = b['y'] + b['h'] - w, w
            elif nome == 'esquerda': cx, cw = b['x'], w
            else:                 cx, cw = b['x'] + b['w'] - w, w
            fil = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                         E(cx), E(cy), E(cw), E(ch))
            sem_estilo(fil)
            c, a = cor(bd['cor'])
            fil.fill.solid(); fil.fill.fore_color.rgb = c; alpha_na_forma(fil, a)
            fil.line.fill.background()
    if not it.get('fundo') and not todas:
        f._element.getparent().remove(f._element)   # so os filetes ficam
        return
    # cantos assimetricos: tapa o lado que deve ser reto
    if raio > 0 and len(set(raios)) > 1 and it.get('fundo'):
        esq, dir_ = raios[0] or raios[3], raios[1] or raios[2]
        if esq and not dir_:
            tapa = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                E(b['x'] + raio), E(b['y']), E(b['w'] - raio), E(b['h']))
        elif dir_ and not esq:
            tapa = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                E(b['x']), E(b['y']), E(b['w'] - raio), E(b['h']))
        else:
            tapa = None
        if tapa is not None:
            sem_estilo(tapa)
            c, a = cor(it['fundo'])
            tapa.fill.solid(); tapa.fill.fore_color.rgb = c; alpha_na_forma(tapa, a)
            tapa.line.fill.background()

def forma_texto(slide, it, folga=0.0):
    b = it['b']
    cx, cy, cw, ch = b['cx'], b['cy'], b['cw'], b['ch']
    # O navegador centra a linha dentro da entrelinha; o PowerPoint apoia o texto
    # mais abaixo. ALTURA_LINHA e a altura real da Outfit (ascendente + descendente)
    # medida contra o LibreOffice: sem este ajuste o corpo desce ~5px.
    ajuste = -(it['lh'] - ALTURA_LINHA * it['tam']) / 2.0
    tb = slide.shapes.add_textbox(E(cx), E(cy + folga + ajuste), E(cw), E(ch + 40))
    tf = tb.text_frame
    tf.word_wrap = not it.get('nowrap')
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    sem_autofit(tf)
    paragrafos = [[]]
    for t in it['trechos']:
        if t.get('br'): paragrafos.append([])
        else: paragrafos[-1].append(t)
    primeiro = True
    for trechos in paragrafos:
        p = tf.paragraphs[0] if primeiro else tf.add_paragraph()
        primeiro = False
        p.alignment = ALIN.get(it['align'], PP_ALIGN.LEFT)
        p.line_spacing = P(it['lh'])
        p.space_before = Pt(0); p.space_after = Pt(0)
        if not trechos:
            r = p.add_run(); r.text = ' '
            r.font.size = P(it['tam']); r.font.name = PESOS[it['peso']]
            continue
        for t in trechos:
            r = p.add_run()
            r.text = t['t']
            r.font.size = P(t.get('tam') or it['tam'])
            r.font.name = PESOS.get(t.get('peso') or it['peso'], 'Outfit 1')
            c, _ = cor(t.get('cor') or it['cor'])
            r.font.color.rgb = c
            espacamento(r, t.get('ls') or 0)

def forma_imagem(slide, it):
    b = it['b']
    if it.get('arquivo'):
        cam = os.path.join(EDIT, it['arquivo'])
        slide.shapes.add_picture(cam, E(b['x']), E(b['y']), E(b['w']), E(b['h']))
        return
    cam, x, y, w, h = preparar(it['src'], b, it.get('fit', 'fill'), it.get('raio', 0))
    slide.shapes.add_picture(cam, E(x), E(y), E(w), E(h))

def forma_svg(slide, it):
    b = it['b']
    cam = os.path.join(EDIT, it['arquivo'])
    slide.shapes.add_picture(cam, E(b['x']), E(b['y']), E(b['w']), E(b['h']))

def montar(spec, saida, folga=0.0):
    prs = Presentation()
    prs.slide_width = Emu(EMU_W)
    prs.slide_height = Emu(int(round(EMU_W * ALT / LARG)))
    branco = prs.slide_layouts[6]
    for s in spec:
        slide = prs.slides.add_slide(branco)
        c, a = cor(s['fundo'])
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = c
        for it in s['itens']:
            if it['tipo'] == 'rect': forma_retangulo(slide, it)
            elif it['tipo'] == 'texto': forma_texto(slide, it, folga)
            elif it['tipo'] == 'img': forma_imagem(slide, it)
            elif it['tipo'] == 'svg': forma_svg(slide, it)
        if s.get('nota'):
            slide.notes_slide.notes_text_frame.text = s['nota']
    prs.save(saida)
    return saida

if __name__ == '__main__':
    spec = json.load(open(os.path.join(EDIT, 'spec.json')))
    alvo = sys.argv[2] if len(sys.argv) > 2 else os.path.join(EDIT, 'editavel.pptx')
    ids = sys.argv[3:]
    if ids: spec = [s for s in spec if s['id'] in ids]
    montar(spec, alvo)
    print(len(spec), 'slides ->', alvo, round(os.path.getsize(alvo)/1e6, 1), 'MB')
