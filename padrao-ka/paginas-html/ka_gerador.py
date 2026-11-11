# -*- coding: utf-8 -*-
"""Arquétipos de página do Padrão KA, na mesma marcação do Plano de Conteúdo
do Lucas. Cada função devolve o HTML de um slide de 1920 x 1080."""
import hashlib, os, re

PAPEL, PAPEL2 = '#f8f7f2', '#eeece4'
MARINHO, AZUL2 = '#152535', '#223a52'
CARAMELO, CARAMELO_CLARO = '#d86f2a', '#df8a53'
FONTE = "Outfit, 'Helvetica Neue', Arial, sans-serif"
W = 1704

KA_ESCURO = '8d5913128f405715125bd34facfd8b72.svg'
KA_CLARO = '3b0fd5a7044b351c7bcf6371dbdff61a.svg'
VM_ESCURO, VM_CLARO = 'vm-rocks.png', 'vm-rocks-claro.png'

def blob(nome):
    return '/_blob/' + hashlib.md5(nome.encode()).hexdigest()

def b(t):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)

# ---------------------------------------------------------------- moldura
def rodape(rotulo, marca, claro=False):
    pil = '#223a528c' if claro else '#eeece48c'
    cor = PAPEL if claro else MARINHO
    bar = CARAMELO_CLARO if claro else CARAMELO
    logo = KA_CLARO if claro else KA_ESCURO
    return (f'<div style="position:absolute;left:108px;bottom:36px;width:1075px;'
            f'height:52px;border-radius:52px;background:{pil}"></div>\n'
            f'<p style="position:absolute;left:148px;top:1003px;width:1000px;line-height:1.2;'
            f'font-size:24px;font-weight:500;letter-spacing:3px;color:{cor}">{rotulo} '
            f'<span style="color:{bar}">|</span> <b>{marca}</b></p>\n'
            f'<img src="{blob(logo)}" alt="KA Inteligência para Marcas" '
            f'style="position:absolute;right:108px;bottom:42px;width:320px;height:72px;'
            f'object-fit:contain">')

def secao(sid, corpo, fundo=PAPEL, cor=MARINHO, pad='108px 108px 160px',
          just='', align='', gap=40, nota=None, rodape_html=''):
    j = f'justify-content:{just};' if just else ''
    a = f'align-items:{align};' if align else ''
    aside = f'\n<aside>{nota}</aside>' if nota else ''
    return (f'<section id="{sid}" data-transition="fade" style="background:{fundo};color:{cor};'
            f'font-family:{FONTE};padding:{pad};display:flex;flex-direction:column;'
            f'{j}{a}gap:{gap}px">\n{corpo}\n{rodape_html}{aside}\n</section>\n')

def cabeca(titulo):
    return (f'<div style="display:flex;flex-direction:column;gap:24px">'
            f'<h2 style="font-size:52px;font-weight:300;line-height:1.15;letter-spacing:3px;'
            f'width:{W}px">{b(titulo)}</h2>'
            f'<div style="width:{W}px;height:2px;background:{CARAMELO}"></div></div>')

def miolo(interno, gap=40):
    return (f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center;'
            f'align-items:center;gap:{gap}px;width:{W}px">\n{interno}\n</div>')

def par(texto, tam=38, cor=None, larg=W, lh=1.4, al='left', peso=300):
    c = f';color:{cor}' if cor else ''
    return (f'<p style="font-size:{tam}px;font-weight:{peso};line-height:{lh};text-align:{al};'
            f'width:{larg}px{c}">{b(texto)}</p>')

def rotulo(texto, tam=26, cor=None, larg=W):
    return (f'<p style="font-size:{tam}px;font-weight:600;letter-spacing:5px;'
            f'color:{cor or CARAMELO};width:{larg}px;line-height:1.3">| {texto}</p>')

def filete(larg=96, alt=3):
    return f'<div style="width:{larg}px;height:{alt}px;background:{CARAMELO}"></div>'

