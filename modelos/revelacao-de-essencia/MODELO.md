# MODELO — REVELAÇÃO DE ESSÊNCIA

Primeira etapa do **Método Marca com Essência ©**. Investiga a origem
identitária de uma marca a partir da história de quem a fundou, e entrega a
frase de essência que a Base Estratégica vai traduzir em direção.

Este documento descreve o **roteiro e o conteúdo**. A aparência vem do padrão
de layout comum a todas as apresentações do KA, documentado em
[`padrao-ka/SISTEMA-VISUAL.md`](../../padrao-ka/SISTEMA-VISUAL.md).

```bash
python3 modelos/revelacao-de-essencia/gerar.py clientes/<cliente>
```

---

## 1. A tese

A apresentação responde a uma pergunta só:

> **O que já fazia parte de quem a fundadora é, antes das marcas existirem?**

E chega lá por acumulação, não por afirmação. A essência nunca é declarada de
saída: ela é a única leitura que sobra depois que história, tensões, padrões e
Ikigai apontam para a mesma lógica. Por isso a ordem das seis seções é fixa —
inverter qualquer uma delas transforma a revelação em opinião.

**História + tensões + padrões + Ikigai = essência**

O que a apresentação **não** é: uma análise psicológica da fundadora. É a
investigação da origem identitária das marcas a partir dela. Essa distinção
aparece explicitamente no slide 4 e deve continuar aparecendo.

---

## 2. As seis seções

| | Seção | O que estabelece |
|---|---|---|
| 01 | **A origem** | As experiências que formaram a visão de mundo. |
| 02 | **As tensões** | Os momentos que a colocaram em movimento. |
| 03 | **Os padrões** | A lógica que se repete ao longo da trajetória. |
| 04 | **O Ikigai** | O que gera sentido e realização. |
| 05 | **A essência** | O princípio que conecta a história. |
| 06 | **As marcas** | Como essa essência se manifesta em cada negócio. |

---

## 3. O roteiro página a página

Ordem fixa, montada por `gerar.py`. As páginas marcadas **(n)** se repetem
conforme o volume de conteúdo — o gerador quebra sozinho e nunca deixa texto
vazar do painel.

| # | Arquétipo | Página | Campo |
|---|---|---|---|
| 1 | A1 | Abertura (logos) | — |
| 2 | A2 | Capa | `TITULO_1/2`, `SUBTITULO`, `ASSINATURA`, `DATA` |
| 3 | A3 | Sumário | `SECOES` |
| 4 | A5 | Por que começamos pela essência | `PORQUE` |
| 5 | A5 | A pergunta que conduz a etapa | `PERGUNTA` |
| 6 | A3 | Como chegamos à revelação (o método) | `METODO` |
| 7 | A4 | **Divisor 01 — A origem** | `SECOES[0]` |
| 8 | A5 | Onde essa história começa | `ORIGEM` |
| 9 | A5 | Os primeiros sinais | `SINAIS` |
| 10–11 **(n)** | A5 | As experiências que a formaram — 2 por página | `EXPERIENCIAS` |
| 12 | A4 | **Divisor 02 — As tensões** | `SECOES[1]` |
| 13–14 **(n)** | A5 | As tensões — 3 linhas por página | `TENSOES` |
| 15 | A4 | **Divisor 03 — Os padrões** | `SECOES[2]` |
| 16 | A5 | O padrão invisível | `PADRAO` |
| 17 | A5 | O movimento que se repete | `MOVIMENTO` |
| 18 | A6 | Manifesto — a linha mestra | `LINHA_MESTRA` |
| 19 | A4 | **Divisor 04 — O Ikigai** | `SECOES[3]` |
| 20 | A5 | O que move a fundadora | `IKIGAI` |
| 21 | A3 | O mapa do Ikigai (4 quadrantes) | `MAPA` |
| 22 | A5 | O centro do Ikigai | `CENTRO` |
| 23 | A3 | Razão de ser | `RAZAO_DE_SER` |
| 24 | A4 | **Divisor 05 — A essência** | `SECOES[4]` |
| 25 | A3 | Onde a história e o Ikigai se encontram | `ENCONTRO` |
| 26 | A3 | **A frase de essência** | `ESSENCIA` |
| 27 | A4 | **Divisor 06 — As marcas** | `SECOES[5]` |
| 28 | A5 | Como a essência se manifesta nas marcas | `MARCAS` |
| 29 | A5 | Da essência à estratégia | `PROXIMA` |
| 30 | A3 | Fecho seco | `FECHO` |
| 31 | A7 | Agradecimento | — |

A foto **alterna de lado** automaticamente a cada página A5.

---

## 4. As fotos

Em `clientes/<cliente>/assets/`, nomeadas pelo destino. `.jpg`. Qualquer uma
que faltar é simplesmente ignorada — a página sai sem a foto.

```
04-metodo.jpg           09-origem.jpg          14-tensoes.jpg      20-ikigai.jpg
05-pergunta.jpg         10-primeiros-sinais.jpg 16-padrao-invisivel.jpg 23-centro-ikigai.jpg
11-experiencias-1.jpg   12-experiencias-2.jpg  18-movimento.jpg    29-marcas.jpg
30-estrategia.jpg
```

