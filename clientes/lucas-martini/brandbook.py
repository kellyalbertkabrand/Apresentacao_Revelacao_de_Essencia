# -*- coding: utf-8 -*-
"""
BRAND BOOK — Lucas Martini | Proteção & Sucessão

A mesma Base Estratégica, em formato de manual: 26 páginas na diagramação do
Brand Book KA 2026 (cabeçalho com paginação, capítulos numerados, título à
esquerda e conteúdo à direita), vestida com a identidade visual do Lucas —
verde profundo, dourado e o escudo LM.

Só conteúdo. A diagramação está em padrao-ka/ka_brandbook.py.

Nada aqui foi inventado: cada definição vem da Base Estratégica aprovada
(clientes/lucas-martini/base_estrategica.py). As duas exceções, marcadas no
README, são a página de vocabulário e a de usos da marca — derivadas dos
territórios e da personalidade já definidos, porque todo brand book precisa
delas e a Base não as trazia escritas.
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
MARCA_DIR = os.path.join(AQUI, "assets", "marca")

MARCA = "Lucas Martini"
DOCUMENTO = "Brand Book"
ARQUIVO = "Brand-Book-Lucas-Martini"

# ------------------------------------------------------------------ paleta
# Medida na identidade visual do Lucas: o verde do fundo, o dourado do
# escudo, o cinza do monograma e a areia das aplicações claras.
PALETA = {
    "escuro": "4A534E",         # verde profundo — a cor da marca
    "escuro2": "5A635E",        # o mesmo verde, um tom acima, para volume
    "claro": "F6F4EF",          # papel
    "areia": "CEC3B5",          # areia das aplicações claras
    "tinta": "2C322E",          # títulos
    "corpo": "5F6661",          # corpo de texto
    "suave": "9AA09A",          # legenda e rótulo apagado
    "fio": "DCD8CE",            # filetes
    "acento": "AE8C4E",         # dourado sobre papel
    "acento_escuro": "E3C88B",  # dourado sobre o verde
    "sobre_escuro": "F2F0E9",   # texto sobre o verde
    "corpo_escuro": "C8CCC6",   # corpo sobre o verde
}

LOGOS = {
    "capa": os.path.join(MARCA_DIR, "lm-vertical-dourado-escuro.png"),
    "escuro": os.path.join(MARCA_DIR, "lm-vertical-dourado-escuro.png"),
    "claro": os.path.join(MARCA_DIR, "lm-vertical-preto.png"),
    "escudo": os.path.join(MARCA_DIR, "lm-escudo-dourado.png"),
}

V_DOURADO = os.path.join(MARCA_DIR, "lm-horizontal-dourado.png")
V_PRETO = os.path.join(MARCA_DIR, "lm-horizontal-preto.png")
V_VERTICAL_PRETO = os.path.join(MARCA_DIR, "lm-vertical-preto.png")
V_CLARO = os.path.join(MARCA_DIR, "lm-vertical-claro.png")

PAGINAS = [
    # 01 — capa
    {"tipo": "capa", "titulo": "Brand Book", "edicao": "Edição 2026",
     "logo_largura": 7.6, "logo_y": 3.05, "y_titulo": 6.75},

    # 02 — para que serve
    {"tipo": "texto", "olho": "Antes de começar",
     "titulo": ["Para que serve", "este brand book"],
     "paragrafos": [
         "Este documento reúne, em um só lugar, a **essência, a voz, o "
         "posicionamento e a identidade visual** da marca Lucas Martini | "
         "Proteção & Sucessão.",
         "Ele existe para garantir a **unidade da marca**: todo ponto de "
         "contato com a mesma consistência visual e verbal, não importa quem "
         "produza.",
         "Use como guia antes de criar, aprovar ou contratar qualquer "
         "material. **Marca consistente é marca reconhecida.**",
     ]},

    # 03 — índice
    {"tipo": "indice", "titulo": "Conteúdo", "passo": 1.30, "y": 3.95,
     "itens": [
         ("01", "A marca", "O que ela é, no que acredita e onde se coloca."),
         ("02", "Público e território",
          "Para quem ela fala e sobre o que ela fala."),
         ("03", "Voz", "Como ela se comporta e como ela escreve."),
         ("04", "Identidade visual",
          "O logo, as cores e a tipografia — e o que preserva tudo isso."),
         ("05", "Manifesto", "A marca em palavras, e a marca em uma página."),
     ]},

    # ——————————————————————————————————————————— 01 A MARCA
    {"tipo": "divisor", "numero": "01", "nome": "A marca",
     "legenda": "O que levou anos para ser construído tem um nome."},

    # 05 — o que esta marca é
    {"tipo": "texto", "olho": "Definição central",
     "titulo": ["O que esta", "marca é"],
     "resumo": ["Lucas não começa pelo produto. Começa pela realidade de quem "
                "está na frente dele."],
     "marcado": ["A proteção é consequência", "do diagnóstico."],
     "paragrafos": [
         "**Lucas Martini estrutura proteção e sucessão para preservar "
         "possibilidades quando a vida, a família ou a empresa entram em "
         "transição.**",
         "Produto: seguro e soluções de proteção. Serviço: planejamento. "
         "Valor estratégico: continuidade. Valor humano: capacidade de "
         "escolha.",
         "A marca já existia antes da comunicação: experiência, resultado, "
         "recomendação, confiança e histórico de atendimento. Primeiro veio a "
         "reputação. **Agora a marca precisa torná-la visível.**",
     ]},

    # 06 — a crença fundadora
    {"tipo": "declaracao", "tom": "escuro", "olho": "A crença fundadora",
     "y": 4.55, "tam": 50,
     "linhas": ["O que levou anos para ser construído",
                "**não deveria ficar entregue ao acaso.**"],
     "apoio": ["Não porque todos os riscos possam ser eliminados, mas porque "
               "muitos dos seus impactos podem ser preparados.",
               "Nem tudo pode ser previsto. Mas muito pode ser preparado."]},

    # 07 — essência, razão de ser, causa
    {"tipo": "colunas", "olho": "O núcleo", "titulo": "Essência da marca",
     "y": 4.45,
     "colunas": [
         ("Essência", "Construir segurança",
          "Preservar liberdade de escolha. É o princípio que conecta a "
          "história, o método e a entrega."),
         ("Razão de ser", "Preservar a escolha",
          "Manter a capacidade de decidir quando a vida tira a "
          "previsibilidade de alguém."),
         ("Causa", "Preparar antes",
          "Ampliar a cultura da preparação antes da urgência. De resolver "
          "depois para pensar antes."),
     ],
     "fecho": "O que a marca combate não é a morte nem a incerteza: é o "
              "improviso, o adiamento, a falta de liquidez e a decisão tomada "
              "sob pressão."},

    # 08 — golden circle
    {"tipo": "colunas", "olho": "Golden Circle",
     "titulo": "Por quê, como e o quê", "y": 4.45,
     "colunas": [
         ("01", "Por quê",
          "Porque o que levou anos para ser construído não deveria perder "
          "sua continuidade por falta de preparação."),
         ("02", "Como",
          "Entendendo a realidade do cliente, identificando "
          "vulnerabilidades, projetando impactos e estruturando proteção de "
          "forma personalizada, com acompanhamento de longo prazo."),
         ("03", "O quê",
          "Proteção de renda, familiar e empresarial. Pessoa-chave. "
          "Planejamento sucessório. Liquidez para sucessão e inventário."),
     ],
     "fecho": "Não começar pelo produto. **Começar pela consequência.**"},

    # 09 — posicionamento
    {"tipo": "texto", "olho": "Posicionamento",
     "titulo": "Posicionamento",
     "resumo": ["O produto não diferencia. A diferenciação está na "
                "combinação de diagnóstico, personalização, conhecimento "
                "técnico, confiança, pós-venda e relação de longo prazo."],
     "marcado": ["Preparar antes para", "preservar escolhas depois."],
     "paragrafos": [
         "**Lucas Martini é especialista em proteção e sucessão para pessoas, "
         "famílias e empresas que desejam preservar o que construíram e "
         "manter possibilidades diante do imprevisto.**",
         "A promessa: estruturar proteção e sucessão de forma personalizada "
         "para que famílias, profissionais e empresas mantenham recursos, "
         "possibilidades e continuidade diante de imprevistos.",
         "A melhor proteção não é a maior. **É a que faz sentido para aquela "
         "realidade.**",
     ]},

    # 10 — arquitetura
    {"tipo": "colunas", "olho": "Arquitetura de marca",
     "titulo": "O nome no centro", "y": 4.60,
     "colunas": [
         ("Frente 01", "Proteção pessoal e familiar",
          "Renda, família e pilares financeiros."),
         ("Frente 02", "Proteção empresarial",
          "Pessoa-chave e continuidade do negócio."),
         ("Frente 03", "Sucessão familiar",
          "Transferência, liquidez e inventário."),
         ("Frente 04", "Sucessão empresarial",
          "Passagem de responsabilidade e sociedade."),
     ],
     "fecho": "A confiança está associada à pessoa: a indicação chega pelo "
              "nome e o relacionamento acontece com Lucas. **A seguradora "
              "entrega o instrumento. Lucas constrói a estratégia.**"},

    # ——————————————————————————————— 02 PÚBLICO E TERRITÓRIO
    {"tipo": "divisor", "numero": "02", "nome": ["Público", "e território"],
     "legenda": "Para quem a marca fala, e sobre o que ela fala."},

    # 12 — quem carrega responsabilidade
    {"tipo": "lista", "olho": "Público",
     "titulo": ["Quem carrega", "responsabilidade"],
     "resumo": ["Quatro perfis diferentes com uma coisa em comum: existe algo "
                "ou alguém que depende das decisões de cada um."],
     "rotulo": "A tribo", "y_direita": 2.30,
     "itens": [
         "**Quem produz a própria renda** — profissionais liberais, "
         "autônomos, executivos e especialistas;",
         "**Quem sustenta outras pessoas** — pilares financeiros da família, "
         "cuja ausência alteraria a estrutura econômica de casa;",
         "**Quem responde por uma empresa** — empresários, sócios e "
         "pessoas-chave de negócios dependentes de indivíduos específicos;",
         "**Quem construiu patrimônio** — famílias e sócios que precisam "
         "organizar transferência, liquidez e sucessão.",
     ],
     "fecho": "São pessoas que decidem com responsabilidade sobre outros. "
              "**Falar com elas é falar de consequência, nunca de medo.**"},

    # 13 — territórios de comunicação
    {"tipo": "lista", "olho": "Territórios de comunicação",
     "titulo": ["Continuidade", "é o território"],
     "resumo": ["Todo conteúdo da marca nasce de um destes cinco territórios. "
                "Fora deles, a marca está falando de outra coisa."],
     "rotulo": "Do que a marca fala", "y_direita": 2.30,
     "itens": [
         "**Continuidade** — o que precisa seguir existindo: renda, família, "
         "empresa, patrimônio, projetos e legado;",
         "**Proteção** — os recursos e estruturas que sustentam essa "
         "continuidade;",
         "**Sucessão** — a preparação para a passagem de responsabilidade e "
         "patrimônio;",
         "**Dignidade financeira** — a preservação de alternativas em "
         "momentos difíceis;",
         "**Escolha e responsabilidade** — decidir sem ser dominado pela "
         "urgência.",
     ]},

    # 14 — os cinco pilares
    {"tipo": "numerais", "olho": "Como a marca atua",
     "titulo": "Os cinco pilares", "y": 4.75,
     "itens": [
         ("Antecipação", "Decisões são melhores sem urgência."),
         ("Personalização", "Não existe proteção ideal fora de contexto."),
         ("Confiança", "Transparência e consistência ao longo dos anos."),
         ("Continuidade", "A proteção não termina na contratação."),
         ("Excelência", "Menos discurso, mais padrão de execução."),
     ]},

    # ——————————————————————————————————————————————— 03 VOZ
    {"tipo": "divisor", "numero": "03", "nome": "Voz",
     "legenda": "Autoridade discreta: provar, não proclamar."},

    # 16 — personalidade
    {"tipo": "colunas", "olho": "Personalidade",
     "titulo": "Autoridade discreta", "y": 4.45,
     "colunas": [
         ("Postura", "Seguro e preparado",
          "Transmite domínio sem precisar provar o tempo todo. Estuda antes "
          "de orientar."),
         ("Relação", "Consultivo e humano",
          "Pergunta antes de oferecer e entende o que existe por trás dos "
          "números."),
         ("Forma", "Elegante e acessível",
          "Sofisticação sem ostentação. Torna o complexo compreensível."),
     ],
     "fecho": "**Nunca:** alarmista, exibicionista, técnica demais, comercial "
              "demais ou genérica."},

    # 17 — tom de voz
    {"tipo": "pares", "olho": "Tom de voz",
     "titulo": ["Provar,", "não proclamar"],
     "resumo": ["A marca não precisa assustar para ser ouvida, nem anunciar "
                "para ser reconhecida.",
                "A autoridade aparece na qualidade da pergunta."],
     "y_direita": 1.95,
     "pares": [
         ("Você pode morrer amanhã.",
          "Quem depende financeiramente de você hoje?"),
         ("Você precisa contratar um seguro de vida.",
          "Antes do produto, precisamos entender o impacto financeiro que "
          "uma ausência produziria."),
         ("Olha onde eu cheguei.",
          "Esse reconhecimento representa dez anos de consistência e "
          "confiança de clientes."),
     ]},

    # 18 — vocabulário
    {"tipo": "colunas", "olho": "Vocabulário e estilo",
     "titulo": "As palavras da marca", "y": 4.45,
     "colunas": [
         ("Verbos", "Preparar · estruturar",
          "Preservar · antecipar · organizar · traduzir · acompanhar. São "
          "verbos de preparação: a marca conduz, não assiste."),
         ("Palavras próprias", "Continuidade · escolha",
          "Proteção · sucessão · dignidade financeira · liquidez · "
          "possibilidades · responsabilidade · consequência."),
         ("Nunca usamos", "~~Tragédia · urgência~~",
          "~~Fatalidade · desespero · oportunidade imperdível · a melhor "
          "proteção do mercado.~~ Nada que venda pelo susto."),
     ],
     "fecho": "Frases curtas. Ponto final. Argumento concreto. A comunicação "
              "acompanha o comportamento da marca: **escuta, entende e vai "
              "ao ponto.**"},

    # ————————————————————————————————————— 04 IDENTIDADE VISUAL
    {"tipo": "divisor", "numero": "04", "nome": ["Identidade", "visual"],
     "legenda": "O escudo, o verde e o dourado."},

    # 20 — as versões da marca
    {"tipo": "marca", "olho": "Logotipo", "titulo": "As versões da marca",
     "y": 4.35, "altura": 2.95,
     "versoes": [
         ("Principal", V_DOURADO, "4A534E",
          "Dourado sobre o verde da marca. É a versão de assinatura."),
         ("Monocromática", V_PRETO, "F6F4EF",
          "Preto sobre papel. Documento, contrato, impressão em uma cor."),
         ("Vertical", V_VERTICAL_PRETO, "CEC3B5",
          "Para espaços estreitos: avatar, carimbo, assinatura de e-mail."),
         ("Sobre fotografia", V_CLARO, "2C322E",
          "Versão clara, só quando o fundo for escuro o bastante."),
     ]},

    # 21 — o que preserva a marca
    {"tipo": "lista", "olho": "Usos", "titulo": "O que preserva a marca",
     "resumo": ["O escudo é o ativo mais permanente da identidade. Tudo o que "
                "o deforma, enfraquece a marca inteira."],
     "rotulo": "Sempre", "y_direita": 2.30,
     "itens": [
         "**Respiro.** Deixar em volta do logo, livre, pelo menos a altura do "
         "escudo;",
         "**Contraste.** Dourado sobre verde ou escuro; preto sobre papel ou "
         "areia. Dourado sobre claro, nunca;",
         "**Proporção.** O logo nunca é esticado, inclinado ou recortado;",
         "**Tamanho mínimo.** Abaixo de 2 cm de largura, usar só o escudo;",
         "**Uma marca por peça.** O escudo não divide espaço com selo, "
         "etiqueta ou moldura decorativa.",
     ],
     "fecho": "Nenhuma sombra, nenhum contorno, nenhum efeito. **A elegância "
              "da marca está na sua contenção.**"},

    # 22 — as cores
    {"tipo": "paleta", "olho": "Cores", "titulo": "A paleta", "y": 4.30,
     "altura": 2.90,
     "cores": [
         ("Verde profundo", "#4A534E",
          "A cor da marca. Fundo de capa, de capítulo e de assinatura."),
         ("Dourado", "#C9A961",
          "O acento. Filete, numeral e destaque — nunca em área grande."),
         ("Areia", "#CEC3B5",
          "A cor de apoio. Fundos claros, papelaria e aplicações impressas."),
         ("Grafite", "#2C322E",
          "O texto. Títulos e corpo sobre papel."),
         ("Papel", "#F6F4EF",
          "O fundo de leitura e o texto sobre o verde."),
     ]},

    # 23 — tipografia
    {"tipo": "tipografia", "olho": "Tipografia",
     "titulo": "A tipografia", "y": 4.25, "tam": 44,
     "familias": [
         ("Assinatura · Allrounder", "Outfit 1 Light",
          "Lucas Martini",
          "A serifada do logotipo. Vive no logo e na assinatura — não é "
          "fonte de texto corrido."),
         ("Texto · DM Sans", "Outfit 1 Light",
          "Proteção & Sucessão",
          "A sem-serifa de apoio: títulos, corpo e legenda. Caixa alta "
          "espacejada nos rótulos, sempre com espacejamento largo."),
         ("Hierarquia", "Outfit 1 Semi-Bold",
          "Clareza antes de volume",
          "Título grande em peso leve; destaque em semibold. O peso marca a "
          "frase que a pessoa leva embora — nunca a frase inteira."),
     ],
     "nota": "Os espécimes desta página estão compostos na fonte deste "
             "documento. As fontes oficiais da marca são a Allrounder, no "
             "logotipo, e a DM Sans, no texto."},

    # ——————————————————————————————————————————— 05 MANIFESTO
    {"tipo": "divisor", "numero": "05", "nome": "Manifesto",
     "legenda": "A marca em palavras, e a marca em uma página."},

    # 25 — manifesto
    {"tipo": "declaracao", "tom": "escuro", "olho": "Manifesto", "y": 2.95,
     "tam": 31, "agua": True,
     "linhas": ["Há coisas que levam anos para construir.",
                "Uma carreira. Uma família. Uma empresa. Um patrimônio.",
                "E nenhuma delas deveria ficar completamente",
                "dependente daquilo que não podemos controlar.",
                "Planejar não é esperar que algo dê errado.",
                "É reconhecer o valor daquilo que deu certo.",
                "É pensar antes. Enquanto existe tempo.",
                "Enquanto podemos escolher.",
                "Nem tudo pode ser previsto. **Mas muito pode ser preparado.**",
                "Porque proteção não existe para preservar dinheiro.",
                "**Existe para preservar possibilidades.**"]},

    # 26 — a marca em uma página
    {"tipo": "lista", "olho": "Síntese", "titulo": ["A marca em", "uma página"],
     "resumo": ["Se este documento inteiro se perdesse, bastaria esta "
                "página."],
     "rotulo": "O essencial", "y_direita": 1.95,
     "itens": [
         "**Crença fundadora.** O que levou anos para ser construído não "
         "deveria ficar entregue ao acaso.",
         "**Essência.** Construir segurança para preservar liberdade de "
         "escolha.",
         "**Causa.** Ampliar a cultura da preparação antes da urgência.",
         "**Território.** Continuidade.",
         "**Posicionamento.** Especialista em proteção e sucessão para quem "
         "deseja preservar o que construiu.",
         "**Princípio de comunicação.** Provar, não proclamar.",
         "**Personalidade.** Autoridade discreta.",
     ]},

    # 27 — fecho
    {"tipo": "fecho", "frase": "Proteção & Sucessão",
     "assinatura": "Método Marca com Essência ©   ·   KA | Inteligência para Marcas",
     "logo_largura": 6.6, "logo_y": 3.80, "y": 6.95},
]
