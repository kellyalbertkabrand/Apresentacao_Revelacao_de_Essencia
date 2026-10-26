# -*- coding: utf-8 -*-
"""
CULTURA DE MARCA — MY HOME

Só conteúdo. Identidade, grade, paleta e escala são as de sempre
(padrao-ka/ka_layout.py e padrao-ka/ka_paginas.py).

O roteiro da Kelly veio como UM documento cobrindo as duas marcas; ela pediu
**duas apresentações separadas**. Esta é a da My Home, na mesma estrutura de
quatro seções da apresentação da Forma — mesma grade, mesma ordem, mesmos
arquétipos. É o que faz as duas serem lidas como irmãs sem serem a mesma
coisa.

As duas últimas páginas antes do fecho são a síntese (slide 13 do roteiro),
que compara as duas marcas. Nesta apresentação ela carrega um ponto que o
próprio conteúdo levanta: a My Home **não deve ser percebida apenas como o
braço operacional da Forma**. Se preferir a My Home sozinha do começo ao
fim, são duas páginas para tirar.

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela. Quando o arquivo entrar em `assets/` com o nome declarado em
`foto`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py marca-my-home
"""

MARCA = "MY HOME"
DOCUMENTO = "Cultura de Marca"
RODAPE = False
ARQUIVO = "Cultura-de-Marca-My-Home"

