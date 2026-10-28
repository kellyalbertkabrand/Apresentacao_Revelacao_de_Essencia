# -*- coding: utf-8 -*-
"""
O QUE TORNA ESSAS MARCAS ÚNICAS — Cultura Organizacional e Cultura de Marca
FORMA · MY HOME

Apresentação nova, no formato que a Kelly rediagramou à mão em outubro/2026 e
que está medido em `padrao-ka/PADRAO-KELLY.md`. Nada aqui é estilo novo: é o
padrão aplicado a um roteiro mais fundo que o da versão anterior — este traz
os depoimentos nominais, as três situações da equipe, a tabela de forças e
desafios, os pontos de atenção e as duas essências culturais.

Ela **não substitui** `cultura.py`: aquela continua no diretório, com o
roteiro antigo. Esta é a apresentação pedida depois do mapeamento.

O que o padrão impõe e este arquivo obedece:

- **um título e um bloco de texto por página** — nada empilhado. Cada slide
  do roteiro carregava três, quatro, cinco blocos (definição, método,
  elementos, crença, valores, personalidade, expressão); os arquétipos
  distribuem isso em páginas;
- **a frase-chave do título em Bold**, marcada com `**`. Título de duas ou
  três palavras fica sem marcação — o negrito só funciona como exceção;
- **voz em terceira pessoa** (CLAUDE.md). As duas falas entre aspas são
  citação de discurso — o Joel e a Pâmella falando —, não afirmação sobre a
  marca, e por isso ficam como foram ditas;
- **sem rodapé**, como ela pediu nas apresentações da Flávia.

A estrutura segue o sumário dela: **quatro seções numeradas**. A virada
"Cultura de marca · Forma e My Home" entra **sem número**, como ponte — é o
conceito que vale para as duas marcas, exatamente onde o roteiro a coloca. As
viradas internas ("História e origem", "Comportamentos e experiência",
"Percepção externa e coerência") também são sem número: são os sub-abres do
próprio roteiro, e a hierarquia fica legível porque só as quatro seções levam
numeral e fotografia.

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` | 4 viradas de seção com foto + 8 sub-abres tipográficos | 12 |
| `declaracao` | a página de silêncio: uma crença, uma descoberta | 11 |
| `texto` | narrativa — origem, história, ponto de atenção | 12 |
| `colunas` | campos em paralelo: valores, cultura em ação, experiência | 6 |
| `camadas` | rótulo e leitura lado a lado: valores, depoimentos, tabela | 6 |
| `palavras` | os elementos investigados, como composição | 2 |
| `foto_cheia` | as duas falas e as duas essências, em tela cheia | 4 |

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO: a área exata, identificada, com o briefing. Quando o arquivo entrar
em `assets/` com o nome declarado em `foto`, a marcação some e nada muda de
lugar.

    python3 clientes/flavia-muccelin/gerar.py marcas_unicas
"""

MARCA = "FORMA e My Home"
DOCUMENTO = "Cultura Organizacional e de Marca"
RODAPE = False
ARQUIVO = "O-Que-Torna-Essas-Marcas-Unicas-Forma-e-My-Home"

