# -*- coding: utf-8 -*-
"""
CULTURA ORGANIZACIONAL E CULTURA DE MARCA — FORMA e My Home

**Uma apresentação só.** A cultura organizacional e as duas culturas de marca
vivem no mesmo documento: a organizacional é compartilhada pelas duas
empresas, e cada marca tem a sua seção dentro dele. Foi o pedido da Kelly, e
este arquivo substitui os três que existiam antes (`cultura.py` da
organizacional + `marca_forma.py` + `marca_my_home.py`).

Identidade, grade, paleta e escala são as de sempre (padrao-ka/ka_layout.py e
padrao-ka/ka_paginas.py): painel claro sobre a textura de ondas, Outfit,
acento terracota. Sem rodapé. Voz em terceira pessoa, como manda o CLAUDE.md.

As 19 páginas do roteiro saem em 40, pela regra de sempre — **um título e um
bloco de texto por página**. Cada slide do roteiro carregava de três a cinco
blocos (definição, método, elementos, crença, valores, personalidade,
expressão), e empilhar isso é o que a regra proíbe. Os arquétipos fazem o
trabalho:

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` com foto | as cinco viradas de seção, em tela cheia de imagem | 5 |
| `declaracao` | a página de silêncio: uma crença, uma descoberta | 8 |
| `colunas` | os campos em paralelo — comportamento, experiência, percepção | 8 |
| `camadas` | rótulo e leitura lado a lado — valores, tensões, síntese | 3 |
| `palavras` | os elementos investigados e a liderança, como composição | 3 |
| `contraste` | as duas essências culturais, separadas pelo × | 1 |
| `foto_cheia` | a essência de cada marca, em tela cheia | 2 |
| `texto` | só onde o conteúdo é mesmo narrativa | 7 |

Uma observação de estrutura, assinalada e não silenciosa: o sumário do
roteiro traz quatro seções (organizacional, marca Forma, marca My Home,
síntese), mas o corpo abre "02. CULTURA DE MARCA" com o conceito e o método
**antes** de entrar em cada marca. Como esse conceito vale para as duas, ele
virou a seção 02 e as marcas passaram a 03 e 04 — assim o sumário e as
viradas contam a mesma história. São cinco seções numeradas.

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela. Quando o arquivo entrar em `assets/` com o nome declarado em
`foto`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py cultura
"""

MARCA = "FORMA e My Home"
DOCUMENTO = "Cultura Organizacional e de Marca"
RODAPE = False
ARQUIVO = "Cultura-Organizacional-e-de-Marca-Forma-e-My-Home"