# ---------------------------------------------------------------- páginas
def pg_abertura(sid):
    return secao(sid, (
        f'<img src="{blob(KA_ESCURO)}" alt="KA Inteligência para Marcas" '
        f'style="width:480px;height:152px;object-fit:contain">\n'
        f'<div style="width:2px;height:140px;background:{CARAMELO}"></div>\n'
        f'<img src="{blob(VM_ESCURO)}" alt="VM Rocks Design" '
        f'style="width:380px;height:109px;object-fit:contain">'),
        pad='108px', just='center', align='center', gap=56
    ).replace('flex-direction:column;justify-content', 'flex-direction:row;justify-content')

def pg_capa(sid, linhas, assinatura, data='OUTUBRO/2026', nota=None):
    titulo = '<br>'.join(b(l) for l in linhas)
    return secao(sid, (
        f'<h1 style="font-size:110px;font-weight:300;line-height:1.02;letter-spacing:3px;'
        f'width:{W}px">{titulo}</h1>\n'
        f'<p style="font-size:60px;font-weight:300;line-height:1.2;text-align:left;width:{W}px;'
        f'padding:40px 0px 0px">{b(assinatura)}</p>\n'
        f'<div style="display:flex;align-items:center;gap:40px;padding:88px 0px 0px">'
        f'<img src="{blob(KA_ESCURO)}" alt="KA Inteligência para Marcas" '
        f'style="width:340px;height:108px;object-fit:contain">'
        f'<div style="width:2px;height:96px;background:{CARAMELO}"></div>'
        f'<img src="{blob(VM_ESCURO)}" alt="VM Rocks Design" '
        f'style="width:260px;height:75px;object-fit:contain">'
        f'<div style="width:2px;height:96px;background:{CARAMELO}"></div>'
        f'<p style="font-size:32px;font-weight:300;line-height:1.3;text-align:left;width:224px;'
        f'white-space:nowrap">Método <b>Marca</b><br><b>com Essência©</b></p>'
        f'<div style="width:2px;height:96px;background:{CARAMELO}"></div>'
        f'<p style="font-size:24px;font-weight:500;line-height:1.4;text-align:left;width:280px;'
        f'letter-spacing:6px;white-space:nowrap">{data}</p></div>'),
        pad='108px', just='center', align='flex-start', gap=0, nota=nota)

def pg_sumario(sid, itens, rod, tam=38, pad_linha=22):
    meio = (len(itens) + 1) // 2
    def coluna(bloco, ini):
        linhas = ''
        for i, t in enumerate(bloco, ini):
            linhas += (f'<div style="display:flex;gap:28px;padding:{pad_linha}px 0px;'
                       f'border-top:1px solid {CARAMELO}">'
                       f'<p style="font-size:{tam}px;font-weight:700;color:{CARAMELO};width:72px;'
                       f'line-height:1.3">{i:02d}</p>'
                       f'<p style="font-size:{tam}px;font-weight:300;line-height:1.3;'
                       f'text-align:left;width:700px">{t}</p></div>')
        return (f'<div style="width:812px;display:flex;flex-direction:column;'
                f'border-bottom:1px solid {CARAMELO}">{linhas}</div>')
    corpo = (cabeca('<b>SUMÁRIO</b>') + '\n' +
             miolo(f'<div style="display:flex;gap:80px;width:{W}px">'
                   f'{coluna(itens[:meio], 1)}{coluna(itens[meio:], meio + 1)}</div>'))
    return secao(sid, corpo, rodape_html=rod)

def pg_divisor(sid, numero, titulo, linha, foto, rotulo_rod, marca, nota=None):
    tit = '<br>'.join(titulo) if isinstance(titulo, list) else titulo
    corpo = (f'<img src="{blob(foto)}" alt="{nota or "Lucas Martini"}" '
             f'style="position:absolute;left:960px;top:108px;width:852px;height:812px;'
             f'object-fit:cover;border-radius:24px">\n'
             f'<p style="font-size:30px;font-weight:600;letter-spacing:7px;color:{CARAMELO}">'
             f'| {numero}</p>\n'
             f'<h1 style="font-size:120px;font-weight:600;line-height:1;letter-spacing:4px;'
             f'width:833px">{tit}</h1>\n'
             f'<p style="font-size:44px;font-weight:300;line-height:1.3;text-align:left;'
             f'width:760px;color:{PAPEL2}">{b(linha)}</p>')
    return secao(sid, corpo, fundo=MARINHO, cor=PAPEL, just='center', align='flex-start',
                 gap=24, nota=nota, rodape_html=rodape(rotulo_rod, marca, claro=True))

