# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — Lucas Martini | Proteção & Sucessão

Só conteúdo. Layout em padrao-ka/ka_layout.py, arquétipos de página em
padrao-ka/ka_paginas.py.

Aqui as fotografias aparecem menos como história do Lucas e mais como prova
da marca em ação, conforme o gabarito da Kelly. A imagem 07 ficou de fora.
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
    {"tipo": "abertura"},

    # 01 — capa
    {"tipo": "capa",
     "titulo": ["BASE ESTRATÉGICA", "DA MARCA"],
     "subtitulo": "Lucas Martini  |  Proteção & Sucessão",
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026",
     "foto": IMG[1], "foco": 0.42},

    # 02 — sumário
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
    {"tipo": "divisor", "numero": "01", "nome": "Leitura do momento da marca"},

    # 04
    {"tipo": "lista", "eyebrow": "Leitura do momento", "foto": IMG[10],
     "fatia": 0.32, "foco": 0.24,
     "titulo": "A marca já existe antes da comunicação",
     "lead": "Lucas já possui ativos que não podem ser fabricados por "
             "identidade visual ou conteúdo:",
     "itens": ["experiência;", "resultado;", "recomendação;", "confiança;",
               "relacionamento;", "reconhecimento;",
               "histórico de atendimento."],
     "destaque": "Primeiro veio a reputação. Agora a marca precisa torná-la "
                 "visível."},

    # 05
    {"tipo": "texto", "eyebrow": "Leitura do momento", "foto": IMG[14],
     "lado": "baixo", "fatia": 0.36, "foco": 0.12,
     "titulo": "O paradoxo atual",
     "lead": "A autoridade real é maior do que a autoridade percebida.",
     "paragrafos": [
         "Lucas possui conquistas e reconhecimentos relevantes, mas admite "
         "dificuldade em comunicá-los e se expor. O problema estratégico não "
         "é falta de substância: é falta de tradução pública dessa "
         "substância.",
     ]},

    # 06
    {"tipo": "texto", "eyebrow": "Leitura do momento", "foto": IMG[1],
     "lado": "direita", "foco": 0.44,
     "titulo": "O risco de percepção",
     "lead": "Sem uma construção própria, Lucas pode ser percebido apenas "
             "como corretor de seguros, ou como profissional ligado à "
             "Prudential.",
     "paragrafos": [
         "Mas sua atuação é mais ampla. Ele analisa realidade financeira, "
         "profissional, familiar, empresarial e patrimonial para estruturar "
         "proteção, sucessão e continuidade de maneira personalizada.",
     ]},

    # 07
    {"tipo": "declaracao",
     "linhas": ["O desafio não é parecer maior.",
                "É fazer a percepção alcançar a entrega."]},

    # 08
    {"tipo": "camadas", "eyebrow": "Leitura do momento", "foto": IMG[6],
     "lado": "cima", "fatia": 0.30, "foco": 0.22,
     "titulo": "A evolução de percepção",
     "camadas": [
         ("Não apenas", "Corretor de seguros."),
         ("Mas", "Especialista em proteção e sucessão."),
         ("Em uma camada mais estratégica",
          "Um profissional que estrutura continuidade e preserva "
          "possibilidades."),
     ]},

    # ——— 02 DEFINIÇÃO CENTRAL
    {"tipo": "divisor", "numero": "02", "nome": "Definição central da marca"},

    # 10
    {"tipo": "lista", "eyebrow": "Definição central", "foto": IMG[11],
     "fatia": 0.30, "foco": 0.22,
     "titulo": "O que Lucas faz de verdade?",
     "lead": "Lucas não começa pelo produto. Começa pela realidade.",
     "itens": ["Quem depende daquele cliente?", "O que está vulnerável?",
               "Que impacto sua ausência produziria?",
               "O que aconteceria com a empresa?",
               "Como o patrimônio seria transferido?",
               "Existe liquidez?", "Existe continuidade?"],
     "destaque": "A proteção é consequência do diagnóstico."},

    # 11
    {"tipo": "foto_cheia", "foto": IMG[2], "foco": 0.40, "veu": 0.66,
     "eyebrow": "Definição central",
     "linhas": ["Lucas Martini estrutura proteção e sucessão",
                "para preservar possibilidades quando a vida,",
                "a família ou a empresa entram em transição."],
     "tam": 32},

    # 12
    {"tipo": "camadas", "eyebrow": "Definição central",
     "titulo": "As quatro camadas da entrega",
     "camadas": [
         ("Produto", "Seguro e soluções financeiras de proteção."),
         ("Serviço", "Planejamento de proteção e sucessão."),
         ("Valor estratégico", "Continuidade."),
         ("Valor humano", "Capacidade de escolha."),
     ]},

    # 13
    {"tipo": "palavras", "eyebrow": "Definição central", "foto": IMG[3],
     "lado": "baixo", "fatia": 0.30, "foco": 0.26,
     "titulo": "O território central: continuidade",
     "palavras": ["Da renda", "Da família", "Dos projetos",
                  "Da empresa", "Do patrimônio", "Do legado"],
     "grade": 2, "tam": 22,
     "destaque": "A continuidade é o território capaz de conectar as "
                 "diferentes soluções sem reduzir a marca ao seguro."},

    # ——— 03 CAUSA, LIDERANÇA E TRIBO
    {"tipo": "divisor", "numero": "03", "nome": "Causa, liderança e tribo"},

    # 15
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.38, "veu": 0.66,
     "eyebrow": "A causa",
     "linhas": ["O que levou anos para ser construído",
                "não deveria ficar entregue ao acaso."],
     "apoio": "Não porque todos os riscos possam ser eliminados. Mas porque "
              "muitos dos seus impactos podem ser preparados."},

    # 16
    {"tipo": "camadas", "eyebrow": "A causa",
     "titulo": "A mudança cultural que a marca defende",
     "camadas": [
         ("De resolver depois", "Para pensar antes."),
         ("De seguro como produto", "Para proteção como estratégia."),
         ("De sucessão como problema futuro",
          "Para sucessão como responsabilidade presente."),
     ]},

    # 17
    {"tipo": "contraste", "eyebrow": "A causa",
     "titulo": "O que a marca combate",
     "esquerda": ("Combate",
                  ["improviso;", "desorganização;", "adiamento;",
                   "falta de liquidez;", "dependência não mapeada;",
                   "decisões tomadas sob pressão;",
                   "proteção tratada apenas como compra de produto."]),
     "direita": ("Não combate",
                 ["a morte;", "a doença;", "a incerteza."])},

    # 18
    {"tipo": "foto_cheia", "foto": IMG[12], "foco": 0.42, "veu": 0.58,
     "linhas": ["Nem tudo pode ser previsto.",
                "Mas muito pode ser preparado."]},

    # 19
    {"tipo": "lista", "eyebrow": "A liderança da marca", "foto": IMG[11],
     "lado": "cima", "fatia": 0.30, "foco": 0.24,
     "titulo": "Ajudar o cliente a enxergar antes",
     "lead": "Lucas não deve ocupar o território do medo. Também não precisa "
             "assumir o papel do vendedor que pressiona. Seu papel é outro:",
     "itens": ["Perguntar.", "Provocar reflexão.", "Traduzir risco.",
               "Organizar possibilidades.", "Trazer clareza.",
               "Estruturar decisões."]},

    # 20
    {"tipo": "palavras", "eyebrow": "A tribo", "foto": IMG[2],
     "lado": "baixo", "fatia": 0.30, "foco": 0.26,
     "titulo": "A tribo",
     "lead": "A tribo do Lucas não é definida apenas por idade ou renda. É "
             "formada principalmente por pessoas que carregam "
             "responsabilidade.",
     "palavras": ["Empresários", "Sócios", "Profissionais liberais",
                  "Autônomos", "Pilares financeiros",
                  "Famílias com patrimônio", "Pessoas-chave"],
     "grade": 2, "tam": 22,
     "destaque": "Há algo ou alguém que depende de suas decisões."},

    # 21
    {"tipo": "declaracao",
     "linhas": ["Quanto maior a responsabilidade",
                "que uma pessoa carrega, maior a importância",
                "de não deixar todas as respostas para depois."]},

    # ——— 04 GOLDEN CIRCLE
    {"tipo": "divisor", "numero": "04", "nome": "Golden Circle"},

    # 23
    {"tipo": "texto", "eyebrow": "Why | Por quê?", "foto": IMG[3],
     "lado": "cima", "fatia": 0.36, "foco": 0.26,
     "titulo": "Por quê?",
     "destaque": "Porque o que levou anos para ser construído não deveria "
                 "perder sua continuidade por falta de preparação.",
     "tam_destaque": 28,
     "paragrafos": [
         "A marca existe para preservar possibilidades diante daquilo que não "
         "pode ser controlado.",
     ]},

    # 24
    {"tipo": "lista", "eyebrow": "How | Como?", "foto": IMG[9],
     "lado": "baixo", "fatia": 0.30, "foco": 0.24,
     "titulo": "Como?",
     "itens": ["Entendendo profundamente a realidade do cliente.",
               "Identificando vulnerabilidades.", "Projetando impactos.",
               "Construindo cenários.",
               "Estruturando proteção e sucessão de forma personalizada.",
               "Mantendo acompanhamento de longo prazo."],
     "destaque": "Não começar pelo produto. Começar pela consequência."},

    # 25
    {"tipo": "lista", "eyebrow": "What | O quê?",
     "titulo": "O quê?",
     "itens": ["Proteção de renda.", "Proteção pessoal e familiar.",
               "Proteção empresarial.", "Pessoa-chave.",
               "Planejamento sucessório familiar.",
               "Planejamento sucessório empresarial.",
               "Liquidez para sucessão e inventário.",
               "Seguro de vida como instrumento estratégico de proteção."]},

    # 26
    {"tipo": "colunas", "eyebrow": "Golden Circle",
     "titulo": "Golden Circle | síntese",
     "colunas": [
         ("Por quê", "Preservar possibilidades e continuidade."),
         ("Como",
          "Antecipando vulnerabilidades e estruturando alternativas antes da "
          "urgência."),
         ("O quê",
          "Proteção financeira e planejamento sucessório para pessoas, "
          "famílias e empresas."),
     ]},

    # ——— 05 PROPOSTA DE VALOR
    {"tipo": "divisor", "numero": "05",
     "nome": "Proposta de valor e posicionamento"},

    # 28
    {"tipo": "foto_cheia", "foto": IMG[2], "foco": 0.45, "veu": 0.66,
     "eyebrow": "Proposta de valor",
     "linhas": ["Estruturar proteção e sucessão de forma",
                "personalizada para que famílias, profissionais",
                "e empresas mantenham recursos, possibilidades",
                "e continuidade diante de imprevistos e transições."],
     "tam": 28},

    # 29
    {"tipo": "texto", "eyebrow": "Proposta de valor", "foto": IMG[11],
     "lado": "cima", "fatia": 0.36, "foco": 0.24,
     "titulo": "Não é sobre vender mais proteção",
     "lead": "Lucas afirma que seu planejamento parte das necessidades do "
             "cliente e não do comissionamento.",
     "destaque": "A melhor proteção não é a maior. É a que faz sentido para "
                 "aquela realidade."},

    # 30
    {"tipo": "palavras", "eyebrow": "Diferenciação", "foto": IMG[13],
     "lado": "baixo", "fatia": 0.30, "foco": 0.22,
     "titulo": "Diferenciação",
     "lead": "O produto não é suficiente para diferenciar a marca. A "
             "diferenciação está na combinação de:",
     "palavras": ["Diagnóstico", "Personalização", "Proteção + sucessão",
                  "Conhecimento técnico", "Confiança", "Pós-venda",
                  "Relação de longo prazo"],
     "grade": 2, "tam": 22},

    # 31
    {"tipo": "declaracao",
     "linhas": ["O produto pode ser comparável.",
                "A qualidade da decisão não precisa ser."]},

    # 32
    {"tipo": "texto", "eyebrow": "Posicionamento", "foto": IMG[1],
     "lado": "esquerda", "foco": 0.44,
     "titulo": "Posicionamento",
     "lead": "Lucas Martini é especialista em proteção e sucessão para "
             "pessoas, famílias e empresas que desejam preservar o que "
             "construíram e manter possibilidades diante do imprevisto e das "
             "transições da vida.",
     "paragrafos": [
         "Sua atuação une visão consultiva, planejamento personalizado, "
         "relacionamento e acompanhamento.",
     ]},

    # 33
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.40, "veu": 0.62,
     "eyebrow": "Expressão de posicionamento",
     "linhas": ["Proteção e sucessão", "para o que precisa continuar."]},

    # 34
    {"tipo": "declaracao", "eyebrow": "Expressão conceitual", "marcar": True,
     "linhas": ["Preparar antes", "para preservar escolhas depois."]},

    # ——— 06 ARQUITETURA DE MARCA
    {"tipo": "divisor", "numero": "06", "nome": "Arquitetura de marca"},

    # 36
    {"tipo": "lista", "eyebrow": "A marca protagonista", "foto": IMG[14],
     "lado": "baixo", "fatia": 0.34, "foco": 0.12,
     "titulo": "Lucas Martini",
     "lead": "Por que a pessoa, e não a operação, é o centro:",
     "itens": ["A confiança está associada à pessoa.",
               "A indicação chega pelo nome.",
               "O relacionamento acontece com Lucas.",
               "O conhecimento é reconhecido nele."],
     "destaque": "Lucas Martini deve ser o principal ativo da arquitetura."},

    # 37
    {"tipo": "lista", "eyebrow": "Descritor", "foto": IMG[1],
     "lado": "direita", "foco": 0.44,
     "titulo": "Proteção & Sucessão",
     "lead": "O descritor deve explicar o campo de atuação sem aprisionar a "
             "marca a:",
     "itens": ["uma seguradora;", "um produto;", "uma única solução."]},

    # 38
    {"tipo": "colunas", "eyebrow": "Arquitetura",
     "titulo": "Lucas Martini · Proteção & Sucessão",
     "tam_titulo": 34,
     "colunas": [
         ("Proteção pessoal e familiar",
          "Renda, família e pilares financeiros."),
         ("Proteção empresarial", "Pessoa-chave e continuidade do negócio."),
         ("Sucessão familiar e patrimonial",
          "Transferência, liquidez e inventário."),
         ("Sucessão empresarial", "Passagem de responsabilidade e sociedade."),
     ],
     "fecho": "Pessoa-chave, seguro de vida, liquidez e demais soluções "
              "entram dentro dessas frentes."},

    # 39
    {"tipo": "lista", "eyebrow": "O papel das seguradoras", "foto": IMG[1],
     "lado": "esquerda", "foco": 0.44,
     "titulo": "O papel das seguradoras",
     "lead": "Seguradoras são parceiras, fornecedoras das soluções e "
             "credenciais relevantes. Mas não devem ser o centro da "
             "identidade.",
     "itens": [],
     "destaque": "A seguradora entrega o instrumento. Lucas constrói a "
                 "estratégia."},

    # ——— 07 TERRITÓRIOS, PILARES E PÚBLICO
    {"tipo": "divisor", "numero": "07",
     "nome": "Territórios, pilares e público"},

    # 41
    {"tipo": "palavras", "eyebrow": "Território principal", "foto": IMG[3],
     "lado": "cima", "fatia": 0.30, "foco": 0.26,
     "titulo": "Continuidade",
     "lead": "É o território mais abrangente para a marca porque permite "
             "falar simultaneamente de:",
     "palavras": ["Renda", "Família", "Empresa", "Patrimônio",
                  "Sucessão", "Projetos", "Legado"],
     "grade": 2, "tam": 22},

    # 42
    {"tipo": "camadas", "eyebrow": "Territórios de comunicação",
     "titulo": "Territórios de comunicação",
     "camadas": [
         ("Continuidade", "O que precisa seguir existindo."),
         ("Proteção",
          "Os recursos e estruturas que sustentam essa continuidade."),
         ("Sucessão",
          "A preparação para a passagem de responsabilidade e patrimônio."),
         ("Dignidade financeira",
          "A preservação de alternativas em momentos difíceis."),
         ("Escolha",
          "A possibilidade de decidir sem ser totalmente dominado pela "
          "urgência."),
         ("Responsabilidade",
          "Pensar hoje nas consequências que podem existir amanhã."),
     ]},

    # 43–47 — os cinco pilares
    {"tipo": "texto", "eyebrow": "Pilar 01", "foto": IMG[9], "lado": "cima",
     "fatia": 0.40, "foco": 0.24,
     "titulo": "Antecipação",
     "lead": "Algumas decisões são melhores quando tomadas sem urgência. A "
             "marca ajuda o cliente a olhar antes."},

    {"tipo": "texto", "eyebrow": "Pilar 02", "foto": IMG[11], "lado": "baixo",
     "fatia": 0.38, "foco": 0.22,
     "titulo": "Personalização",
     "lead": "Não existe proteção ideal fora de contexto. A solução deve "
             "nascer da realidade financeira, profissional, familiar, "
             "empresarial e patrimonial de cada cliente."},

    {"tipo": "texto", "eyebrow": "Pilar 03", "foto": IMG[8], "lado": "cima",
     "fatia": 0.40, "foco": 0.26,
     "titulo": "Confiança",
     "lead": "Lucas trabalha com decisões que podem produzir consequências "
             "anos depois. Transparência, responsabilidade e consistência são "
             "indispensáveis."},

    {"tipo": "texto", "eyebrow": "Pilar 04", "foto": IMG[13], "lado": "baixo",
     "fatia": 0.38, "foco": 0.20,
     "titulo": "Continuidade",
     "lead": "Proteção não termina na contratação. Ela existe para sustentar "
             "uma trajetória."},

    {"tipo": "lista", "eyebrow": "Pilar 05", "foto": IMG[9], "lado": "cima",
     "fatia": 0.32, "foco": 0.24,
     "titulo": "Excelência",
     "itens": ["Estudar.", "Aprimorar.", "Atualizar.", "Acompanhar.",
               "Estar disponível."],
     "destaque": "A excelência aparece menos como discurso e mais como padrão "
                 "de execução."},

    # 48–51 — os quatro públicos
    {"tipo": "lista", "eyebrow": "Público 01", "foto": IMG[11],
     "lado": "baixo", "fatia": 0.30, "foco": 0.22,
     "titulo": "Quem depende da própria capacidade de produzir renda",
     "tam_titulo": 34,
     "itens": ["Profissionais liberais.", "Autônomos.", "Executivos.",
               "Especialistas.", "Empresários.",
               "Pessoas cuja renda depende diretamente da própria capacidade "
               "de trabalho."]},

    {"tipo": "lista", "eyebrow": "Público 02", "foto": IMG[2], "lado": "cima",
     "fatia": 0.30, "foco": 0.24,
     "titulo": "Quem sustenta financeiramente outras pessoas",
     "tam_titulo": 34,
     "itens": ["Pilares financeiros familiares.", "Pais.", "Mães.",
               "Cônjuges.",
               "Pessoas cuja ausência alteraria significativamente a "
               "estrutura econômica da família."]},

    {"tipo": "lista", "eyebrow": "Público 03", "foto": IMG[11],
     "lado": "baixo", "fatia": 0.30, "foco": 0.22,
     "titulo": "Quem carrega responsabilidade sobre uma empresa",
     "tam_titulo": 34,
     "itens": ["Empresários.", "Sócios.", "Pessoas-chave.",
               "Negócios dependentes de indivíduos específicos.",
               "Empresas preocupadas com continuidade e sucessão."]},

    {"tipo": "lista", "eyebrow": "Público 04", "foto": IMG[5], "lado": "cima",
     "fatia": 0.30, "foco": 0.20,
     "titulo": "Quem construiu patrimônio e precisa pensar em sua continuidade",
     "tam_titulo": 32,
     "itens": ["Famílias com patrimônio.", "Sócios.", "Empresários.",
               "Pessoas que precisam organizar transferência, liquidez e "
               "sucessão."]},

    # 52
    {"tipo": "declaracao", "eyebrow": "O denominador comum", "marcar": True,
     "linhas": ["Existem pessoas, projetos, renda, empresas",
                "ou patrimônios que dependem",
                "de suas decisões."],
     "apoio": "Esses públicos parecem diferentes. Mas têm isso em comum."},

    # ——— 08 PERSONALIDADE E TOM DE VOZ
    {"tipo": "divisor", "numero": "08", "nome": "Personalidade e tom de voz"},

    # 54
    {"tipo": "lista", "eyebrow": "Personalidade central", "foto": IMG[14],
     "lado": "baixo", "fatia": 0.34, "foco": 0.12,
     "titulo": "Autoridade discreta",
     "lead": "Lucas não precisa construir autoridade pelo excesso de "
             "exposição. Sua marca deve transmitir autoridade por:",
     "itens": ["repertório;", "clareza;", "consistência;", "prova;",
               "experiência;", "resultado."]},

    # 55
    {"tipo": "camadas", "eyebrow": "Personalidade", "foto": IMG[10],
     "lado": "cima", "fatia": 0.26, "foco": 0.22,
     "titulo": "Personalidade",
     "camadas": [
         ("Seguro", "Transmite domínio sem necessidade de provar o tempo "
                    "todo."),
         ("Confiável", "Assume a responsabilidade daquilo que recomenda."),
         ("Preparado", "Estuda antes de orientar."),
         ("Consultivo", "Pergunta antes de oferecer."),
         ("Humano", "Entende o que existe por trás dos números."),
         ("Elegante", "Sofisticação sem ostentação."),
         ("Acessível", "Torna assuntos complexos compreensíveis."),
     ]},

    # 56
    {"tipo": "camadas", "eyebrow": "O que a marca não deve ser",
     "titulo": "O que a marca não deve ser",
     "camadas": [
         ("Alarmista", "Não usa medo para pressionar."),
         ("Exibicionista", "Não transforma conquista em ostentação."),
         ("Técnica demais", "Conhecimento deve aproximar."),
         ("Comercial demais",
          "O produto nunca deve parecer anterior ao diagnóstico."),
         ("Genérica",
          "Não deve repetir apenas “segurança, proteção e tranquilidade” sem "
          "traduzir seu significado."),
     ]},

    # 57
    {"tipo": "alternativas", "eyebrow": "Princípio de comunicação",
     "titulo": "Provar, não proclamar",
     "rot_evitar": "Em vez de dizer", "rot_preferir": "Mostrar",
     "pares": [
         ("Sou referência.", "Reconhecimento comprovado por terceiros."),
         ("Tenho experiência.", "Raciocínio e casos reais."),
         ("Sou um dos melhores.", "Resultados contextualizados."),
     ]},

    # 58
    {"tipo": "foto_cheia", "foto": IMG[14], "foco": 0.12, "veu": 0.60,
     "linhas": ["Ele não precisa aparecer mais.",
                "Precisa fazer sua competência aparecer mais."],
     "tam": 36},

    # 59
    {"tipo": "palavras", "eyebrow": "Tom de voz",
     "titulo": "Tom de voz",
     "palavras": ["Claro sem ser simplista", "Seguro sem ser arrogante",
                  "Humano sem ser dramático",
                  "Sofisticado sem ser ostentatório",
                  "Consultivo sem ser burocrático", "Direto sem ser frio"],
     "grade": 2, "tam": 22},

    # 60
    {"tipo": "alternativas", "eyebrow": "Como a marca fala",
     "titulo": "Como a marca fala",
     "pares": [
         ("Você pode morrer amanhã.",
          "Quem depende financeiramente de você hoje?"),
         ("Você precisa contratar um seguro de vida.",
          "Antes de pensar em produto, precisamos entender o impacto "
          "financeiro que uma ausência ou incapacidade produziria."),
         ("Proteja-se antes que seja tarde.",
          "Algumas decisões são melhores quando ainda existe tempo para "
          "escolher."),
     ]},

    # 61
    {"tipo": "alternativas", "eyebrow": "Como falar das próprias conquistas",
     "titulo": "Não como autocelebração. Como evidência.",
     "tam_titulo": 34,
     "foto": IMG[6], "lado": "cima", "fatia": 0.30, "foco": 0.22,
     "rot_evitar": "Não", "rot_preferir": "Sim",
     "pares": [
         ("Olha onde eu cheguei.",
          "Esse reconhecimento representa dez anos de consistência, "
          "atendimento e confiança de clientes."),
     ]},

    # ——— 09 MANIFESTO E SÍNTESE
    {"tipo": "divisor", "numero": "09", "nome": "Manifesto e síntese final"},

    # 63
    {"tipo": "manifesto", "eyebrow": "Manifesto",
     "paragrafos": [
         "Há coisas que levam anos para construir. Uma carreira. Uma família. "
         "Uma empresa. Um patrimônio. Uma história.",
         "E nenhuma delas deveria ficar completamente dependente daquilo que "
         "não podemos controlar.",
         "Planejar não é esperar que algo dê errado. É reconhecer o valor "
         "daquilo que deu certo.",
         "É pensar antes. Enquanto existe tempo. Enquanto existem "
         "alternativas. Enquanto podemos escolher.",
         "Nem tudo pode ser previsto. Mas muito pode ser preparado.",
         "E quando existe preparação, o imprevisto pode mudar a vida sem "
         "necessariamente decidir sozinho tudo o que virá depois.",
         "Porque proteção não existe apenas para preservar dinheiro. Existe "
         "para preservar possibilidades.",
     ],
     "assinatura": "LUCAS MARTINI  |  PROTEÇÃO & SUCESSÃO"},

    # 64
    {"tipo": "ficha", "eyebrow": "A marca em uma página",
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
          "Especialista em proteção e sucessão para pessoas, famílias e "
          "empresas que desejam preservar o que construíram e manter "
          "possibilidades diante do imprevisto e das transições da vida."),
         ("Proposta de valor",
          "Estruturar proteção e sucessão de forma personalizada para "
          "preservar recursos, patrimônio, continuidade e capacidade de "
          "escolha."),
         ("Princípio de comunicação", "Provar, não proclamar."),
         ("Personalidade", "Autoridade discreta."),
     ]},

    # 65
    {"tipo": "foto_cheia", "foto": IMG[12], "foco": 0.42, "veu": 0.60,
     "eyebrow": "A lógica da marca",
     "linhas": ["Nem tudo pode ser previsto.",
                "Mas muito pode ser preparado."]},

    # 66
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.45, "veu": 0.66,
     "eyebrow": "A grande síntese",
     "linhas": ["Lucas não trabalha para controlar o futuro.",
                "Trabalha para preservar escolhas",
                "quando o futuro muda."],
     "tam": 36},

    # 67
    {"tipo": "foto_cheia", "foto": IMG[1], "foco": 0.35, "veu": 0.64,
     "linhas": ["Preparar antes.",
                "Proteger o que foi construído.",
                "Preservar a possibilidade de continuar."],
     "apoio": "Lucas Martini  |  Proteção & Sucessão"},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
