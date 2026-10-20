# -*- coding: utf-8 -*-
"""
DUAS TRAJETÓRIAS. UMA NOVA FORÇA. — Flávia & Elande | FORMA e My Home

Só conteúdo. A identidade visual é a mesma de sempre: painel claro sobre a
textura de ondas, Outfit, acento terracota (padrao-ka/ka_layout.py e
padrao-ka/ka_paginas.py) — a mesma da Base Estratégica do Lucas e das outras
apresentações da Flávia.

A diagramação segue a regra que a Kelly fixou em outubro: **um título e um
bloco de texto por página**. Sem eyebrow, sem linha de abertura em outro
corpo, sem frase de destaque com filete embaixo. Onde o conteúdo é de campos
(entregas, papéis, atributos), ele vira colunas ou palavras — rótulo e texto
lado a lado, nunca empilhados.

Por isso o roteiro dela de 10 slides sai aqui em 21 páginas: cada slide do
documento carregava até quatro blocos (rótulo, atributos, lista, citação e
fecho), e empilhar os quatro é exatamente o que a regra proíbe. O texto é o
dela, palavra por palavra, na ordem dela.

Uma correção de ordem, assinalada e não silenciosa: no documento, o sumário
lista "Papéis e responsabilidades" em 04, mas o slide correspondente vem
depois de "Onde nasce a potência" e de "Os pontos de atenção". O sumário
aqui foi renumerado para seguir a ordem da narrativa que ela escreveu.

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela: a área exata que a foto vai ocupar, com o briefing do que
entra ali. No dia em que o arquivo com o nome declarado em `foto` entrar em
`assets/`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py sociedade
"""

MARCA = "Flávia & Elande"
DOCUMENTO = "Duas Trajetórias. Uma Nova Força."
RODAPE = False          # sem pílula e sem logo no pé, como ela pediu
ARQUIVO = "Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elande"

