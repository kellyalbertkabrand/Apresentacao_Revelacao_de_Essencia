# -*- coding: utf-8 -*-
"""Base Estratégica da Marca · Lucas Martini — no Padrão KA de apresentações."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../../padrao-ka/paginas-html'))
from ka_gerador import *

PASTA = os.environ.get('KA_SAIDA', 'bas-ka')
ROT, MARCA = 'BASE ESTRATÉGICA', 'LUCAS MARTINI'
rod = rodape(ROT, MARCA)
rodc = rodape(ROT, MARCA, claro=True)
CAR = f'<span style="color:{CARAMELO}">|</span>'

F_RETRATO = '01_retrato_corporativo_prudential.png'
F_JANELA = '03_lucas_janela_entardecer.png'
F_CASAL = '02_reuniao_consultiva_casal.png'
F_SALA = '10_lucas_sala_reuniao.png'


paginas = []
def add(sid, html): paginas.append(sid); gravar(PASTA, sid, html)

add('abertura', pg_abertura('abertura'))

add('capa', pg_capa('capa', ['BASE ESTRATÉGICA', '**DA MARCA**'],
    '**Lucas Martini** Proteção &amp; Sucessão',
    nota='Base Estratégica da Marca de Lucas Martini, construída pelo Método '
         'Marca com Essência©.'))

add('sumario', pg_sumario('sumario', [
    'Essência da marca', 'Quem é Lucas Martini', 'Causa, liderança e tribo',
    'Princípio central', 'Público-alvo e persona', 'Arquétipos da marca',
    'Pilares da marca', 'DNA da marca', 'Voz da marca', 'Tom de voz',
    'Posicionamento', 'Golden Circle', 'Arquitetura da marca', 'Manifesto'],
    rod, tam=32, pad_linha=14))

add('essencia', pg_frase('essencia', '01 · ESSÊNCIA DA MARCA',
    'CONSTRUIR SEGURANÇA PARA QUE AS ESCOLHAS **CONTINUEM POSSÍVEIS.**',
    'Nem tudo pode ser previsto. Mas é possível se preparar para que um imprevisto não '
    'elimine alternativas nem comprometa o que levou anos para ser construído.',
    rodc, foto=F_RETRATO, tam=62, nota='A essência que organiza toda a marca.'))

add('quem', pg_texto('quem', f'02 {CAR} QUEM É **LUCAS MARTINI**', [
    '**Especialista em Proteção &amp; Sucessão, com mais de dez anos de atuação.**',
    'Sua experiência no mercado financeiro e a vivência com famílias e empresas deram origem '
    'a uma atuação consultiva, baseada em planejamento, personalização, relacionamento '
    'e acompanhamento.'], rod, tam=40))

add('causa', pg_camadas('causa', f'03 {CAR} CAUSA, LIDERANÇA E **TRIBO**', [
    ('CAUSA', 'Ampliar a cultura de proteção e preparação antes do imprevisto.'),
    ('LIDERANÇA', 'Ajudar pessoas a enxergar riscos, impactos e possibilidades antes que '
                  'a urgência determine as decisões.'),
    ('TRIBO', 'Pessoas que carregam responsabilidade sobre renda, família, patrimônio '
              'ou empresa.')],
    rod, larg_rotulo=340, tam=36, pad=34))

add('principio', pg_frase('principio', '04 · PRINCÍPIO CENTRAL',
    'O QUE LEVOU ANOS PARA SER CONSTRUÍDO **NÃO DEVERIA FICAR ENTREGUE AO ACASO.**',
    'Planejamento é uma forma de proteger conquistas e preservar possibilidades diante '
    'do que não pode ser controlado.', rodc, tam=72))

add('publico', pg_texto('publico', f'05 {CAR} PÚBLICO-ALVO E **PERSONA**', [
    'Profissionais, empresários, sócios e famílias que possuem responsabilidades financeiras, '
    'patrimoniais ou sucessórias e querem proteger o que construíram.',
    '**A persona central é alguém que entende o valor das suas conquistas e quer se preparar '
    'para que um imprevisto não comprometa sua família, seu patrimônio ou sua empresa.**'],
    rod, tam=38))

add('arquetipos', pg_cartoes('arquetipos', f'06 {CAR} ARQUÉTIPOS DA **MARCA**', [
    ('SÁBIO · PRINCIPAL', 'Traduz complexidade, orienta decisões e transforma informação '
                          'em planejamento.'),
    ('CUIDADOR · SECUNDÁRIO', 'Protege, acompanha e assume responsabilidade sobre decisões '
                              'que afetam pessoas, famílias e empresas.')],
    rod, tam=34))

add('pilares', pg_camadas('pilares', f'07 {CAR} PILARES DA **MARCA**', [
    ('PROTEÇÃO', 'Preservar o que foi construído.'),
    ('PLANEJAMENTO', 'Antecipar riscos e criar alternativas.'),
    ('PERSONALIZAÇÃO', 'Construir soluções a partir de cada realidade.'),
    ('CONFIANÇA', 'Sustentar relações de longo prazo.'),
    ('CONTINUIDADE', 'Permitir que família, patrimônio e empresa possam seguir.')],
    rod, larg_rotulo=420, tam=36, pad=30))

add('dna', pg_chips('dna', f'08 {CAR} DNA DA **MARCA**', None,
    ['PROTEÇÃO', 'CONFIANÇA', 'RESPONSABILIDADE', 'PERSONALIZAÇÃO', 'CONTINUIDADE'], rod,
    fecho='Esses são os atributos que devem permanecer presentes em **qualquer expressão '
          'da marca**, do atendimento à comunicação.', tam=38))

add('voz', pg_chips('voz', f'09 {CAR} VOZ DA **MARCA**',
    'A voz de Lucas deve transmitir **conhecimento sem distanciamento** e '
    '**segurança sem arrogância.**',
    ['CLARA', 'SEGURA', 'HUMANA', 'ELEGANTE', 'CONSULTIVA'], rod, tam=38))

add('tom', pg_camadas('tom', f'10 {CAR} TOM DE **VOZ**', [
    ('TÉCNICO', 'sem ser complicado.'),
    ('DIRETO', 'sem ser frio.'),
    ('SEGURO', 'sem ser arrogante.'),
    ('HUMANO', 'sem dramatização.'),
    ('SOFISTICADO', 'sem ostentação.')],
    rod, larg_rotulo=420, tam=38, pad=30))

add('posicionamento', pg_caixa('posicionamento', f'11 {CAR} **POSICIONAMENTO**',
    'A FRASE DE POSICIONAMENTO',
    'PROTEÇÃO &amp; SUCESSÃO PARA O QUE PRECISA **CONTINUAR.**',
    ['Lucas Martini é especialista em Proteção &amp; Sucessão para pessoas, famílias e '
     'empresas que querem preservar o que construíram e manter possibilidades diante de '
     'imprevistos e transições.'], rod, tam_frase=58, tam=36))

add('golden', pg_camadas('golden', f'12 {CAR} GOLDEN **CIRCLE**', [
    ('POR QUÊ', 'Preservar possibilidades quando a vida foge do previsto.'),
    ('COMO', 'Com planejamento personalizado, conhecimento, relacionamento '
             'e acompanhamento.'),
    ('O QUÊ', 'Estratégias de proteção pessoal, familiar, empresarial e sucessória.')],
    rod, larg_rotulo=340, tam=36, pad=34))

add('arquitetura', pg_camadas('arquitetura', f'13 {CAR} ARQUITETURA DA **MARCA**', [
    ('MARCA PESSOAL', 'Lucas Martini'),
    ('ATUAÇÃO', 'Proteção &amp; Sucessão'),
    ('ASSINATURA EMPRESARIAL', 'Martini | Proteção &amp; Sucessão'),
    ('MONOGRAMA', 'LM')],
    rod, larg_rotulo=480, tam=36, pad=28,
    fecho='O uso de “Martini” ganha força porque é a forma pela qual Lucas já é reconhecido '
          'em seu convívio pessoal e profissional.'))

add('manifesto1', pg_manifesto('manifesto1', [
    'Há coisas que levam uma vida inteira para construir.',
    'Uma família. Uma carreira. Uma empresa.<br>Um patrimônio. Uma história.',
    'São anos de trabalho, escolhas e renúncias.',
    'E é justamente por isso que proteger não é pensar no pior.<br>'
    '**É reconhecer o valor de tudo o que deu certo.**'],
    rodc, nota='Manifesto da marca, primeira parte. Único texto do documento em '
               'primeira pessoa — é a convenção do gênero.'))

add('manifesto2', pg_manifesto('manifesto2', [
    'A vida nem sempre avisa quando vai mudar. Mas podemos decidir, enquanto há tempo, '
    'como queremos atravessar essas mudanças.',
    'Para que uma família continue amparada. Uma empresa continue em pé. Um patrimônio '
    'não precise ser desfeito às pressas. E os planos não desapareçam junto com o imprevisto.',
    'Porque não podemos controlar tudo o que acontece.<br>'
    '**Mas podemos proteger aquilo que queremos que continue.**'],
    rodc, assinatura='LUCAS MARTINI &nbsp;|&nbsp; PROTEÇÃO &amp; SUCESSÃO', tam=40,
    nota='Manifesto da marca, segunda parte.'))

add('obrigada', pg_obrigada('obrigada'))

deck = {
    'v': 4,
    'createdOnFiles': {'v': 1, 'at': '2026-11-11T21:00:00Z'},
    'lists': 'css',
    'title': 'Base Estratégica da Marca · Lucas Martini',
    'cover': 'capa',
    'order': paginas,
    'sections': {
        's0': {'description': 'Abertura, capa e sumário.', 'start': 'abertura'},
        's1': {'description': 'Essência, quem é Lucas e a causa da marca.', 'start': 'essencia'},
        's2': {'description': 'Público, arquétipos, pilares e DNA.', 'start': 'publico'},
        's3': {'description': 'Voz, tom, posicionamento e Golden Circle.', 'start': 'voz'},
        's4': {'description': 'Arquitetura da marca e manifesto.', 'start': 'arquitetura'},
    },
    'faces': {'outfit': {'family': 'Outfit',
              'href': 'https://fonts.googleapis.com/css2?family=Outfit:wght@200..800&display=swap'}},
}
os.makedirs(PASTA + '/project', exist_ok=True)
json.dump(deck, open(PASTA + '/project/deck.json', 'w'), ensure_ascii=False, indent=2)
print(len(paginas), 'paginas')
