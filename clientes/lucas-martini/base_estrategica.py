# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — Lucas Martini | Proteção & Sucessão

Só conteúdo. Layout em padrao-ka/ka_layout.py, arquétipos de página em
padrao-ka/ka_paginas.py.

30 páginas. A versão anterior tinha 69 e dizia a mesma coisa: cada
definição vinha anunciada, desenvolvida e repetida.

A conta aqui é apertada e vale explicar. São NOVE seções, e os divisores
sozinhos já ocupam 9 das 30 páginas. Com capa, sumário, abertura e fecho,
sobram 17 para o conteúdo — menos de duas por seção. Por isso os cinco
pilares viraram uma página, os quatro públicos viraram uma, e o Golden
Circle inteiro cabe numa só. Nenhuma definição do material original saiu;
o que saiu foi a página de anúncio antes de cada uma.

As fotografias entram em tira vertical ou tela cheia; o recorte sai de
`assets/rostos.json` para que o rosto nunca seja cortado.
"""

MARCA = "Lucas Martini"
DOCUMENTO = "Base Estratégica da Marca"
ARQUIVO = "Base-Estrategica-da-Marca-Lucas-Martini"

IMG = {
    1: "01_retrato_corporativo_prudential.png",
    2: "02_reuniao_consultiva_casal.png",
    3: "03_lucas_janela_entardecer.png",
    5: "05_lucas_casal_mais_velho.png",
    6: "06_lucas_corredor_prudential.png",
    8: "08_lucas_aperto_de_maos_cliente.png",
    9: "09_lucas_analisando_documentos.png",
    10: "10_lucas_sala_reuniao.png",
    11: "11_lucas_consulta_individual.png",
    12: "12_lucas_caminhando_janela.png",
    13: "13_lucas_ouvindo_casal.png",
    14: "14_retrato_lucas_corredor.png",
}

PAGINAS = [
    # 01
    {"tipo": "abertura"},

    # 02 — capa
    {"tipo": "capa",
     "titulo": ["BASE", "ESTRATÉGICA"],
     "subtitulo": ["Lucas Martini", "Proteção & Sucessão"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026",
     "foto": IMG[1], "foco": 0.42},

    # 03 — sumário
    {"tipo": "sumario", "itens": [
        ("01", "Leitura do momento da marca"),
        ("02", "Definição central da marca"),
        ("03", "Causa, liderança e tribo"),
        ("04", "Golden Circle"),
        ("05", "Proposta de valor e posicionamento"),
        ("06", "Arquitetura de marca"),
        ("07", "Territórios, pilares e público"),
        ("08", "Personalidade e tom de voz"),
        ("09", "Manifesto e síntese final"),
    ]},

    # ——— 01 LEITURA DO MOMENTO
    {"tipo": "divisor", "numero": "01", "nome": "Leitura do momento",
     "apoio": "O que a marca já tem, e o que ainda não aparece."},

    # 05 — a marca já existe antes da comunicação
    {"tipo": "lista", "eyebrow": "Leitura do momento", "foto": IMG[10],
     "lado": "direita",
     "titulo": "A marca já existe antes da comunicação",
     "lead": "Lucas possui ativos que identidade visual e conteúdo não "
             "fabricam:",
     "itens": ["experiência, resultado e recomendação;",
               "confiança, relacionamento e reconhecimento;",
               "histórico de atendimento."],
     "destaque": "Primeiro veio a reputação. Agora a marca precisa torná-la "
                 "visível."},

    # 06 — o paradoxo e a evolução de percepção
    {"tipo": "camadas", "eyebrow": "Leitura do momento",
     "titulo": "A autoridade real é maior que a percebida",
     "camadas": [
         ("O paradoxo",
          "Lucas tem conquistas relevantes e dificuldade em comunicá-las. O "
          "problema não é falta de substância: é falta de tradução pública "
          "dessa substância."),
         ("O risco",
          "Sem construção própria, ele é percebido apenas como corretor de "
          "seguros, ou como alguém ligado a uma seguradora."),
         ("A evolução",
          "De corretor de seguros a especialista em proteção e sucessão — e, "
          "numa camada mais estratégica, a um profissional que estrutura "
          "continuidade e preserva possibilidades."),
     ]},

    # ——— 02 DEFINIÇÃO CENTRAL
    {"tipo": "divisor", "numero": "02", "nome": "Definição central",
     "apoio": "O que Lucas entrega, abaixo do produto."},

    # 08 — o que ele faz de verdade
    {"tipo": "lista", "eyebrow": "Definição central", "foto": IMG[11],
     "lado": "esquerda",
     "titulo": "O que Lucas faz de verdade",
     "lead": "Ele não começa pelo produto. Começa pela realidade:",
     "itens": ["Quem depende daquele cliente?",
               "Que impacto sua ausência produziria?",
               "Como o patrimônio seria transferido? Existe liquidez?"],
     "destaque": "A proteção é consequência do diagnóstico."},

    # 09 — a definição central
    {"tipo": "foto_cheia", "foto": IMG[2], "foco": 0.40, "veu": 0.66,
     "eyebrow": "Definição central",
     "linhas": ["Lucas Martini estrutura proteção",
                "e sucessão para preservar possibilidades",
                "quando a vida, a família ou a empresa",
                "entram em transição."],
     "apoio": "Produto: seguro e soluções de proteção. Serviço: planejamento. "
              "Valor estratégico: continuidade. Valor humano: capacidade de "
              "escolha."},

    # ——— 03 CAUSA, LIDERANÇA E TRIBO
    {"tipo": "divisor", "numero": "03", "nome": "Causa e tribo",
     "apoio": "No que a marca acredita, e para quem ela fala."},

    # 11 — a causa
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.38, "veu": 0.66,
     "eyebrow": "A causa",
     "linhas": ["O que levou anos para ser construído",
                "não deveria ficar entregue ao acaso."],
     "apoio": "Não porque todos os riscos possam ser eliminados, mas porque "
              "muitos dos seus impactos podem ser preparados. Nem tudo pode "
              "ser previsto — mas muito pode ser preparado."},

    # 12 — a mudança que defende, o que combate e a tribo
    {"tipo": "camadas", "eyebrow": "Causa e tribo",
     "titulo": "O que a marca defende e para quem",
     "camadas": [
         ("A mudança",
          "De resolver depois para pensar antes. De seguro como produto para "
          "proteção como estratégia. De sucessão como problema futuro para "
          "responsabilidade presente."),
         ("O que combate",
          "Não a morte nem a incerteza: o improviso, o adiamento, a falta de "
          "liquidez e as decisões tomadas sob pressão."),
         ("A liderança",
          "Não ocupar o território do medo nem pressionar. Perguntar, traduzir "
          "risco, organizar possibilidades e estruturar decisões."),
         ("A tribo",
          "Empresários, sócios, profissionais liberais, pilares financeiros e "
          "pessoas-chave. Há algo ou alguém que depende das suas decisões."),
     ]},

    # ——— 04 GOLDEN CIRCLE
    {"tipo": "divisor", "numero": "04", "nome": "Golden Circle",
     "apoio": "Por quê, como e o quê — nesta ordem."},

    # 14 — golden circle
    {"tipo": "colunas", "eyebrow": "Golden Circle",
     "titulo": "Por quê, como e o quê",
     "colunas": [
         ("Por quê",
          "Porque o que levou anos para ser construído não deveria perder sua "
          "continuidade por falta de preparação."),
         ("Como",
          "Entendendo a realidade do cliente, identificando "
          "vulnerabilidades, projetando impactos e estruturando proteção de "
          "forma personalizada, com acompanhamento de longo prazo."),
         ("O quê",
          "Proteção de renda, familiar e empresarial. Pessoa-chave. "
          "Planejamento sucessório. Liquidez para sucessão e inventário."),
     ],
     "fecho": "Não começar pelo produto. Começar pela consequência."},

    # ——— 05 PROPOSTA DE VALOR E POSICIONAMENTO
    {"tipo": "divisor", "numero": "05", "nome": "Posicionamento",
     "apoio": "O que a marca promete e onde ela se coloca."},

    # 16 — proposta de valor
    {"tipo": "foto_cheia", "foto": IMG[12], "foco": 0.42, "veu": 0.64,
     "eyebrow": "Proposta de valor",
     "linhas": ["Estruturar proteção e sucessão de forma",
                "personalizada para que famílias, profissionais",
                "e empresas mantenham recursos, possibilidades",
                "e continuidade diante de imprevistos."]},

    # 17 — posicionamento e diferenciação
    {"tipo": "texto", "eyebrow": "Posicionamento", "foto": IMG[13],
     "lado": "esquerda",
     "titulo": "Posicionamento",
     "lead": "Lucas Martini é especialista em proteção e sucessão para "
             "pessoas, famílias e empresas que desejam preservar o que "
             "construíram e manter possibilidades diante do imprevisto.",
     "paragrafos": [
         "O produto não diferencia. A diferenciação está na combinação de "
         "diagnóstico, personalização, conhecimento técnico, confiança, "
         "pós-venda e relação de longo prazo. A melhor proteção não é a "
         "maior: é a que faz sentido para aquela realidade.",
     ],
     "destaque": "Preparar antes para preservar escolhas depois."},

    # ——— 06 ARQUITETURA
    {"tipo": "divisor", "numero": "06", "nome": "Arquitetura",
     "apoio": "O nome no centro, e as frentes que ele sustenta."},

    # 19 — arquitetura
    {"tipo": "colunas", "eyebrow": "Arquitetura",
     "titulo": "Lucas Martini · Proteção & Sucessão",
     "tam_titulo": 36,
     "lead": "A confiança está associada à pessoa, a indicação chega pelo "
             "nome e o relacionamento acontece com Lucas. Ele é o principal "
             "ativo da arquitetura; o descritor explica o campo sem prender a "
             "marca a uma seguradora ou a um produto.",
     "colunas": [
         ("Proteção pessoal e familiar",
          "Renda, família e pilares financeiros."),
         ("Proteção empresarial",
          "Pessoa-chave e continuidade do negócio."),
         ("Sucessão familiar",
          "Transferência, liquidez e inventário."),
         ("Sucessão empresarial",
          "Passagem de responsabilidade e sociedade."),
     ],
     "fecho": "A seguradora entrega o instrumento. Lucas constrói a "
              "estratégia."},

    # ——— 07 TERRITÓRIOS, PILARES E PÚBLICO
    {"tipo": "divisor", "numero": "07", "nome": "Territórios e público",
     "apoio": "Do que a marca fala, como atua e com quem."},

    # 21 — territórios
    {"tipo": "camadas", "eyebrow": "Territórios de comunicação",
     "titulo": "Continuidade é o território",
     "camadas": [
         ("Continuidade", "O que precisa seguir existindo: renda, família, "
                          "empresa, patrimônio, projetos e legado."),
         ("Proteção",
          "Os recursos e estruturas que sustentam essa continuidade."),
         ("Sucessão",
          "A preparação para a passagem de responsabilidade e patrimônio."),
         ("Dignidade financeira",
          "A preservação de alternativas em momentos difíceis."),
         ("Escolha e responsabilidade",
          "Decidir sem ser dominado pela urgência; pensar hoje nas "
          "consequências de amanhã."),
     ]},

    # 22 — os cinco pilares
    {"tipo": "camadas", "eyebrow": "Os pilares", "foto": IMG[9],
     "lado": "direita",
     "titulo": "Os cinco pilares",
     "camadas": [
         ("Antecipação", "Decisões são melhores sem urgência."),
         ("Personalização", "Não existe proteção ideal fora de contexto."),
         ("Confiança", "Transparência e consistência ao longo dos anos."),
         ("Continuidade", "A proteção não termina na contratação."),
         ("Excelência", "Menos discurso, mais padrão de execução."),
     ]},

    # 23 — os quatro públicos
    {"tipo": "colunas", "eyebrow": "Público",
     "titulo": "Quem carrega responsabilidade",
     "colunas": [
         ("Quem produz a própria renda",
          "Profissionais liberais, autônomos, executivos e especialistas."),
         ("Quem sustenta outras pessoas",
          "Pilares financeiros da família, cuja ausência alteraria a "
          "estrutura econômica de casa."),
         ("Quem responde por uma empresa",
          "Empresários, sócios e pessoas-chave de negócios dependentes de "
          "indivíduos específicos."),
         ("Quem construiu patrimônio",
          "Famílias e sócios que precisam organizar transferência, liquidez "
          "e sucessão."),
     ],
     "fecho": "Parecem diferentes, mas existe algo ou alguém que depende das "
              "decisões de cada um."},

    # ——— 08 PERSONALIDADE E TOM DE VOZ
    {"tipo": "divisor", "numero": "08", "nome": "Personalidade e voz",
     "apoio": "Como a marca se comporta e como ela fala."},

    # 25 — personalidade
    {"tipo": "camadas", "eyebrow": "Personalidade", "foto": IMG[14],
     "lado": "esquerda",
     "titulo": "Autoridade discreta",
     "camadas": [
         ("Seguro e preparado",
          "Transmite domínio sem precisar provar o tempo todo; estuda antes "
          "de orientar."),
         ("Consultivo e humano",
          "Pergunta antes de oferecer e entende o que existe por trás dos "
          "números."),
         ("Elegante e acessível",
          "Sofisticação sem ostentação; torna o complexo compreensível."),
         ("Nunca",
          "Alarmista, exibicionista, técnica demais, comercial demais ou "
          "genérica."),
     ]},

    # 26 — como a marca fala
    {"tipo": "alternativas", "eyebrow": "Tom de voz",
     "titulo": "Provar, não proclamar",
     "pares": [
         ("Você pode morrer amanhã.",
          "Quem depende financeiramente de você hoje?"),
         ("Você precisa contratar um seguro de vida.",
          "Antes do produto, precisamos entender o impacto financeiro que "
          "uma ausência produziria."),
         ("Olha onde eu cheguei.",
          "Esse reconhecimento representa dez anos de consistência e "
          "confiança de clientes."),
     ]},

    # ——— 09 MANIFESTO E SÍNTESE
    {"tipo": "divisor", "numero": "09", "nome": "Manifesto",
     "apoio": "A marca em palavras, e a marca em uma página."},

    # 28 — manifesto
    {"tipo": "manifesto", "eyebrow": "Manifesto",
     "paragrafos": [
         "Há coisas que levam anos para construir. Uma carreira. Uma família. "
         "Uma empresa. Um patrimônio.",
         "E nenhuma delas deveria ficar completamente dependente daquilo que "
         "não podemos controlar.",
         "Planejar não é esperar que algo dê errado. É reconhecer o valor "
         "daquilo que deu certo.",
         "É pensar antes. Enquanto existe tempo. Enquanto podemos escolher.",
         "Nem tudo pode ser previsto. Mas muito pode ser preparado.",
         "Porque proteção não existe para preservar dinheiro. Existe para "
         "preservar possibilidades.",
     ],
     "assinatura": "LUCAS MARTINI  |  PROTEÇÃO & SUCESSÃO"},

    # 29 — a marca em uma página
    {"tipo": "ficha", "eyebrow": "Síntese",
     "titulo": "A marca em uma página",
     "campos": [
         ("Crença fundadora",
          "O que levou anos para ser construído não deveria ficar entregue "
          "ao acaso."),
         ("Razão de ser",
          "Preservar a capacidade de escolha quando a vida tira a "
          "previsibilidade."),
         ("Essência", "Construir segurança para preservar liberdade de "
                      "escolha."),
         ("Causa", "Ampliar a cultura da preparação antes da urgência."),
         ("Território", "Continuidade."),
         ("Posicionamento",
          "Especialista em proteção e sucessão para quem deseja preservar o "
          "que construiu e manter possibilidades diante do imprevisto."),
         ("Proposta de valor",
          "Estruturar proteção e sucessão de forma personalizada para "
          "preservar recursos, continuidade e capacidade de escolha."),
         ("Princípio de comunicação", "Provar, não proclamar."),
         ("Personalidade", "Autoridade discreta."),
     ]},

    # 30
    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