# As imagens que a apresentação pede. Os arquivos ainda não existem — cada
# página mostra a marcação até que eles cheguem em assets/ com estes nomes.
IMG = {
    "flavia": "sociedade-flavia-retrato.png",
    "elande": "sociedade-elande-retrato.png",
    "dupla": "sociedade-flavia-elande.png",
    "rotina": "sociedade-rotina-noite.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    {"tipo": "capa",
     "titulo": ["DUAS TRAJETÓRIAS.", "UMA NOVA FORÇA."],
     "subtitulo": ["Flávia & Elande", "FORMA e My Home"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["O encontro de duas competências",
                "para construir o próximo capítulo",
                "da FORMA e da My Home."]},

    {"tipo": "sumario", "itens": [
        ("01", "A força que construiu"),
        ("02", "A força que chega para estruturar"),
        ("03", "O valor singular de cada um"),
        ("04", "Onde nasce a potência"),
        ("05", "Os pontos de atenção"),
        ("06", "Papéis e responsabilidades"),
        ("07", "A nova fase dos negócios"),
    ]},

    # ————————————————————————————— 01 A FORÇA QUE CONSTRUIU
    {"tipo": "palavras", "titulo": "Flávia · essência empreendedora",
     "foto": IMG["flavia"], "lado": "direita",
     "imagem": "Retrato da Flávia, meio corpo, em obra ou em ambiente de "
               "trabalho. Olhar direto, postura de quem conduz. Luz natural, "
               "sem pose de estúdio.",
     "palavras": ["Autonomia", "Inconformismo", "Visão", "Realização"]},

    {"tipo": "lista",
     "titulo": "A força que não aceita limites como destino.",
     "itens": [
         "Superou as limitações de sua origem sem aceitá-las como destino.",
         "Rompeu estruturas profissionais que restringiam sua capacidade de "
         "criar.",
         "Transformou conhecimento técnico em negócio, liderança e "
         "reputação.",
         "Enxerga oportunidades onde outros enxergam obstáculos ou descarte.",
     ],
     "marcar_ultimo": True,
     "fecho": "Sua força singular: transformar aquilo que ainda não existe "
              "em algo que as pessoas podem viver, utilizar e valorizar."},

    # ——————————————————— 02 A FORÇA QUE CHEGA PARA ESTRUTURAR
    {"tipo": "palavras", "titulo": "Elande · essência profissional",
     "foto": IMG["elande"], "lado": "esquerda",
     "imagem": "Retrato do Elande, meio corpo, em ambiente de escritório ou "
               "de gestão. Expressão serena e atenta. Mesma luz e mesmo "
               "enquadramento do retrato da Flávia — os dois precisam "
               "conversar lado a lado.",
     "palavras": ["Responsabilidade", "Critério", "Consistência",
                  "Previsibilidade"]},

    {"tipo": "lista",
     "titulo": "A força que enxerga o que sustenta uma conquista.",
     "itens": [
         "Construiu sua carreira assumindo responsabilidades de gestão e "
         "controladoria.",
         "Aprendeu a olhar além do faturamento, considerando custos, margens "
         "e consequências.",
         "Valoriza processos que tornam a empresa menos dependente de uma "
         "única pessoa.",
         "Reconhece a liderança da Flávia e quer contribuir sem substituir "
         "sua maneira de empreender.",
     ],
     "marcar_ultimo": True,
     "fecho": "Sua força singular: transformar conhecimento e informação em "
              "decisões que protegem o futuro."},

    {"tipo": "declaracao",
     "linhas": ["“Eu tô bem preparado em não ser",
                "um obstáculo, e sim ser",
                "um agregador.”"],
     "apoio": "Elande, em entrevista."},

    # ——————————————————————— 03 O VALOR SINGULAR DE CADA UM
    {"tipo": "colunas",
     "titulo": "Duas competências. Duas responsabilidades essenciais.",
     "colunas": [
         ("Flávia — fazer o negócio avançar",
          "Visão de mercado, relacionamento, produto, inovação, liderança e "
          "direção comercial."),
         ("Elande — dar condições para o avanço",
          "Controladoria, custos, fluxo de caixa, planejamento, gestão "
          "financeira e administrativa."),
     ],
     "fecho": "Flávia deve preservar a liberdade de empreender. Elande deve "
              "ter autonomia real para estruturar e conduzir sua área. "
              "Nenhum dos dois deve precisar administrar o trabalho do "
              "outro."},

    # ————————————————————————————— 04 ONDE NASCE A POTÊNCIA
    {"tipo": "colunas",
     "titulo": "Ele não chega para frear. Ela não precisa continuar "
               "carregando tudo.",
     "foto": IMG["dupla"], "lado": "esquerda",
     "imagem": "Flávia e Elande juntos, em conversa de trabalho — mesa, "
               "planta, obra ou escritório. Interação real, não retrato "
               "posado lado a lado.",
     "colunas": [
         ("Flávia entrega",
          "Visão, oportunidades, velocidade e capacidade de realização."),
         ("Elande entrega",
          "Clareza financeira, planejamento, estrutura e segurança para "
          "decidir."),
     ]},

    {"tipo": "foto_cheia", "foto": IMG["rotina"],
     "imagem": "A rotina que a frase descreve: mesa de trabalho em casa à "
               "noite, luminária acesa, computador e papéis. Pode ser sem "
               "pessoa — o que importa é a hora.",
     "linhas": ["“Hoje pra pagar boleto, ela paga",
                "boleto em casa, oito hora da noite.”"],
     "apoio": "Elande, em entrevista."},

    {"tipo": "declaracao",
     "linhas": ["Mais capacidade de crescer.",
                "Menos dependência individual."],
     "apoio": "O maior ganho dessa união não é dividir o trabalho. É "
              "devolver à Flávia tempo para criar oportunidades e dar ao "
              "Elande espaço para construir uma gestão mais sólida."},

    # ————————————————————————————— 05 OS PONTOS DE ATENÇÃO
    {"tipo": "declaracao",
     "linhas": ["Autonomia não é ausência de limites.",
                "Controle não é poder de veto."]},

    {"tipo": "lista", "titulo": "Flávia precisa",
     "itens": [
         "Delegar sem retomar tudo para si.",
         "Respeitar critérios financeiros acordados.",
         "Confiar na autonomia de gestão dele.",
         "Compartilhar informações e planos com antecedência.",
     ]},

    {"tipo": "lista", "titulo": "Elande precisa",
     "itens": [
         "Orientar sem interferir em todas as decisões.",
         "Compreender a velocidade do negócio.",
         "Confiar no conhecimento comercial e técnico dela.",
         "Oferecer alternativas, não apenas apontar riscos.",
     ],
     "fecho": "O equilíbrio não está em um ceder sempre ao outro. Está em "
              "cada um assumir plenamente sua responsabilidade."},

    # ——————————————————————— 06 PAPÉIS E RESPONSABILIDADES
    {"tipo": "colunas", "titulo": "Papéis claros. Decisões compartilhadas.",
     "colunas": [
         ("Flávia lidera",
          "Mercado, clientes, posicionamento, produto, desenvolvimento de "
          "oportunidades e direção comercial e produtiva."),
         ("Elande lidera",
          "Finanças, controladoria, custos, fluxo de caixa, orçamento, "
          "controles administrativos e gestão dos recursos sob sua "
          "responsabilidade."),
         ("Os dois decidem",
          "Grandes investimentos, expansão, endividamento, prioridades "
          "estratégicas e decisões que comprometam significativamente a "
          "capacidade financeira ou operacional das empresas."),
     ],
     "fecho": "A regra: decisões do dia a dia devem ter responsáveis "
              "definidos; decisões que alteram o futuro dos negócios "
              "precisam reunir os dois olhares. Esta é uma proposta de "
              "divisão de responsabilidades para validação entre os sócios, "
              "não um organograma já acordado."},

    # ——————————————————————— 07 A NOVA FASE DOS NEGÓCIOS
    {"tipo": "texto",
     "titulo": "A liberdade que ela conquistou. A segurança que ele aprendeu "
               "a construir.",
     # três parágrafos não são a página de um bloco só: o corpo volta aos
     # 21pt da escala, que é o tamanho padrão — não é reduzir, é recusar o
     # aumento que a página de uma ideia só recebe
     "tam_corpo": 21,
     "paragrafos": [
         "Flávia passou a vida conquistando liberdade para fazer acontecer. "
         "Elande construiu uma carreira aprendendo a sustentar decisões e "
         "resultados.",
         "Agora, o desafio é fazer com que essas duas forças deixem de "
         "existir apenas como apoio pessoal e se transformem em uma parceria "
         "profissional estruturada.",
         "O futuro da FORMA e da My Home não deve depender de quem consegue "
         "carregar mais responsabilidades, mas da capacidade dos dois de "
         "construir uma empresa que funcione melhor, cresça com consistência "
         "e preserve aquilo que a tornou especial.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Ela não precisa perder sua liberdade",
                "para a empresa crescer.",
                "Ele não precisa limitar essa liberdade",
                "para proteger a empresa."],
     "apoio": "A potência está em fazer as duas coisas acontecerem juntas."},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
