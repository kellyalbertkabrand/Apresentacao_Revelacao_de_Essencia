# -*- coding: utf-8 -*-
"""
CONTEÚDO — Revelação de Essência · Flávia Pereira Muccelin

Este arquivo guarda SÓ o conteúdo. O layout vem de padrao-ka/ka_layout.py e o
roteiro de modelos/revelacao-de-essencia/gerar.py.

Para um cliente novo: copie esta pasta, troque os textos e as fotos.
A estrutura de cada campo está documentada em
modelos/revelacao-de-essencia/MODELO.md.

    python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin
"""

# ---------------------------------------------------------------- identificação
MARCA = "Flávia Pereira Muccelin"
ARQUIVO = "Flavia-Pereira-Muccelin"
TITULO_1 = "REVELAÇÃO DE"
TITULO_2 = "ESSÊNCIA"
SUBTITULO = "Flávia Pereira Muccelin  |  Origem Identitária da Fundadora"
ASSINATURA = ["Método Marca", "com Essência ©"]
DATA = "Setembro/2026"

# ---------------------------------------------------------------- sumário
SECOES = [
    ("01", "A origem",
     "As experiências que formaram a visão de mundo da Flávia."),
    ("02", "As tensões", "Os momentos que a colocaram em movimento."),
    ("03", "Os padrões", "A lógica que se repete ao longo da trajetória."),
    ("04", "O Ikigai", "O que gera sentido e realização para a Flávia."),
    ("05", "A essência", "O princípio que conecta a sua história."),
    ("06", "As marcas",
     "Como essa essência se manifesta na origem da Forma e da My Home."),
]

# ---------------------------------------------------------------- abertura
PORQUE = {
    "titulo": "Por que começamos pela essência?",
    "lead": "A Forma e a My Home são negócios distintos, mas nasceram e se "
            "desenvolveram a partir da visão de uma mesma fundadora.",
    "corpo": "Em marcas fortemente ligadas à fundadora, compreender a história "
             "de quem as criou ajuda a identificar crenças, princípios e "
             "formas de pensar e agir que influenciaram a construção dos "
             "negócios.",
    "nao_e": "Uma análise psicológica da Flávia.",
    "e": "A investigação da origem identitária das marcas a partir da "
         "fundadora.",
}

PERGUNTA = ["O que já fazia parte de quem", "a Flávia é antes da Forma",
            "e da My Home?"]

METODO = {
    "titulo": "Como chegamos à revelação",
    "lead": "A essência não é definida por uma característica isolada. Ela se "
            "revela quando diferentes momentos da trajetória apresentam uma "
            "mesma lógica.",
    "dimensoes": [
        ("História", "Mostra as experiências e as referências que formaram a "
                     "visão de mundo da Flávia."),
        ("Tensões", "Mostram os momentos em que aquilo que existia entrou em "
                    "conflito com aquilo que ela desejava ou conseguia "
                    "enxergar."),
        ("Padrões", "Revelam como a Flávia responde, repetidamente, a essas "
                    "situações."),
        ("Ikigai", "Revela o que gera sentido, realização e vontade de "
                   "contribuir."),
    ],
    "equacao": ["História", "tensões", "padrões", "Ikigai"],
    "nota": "A essência é o princípio central que conecta essas dimensões e "
            "revela a lógica que orienta a forma como a Flávia enxerga, age e "
            "transforma.",
}

# ---------------------------------------------------------------- 01 A origem
ORIGEM = {
    "titulo": "Onde essa história começa",
    "lead": "A história familiar da Flávia é marcada por limitações, trabalho, "
            "fé e recomeços.",
    "corpo": "A família deixou Guiratinga e foi para Primavera do Leste em "
             "busca de uma vida melhor. O pai da Flávia passou a trabalhar "
             "como caseiro justamente na propriedade onde, décadas depois, "
             "ela viveria como proprietária.",
    "marcante": "A Flávia chegou àquele lugar como “a filha do peão”.",
    "valores": ["Trabalho", "Família", "Fé", "Honestidade", "Gratidão"],
}

SINAIS = {
    "titulo": "Os primeiros sinais",
    "lead": "A vontade de construir uma realidade diferente aparece muito "
            "antes da criação das empresas.",
    "corpo": "Ainda criança, a Flávia acompanhava o pai no garimpo e chegou a "
             "cozinhar para os trabalhadores. Mais tarde, ia de bicicleta da "
             "chácara até o centro para trabalhar. Também estudava e jogava "
             "futsal para conquistar uma bolsa que ajudasse a manter a "
             "faculdade.",
    "falas": [
        ("Ela mesma diz:", "Eu não quero isso para mim."),
        ("E, mais tarde, ao perceber que o cargo limitaria o seu crescimento:",
         "Eu queria mais."),
    ],
}

