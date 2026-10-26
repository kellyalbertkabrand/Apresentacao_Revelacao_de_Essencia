# -*- coding: utf-8 -*-
"""
CULTURA ORGANIZACIONAL — FORMA e My Home

Só conteúdo. Identidade, grade, paleta e escala são as de sempre
(padrao-ka/ka_layout.py e padrao-ka/ka_paginas.py): painel claro sobre a
textura de ondas, Outfit, acento terracota.

A Kelly pediu **o mais visual possível**. No padrão KA isso não significa
encher a página de caixas — significa usar os arquétipos que carregam a
ideia na forma, e deixar o parágrafo corrido só onde ele é mesmo necessário.
Aqui a conta ficou assim:

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` | a virada de tema em **tela cheia de imagem**: numeral, nome em 94pt e um filete que atravessa | 5 |
| `declaracao` | a página de silêncio: uma frase, muito ar | 6 |
| `camadas` | rótulo e leitura lado a lado — valores e a tabela do futuro | 2 |
| `colunas` | os três comportamentos, em paralelo | 1 |
| `lista` | a cultura nas pequenas decisões | 1 |
| `foto_cheia` | o princípio cultural, em tela cheia | 1 |
| `texto` | só onde o conteúdo é mesmo narrativa | 4 |

Das 15 páginas do roteiro dela saem 26: os cinco "ABERTURA DO TEMA" viram
divisores de verdade, e cada frase-tese que ela escreveu em negrito ganha a
sua própria página de silêncio em vez de ficar empilhada embaixo do
parágrafo. É a regra de sempre — um título e um bloco por página — levada ao
limite visual.

Quatro observações, assinaladas e não silenciosas:

1. **A cultura organizacional é das DUAS empresas, juntas.** Forma e My
   Home dividem a mesma cultura — é a Cultura de *Marca* que se separa em
   duas apresentações, não esta. Por isso as duas aparecem nomeadas na capa
   e o texto fala sempre no plural ("as duas empresas acreditam", "a Forma e
   a My Home não se limitam ao problema"), nunca "a empresa" no singular. Na
   primeira passagem para terceira pessoa o singular entrou sem querer e
   apagou a My Home do documento; está corrigido.
2. **A voz é de terceira pessoa.** O roteiro veio em primeira pessoa do
   plural ("nossa origem", "assumimos responsabilidade", "mudar nossa
   essência") e a Kelly pediu para tirar. Em documento de cultura isso não é
   preciosismo: na primeira pessoa o texto só funciona lido de dentro, e o
   mesmo documento precisa servir para apresentar a cultura a um sócio, a um
   candidato ou a um parceiro. Em terceira pessoa ele afirma; na primeira,
   ele desabafa. O conteúdo é o dela — o que mudou foi quem fala.
3. O documento trazia **dois sumários**: um de capa e o do SLIDE 02. Valeu o
   do slide 02, que é o que está dentro da apresentação.
4. Os nomes citados no slide 09 — Letícia, Mapinha e Joel — ficaram como ela
   escreveu. Se a apresentação for para a equipe inteira, vale conferir se
   todos topam ser citados.

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela: a área exata que a foto vai ocupar, com o briefing do que
entra ali. Quando o arquivo entrar em `assets/` com o nome declarado em
`foto`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py cultura
"""

MARCA = "FORMA e My Home"
DOCUMENTO = "Cultura Organizacional"
RODAPE = False
ARQUIVO = "Cultura-Organizacional-Forma-e-My-Home"

