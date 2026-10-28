# -*- coding: utf-8 -*-
"""
PLANO DE CONTEÚDO — Lucas Martini | Proteção & Sucessão

Só conteúdo. Mesma identidade e mesma diagramação da Base Estratégica:
painel claro sobre a textura de ondas, Outfit, acento terracota — e **um
título e um bloco de texto por página**. Sem eyebrow, sem linha de abertura
em outro corpo, sem frase de destaque com filete embaixo. Onde o conteúdo é
de campos (eixos, distribuição, formatos, cronograma), ele vira colunas ou
camadas: rótulo e texto lado a lado.

Conteúdo: o texto da Kelly, na ordem dela. As marcas de origem que vieram
coladas ("mft-nwyj-ixz…", "IKIGAI Empresarial - Lucas Jose…") são
referências da ferramenta dela, não conteúdo de slide, e ficaram de fora.
"""

MARCA = "Lucas Martini"
DOCUMENTO = "Plano de Conteúdo"
RODAPE = False
ARQUIVO = "Plano-de-Conteudo-Lucas-Martini"

IMG = {
    1: "01_retrato_corporativo_prudential.png",
    3: "03_lucas_janela_entardecer.png",
    8: "08_lucas_aperto_de_maos_cliente.png",
    9: "09_lucas_analisando_documentos.png",
    11: "11_lucas_consulta_individual.png",
    12: "12_lucas_caminhando_janela.png",
    13: "13_lucas_ouvindo_casal.png",
    14: "14_retrato_lucas_corredor.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    {"tipo": "capa",
     "titulo": ["PLANO DE", "CONTEÚDO"],
     "subtitulo": ["Lucas Martini", "Proteção & Sucessão"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "sumario", "itens": [
        ("01", "Objetivo do conteúdo"),
        ("02", "Linha editorial"),
        ("03", "Distribuição do conteúdo"),
        ("04", "Formatos"),
        ("05", "Cronograma de publicações"),
        ("06", "Ciclo mensal"),
        ("07", "Regra central e direção"),
    ]},

    # ——————————————————————————————— 01 OBJETIVO
    {"tipo": "texto", "foto": IMG[14], "lado": "direita",
     "titulo": "Objetivo do conteúdo",
     "paragrafos": [
         "Transformar a experiência e o conhecimento que já existem em "
         "autoridade percebida.",
         "A lógica não é produzir conteúdo para volume de leads, mas "
         "fortalecer uma atuação que hoje já acontece fortemente por "
         "recomendação.",
     ]},

    {"tipo": "lista", "titulo": "O que o conteúdo **precisa fazer**",
     "itens": ["Educar antes de vender.",
               "Despertar necessidades que muitas vezes não são percebidas.",
               "Reforçar confiança.",
               "Manter-se presente na memória de clientes e indicações.",
               "Gerar conversas qualificadas."],
     "marcar_ultimo": True},

    # ——————————————————————————— 02 LINHA EDITORIAL
    {"tipo": "camadas", "titulo": "Linha editorial",
     "camadas": [
         ("01 · Despertar", "Proteção antes do imprevisto."),
         ("02 · Ampliar", "Sucessão e continuidade."),
         ("03 · Demonstrar", "Planejamento na prática."),
         ("04 · Educar", "Proteção em vida."),
         ("05 · Provar", "Prova e autoridade."),
     ]},

    {"tipo": "texto", "foto": IMG[13], "lado": "esquerda",
     "titulo": "01 · **Proteção** antes do imprevisto",
     "tam_titulo": 38,
     "paragrafos": [
         "Conteúdos que façam a pessoa perceber vulnerabilidades que "
         "normalmente só seriam consideradas quando algo acontece.",
         "Temas: renda, incapacidade, doenças, acidentes, dependência "
         "financeira e proteção familiar. O papel deste eixo é despertar.",
     ]},

    {"tipo": "texto",
     "titulo": "02 · **Sucessão** e continuidade",
     "tam_titulo": 38,
     "paragrafos": [
         "Mostrar que patrimônio e empresa precisam de estratégia para "
         "continuar.",
         "Temas: sucessão familiar, sucessão empresarial, liquidez, "
         "inventário, cotas, pessoa-chave e continuidade da empresa. O papel "
         "deste eixo é ampliar a percepção sobre o trabalho de Lucas.",
     ]},

    {"tipo": "texto", "foto": IMG[9], "lado": "direita",
     "titulo": "03 · **Planejamento** na prática",
     "tam_titulo": 38,
     "paragrafos": [
         "Traduzir situações complexas para decisões simples e "
         "compreensíveis.",
         "Temas: como avaliar uma proteção, perguntas que precisam ser "
         "feitas, erros de planejamento, cenários e decisões. O papel deste "
         "eixo é demonstrar conhecimento consultivo.",
     ]},

    {"tipo": "texto",
     "titulo": "04 · **Proteção em vida**",
     "tam_titulo": 38,
     "paragrafos": [
         "Romper a associação de seguro apenas com morte. O próprio Lucas "
         "destaca que o seguro de vida também é proteção em vida, e que essa "
         "dimensão ainda é pouco compreendida.",
         "Temas: acidentes, invalidez, doença, perda de capacidade de "
         "trabalho, manutenção de renda e dignidade financeira. O papel "
         "deste eixo é educar e mudar percepção.",
     ]},

    {"tipo": "texto", "foto": IMG[8], "lado": "esquerda",
     "titulo": "05 · **Prova** e autoridade",
     "tam_titulo": 38,
     "paragrafos": [
         "Mostrar aquilo que já foi construído sem transformar a comunicação "
         "em autopromoção.",
         "Temas: reconhecimentos, eventos, estudos, bastidores, "
         "aprendizados, casos possíveis de serem compartilhados e "
         "depoimentos. O papel deste eixo é provar, não proclamar.",
     ]},

    # ————————————————————————————— 03 DISTRIBUIÇÃO
    {"tipo": "camadas", "titulo": "**Distribuição** do conteúdo",
     "camadas": [
         ("40%", "Educação e planejamento: proteção, riscos, escolhas e "
                 "tomada de decisão."),
         ("25%", "Sucessão e continuidade: família, patrimônio e empresa."),
         ("15%", "Proteção em vida: acidente, doença, invalidez e renda."),
         ("10%", "Autoridade: reconhecimentos, eventos e conhecimento "
                 "adquirido."),
         ("10%", "Bastidores e relacionamento: rotina, atendimento, estudos "
                 "e visão pessoal sobre o trabalho."),
     ]},

    # ——————————————————————————————— 04 FORMATOS
    {"tipo": "colunas", "titulo": "Formatos",
     "colunas": [
         ("Reels",
          "O principal formato. Vídeos curtos e diretos, com uma pergunta ou "
          "uma situação real como ponto de partida."),
         ("Carrossel",
          "Para organizar raciocínio: sucessão, planejamento, erros, "
          "checklists, comparações e passo a passo."),
         ("Card único",
          "Para uma ideia forte, sozinha na página."),
         ("Stories",
          "A parte espontânea: bastidores, agenda, eventos, perguntas de "
          "clientes, estudos e reuniões — sem virar reality show."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Se você ficasse seis meses sem trabalhar,",
                "sua renda continuaria existindo?"],
     "apoio": "O ponto de partida de um reel é sempre uma pergunta ou uma "
              "situação real — nunca um produto."},

    # ——————————————————————————————— 05 CRONOGRAMA
    {"tipo": "colunas", "titulo": "**Cronograma** de publicações",
     "colunas": [
         ("Segunda", "Reel educativo, para despertar."),
         ("Quarta", "Carrossel ou card, para aprofundar."),
         ("Sexta", "Reel, caso ou autoridade, para construir confiança."),
     ],
     "fecho": "Três conteúdos por semana — suficiente para construir "
              "presença sem criar uma rotina impossível. Stories em três a "
              "cinco dias por semana, aproveitando situações reais da "
              "rotina."},

    # ————————————————————————————— 06 CICLO MENSAL
    {"tipo": "lista", "titulo": "Ciclo mensal · semana 1",
     "itens": ["Reel: você sabe quanto tempo sua família manteria o padrão "
               "de vida sem a sua renda?",
               "Carrossel: cinco riscos financeiros que uma família "
               "normalmente não calcula.",
               "Reel: seguro de vida não é só sobre morte."]},

    {"tipo": "lista", "titulo": "Ciclo mensal · semana 2",
     "itens": ["Reel: sua empresa continuaria funcionando sem você?",
               "Carrossel: o que acontece com uma empresa quando uma "
               "pessoa-chave sai da operação?",
               "Autoridade: bastidor, reunião, estudo ou experiência "
               "profissional."]},

    {"tipo": "lista", "titulo": "Ciclo mensal · semana 3",
     "itens": ["Reel: ter patrimônio não significa ter liquidez.",
               "Carrossel: holding resolve toda a sucessão?",
               "Reel: o que precisa ser pensado antes de um inventário."]},

    {"tipo": "lista", "titulo": "Ciclo mensal · semana 4",
     "itens": ["Reel: o imprevisto pode ser um problema — ou não.",
               "Carrossel: o que analisar antes de contratar uma proteção.",
               "Prova: caso, aprendizado, reconhecimento ou depoimento."]},

    # ———————————————————————— 07 REGRA CENTRAL E DIREÇÃO
    {"tipo": "texto", "foto": IMG[11], "lado": "direita",
     "titulo": "A **regra central**",
     "paragrafos": [
         "O conteúdo de Lucas não deve começar pelo produto. Deve começar "
         "por uma situação, uma pergunta ou uma consequência que faça o "
         "cliente pensar.",
         "É a mesma ordem do seu processo: primeiro entender a realidade e "
         "despertar a necessidade; depois estruturar a solução.",
     ]},

    {"tipo": "alternativas", "titulo": "Em vez de, prefira",
     "pares": [("Conheça este seguro.",
                "Se você não pudesse trabalhar amanhã, por quanto tempo sua "
                "estrutura financeira continuaria funcionando?")],
     "rot_evitar": "Em vez de", "rot_preferir": "Prefira"},

    {"tipo": "camadas", "titulo": "**Direção** final",
     "camadas": [
         ("Despertar", "Para aquilo que ainda não foi pensado."),
         ("Explicar", "O que parece complexo."),
         ("Provar", "A autoridade construída."),
         ("Permanecer presente",
          "Para que, quando surgir a necessidade, Lucas seja lembrado."),
     ]},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
