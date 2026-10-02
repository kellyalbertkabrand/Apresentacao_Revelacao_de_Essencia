# -*- coding: utf-8 -*-
"""
REVELAÇÃO DE ESSÊNCIA — Lucas José Martini

Só conteúdo. Layout em padrao-ka/ka_layout.py, arquétipos de página em
padrao-ka/ka_paginas.py.

30 páginas. A versão anterior tinha 63 e dizia a mesma coisa: cada
descoberta vinha anunciada numa página, desenvolvida na seguinte e
repetida numa terceira em caixa alta. Aqui cada descoberta ocupa uma
página só — a afirmação, a evidência e a leitura juntas. Nenhuma ideia
do material original foi perdida; o que saiu foi a repetição.

As fotografias entram em tira vertical (o padrão, porque o material é
16:9) ou em tela cheia. O recorte é calculado a partir de `assets/rostos.json`
para que o rosto nunca seja cortado.
"""

MARCA = "Lucas José Martini"
DOCUMENTO = "Revelação de Essência"
ARQUIVO = "Revelacao-de-Essencia-Lucas-Jose-Martini"

IMG = {
    1: "01_retrato_corporativo_prudential.png",
    2: "02_reuniao_consultiva_casal.png",
    3: "03_lucas_janela_entardecer.png",
    4: "04_jovem_colete_vermelho_caixa_eletronico.png",
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
     "titulo": ["REVELAÇÃO", "DE ESSÊNCIA"],
     "subtitulo": ["Lucas José Martini",
                   "Origem Identitária do Fundador"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026",
     "foto": IMG[1], "foco": 0.42},

    # 03 — sumário
    {"tipo": "sumario", "itens": [
        ("01", "A origem",
         "As experiências que formaram sua relação com construção, segurança "
         "e futuro."),
        ("02", "As tensões",
         "Os contrastes que revelam o que realmente o coloca em movimento."),
        ("03", "Os padrões",
         "A lógica que se repete por trás de escolhas diferentes."),
        ("04", "O Ikigai",
         "Onde capacidade, realização, contribuição e profissão se encontram."),
        ("05", "A essência",
         "O princípio mais profundo que conecta sua trajetória."),
        ("06", "A marca",
         "O que essa essência revela sobre o papel que Lucas pode ocupar."),
    ]},

    # 04 — por que começamos pela essência
    {"tipo": "texto", "eyebrow": "Conceito", "foto": IMG[3], "lado": "direita",
     "titulo": "Por que começamos pela essência?",
     "lead": "Uma marca pessoal não começa naquilo que o profissional vende. "
             "Começa na maneira como ele enxerga o mundo, toma decisões e "
             "atribui significado ao próprio trabalho.",
     "paragrafos": [
         "No caso do Lucas, proteção e sucessão são a parte visível. Esta "
         "etapa não é uma análise psicológica: é a investigação dos padrões, "
         "crenças e tensões que explicam a origem da sua atuação.",
     ],
     "destaque": "O que existe por trás da forma como ele protege?"},

    # 05
    {"tipo": "declaracao",
     "linhas": ["A história não é a revelação.",
                "A história é a evidência."]},

    # 06 — método
    {"tipo": "colunas", "eyebrow": "Método",
     "titulo": "Como chegamos à revelação",
     "lead": "A essência não é um adjetivo, nem uma frase bonita criada para "
             "comunicação. Ela aparece quando momentos aparentemente "
             "diferentes revelam uma mesma lógica.",
     "colunas": [
         ("História", "O que ajudou a formar sua visão de mundo."),
         ("Tensões",
          "Os contrastes que mostram aquilo que realmente importa."),
         ("Padrões", "A forma recorrente como Lucas responde."),
         ("Ikigai",
          "Onde competência, realização, contribuição e profissão se "
          "encontram."),
     ],
     "equacao": ["história", "tensões", "padrões", "Ikigai", "essência"]},

    # ——— 01 A ORIGEM
    {"tipo": "divisor", "numero": "01", "nome": "A origem",
     "apoio": "As experiências que formaram sua relação com construção, "
              "segurança e futuro."},

    # 08 — construção + a primeira crença
    {"tipo": "palavras", "eyebrow": "A origem",
     "titulo": "Uma história sobre construção",
     "lead": "Lucas não viveu a dificuldade dos pais, mas cresceu conhecendo "
             "a história de uma família que saiu do campo, enfrentou "
             "escassez, trabalhou, adquiriu um terreno e construiu uma casa. "
             "Nada do que aparece abaixo chega até ele como algo dado:",
     "palavras": ["Casa", "Renda", "Patrimônio",
                  "Carreira", "Empresa", "Estabilidade"],
     "destaque": "Segurança pode levar anos para ser construída. O valor "
                 "está em tudo o que foi preciso para chegar até ali."},

    # 09 — o segundo aprendizado
    {"tipo": "texto", "eyebrow": "A origem", "foto": IMG[4],
     "lado": "esquerda",
     "titulo": "O segundo aprendizado",
     "lead": "Anos depois, na recuperação de ativos do Bradesco, Lucas passa "
             "a ver o outro lado dessa lógica: famílias e empresas que "
             "levaram anos construindo patrimônio entravam rapidamente em "
             "dificuldade diante de morte, doença ou sucessão mal planejada.",
     "paragrafos": [
         "Talvez o primeiro grande aprendizado do Lucas não tenha sido sobre "
         "seguro. Tenha sido sobre fragilidade.",
     ],
     "destaque": "O que leva anos para ser construído pode ser comprometido "
                 "muito rapidamente."},

    # 10 — o que a fragilidade significa
    {"tipo": "lista", "eyebrow": "A origem", "foto": IMG[6],
     "lado": "direita",
     "titulo": "O que essa fragilidade significa",
     "lead": "Não é acreditar que tudo pode dar errado. É compreender que:",
     "itens": [
         "uma renda pode parar;",
         "uma empresa pode perder uma pessoa essencial;",
         "um patrimônio pode precisar ser desmontado;",
         "uma família pode perder, junto com alguém, a estrutura que "
         "sustentava sua vida.",
     ],
     "destaque": "O imprevisto não destrói apenas dinheiro. Ele retira "
                 "possibilidades."},

    # ——— 02 AS TENSÕES
    {"tipo": "divisor", "numero": "02", "nome": "As tensões",
     "apoio": "Os contrastes que revelam o que realmente o coloca em "
              "movimento."},

    # 12 — segurança × risco
    {"tipo": "texto", "eyebrow": "Primeira tensão", "foto": IMG[12],
     "lado": "esquerda",
     "titulo": "Segurança × risco",
     "lead": "Lucas constrói segurança para outras pessoas. Mas, num momento "
             "decisivo da própria carreira, abriu mão de uma trajetória "
             "sólida no banco para empreender.",
     "paragrafos": [
         "Ele aceita risco quando existe decisão, consciência, preparo e "
         "responsabilidade. O que o incomoda não é a incerteza.",
     ],
     "destaque": "Segurança, para o Lucas, não é viver sem risco. É não ficar "
                 "sem escolha quando algo acontece."},

    # 13 — dinheiro × propósito
    {"tipo": "texto", "eyebrow": "Segunda tensão", "foto": IMG[9],
     "lado": "direita",
     "titulo": "Dinheiro × propósito",
     "lead": "Lucas não romantiza a própria decisão: a possibilidade "
             "financeira pesou. Mas resume a trajetória com uma frase "
             "reveladora — “fui pelo dinheiro e acabei ficando pelo "
             "propósito”.",
     "paragrafos": [
         "O significado aparece quando ele começa a acompanhar pagamentos de "
         "benefícios e percebe o que uma decisão tomada antes representava na "
         "vida de alguém. Crescimento, resultado e reconhecimento movem o "
         "Lucas — e seguem movendo.",
     ],
     "destaque": "O dinheiro explica a entrada. O impacto explica a "
                 "permanência."},

    # 14 — reconhecimento × exposição
    {"tipo": "texto", "eyebrow": "Terceira tensão", "foto": IMG[14],
     "lado": "esquerda",
     "titulo": "Reconhecimento × exposição",
     "lead": "Lucas acumula reconhecimentos e valoriza estar entre os "
             "melhores. Mas tem dificuldade declarada em comunicar essas "
             "conquistas.",
     "paragrafos": [
         "O paradoxo é aparente. Ele não tem dificuldade com reconhecimento: "
         "tem dificuldade com autoproclamação. Existe conforto quando um "
         "cliente, uma companhia ou um ranking reconhecem; existe desconforto "
         "quando ele próprio precisa dizer “olhem o que eu conquistei”.",
     ],
     "destaque": "Para o Lucas, legitimidade precisa ser conquistada. Não "
                 "declarada."},

    # 15 — autoridade discreta
    {"tipo": "foto_cheia", "foto": IMG[8], "veu": 0.64,
     "eyebrow": "O que isso revela",
     "linhas": ["Alta performance.", "Baixa performatividade."],
     "apoio": "Lucas performa muito, mas performatiza pouco. Construiu "
              "autoridade e poucos signos públicos dela. Isso não precisa ser "
              "corrigido: pode virar assinatura — autoridade discreta."},

    # ——— 03 OS PADRÕES
    {"tipo": "divisor", "numero": "03", "nome": "Os padrões",
     "apoio": "A lógica que se repete por trás de escolhas diferentes."},

    # 17 — os três padrões
    {"tipo": "camadas", "eyebrow": "Os padrões",
     "titulo": "O que se repete em toda escolha",
     "camadas": [
         ("Preparar antes",
          "Diante de algo importante, Lucas entende, estuda, organiza e "
          "estrutura. Cria estrutura antes que ela seja necessária."),
         ("Repetir bem",
          "Começa cedo, avança no banco, recomeça, constrói carteira e mantém "
          "ritmo. Chega a 100 semanas consecutivas protegendo três famílias "
          "por semana."),
         ("Permanecer depois",
          "Não encerra o trabalho na venda. Relacionamento, confiança e "
          "pós-venda são centrais na sua forma de atuar."),
     ]},

    # 18 — o movimento
    {"tipo": "fluxo", "eyebrow": "Os padrões",
     "titulo": "O movimento que se repete",
     "passos": ["Entender", "Antecipar", "Estruturar", "Acompanhar",
                "Preservar possibilidades"],
     "sintese": ["Entender antes", "Preparar antes", "Permanecer depois"]},

    # ——— 04 O IKIGAI
    {"tipo": "divisor", "numero": "04", "nome": "O Ikigai",
     "apoio": "Onde capacidade, realização, contribuição e profissão se "
              "encontram."},

    # 20 — o Ikigai nos quatro cruzamentos
    {"tipo": "ikigai", "eyebrow": "O Ikigai",
     "titulo": "Os quatro encontros",
     "campos": [
         ("Paixão · o que ama + no que é bom",
          "Conversar, compreender e construir soluções que façam sentido "
          "para cada realidade."),
         ("Profissão · no que é bom + pelo que pode ser pago",
          "Estruturar proteção e sucessão com visão consultiva, "
          "personalização e relacionamento."),
         ("Missão · o que o mundo precisa + o que gosta de fazer",
          "Ampliar a consciência de que preparação financeira também é uma "
          "forma de cuidado e responsabilidade."),
         ("Vocação · o que o mundo precisa + pelo que pode ser pago",
          "Ajudar pessoas, famílias e empresas a chegarem mais preparadas "
          "aos momentos que não podem controlar."),
     ],
     "centro": "Sua competência não é conhecer produtos — é transformar "
               "complexidade em decisão estruturada."},

    # 21 — realização e dignidade financeira
    {"tipo": "lista", "eyebrow": "O Ikigai", "foto": IMG[5], "lado": "direita",
     "titulo": "Onde Lucas encontra realização",
     "lead": "Quando o planejamento cumpre aquilo para o qual foi criado: "
             "um benefício é pago, uma empresa pode continuar.",
     "itens": [
         "Manter possibilidades quando a vida muda.",
         "Não precisar desmontar tudo nem aceitar qualquer saída.",
         "Não transformar uma perda humana em colapso financeiro.",
     ],
     "destaque": "Dignidade financeira não é dinheiro disponível. É o que "
                 "preserva possibilidades."},

    # 22 — razão de ser
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.40, "veu": 0.66,
     "eyebrow": "Razão de ser",
     "linhas": ["Preservar a capacidade",
                "de escolha quando a vida",
                "tira a previsibilidade."]},

    # ——— 05 A ESSÊNCIA
    {"tipo": "divisor", "numero": "05", "nome": "A essência",
     "apoio": "O princípio mais profundo que conecta sua trajetória."},

    # 24 — onde tudo se encontra
    {"tipo": "camadas", "eyebrow": "A essência",
     "titulo": "Onde tudo se encontra",
     "camadas": [
         ("A origem", "Ensinou que segurança é construída."),
         ("O banco",
          "Mostrou como aquilo que levou anos para existir se fragiliza "
          "depressa."),
         ("O empreendedorismo",
          "Mostrou que ele aceita risco quando pode escolher "
          "conscientemente."),
         ("A profissão", "Mostrou que preparação preserva possibilidades."),
         ("A crença fundadora",
          "O que levou anos para ser construído não deveria ficar entregue "
          "ao acaso."),
     ]},

    # 25 — a essência
    {"tipo": "foto_cheia", "foto": IMG[12], "foco": 0.45, "veu": 0.68,
     "eyebrow": "A essência de Lucas",
     "linhas": ["Construir segurança para",
                "preservar liberdade",
                "de escolha."],
     "apoio": "Lucas não trabalha para controlar o imprevisto. Trabalha para "
              "que o imprevisto não decida sozinho o que vem depois."},

    # 26 — as três camadas
    {"tipo": "colunas", "eyebrow": "A essência de Lucas",
     "titulo": "O que a frase carrega",
     "colunas": [
         ("Construir segurança",
          "Transformar vulnerabilidades em planejamento, recursos e "
          "alternativas."),
         ("Preservar liberdade",
          "Manter possibilidades diante de acontecimentos que fogem ao "
          "controle."),
         ("Escolha",
          "Evitar que a urgência seja a única responsável pelas decisões."),
     ],
     "fecho": "Responsável, disciplinado, ambicioso e constante são "
              "características do Lucas. Mas são manifestações de uma lógica "
              "mais profunda: preparar o que pode ser preparado para proteger "
              "o que não pode ser previsto."},

    # ——— 06 A MARCA
    {"tipo": "divisor", "numero": "06", "nome": "A marca",
     "apoio": "O que essa essência revela sobre o papel que Lucas pode "
              "ocupar."},

    # 28 — o produto não é o centro
    {"tipo": "camadas", "eyebrow": "A marca", "foto": IMG[2],
     "lado": "esquerda",
     "titulo": "O produto não é o centro",
     "camadas": [
         ("Seguro", "É instrumento."),
         ("Planejamento", "É método."),
         ("Proteção e sucessão", "São campos de atuação."),
         ("Continuidade", "É o território."),
         ("Liberdade de escolha", "É o significado humano."),
     ]},

    # 29 — prova, não proclamação
    {"tipo": "texto", "eyebrow": "A marca", "foto": IMG[13],
     "lado": "direita",
     "titulo": "Prova, não proclamação",
     "lead": "A dificuldade de comunicação do Lucas não exige que ele se "
             "transforme em alguém que não é. Sua marca pode ser construída "
             "pela lógica que já existe nele.",
     "paragrafos": [
         "Resultados, casos, conhecimento, reconhecimentos contextualizados e "
         "consistência. Ele não precisa se tornar mais exibido: precisa "
         "tornar mais visível aquilo que já construiu.",
     ],
     "destaque": "A essência revela a origem. A estratégia define a direção."},

    # 30
    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
