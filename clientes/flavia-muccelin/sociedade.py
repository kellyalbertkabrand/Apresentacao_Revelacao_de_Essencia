# -*- coding: utf-8 -*-
"""
DUAS TRAJETÓRIAS, UMA NOVA FORÇA — Flávia & Elandi | FORMA e My Home

Só conteúdo. A identidade visual é a de sempre: painel claro sobre a textura
de ondas, Outfit, acento terracota (padrao-ka/ka_layout.py e
padrao-ka/ka_paginas.py).

A diagramação segue a regra da Kelly: **um título e um bloco de texto por
página**. Sem eyebrow, sem linha de abertura em outro corpo, sem frase de
destaque com filete embaixo. Onde o conteúdo é de campos (atributos, papéis,
as duas empresas), ele vira camadas ou colunas — rótulo e texto lado a lado,
nunca empilhados.

Versão de 21/10/2026. O texto é o dela, palavra por palavra, na ordem dela.
Duas observações sobre a estrutura, assinaladas e não silenciosas:

1. **Não há sumário.** O roteiro desta versão não traz seções, e inventar
   nomes de capítulo seria escrever por cima dela. É uma narrativa contínua,
   e lê melhor assim. Se quiser índice, basta nomear as três partes
   (a Flávia, o Elandi, o encontro).
2. **"O próximo capítulo" é título de duas páginas** — a 02 e a 21. No
   roteiro dela isso é proposital: abre e fecha o documento. Ficou como ela
   escreveu.

**As fotografias ainda não existem.** Cada página que pede imagem traz a
MARCAÇÃO dela: a área exata que a foto vai ocupar, com o briefing do que
entra ali. No dia em que o arquivo com o nome declarado em `foto` entrar em
`assets/`, a marcação some e nada se move de lugar.

    python3 clientes/flavia-muccelin/gerar.py sociedade
"""

MARCA = "Flávia & Elandi"
DOCUMENTO = "Duas Trajetórias, Uma Nova Força"
RODAPE = False          # sem pílula e sem logo no pé, como ela pediu
ARQUIVO = "Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elandi"

# As imagens que a apresentação pede. Os arquivos ainda não existem — cada
# página mostra a marcação até que eles cheguem em assets/ com estes nomes.
IMG = {
    "portao": "sociedade-casa-portao.png",
    "forma": "sociedade-ambiente-forma.png",
    "myhome": "sociedade-produto-my-home.png",
    "flavia": "sociedade-flavia-equipe.png",
    "elandi": "sociedade-elandi-retrato.png",
    "dupla": "sociedade-flavia-elandi.png",
}

