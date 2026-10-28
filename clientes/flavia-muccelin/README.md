# Flávia Pereira Muccelin — FORMA e My Home

Quatro entregas, dois motores.

| Arquivo | O que é | Páginas | Como gerar |
|---|---|---|---|
| `conteudo.py` | Revelação de Essência — origem identitária da fundadora | 31 | `python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin` |
| `sociedade.py` | Duas trajetórias, uma nova força — Flávia & Elandi | 26 | `python3 clientes/flavia-muccelin/gerar.py sociedade` |
| `cultura.py` | Cultura Organizacional **e** de Marca — FORMA e My Home | 40 | `python3 clientes/flavia-muccelin/gerar.py cultura` |
| `marcas_unicas.py` | O que torna essas marcas únicas — a versão longa, no formato mapeado | 60 | `python3 clientes/flavia-muccelin/gerar.py marcas_unicas` |

A Revelação tem **roteiro fixo** e gerador próprio. A apresentação da
sociedade tem roteiro próprio e usa o **roteiro declarativo**
([`padrao-ka/ROTEIRO-DECLARATIVO.md`](../../padrao-ka/ROTEIRO-DECLARATIVO.md)).

A identidade visual é a mesma em todas, e é a mesma do Lucas: painel claro
sobre a textura de ondas, Outfit, acento terracota.

**A voz é de terceira pessoa em todas elas.** Sem "nossa origem", "nossos
valores", "assumimos responsabilidade", "mudar nossa essência" — pedido da
Kelly, e por um motivo prático: na primeira pessoa o documento só funciona
lido de dentro, e o mesmo arquivo precisa apresentar a marca a um sócio, a um
candidato ou ao mercado. A regra está em [`CLAUDE.md`](../../CLAUDE.md) e a
varredura em `padrao-ka/conferir_voz.py`:

```bash
python3 padrao-ka/conferir_voz.py
```

---

## Duas trajetórias, uma nova força

Documento de alinhamento societário entre Flávia e Elandi, para a FORMA e a
My Home. O conteúdo veio da Kelly em 21 slides; sai aqui em 26 páginas, e a
razão é a regra dela:

> "Um título e um texto num slide."

Três slides do roteiro carregavam dois blocos distintos — a citação do
Elandi e a leitura dela, a narrativa final e a sua conclusão. Empilhar os
dois é o que a regra proíbe, então cada bloco virou a sua própria página. O
texto é o dela, palavra por palavra, na ordem dela.

**Sem rodapé** (`RODAPE = False`): sem a pílula `DOCUMENTO | MARCA` e sem o
logo KA no pé, como ela pediu.

### Duas decisões de estrutura, assinaladas

1. **Não há sumário.** O roteiro desta versão não traz seções, e inventar
   nomes de capítulo seria escrever por cima dela. É uma narrativa contínua
   — a Flávia, o Elandi, o encontro — e lê melhor assim. Se quiser índice, é
   só nomear as três partes.
2. **"O próximo capítulo" é título de duas páginas**, a 02 e a 21. No
   roteiro dela isso abre e fecha o documento. Ficou como ela escreveu.

### Como o conteúdo virou página

| Arquétipo | Onde |
|---|---|
| `texto` | a narrativa corrida — a maioria das páginas |
| `lista` | o padrão que atravessa a história (slide 04) |
| `camadas` | as essências de cada um (slides 05 e 11): rótulo e leitura lado a lado |
| `colunas` | papéis, as duas empresas, onde cada um gera valor (16, 18, 19) |
| `declaracao` | a abertura e a conquista final |
| `foto_cheia` | a citação do Elandi |

### As imagens ainda não existem

Seis páginas pedem fotografia e trazem a **marcação**: a área exata que a
imagem vai ocupar, com o briefing do que entra ali.

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `sociedade-casa-portao.png` | a casa além do portão — o lugar da história |
| `sociedade-ambiente-forma.png` | um ambiente assinado pela FORMA |
| `sociedade-produto-my-home.png` | um produto My Home, o que nasceu da sobra |
| `sociedade-flavia-equipe.png` | Flávia com a equipe, liderança em ação |
| `sociedade-elandi-retrato.png` | retrato do Elandi, meio corpo |
| `sociedade-flavia-elandi.png` | os dois em conversa de trabalho — tela cheia |

Quando esses arquivos entrarem em `assets/` com esses nomes, **a marcação
desaparece sozinha e nada muda de lugar**. Depois de colocá-los, rodar o
mapa de rostos para que o corte nunca decepe ninguém:

```bash
python3 padrao-ka/rostos.py clientes/flavia-muccelin/assets
python3 clientes/flavia-muccelin/gerar.py sociedade
python3 padrao-ka/conferir_rostos.py \
    clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elandi.pptx \
    clientes/flavia-muccelin/assets
```

### Conferência

```bash
padrao-ka/conferir.sh clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elandi.pptx
```

---

## Cultura Organizacional e de Marca — uma apresentação só

**As três apresentações de cultura viraram uma.** A Kelly foi clara: a
cultura organizacional e as duas culturas de marca vivem no mesmo documento.
Faz sentido — a organizacional é compartilhada pelas duas empresas, e separar
as marcas em arquivos distintos obrigava o leitor a abrir três para entender
uma coisa só.

`marca_forma.py` e `marca_my_home.py` foram aposentados; o conteúdo atual é o
roteiro novo de 19 slides que ela mandou, e vive inteiro em `cultura.py`.
O histórico dos arquivos antigos está no git.