IMG = {
    "div1": "cultura-div-organizacional.png",
    "div2": "cultura-div-forma.png",
    "div3": "cultura-div-my-home.png",
    "div4": "cultura-div-sintese.png",
    "origem": "cultura-oficina-forma.png",
    "obra": "cultura-obra-cliente.png",
    "forma": "cultura-projeto-forma.png",
    "ess_forma": "cultura-ambiente-forma.png",
    "myhome": "cultura-produto-my-home.png",
    "producao": "cultura-producao-my-home.png",
    "ess_myhome": "cultura-produto-em-casa.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    # ——————————————————————————————————————————————————————— CAPA
    {"tipo": "capa",
     "titulo": ["O QUE TORNA", "ESSAS MARCAS ÚNICAS"],
     "subtitulo": ["Cultura Organizacional e Cultura de Marca",
                   "FORMA · MY HOME"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["Uma história que construiu uma cultura.",
                "Uma cultura que sustenta duas marcas."]},

    # ———————————————————————————————————————————————————— SUMÁRIO
    {"tipo": "sumario", "titulo": "O caminho", "itens": [
        ("01", "Cultura organizacional",
         "A história, as crenças e os comportamentos que conectam as duas "
         "empresas."),
        ("02", "Cultura de marca Forma",
         "A capacidade de transformar projetos complexos em confiança."),
        ("03", "Cultura de marca My Home",
         "A capacidade de transformar possibilidades em criação."),
        ("04", "Síntese",
         "O que compartilham e o que torna cada marca singular."),
    ]},

    # ═══════════════════════════════════ 01 CULTURA ORGANIZACIONAL
    {"tipo": "divisor", "numero": "01", "nome": "Cultura organizacional",
     "apoio": "A história, as crenças e os comportamentos que conectam as "
              "duas empresas.",
     "foto": IMG["div1"],
     "imagem": "A oficina com várias pessoas trabalhando ao mesmo tempo. "
               "Plano aberto, o coletivo em ação."},

    {"tipo": "texto", "titulo": "O que é **cultura organizacional**?",
     "paragrafos": [
         "É o conjunto de crenças, valores e comportamentos que determina "
         "como as pessoas pensam, decidem, se relacionam e trabalham, mesmo "
         "quando ninguém está dizendo o que fazer.",
     ]},

    {"tipo": "texto", "titulo": "Como foi **mapeada**",
     "paragrafos": [
         "A análise cruzou a história da fundadora, entrevistas com oito "
         "colaboradores, relatos da liderança e depoimentos de clientes e "
         "arquitetos.",
         "Mais do que identificar valores declarados, o objetivo foi "
         "compreender quais princípios aparecem nas atitudes e decisões do "
         "cotidiano.",
     ]},

    {"tipo": "palavras", "titulo": "O que foi **investigado**",
     "palavras": ["História e origem", "Valores e crenças", "Liderança",
                  "Comportamentos", "Relações internas", "Práticas e rituais",
                  "Tensões culturais"]},

    # —————————————————————————————————————————— história e origem
    {"tipo": "divisor", "nome": "História e origem"},

    {"tipo": "texto", "foto": IMG["origem"], "lado": "direita",
     "imagem": "A origem do ofício: a primeira oficina, uma máquina em "
               "operação, ou o lugar onde tudo começou.",
     "titulo": "Não aceitar o limite como **resposta definitiva**.",
     "paragrafos": [
         "A trajetória profissional e pessoal da Flávia revela o movimento "
         "de não aceitar que a posição de funcionária definisse seu futuro, "
         "que os padrões das franquias limitassem suas ideias ou que "
         "materiais descartados não pudessem ter outro destino.",
         "Essa mentalidade aparece nas equipes como disposição para buscar "
         "soluções, aprender e fazer acontecer.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["As circunstâncias podem estabelecer condições,",
                "mas não precisam determinar",
                "até onde é possível chegar."],
     "apoio": "A crença de origem."},

    # ———————————————————————————————— valores, crenças e liderança
    {"tipo": "divisor", "nome": "Valores, crenças e liderança",
     "apoio": "As entrevistas revelam uma combinação particular de "
              "liberdade, exigência e proximidade humana."},

    {"tipo": "camadas",
     "titulo": "**Liberdade** para agir. **Responsabilidade** para entregar.",
     "camadas": [
         ("Autonomia", "Liberdade para encontrar soluções e agir com "
                       "iniciativa."),
         ("Comprometimento", "Responsabilidade que ultrapassa a tarefa "
                             "individual."),
         ("Excelência", "Não aceitar uma entrega que poderia ter sido "
                        "melhor."),
         ("Cooperação", "Compreender que o resultado depende de muitas "
                        "mãos."),
         ("Evolução", "Aprender continuamente para ampliar o que é possível "
                      "realizar."),
     ]},

    {"tipo": "camadas",
     "titulo": "A **liderança** por trás dessa cultura",
     "camadas": [
         ("Tanyllo", "Descreve a liberdade de trabalhar sem medo de propor "
                     "soluções."),
         ("Pâmella", "Destaca a facilidade de acesso à Flávia, "
                     "independentemente do cargo."),
         ("Letícia", "Reconhece a iniciativa e a força de vontade como "
                     "atitudes especialmente valorizadas."),
         ("A leitura", "A liderança é percebida como próxima, exigente e "
                       "acessível."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["O que distingue essa cultura não é apenas",
                "a liberdade oferecida às pessoas.",
                "É a confiança depositada na capacidade",
                "delas de assumir responsabilidades."]},

    # —————————————————————— comportamentos, relações e práticas
    {"tipo": "divisor", "nome": "Comportamentos, relações e práticas",
     "apoio": "Três situações relatadas pelos colaboradores revelam mais do "
              "que qualquer declaração de valores."},

    {"tipo": "colunas",
     "titulo": "A cultura se revela **diante dos problemas**.",
     "colunas": [
         ("Resolver · Letícia",
          "Quando uma peça chega à obra com defeito, a própria equipe se "
          "mobiliza para corrigir. Nem toda decisão precisa passar pela "
          "liderança."),
         ("Cuidar · Mapinha",
          "Em experiências anteriores, presenciou empresas aceitarem peças "
          "inadequadas na esperança de que o cliente não percebesse. Na "
          "Forma e na My Home, descreve uma orientação diferente: se não "
          "ficou bom, é necessário refazer."),
         ("Se importar · Joel",
          "A equipe procura ajudar até quando o problema surgiu com outros "
          "prestadores de serviço, porque reconhece o desgaste que o cliente "
          "já enfrentou durante a obra."),
     ]},

    {"tipo": "foto_cheia", "foto": IMG["obra"],
     "imagem": "A obra em andamento, do ponto de vista de quem mora ali: o "
               "ambiente ainda em processo. Imagem ampla.",
     "linhas": ["“Então a gente tenta",
                "amenizar o máximo possível",
                "[...] pra que ele",
                "não sofra mais.”"],
     "apoio": "Joel, sobre o cliente que já atravessou o desgaste de uma "
              "obra."},

    {"tipo": "declaracao", "eyebrow": "A descoberta cultural mais profunda",
     "marcar": True,
     "linhas": ["A responsabilidade não termina",
                "quando a própria tarefa acaba."],
     "apoio": "Existe uma disposição de cuidar do resultado e das pessoas "
              "afetadas por ele."},

    # —————————————————————————————————————————————— o crescimento
    {"tipo": "texto",
     "titulo": "O crescimento exige a **evolução da cultura**.",
     "paragrafos": [
         "A cultura foi construída com relações próximas, pessoas "
         "experientes e grande capacidade de resolver situações inesperadas.",
         "Mas a expansão exige que essas forças deixem de depender apenas de "
         "quem já conhece profundamente o negócio.",
     ]},

    {"tipo": "camadas",
     "titulo": "O que sustenta hoje e **o que a escala vai pedir**",
     "cabecalhos": ("Forças atuais", "Desafios do crescimento"),
     "camadas": [
         ("Proximidade com a fundadora",
          "Desenvolver lideranças com os mesmos princípios."),
         ("Liberdade para resolver",
          "Estabelecer critérios e responsabilidades claros."),
         ("Agilidade diante dos problemas",
          "Criar processos que antecipem dificuldades."),
         ("Conhecimento acumulado",
          "Transmitir e reproduzir padrões de excelência."),
         ("União entre as equipes",
          "Preservar vínculos em estruturas maiores."),
     ]},

    {"tipo": "texto", "titulo": "A **reflexão central**",
     "paragrafos": [
         "O que hoje é resolvido pela experiência de algumas pessoas "
         "precisará se transformar em conhecimento compartilhado.",
         "O que hoje depende de relações próximas precisará ser preservado "
         "mesmo com novos funcionários e lideranças.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["O maior legado da Flávia não será fazer com que",
                "tudo continue dependendo dela, mas construir",
                "uma organização capaz de preservar seus princípios",
                "sem precisar de sua presença em cada decisão."]},

    # ═════════════════════════════════ ponte · CULTURA DE MARCA
    {"tipo": "divisor", "nome": "Cultura de marca",
     "apoio": "Forma · My Home"},

    {"tipo": "texto", "titulo": "O que é **cultura de marca**?",
     "paragrafos": [
         "É o conjunto de crenças, valores e significados que orientam a "
         "identidade de uma marca e se manifesta em seu comportamento, seus "
         "produtos, sua comunicação e na experiência que entrega.",
     ]},

    {"tipo": "texto", "titulo": "Como foi **mapeada**",
     "paragrafos": [
         "Foram cruzados os relatos da Flávia, a trajetória das empresas, as "
         "entrevistas com colaboradores, os documentos de identidade verbal "
         "e as percepções de clientes e arquitetos.",
     ]},

    {"tipo": "palavras", "titulo": "O que foi **analisado**",
     "palavras": ["Origem e significado", "Valores",
                  "Personalidade e expressão", "Comportamento da equipe",
                  "Experiência entregue", "Percepção externa", "Coerência"]},

    {"tipo": "declaracao", "eyebrow": "A questão central", "marcar": True,
     "linhas": ["Compreender não apenas o que cada empresa faz,",
                "mas o significado que seu trabalho assume",
                "para as pessoas e o que a diferencia no mercado."]},

    # ═══════════════════════════════════════════════════ 02 FORMA
    {"tipo": "divisor", "numero": "02", "nome": "Forma",
     "apoio": "Cultura de marca · origem, valores e personalidade.",
     "foto": IMG["div2"],
     "imagem": "Um projeto complexo em execução — marcenaria sob medida, "
               "encaixe, peça grande em montagem."},

    {"tipo": "texto", "foto": IMG["forma"], "lado": "solta",
     "imagem": "Uma conversa técnica sobre o projeto — prancha, amostra de "
               "material, desenho na mesa.",
     "titulo": "A liberdade de criar exige a **capacidade de realizar**.",
     "paragrafos": [
         "Durante anos, Flávia aprendeu a trabalhar com marcas de móveis "
         "consolidadas. Conhecia os sistemas, os padrões e as possibilidades "
         "oferecidas por eles. Mas havia algo que a incomodava: saber que "
         "uma ideia poderia ser melhor e precisar adaptá-la aos limites de "
         "uma marca pronta. Quando assumiu a Forma, encontrou a "
         "possibilidade de construir seus próprios padrões e executar "
         "projetos com maior liberdade.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["A essência da Forma não está apenas",
                "em personalizar móveis.",
                "Está em colocar o conhecimento técnico a serviço",
                "daquilo que cada projeto realmente necessita."]},

    {"tipo": "declaracao", "eyebrow": "Crença central", "marcar": True,
     "linhas": ["Uma ideia singular merece",
                "uma execução à sua altura."]},

    {"tipo": "colunas", "titulo": "Os valores e a personalidade da **Forma**",
     "colunas": [
         ("Valores",
          "Precisão · Personalização · Responsabilidade · Confiança · "
          "Evolução técnica"),
         ("Personalidade", "Segura · Criteriosa · Determinada · Próxima"),
         ("Expressão",
          "Sofisticação que se comprova na competência, não na ostentação."),
     ]},

    # ——————————————————————————— Forma · comportamentos e experiência
    {"tipo": "divisor", "nome": "Comportamentos e experiência",
     "apoio": "Cultura de marca Forma"},

    {"tipo": "texto",
     "titulo": "O verdadeiro alto padrão é a **tranquilidade de quem "
               "confia**.",
     "paragrafos": [
         "Uma cliente relatou que atravessava o ano mais desafiador de sua "
         "vida. Ao agradecer à Forma, não destacou apenas a beleza dos "
         "móveis. Disse que o profissionalismo da equipe havia aliviado seu "
         "fardo, porque sabia que tudo estava em boas mãos.",
         "Um projeto de móveis faz parte de um momento importante, mas "
         "muitas vezes exaustivo, da vida do cliente. Esse depoimento revela "
         "algo profundamente significativo sobre o valor da marca.",
     ]},

    {"tipo": "colunas",
     "titulo": "A cultura em ação, **a experiência entregue**.",
     "colunas": [
         ("A cultura em ação",
          "Compreender necessidades. Antecipar dificuldades. Respeitar o "
          "projeto. Cuidar da casa. Assumir a responsabilidade até a "
          "entrega."),
         ("A experiência entregue",
          "Mais do que um ambiente bonito, a possibilidade de atravessar um "
          "processo complexo com segurança e confiança."),
     ],
     "fecho": "A Forma não elimina todos os imprevistos de uma obra. Mas "
              "pode ser a parte dessa experiência em que o cliente encontra "
              "cuidado, competência e tranquilidade."},

    # ——————————————————————— Forma · percepção externa e coerência
    {"tipo": "divisor", "nome": "Percepção externa e coerência",
     "apoio": "Os depoimentos dos arquitetos revelam uma relação que "
              "ultrapassa a contratação de um fornecedor."},

    {"tipo": "camadas",
     "titulo": "O valor da Forma está na **confiança que constrói**.",
     "camadas": [
         ("Júlia Matsuda", "Destaca a atenção minuciosa aos detalhes e a "
                           "presença da equipe durante a execução."),
         ("Rodrigues", "Procurava uma empresa que abraçasse a "
                       "responsabilidade de entregar aquilo que havia sido "
                       "prometido ao cliente."),
         ("Nathaly", "Valoriza a confiança de contar com uma equipe capaz de "
                     "discutir soluções técnicas e integrar diferentes "
                     "acabamentos."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["A Forma não é reconhecida somente",
                "pelo produto final, mas pela segurança que oferece",
                "a quem precisa confiar a execução de um projeto."]},

    {"tipo": "texto", "titulo": "Ponto de atenção",
     "paragrafos": [
         "A expansão industrial não pode transformar a personalização em "
         "uma promessa comercial desconectada da experiência.",
     ]},

    {"tipo": "foto_cheia", "foto": IMG["ess_forma"],
     "imagem": "Um ambiente completo entregue pela Forma. Imagem ampla, que "
               "aguente a frase por cima.",
     "linhas": ["Transformar complexidade",
                "em confiança."],
     "apoio": "Precisão que realiza. A essência cultural da Forma."},

    # ═════════════════════════════════════════════════ 03 MY HOME
    {"tipo": "divisor", "numero": "03", "nome": "My Home",
     "apoio": "Cultura de marca · origem, valores e personalidade.",
     "foto": IMG["div3"],
     "imagem": "A bancada de criação: protótipo, teste de acabamento, peça "
               "em desenvolvimento."},

    {"tipo": "texto", "foto": IMG["myhome"], "lado": "esquerda",
     "imagem": "O material antes de virar produto — a sobra, o retalho, a "
               "chapa separada. O ponto de partida.",
     "titulo": "Enxergar **possibilidades** onde outros enxergam limites.",
     "paragrafos": [
         "Na produção da Forma, materiais eram descartados porque já não "
         "tinham aplicação prevista. Para Flávia, aquilo representava uma "
         "possibilidade ainda não explorada.",
         "A decisão de guardar e transformar as sobras deu origem a produtos "
         "decorativos e a uma nova empresa. Inicialmente, foi necessário "
         "convencer a equipe de que aquela ideia poderia funcionar. Com o "
         "desenvolvimento da produção, as sobras deixaram de ser suficientes "
         "para atender à demanda.",
     ]},

    {"tipo": "declaracao", "eyebrow": "A descoberta", "marcar": True,
     "linhas": ["A My Home não nasceu apenas do reaproveitamento",
                "de materiais. Nasceu da recusa em aceitar",
                "que algo havia perdido seu valor porque",
                "seu uso original havia terminado."]},

    {"tipo": "declaracao", "eyebrow": "Crença central", "marcar": True,
     "linhas": ["Uma possibilidade ainda não explorada",
                "não significa uma possibilidade inexistente."]},

    {"tipo": "colunas",
     "titulo": "Os valores e a personalidade da **My Home**",
     "colunas": [
         ("Valores",
          "Inventividade · Transformação · Originalidade · Qualidade · "
          "Acessibilidade · Evolução"),
         ("Personalidade", "Criativa · Curiosa · Expressiva · Vibrante"),
         ("Expressão",
          "O prazer de descobrir novas possibilidades para materiais, "
          "objetos e ambientes."),
     ]},

    # ————————————————————————— My Home · comportamentos e experiência
    {"tipo": "divisor", "nome": "Comportamentos e experiência",
     "apoio": "Cultura de marca My Home"},

    {"tipo": "camadas",
     "titulo": "Criatividade não é improvisação. É **transformação com "
               "conhecimento**.",
     "camadas": [
         ("Na My Home", "Uma ideia precisa passar pelas mãos e pelo "
                        "conhecimento de quem sabe transformá-la em algo "
                        "concreto."),
         ("Letícia", "Até o desenho de uma borboleta previsto em um projeto "
                     "pode se tornar um molde enviado para a produção."),
         ("Weudes", "Processos que exigem concentração, trabalhos manuais "
                    "minuciosos e acabamentos que não admitem soluções pela "
                    "metade."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["A criatividade da My Home também depende",
                "de precisão, técnica e habilidade de execução."],
     "apoio": "Uma característica pouco evidente para quem observa somente o "
              "produto pronto."},

    {"tipo": "colunas",
     "titulo": "A cultura em ação, **a experiência pretendida**.",
     "colunas": [
         ("A cultura em ação",
          "Experimentar. Encontrar novos usos. Dominar materiais. "
          "Transformar ideias em produtos. Aperfeiçoar cada detalhe."),
         ("A experiência pretendida",
          "Surpreender com produtos criativos que acrescentem "
          "personalidade, originalidade e novas possibilidades aos "
          "ambientes."),
     ],
     "fecho": "A My Home pode transformar aquilo que parecia comum em algo "
              "que desperta um novo olhar."},

    # ————————————————————— My Home · percepção externa e coerência
    {"tipo": "divisor", "nome": "Percepção externa e coerência",
     "apoio": "Cultura de marca My Home"},

    {"tipo": "texto",
     "titulo": "Uma marca que aprendeu a criar para outros. Agora precisa "
               "ser **reconhecida pelo que cria**.",
     "paragrafos": [
         "A My Home já possui uma competência produtiva reconhecida. "
         "Arquitetos valorizam sua capacidade de executar detalhes que "
         "ampliam as possibilidades dos projetos da Forma.",
         "Entretanto, as entrevistas revelam uma questão importante sobre "
         "sua identidade: Júlio César descreve a My Home como o braço "
         "direito da Forma.",
     ]},

    {"tipo": "foto_cheia", "foto": IMG["producao"],
     "imagem": "A produção da My Home em plano aberto — a bancada, as peças "
               "em série, o trabalho acontecendo.",
     "linhas": ["“A My Home [...]",
                "monta o palco",
                "pra Forma dançar.”"],
     "apoio": "Pâmella. A fala não diminui a importância da marca: mostra o "
              "quanto sua contribuição permanece associada à outra."},

    {"tipo": "texto", "titulo": "O desafio",
     "paragrafos": [
         "Preservar a capacidade de apoiar a Forma, mas conquistar "
         "reconhecimento independente por seus próprios produtos, sua "
         "criatividade e sua experiência de compra.",
         "A confiança no e-commerce também precisará ser fortalecida.",
     ]},

    {"tipo": "foto_cheia", "foto": IMG["ess_myhome"],
     "imagem": "Um produto My Home em destaque no ambiente. Imagem ampla, "
               "que aguente a frase por cima.",
     "linhas": ["Transformar possibilidades",
                "em criação."],
     "apoio": "Criatividade que transforma. A essência cultural da My Home."},

    # ═══════════════════════════════════════════════════ 04 SÍNTESE
    {"tipo": "divisor", "numero": "04", "nome": "Síntese",
     "apoio": "O que compartilham e o que torna cada marca singular.",
     "foto": IMG["div4"],
     "imagem": "O time completo das duas operações, ou o ambiente de "
               "trabalho cheio de gente. Plano aberto."},

    {"tipo": "texto", "titulo": "Uma origem. **Duas formas de transformar**.",
     "paragrafos": [
         "A trajetória de Flávia revela uma constante: recusar que as "
         "circunstâncias determinem todas as possibilidades do futuro.",
         "Essa mentalidade contribuiu para construir uma cultura "
         "organizacional marcada pela iniciativa, pela proximidade humana e "
         "pela responsabilidade com o resultado. Mas encontrou expressões "
         "distintas em cada marca.",
     ]},

    {"tipo": "camadas",
     "titulo": "Uma cultura compartilhada. **Duas expressões**.",
     "camadas": [
         ("Cultura organizacional",
          "Liberdade para encontrar caminhos. Responsabilidade pelo "
          "resultado coletivo."),
         ("Forma",
          "O conhecimento e a liberdade técnica transformam projetos "
          "complexos em confiança."),
         ("My Home",
          "A inventividade e a capacidade de execução transformam "
          "possibilidades em novas criações."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["O que conecta as duas marcas não é apenas",
                "a história de quem as construiu.",
                "É a convicção de que sempre existe algo mais",
                "que pode ser feito, criado ou transformado."]},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