def pg_texto(sid, titulo, paragrafos, rod, tam=38, gap=28, nota=None):
    blocos = ''.join(par(p, tam=tam) for p in paragrafos)
    corpo = (cabeca(titulo) + '\n' +
             miolo(f'<div style="width:{W}px;display:flex;flex-direction:column;'
                   f'gap:{gap}px">{blocos}</div>'))
    return secao(sid, corpo, nota=nota, rodape_html=rod)

def pg_camadas(sid, titulo, linhas, rod, larg_rotulo=360, tam=38, tam_rot=28,
               pad=30, fecho=None, nota=None, intro=None, tam_intro=34):
    larg_txt = W - larg_rotulo - 40
    rows = ''
    for rot, txt in linhas:
        rows += (f'<div style="display:flex;gap:40px;align-items:baseline;padding:{pad}px 0px;'
                 f'border-top:1px solid {CARAMELO}">'
                 f'<p style="font-size:{tam_rot}px;font-weight:600;letter-spacing:5px;'
                 f'color:{CARAMELO};width:{larg_rotulo}px;line-height:1.3">{rot}</p>'
                 f'<p style="font-size:{tam}px;font-weight:300;line-height:1.35;text-align:left;'
                 f'width:{larg_txt}px">{b(txt)}</p></div>')
    escada = (f'<div style="width:{W}px;display:flex;flex-direction:column;'
              f'border-bottom:1px solid {CARAMELO}">{rows}</div>')
    if intro:
        escada = par(intro, tam=tam_intro, lh=1.45) + '\n' + escada
    if fecho:
        escada += '\n' + par(fecho, tam=32, cor=AZUL2, larg=W, al='left')
    return secao(sid, cabeca(titulo) + '\n' + miolo(escada), nota=nota, rodape_html=rod)

def pg_cartoes(sid, titulo, cartoes, rod, tam=32, fecho=None, nota=None):
    cs = ''
    for rot, txt in cartoes:
        cs += (f'<div style="flex:1;display:flex;flex-direction:column;gap:20px;'
               f'background:{PAPEL2};padding:44px 40px;border-radius:24px">'
               f'<p style="font-size:26px;font-weight:600;letter-spacing:5px;color:{CARAMELO};'
               f'line-height:1.3">| {rot}</p>'
               f'<p style="font-size:{tam}px;font-weight:300;line-height:1.4;text-align:left">'
               f'{b(txt)}</p></div>')
    interno = f'<div style="display:flex;gap:28px;width:{W}px">{cs}</div>'
    if fecho:
        interno += '\n' + par(fecho, tam=34, larg=1400, al='center')
    return secao(sid, cabeca(titulo) + '\n' + miolo(interno), nota=nota, rodape_html=rod)

def pg_caixa(sid, titulo, etiqueta, frase, paragrafos, rod, tam_frase=52, tam=34,
             pad='72px 80px', nota=None):
    ps = ''.join(par(p, tam=tam, lh=1.45, larg=1544) for p in paragrafos)
    caixa = (f'<div style="width:1544px;display:flex;flex-direction:column;gap:32px;'
             f'background:{PAPEL2};padding:{pad};border-radius:24px">'
             f'{rotulo(etiqueta, larg=1544)}'
             f'<p style="font-size:{tam_frase}px;font-weight:600;line-height:1.2;text-align:left;'
             f'width:1544px">{b(frase)}</p>{filete()}{ps}</div>')
    return secao(sid, cabeca(titulo) + '\n' + miolo(caixa), nota=nota, rodape_html=rod)

