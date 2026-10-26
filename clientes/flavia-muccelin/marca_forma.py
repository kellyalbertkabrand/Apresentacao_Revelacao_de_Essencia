# -*- coding: utf-8 -*-
"""
CULTURA DE MARCA — FORMA

Só conteúdo. Identidade, grade, paleta e escala são as de sempre
(padrao-ka/ka_layout.py e padrao-ka/ka_paginas.py).

O roteiro da Kelly veio como UM documento cobrindo as duas marcas; ela pediu
**duas apresentações separadas**. Esta é a da Forma: a capa, o sumário e as
quatro seções são dela, e nenhuma página do miolo fala da My Home.

As duas últimas páginas antes do fecho são a exceção, e é proposital: a
síntese (slide 13 do roteiro) compara as duas marcas, e é o que situa a
Forma ao lado da irmã. Uma cultura de marca precisa dizer onde a marca
está. Se preferir a Forma sozinha do começo ao fim, são duas páginas para
tirar.

Como fica visual, pelos arquétipos:

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` com foto | as quatro viradas de seção, em tela cheia de imagem | 4 |
| `declaracao` | a página de silêncio: uma frase, muito ar | 5 |
| `palavras` | os valores e a personalidade, como composição | 2 |
| `colunas` | equipe × cliente, reconhecimento × preservação | 2 |
| `contraste` | a síntese das duas marcas, separadas pelo × | 1 |
| `foto_cheia` | a essência cultural, em tela cheia | 1 |
| `texto` | só onde o conteúdo é mesmo narrativa | 2 |

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela. Quando o arquivo entrar em `assets/` com o nome declarado em
`foto`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py marca-forma
"""

MARCA = "FORMA"
DOCUMENTO = "Cultura de Marca"
RODAPE = False
ARQUIVO = "Cultura-de-Marca-Forma"