O `foto()` faz center-crop, então a imagem pode vir em qualquer proporção —
mas como ela sangra numa faixa vertical de ~40% da largura, **retrato funciona
melhor que paisagem**, e o assunto precisa estar no centro do quadro.

---

## 5. O contrato do `conteudo.py`

Um módulo Python só com dados, em `clientes/<cliente>/conteudo.py`.

### Identificação
```python
MARCA      = "Flávia Pereira Muccelin"      # vai para o rodapé, em caixa alta
ARQUIVO    = "Flavia-Pereira-Muccelin"      # nome do .pptx, sem acento
TITULO_1   = "REVELAÇÃO DE"                 # capa, linha 1
TITULO_2   = "ESSÊNCIA"                     # capa, linha 2
SUBTITULO  = "Nome  |  Origem Identitária da Fundadora"
ASSINATURA = ["Método Marca", "com Essência ©"]
DATA       = "Setembro/2026"
```

### Sumário
```python
SECOES = [("01", "A origem", "As experiências que formaram a visão de mundo."), ...]
```
Seis tuplas `(numero, nome, descricao)`. São elas que geram os seis divisores.

### Campos de conteúdo

| Campo | Estrutura |
|---|---|
| `PORQUE` | `{titulo, lead, corpo, nao_e, e}` |
| `PERGUNTA` | lista de linhas — a pergunta central, quebrada à mão |
| `METODO` | `{titulo, lead, dimensoes: [(nome, desc)] ×4, equacao: [str], nota}` |
| `ORIGEM` | `{titulo, lead, corpo, marcante, valores: [str]}` |
| `SINAIS` | `{titulo, lead, corpo, falas: [(contexto, fala)]}` |
| `EXPERIENCIAS_TITULO` | string, repetida em cada página do bloco |
| `EXPERIENCIAS` | `[(num, titulo, fato, revela)]` — **2 por página** |
| `TENSOES` | `{titulo, lead, linhas: [(rotulo, fala, resposta, e_relato)], fecho}` — **3 linhas por página** |
| `PADRAO` | `{titulo, lead, etapas: [str], fecho}` |
| `MOVIMENTO` | `{titulo, passos: [str], sintese: [str]}` |
| `LINHA_MESTRA` | `{frase: [linhas], apoio}` |
| `IKIGAI` | `{titulo, lead, perguntas: [str] ×4, fecho}` |
| `MAPA` | `{titulo, quadrantes: [(rotulo, texto)] ×4}` |
| `CENTRO` | `{titulo, lead, exemplos: [str], contexto, fala}` |
| `RAZAO_DE_SER` | `{frase: [linhas], apoio}` |
| `ENCONTRO` | `{titulo, lead, eixos: [(rotulo, desc)] ×4, movimentos: [str]}` |
| `ESSENCIA` | `{eyebrow, frase: [linhas], camadas: [(rotulo, desc)] ×3, fecho}` |
| `MARCAS` | `{titulo, lead, marcas: [(rotulo, titulo, desc)], fecho}` |
| `PROXIMA` | `{titulo, lead, corpo, destaque}` |
| `FECHO` | lista de linhas |

Onde o campo é uma **lista de linhas** (`PERGUNTA`, `frase`, `FECHO`), a quebra
é manual e intencional: cada linha é uma unidade de sentido. Não escrever um
parágrafo corrido e deixar o PowerPoint quebrar.

Campos marcados **×4** ou **×3** têm o número de colunas fixado pela grade.
Mudar a quantidade quebra o alinhamento.

---

## 6. Como abrir um cliente novo

```bash
cp -r clientes/flavia-muccelin clientes/<novo-cliente>
rm clientes/<novo-cliente>/assets/*.jpg
rm clientes/<novo-cliente>/*.pptx
# trocar os textos em conteudo.py, colocar as fotos em assets/
python3 modelos/revelacao-de-essencia/gerar.py clientes/<novo-cliente>
```

Depois **conferir que nada vazou do painel** — o procedimento está em
`padrao-ka/SISTEMA-VISUAL.md` §7. Texto mais longo que o da Flávia quebra em
mais linhas e pode passar do fundo do painel (9,60"); o gerador não encolhe
fonte sozinho, de propósito. Quando vazar, a correção certa é **cortar texto**,
não diminuir corpo: se não coube, é porque o slide está dizendo duas coisas.

---

## 7. O que perguntar ao cliente antes de começar

- Nome da fundadora e das marcas; mês/ano do documento.
- A história de origem: de onde veio, o que faltava, o que marcou.
- Dois ou três episódios concretos da juventude — **com cena**, não com adjetivo.
- Os momentos em que ouviu um "não" e não aceitou (viram as tensões).
- O que ela ama, no que é boa, como gosta de contribuir, onde se realiza.
- O legado que quer deixar, na frase dela.
- Fotos: dela, do lugar de origem, dos pais, dos produtos e dos ambientes.

O material bruto sempre vem em adjetivo ("ela é determinada"). O trabalho é
trocar cada adjetivo por um fato com cena — é o fato que revela o padrão; o
adjetivo só o nomeia depois.