IMG = {
    "div1": "cultura-div-organizacional.png",
    "div2": "cultura-div-marca.png",
    "div3": "cultura-div-forma.png",
    "div4": "cultura-div-my-home.png",
    "div5": "cultura-div-sintese.png",
    "origem": "cultura-oficina-forma.png",
    "forma": "cultura-projeto-forma.png",
    "myhome": "cultura-produto-my-home.png",
    "ess_forma": "cultura-ambiente-forma.png",
    "ess_myhome": "cultura-produto-em-casa.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    # ——————————————————————————————————————————— 01 CAPA
    {"tipo": "capa",
     "titulo": ["O QUE DEFINE", "A FORMA E A MY HOME"],
     "subtitulo": ["Cultura Organizacional e de Marca", "FORMA e My Home"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["Uma cultura organizacional compartilhada.",
                "Duas culturas de marca",
                "com identidades próprias."]},

    # ——————————————————————————————————————————— 02 SUMÁRIO
    {"tipo": "sumario", "titulo": "Cultura e identidade", "itens": [
        ("01", "Cultura organizacional",
         "Origem, valores, liderança e comportamentos compartilhados."),
        ("02", "Cultura de marca",
         "O conceito e o método que valem para as duas marcas."),
        ("03", "Cultura de marca Forma",
         "Uma marca orientada à realização."),
        ("04", "Cultura de marca My Home",
         "Uma marca orientada à criação."),
        ("05", "Síntese",
         "O que conecta as empresas e o que diferencia cada marca."),
    ]},

    # ═══════════════════════════════════ 01 CULTURA ORGANIZACIONAL
    {"tipo": "divisor", "numero": "01", "nome": "Cultura organizacional",
     "apoio": "Origem, valores, liderança e comportamentos compartilhados.",
     "foto": IMG["div1"],
     "imagem": "A oficina com várias pessoas trabalhando ao mesmo tempo. "
               "Plano aberto, o coletivo em ação."},

    {"tipo": "texto", "titulo": "O que é **cultura organizacional**?",
     "paragrafos": [
         "É o conjunto de crenças, valores, comportamentos e práticas "
         "compartilhadas que orientam a maneira como as pessoas trabalham, "
         "se relacionam e tomam decisões dentro de uma organização.",
     ]},

    {"tipo": "texto", "titulo": "Como foi mapeada",
     "paragrafos": [
         "A análise considerou a história da fundadora, entrevistas com oito "
         "colaboradores, relatos da liderança e depoimentos de clientes e "
         "arquitetos.",
         "O objetivo: identificar o que é declarado, o que é vivenciado e "
         "quais características precisam ser preservadas ou desenvolvidas.",
     ]},

    {"tipo": "palavras", "titulo": "Os sete elementos investigados",
     "palavras": ["História e origem", "Valores e crenças", "Liderança",
                  "Comportamentos", "Relações internas", "Práticas e rituais",
                  "Tensões culturais"]},

    {"tipo": "texto", "foto": IMG["origem"], "lado": "direita",
     "imagem": "A origem do ofício: a primeira oficina, uma máquina em "
               "operação, ou o lugar onde tudo começou.",
     "titulo": "Não aceitar o limite como **resposta definitiva**.",
     "paragrafos": [
         "A trajetória de Flávia revela uma mentalidade recorrente: diante "
         "das limitações, buscar novas possibilidades.",
         "Essa característica influenciou a criação e o crescimento das "
         "empresas e encontra correspondência na iniciativa e na capacidade "
         "de resolução relatadas pelos colaboradores.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Uma dificuldade não precisa",
                "determinar o resultado final."],
     "apoio": "A crença de origem."},

    {"tipo": "camadas",
     "titulo": "**Liberdade** para agir. **Responsabilidade** para entregar.",
     "camadas": [
         ("Comprometimento", "Responsabilidade pelo resultado."),
         ("Autonomia", "Liberdade para encontrar soluções."),
         ("Excelência", "Exigência com a qualidade."),
         ("Cooperação", "Compromisso com o trabalho coletivo."),
         ("Evolução", "Busca contínua por conhecimento e melhoria."),
     ]},

    {"tipo": "palavras", "titulo": "A liderança identificada", "grade": 1,
     "palavras": ["Próxima", "Acessível", "Exigente",
                  "Orientada à realização"]},

    {"tipo": "declaracao",
     "linhas": ["Competência não se limita",
                "ao conhecimento técnico.",
                "Também exige envolvimento com aquilo",
                "que precisa ser realizado."],
     "apoio": "A crença compartilhada."},

    {"tipo": "colunas", "titulo": "A cultura se revela **diante dos problemas**.",
     "colunas": [
         ("Resolver",
          "Tomar iniciativa sem depender de ordens para cada decisão."),
         ("Cuidar",
          "Corrigir aquilo que não atende ao padrão e considerar o impacto "
          "sobre o cliente."),
         ("Colaborar",
          "Ajudar outras pessoas e áreas para assegurar a entrega."),
     ],
     "fecho": "Esses comportamentos são favorecidos por relações próximas, "
              "diálogo e sentimento de pertencimento."},

    {"tipo": "declaracao",
     "linhas": ["A responsabilidade não termina",
                "no limite de uma função.",
                "Ela se estende ao resultado coletivo."],
     "apoio": "A descoberta cultural."},

    {"tipo": "camadas",
     "titulo": "O crescimento exige a **evolução da cultura**.",
     "cabecalhos": ("Força identificada", "Desafio do crescimento"),
     "camadas": [
         ("Proximidade", "Desenvolver novas lideranças."),
         ("Autonomia", "Estabelecer critérios compartilhados."),
         ("Agilidade", "Estruturar processos previsíveis."),
         ("Excelência", "Reproduzir padrões em escala."),
         ("Cooperação", "Definir responsabilidades entre operações."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Transformar uma cultura fortemente",
                "influenciada pela fundadora em princípios",
                "e práticas sustentados por toda a organização."],
     "apoio": "O desafio central."},

    # ═══════════════════════════════════════ 02 CULTURA DE MARCA
    {"tipo": "divisor", "numero": "02", "nome": "Cultura de marca",
     "apoio": "O conceito e o método que valem para as duas marcas.",
     "foto": IMG["div2"],
     "imagem": "Um detalhe de acabamento em plano fechado — a junção, a "
               "borda, a textura. A identidade vista de perto."},

    {"tipo": "texto", "titulo": "O que é **cultura de marca**?",
     "paragrafos": [
         "É o conjunto de crenças, valores e princípios que orientam a "
         "identidade de uma marca, manifestando-se em seus comportamentos, "
         "produtos, comunicação e experiência oferecida ao público.",
     ]},

    {"tipo": "texto", "titulo": "Como foi mapeada",
     "paragrafos": [
         "A análise cruzou a história e as intenções da fundadora, os "
         "documentos de identidade verbal, as percepções dos colaboradores e "
         "os depoimentos de clientes e arquitetos.",
         "O objetivo: identificar a identidade cultural de cada marca, "
         "distinguindo atributos já reconhecidos no mercado daqueles que "
         "ainda precisam ser desenvolvidos.",
     ]},

    {"tipo": "palavras", "titulo": "Os sete elementos investigados",
     "palavras": ["Origem e significado", "Valores",
                  "Personalidade e expressão", "Comportamento da equipe",
                  "Experiência entregue", "Percepção externa", "Coerência"]},

    # ═══════════════════════════════════════════════════ 03 FORMA
    {"tipo": "divisor", "numero": "03", "nome": "Forma",
     "apoio": "Cultura de marca · uma marca orientada à realização.",
     "foto": IMG["div3"],
     "imagem": "Um projeto complexo em execução — marcenaria sob medida, "
               "encaixe, peça grande em montagem."},

    {"tipo": "texto", "foto": IMG["forma"], "lado": "direita",
     "imagem": "Uma conversa técnica sobre o projeto — prancha, amostra de "
               "material, desenho na mesa.",
     "titulo": "A liberdade de criar exige a **capacidade de realizar**.",
     "paragrafos": [
         "A Forma representa a liberdade conquistada para executar projetos "
         "sem ficar restrita às limitações dos sistemas padronizados.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Uma ideia singular merece",
                "uma execução à sua altura."],
     "apoio": "A crença central da Forma."},

    {"tipo": "colunas", "titulo": "Os valores e a personalidade da **Forma**",
     "colunas": [
         ("Valores",
          "Precisão · Personalização · Responsabilidade · Confiança · "
          "Evolução técnica"),
         ("Personalidade", "Segura · Criteriosa · Técnica · Próxima"),
     ],
     "fecho": "Expressão da marca: sofisticação sustentada pelo conhecimento "
              "e pela competência."},

    {"tipo": "colunas",
     "titulo": "O verdadeiro alto padrão é a **tranquilidade de quem confia**.",
     "colunas": [
         ("Comportamento",
          "Compreender o projeto, antecipar dificuldades, encontrar soluções "
          "e assumir responsabilidade pela execução."),
         ("Experiência entregue",
          "Segurança para realizar projetos personalizados e complexos, com "
          "precisão, acompanhamento e atenção aos detalhes."),
     ],
     "fecho": "O significado da experiência: a confiança não está apenas no "
              "resultado final, mas na tranquilidade proporcionada durante "
              "todo o processo."},

    {"tipo": "colunas", "titulo": "Transformar complexidade em **confiança**.",
     "colunas": [
         ("Percepção reconhecida",
          "Arquitetos e clientes destacam domínio técnico, qualidade de "
          "execução, cuidado com os detalhes e parceria."),
         ("Desafio da marca",
          "Preservar a personalização e a proximidade mesmo com a expansão "
          "industrial."),
     ]},

    {"tipo": "foto_cheia", "foto": IMG["ess_forma"],
     "imagem": "Um ambiente completo entregue pela Forma. Imagem ampla, que "
               "aguente a frase por cima.",
     "linhas": ["Precisão que realiza."],
     "apoio": "A essência cultural da Forma."},

    # ═══════════════════════════════════════════════ 04 MY HOME
    {"tipo": "divisor", "numero": "04", "nome": "My Home",
     "apoio": "Cultura de marca · uma marca orientada à criação.",
     "foto": IMG["div4"],
     "imagem": "A bancada de criação: protótipo, teste de acabamento, peça "
               "em desenvolvimento."},

    {"tipo": "texto", "foto": IMG["myhome"], "lado": "esquerda",
     "imagem": "O material antes de virar produto — a sobra, o retalho, a "
               "chapa separada. O ponto de partida.",
     "titulo": "Enxergar **possibilidades** onde outros enxergam limites.",
     "paragrafos": [
         "A My Home nasceu do inconformismo diante do desperdício e da "
         "capacidade de transformar materiais descartados em novas criações.",
         "O reaproveitamento foi o ponto de partida. A inventividade "
         "constitui sua principal oportunidade de diferenciação.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["O valor de um material não se limita",
                "ao uso para o qual",
                "foi originalmente pensado."],
     "apoio": "A crença central da My Home."},

    {"tipo": "colunas", "titulo": "Os valores e a personalidade da **My Home**",
     "colunas": [
         ("Valores",
          "Inventividade · Transformação · Originalidade · Qualidade · "
          "Acessibilidade · Evolução"),
         ("Personalidade", "Criativa · Curiosa · Expressiva · Próxima"),
     ]},

    {"tipo": "colunas",
     "titulo": "Criar não é improvisar. É **transformar com conhecimento**.",
     "colunas": [
         ("Comportamento",
          "Experimentar possibilidades, compartilhar ideias, dominar "
          "técnicas e aperfeiçoar materiais e acabamentos."),
         ("Experiência pretendida",
          "Oferecer produtos originais que despertem descoberta, surpreendam "
          "e acrescentem personalidade aos ambientes."),
     ],
     "fecho": "O significado da experiência: a criatividade transforma "
              "materiais e objetos em novas possibilidades para a casa."},

    {"tipo": "colunas", "titulo": "Transformar possibilidades em **criação**.",
     "colunas": [
         ("Percepção reconhecida",
          "Arquitetos valorizam a capacidade técnica da My Home para "
          "executar acabamentos, detalhes e soluções especiais."),
         ("Desafio da marca",
          "Consolidar sua identidade independente e ser reconhecida pelo "
          "consumidor final pela criatividade, originalidade e qualidade dos "
          "produtos."),
     ]},

    {"tipo": "foto_cheia", "foto": IMG["ess_myhome"],
     "imagem": "Um produto My Home em destaque no ambiente. Imagem ampla, "
               "que aguente a frase por cima.",
     "linhas": ["Criatividade que transforma."],
     "apoio": "A essência cultural da My Home."},

    # ═══════════════════════════════════════════════ 05 SÍNTESE
    {"tipo": "divisor", "numero": "05", "nome": "Síntese",
     "apoio": "O que conecta as empresas e o que diferencia cada marca.",
     "foto": IMG["div5"],
     "imagem": "O time completo das duas operações, ou o ambiente de "
               "trabalho cheio de gente. Plano aberto."},

    {"tipo": "camadas",
     "titulo": "Uma cultura compartilhada. **Duas identidades de marca**.",
     "camadas": [
         ("Cultura organizacional",
          "Proximidade, autonomia, cooperação e responsabilidade pelo "
          "resultado."),
         ("Forma",
          "A liberdade de personalizar encontra valor na precisão e na "
          "confiança da execução."),
         ("My Home",
          "A liberdade de imaginar encontra valor na criatividade e na "
          "transformação."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["As duas marcas compartilham uma mentalidade",
                "de superação dos limites,",
                "mas a expressam de maneiras diferentes."]},

    {"tipo": "contraste", "titulo": "As duas essências culturais.",
     "esquerda": ("Forma", ["Transformar complexidade em confiança."]),
     "direita": ("My Home", ["Transformar possibilidades em criação."])},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
