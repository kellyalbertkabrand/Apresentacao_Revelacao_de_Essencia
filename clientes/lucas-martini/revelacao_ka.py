# -*- coding: utf-8 -*-
"""Revelação de Essência · Lucas José Martini — no Padrão KA de apresentações.
O texto é o da Kelly, transcrito; o que muda é a diagramação."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../../padrao-ka/paginas-html'))
from ka_gerador import *

PASTA = os.environ.get('KA_SAIDA', 'rev-ka')
ROT, MARCA = 'REVELAÇÃO DE ESSÊNCIA', 'LUCAS MARTINI'
rod = rodape(ROT, MARCA)
rodc = rodape(ROT, MARCA, claro=True)

F_JOVEM = '04_jovem_colete_vermelho_caixa_eletronico.png'
F_JANELA = '03_lucas_janela_entardecer.png'
F_DOCS = '09_lucas_analisando_documentos.png'
F_CASAL = '02_reuniao_consultiva_casal.png'
F_RETRATO = '01_retrato_corporativo_prudential.png'
F_MAOS = '08_lucas_aperto_de_maos_cliente.png'
F_CAMINHA = '12_lucas_caminhando_janela.png'
F_CONSULTA = '11_lucas_consulta_individual.png'
F_SALA = '10_lucas_sala_reuniao.png'


paginas = []
def add(sid, html): paginas.append(sid); gravar(PASTA, sid, html)

add('abertura', pg_abertura('abertura'))

add('capa', pg_capa('capa', ['REVELAÇÃO DE', '**ESSÊNCIA**'],
    '**Lucas José Martini** Origem Identitária do Fundador',
    nota='Revelação de Essência de Lucas José Martini, primeira etapa do Método '
         'Marca com Essência©.'))

add('sumario', pg_sumario('sumario', [
    'A origem', 'As tensões', 'Os padrões',
    'O Ikigai', 'A essência', 'Da essência à atuação'], rod, pad_linha=30))

add('porque', pg_frase('porque', None,
    'POR QUE A ESSÊNCIA<br>**VEM PRIMEIRO?**', None, rodc, foto=F_RETRATO, tam=92,
    nota='A pergunta que abre o documento.'))

add('conceito', pg_texto('conceito', 'O QUE A REVELAÇÃO **INVESTIGA**', [
    '**Uma marca pessoal não começa naquilo que o profissional vende.** Começa na maneira '
    'como ele enxerga o mundo, toma decisões e atribui significado ao próprio trabalho.',
    'Proteção e sucessão são a parte mais visível da sua atuação. A Revelação de Essência '
    'existe para ir além dessa superfície.',
    'Não se trata de uma análise psicológica, mas de investigar os padrões, crenças e tensões '
    'que ajudam a explicar de onde vem a forma como você pensa, decide, trabalha e se '
    'relaciona com seus clientes.',
    '**O que, na sua trajetória, ajuda a explicar a forma como você atua hoje?**'],
    rod, tam=36))

add('trajetoria', pg_frase('trajetoria', None,
    'É NA SUA TRAJETÓRIA QUE APARECEM OS PADRÕES QUE FORMAM A SUA **ESSÊNCIA**.',
    None, rodc, foto=F_CAMINHA, tam=68))

add('metodo', pg_camadas('metodo', 'COMO A REVELAÇÃO É **CONSTRUÍDA**', [
    ('HISTÓRIA', 'O que ajudou a formar sua visão de mundo.'),
    ('TENSÕES', 'Os contrastes que mostram aquilo que realmente importa.'),
    ('PADRÕES', 'A forma recorrente como Lucas responde.'),
    ('IKIGAI', 'Onde competência, realização, contribuição e profissão se encontram.')],
    rod, larg_rotulo=320,
    intro='A essência não é um adjetivo, nem uma frase bonita criada para comunicação. '
          'Ela aparece quando momentos aparentemente diferentes revelam uma mesma lógica.',
    fecho='história + tensões + padrões + Ikigai = **essência**'))

# ---------------------------------------------------------------- 01 origem
add('d1', pg_divisor('d1', '01', 'A ORIGEM',
    'As experiências que ajudaram a formar sua visão sobre segurança, responsabilidade e futuro.',
    F_JOVEM, ROT, MARCA, nota='Lucas no início da carreira, no atendimento bancário.'))

add('origem1', pg_chips('origem1', 'ONDE COMEÇA SUA RELAÇÃO COM **SEGURANÇA**',
    'Você não viveu as mesmas dificuldades que seus pais enfrentaram, mas cresceu conhecendo a '
    'história de uma família que saiu do campo, passou por escassez, trabalhou e construiu uma '
    'nova base de vida. Essa trajetória ajuda a explicar por que segurança, patrimônio e '
    'estabilidade nunca aparecem para você como algo simplesmente garantido.',
    ['CASA', 'RENDA', 'PATRIMÔNIO', 'CARREIRA', 'EMPRESA', 'ESTABILIDADE'], rod,
    fecho='Tudo isso leva tempo para ser construído. E o valor não está apenas no que foi '
          'conquistado, **mas em tudo o que foi necessário para chegar até ali.**'))

add('origem2', pg_texto('origem2', 'O SEGUNDO **APRENDIZADO**', [
    'Sua trajetória no Bradesco começou no atendimento, ainda muito jovem, em contato direto '
    'com as pessoas e suas necessidades do dia a dia.',
    'Anos depois, já na recuperação de ativos, você passou a ver o outro lado dessa realidade: '
    'famílias e empresas que levaram anos construindo patrimônio entravam rapidamente em '
    'dificuldade diante de morte, doença ou sucessão mal planejada.',
    '**Um dos seus primeiros grandes aprendizados não foi sobre seguro, mas sobre fragilidade.** '
    'O que leva anos para ser construído pode ser comprometido muito rapidamente.'],
    rod, tam=36))

add('origem3', pg_lista('origem3', 'O QUE ESSA EXPERIÊNCIA **MOSTROU**',
    'Ao acompanhar situações de recuperação de ativos, você passou a perceber que a fragilidade '
    'não estava apenas na perda financeira. Ela aparecia quando:', [
    'uma renda parava;', 'uma empresa perdia uma pessoa essencial;',
    'um patrimônio precisava ser desfeito;',
    'uma família perdia parte da estrutura que sustentava sua vida.'],
    rod, fecho='**O imprevisto não compromete apenas dinheiro.** Ele pode reduzir escolhas '
               'e possibilidades.'))

# ---------------------------------------------------------------- 02 tensões
add('d2', pg_divisor('d2', '02', 'AS TENSÕES',
    'Os contrastes que ajudaram a revelar o que realmente importa para você.',
    F_JANELA, ROT, MARCA, nota='Lucas diante da janela, ao entardecer.'))

add('tensao1', pg_texto('tensao1',
    f'PRIMEIRA TENSÃO <span style="color:{CARAMELO}">|</span> SEGURANÇA × **RISCO**', [
    'Hoje você constrói segurança para outras pessoas. Mas, num momento decisivo da própria '
    'carreira, abriu mão de uma trajetória sólida no banco para empreender.',
    'Você aceita correr riscos quando pode escolher, se preparar e assumir as consequências. '
    'O que incomoda é quando um imprevisto tira essa possibilidade.',
    '**Segurança, para você, é ter margem de escolha mesmo quando algo sai do previsto.**'],
    rod, tam=38))

add('tensao2', pg_texto('tensao2',
    f'SEGUNDA TENSÃO <span style="color:{CARAMELO}">|</span> DINHEIRO × **PROPÓSITO**', [
    'Você não romantiza a própria decisão: a possibilidade financeira pesou. Mas resume a '
    'trajetória com uma frase reveladora — “fui pelo dinheiro e acabei ficando pelo propósito”.',
    'Esse propósito ganhou força quando você passou a acompanhar pagamentos de benefícios e '
    'enxergar, na prática, o impacto de uma proteção estruturada antes do imprevisto.',
    'Resultado, crescimento e reconhecimento continuam sendo importantes. Mas, com o tempo, '
    'o impacto do trabalho também passou a dar sentido à trajetória.',
    '**O dinheiro explica a entrada. O propósito ajuda a explicar por que você ficou.**'],
    rod, tam=34))

add('tensao3', pg_texto('tensao3',
    f'TERCEIRA TENSÃO <span style="color:{CARAMELO}">|</span> RECONHECIMENTO × **EXPOSIÇÃO**', [
    'Você acumula reconhecimentos e valoriza estar entre os melhores, mas ainda encontra '
    'dificuldade em comunicar essas conquistas.',
    'O ponto não parece estar no reconhecimento em si, mas em falar sobre ele. Quando o '
    'reconhecimento vem de clientes, da companhia ou de rankings, ele é recebido com '
    'naturalidade. O desconforto aparece quando é você quem precisa destacar o que conquistou.',
    '**Na sua trajetória, a legitimidade parece ter mais valor quando é construída e '
    'reconhecida pelos outros do que quando precisa ser afirmada por você mesmo.**'],
    rod, tam=34))

add('revela', pg_frase('revela', 'O QUE ISSO REVELA',
    'ALTA PERFORMANCE.<br>**BAIXA EXPOSIÇÃO.**',
    'Você construiu uma trajetória de resultados, reconhecimento e autoridade, mas ainda '
    'comunica pouco sobre isso. O ponto não é se tornar alguém excessivamente exposto ou '
    'promocional, e sim **tornar mais visível a autoridade que já existe** — uma autoridade '
    'discreta, mas presente.', rodc, foto=F_CONSULTA, tam=76))

# ---------------------------------------------------------------- 03 padrões
add('d3', pg_divisor('d3', '03', 'OS PADRÕES',
    'O que se repete, mesmo quando as escolhas mudam.',
    F_DOCS, ROT, MARCA, nota='Lucas analisando documentos.'))

add('padroes', pg_camadas('padroes', 'O QUE SE **REPETE**', [
    ('SE ANTECIPAR', 'Quando algo é importante, você busca entender, estudar, organizar e '
                     'estruturar antes. Essa forma de agir aparece em diferentes momentos '
                     'da sua trajetória.'),
    ('FAZER COM CONSISTÊNCIA', 'Você começou cedo, cresceu dentro do banco, depois recomeçou '
                               'no empreendedorismo, construiu sua carteira e manteve '
                               'consistência ao longo do tempo.'),
    ('PERMANECER PRESENTE', 'Sua atuação não termina na venda. Relacionamento, confiança e '
                            'pós-venda fazem parte da forma como você constrói e mantém '
                            'essa relação com o cliente.')],
    rod, larg_rotulo=460, tam=34, pad=34))

# ---------------------------------------------------------------- 04 ikigai
add('d4', pg_divisor('d4', '04', 'O IKIGAI',
    'Onde competência, realização profissional e impacto se encontram.',
    F_CASAL, ROT, MARCA, nota='Reunião consultiva com um casal.'))

add('ikigai', pg_camadas('ikigai', 'OS QUATRO **ENCONTROS**', [
    ('PAIXÃO<br>O QUE AMA + NO QUE É BOM',
     'Conversar, compreender e construir soluções que façam sentido para cada realidade.'),
    ('PROFISSÃO<br>NO QUE É BOM + PELO QUE PODE SER PAGO',
     'Estruturar proteção e sucessão com visão consultiva, personalização e relacionamento.'),
    ('MISSÃO<br>O QUE O MUNDO PRECISA + O QUE GOSTA DE FAZER',
     'Ampliar a consciência de que preparação financeira também é uma forma de cuidado '
     'e responsabilidade.'),
    ('VOCAÇÃO<br>O QUE O MUNDO PRECISA + PELO QUE PODE SER PAGO',
     'Ajudar pessoas, famílias e empresas a chegarem mais preparadas aos momentos que '
     'não podem controlar.')],
    rod, larg_rotulo=620, tam=32, tam_rot=24, pad=26,
    fecho='Sua competência não é conhecer produtos — é **transformar complexidade em '
          'decisão estruturada.**'))

add('realizacao', pg_texto('realizacao', 'ONDE VOCÊ ENCONTRA **REALIZAÇÃO**', [
    'A realização aparece quando o planejamento cumpre o papel para o qual foi criado: '
    'um benefício é pago, uma família mantém sua estrutura, uma empresa consegue continuar.',
    '**É nesse momento que a proteção deixa de ser apenas planejamento e passa a preservar '
    'possibilidades.**',
    'Dignidade financeira, para você, é isso: evitar que um imprevisto obrigue alguém a '
    'desmontar o que construiu ou tomar decisões sem alternativas.'],
    rod, tam=36))

add('razao', pg_frase('razao', 'RAZÃO DE SER',
    'PRESERVAR A LIBERDADE DE ESCOLHA **QUANDO A VIDA FOGE DO PREVISTO.**',
    None, rodc, foto=F_SALA, tam=68))

# ---------------------------------------------------------------- 05 essência
add('d5', pg_divisor('d5', '05', 'A ESSÊNCIA',
    'O princípio mais profundo que conecta sua trajetória.',
    F_RETRATO, ROT, MARCA, nota='Retrato corporativo de Lucas Martini.'))

add('encontro', pg_camadas('encontro', 'ONDE TUDO SE **ENCONTRA**', [
    ('A ORIGEM', 'Sua história mostrou que segurança é construída.'),
    ('O BANCO', 'Sua experiência mostrou como aquilo que leva anos para existir pode se '
                'fragilizar rapidamente.'),
    ('O EMPREENDEDORISMO', 'Sua trajetória mostrou que assumir riscos faz parte, desde que '
                           'exista decisão e preparo.'),
    ('A PROFISSÃO', 'Mostrou que preparação preserva possibilidades.'),
    ('A CRENÇA FUNDADORA', 'O que levou anos para ser construído não deveria ficar '
                           'entregue ao acaso.')],
    rod, larg_rotulo=480, tam=32, tam_rot=26, pad=26))

add('essencia', pg_frase('essencia', 'A ESSÊNCIA DE LUCAS',
    'CONSTRUIR SEGURANÇA PARA PRESERVAR **LIBERDADE DE ESCOLHA.**',
    'Lucas não trabalha para controlar o imprevisto. Trabalha para que o imprevisto não '
    'decida sozinho o que vem depois.', rodc, tam=94,
    nota='A frase-essência, o centro do documento.'))

add('frase', pg_camadas('frase', 'O QUE A FRASE **CARREGA**', [
    ('CONSTRUIR SEGURANÇA',
     'Transformar vulnerabilidades em planejamento, recursos e alternativas.'),
    ('PRESERVAR LIBERDADE',
     'Manter possibilidades diante de acontecimentos que fogem ao controle.'),
    ('ESCOLHA',
     'Evitar que a urgência seja a única responsável pelas decisões.')],
    rod, larg_rotulo=460, tam=34, pad=34,
    fecho='Responsável, disciplinado, ambicioso e constante são características do Lucas. '
          'Mas são manifestações de uma lógica mais profunda: **preparar o que pode ser '
          'preparado para proteger o que não pode ser previsto.**'))

# ---------------------------------------------------------- 06 da essência à atuação
add('d6', pg_divisor('d6', '06', ['DA ESSÊNCIA', 'À ATUAÇÃO'],
    'O que essa essência revela sobre o lugar que a marca pode ocupar.',
    F_MAOS, ROT, MARCA, nota='Aperto de mãos com um cliente.'))

add('atuacao', pg_texto('atuacao', 'PROVA, NÃO **PROCLAMAÇÃO**', [
    'Você não precisa se comunicar de um jeito que não combina com você.',
    'A construção da sua marca pode partir do que já existe na sua trajetória: resultados, '
    'casos, conhecimento, reconhecimentos e consistência.',
    'O ponto não é se expor mais por se expor. É tornar mais visível a autoridade que você '
    'já construiu.',
    '**A essência explica de onde você vem. A estratégia define para onde sua marca pode ir.**'],
    rod, tam=36))

add('obrigada', pg_obrigada('obrigada'))

deck = {
    'v': 4,
    'createdOnFiles': {'v': 1, 'at': '2026-11-11T21:00:00Z'},
    'lists': 'css',
    'title': 'Revelação de Essência · Lucas José Martini',
    'cover': 'capa',
    'order': paginas,
    'sections': {
        's0': {'description': 'Abertura, capa, sumário e o método da Revelação.',
               'start': 'abertura'},
        's1': {'description': 'A origem: segurança, fragilidade e o aprendizado do banco.',
               'start': 'd1'},
        's2': {'description': 'As três tensões e o que elas revelam.', 'start': 'd2'},
        's3': {'description': 'Os padrões que se repetem.', 'start': 'd3'},
        's4': {'description': 'O Ikigai e a razão de ser.', 'start': 'd4'},
        's5': {'description': 'A essência e o que a frase carrega.', 'start': 'd5'},
        's6': {'description': 'Da essência à atuação.', 'start': 'd6'},
    },
    'faces': {'outfit': {'family': 'Outfit',
              'href': 'https://fonts.googleapis.com/css2?family=Outfit:wght@200..800&display=swap'}},
}
os.makedirs(PASTA + '/project', exist_ok=True)
json.dump(deck, open(PASTA + '/project/deck.json', 'w'), ensure_ascii=False, indent=2)
print(len(paginas), 'paginas')
