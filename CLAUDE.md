# CLAUDE.md — Instruções do projeto

Repositório das apresentações do **KA · Inteligência para Marcas**
(Kelly Albert). Duas camadas, sempre nesta ordem:

| Camada | O que define | Onde está |
|---|---|---|
| **1. Padrão de layout** | a aparência de **todas** as apresentações do KA | `padrao-ka/` |
| **2. Modelo de apresentação** | o roteiro e o conteúdo de **um tipo** de entrega | `modelos/<tipo>/` |
| **3. Cliente** | os textos e as fotos de **um** projeto | `clientes/<cliente>/` |

O layout nunca muda de um tipo de apresentação para outro. O que muda é o
roteiro.

---

## Gatilho: "padrão KA" / "modelo padrão" / "layout padrão"

Qualquer pedido de gerar apresentação **sem outro modelo especificado** usa o
padrão KA. Não inventar outro estilo.

1. Ler **`padrao-ka/SISTEMA-VISUAL.md`** — grade, paleta, tipografia,
   os sete arquétipos de página e os assets.
2. Montar com **`padrao-ka/ka_layout.py`**, que já traz tudo isso pronto.
   Não redesenhar o sistema; usar os arquétipos.
3. **Conferir antes de entregar** — obrigatório:
   ```bash
   padrao-ka/conferir.sh <arquivo>.pptx
   ```
   Ele acusa qualquer texto que passe do fundo do painel (9,60") e deixa a
   prévia em PNG para inspeção visual.
4. Commitar no branch de trabalho e entregar o `.pptx` com `SendUserFile`.

## O padrão de página pedido pela Kelly (outubro/2026)

**Um título e um bloco de texto. Nada empilhado.** Palavras dela:

> "Tem título, aí tem um títulozinho menor, aí outro menorzinho, aí uma
>  frase maior, aí uma linha. Não quero isso. Um título e um texto num
>  slide."

Na prática, numa página de conteúdo:

- **sem** eyebrow, **sem** linha de abertura em outro tamanho, **sem** frase
  de destaque com filete embaixo;
- título em caixa alta, o filete do padrão, e **um** bloco de texto — um
  corpo só, uma cor só;
- quando o conteúdo é mesmo de campos (causa, arquétipos, Golden Circle,
  pilares), vira **colunas** ou **camadas**: rótulo e texto lado a lado,
  nunca empilhados.

A página de um bloco só lê num corpo maior (24pt, não 21): é o único texto
da página.

**A identidade visual não muda**: painel claro sobre a textura de ondas,
Outfit, acento terracota — a de sempre. Os prints do brand book que ela
mandou eram referência de **limpeza de texto**, não de layout.

Referência viva: `clientes/lucas-martini/base_estrategica.py` — 18 páginas.

## Gatilho: "base estratégica" / apresentação com roteiro próprio

Quando a entrega **não** tem roteiro fixo — Base Estratégica, plano, proposta,
ou uma Revelação com estrutura diferente da padrão — use o **roteiro
declarativo**: o conteúdo declara a lista de páginas, e os arquétipos vêm
prontos.

1. Ler **`padrao-ka/ROTEIRO-DECLARATIVO.md`** — os 18 arquétipos de página,
   os três tratamentos de fotografia e as regras de ajuste automático.
2. Montar com **`padrao-ka/ka_paginas.py`** (`DeckNarrativo`).
3. Conferir com `padrao-ka/conferir.sh`.

Referência viva: `clientes/lucas-martini/` — duas apresentações, 63 e 69
slides. E `clientes/flavia-muccelin/sociedade.py` — 20 páginas com marcação
de imagem.

### Quando as fotos ainda não existem

Declarar a foto assim mesmo, com o **nome do arquivo futuro** e o briefing:

```python
{"tipo": "texto", "foto": "sociedade-flavia-retrato.png", "lado": "direita",
 "imagem": "Retrato da Flávia, meio corpo, em obra. Olhar direto.",
 "titulo": "...", "paragrafos": [...]}
```

A página sai com a **marcação**: a área exata que a imagem vai ocupar,
identificada. Quando o arquivo entrar em `assets/` com esse nome, a marcação
some e nada muda de lugar. Detalhe em `padrao-ka/ROTEIRO-DECLARATIVO.md`.

## A voz dos documentos: terceira pessoa

**Nada de primeira pessoa do plural.** Sem "nossa origem", "nossos valores",
"assumimos responsabilidade", "mudar nossa essência", "o que precisamos
preservar". Pedido da Kelly em outubro/2026, e vale para **todas** as
apresentações.

A razão é prática, não estilística: na primeira pessoa o documento só
funciona lido de dentro, e o mesmo arquivo precisa servir para apresentar a
marca a um sócio, a um candidato, a um parceiro ou ao mercado. Em terceira
pessoa ele afirma; na primeira, ele desabafa.

| Em vez de | Escrever |
|---|---|
| Nossa origem · Nossos valores | A origem · Os valores |
| Assumimos responsabilidade pelo resultado. | Responsabilidade pelo resultado. |
| Temos liberdade para propor. | Liberdade para propor. |
| O que precisamos preservar | O que preservar · O que precisa ser preservado |
| Crescer sem perder o que nos torna diferentes. | Crescer sem perder o que torna estas empresas diferentes. |
| O desafio não é mudar nossa essência. | O desafio não é mudar a essência. |
| Por que começamos pela essência? | Por que a essência vem primeiro? |

Nos valores e nos atributos, o infinitivo e o substantivo resolvem melhor que
a conjugação: "Aprender, melhorar e ampliar as possibilidades" diz o mesmo
que "Buscamos aprender…" e cabe em qualquer leitor.

**Duas exceções, e só estas duas:**

- **O manifesto.** É o gênero em que a marca fala — a primeira pessoa ali é
  convenção, e costuma ser o "nós" universal, não o corporativo.
- **A fala de exemplo.** Numa página de tom de voz, a frase que a marca diz
  ao cliente ("Antes do produto, precisamos entender o impacto…") é citação
  de discurso, não afirmação sobre a marca.

Para conferir antes de entregar, a varredura está em
`padrao-ka/conferir_voz.py`.

## Gatilho: "brand book" / "manual de marca"

Um brand book **não** é apresentação: é manual. Outra diagramação — cabeçalho
com paginação, capítulos numerados, título à esquerda e conteúdo à direita — e
é o único documento do padrão que veste a **identidade visual do cliente**, não
a do KA.

1. Ler **`padrao-ka/BRAND-BOOK.md`** — a grade, os 14 arquétipos e a paleta
   como parâmetro.
2. Montar com **`padrao-ka/ka_brandbook.py`** (`Brandbook`).
3. Conferir com `padrao-ka/conferir.sh <arquivo>.pptx --fundo 10.30`.

A tipografia continua sendo a Outfit. Fonte própria do cliente é **nomeada**
na página de tipografia, não usada no documento.

Referência viva: `clientes/lucas-martini/brandbook.py` — 27 páginas.

## Gatilho: "revelação de essência"

Primeira etapa do Método Marca com Essência ©.

1. Ler **`modelos/revelacao-de-essencia/MODELO.md`** — a tese, as seis seções,
   o roteiro página a página e o contrato do `conteudo.py`.
2. Criar `clientes/<cliente>/` (copiando `clientes/flavia-muccelin/` como
   referência), preencher o `conteudo.py` e colocar as fotos em `assets/`.
3. Gerar:
   ```bash
   python3 modelos/revelacao-de-essencia/gerar.py clientes/<cliente>
   ```

Referência viva e completa: `clientes/flavia-muccelin/` — 31 slides,
aprovado pela Kelly.

---

## Regras visuais inegociáveis

Detalhe completo em `padrao-ka/SISTEMA-VISUAL.md`. O essencial:

- Formato 16:9 — 20" × 11,25".
- Textura de ondas a 32% de opacidade no fundo de todo slide; painel claro
  `#F8F7F2` de cantos arredondados por cima, recuado 1,10", fundo em **9,60"**.
- **Fonte única: Outfit**, nas variantes nomeadas — a família de texto é a
  **Outfit 1** (`Outfit 1 Light` é o peso padrão; a Outfit 2 sobrou no eyebrow
  e na assinatura da capa). Nada de Calibri, Playfair ou IBM Plex. O peso vem
  do **nome** da fonte, nunca de negrito sintético.
- **O filete organiza a página, não a caixa.** Encher de cartõezinhos foi
  exatamente o que a Kelly rejeitou como "grosseiro, pouco elegante".
- Hierarquia por **escala e ar**, não por peso: título grande em **caixa
  alta** e peso leve. Títulos de página e nomes de seção sempre em caixa alta.
- Um único acento quente, o terracota `#A9724A`, em filetes curtos, pontos de
  lista e numerais. Nunca em área grande.
- Círculos de contorno fino, **nunca preenchidos**.
- Rodapé: pílula `DOCUMENTO | MARCA` à esquerda, logo KA à direita. Sem número
  de página.
- Escala tipográfica fechada — não inventar tamanho fora da tabela.

## Fotografia

**Tira vertical é o padrão.** Numa faixa horizontal o corte é vertical e come
a maior parte da altura: com foto 16:9, uma faixa que preserva o rosto não
deixa página para o texto. O horizontal que funciona é a **tela cheia**, onde
nada é cortado.

**O rosto nunca é cortado.** `padrao-ka/rostos.py` mapeia a cabeça de cada
foto; o motor calcula o recorte a partir desse mapa e, quando não cabe, vira a
orientação e avisa no build. Depois de trocar qualquer foto:

```bash
python3 padrao-ka/rostos.py clientes/<cliente>/assets
python3 padrao-ka/conferir_rostos.py <arquivo>.pptx clientes/<cliente>/assets
```

Detalhe em `padrao-ka/ROTEIRO-DECLARATIVO.md`.

## Quando o texto não couber

Cortar texto, **não** diminuir o corpo da fonte. Se não coube, o slide está
dizendo duas coisas — quebrar em duas páginas, como o gerador já faz com as
experiências formadoras e com a tabela de tensões.

O motor mede o texto na própria Outfit e avisa no build quando não cabe:

```
! texto nao cabe em "Reconhecimento × exposição": sobram 0.21" para cortar
```

Esse aviso é para ser atendido, não ignorado.

## Ambiente

LibreOffice Impress **está instalado e funciona** — usar para conferir o
resultado, sempre.

As fontes moram em `padrao-ka/fontes/` e precisam estar instaladas, uma vez
por máquina:

```bash
padrao-ka/instalar-fontes.sh
```

Sem elas o LibreOffice cai na DejaVu Sans, que é mais larga: a prévia mente e
a conferência acusa vazamento onde não há.

## `arquivo/`

Material anterior ao padrão KA atual (modelo YUFIL, gerador da primeira
versão da Revelação de Essência). Mantido só como histórico — **não usar como
base para nada novo**.
