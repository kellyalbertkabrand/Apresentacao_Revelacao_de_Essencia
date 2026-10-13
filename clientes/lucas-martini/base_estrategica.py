# -*- coding: utf-8 -*-
"""
BASE ESTRATÉGICA DA MARCA — Lucas Martini | Proteção & Sucessão

Só conteúdo. A diagramação é a do **brand book** (padrao-ka/ka_brandbook.py):
título à esquerda, bloco de texto à direita, página limpa — foi o que a Kelly
pediu depois de ver os slides do Brand Book KA 2026.

O padrão é um só: **um título e um bloco de texto**. Nada de frase miúda
empilhada com outra frase miúda. Onde o conteúdo tem campos (causa,
arquétipos, pilares, Golden Circle, arquitetura), eles viram colunas com
rótulo, nome e filete — o mesmo arranjo da página de arquétipos dela.

Conteúdo: o texto que a Kelly escreveu, na ordem dela, com a essência em 01 e
o Lucas em 02, como ela pediu. As marcas de origem que vieram coladas no
texto ("Identidade Verbal - Lucas José…", "mft-nwyj-ixz…", "IKIGAI
Empresarial…") são referências da ferramenta dela, não conteúdo de slide, e
ficaram de fora.

Sem páginas de separação: o título de cada página já é o nome do tema, e um
separador com o mesmo nome seria repetição. Ligar os separadores é uma linha
(`divisor` antes de cada tema).
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, os.path.join(RAIZ, "padrao-ka"))

from ka_layout import LOGO_KA, LOGO_KELLY, LOGO_PARCEIRO  # noqa: E402

MARCA = "Lucas Martini"
DOCUMENTO = "Base Estratégica da Marca"
ARQUIVO = "Base-Estrategica-da-Marca-Lucas-Martini"
MOTOR = "brandbook"          # a diagramacao limpa, de duas colunas
CABECALHO_DOCUMENTO = False  # no alto fica so a paginacao

# A paleta do Brand Book KA 2026, medida no arquivo da Kelly: papel, marinho
# e o acento quente. É a dela, não a do cliente — este documento é do KA.
PALETA = {
    "escuro": "152535", "escuro2": "1F3449", "claro": "F8F7F2",
    "tinta": "152535", "corpo": "5A6066", "suave": "9AA0A6", "fio": "E2E0DA",
    "acento": "C87A44", "acento_escuro": "F0A337", "sobre_escuro": "F2F1EC",
    "corpo_escuro": "C9CFD6", "areia": "E8E4DA",
}

LOGOS = {
    "ka": LOGO_KA,
    "kelly": LOGO_KELLY,
    "parceiro": LOGO_PARCEIRO,
    "escuro": LOGO_KA,
}

PAGINAS = [
    {"tipo": "abertura"},

    {"tipo": "capa_ka",
     "titulo": ["Base estratégica", "da marca"],
     "subtitulo": ["Lucas Martini", "Proteção & Sucessão"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "indice", "titulo": "Conteúdo", "grade": 2, "y": 4.00,
     "passo": 0.86,
     "itens": [
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

    # 01
    {"tipo": "texto", "olho": "01",
     "titulo": ["Essência", "da marca"],
     "paragrafos": [
         "**Construir segurança para preservar liberdade de escolha.**",
         "A marca parte da ideia de que nem tudo pode ser previsto, mas é "
         "possível se preparar para que um imprevisto não elimine "
         "alternativas nem comprometa tudo o que foi construído.",
     ]},

    # 02
    {"tipo": "texto", "olho": "02",
     "titulo": ["Quem é", "Lucas Martini"],
     "paragrafos": [
         "**Especialista em Proteção & Sucessão, com mais de dez anos de "
         "atuação.**",
         "Sua experiência no mercado financeiro e a vivência com famílias e "
         "empresas deram origem a uma atuação consultiva, baseada em "
         "**planejamento, personalização, relacionamento e acompanhamento.**",
     ]},

    # 03
    {"tipo": "colunas", "olho": "03",
     "titulo": ["Causa, liderança", "e tribo"], "y": 4.55,
     "colunas": [
         ("Causa", "Preparar antes",
          "Ampliar a cultura de proteção e preparação antes do imprevisto."),
         ("Liderança", "Enxergar antes",
          "Ajudar pessoas a enxergar riscos, impactos e possibilidades antes "
          "que a urgência determine as decisões."),
         ("Tribo", "Quem carrega responsabilidade",
          "Pessoas que carregam responsabilidade sobre renda, família, "
          "patrimônio ou empresa."),
     ]},

    # 04
    {"tipo": "texto", "olho": "04",
     "titulo": ["Princípio", "central"],
     "paragrafos": [
         "**O que levou anos para ser construído não deveria ficar entregue "
         "ao acaso.**",
         "Planejamento é uma forma de proteger conquistas e preservar "
         "possibilidades diante do que não pode ser controlado.",
     ]},

    # 05
    {"tipo": "texto", "olho": "05",
     "titulo": ["Público-alvo", "e persona"],
     "paragrafos": [
         "Profissionais, empresários, sócios e famílias que possuem "
         "responsabilidades financeiras, patrimoniais ou sucessórias e "
         "**querem proteger o que construíram.**",
         "A persona central é alguém que entende o valor das suas conquistas "
         "e quer se preparar para que um imprevisto não comprometa sua "
         "família, seu patrimônio ou sua empresa.",
     ]},

    # 06
    {"tipo": "colunas", "olho": "06",
     "titulo": ["Arquétipos", "da marca"], "y": 4.55,
     "colunas": [
         ("Principal", "O Sábio",
          "Traduz complexidade, orienta decisões e transforma informação em "
          "planejamento."),
         ("Secundário", "O Cuidador",
          "Protege, acompanha e assume responsabilidade sobre decisões que "
          "afetam pessoas, famílias e empresas."),
     ],
     "fecho": "Os arquétipos são uma síntese estratégica a partir da atuação "
              "consultiva, do relacionamento e da responsabilidade descritos "
              "pelo próprio Lucas."},

    # 07
    {"tipo": "numerais", "olho": "07",
     "titulo": ["Pilares", "da marca"], "y": 4.80,
     "itens": [
         ("Proteção", "Preservar o que foi construído."),
         ("Planejamento", "Antecipar riscos e criar alternativas."),
         ("Personalização", "Construir soluções a partir de cada realidade."),
         ("Confiança", "Sustentar relações de longo prazo."),
         ("Continuidade",
          "Permitir que família, patrimônio e empresa possam seguir."),
     ]},

    # 08
    {"tipo": "texto", "olho": "08",
     "titulo": ["DNA", "da marca"],
     "paragrafos": [
         "**Proteção. Confiança. Responsabilidade. Personalização. "
         "Continuidade.**",
         "Esses são os atributos que devem permanecer presentes em qualquer "
         "expressão da marca, do atendimento à comunicação.",
     ]},

    # 09
    {"tipo": "texto", "olho": "09",
     "titulo": ["Voz", "da marca"],
     "paragrafos": [
         "A voz de Lucas deve transmitir **conhecimento sem distanciamento** "
         "e **segurança sem arrogância.**",
         "**Clara, segura, humana, elegante e consultiva.**",
     ]},

    # 10
    {"tipo": "lista", "olho": "10", "titulo": ["Tom", "de voz"],
     "y_direita": 2.60,
     "itens": ["**Técnico**, sem ser complicado.",
               "**Direto**, sem ser frio.",
               "**Seguro**, sem ser arrogante.",
               "**Humano**, sem dramatização.",
               "**Sofisticado**, sem ostentação."]},

    # 11
    {"tipo": "texto", "olho": "11", "titulo": "Posicionamento",
     "paragrafos": [
         "**Lucas Martini é especialista em Proteção & Sucessão para "
         "pessoas, famílias e empresas que querem preservar o que "
         "construíram e manter possibilidades diante de imprevistos e "
         "transições.**",
         "**Proteção & Sucessão para o que precisa continuar.**",
     ]},

    # 12
    {"tipo": "colunas", "olho": "12", "titulo": "Golden Circle", "y": 4.55,
     "colunas": [
         ("Por quê", "Preservar possibilidades",
          "Quando a vida foge do previsto."),
         ("Como", "Com planejamento personalizado",
          "Conhecimento, relacionamento e acompanhamento ao longo do tempo."),
         ("O quê", "Estratégias de proteção",
          "Proteção pessoal, familiar, empresarial e sucessória."),
     ]},

    # 13
    {"tipo": "colunas", "olho": "13",
     "titulo": ["Arquitetura", "da marca"], "y": 4.70,
     "colunas": [
         ("Marca pessoal", "Lucas Martini", ""),
         ("Atuação", "Proteção & Sucessão", ""),
         ("Assinatura empresarial", "Martini | Proteção & Sucessão", ""),
         ("Monograma", "LM", ""),
     ],
     "fecho": "O uso de “Martini” ganha força porque é a forma pela qual "
              "Lucas já é reconhecido em seu convívio pessoal e "
              "profissional."},

    # 14
    {"tipo": "declaracao", "tom": "escuro", "olho": "14 · Manifesto",
     "y": 2.95, "tam": 31,
     "linhas": ["Há coisas que levam anos para construir.",
                "Uma carreira. Uma família. Uma empresa.",
                "Um patrimônio. Uma história.",
                "Nem tudo pode ser previsto.",
                "Mas muito pode ser preparado.",
                "Planejar é proteger o que foi construído",
                "enquanto ainda existe tempo para escolher.",
                "Porque proteção não existe apenas",
                "para preservar patrimônio.",
                "**Existe para preservar possibilidades.**"]},

    {"tipo": "fecho", "tom": "claro", "frase": "Obrigada!",
     "assinatura": "Método Marca com Essência ©   ·   KA | Inteligência para Marcas",
     "logo_largura": 4.40, "logo_y": 4.70, "y": 6.40},
]