EXPERIENCIAS_TITULO = "As experiências que a formaram"
EXPERIENCIAS = [
    ("01", "A escassez",
     "A Flávia cresceu em uma realidade de poucos recursos.",
     "A vontade de ampliar possibilidades e não aceitar a condição presente "
     "como limite."),
    ("02", "O portão",
     "Ainda adolescente, a Flávia entrava escondida na casa dos donos da "
     "fazenda onde o pai trabalhava e se imaginava vivendo aquela realidade. "
     "Anos depois, tornou-se proprietária daquele mesmo lugar.",
     "A capacidade de se enxergar dentro de uma realidade antes de ela existir "
     "concretamente."),
    ("03", "O trabalho e o estudo",
     "Trabalho, faculdade, bicicleta e futsal como caminho para conquistar uma "
     "bolsa de estudos.",
     "Para a Flávia, enxergar uma possibilidade exige movimento para torná-la "
     "real."),
    ("04", "A trajetória dos pais",
     "A Flávia cresceu vendo os pais recomeçarem sem abandonar a honestidade, "
     "a fé, o trabalho e a família.",
     "A forma de construir importa tanto quanto aquilo que é conquistado."),
]

# ---------------------------------------------------------------- 02 As tensões
TENSOES = {
    "titulo": "As tensões que a colocaram em movimento",
    "lead": "Existe uma lógica recorrente na trajetória da Flávia.",
    # (rótulo, fala, resposta, é relato e não fala entre aspas)
    "linhas": [
        ("A realidade dizia", "“Essa é a sua condição.”",
         "A Flávia enxergava outra.", False),
        ("O cargo dizia", "“Até aqui você pode chegar.”",
         "A Flávia queria mais.", False),
        ("As marcas prontas diziam", "“É assim que deve ser feito.”",
         "A Flávia queria fazer do seu jeito.", False),
        ("A maternidade exigiu uma escolha",
         "Conciliar a maternidade e o empreendedorismo não era possível como "
         "ela desejava naquele momento.",
         "Ela parou e, anos depois, construiu um caminho de volta.", True),
        ("As sobras tinham um destino", "“O descarte.”",
         "A Flávia enxergou matéria para uma nova criação.", False),
    ],
    "fecho": "Quando aquilo que está dado não corresponde ao que a Flávia "
             "enxerga como possível, ela entra em movimento.",
}

# ---------------------------------------------------------------- 03 Os padrões
PADRAO = {
    "titulo": "O padrão invisível",
    "lead": "As situações são diferentes. A resposta da Flávia segue a mesma "
            "lógica.",
    "etapas": [
        "Ela encontra uma realidade ou um limite.",
        "Enxerga que aquilo pode ser diferente.",
        "Constrói um caminho para transformar essa possibilidade em realidade.",
    ],
    "fecho": "O padrão está na forma como a Flávia responde quando percebe que "
             "existe uma possibilidade além daquilo que está dado.",
}

MOVIMENTO = {
    "titulo": "O movimento que se repete",
    "passos": [
        "Enxerga a realidade como ela é",
        "Percebe que aquilo não precisa ser definitivo",
        "Enxerga outra possibilidade",
        "Procura um caminho",
        "Busca conhecimento, mobiliza pessoas e recursos",
        "Transforma a possibilidade em realidade",
    ],
    "sintese": ["Enxergar além", "colocar em movimento", "fazer existir"],
}

LINHA_MESTRA = {
    "apoio": "Ao longo da sua trajetória, a Flávia repete um mesmo movimento:",
    "frase": ["A Flávia não aceita que aquilo que",
              "existe determine aquilo que pode existir."],
}

# ---------------------------------------------------------------- 04 O Ikigai
IKIGAI = {
    "titulo": "O que move a Flávia?",
    "lead": "Até aqui, a história revelou como a Flávia responde à realidade e "
            "entra em movimento. O Ikigai acrescenta outra dimensão: o que faz "
            "esse movimento ter sentido para ela.",
    "perguntas": [
        "O que a Flávia ama?",
        "No que reconhece as suas forças?",
        "Onde encontra realização?",
        "Como deseja contribuir para outras pessoas?",
    ],
    "fecho": "Não buscamos apenas aquilo que ela gosta de fazer, e sim o que "
             "faz uma realização ter significado para a Flávia.",
}

MAPA = {
    "titulo": "O mapa do Ikigai",
    "quadrantes": [
        ("O que a Flávia ama",
         "A família. As pessoas. Os momentos de qualidade. As conversas e as "
         "trocas verdadeiras. As conexões."),
        ("No que a Flávia é boa",
         "No conhecimento que construiu. Na persuasão. Na seriedade. Na "
         "persistência. No domínio daquilo que vende. Na capacidade de "
         "envolver pessoas."),
        ("Como a Flávia gosta de contribuir",
         "Sendo útil. Compartilhando conhecimentos e experiências. Ajudando "
         "pessoas e empresários. Criando oportunidades. Fazendo diferença na "
         "vida das pessoas."),
        ("Onde a Flávia encontra realização",
         "Ao ver algo ganhar forma. Ao transformar matéria em algo de valor. "
         "Ao perceber a alegria do cliente. Ao ver o sonho de outra pessoa se "
         "tornar concreto. Ao saber que aquilo que construiu também ampliou as "
         "possibilidades de alguém."),
    ],
}

