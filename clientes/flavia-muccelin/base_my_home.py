# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — MY HOME | CASA CRIATIVA

Mesmo formato das outras: o padrão medido em `padrao-ka/PADRAO-KELLY.md` —
corpo 25, título 42 em dois pesos, filete `#A5A49F`, acento `#CC754E`,
entrelinha exata, sem rodapé.

**Um título e um bloco de texto por página.** Os 17 slides do roteiro saem em
45 páginas porque quase todos carregavam três, quatro, cinco blocos (causa +
liderança + tribo; público + persona + oportunidade + desejo; seis pilares +
a síntese). Onde o conteúdo é de campos, ele vira **colunas** ou **camadas**:
rótulo e texto lado a lado, nunca empilhados.

**Sem viradas de seção.** São catorze seções: numerar cada uma com a virada de
143,5pt dobraria o documento e transformaria a leitura numa sequência de
capas. O sumário em duas colunas dá conta da estrutura, como na Base
Estratégica do Lucas — a referência viva desse tipo de entrega.

A voz é de terceira pessoa, como manda o CLAUDE.md. O **manifesto** é a
exceção prevista: é o gênero em que a marca fala. Aqui ele nem precisa da
exceção — o texto da Kelly já está em terceira pessoa.

**As fotografias ainda não existem.** Cinco páginas trazem a MARCAÇÃO: a área
exata, identificada, com o briefing. Quando o arquivo entrar em `assets/` com
o nome declarado em `foto`, a marcação some e nada muda de lugar.

    python3 clientes/flavia-muccelin/gerar.py base_my_home
