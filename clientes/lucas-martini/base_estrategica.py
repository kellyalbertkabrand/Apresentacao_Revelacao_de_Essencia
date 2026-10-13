# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — Lucas Martini | Proteção & Sucessão

Só conteúdo. Layout em padrao-ka/ka_layout.py, arquétipos de página em
padrao-ka/ka_paginas.py.

Reescrita a partir do texto novo da Kelly (outubro/2026): 38 páginas de
conteúdo, UMA ideia por página, menos texto e hierarquia simples. A versão
anterior tinha 30 páginas densas; esta tem mais páginas e muito menos texto
em cada uma — era exatamente o pedido.

Estrutura: abertura, capa, sumário, nove seções com divisor e os 38 slides
do roteiro, fecho. 51 páginas.

As fotografias entram em tira vertical ou tela cheia; o recorte sai de
`assets/rostos.json` para que o rosto nunca seja cortado. A imagem 07 ficou
de fora, como pedido.
"""

MARCA = "Lucas Martini"
DOCUMENTO = "Base Estratégica da Marca"
RODAPE = False          # a Kelly pediu a Base sem rodape
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

    {"tipo": "capa",
     "titulo": ["BASE ESTRATÉGICA", "DA MARCA"],
     "subtitulo": ["Lucas Martini", "Proteção & Sucessão"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

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

    # ——————————————————————— 01 LEITURA DO MOMENTO DA MARCA
    {"tipo": "divisor", "numero": "01", "nome": "Leitura do momento",
     "apoio": "O que a marca já tem, e o que ainda não aparece."},

    # 01
    {"tipo": "texto", "eyebrow": "Leitura do momento", "foto": IMG[1],
     "lado": "direita",
     "titulo": "A autoridade já existe",
     "lead": "Dez anos de atuação, uma carteira construída por "
             "relacionamento, resultados e reconhecimento.",
     "destaque": "Hoje, grande parte do negócio acontece por recomendação."},

    # 02
    {"tipo": "palavras", "eyebrow": "Leitura do momento",
     "titulo": "A entrega é maior do que a percepção",
     "lead": "Na prática, existe:",
     "palavras": ["Experiência", "Personalização", "Relacionamento",
                  "Pós-venda", "Resultados", "Reconhecimento"],
     "destaque": "A marca ainda não comunica tudo isso com a mesma força."},

    # 03
    {"tipo": "declaracao", "eyebrow": "A evolução", "marcar": True,
     "linhas": ["De seguro como produto",
                "para proteção como estratégia."],
     "apoio": "De corretor de seguros para especialista em Proteção & "
              "Sucessão. Sua atuação já envolve realidade financeira, "
              "familiar, empresarial e patrimonial."},

    # 04
    {"tipo": "texto", "eyebrow": "Leitura do momento", "foto": IMG[14],
     "lado": "esquerda",
     "titulo": "Autoridade discreta, mas presente",
     "lead": "A discrição faz parte do seu perfil.",
     "destaque": "O desafio é tornar mais visíveis a experiência, os "
                 "resultados e o conhecimento que já sustentam sua atuação."},

    # ———————————————————————— 02 DEFINIÇÃO CENTRAL DA MARCA
    {"tipo": "divisor", "numero": "02", "nome": "Definição central",
     "apoio": "O que Lucas entrega, abaixo do produto."},

    # 05
    {"tipo": "texto", "eyebrow": "Definição central", "foto": IMG[11],
     "lado": "direita",
     "titulo": "O seguro é parte da solução",
     "lead": "Seu trabalho começa antes do produto.",
     "destaque": "Você entende a realidade do cliente, identifica "
                 "vulnerabilidades e estrutura uma proteção adequada a cada "
                 "situação."},

    # 06
    {"tipo": "palavras", "eyebrow": "Definição central",
     "titulo": "O que você entrega",
     "lead": "Estratégias personalizadas de proteção e sucessão para "
             "preservar:",
     "palavras": ["Renda", "Família", "Patrimônio", "Empresas",
                  "Possibilidades"]},

    # 07
    {"tipo": "camadas", "eyebrow": "Definição central",
     "titulo": "O valor em camadas",
     "camadas": [
         ("Seguro", "Um dos instrumentos."),
         ("Planejamento", "O método."),
         ("Proteção & Sucessão", "A atuação."),
         ("Continuidade", "O território."),
         ("Liberdade de escolha",
          "Poder decidir sem que a urgência decida por você."),
     ]},

    # 08
    {"tipo": "foto_cheia", "foto": IMG[2], "foco": 0.40, "veu": 0.66,
     "eyebrow": "Definição central",
     "linhas": ["Não é apenas dinheiro."],
     "apoio": "É a estrutura que permite que uma família, uma empresa, um "
              "patrimônio ou um projeto continue existindo mesmo quando algo "
              "foge do previsto."},

    # ————————————————————————— 03 CAUSA, LIDERANÇA E TRIBO
    {"tipo": "divisor", "numero": "03", "nome": "Causa e tribo",
     "apoio": "No que a marca acredita, e para quem ela fala."},

    # 09
    {"tipo": "declaracao", "eyebrow": "A causa",
     "linhas": ["Preparar antes de precisar."],
     "apoio": "Proteção e sucessão não começam quando o problema acontece. "
              "Começam enquanto ainda existem tempo e alternativas para "
              "decidir."},

    # 10
    {"tipo": "lista", "eyebrow": "A causa",
     "titulo": "A mudança que a marca defende",
     "itens": ["Do improviso para o planejamento.",
               "Da reação para a antecipação.",
               "Do produto para a estratégia.",
               "Da urgência para a escolha."],
     "marcar_ultimo": True},

    # 11
    {"tipo": "texto", "eyebrow": "Liderança", "foto": IMG[13],
     "lado": "esquerda",
     "titulo": "Ajudar a enxergar antes",
     "lead": "Uma parte importante da sua atuação é fazer o cliente perceber "
             "riscos e consequências que ainda não foram considerados.",
     "destaque": "Não para gerar medo, mas para permitir preparação."},

    # 12
    {"tipo": "palavras", "eyebrow": "A tribo",
     "titulo": "Quem depende das suas decisões",
     "lead": "Pessoas para quem algo importante depende das suas decisões.",
     "palavras": ["Profissionais", "Pilares financeiros de famílias",
                  "Empresários e sócios", "Pessoas-chave",
                  "Famílias com patrimônio", "Responsáveis por sucessões"],
     "tam": 23},

    # ——————————————————————————————————— 04 GOLDEN CIRCLE
    {"tipo": "divisor", "numero": "04", "nome": "Golden Circle",
     "apoio": "Por quê, como e o quê — nesta ordem."},

    # 13
    {"tipo": "declaracao", "eyebrow": "Por quê", "marcar": True,
     "linhas": ["Preservar possibilidades."],
     "apoio": "Para que um imprevisto não tenha poder para decidir sozinho o "
              "que acontece depois."},

    # 14
    {"tipo": "lista", "eyebrow": "Como",
     "titulo": "Conhecer antes de recomendar",
     "itens": ["Entender a realidade.",
               "Identificar vulnerabilidades.",
               "Projetar impactos.",
               "Estruturar alternativas.",
               "Acompanhar ao longo do tempo."],
     "marcar_ultimo": True},

    # 15
    {"tipo": "palavras", "eyebrow": "O quê",
     "titulo": "As quatro frentes",
     "palavras": ["Proteção pessoal e familiar", "Proteção empresarial",
                  "Sucessão familiar e patrimonial", "Sucessão empresarial"],
     "tam": 32, "grade": 1},

    # ————————————————————— 05 PROPOSTA DE VALOR E POSICIONAMENTO
    {"tipo": "divisor", "numero": "05", "nome": "Posicionamento",
     "apoio": "O que a marca promete e onde ela se coloca."},

    # 16
    {"tipo": "foto_cheia", "foto": IMG[12], "foco": 0.42, "veu": 0.64,
     "eyebrow": "Proposta de valor",
     "linhas": ["Proteção personalizada."],
     "apoio": "Estruturar proteção e sucessão de acordo com a realidade de "
              "cada cliente, preservando recursos e alternativas diante de "
              "imprevistos e transições."},

    # 17
    {"tipo": "palavras", "eyebrow": "O diferencial",
     "titulo": "O diferencial não está apenas no produto",
     "lead": "Está em:",
     "palavras": ["Diagnóstico", "Personalização", "Conhecimento",
                  "Relacionamento", "Pós-venda", "Presença"],
     "destaque": "Atendimento consultivo e pós-venda são diferenciais "
                 "reconhecidos pelo próprio Lucas."},

    # 18
    {"tipo": "texto", "eyebrow": "Posicionamento", "foto": IMG[8],
     "lado": "direita",
     "titulo": "A relação não termina na venda",
     "lead": "O acompanhamento continua depois da contratação.",
     "destaque": "Orientação, pós-venda e presença fazem parte da entrega."},

    # 19
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.38, "veu": 0.66,
     "eyebrow": "Posicionamento",
     "linhas": ["Proteção & Sucessão",
                "para o que precisa continuar."],
     "apoio": "Lucas Martini atua com pessoas, famílias e empresas que querem "
              "preservar o que construíram e manter possibilidades diante de "
              "imprevistos e transições."},

    # ———————————————————————————— 06 ARQUITETURA DE MARCA
    {"tipo": "divisor", "numero": "06", "nome": "Arquitetura",
     "apoio": "O nome no centro, e as frentes que ele sustenta."},

    # 20
    {"tipo": "palavras", "eyebrow": "Arquitetura", "titulo": "Lucas Martini",
     "lead": "É a marca pessoal.",
     "palavras": ["A autoridade.", "O conhecimento.", "A relação.",
                  "A voz."],
     "grade": 1, "tam": 29},

    # 21
    {"tipo": "texto", "eyebrow": "Arquitetura", "foto": IMG[1],
     "lado": "esquerda",
     "titulo": "Martini",
     "lead": "Martini já é a forma pela qual Lucas é reconhecido em "
             "diferentes ambientes.",
     "destaque": "Isso permite que o sobrenome ganhe força também como "
                 "assinatura empresarial."},

    # 22
    {"tipo": "camadas", "eyebrow": "Arquitetura",
     "titulo": "A arquitetura da marca",
     "camadas": [
         ("Marca pessoal", "Lucas Martini"),
         ("Atuação", "Proteção & Sucessão"),
         ("Assinatura empresarial", "Martini | Proteção & Sucessão"),
         ("Monograma", "LM"),
     ]},

    # 23
    {"tipo": "declaracao", "eyebrow": "Proteção & Sucessão",
     "linhas": ["Primeiro proteger,",
                "depois estruturar a sucessão."],
     "apoio": "A ordem também expressa a lógica da atuação."},

    # 24
    {"tipo": "texto", "eyebrow": "Arquitetura", "foto": IMG[6],
     "lado": "direita",
     "titulo": "O papel das seguradoras",
     "lead": "As seguradoras fornecem instrumentos.",
     "destaque": "Lucas analisa, escolhe e estrutura a estratégia de acordo "
                 "com a necessidade do cliente."},

    # ———————————————————— 07 TERRITÓRIOS, PILARES E PÚBLICO
    {"tipo": "divisor", "numero": "07", "nome": "Territórios e público",
     "apoio": "Do que a marca fala, como atua e com quem."},

    # 25
    {"tipo": "lista", "eyebrow": "O território central",
     "titulo": "Continuidade",
     "itens": ["Continuar a renda.",
               "Continuar a empresa.",
               "Preservar o patrimônio.",
               "Manter a estrutura familiar.",
               "Dar continuidade aos projetos."],
     "marcar_ultimo": True},

    # 26
    {"tipo": "palavras", "eyebrow": "Territórios da marca",
     "titulo": "Do que a marca fala",
     "palavras": ["Proteção", "Sucessão", "Planejamento",
                  "Dignidade financeira", "Continuidade"]},

    # 27
    {"tipo": "camadas", "eyebrow": "Os pilares",
     "titulo": "Como a marca atua", "foto": IMG[9], "lado": "direita",
     "camadas": [
         ("Antecipação", "Pensar antes."),
         ("Personalização", "Construir para cada realidade."),
         ("Responsabilidade", "Entender o peso das decisões."),
         ("Confiança", "Construir relações de longo prazo."),
         ("Presença", "Continuar depois da contratação."),
     ]},

    # 28
    {"tipo": "lista", "eyebrow": "Público",
     "titulo": "Quem a marca atende",
     "itens": ["Profissionais cuja renda depende da própria capacidade de "
               "trabalho.",
               "Pilares financeiros de famílias.",
               "Empresários e sócios.",
               "Famílias e empresas com patrimônio e questões sucessórias."]},

    # 29
    {"tipo": "foto_cheia", "foto": IMG[5], "foco": 0.40, "veu": 0.66,
     "eyebrow": "O que une esse público",
     "linhas": ["Não é idade ou profissão."],
     "apoio": "É a responsabilidade sobre algo que precisa ser protegido ou "
              "continuar."},

    # ——————————————————————— 08 PERSONALIDADE E TOM DE VOZ
    {"tipo": "divisor", "numero": "08", "nome": "Personalidade e voz",
     "apoio": "Como a marca se comporta e como ela fala."},

    # 30
    {"tipo": "declaracao", "eyebrow": "Personalidade",
     "linhas": ["Competência sem ostentação.",
                "Segurança sem arrogância.",
                "Presença sem exposição excessiva."],
     "tam": 40},

    # 31
    {"tipo": "palavras", "eyebrow": "Personalidade",
     "titulo": "Autoridade discreta",
     "palavras": ["Seguro", "Confiável", "Preparado", "Consultivo", "Humano",
                  "Discreto"]},

    # 32
    {"tipo": "lista", "eyebrow": "Tom de voz",
     "titulo": "Como a marca fala",
     "itens": ["Claro, sem simplificar demais.",
               "Seguro, sem arrogância.",
               "Humano, sem dramatização.",
               "Sofisticado, sem ostentação.",
               "Consultivo, sem burocracia.",
               "Direto, sem frieza."]},

    # 33
    {"tipo": "palavras", "eyebrow": "Tom de voz",
     "titulo": "Provar, não proclamar",
     "lead": "A comunicação deve mostrar a autoridade por meio de:",
     "palavras": ["Conhecimento", "Casos", "Resultados", "Reconhecimentos",
                  "Depoimentos", "Experiência"]},

    # 34
    {"tipo": "lista", "eyebrow": "O papel do conteúdo", "foto": IMG[10],
     "lado": "esquerda",
     "titulo": "Não é aparecer por aparecer",
     "lead": "É usar conhecimento e experiência para:",
     "itens": ["Despertar", "Explicar", "Orientar", "Construir confiança"],
     "marcar_ultimo": True},

    # ——————————————————————— 09 MANIFESTO E SÍNTESE FINAL
    {"tipo": "divisor", "numero": "09", "nome": "Manifesto",
     "apoio": "A marca em palavras, e a marca em uma página."},

    # 35
    {"tipo": "manifesto", "eyebrow": "Manifesto",
     "paragrafos": [
         "Há coisas que levam anos para construir.",
         "Uma carreira. Uma família. Uma empresa. Um patrimônio. Uma "
         "história.",
         "Nem tudo pode ser previsto.",
         "Mas muito pode ser preparado.",
         "Proteção é preservar possibilidades quando a vida foge do "
         "previsto.",
     ],
     "assinatura": "LUCAS MARTINI  |  PROTEÇÃO & SUCESSÃO"},

    # 36
    {"tipo": "ficha", "eyebrow": "A marca",
     "titulo": "Lucas Martini · Proteção & Sucessão",
     "tam_titulo": 36,
     "campos": [
         ("Crença",
          "O que levou anos para ser construído não deveria ficar entregue ao "
          "acaso."),
         ("Razão de ser", "Preservar possibilidades."),
         ("Território", "Continuidade."),
         ("Personalidade", "Autoridade discreta."),
     ]},

    # 37
    {"tipo": "declaracao", "eyebrow": "Síntese", "marcar": True,
     "linhas": ["Preparar antes.",
                "Proteger o que foi construído."],
     "apoio": "Preservar recursos, alternativas e possibilidades para que "
              "aquilo que importa possa continuar."},

    # 38
    {"tipo": "foto_cheia", "foto": IMG[10], "foco": 0.42, "veu": 0.68,
     "eyebrow": "A marca",
     "linhas": ["Quando algo muda,",
                "ainda precisam existir escolhas."],
     "apoio": "É isso que a proteção bem estruturada torna possível."},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