IMG = {
    # as cinco viradas de tema — e onde a fotografia rende mais, porque a
    # pagina inteira e dela e nao disputa com texto nenhum
    "div1": "cultura-div-origem.png",
    "div2": "cultura-div-valores.png",
    "div3": "cultura-div-jeito-de-trabalhar.png",
    "div4": "cultura-div-pratica.png",
    "div5": "cultura-div-futuro.png",

    "origem": "cultura-oficina-forma.png",
    "lideranca": "cultura-flavia-equipe.png",
    "relacoes": "cultura-equipe-conversa.png",
    "praticas": "cultura-maos-trabalho.png",
    "principio": "cultura-time-completo.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    # ——————————————————————————————————————————— 01 CAPA
    {"tipo": "capa",
     "titulo": ["O QUE DEFINE", "A FORMA E A MY HOME"],
     "subtitulo": ["Cultura Organizacional", "FORMA e My Home"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["O que conecta as duas empresas,",
                "como elas trabalham",
                "e o que precisa ser preservado no crescimento."]},

    # ——————————————————————————————————————————— 02 SUMÁRIO
    {"tipo": "sumario", "titulo": "A cultura", "itens": [
        ("01", "A origem", "De onde vem o jeito de pensar."),
        ("02", "Os valores",
         "Aquilo em que as duas empresas acreditam e como lideram."),
        ("03", "O jeito de trabalhar",
         "Os comportamentos e as relações que definem as duas."),
        ("04", "A cultura na prática",
         "Como as crenças aparecem no dia a dia."),
        ("05", "O futuro", "O que preservar e o que desenvolver."),
    ]},

    # ═══════════════════════════════════════════ 01 NOSSA ORIGEM
    {"tipo": "divisor", "numero": "01", "nome": "A origem",
     "apoio": "De onde vem o jeito de pensar.",
     "foto": IMG["div1"],
     "imagem": "A origem do ofício: a primeira oficina, uma foto antiga da "
               "Flávia trabalhando, ou o lugar onde tudo começou."},

    {"tipo": "texto", "foto": IMG["origem"], "lado": "direita",
     "imagem": "A oficina da FORMA em trabalho — marcenaria, máquina, "
               "material, mãos. O ofício, não o retrato.",
     "titulo": "Não aceitar o limite como resposta definitiva.",
     "tam_corpo": 21,
     "paragrafos": [
         "A cultura da Forma e da My Home tem origem na trajetória da Flávia "
         "e em sua capacidade de encontrar alternativas diante das "
         "limitações.",
         "Essa mentalidade ultrapassou sua história pessoal e passou a "
         "influenciar as empresas e as pessoas que trabalham nelas.",
         "O que nasceu como uma característica da fundadora tornou-se um "
         "jeito coletivo de enfrentar desafios.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Diante de uma dificuldade,",
                "a Forma e a My Home não se limitam ao problema.",
                "Procuram possibilidades para resolvê-lo."],
     "apoio": "A crença de origem."},

    # ═══════════════════════════════════════════ 02 NOSSOS VALORES
    {"tipo": "divisor", "numero": "02", "nome": "Os valores",
     "apoio": "Aquilo em que as duas empresas acreditam e como lideram.",
     "foto": IMG["div2"],
     "imagem": "Alguém da equipe concentrado no trabalho — o cuidado "
               "aparecendo na mão e no olhar. Plano fechado."},

    {"tipo": "camadas",
     "titulo": "Liberdade para agir. Responsabilidade para entregar.",
     "camadas": [
         ("Comprometimento",
          "Responsabilidade pelo resultado, não apenas pela tarefa."),
         ("Autonomia", "Liberdade para propor, decidir e solucionar."),
         ("Excelência",
          "Nada é entregue quando ainda pode ser melhor."),
         ("Cooperação", "O resultado depende do trabalho de todos."),
         ("Evolução",
          "Aprender, melhorar e ampliar as possibilidades."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Não basta saber fazer.",
                "É preciso se envolver para fazer acontecer."],
     "apoio": "A crença central."},

    {"tipo": "texto", "foto": IMG["lideranca"], "lado": "esquerda",
     "imagem": "Flávia com a equipe, em conversa de trabalho — chão de "
               "fábrica, mesa ou obra. Liderança próxima, não retrato "
               "posado.",
     "titulo": "Proximidade que acolhe. Confiança que dá autonomia.",
     "tam_corpo": 21,
     "paragrafos": [
         "As entrevistas revelam uma liderança reconhecida pela "
         "acessibilidade, pelo conhecimento técnico e pela exigência com os "
         "resultados.",
         "A Flávia construiu relações próximas, nas quais as pessoas "
         "encontram espaço para conversar, aprender e agir.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Seu maior legado cultural não está apenas",
                "naquilo que ela realiza, mas na maneira",
                "como incentiva outras pessoas a realizar."],
     "apoio": "O desafio é fazer com que esses princípios sejam "
              "compartilhados pelas futuras lideranças."},

    # ═══════════════════════════════════ 03 NOSSO JEITO DE TRABALHAR
    {"tipo": "divisor", "numero": "03", "nome": "O jeito de trabalhar",
     "apoio": "Os comportamentos e as relações que definem as duas.",
     "foto": IMG["div3"],
     "imagem": "A oficina em movimento, com várias pessoas trabalhando ao "
               "mesmo tempo. Plano aberto, o coletivo em ação."},

    {"tipo": "colunas",
     "titulo": "O problema não deixa de importar porque começou em outro "
               "lugar.",
     "colunas": [
         ("Resolver", "Tomar iniciativa diante dos desafios."),
         ("Cuidar", "Não aceitar uma entrega abaixo do padrão esperado."),
         ("Colaborar",
          "Ajudar outras pessoas e áreas para alcançar o resultado."),
     ],
     "fecho": "Letícia relata correções feitas pela própria equipe, Mapinha "
              "descreve peças refeitas por não atenderem ao padrão e Joel "
              "destaca o envolvimento com problemas que afetam o cliente, "
              "mesmo quando surgem de terceiros. A responsabilidade vai "
              "além da execução individual: alcança o resultado construído "
              "em conjunto."},

    {"tipo": "texto", "foto": IMG["relacoes"], "lado": "direita",
     "imagem": "Duas ou três pessoas da equipe conversando no trabalho — "
               "proximidade real, sem pose. Pode ser um momento de pausa.",
     "titulo": "A proximidade é uma força nas duas empresas.",
     "tam_corpo": 21,
     "paragrafos": [
         "As pessoas descrevem um ambiente marcado por acolhimento, "
         "confiança e facilidade de acesso à liderança.",
         "A união não aparece apenas como sentimento. Ela facilita a "
         "comunicação, a colaboração e a resolução de problemas.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["O diferencial não é trabalhar como uma família,",
                "mas construir relações humanas em que as pessoas",
                "se sintam respeitadas e responsáveis",
                "umas pelas outras."],
     "apoio": "O crescimento deve preservar esse vínculo, sem abrir mão do "
              "profissionalismo e da clareza de responsabilidades."},

    # ═══════════════════════════════ 04 NOSSA CULTURA NA PRÁTICA
    {"tipo": "divisor", "numero": "04", "nome": "A cultura na prática",
     "apoio": "Como as crenças aparecem no dia a dia.",
     "foto": IMG["div4"],
     "imagem": "Uma montagem na casa do cliente, ou a equipe protegendo o "
               "ambiente antes de começar. O cuidado em ato."},

    {"tipo": "lista", "titulo": "A cultura aparece nas pequenas decisões.",
     "itens": [
         "Uma peça é refeita porque não ficou boa.",
         "Um colaborador resolve um problema sem esperar uma ordem.",
         "A equipe protege e cuida da casa do cliente.",
         "Colegas de diferentes áreas se ajudam.",
         "A liderança mantém o diálogo aberto.",
         "Os encontros e as celebrações fortalecem os vínculos.",
     ],
     "marcar_ultimo": True,
     "fecho": "O que conecta essas atitudes é a combinação de "
              "responsabilidade com o trabalho e cuidado com as pessoas. É "
              "assim que valores deixam de ser palavras e se transformam em "
              "cultura."},

    # ═══════════════════════════════════════════ 05 NOSSO FUTURO
    {"tipo": "divisor", "numero": "05", "nome": "O futuro",
     "apoio": "O que preservar e o que desenvolver.",
     "foto": IMG["div5"],
     "imagem": "Um ambiente entregue, pronto e em uso — o resultado. Ou a "
               "fachada/expansão das empresas. Imagem de horizonte."},

    {"tipo": "camadas",
     "titulo": "Crescer sem perder o que torna estas empresas diferentes.",
     "cabecalhos": ("O que preservar", "O que desenvolver"),
     "camadas": [
         ("Proximidade",
          "Lideranças capazes de manter os mesmos princípios."),
         ("Autonomia", "Critérios e responsabilidades compartilhados."),
         ("Agilidade", "Processos que evitem problemas recorrentes."),
         ("Excelência", "Padrões que possam ser ensinados e reproduzidos."),
         ("Cooperação", "Integração com papéis claros entre as operações."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["O desafio não é mudar a essência.",
                "É fazer com que ela continue presente",
                "quando as empresas crescerem",
                "e novas pessoas chegarem."]},

    {"tipo": "texto", "foto": IMG["praticas"], "lado": "esquerda",
     "imagem": "O trabalho acontecendo: mãos, ferramenta, acabamento, "
               "montagem. Detalhe fechado, sem rosto.",
     "titulo": "Uma cultura que se constrói com pessoas e se comprova nas "
               "entregas.",
     "tam_corpo": 21,
     "paragrafos": [
         "A Forma e a My Home compartilham uma cultura de proximidade, "
         "autonomia e responsabilidade.",
         "Uma cultura em que as pessoas são incentivadas a encontrar "
         "soluções, colaborar e buscar o melhor resultado possível.",
     ]},

    {"tipo": "foto_cheia", "foto": IMG["principio"],
     "imagem": "O time completo das duas operações. Imagem ampla, que "
               "aguente a frase por cima.",
     # quebrado em linhas curtas de propósito: o motor dimensiona a frase
     # pela linha mais longa, e assim o princípio entra grande, como a
     # última página pede
     "linhas": ["Liberdade para encontrar caminhos.",
                "Responsabilidade pelo que",
                "se constrói em conjunto."],
     "apoio": "O princípio cultural das duas marcas. Uma cultura "
              "organizacional compartilhada."},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