"""

MARCA = "My Home | Casa Criativa"
DOCUMENTO = "Base Estratégica da Marca"
RODAPE = False
ARQUIVO = "Base-Estrategica-da-Marca-My-Home"

IMG = {
    "essencia": "myhome-sobras-materiais.png",
    "quem": "myhome-producao-bancada.png",
    "principio": "myhome-material-guardado.png",
    "produto": "myhome-produto-ambiente.png",
    "assinatura": "myhome-colecao-ambiente.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    # ——————————————————————————————————————————————————————— CAPA
    {"tipo": "capa",
     "titulo": ["BASE ESTRATÉGICA", "DA MARCA"],
     "subtitulo": ["My Home", "Casa Criativa"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["Uma marca que nasceu de um novo olhar",
                "sobre o que parecia não ter mais valor."]},

    # ———————————————————————————————————————————————————— SUMÁRIO
    {"tipo": "sumario", "titulo": "O caminho", "grade": 2, "itens": [
        ("01", "Essência da marca"),
        ("02", "Quem é a My Home"),
        ("03", "Causa, liderança e tribo"),
        ("04", "Princípio central"),
        ("05", "Público-alvo e persona"),
        ("06", "Personalidade da marca"),
        ("07", "Pilares da marca"),
        ("08", "DNA da marca"),
        ("09", "Voz da marca"),
        ("10", "Tom de voz"),
        ("11", "Posicionamento"),
        ("12", "Golden Circle"),
        ("13", "Arquitetura da marca"),
        ("14", "Manifesto"),
    ]},

    # ———————————————————————————————————————— 01 ESSÊNCIA DA MARCA
    {"tipo": "texto", "foto": IMG["essencia"], "lado": "direita",
     "imagem": "O material antes de virar produto — a sobra, o retalho, a "
               "chapa guardada. O ponto de partida.",
     "titulo": "Enxergar **possibilidades** onde outros enxergam limites.",
     "paragrafos": [
         "A My Home nasceu de um olhar inconformado com o desperdício, "
         "capaz de perceber potencial em materiais que já tinham um destino "
         "definido. Mas sua essência vai além do reaproveitamento: está na "
         "capacidade de imaginar novos usos, combinar elementos e "
         "transformar ideias em produtos que acrescentam personalidade à "
         "casa.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["O que a torna especial não é apenas",
                "aquilo que transforma.",
                "É a maneira como enxerga",
                "o que ainda pode ser criado."],
     "apoio": "A essência da marca."},

    # ————————————————————————————————————————— 02 QUEM É A MY HOME
    {"tipo": "texto", "foto": IMG["quem"], "lado": "solta",
     "imagem": "A bancada de produção da My Home: a máquina, a peça em "
               "desenvolvimento, o trabalho acontecendo.",
     "titulo": "Quem é a **My Home**",
     "paragrafos": [
         "Uma marca brasileira de decoração criativa que desenvolve e "
         "fabrica peças decorativas e funcionais para transformar ambientes "
         "com originalidade e personalidade.",
         "Fundada por Flávia Pereira Muccelin, nasceu do aproveitamento de "
         "materiais excedentes da produção moveleira. A ideia evoluiu, "
         "incorporando máquinas, conhecimentos e novas possibilidades de "
         "fabricação.",
     ]},

    {"tipo": "texto", "titulo": "Inventividade, domínio técnico e **cuidado "
                                "com os detalhes**",
     "paragrafos": [
         "Hoje a My Home reúne essas três coisas, com a ambição de alcançar "
         "consumidores em todo o Brasil por meio do comércio eletrônico.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["Uma marca que nasceu da capacidade de reaproveitar",
                "e cresceu pela capacidade de criar."]},

    # —————————————————————————————————— 03 CAUSA, LIDERANÇA E TRIBO
    {"tipo": "colunas", "titulo": "**Causa**, liderança e tribo",
     "colunas": [
         ("Causa",
          "Mostrar que sempre existem novas possibilidades de transformar "
          "materiais, objetos e ambientes. Valorizar o aproveitamento "
          "inteligente de recursos e tornar a criatividade mais presente na "
          "vida cotidiana."),
         ("Liderança",
          "Incentivar as pessoas a olhar para os detalhes da casa de "
          "maneira diferente, descobrindo que pequenas mudanças podem "
          "produzir novas experiências."),
         ("Tribo",
          "Pessoas que gostam de descobrir, criar, combinar e personalizar. "
          "Que não procuram apenas objetos funcionais, mas escolhas capazes "
          "de expressar seu jeito de viver."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["O vínculo com a marca nasce do desejo",
                "de fazer da casa uma expressão pessoal."]},

    # ———————————————————————————————————————— 04 PRINCÍPIO CENTRAL
    {"tipo": "texto", "foto": IMG["principio"], "lado": "esquerda",
     "imagem": "O estoque de sobras: as chapas empilhadas, guardadas à "
               "espera de um destino.",
     "titulo": "O que parece ter chegado ao fim pode ser **o começo de outra "
               "coisa**.",
     "paragrafos": [
         "Durante aproximadamente um ano, Flávia guardou sobras de MDF e "
         "outros materiais sem ainda ter uma solução definitiva para eles. "
         "Enquanto ocupavam espaço, uma ideia permanecia viva: encontrar uma "
         "maneira de transformá-los. "
         "O que parecia improvável tornou-se produto, e aquilo que antes era "
         "descartado passou a gerar novas oportunidades. Com o crescimento "
         "da produção, as sobras já não eram suficientes para atender à "
         "demanda.",
     ]},

    {"tipo": "camadas", "titulo": "A grande descoberta sobre a **My Home**",
     "camadas": [
         ("O reaproveitamento", "Explica como a marca começou."),
         ("O olhar", "Explica por que ela pode continuar crescendo."),
     ]},

    # —————————————————————————————————————— 05 PÚBLICO-ALVO E PERSONA
    {"tipo": "colunas", "titulo": "Público-alvo e **persona**",
     "colunas": [
         ("Público-alvo prioritário",
          "Consumidores que valorizam decoração, funcionalidade e "
          "originalidade, gostam de comprar pela internet e procuram "
          "produtos capazes de transformar ambientes sem necessariamente "
          "realizar grandes mudanças."),
         ("Persona central",
          "Uma pessoa que deseja uma casa com mais personalidade. Gosta de "
          "descobrir objetos diferentes, valoriza detalhes bem pensados e "
          "procura produtos que combinem estética, utilidade e preço "
          "acessível."),
     ],
     "fecho": "Não deseja apenas acompanhar tendências: quer fazer escolhas "
              "que tenham relação com seu próprio gosto."},

    {"tipo": "texto", "foto": IMG["produto"], "lado": "solta",
     "imagem": "Uma peça do catálogo atual no ambiente — de preferência um "
               "acessório ou uma peça infantil.",
     "titulo": "A oportunidade comercial **identificada**",
     "paragrafos": [
         "O catálogo atual apresenta uma presença relevante de acessórios e "
         "peças infantis. Esse universo pode se tornar uma linha estratégica "
         "importante, sem limitar a identidade da My Home exclusivamente à "
         "decoração infantil.",
     ]},

    {"tipo": "declaracao", "eyebrow": "O desejo central", "marcar": True,
     "linhas": ["Transformar a casa por meio de escolhas",
                "que façam os ambientes parecer mais pessoais,",
                "acolhedores e criativos."]},

    # ————————————————————————————————————— 06 PERSONALIDADE DA MARCA
    {"tipo": "camadas", "titulo": "Personalidade da marca",
     "camadas": [
         ("Inventiva", "Enxerga outras possibilidades para aquilo que parece "
                       "comum."),
         ("Curiosa", "Experimenta formas, materiais, combinações e "
                     "aplicações."),
         ("Vibrante", "Transmite entusiasmo e prazer em criar."),
         ("Cuidadosa", "Valoriza o capricho, a funcionalidade e a "
                       "qualidade."),
         ("Próxima", "Fala com simplicidade, acolhimento e espontaneidade."),
         ("Visionária", "Não limita suas possibilidades ao que já foi "
                        "desenvolvido."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Criatividade com conhecimento.",
                "Leveza com responsabilidade."],
     "apoio": "A My Home deve transmitir a energia de quem gosta de imaginar, "
              "mas também a segurança de quem sabe transformar uma ideia em "
              "produto."},

    # ——————————————————————————————————————————— 07 PILARES DA MARCA
    {"tipo": "camadas", "titulo": "Os pilares da **criação**",
     "camadas": [
         ("01 · Inventividade",
          "A capacidade de encontrar caminhos, combinações e soluções fora "
          "do habitual."),
         ("02 · Ressignificação",
          "Reconhecer possibilidades de transformação em materiais, formas e "
          "objetos, valorizando o aproveitamento inteligente de recursos."),
         ("03 · Originalidade",
          "Desenvolver produtos com personalidade, capazes de despertar "
          "curiosidade e interesse."),
     ]},

    {"tipo": "camadas", "titulo": "Os pilares da **entrega**",
     "camadas": [
         ("04 · Qualidade com cuidado",
          "Unir criatividade, conhecimento produtivo, funcionalidade e "
          "atenção ao acabamento."),
         ("05 · Acessibilidade",
          "Buscar soluções criativas que possam fazer parte do cotidiano de "
          "diferentes consumidores, com uma relação coerente entre design, "
          "qualidade e preço."),
         ("06 · Evolução contínua",
          "Experimentar, aprender e ampliar o repertório de produtos, "
          "materiais e possibilidades de criação."),
     ]},

    {"tipo": "declaracao", "eyebrow": "O que une os pilares", "marcar": True,
     "linhas": ["A criatividade precisa produzir algo",
                "que faça sentido, funcione bem",
                "e gere valor para quem recebe."]},

    # ———————————————————————————————————————————————— 08 DNA DA MARCA
    {"tipo": "palavras", "titulo": "O DNA da **My Home**",
     "palavras": ["Inventividade", "Transformação", "Originalidade",
                  "Cuidado", "Personalidade"]},

    {"tipo": "camadas", "titulo": "Como esses atributos viram **linguagem**",
     "camadas": [
         ("No produto",
          "Formas criativas, funcionalidade, detalhes bem resolvidos e "
          "acabamento cuidadoso."),
         ("Na identidade visual",
          "Peças, recortes, encaixes e formas geométricas que ganham um novo "
          "significado quando combinados."),
         ("Nas cores e materiais",
          "Uma linguagem acolhedora e expressiva, com tons terrosos, "
          "mostarda, verdes e referências às texturas dos materiais."),
         ("Na experiência",
          "O cuidado percebido desde a apresentação do produto até a "
          "embalagem, a entrega e o pós-venda."),
     ]},

    {"tipo": "texto", "titulo": "O monograma **MH**",
     "paragrafos": [
         "A construção de um monograma MH por módulos é um caminho promissor "
         "para expressar visualmente essa ideia de transformação.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["A criatividade não está somente nos objetos.",
                "Está no jeito como a marca pensa e faz."]},

    # ————————————————————————————————————————————— 09 VOZ DA MARCA
    {"tipo": "palavras", "titulo": "A voz da **My Home**",
     "palavras": ["Criativa", "Leve", "Inspiradora", "Afetiva", "Autêntica"]},

    {"tipo": "texto", "titulo": "Comunicar com entusiasmo, **sem exageros**",
     "paragrafos": [
         "A voz da My Home deve despertar curiosidade e aproximar as pessoas "
         "das possibilidades de transformar seus ambientes: valorizar a "
         "história por trás das criações, mostrar o processo produtivo e "
         "ajudar o consumidor a imaginar como um detalhe pode mudar seu "
         "ambiente.",
         "Ela não deve apenas anunciar produtos. Deve despertar novas "
         "maneiras de olhar para a casa.",
     ]},

    {"tipo": "declaracao", "eyebrow": "Exemplo de expressão", "marcar": True,
     "linhas": ["Um detalhe pode mudar a forma",
                "como um ambiente é percebido.",
                "Uma nova combinação pode transformar",
                "aquilo que parecia comum.",
                "E uma ideia pode encontrar",
                "seu lugar na casa de alguém."]},

    # ——————————————————————————————————————————————— 10 TOM DE VOZ
    {"tipo": "camadas", "titulo": "Tom de voz",
     "camadas": [
         ("Criativo", "Sem ser confuso."),
         ("Vibrante", "Sem ser infantil."),
         ("Afetivo", "Sem exagerar no sentimentalismo."),
         ("Próximo", "Sem perder a credibilidade."),
         ("Inspirador", "Sem fazer promessas vazias."),
         ("Confiável", "Com informações claras sobre materiais, compra e "
                       "entrega."),
     ]},

    {"tipo": "texto", "titulo": "A diretriz de **linguagem**",
     "paragrafos": [
         "Priorizar palavras que expressem possibilidades, criação, "
         "detalhes, descobertas, combinações, personalidade e transformação.",
         "Evitar comunicar a marca exclusivamente como sustentável, "
         "artesanal ou feita de resíduos, quando essas características não "
         "forem comprováveis em todos os produtos.",
     ]},

    # ————————————————————————————————————————————— 11 POSICIONAMENTO
    {"tipo": "texto", "titulo": "Posicionamento",
     "paragrafos": [
         "A My Home é uma marca brasileira de decoração criativa para "
         "pessoas que desejam transformar seus ambientes com produtos "
         "originais, funcionais e acessíveis.",
         "Com produção própria, conhecimento técnico e um olhar inventivo "
         "sobre materiais e formas, desenvolve peças que acrescentam "
         "personalidade à casa e tornam pequenas transformações possíveis.",
     ]},

    {"tipo": "texto", "titulo": "O território de **diferenciação**",
     "paragrafos": [
         "Enquanto grandes varejistas competem pela variedade e curadoria, e "
         "marketplaces oferecem inúmeras opções comparáveis por preço, a My "
         "Home busca construir reconhecimento pela combinação de olhar "
         "criativo, capacidade de fabricação e personalidade nos detalhes.",
         "A proposta não é competir pelo maior catálogo ou pelo menor preço. "
         "É desenvolver produtos que façam o consumidor reconhecer um jeito "
         "próprio de criar.",
     ]},

    {"tipo": "declaracao", "eyebrow": "Posicionamento central", "marcar": True,
     "linhas": ["Pequenos detalhes podem revelar",
                "grandes possibilidades."]},

    {"tipo": "foto_cheia", "foto": IMG["assinatura"],
     "imagem": "Um ambiente com várias peças My Home em uso. Imagem ampla, "
               "que aguente a frase por cima.",
     "linhas": ["Um novo olhar",
                "para cada detalhe."],
     "apoio": "Assinatura de marca proposta."},

    # ————————————————————————————————————————————— 12 GOLDEN CIRCLE
    {"tipo": "colunas", "titulo": "Golden Circle",
     "colunas": [
         ("Por quê · propósito",
          "Porque uma casa pode ganhar novas possibilidades e expressar mais "
          "personalidade por meio da criatividade e dos detalhes."),
         ("Como · diferencial",
          "Com inventividade, experimentação, aproveitamento inteligente de "
          "materiais quando aplicável, produção própria e cuidado no "
          "desenvolvimento e acabamento."),
         ("O quê · oferta",
          "Produtos decorativos e funcionais, acessórios, pequenos móveis e "
          "novas criações para a casa, comercializados principalmente pelo "
          "e-commerce."),
     ]},

    {"tipo": "declaracao", "eyebrow": "A lógica da marca", "marcar": True,
     "linhas": ["Um novo olhar revela possibilidades.",
                "O conhecimento transforma essas possibilidades",
                "em produtos. E os produtos levam novas",
                "expressões para dentro de casa."]},

    # —————————————————————————————————————— 13 ARQUITETURA DA MARCA
    {"tipo": "camadas", "titulo": "Arquitetura da marca",
     "camadas": [
         ("Marca principal", "My Home | Casa Criativa."),
         ("Atuação comercial",
          "Marca própria de produtos decorativos e funcionais, com foco na "
          "venda direta ao consumidor e expansão digital."),
         ("Linhas de produtos",
          "Decoração, organização, acessórios, pequenos móveis e coleções "
          "temáticas. O universo infantil é uma oportunidade de "
          "desenvolvimento comercial, sem definir sozinho toda a marca."),
         ("Competência produtiva",
          "Usinagem, transformação de materiais, pintura, acabamentos e "
          "desenvolvimento de soluções técnicas."),
     ]},

    {"tipo": "texto", "titulo": "A relação com **a Forma**",
     "paragrafos": [
         "A My Home compartilha parte de sua origem, cultura organizacional "
         "e competências produtivas com a Forma, podendo atuar como "
         "fornecedora especializada.",
         "Entretanto, possui proposta comercial, público, identidade e "
         "experiência de marca próprios.",
     ]},

    {"tipo": "texto", "titulo": "A direção **estratégica**",
     "paragrafos": [
         "Construir o reconhecimento da My Home como marca independente de "
         "produtos criativos, e não como uma extensão comercial da Forma.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["O que conecta as empresas pode fortalecer a operação.",
                "O que diferencia a My Home deve fortalecer",
                "sua presença no mercado."]},

    # ——————————————————————————————————————————————— 14 MANIFESTO
    {"tipo": "manifesto", "titulo": "Manifesto",
     "paragrafos": [
         "Tudo começou com aquilo que já não parecia ter destino. Pedaços de "
         "madeira. Recortes. Sobras de materiais que haviam cumprido sua "
         "função e seriam descartados.",
         "Para muitos, o fim de um processo. Para alguém que enxergava "
         "diferente, o começo de uma possibilidade.",
         "Durante algum tempo, esses materiais foram guardados enquanto uma "
         "ideia tomava forma. Foi preciso imaginar, experimentar, aprender e "
         "fazer outras pessoas acreditarem que dali poderia nascer algo "
         "novo. E nasceu.",
         "O que antes era sobra transformou-se em produto. O que parecia sem "
         "utilidade encontrou uma nova função. E a criatividade que começou "
         "no reaproveitamento passou a descobrir caminhos muito maiores.",
     ],
     "assinatura": "MY HOME  |  CASA CRIATIVA"},

    {"tipo": "manifesto", "titulo": "Manifesto",
     "paragrafos": [
         "Porque a My Home nunca foi apenas sobre transformar materiais. É "
         "sobre transformar o olhar.",
         "Enxergar possibilidades no que parece comum. Descobrir novas "
         "formas para aquilo que já existe. Criar produtos que acrescentem "
         "beleza, função e personalidade aos espaços.",
         "Uma casa não precisa ser igual a nenhuma outra. Ela pode ganhar "
         "identidade aos poucos, nas escolhas, nas combinações e nos "
         "detalhes que fazem sentido para quem vive nela.",
         "E é nesses detalhes que novas possibilidades encontram seu lugar.",
     ],
     "assinatura": "UM NOVO OLHAR PARA CADA DETALHE"},

    # ————————————————————————————————————————————— 15 ENCERRAMENTO
    {"tipo": "camadas", "titulo": "A síntese da **marca**",
     "camadas": [
         ("Essência", "Enxergar possibilidades onde outros enxergam "
                      "limites."),
         ("Competência", "Transformar ideias e materiais com criatividade e "
                         "conhecimento."),
         ("Proposta de valor", "Levar originalidade e personalidade para os "
                               "detalhes da casa."),
         ("Posicionamento", "Um novo olhar para cada detalhe."),
     ]},

    {"tipo": "declaracao",
     "linhas": ["Onde possibilidades ganham forma."],
     "apoio": "My Home · Casa Criativa"},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