def pg_frase(sid, etiqueta, frase, apoio, rod_claro, foto=None, tam=72, nota=None,
             rotulo_rod=None, marca=None):
    """Página-manifesto: marinho, frase grande e, opcionalmente, foto à direita."""
    larg = 1140 if foto else W
    corpo = ''
    if foto:
        corpo += (f'<img src="{blob(foto)}" alt="Lucas Martini" '
                  f'style="position:absolute;left:1292px;top:108px;width:520px;height:812px;'
                  f'object-fit:cover;border-radius:24px">\n')
    if etiqueta:
        corpo += (f'<p style="font-size:30px;font-weight:600;letter-spacing:7px;'
                  f'color:{CARAMELO_CLARO}">| {etiqueta}</p>\n')
    corpo += (f'<h2 style="font-size:{tam}px;font-weight:600;line-height:1.15;letter-spacing:2px;'
              f'width:{larg}px">{b(frase)}</h2>\n'
              f'<div style="width:96px;height:3px;background:{CARAMELO_CLARO}"></div>')
    if apoio:
        corpo += ('\n' + f'<p style="font-size:34px;font-weight:300;line-height:1.45;'
                  f'text-align:left;width:{larg}px;color:{PAPEL2}">{b(apoio)}</p>')
    return secao(sid, corpo, fundo=MARINHO, cor=PAPEL, just='center', align='flex-start',
                 gap=28, nota=nota, rodape_html=rod_claro)

def pg_obrigada(sid, svg=None):
    svg = svg if svg is not None else SVG_XADREZ
    corpo = (f'<h1 style="font-size:120px;font-weight:600;line-height:1;letter-spacing:2px;'
             f'width:1120px;white-space:nowrap">MUITO OBRIGADA!</h1>\n'
             f'<div style="display:flex;align-items:center;gap:40px">'
             f'<img src="{blob(KA_ESCURO)}" alt="KA Inteligência para Marcas" '
             f'style="width:390px;height:124px;object-fit:contain">'
             f'<div style="width:2px;height:110px;background:{CARAMELO}"></div>'
             f'<img src="{blob(VM_ESCURO)}" alt="VM Rocks Design" '
             f'style="width:300px;height:86px;object-fit:contain"></div>\n'
             f'<div style="position:absolute;left:1292px;top:280px;width:520px;height:500px">'
             f'{svg}</div>')
    return secao(sid, corpo, pad='108px', just='center', align='flex-start', gap=64)

def gravar(pasta, sid, html):
    os.makedirs(os.path.join(pasta, 'project/slides'), exist_ok=True)
    open(os.path.join(pasta, 'project/slides', sid + '.html'), 'w').write(html)


def pg_lista(sid, titulo, intro, itens, rod, fecho=None, tam=34, colunas=2, nota=None):
    """Intro, uma lista marcada com a barra caramelo em colunas, e o fecho."""
    por = (len(itens) + colunas - 1) // colunas
    larg = (W - 64 * (colunas - 1)) // colunas
    cols = ''
    for c in range(colunas):
        bloco = itens[c * por:(c + 1) * por]
        linhas = ''.join(
            f'<p style="font-size:{tam}px;font-weight:300;line-height:1.35;text-align:left;'
            f'width:{larg}px"><span style="color:{CARAMELO}">|</span> {b(i)}</p>'
            for i in bloco)
        cols += (f'<div style="width:{larg}px;display:flex;flex-direction:column;gap:14px">'
                 f'{linhas}</div>')
    interno = ''
    if intro:
        interno += par(intro, tam=tam, lh=1.45) + '\n'
    interno += f'<div style="display:flex;gap:64px;width:{W}px">{cols}</div>'
    if fecho:
        interno += '\n' + filete() + '\n' + par(fecho, tam=tam, lh=1.45)
    return secao(sid, cabeca(titulo) + '\n' + miolo(interno, gap=28),
                 nota=nota, rodape_html=rod)


def pg_chips(sid, titulo, intro, chips, rod, fecho=None, tam=34, nota=None):
    """Intro, uma fileira de pílulas curtas e o fecho."""
    cs = ''.join(
        f'<div style="flex:1;display:flex;justify-content:center;background:{PAPEL2};'
        f'padding:28px 20px;border-radius:52px">'
        f'<p style="font-size:30px;font-weight:500;line-height:1.2;text-align:center;'
        f'letter-spacing:2px;white-space:nowrap">{c}</p></div>' for c in chips)
    interno = ''
    if intro:
        interno += par(intro, tam=tam, lh=1.45) + '\n'
    interno += f'<div style="display:flex;gap:20px;width:{W}px">{cs}</div>'
    if fecho:
        interno += '\n' + par(fecho, tam=tam, lh=1.45)
    return secao(sid, cabeca(titulo) + '\n' + miolo(interno, gap=36),
                 nota=nota, rodape_html=rod)


