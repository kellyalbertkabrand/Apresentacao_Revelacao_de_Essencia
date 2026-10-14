# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — Lucas Martini | Proteção & Sucessão

Só conteúdo. A identidade visual é a de sempre: painel claro sobre a textura
de ondas, Outfit, acento terracota (padrao-ka/ka_layout.py e
padrao-ka/ka_paginas.py).

O que mudou foi a DIAGRAMAÇÃO DO TEXTO, e só ela. A Kelly foi direta:

    "Tem título, aí tem um títulozinho menor, aí tem outro menorzinho, aí
     uma frase maior, aí uma linha. Não quero isso. Um título e um texto
     num slide. Um título e um texto no slide."

Então cada página aqui tem **um título e um bloco de texto** — um só corpo,
uma só cor, sem eyebrow, sem linha de abertura em outro tamanho, sem frase
de destaque com filete embaixo. Onde o conteúdo é mesmo de campos (causa,
arquétipos, Golden Circle, arquitetura, pilares), ele vira colunas: rótulo e
texto, lado a lado — nunca empilhado.

Conteúdo: o texto da Kelly, na ordem dela, com a essência em 01 e o Lucas em
02. As marcas de origem que vieram coladas ("Identidade Verbal - Lucas
José…", "mft-nwyj-ixz…", "IKIGAI Empresarial…") são referências da
ferramenta dela, não conteúdo de slide, e ficaram de fora.
"""

MARCA = "Lucas Martini"
DOCUMENTO = "Base Estratégica da Marca"
RODAPE = False          # sem pilula e sem logo no pe, como ela pediu
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

    {"tipo": "sumario", "grade": 2, "itens": [
        ("01", "Essência da marca"),
        ("02", "Quem é Lucas Martini"),
        ("03", "Causa, liderança e tribo"),
        ("04", "Princípio central"),
        ("05", "Público-alvo e persona"),
        ("06", "Arquétipos da marca"),
        ("07", "Pilares da marca"),
        ("08", "DNA da marca"),
        ("09", "Voz da marca"),
        ("10", "Tom de voz"),
        ("11", "Posicionamento"),
        ("12", "Golden Circle"),
        ("13", "Arquitetura da marca"),
        ("14", "Manifesto"),
    ]},

    # 01 — ESSÊNCIA DA MARCA
    {"tipo": "texto", "foto": IMG[3], "lado": "direita",
     "titulo": "Essência da marca",
     "paragrafos": [
         "Construir segurança para preservar liberdade de escolha.",
         "A marca parte da ideia de que nem tudo pode ser previsto, mas é "
         "possível se preparar para que um imprevisto não elimine "
         "alternativas nem comprometa tudo o que foi construído.",
     ]},

    # 02 — QUEM É LUCAS MARTINI
    {"tipo": "texto", "foto": IMG[1], "lado": "esquerda",
     "titulo": "Quem é Lucas Martini",
     "paragrafos": [
         "Especialista em Proteção & Sucessão, com mais de dez anos de "
         "atuação.",
         "Sua experiência no mercado financeiro e a vivência com famílias e "
         "empresas deram origem a uma atuação consultiva, baseada em "
         "planejamento, personalização, relacionamento e acompanhamento.",
     ]},

    # 03 — CAUSA, LIDERANÇA E TRIBO
    {"tipo": "colunas", "titulo": "Causa, liderança e tribo",
     "colunas": [
         ("Causa",
          "Ampliar a cultura de proteção e preparação antes do imprevisto."),
         ("Liderança",
          "Ajudar pessoas a enxergar riscos, impactos e possibilidades antes "
          "que a urgência determine as decisões."),
         ("Tribo",
          "Pessoas que carregam responsabilidade sobre renda, família, "
          "patrimônio ou empresa."),
     ]},

    # 04 — PRINCÍPIO CENTRAL
    {"tipo": "declaracao",
     "linhas": ["O que levou anos para ser construído",
                "não deveria ficar entregue ao acaso."],
     "apoio": "Planejamento é uma forma de proteger conquistas e preservar "
              "possibilidades diante do que não pode ser controlado."},

    # 05 — PÚBLICO-ALVO E PERSONA
    {"tipo": "texto", "foto": IMG[13], "lado": "direita",
     "titulo": "Público-alvo e persona",
     "paragrafos": [
         "Profissionais, empresários, sócios e famílias que possuem "
         "responsabilidades financeiras, patrimoniais ou sucessórias e "
         "querem proteger o que construíram.",
         "A persona central é alguém que entende o valor das suas conquistas "
         "e quer se preparar para que um imprevisto não comprometa sua "
         "família, seu patrimônio ou sua empresa.",
     ]},

    # 06 — ARQUÉTIPOS DA MARCA
    {"tipo": "colunas", "titulo": "Arquétipos da marca",
     "colunas": [
         ("Sábio · principal",
          "Traduz complexidade, orienta decisões e transforma informação em "
          "planejamento."),
         ("Cuidador · secundário",
          "Protege, acompanha e assume responsabilidade sobre decisões que "
          "afetam pessoas, famílias e empresas."),
     ],
     "fecho": "Síntese estratégica a partir da atuação consultiva, do "
              "relacionamento e da responsabilidade descritos pelo próprio "
              "Lucas."},

    # 07 — PILARES DA MARCA
    {"tipo": "camadas", "titulo": "Pilares da marca",
     "camadas": [
         ("Proteção", "Preservar o que foi construído."),
         ("Planejamento", "Antecipar riscos e criar alternativas."),
         ("Personalização", "Construir soluções a partir de cada realidade."),
         ("Confiança", "Sustentar relações de longo prazo."),
         ("Continuidade",
          "Permitir que família, patrimônio e empresa possam seguir."),
     ]},

    # 08 — DNA DA MARCA
    {"tipo": "texto", "foto": IMG[9], "lado": "esquerda",
     "titulo": "DNA da marca",
     "paragrafos": [
         "Proteção. Confiança. Responsabilidade. Personalização. "
         "Continuidade.",
         "Esses são os atributos que devem permanecer presentes em qualquer "
         "expressão da marca, do atendimento à comunicação.",
     ]},

    # 09 — VOZ DA MARCA
    {"tipo": "texto",
     "titulo": "Voz da marca",
     "paragrafos": [
         "A voz de Lucas deve transmitir conhecimento sem distanciamento e "
         "segurança sem arrogância.",
         "Clara, segura, humana, elegante e consultiva.",
     ]},

    # 10 — TOM DE VOZ
    {"tipo": "colunas", "titulo": "Tom de voz",
     "colunas": [
         ("Técnico", "sem ser complicado."),
         ("Direto", "sem ser frio."),
         ("Seguro", "sem ser arrogante."),
         ("Humano", "sem dramatização."),
         ("Sofisticado", "sem ostentação."),
     ]},

    # 11 — POSICIONAMENTO
    {"tipo": "texto", "foto": IMG[12], "lado": "direita",
     "titulo": "Posicionamento",
     "paragrafos": [
         "Lucas Martini é especialista em Proteção & Sucessão para pessoas, "
         "famílias e empresas que querem preservar o que construíram e "
         "manter possibilidades diante de imprevistos e transições.",
         "Proteção & Sucessão para o que precisa continuar.",
     ]},

    # 12 — GOLDEN CIRCLE
    {"tipo": "colunas", "titulo": "Golden Circle",
     "colunas": [
         ("Por quê",
          "Preservar possibilidades quando a vida foge do previsto."),
         ("Como",
          "Com planejamento personalizado, conhecimento, relacionamento e "
          "acompanhamento."),
         ("O quê",
          "Estratégias de proteção pessoal, familiar, empresarial e "
          "sucessória."),
     ]},

    # 13 — ARQUITETURA DA MARCA
    {"tipo": "colunas", "titulo": "Arquitetura da marca",
     "colunas": [
         ("Marca pessoal", "Lucas Martini"),
         ("Atuação", "Proteção & Sucessão"),
         ("Assinatura empresarial", "Martini | Proteção & Sucessão"),
         ("Monograma", "LM"),
     ],
     "fecho": "O uso de “Martini” ganha força porque é a forma pela qual "
              "Lucas já é reconhecido em seu convívio pessoal e "
              "profissional."},

    # 14 — MANIFESTO
    {"tipo": "manifesto", "titulo": "Manifesto",
     "paragrafos": [
         "Há coisas que levam anos para construir. Uma carreira. Uma "
         "família. Uma empresa. Um patrimônio. Uma história.",
         "Nem tudo pode ser previsto. Mas muito pode ser preparado.",
         "Planejar é proteger o que foi construído enquanto ainda existe "
         "tempo para escolher.",
         "Porque proteção não existe apenas para preservar patrimônio. "
         "Existe para preservar possibilidades.",
     ],
     "assinatura": "LUCAS MARTINI  |  PROTEÇÃO & SUCESSÃO"},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