As 19 páginas saem em **40**, pela regra de sempre — um título e um bloco de
texto por página. Cada slide carregava de três a cinco blocos (definição,
método, elementos, crença, valores, personalidade, expressão), e empilhar
isso é o que a regra proíbe.

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` com foto | as cinco viradas de seção, em tela cheia de imagem | 5 |
| `declaracao` | a página de silêncio: uma crença, uma descoberta | 8 |
| `colunas` | os campos em paralelo — comportamento, experiência, percepção | 8 |
| `camadas` | rótulo e leitura lado a lado — valores, tensões, síntese | 3 |
| `palavras` | os elementos investigados e a liderança | 3 |
| `contraste` | as duas essências culturais, separadas pelo × | 1 |
| `foto_cheia` | a essência de cada marca, em tela cheia | 2 |
| `texto` | só onde o conteúdo é mesmo narrativa | 7 |

### Cinco seções, não quatro

O sumário do roteiro traz quatro seções (organizacional, marca Forma, marca
My Home, síntese), mas o corpo abre "02. CULTURA DE MARCA" com o conceito e o
método **antes** de entrar em cada marca. Como esse conceito vale para as
duas, ele virou a seção 02 e as marcas passaram a 03 e 04 — assim o sumário e
as viradas contam a mesma história.

| | Seção |
|---|---|
| 01 | Cultura organizacional |
| 02 | Cultura de marca — o conceito e o método |
| 03 | Cultura de marca Forma |
| 04 | Cultura de marca My Home |
| 05 | Síntese |

### As dez imagens

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `cultura-div-organizacional.png` | virada 01 — a oficina em movimento, plano aberto |
| `cultura-div-marca.png` | virada 02 — detalhe de acabamento, plano fechado |
| `cultura-div-forma.png` | virada 03 — projeto complexo em execução |
| `cultura-div-my-home.png` | virada 04 — a bancada de criação, protótipo |
| `cultura-div-sintese.png` | virada 05 — o time completo das duas operações |
| `cultura-oficina-forma.png` | a origem do ofício, onde tudo começou |
| `cultura-projeto-forma.png` | conversa técnica sobre o projeto |
| `cultura-produto-my-home.png` | o material antes de virar produto |
| `cultura-ambiente-forma.png` | ambiente entregue — tela cheia da essência da Forma |
| `cultura-produto-em-casa.png` | produto no ambiente — tela cheia da essência da My Home |

Enquanto não existirem, cada página mostra a **marcação**: a área exata com o
briefing. Quando entrarem em `assets/` com esses nomes, a marcação some e
nada muda de lugar.

```bash
python3 padrao-ka/rostos.py clientes/flavia-muccelin/assets
python3 clientes/flavia-muccelin/gerar.py cultura
padrao-ka/conferir.sh clientes/flavia-muccelin/Cultura-Organizacional-e-de-Marca-Forma-e-My-Home.pptx
python3 padrao-ka/conferir_voz.py clientes/flavia-muccelin
```

---

## O que torna essas marcas únicas — a versão longa

Roteiro novo, mandado pela Kelly depois do mapeamento do arquivo que ela
rediagramou à mão. É a mesma matéria de `cultura.py`, muito mais funda: os
depoimentos nominais, as três situações da equipe, a tabela de forças e
desafios, os pontos de atenção e as duas essências culturais.

**Ela não substitui `cultura.py`.** As duas convivem: aquela é o roteiro de
19 slides, esta é o de 23. Se a Kelly quiser aposentar a primeira, é só
tirá-la de `DECKS` em `gerar.py` — o histórico fica no git.

As 23 páginas saem em **60**, pela regra de sempre: um título e um bloco de
texto por página.

### Quatro seções numeradas, como no sumário dela

O roteiro tem uma virada "CULTURA DE MARCA · FORMA E MY HOME" que não está no
sumário — é o conceito que vale para as duas marcas. Ela entra **sem
número**, como ponte, e as quatro seções do sumário ficam intactas. As
viradas internas do roteiro ("História e origem", "Comportamentos e
experiência", "Percepção externa e coerência") também são sem número: só as
quatro seções levam numeral e fotografia, e é isso que mantém a hierarquia
legível com doze viradas no documento.

| | Seção |
|---|---|
| 01 | Cultura organizacional |
| 02 | Cultura de marca Forma |
| 03 | Cultura de marca My Home |
| 04 | Síntese |

### As pessoas aparecem com nome

Tanyllo, Pâmella, Letícia, Mapinha, Joel, Weudes, Júlia Matsuda, Rodrigues,
Nathaly e Júlio César são citados nominalmente, como no roteiro — e duas
falas vão entre aspas, do Joel e da Pâmella. **Vale confirmar com cada um
antes de a apresentação circular fora da empresa.**

As duas falas ficam na primeira pessoa porque são citação de discurso, não
afirmação sobre a marca: é a exceção que o CLAUDE.md prevê.

### As imagens

Dez páginas pedem fotografia. Oito nomes são os mesmos de `cultura.py` — a
mesma foto serve às duas apresentações — e dois são novos:

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `cultura-obra-cliente.png` | a obra em andamento — tela cheia da fala do Joel |
| `cultura-producao-my-home.png` | a produção da My Home — tela cheia da fala da Pâmella |

```bash
python3 clientes/flavia-muccelin/gerar.py marcas_unicas
padrao-ka/conferir.sh clientes/flavia-muccelin/O-Que-Torna-Essas-Marcas-Unicas-Forma-e-My-Home.pptx
python3 padrao-ka/conferir_voz.py clientes/flavia-muccelin
```