def pg_manifesto(sid, linhas, rod_claro, assinatura=None, tam=44, nota=None):
    """Página de manifesto: marinho, as linhas respiradas, a assinatura no fim."""
    corpo = f'<div style="width:{W}px;height:3px;background:{CARAMELO_CLARO}"></div>\n'
    corpo += '\n'.join(
        f'<p style="font-size:{tam}px;font-weight:300;line-height:1.35;text-align:left;'
        f'width:{W}px;color:{PAPEL}">{b(l)}</p>' for l in linhas)
    if assinatura:
        corpo += (f'\n<p style="font-size:26px;font-weight:600;letter-spacing:5px;'
                  f'color:{CARAMELO_CLARO};width:{W}px;line-height:1.3;'
                  f'padding:16px 0px 0px">{assinatura}</p>')
    return secao(sid, corpo, fundo=MARINHO, cor=PAPEL, just='center', align='flex-start',
                 gap=24, nota=nota, rodape_html=rod_claro)


# O desenho do fecho: tabuleiro em traco tecnico, do universo do cliente.
SVG_XADREZ = '''<svg aria-label="Desenho em traço fino: tabuleiro de xadrez com peças, cotas e um detalhe ampliado" width="520" height="500" viewBox="0 0 560 540" xmlns="http://www.w3.org/2000/svg" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="20" y1="470" x2="540" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><rect x="70" y="400" width="420" height="70" fill="#eeece4" stroke="#152535" stroke-width="2.5"/><line x1="140" y1="400" x2="140" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><line x1="210" y1="400" x2="210" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><line x1="280" y1="400" x2="280" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><line x1="350" y1="400" x2="350" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><line x1="420" y1="400" x2="420" y2="470" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><line x1="70" y1="435" x2="490" y2="435" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><path d="M140,400 L140,384 L148,378 L148,360 L138,346 L142,268 L132,252 L132,236 L156,236 L156,218 L148,218 L148,198 L170,198 L170,182 L196,182 L196,198 L218,198 L218,218 L210,218 L210,236 L234,236 L234,252 L224,268 L228,346 L218,360 L218,378 L226,384 L226,400 Z" fill="#f8f7f2" stroke="#152535" stroke-width="2.5"/><line x1="138" y1="346" x2="228" y2="346" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><path d="M158,166 L183,142 L208,166" stroke="#d86f2a" stroke-width="2.5"/><line x1="183" y1="142" x2="183" y2="182" stroke="#d86f2a" stroke-width="2.5"/><path d="M320,400 L320,386 L328,380 L328,340 L318,326 L322,290 L312,278 L312,264 L380,264 L380,278 L370,290 L374,326 L364,340 L364,380 L372,386 L372,400 Z" fill="#f8f7f2" stroke="#152535" stroke-width="2.5"/><circle cx="346" cy="236" r="28" fill="#f8f7f2" stroke="#152535" stroke-width="2.5"/><circle cx="470" cy="236" r="72" stroke="#152535" stroke-opacity="0.45" stroke-width="1.5"/><path d="M442,246 L462,266 L500,218" stroke="#d86f2a" stroke-width="3"/><line x1="398" y1="236" x2="418" y2="236" stroke="#152535" stroke-opacity="0.25" stroke-width="1.5" stroke-dasharray="3 6"/><line x1="70" y1="496" x2="490" y2="496" stroke="#d86f2a" stroke-width="1.5"/><line x1="65" y1="501" x2="75" y2="491" stroke="#d86f2a" stroke-width="1.5"/><line x1="485" y1="501" x2="495" y2="491" stroke="#d86f2a" stroke-width="1.5"/><line x1="70" y1="478" x2="70" y2="502" stroke="#d86f2a" stroke-width="1.5"/><line x1="490" y1="478" x2="490" y2="502" stroke="#d86f2a" stroke-width="1.5"/></svg>'''