IMG = {
    "div1": "forma-div-origem.png",
    "div2": "forma-div-personalidade.png",
    "div3": "forma-div-cultura-em-acao.png",
    "div4": "forma-div-percepcao.png",
    "origem": "forma-projeto-complexo.png",
    "expressao": "forma-detalhe-acabamento.png",
    "essencia": "forma-ambiente-entregue.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    {"tipo": "capa",
     "titulo": ["FORMA"],
     "subtitulo": ["Cultura de Marca", "Precisão que realiza."],
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
         "O que o mercado reconhece e o que precisa ser fortalecido."),
    ]},

    # ═══════════════════════════════════════ 01 ORIGEM E CRENÇAS
    {"tipo": "divisor", "numero": "01", "nome": "Origem e crenças",
     "apoio": "A história, os significados e os valores que orientam a "
              "marca.",
     "foto": IMG["div1"],
     "imagem": "A origem da Forma: a oficina, uma máquina em operação, ou o "
               "primeiro projeto assinado. Plano aberto."},

    {"tipo": "declaracao",
     "linhas": ["A liberdade de criar exige",
                "a capacidade de realizar."]},

    {"tipo": "texto", "foto": IMG["origem"], "lado": "direita",
     "imagem": "Um projeto complexo em execução — marcenaria sob medida, "
               "encaixe, peça grande em montagem. O domínio técnico "
               "aparecendo no trabalho.",
     "titulo": "Origem, significado e valores",
     "tam_corpo": 21,
     "paragrafos": [
         "A Forma representa a liberdade conquistada por Flávia para "
         "executar projetos sem ficar restrita às limitações dos sistemas "
         "padronizados.",
         "Sua identidade se constrói sobre uma convicção: o conhecimento "
         "técnico deve ampliar as possibilidades de um projeto, não "
         "limitá-las.",
     ]},

    {"tipo": "palavras", "titulo": "Os valores da marca", "grade": 1,
     "palavras": ["Precisão", "Personalização", "Responsabilidade",
                  "Confiança", "Evolução técnica"]},

    {"tipo": "declaracao",
     "linhas": ["Uma ideia singular merece",
                "uma execução à sua altura."],
     "apoio": "A crença central da Forma."},

    # ═══════════════════════════════ 02 PERSONALIDADE E EXPRESSÃO
    {"tipo": "divisor", "numero": "02", "nome": "Personalidade e expressão",
     "apoio": "O jeito de ser, de se comunicar e de se apresentar.",
     "foto": IMG["div2"],
     "imagem": "Um detalhe de acabamento em plano fechado — a junção, a "
               "ferragem, a borda. O critério visto de perto."},

    {"tipo": "palavras", "titulo": "Como a Forma é", "grade": 1,
     "palavras": ["Segura", "Criteriosa", "Técnica", "Próxima"]},

    {"tipo": "texto", "foto": IMG["expressao"], "lado": "esquerda",
     "imagem": "Uma conversa técnica com arquiteto ou cliente, sobre o "
               "projeto — prancha, amostra de material, desenho na mesa.",
     "titulo": "Sofisticação que se comprova na competência.",
     "tam_corpo": 21,
     "paragrafos": [
         "A Forma não precisa demonstrar superioridade. Precisa demonstrar "
         "domínio.",
         "Sua personalidade combina a segurança de quem conhece "
         "profundamente o que faz com a proximidade de quem compreende a "
         "importância daquele projeto para o cliente.",
         "Expressa-se com clareza técnica, atenção aos detalhes, segurança "
         "nas orientações e sofisticação sem ostentação.",
     ]},

    # ═══════════════════════════════════════════ 03 CULTURA EM AÇÃO
    {"tipo": "divisor", "numero": "03", "nome": "Cultura em ação",
     "apoio": "Comportamentos da equipe e experiência entregue ao cliente.",
     "foto": IMG["div3"],
     "imagem": "A equipe montando na casa do cliente — ambiente protegido, "
               "trabalho em andamento, cuidado visível."},

    {"tipo": "colunas",
     "titulo": "O verdadeiro alto padrão é a tranquilidade de quem confia.",
     "colunas": [
         ("O que a equipe precisa viver",
          "Compreender antes de executar. Antecipar dificuldades. Respeitar "
          "o projeto. Cuidar dos detalhes. Assumir a responsabilidade pela "
          "entrega."),
         ("O que o cliente deve experimentar",
          "Segurança para realizar projetos complexos, com acompanhamento, "
          "precisão e cuidado do início ao fim."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Não é apenas receber um móvel impecável.",
                "É sentir que todo o processo",
                "está em mãos competentes."],
     "apoio": "A experiência central da Forma."},

    # ═══════════════════════════════ 04 PERCEPÇÃO E COERÊNCIA
    {"tipo": "divisor", "numero": "04", "nome": "Percepção e coerência",
     "apoio": "O que o mercado reconhece e o que precisa ser fortalecido.",
     "foto": IMG["div4"],
     "imagem": "Um ambiente entregue e em uso, assinado pela Forma. Plano "
               "aberto, luz natural, sem pessoas."},

    {"tipo": "colunas",
     "titulo": "O valor da Forma não está apenas no que ela produz. Está "
               "na confiança que ela constrói.",
     "colunas": [
         ("O que o mercado reconhece",
          "Arquitetos e clientes destacam domínio técnico, qualidade dos "
          "acabamentos, parceria e cuidado na execução."),
         ("O que precisa ser preservado",
          "A capacidade de personalizar, a proximidade com o cliente e a "
          "responsabilidade pelo resultado, mesmo com o crescimento "
          "industrial."),
     ]},

    {"tipo": "foto_cheia", "foto": IMG["essencia"],
     "imagem": "Um ambiente completo entregue pela Forma. Imagem ampla, que "
               "aguente a frase por cima.",
     "linhas": ["Transformar complexidade", "em confiança."],
     "apoio": "A essência cultural da Forma. Precisão que realiza."},

    # ——————————————————————————————————————— síntese das duas marcas
    {"tipo": "contraste", "titulo": "Uma origem. Duas expressões de marca.",
     "esquerda": ("Forma", [
         "Crença: o conhecimento amplia os limites de um projeto.",
         "Comportamento: precisão, cuidado e responsabilidade.",
         "Experiência: segurança para realizar.",
         "Valor central: confiança.",
     ]),
     "direita": ("My Home", [
         "Crença: sempre existe uma nova possibilidade de criação.",
         "Comportamento: experimentação, transformação e aperfeiçoamento.",
         "Experiência pretendida: prazer em descobrir e transformar.",
         "Valor central: criatividade.",
     ])},

    {"tipo": "declaracao",
     "linhas": ["A mesma mentalidade impulsiona as duas marcas",
                "e se manifesta de maneiras distintas",
                "no valor que cada uma entrega ao mercado."]},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