CENTRO = {
    "titulo": "O centro do Ikigai",
    "lead": "A Flávia não se realiza apenas conquistando para si. Ela encontra "
            "realização quando vê uma possibilidade se tornar concreta e "
            "produzir algo na vida de outras pessoas.",
    "exemplos": [
        "Um cliente realiza um sonho.",
        "Uma equipe cresce.",
        "Uma ideia sai do papel.",
        "Uma pessoa recebe uma oportunidade.",
    ],
    "contexto": "Sobre o legado que deseja deixar, a própria Flávia resume:",
    "fala": "Fazer diferença na vida das pessoas.",
}

RAZAO_DE_SER = {
    "frase": ["Transformar possibilidades em realizações",
              "concretas que também ampliem a vida",
              "de outras pessoas."],
    "apoio": "A realização ganha sentido quando aquilo que a Flávia constrói "
             "também amplia possibilidades para outras pessoas.",
}

# ---------------------------------------------------------------- 05 A essência
ENCONTRO = {
    "titulo": "Onde a história e o Ikigai se encontram",
    "lead": "A história revela como a Flávia se movimenta. O Ikigai revela o "
            "que dá sentido a esse movimento. Lado a lado, a mesma lógica "
            "aparece.",
    "eixos": [
        ("Visão", "A Flávia enxerga além da condição presente."),
        ("Movimento", "A distância entre aquilo que existe e aquilo que ela "
                      "enxerga como possível a leva a buscar caminhos, "
                      "conhecimento, pessoas e recursos."),
        ("Pessoas", "A família, a equipe, os clientes e as relações fazem "
                    "parte daquilo que dá significado às suas realizações."),
        ("Impacto", "A conquista ganha mais sentido quando aquilo que ela "
                    "constrói também amplia possibilidades para outras "
                    "pessoas."),
    ],
    "movimentos": ["Enxergar além.", "Colocar em movimento.", "Fazer existir."],
}

ESSENCIA = {
    "eyebrow": "A essência da Flávia como fundadora",
    "frase": ["Enxergar além do que está posto e fazer",
              "existir o que ainda é possibilidade."],
    "camadas": [
        ("Enxergar além", "A Flávia não considera a realidade presente como a "
                          "única possibilidade. Ela consegue enxergar aquilo "
                          "que ainda pode existir."),
        ("Fazer existir", "Ela não permanece apenas no campo da imaginação. "
                          "Procura caminhos e transforma a possibilidade em "
                          "realidade."),
        ("Ampliar possibilidades", "A realização ganha sentido quando aquilo "
                                   "que ela constrói também cria valor, "
                                   "oportunidade ou transformação para outras "
                                   "pessoas."),
    ],
    "fecho": "Forte, determinada, criativa, sonhadora e visionária são "
             "características da Flávia. Mas são manifestações de uma lógica "
             "mais profunda: enxergar além e fazer existir.",
}

# ---------------------------------------------------------------- 06 As marcas
MARCAS = {
    "titulo": "Como essa essência se manifesta nas marcas",
    "lead": "Uma mesma essência. Duas manifestações diferentes.",
    "marcas": [
        ("A Forma", "Dar forma ao que ainda é ideia.",
         "A empresa representa o espaço que a Flávia buscava para criar, "
         "personalizar e construir segundo a sua própria visão. Esse mesmo "
         "movimento está na natureza do negócio: uma necessidade, uma ideia "
         "ou um sonho se transformam em projeto e ganham forma concreta."),
        ("A My Home", "Reabrir possibilidades.",
         "A marca nasce quando a Flávia questiona o destino dado às sobras da "
         "marcenaria. Onde havia descarte, ela enxergou matéria. Onde havia "
         "fim, ela enxergou um novo começo. Aquilo que havia encerrado a sua "
         "função ganhou uma nova possibilidade de existir."),
    ],
    "fecho": "A Forma e a My Home são marcas diferentes e terão estratégias "
             "próprias. Mas as duas carregam, na origem, uma mesma forma de "
             "enxergar e transformar a realidade.",
}

PROXIMA = {
    "titulo": "Da essência à estratégia",
    "lead": "Esta etapa revelou a essência da Flávia como fundadora: uma forma "
            "própria de enxergar e transformar a realidade que já existia "
            "antes da Forma e da My Home.",
    "corpo": "Essa essência ajuda a compreender de onde as duas marcas vêm, "
             "mas não define, sozinha, quem cada marca precisa ser.",
    "destaque": "A Base Estratégica vai definir como essa origem se traduz em "
                "uma direção própria, relevante e diferenciada para a Forma e "
                "para a My Home.",
}

FECHO = ["A essência revela a origem.", "A estratégia define a direção."]
