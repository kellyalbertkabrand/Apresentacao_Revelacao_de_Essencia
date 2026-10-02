# -*- coding: utf-8 -*-
"""
REVELAÇÃO DE ESSÊNCIA — Lucas José Martini

Só conteúdo. O layout vem de padrao-ka/ka_layout.py e os arquétipos de
página de padrao-ka/ka_paginas.py.

As fotografias do Lucas chegaram todas em 16:9 (só a 01 é retrato), por isso
aqui elas entram em FAIXA HORIZONTAL ou em tela cheia com véu — a faixa
vertical da apresentação da Flávia recortaria o enquadramento a um quarto da
largura. O gabarito de imagens da Kelly foi seguido slide a slide; a imagem
07 ficou de fora, como ela pediu.
"""

MARCA = "Lucas José Martini"
DOCUMENTO = "Revelação de Essência"
ARQUIVO = "Revelacao-de-Essencia-Lucas-Jose-Martini"

# ------------------------------------------------------------------- imagens
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
    {"tipo": "abertura"},

    # 01 — capa
    {"tipo": "capa",
     "titulo": ["REVELAÇÃO", "DE ESSÊNCIA"],
     "subtitulo": ["Lucas José Martini",
                   "Origem Identitária do Fundador"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026",
     "foto": IMG[1], "lado": "esquerda", "foco": 0.42},

    # 02 — sumário
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

    # 03 — abertura da etapa
    {"tipo": "declaracao", "eyebrow": "Conceito",
     "linhas": ["Por que começamos", "pela essência?"]},

    # 04 — por que começamos pela essência
    {"tipo": "texto", "eyebrow": "Conceito", "foto": IMG[3], "lado": "direita",
     "titulo": "O que existe por trás da forma como ele protege?",
     "lead": "Uma marca pessoal não começa naquilo que o profissional vende. "
             "Começa na maneira como ele enxerga o mundo, toma decisões, "
             "constrói relações e atribui significado ao próprio trabalho.",
     "paragrafos": [
         "No caso do Lucas, proteção e sucessão são a parte visível. A "
         "pergunta desta etapa é outra: o que existe por trás da forma como "
         "ele protege?",
     ]},

    # 04b — o que não é / o que é
    {"tipo": "camadas", "eyebrow": "Conceito",
     "titulo": "O que esta etapa é — e o que não é",
     "camadas": [
         ("O que não é", "Uma análise psicológica."),
         ("O que é",
          "A investigação dos padrões, crenças e tensões que ajudam a "
          "explicar a origem da sua atuação."),
     ]},

    # 05
    {"tipo": "declaracao",
     "linhas": ["A história não é a revelação.", "A história é a evidência."]},

    # 06 — como chegamos à revelação
    {"tipo": "colunas", "eyebrow": "Método",
     "titulo": "Como chegamos à revelação",
     "lead": "A essência não é um adjetivo. Também não é uma frase bonita "
             "criada para comunicação. Ela aparece quando momentos "
             "aparentemente diferentes revelam uma mesma lógica.",
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

    # 08
    {"tipo": "texto", "eyebrow": "A origem",
     "titulo": "Uma história sobre construção",
     "lead": "Lucas não cresceu vivendo a mesma dificuldade enfrentada pelos "
             "pais. Mas cresceu conhecendo a história de uma família que saiu "
             "do campo, enfrentou escassez, trabalhou, se reorganizou, "
             "adquiriu um terreno, construiu uma casa e conseguiu oferecer "
             "aos filhos uma realidade diferente.",
     "paragrafos": [
         "A importância dessa história não está apenas na origem humilde. "
         "Está no que ela ensina.",
     ],
     "destaque": "Segurança pode levar anos para ser construída."},

    # 09
    {"tipo": "palavras", "eyebrow": "A origem",
     "titulo": "A primeira crença que aparece",
     "lead": "Nada disso aparece na trajetória do Lucas como algo "
             "simplesmente dado. São construções. E aquilo que é construído "
             "carrega tempo, esforço e escolhas.",
     "palavras": ["Casa", "Renda", "Patrimônio",
                  "Carreira", "Empresa", "Estabilidade"],
     "destaque": "O valor não está apenas no que foi conquistado. Está em "
                 "tudo o que foi necessário para chegar até ali."},

    # 10
    {"tipo": "texto", "eyebrow": "A origem", "foto": IMG[4], "lado": "esquerda",
     "titulo": "O segundo aprendizado",
     "lead": "Anos depois, trabalhando na recuperação de ativos do Bradesco, "
             "Lucas passa a enxergar o outro lado dessa lógica.",
     "paragrafos": [
         "Famílias e empresas que levaram anos para construir patrimônio e "
         "estabilidade podiam entrar rapidamente em dificuldade diante de "
         "morte, doença, incapacidade produtiva ou sucessões mal planejadas.",
     ],
     "destaque": "O que leva anos para ser construído pode ser comprometido "
                 "muito rapidamente."},

    # 11
    {"tipo": "declaracao",
     "linhas": ["Talvez o primeiro",
                "grande aprendizado do Lucas",
                "não tenha sido sobre seguro.",
                "Tenha sido sobre fragilidade."]},

    # 12
    {"tipo": "lista", "eyebrow": "A origem",
     "titulo": "O que essa fragilidade significa?",
     "lead": "Não significa acreditar que tudo pode dar errado. Significa "
             "compreender que:",
     "itens": [
         "uma renda pode parar;",
         "uma empresa pode perder uma pessoa essencial;",
         "um patrimônio pode precisar ser desmontado;",
         "uma sucessão pode gerar conflitos;",
         "uma família pode perder, junto com alguém, a estrutura financeira "
         "que sustentava sua vida.",
     ],
     "destaque": "O imprevisto não destrói apenas dinheiro. Ele pode retirar "
                 "possibilidades."},

    # ——— 02 AS TENSÕES
    {"tipo": "divisor", "numero": "02", "nome": "As tensões",
     "apoio": "Os contrastes que revelam o que realmente o coloca em "
              "movimento."},

    # 14
    {"tipo": "texto", "eyebrow": "Primeira tensão", "foto": IMG[12],
     "lado": "direita",
     "titulo": "Segurança × risco",
     "lead": "Existe um paradoxo importante na trajetória do Lucas. Ele "
             "trabalha construindo segurança para outras pessoas. Mas, "
             "quando chegou a um momento decisivo da própria carreira, abriu "
             "mão de uma trajetória sólida no banco para empreender.",
     "destaque": "Lucas não é contra o risco."},

    # 15
    {"tipo": "lista", "eyebrow": "Primeira tensão",
     "titulo": "O risco que ele aceita",
     "lead": "Lucas aceita risco quando existe:",
     "itens": ["decisão;", "consciência;", "possibilidade;", "preparo;",
               "responsabilidade."],
     "destaque": "O que parece incomodá-lo não é a incerteza. É a falta de "
                 "alternativas quando a incerteza se torna real."},

    # 16
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.35, "veu": 0.62,
     "linhas": ["Segurança, para o Lucas,",
                "não é viver sem risco.",
                "É não ficar sem escolha",
                "quando algo acontece."]},

    # 17
    {"tipo": "texto", "eyebrow": "Segunda tensão", "foto": IMG[9],
     "lado": "direita",
     "titulo": "Dinheiro × propósito",
     "lead": "Lucas não romantiza a própria decisão profissional. Ao falar "
             "sobre a mudança de carreira, deixa claro que a possibilidade "
             "financeira pesou.",
     "paragrafos": [
         "Mas também resume sua trajetória com uma frase particularmente "
         "reveladora:",
     ],
     "destaque": "“Fui pelo dinheiro e acabei ficando pelo propósito.”"},

    # 18
    {"tipo": "texto", "eyebrow": "Segunda tensão", "foto": IMG[5],
     "lado": "esquerda",
     "titulo": "O que mudou?",
     "lead": "O dinheiro explicava a oportunidade. Mas não explicava o "
             "significado.",
     "paragrafos": [
         "Esse significado aparece quando Lucas começa a acompanhar "
         "pagamentos de benefícios e percebe concretamente o que uma decisão "
         "tomada anteriormente podia representar na vida de alguém.",
     ],
     "destaque": "O dinheiro explica a entrada. O impacto explica a "
                 "permanência."},

    # 19
    {"tipo": "palavras", "eyebrow": "Segunda tensão",
     "titulo": "Uma leitura mais profunda",
     "lead": "Lucas é movido por tudo isso. Faz parte dele.",
     "palavras": ["Crescimento", "Resultado", "Desempenho",
                  "Reconhecimento", "Realização financeira"],
     "grade": 1, "tam": 22,
     "destaque": "Mas existe algo que torna o resultado mais significativo: "
                 "quando sua performance também produz utilidade real para "
                 "outra pessoa."},

    # 20
    {"tipo": "declaracao",
     "linhas": ["Ele não precisa escolher",
                "entre ambição e propósito.",
                "No Lucas, os dois",
                "podem coexistir."]},

    # 21
    {"tipo": "texto", "eyebrow": "Terceira tensão", "foto": IMG[14],
     "lado": "direita",
     "titulo": "Reconhecimento × exposição",
     "lead": "Lucas acumula reconhecimentos profissionais. Valoriza metas, "
             "valoriza resultado, valoriza estar entre os melhores.",
     "paragrafos": [
         "Mas tem dificuldade declarada em comunicar essas conquistas e se "
         "expor publicamente. Isso cria um aparente paradoxo.",
     ]},

    # 22
    {"tipo": "contraste", "eyebrow": "Terceira tensão",
     "titulo": "O paradoxo é apenas aparente",
     "lead": "O material sugere que Lucas não tem dificuldade com "
             "reconhecimento. Ele tem dificuldade com autoproclamação.",
     "esquerda": ("Existe conforto quando",
                  ["um cliente reconhece;", "uma companhia reconhece;",
                   "um ranking comprova;", "um resultado demonstra."]),
     "direita": ("Existe desconforto quando",
                 ["ele próprio precisa dizer:",
                  "“Olhem o que eu conquistei.”"])},

    # 23
    {"tipo": "texto", "eyebrow": "Terceira tensão", "foto": IMG[8],
     "lado": "esquerda",
     "titulo": "Uma hipótese identitária",
     "lead": "Para o Lucas, legitimidade precisa ser conquistada. Não "
             "declarada.",
     "paragrafos": [
         "Ele parece confiar mais na prova do que na proclamação. Mais no "
         "resultado do que no espetáculo. Mais no reconhecimento externo do "
         "que na autocelebração.",
     ]},

    # 24
    {"tipo": "declaracao",
     "linhas": ["Alta performance.", "Baixa performatividade."]},

    # 25
    {"tipo": "texto", "eyebrow": "Terceira tensão", "foto": IMG[14],
     "lado": "direita",
     "titulo": "O que isso revela?",
     "lead": "Lucas performa muito, mas performatiza pouco. Construiu "
             "autoridade, mas construiu poucos signos públicos dessa "
             "autoridade.",
     "paragrafos": [
         "Essa característica não precisa ser corrigida transformando Lucas "
         "em alguém que gosta de aparecer. Ela pode se transformar em uma "
         "assinatura.",
     ],
     "destaque": "Autoridade discreta."},

    # ——— 03 OS PADRÕES
    {"tipo": "divisor", "numero": "03", "nome": "Os padrões",
     "apoio": "A lógica que se repete por trás de escolhas diferentes."},

    # 27
    {"tipo": "texto", "eyebrow": "Primeiro padrão", "foto": IMG[9],
     "lado": "esquerda",
     "titulo": "Preparar antes é um padrão",
     "lead": "Diante de algo importante, Lucas tende a entender, estudar, "
             "organizar, estruturar e acompanhar.",
     "paragrafos": [
         "Ele não trabalha apenas reagindo. Existe uma tendência recorrente "
         "de criar estrutura antes que ela seja necessária.",
     ]},

    # 28
    {"tipo": "texto", "eyebrow": "Segundo padrão", "foto": IMG[6],
     "lado": "esquerda",
     "titulo": "Resultado não é evento",
     "lead": "A trajetória também revela uma relação forte com constância. "
             "Começa cedo, avança progressivamente no banco, recomeça "
             "profissionalmente, constrói carteira, mantém ritmo e cria metas "
             "próprias.",
     "paragrafos": [
         "Chega a completar 100 semanas consecutivas protegendo três ou mais "
         "famílias por semana.",
     ],
     "destaque": "Para Lucas, resultado não é evento. É repetição bem "
                 "executada."},

    # 29
    {"tipo": "texto", "eyebrow": "Terceiro padrão", "foto": IMG[13],
     "lado": "direita",
     "titulo": "O trabalho não termina na venda",
     "lead": "Lucas não encerra mentalmente o trabalho no momento da venda.",
     "paragrafos": [
         "Relacionamento, proximidade, confiança e pós-venda aparecem "
         "repetidamente como componentes centrais da sua forma de atuar.",
     ],
     "destaque": "Aquilo que precisa continuar exige presença depois do "
                 "começo."},

    # 30
    {"tipo": "fluxo", "eyebrow": "Os padrões",
     "titulo": "O movimento que se repete",
     "passos": ["Entender", "Antecipar", "Estruturar", "Acompanhar",
                "Preservar possibilidades"],
     "sintese": ["Entender antes", "Preparar antes", "Permanecer depois"]},

    # ——— 04 O IKIGAI
    {"tipo": "divisor", "numero": "04", "nome": "O Ikigai",
     "apoio": "Onde capacidade, realização, contribuição e profissão se "
              "encontram."},

    # 32
    {"tipo": "ikigai", "eyebrow": "O Ikigai", "titulo": "O Ikigai",
     "campos": [
         ("O que ele gosta de fazer", "Conversar, compreender e construir."),
         ("No que é bom", "Relacionamento, técnica e planejamento."),
         ("Do que as pessoas precisam", "Preparação antes da urgência."),
         ("Pelo que pode ser remunerado", "Estruturação de proteção."),
     ],
     "centro": "E, principalmente, onde tudo isso ganha significado"},

    # 33
    {"tipo": "texto", "eyebrow": "O Ikigai", "foto": IMG[2], "lado": "esquerda",
     "titulo": "O que Lucas gosta de fazer",
     "lead": "Conversar com o cliente. Entender sua realidade. Fazer "
             "perguntas. Levar o cliente a perceber necessidades que ainda "
             "não estavam claras.",
     "paragrafos": [
         "Pensar. Estruturar. Encontrar uma configuração de proteção que faça "
         "sentido para aquela realidade.",
     ],
     "destaque": "A satisfação não está apenas em vender. Está em compreender "
                 "e construir."},

    # 34
    {"tipo": "texto", "eyebrow": "O Ikigai", "foto": IMG[11], "lado": "direita",
     "titulo": "No que Lucas é bom",
     "lead": "Relacionamento, comunicação, conexão e construção de confiança. "
             "Conhecimento técnico, leitura da realidade do cliente, "
             "planejamento, constância e pós-venda.",
     "destaque": "Sua principal competência não é apenas conhecer produtos. É "
                 "transformar complexidade em uma decisão estruturada."},

    # 35
    {"tipo": "lista", "eyebrow": "O Ikigai", "foto": IMG[9], "lado": "esquerda", "foco": 0.26,
     "titulo": "Pelo que Lucas pode ser pago",
     "itens": [
         "Diagnosticar vulnerabilidades financeiras.",
         "Estruturar proteção de renda.",
         "Criar proteção familiar.",
         "Proteger pessoas-chave.",
         "Planejar sucessões.",
         "Criar liquidez.",
         "Preservar patrimônio.",
         "Organizar alternativas para famílias e empresas.",
     ],
     "destaque": "Sua remuneração vem da estruturação de proteção."},

    # 36
    {"tipo": "texto", "eyebrow": "O Ikigai", "foto": IMG[5], "lado": "direita",
     "titulo": "Do que o mundo precisa, na visão de Lucas",
     "lead": "Mais preparação antes da urgência. Mais pessoas conscientes dos "
             "riscos que carregam. Mais famílias com recursos para atravessar "
             "imprevistos.",
     "paragrafos": [
         "Mais empresas preparadas para ausência, sucessão e transição. Mais "
         "patrimônio protegido de decisões tomadas sob pressão. O legado que "
         "Lucas declara desejar é justamente ampliar a cultura da importância "
         "da proteção diante de um imprevisto.",
     ]},

    # 37–40 — os quatro cruzamentos
    {"tipo": "foto_cheia", "eyebrow": "Paixão — o que ama + no que é bom",
     "foto": IMG[2], "veu": 0.62,
     "linhas": ["Conversar, compreender",
                "e construir soluções que façam",
                "sentido para cada realidade."]},

    {"tipo": "texto", "eyebrow": "Profissão", "foto": IMG[11], "lado": "direita",
     "titulo": "No que é bom + pelo que pode ser pago",
     "destaque": "Estruturar proteção e sucessão com visão consultiva, "
                 "personalização e relacionamento.",
     "tam_destaque": 28},

    {"tipo": "texto", "eyebrow": "Missão", "foto": IMG[13], "lado": "esquerda",
     "titulo": "O que o mundo precisa + o que ele gosta de fazer",
     "destaque": "Ampliar a consciência de que preparação financeira também é "
                 "uma forma de cuidado e responsabilidade.",
     "tam_destaque": 28},

    # Tela cheia: com estas fotos, o horizontal que nao corta rosto nenhum
    # e este — a imagem inteira, sem recorte, e o texto por cima.
    {"tipo": "foto_cheia",
     "eyebrow": "Vocação — o que o mundo precisa + pelo que pode ser pago",
     "foto": IMG[12], "veu": 0.60,
     "linhas": ["Ajudar pessoas, famílias e empresas",
                "a chegarem mais preparadas aos",
                "momentos que não podem controlar."]},

    # 41
    {"tipo": "lista", "eyebrow": "O Ikigai", "foto": IMG[5], "lado": "esquerda", "foco": 0.18,
     "titulo": "Onde Lucas encontra realização",
     "lead": "Quando o planejamento deixa de ser uma hipótese e passa a "
             "cumprir aquilo para o qual foi criado.",
     "itens": [
         "Quando um benefício é pago.",
         "Quando uma família recebe recursos.",
         "Quando uma empresa pode continuar.",
         "Quando aquilo que foi planejado anteriormente reduz o impacto de um "
         "momento difícil.",
     ],
     "destaque": "É aí que o trabalho deixa de ser produto e se torna "
                 "consequência real."},

    # 42
    {"tipo": "lista", "eyebrow": "O Ikigai",
     "titulo": "Dignidade financeira",
     "lead": "Lucas utiliza uma expressão especialmente importante para falar "
             "sobre o impacto do seu trabalho: “dignidade financeira”. Ela "
             "não significa apenas dinheiro disponível.",
     "itens": [
         "Significa manter possibilidades quando a vida muda.",
         "Não precisar desmontar tudo.",
         "Não precisar aceitar qualquer saída.",
         "Não transformar uma perda humana em colapso financeiro.",
     ]},

    # 43
    {"tipo": "declaracao",
     "linhas": ["Dinheiro, nessa lógica,",
                "não é o fim.",
                "É o que preserva",
                "possibilidades."]},

    # 44
    {"tipo": "texto", "eyebrow": "O Ikigai",
     "titulo": "O centro do Ikigai",
     "lead": "Quando cruzamos aquilo que Lucas gosta de fazer, suas "
             "capacidades, seu trabalho e o impacto que mais o realiza, "
             "aparece algo maior do que proteção financeira.",
     "destaque": "Preservar a capacidade de escolha quando a vida tira a "
                 "previsibilidade.",
     "tam_destaque": 28},

    # 45 — razão de ser
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.40, "veu": 0.66,
     "eyebrow": "Razão de ser",
     "linhas": ["Preservar a capacidade",
                "de escolha quando a vida",
                "tira a previsibilidade."]},

    # ——— 05 A ESSÊNCIA
    {"tipo": "divisor", "numero": "05", "nome": "A essência",
     "apoio": "O princípio mais profundo que conecta sua trajetória."},

    # 47
    {"tipo": "camadas", "eyebrow": "A essência",
     "titulo": "Onde tudo se encontra",
     "camadas": [
         ("A origem", "Ensinou que segurança é construída."),
         ("O banco",
          "Mostrou como aquilo que levou anos para existir pode se "
          "fragilizar rapidamente."),
         ("O empreendedorismo",
          "Mostrou que Lucas aceita risco quando pode escolher "
          "conscientemente."),
         ("A profissão", "Mostrou que preparação preserva possibilidades."),
         ("O Ikigai",
          "Mostrou que o maior significado aparece quando aquilo que ele "
          "planejou sustenta alguém no momento em que é necessário."),
     ]},

    # 48
    {"tipo": "declaracao", "eyebrow": "A crença fundadora", "marcar": True,
     "linhas": ["O que levou anos",
                "para ser construído",
                "não deveria ficar",
                "entregue ao acaso."]},

    # 49
    {"tipo": "texto", "eyebrow": "A essência", "foto": IMG[1],
     "lado": "direita",
     "titulo": "Uma frase do próprio Lucas",
     "lead": "Lucas define uma parte importante da própria atuação como "
             "“buscar sempre chegar antes do imprevisto”.",
     "paragrafos": [
         "Essa frase tem um significado maior do que simplesmente vender "
         "proteção antecipadamente.",
     ]},

    # 50
    {"tipo": "texto", "eyebrow": "A essência", "foto": IMG[12],
     "lado": "direita",
     "titulo": "O que significa chegar antes?",
     "lead": "Chegar antes é preservar tempo para decidir. É poder construir "
             "alternativas sem urgência. É impedir que uma situação "
             "inesperada seja a única força determinando aquilo que virá "
             "depois.",
     "destaque": "Chegar antes é preservar escolhas."},

    # 51
    {"tipo": "declaracao",
     "linhas": ["Lucas não trabalha",
                "para controlar o imprevisto.",
                "Trabalha para que ele não decida",
                "sozinho o que vem depois."]},

    # 52 — a essência
    {"tipo": "foto_cheia", "foto": IMG[3], "foco": 0.45, "veu": 0.68,
     "eyebrow": "A essência de Lucas",
     "linhas": ["Construir segurança para", "preservar liberdade de escolha."]},

    # 52b — as três camadas da essência
    {"tipo": "colunas", "eyebrow": "A essência de Lucas",
     "titulo": "Construir segurança para preservar liberdade de escolha",
     "tam_titulo": 34,
     "colunas": [
         ("Construir segurança",
          "Transformar vulnerabilidades em planejamento, recursos e "
          "alternativas."),
         ("Preservar liberdade",
          "Manter possibilidades mesmo diante de acontecimentos que fogem ao "
          "controle."),
         ("Escolha",
          "Evitar que a urgência seja a única responsável pelas decisões."),
     ]},

    # 53
    {"tipo": "palavras", "eyebrow": "A essência",
     "titulo": "A essência não é um adjetivo",
     "lead": "São características do Lucas. Mas nenhuma delas, isoladamente, "
             "explica sua trajetória.",
     "palavras": ["Responsável", "Disciplinado", "Ambicioso", "Confiável",
                  "Preparado", "Constante", "Consultivo"],
     "grade": 2, "tam": 22,
     "destaque": "Elas são manifestações de uma lógica mais profunda: "
                 "preparar o que pode ser preparado para proteger o que não "
                 "pode ser previsto."},

    # ——— 06 A MARCA
    {"tipo": "divisor", "numero": "06", "nome": "A marca",
     "apoio": "O que essa essência revela sobre o papel que Lucas pode "
              "ocupar."},

    # 55
    {"tipo": "texto", "eyebrow": "A marca", "foto": IMG[2], "lado": "esquerda",
     "titulo": "O que essa essência muda?",
     "lead": "Muda o entendimento sobre aquilo que Lucas vende. Na "
             "superfície: seguro, proteção, sucessão, liquidez, planejamento.",
     "destaque": "Em profundidade, ele cria estruturas que preservam "
                 "possibilidades."},

    # 56
    {"tipo": "camadas", "eyebrow": "A marca",
     "titulo": "O produto não é o centro",
     "camadas": [
         ("Seguro", "É instrumento."),
         ("Planejamento", "É método."),
         ("Proteção e sucessão", "São campos de atuação."),
         ("Continuidade", "É o território."),
         ("Liberdade de escolha", "É o significado humano."),
     ]},

    # 57
    {"tipo": "lista", "eyebrow": "A marca", "foto": IMG[8], "lado": "direita", "foco": 0.24,
     "titulo": "Uma segunda revelação",
     "lead": "A dificuldade de comunicação do Lucas não exige que ele se "
             "transforme em alguém que não é. Sua marca pode ser construída "
             "pela lógica que já existe nele: prova, não proclamação.",
     "itens": ["Resultados.", "Casos.", "Conhecimento.",
               "Reconhecimentos contextualizados.", "Experiência.",
               "Raciocínio.", "Consistência."]},

    # 58
    {"tipo": "foto_cheia", "foto": IMG[14], "foco": 0.12, "veu": 0.60,
     "linhas": ["Ele não precisa",
                "se tornar mais exibido.",
                "Precisa tornar mais visível",
                "aquilo que já construiu."]},

    # 59
    {"tipo": "declaracao",
     "linhas": ["A essência revela a origem.",
                "A estratégia define a direção."]},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