PAGINAS = [
    {"tipo": "abertura"},

    # ——————————————————————————————————————————— 01
    {"tipo": "capa",
     "titulo": ["DUAS TRAJETÓRIAS,", "UMA NOVA FORÇA"],
     "subtitulo": ["Flávia & Elandi", "FORMA e My Home"],
     "assinatura": ["Método Marca", "com Essência ©"],
     "data": "Outubro/2026"},

    {"tipo": "declaracao",
     "linhas": ["Duas histórias que podem se encontrar",
                "para construir o próximo capítulo",
                "da FORMA e da My Home."]},

    # ——————————————————————————————————————————— 02
    {"tipo": "texto", "titulo": "O próximo capítulo",
     "paragrafos": [
         "A FORMA e a My Home chegaram até aqui impulsionadas pela visão, "
         "pelo conhecimento e pela liderança de Flávia.",
         "Agora, o crescimento abre espaço para uma nova contribuição: a "
         "experiência de Elandi em gestão e estruturação de grandes "
         "operações.",
     ]},

    # ——————————————————————————————————————————— 03
    {"tipo": "texto", "foto": IMG["portao"], "lado": "direita",
     "imagem": "O lugar da história: a casa além do portão, ou o próprio "
               "portão. Pode ser a casa de hoje, já dela. Imagem de "
               "arquitetura, sem pessoas.",
     "titulo": "A menina que não aceitou os limites",
     "tam_corpo": 21,
     "paragrafos": [
         "Aos 13 anos, Flávia era a filha do caseiro que sonhava com a casa "
         "além do portão.",
         "Enquanto a realidade mostrava o que não podia ter, ela imaginava o "
         "que poderia conquistar.",
         "Hoje, é proprietária daquele lugar.",
     ]},

    # ——————————————————————————————————————————— 04
    {"tipo": "lista", "titulo": "Um padrão que atravessa sua história",
     "itens": [
         "A origem humilde parecia delimitar seu futuro.",
         "A função de projetista limitava seu crescimento.",
         "As franquias restringiam sua liberdade de criar.",
         "As sobras tinham um destino previsto.",
     ],
     "marcar_ultimo": True,
     "fecho": "Flávia encontrou possibilidades onde tudo parecia "
              "determinado."},

    # ——————————————————————————————————————————— 05
    {"tipo": "camadas", "titulo": "A essência empreendedora de Flávia",
     "camadas": [
         ("Inconformismo", "Para questionar limites."),
         ("Imaginação", "Para enxergar possibilidades."),
         ("Autonomia", "Para construir à sua maneira."),
         ("Liderança", "Para mobilizar pessoas e realizar."),
     ]},

    # ——————————————————————————————————————————— 06
    {"tipo": "texto", "foto": IMG["forma"], "lado": "esquerda",
     "imagem": "Um ambiente assinado pela FORMA — marcenaria, acabamento, "
               "projeto entregue. O trabalho, não as pessoas.",
     "titulo": "A FORMA como expressão de sua essência",
     "tam_corpo": 21,
     "paragrafos": [
         "Flávia encontrou uma empresa existente e enxergou o que ela ainda "
         "poderia se tornar.",
         "Trouxe sua experiência, desenvolveu pessoas, elevou padrões e "
         "imprimiu sua visão.",
         "A FORMA tornou-se expressão de sua liberdade de criar.",
     ]},

    # ——————————————————————————————————————————— 07
    {"tipo": "texto", "foto": IMG["myhome"], "lado": "direita",
     "imagem": "Um produto My Home — o que nasceu da sobra. Pode ser a peça "
               "pronta, em uso, ou o material antes de virar produto.",
     "titulo": "A My Home revela outra face dessa força",
     "tam_corpo": 21,
     "paragrafos": [
         "Onde havia materiais destinados ao descarte, Flávia enxergou novas "
         "possibilidades.",
         "Guardou sobras por aproximadamente um ano até encontrar um "
         "caminho.",
         "A My Home nasceu dessa capacidade de dar novos destinos ao que "
         "parecia não ter mais valor.",
     ]},

    # ——————————————————————————————————————————— 08
    {"tipo": "texto", "foto": IMG["flavia"], "lado": "esquerda",
     "imagem": "Flávia com a equipe, ou conduzindo uma conversa de trabalho. "
               "Liderança em ação, não retrato posado.",
     "titulo": "Flávia é mais do que a fundadora",
     "tam_corpo": 21,
     "paragrafos": [
         "Sua presença se reflete nos produtos, no relacionamento com "
         "clientes e na cultura da equipe.",
         "Ela não apenas identifica oportunidades. Consegue mobilizar "
         "pessoas para transformá-las em realidade.",
         "Sua liderança tornou-se parte da identidade das empresas.",
     ]},

    # ——————————————————————————————————————————— 09
    {"tipo": "texto", "titulo": "Uma nova etapa exige uma nova estrutura",
     "paragrafos": [
         "A capacidade de Flávia de resolver e realizar impulsionou o "
         "crescimento.",
         "Mas a expansão trouxe novas responsabilidades e decisões.",
         "O próximo desafio é ampliar a capacidade de gestão sem perder "
         "aquilo que torna sua liderança tão valiosa.",
     ]},

    # ——————————————————————————————————————————— 10
    {"tipo": "texto", "foto": IMG["elandi"], "lado": "esquerda",
     "imagem": "Retrato do Elandi, meio corpo, em ambiente de gestão ou "
               "escritório. Expressão serena e atenta, luz natural.",
     "titulo": "Elandi, uma trajetória de gestão",
     "tam_corpo": 21,
     "paragrafos": [
         "Elandi começou a trabalhar aos 14 anos.",
         "Construiu quatro décadas de experiência profissional, atuando em "
         "grandes empresas e ocupando posições de gestão e controladoria.",
         "Desenvolveu uma visão que conecta operação, recursos, planejamento "
         "e resultados.",
     ]},

    # ——————————————————————————————————————————— 11
    {"tipo": "camadas", "titulo": "A essência profissional de Elandi",
     "camadas": [
         ("Discernimento", "Para compreender cenários."),
         ("Visão sistêmica", "Para conectar decisões e consequências."),
         ("Rigor", "Para proteger resultados."),
         ("Responsabilidade", "Para construir continuidade."),
     ]},

    # ——————————————————————————————————————————— 12
    {"tipo": "texto",
     "titulo": "O olhar de quem compreende a complexidade",
     "paragrafos": [
         "Ao analisar a expansão para mercados a centenas de quilômetros, "
         "Elandi considera custos operacionais, margens, logística e "
         "mudanças tributárias.",
         "Seu olhar não se limita ao resultado de uma venda.",
         "Busca compreender como cada decisão afeta a operação e a saúde "
         "financeira do negócio.",
     ]},

    # ——————————————————————————————————————————— 13
    {"tipo": "texto", "titulo": "Um olhar que vai além dos números",
     "paragrafos": [
         "Elandi também compreende o valor da experiência entregue.",
         "Para ele, uma montagem 99,99% correta ainda pode deixar no cliente "
         "a lembrança de um único detalhe mal resolvido.",
         "Esse olhar conecta eficiência operacional, qualidade e reputação.",
     ]},

    # ——————————————————————————————————————————— 14
    {"tipo": "texto", "titulo": "Responsabilidade é construir continuidade",
     "paragrafos": [
         "Após quase 20 anos na mesma empresa, Elandi vem preparando sua "
         "transição e transmitindo conhecimento à equipe.",
         "Não quer apenas concluir bem sua trajetória.",
         "Quer deixar condições para que o trabalho continue funcionando sem "
         "sua presença.",
     ]},

    # ——————————————————————————————————————————— 15
    {"tipo": "foto_cheia", "foto": IMG["dupla"],
     "imagem": "Flávia e Elandi juntos, em conversa de trabalho — mesa, "
               "projeto, obra ou escritório. Interação real, não retrato "
               "posado lado a lado. Imagem ampla, que aguente a frase por "
               "cima.",
     "linhas": ["“Eu tô bem preparado para não ser",
                "um obstáculo, e sim ser um agregador.”"],
     "apoio": "Elandi, em entrevista."},

    {"tipo": "texto", "titulo": "A maturidade de quem sabe somar",
     "paragrafos": [
         "Elandi reconhece a liderança e o conhecimento de Flávia.",
         "Sua intenção é colocar a própria experiência a serviço de uma "
         "construção que já conhece, acompanha e valoriza.",
     ]},

    # ——————————————————————————————————————————— 16
    {"tipo": "colunas", "titulo": "O papel singular de cada um",
     "colunas": [
         ("Flávia",
          "Representa a força criadora, a identidade e a direção dos "
          "negócios."),
         ("Elandi",
          "Pode representar a inteligência de gestão que estrutura e dá "
          "sustentação à expansão."),
     ],
     "fecho": "Um papel não substitui o outro. São competências que se "
              "encontram em torno de uma mesma ambição."},

    # ——————————————————————————————————————————— 17
    {"tipo": "texto", "titulo": "Uma ambição compartilhada",
     "paragrafos": [
         "Elandi também enxerga o potencial de crescimento das marcas.",
         "Vê a FORMA ampliando sua presença estadual e a My Home alcançando "
         "o mercado nacional.",
         "Ele compartilha a visão de futuro e traz a experiência necessária "
         "para ajudar a planejar sua realização.",
     ]},

    # ——————————————————————————————————————————— 18
    {"tipo": "colunas", "titulo": "Duas empresas, diferentes exigências",
     "colunas": [
         ("FORMA",
          "Combina personalização, alto valor agregado e complexidade "
          "produtiva."),
         ("My Home",
          "Trabalha com produtos próprios, comércio eletrônico e potencial "
          "de escala."),
     ],
     "fecho": "A inteligência de gestão precisa considerar as "
              "particularidades de cada modelo, suas margens, investimentos "
              "e necessidades operacionais."},

    # ——————————————————————————————————————————— 19
    {"tipo": "colunas", "titulo": "Onde cada um pode gerar mais valor",
     "colunas": [
         ("Flávia",
          "Permanece como referência na visão de mercado, nos clientes, nos "
          "produtos, na inovação e na liderança."),
         ("Elandi",
          "Pode assumir maior protagonismo na gestão financeira, "
          "controladoria, custos, planejamento e administração."),
     ],
     "fecho": "A oportunidade está em ampliar a autonomia e a contribuição "
              "de ambos."},

    # ——————————————————————————————————————————— 20
    {"tipo": "texto", "titulo": "Uma parceria que evolui a empresa",
     "paragrafos": [
         "Flávia já construiu conhecimento, reputação, processos e uma "
         "equipe capaz de entregar sua visão.",
         "A chegada de Elandi pode fortalecer essa estrutura com mais "
         "inteligência financeira, planejamento e capacidade de decisão.",
         "Não se trata de mudar a essência do negócio, mas de preparar sua "
         "próxima etapa.",
     ]},

    # ——————————————————————————————————————————— 21
    {"tipo": "texto", "titulo": "O próximo capítulo",
     "paragrafos": [
         "Flávia passou a vida mostrando que os limites não precisam "
         "determinar o futuro.",
         "Elandi construiu sua carreira compreendendo como transformar "
         "decisões em resultados duradouros.",
         "Agora, duas experiências podem se somar em torno daquilo que ambos "
         "acreditam ser possível construir.",
     ]},

    {"tipo": "declaracao",
     "linhas": ["A próxima conquista não é",
                "apenas chegar mais longe."],
     "apoio": "É fazer com que tudo o que foi construído tenha condições de "
              "continuar crescendo."},

    {"tipo": "fecho", "frase": "OBRIGADA!"},
]