IMG = {
    "div1": "myhome-div-origem.png",
    "div2": "myhome-div-personalidade.png",
    "div3": "myhome-div-cultura-em-acao.png",
    "div4": "myhome-div-percepcao.png",
    "origem": "myhome-sobras-material.png",
    "expressao": "myhome-produtos-variedade.png",
    "essencia": "myhome-produto-em-casa.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    {"tipo": "capa",
     "titulo": ["MY HOME"],
     "subtitulo": ["Cultura de Marca", "Criatividade que transforma."],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["Uma origem compartilhada,",
                "duas identidades",
                "com significados próprios."]},

    {"tipo": "sumario", "titulo": "Cultura de marca", "itens": [
        ("01", "Origem e crenças",
         "A história, os significados e os valores que orientam a marca."),
        ("02", "Personalidade e expressão",
         "O jeito de ser, de se comunicar e de se apresentar."),
        ("03", "Cultura em ação",
         "Comportamentos da equipe e experiência entregue ao cliente."),
        ("04", "Percepção e coerência",
         "O que o mercado reconhece e o que precisamos construir."),
    ]},

    # ═══════════════════════════════════════ 01 ORIGEM E CRENÇAS
    {"tipo": "divisor", "numero": "01", "nome": "Origem e crenças",
     "apoio": "A história, os significados e os valores que orientam a "
              "marca.",
     "foto": IMG["div1"],
     "imagem": "A origem da My Home: o material guardado, as sobras "
               "empilhadas à espera de um destino. O começo da história."},

    {"tipo": "declaracao",
     "linhas": ["Enxergar possibilidades",
                "onde outros enxergam limites."]},

    {"tipo": "texto", "foto": IMG["origem"], "lado": "direita",
     "imagem": "O material antes de virar produto — a sobra, o retalho, a "
               "chapa separada. O ponto de partida.",
     "titulo": "Origem, significado e valores",
     "tam_corpo": 21,
     "paragrafos": [
         "A My Home nasceu do inconformismo diante do desperdício. Flávia "
         "viu nos materiais descartados uma oportunidade de transformar "
         "recursos em novas criações.",
         "O reaproveitamento foi o ponto de partida. A capacidade de "
         "transformar possibilidades é o verdadeiro significado da marca.",
     ]},

    {"tipo": "palavras", "titulo": "Os valores da marca",
     "palavras": ["Inventividade", "Transformação", "Originalidade",
                  "Qualidade", "Acessibilidade", "Evolução"]},

    {"tipo": "declaracao",
     "linhas": ["O valor de um material não se limita",
                "ao uso para o qual",
                "foi originalmente pensado."],
     "apoio": "A crença central da My Home."},

    # ═══════════════════════════════ 02 PERSONALIDADE E EXPRESSÃO
    {"tipo": "divisor", "numero": "02", "nome": "Personalidade e expressão",
     "apoio": "O jeito de ser, de se comunicar e de se apresentar.",
     "foto": IMG["div2"],
     "imagem": "Um produto My Home em plano fechado — textura, forma, "
               "encaixe. A criatividade vista de perto."},

    {"tipo": "palavras", "titulo": "Como a My Home é", "grade": 1,
     "palavras": ["Criativa", "Curiosa", "Expressiva", "Próxima"]},

    {"tipo": "texto", "foto": IMG["expressao"], "lado": "esquerda",
     "imagem": "Vários produtos My Home juntos — a variedade e a "
               "originalidade da linha, bem arranjadas.",
     "titulo": "A criatividade que surpreende tem conhecimento por trás.",
     "tam_corpo": 21,
     "paragrafos": [
         "A My Home enxerga o potencial de transformação nas formas, nos "
         "materiais e nos objetos.",
         "Sua personalidade combina imaginação e habilidade técnica para "
         "criar produtos que despertem curiosidade e surpreendam pelo "
         "resultado.",
         "Deve se expressar com leveza, originalidade, experimentação e "
         "valorização das possibilidades de transformação.",
     ]},

    # ═══════════════════════════════════════════ 03 CULTURA EM AÇÃO
    {"tipo": "divisor", "numero": "03", "nome": "Cultura em ação",
     "apoio": "Comportamentos da equipe e experiência entregue ao cliente.",
     "foto": IMG["div3"],
     "imagem": "A bancada de criação: protótipo, teste de acabamento, peça "
               "em desenvolvimento. A experimentação acontecendo."},

    {"tipo": "colunas",
     "titulo": "Criar não é improvisar. É transformar com intenção.",
     "colunas": [
         ("O que a equipe precisa viver",
          "Experimentar novas possibilidades. Compartilhar ideias. Dominar "
          "técnicas. Aperfeiçoar materiais e acabamentos. Transformar "
          "criatividade em produtos viáveis."),
         ("O que o cliente deve experimentar",
          "O prazer de descobrir produtos originais, capazes de acrescentar "
          "personalidade e novas possibilidades à sua casa."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Não é apenas comprar um objeto decorativo.",
                "É encontrar algo inesperado",
                "que faça sentido no próprio ambiente."],
     "apoio": "A experiência pretendida pela My Home."},

    # ═══════════════════════════════ 04 PERCEPÇÃO E COERÊNCIA
    {"tipo": "divisor", "numero": "04", "nome": "Percepção e coerência",
     "apoio": "O que o mercado reconhece e o que precisamos construir.",
     "foto": IMG["div4"],
     "imagem": "Produtos My Home em uso numa casa real — a marca vivendo no "
               "ambiente do cliente."},

    {"tipo": "colunas",
     "titulo": "De uma capacidade criativa a uma marca com identidade "
               "própria.",
     "colunas": [
         ("O que já é reconhecido",
          "Arquitetos valorizam a capacidade da My Home de executar soluções "
          "técnicas, detalhes e acabamentos especiais."),
         ("O que precisamos construir",
          "Uma identidade independente, reconhecida pelo consumidor pela "
          "originalidade dos produtos, pela criatividade e pela confiança na "
          "experiência de compra."),
     ],
     "fecho": "A My Home pode continuar sendo parceira produtiva da Forma, "
              "mas não deve ser percebida apenas como seu braço "
              "operacional."},

    {"tipo": "foto_cheia", "foto": IMG["essencia"],
     "imagem": "Um produto My Home em destaque no ambiente. Imagem ampla, "
               "que aguente a frase por cima.",
     "linhas": ["Transformar possibilidades", "em criação."],
     "apoio": "A essência cultural da My Home. Criatividade que transforma."},

    # ——————————————————————————————————————— síntese das duas marcas
    {"tipo": "contraste", "titulo": "Uma origem. Duas expressões de marca.",
     "esquerda": ("My Home", [
         "Crença: sempre existe uma nova possibilidade de criação.",
         "Comportamento: experimentação, transformação e aperfeiçoamento.",
         "Experiência pretendida: prazer em descobrir e transformar.",
         "Valor central: criatividade.",
     ]),
     "direita": ("Forma", [
         "Crença: o conhecimento amplia os limites de um projeto.",
         "Comportamento: precisão, cuidado e responsabilidade.",
         "Experiência: segurança para realizar.",
         "Valor central: confiança.",
     ])},

    {"tipo": "declaracao",
     "linhas": ["A mesma mentalidade impulsiona as duas marcas",
                "e se manifesta de maneiras distintas",
                "no valor que cada uma entrega ao mercado."]},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
