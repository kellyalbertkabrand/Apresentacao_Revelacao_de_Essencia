# SISTEMA VISUAL KA

Padrão de layout de **todas** as apresentações do KA · Inteligência para Marcas.
Vale para qualquer tipo de documento — Revelação de Essência, Base Estratégica,
Plano de Comunicação, diagnóstico, proposta. O que muda de um tipo para outro é
o **roteiro** (quais páginas, em que ordem, com que conteúdo), nunca a
aparência.

O motor está em [`ka_layout.py`](ka_layout.py). Ele não conhece conteúdo
nenhum: oferece a grade, a tipografia, os arquétipos de página e os assets.
Cada modelo de apresentação importa daqui e monta o seu próprio roteiro.

---

## 1. O princípio

O sistema é editorial, não dashboard. Três decisões sustentam isso e nenhuma
delas é negociável:

1. **O filete organiza a página, não a caixa.** Uma linha de 0,012" separa
   blocos. Cartão com fundo só quando o bloco é, de fato, um destaque isolado.
   Encher a página de caixinhas foi exatamente o que a Kelly rejeitou como
   "grosseiro".
2. **A hierarquia vem da escala e do ar, não do peso.** Título grande em
   **CAIXA ALTA e peso leve** — a força vem do tamanho e do espaço, nunca do
   negrito. Títulos de página e nomes de seção são sempre em caixa alta.
3. **Um único acento quente.** O terracota `#A9724A` aparece em filetes de
   1,3", pontos de lista e numerais de seção. Nunca em área grande.

---

## 2. Formato e grade

| | |
|---|---|
| Formato | 16:9 — **20" × 11,25"** |
| Painel | recuo de **1,10"** nas laterais e no topo; base em **9,60"** |
| Margem de texto | esquerda **2,20"**, limite direito **17,80"** (largura útil 15,60") |
| Eyebrow | y = **1,95"** |
| Título (H1) | y = **2,55"** |
| Rodapé | y = **10,32"** — fora do painel, sobre a textura |
| Grade de 4 colunas | coluna **3,35"**, intervalo **0,55"** |

> **Regra de ouro:** o fundo do painel é **9,60"**. A última caixa de texto de
> qualquer página começa em **9,15"** no máximo. O `conferir.sh` verifica
> isso automaticamente (ver §7).

Todo slide tem a textura de ondas no fundo, **a 32% de opacidade** — chapada,
ela rouba o contraste do texto e acaba com a leveza do padrão. Por cima vem o
painel claro de cantos arredondados (raio 0,18") onde o conteúdo vive. Abertura, capa, fecho e
as páginas com foto sangrando dispensam o painel.

---

## 3. Paleta

| Uso | Hex | Constante |
|---|---|---|
| Painel claro | `#F8F7F2` | `PAINEL` |
| Títulos e frases | `#1C1C1A` | `TINTA` |
| Corpo de texto | `#6B6B66` | `CORPO` |
| Eyebrow, legenda, rodapé | `#A5A49F` | `CLARO` |
| Filetes | `#DFDDD7` | `FIO` |
| Acento terracota | `#A9724A` | `ACENTO` |

---

## 4. Tipografia

**Fonte única: Outfit**, nas variantes nomeadas que vêm incorporadas no arquivo
de referência. Nada de Calibri, Playfair ou IBM Plex.

A família de texto é a **Outfit 1**. No arquivo final da Kelly são **576**
trechos em `Outfit 1 Light` contra 4 em `Outfit 2 Light`: a Outfit 2 sobrou no
eyebrow e na assinatura da capa. A primeira transcrição inverteu as duas
famílias — era daí que vinha a maior diferença visual entre o gerado e o
padrão dela, maior que qualquer tamanho.

| Constante | Nome no OOXML | Uso |
|---|---|---|
| `LIGHT` | `Outfit 1 Light` | títulos, corpo, frases — o peso padrão |
| `REG` | `Outfit 1` | texto neutro e data |
| `SEMI` | `Outfit 1 Semi-Bold` | rótulos e numerais |
| `BOLD` | `Outfit 1 Bold` | título da capa, nome da marca no rodapé |
| `MEDIO` | `Outfit 1 Medium` | — |
| `ULTRA` | `Outfit 1 Ultra-Bold` | título do sumário |
| `SANS` | `Outfit 2` | eyebrow |
| `SANS_LIGHT` | `Outfit 2 Light` | assinatura do método, na capa |
| `SANS_SEMI` | `Outfit 2 Semi-Bold` | nome do método dentro da assinatura |

> **O peso vem do NOME da fonte, nunca de `b="1"`.** `font.bold = False` está
> fixado em `txt()`. Negrito sintético sobre a Outfit engrossa as curvas e
> deixa o texto pastoso.
>
> O arquivo do Canva faz o contrário: aplica `b="true"` por cima de
> `Outfit 1 Medium` no título da capa. Aqui o mesmo peso vem da `Outfit 1
> Bold`, com os 3 pt de espacejamento que dão o ar da capa.

### As fontes estão no repositório

`padrao-ka/fontes/` guarda as doze faces, extraídas do próprio arquivo da
Kelly (lá elas vão embarcadas em EOT dentro do `.pptx`). Cada arquivo foi
renomeado para se chamar, na tabela de nomes, exatamente como o Canva o chama
— `Outfit 1 Light`, `Outfit 1 Semi-Bold` e por aí. Sem isso o LibreOffice não
casa o nome composto, cai na mesma face para todos os pesos e a prévia mente.

```bash
padrao-ka/instalar-fontes.sh      # uma vez por máquina
```

Escala fechada — **não inventar tamanhos fora desta tabela**:

| Constante | pt | Onde |
|---|---|---|
| `T_DIVISOR` | 94 | nome da seção, na virada de tema |
| `T_SUMARIO` | 78 | título do sumário, acima do painel |
| `T_CAPA` | 75 | título da capa |
| `T_DISPLAY` | 74 | frase grande que abre uma etapa |
| `T_H1` | 42 | título de página |
| `T_SUBCAPA` | 30 | subtítulo da capa |
| `T_FRASE` | 29 | aspas de citação |
| `T_ASSINATURA` | 26,8 | assinatura do método, na capa |
| `T_LEAD` | 24 | linha de abertura |
| `T_MEDIO` | 23 | frase forte, item de lista forte |
| `T_CORPO` | 21 | corpo |
| `T_DATA` | 19,5 | data, na capa |
| `T_RODAPE` | 17 | rodapé |
| `T_MINI` | 17 | legenda miúda |
| `T_ROTULO` | 14 | eyebrow e rótulo em caixa alta |

> **Esta tabela foi MEDIDA, não estimada.** O arquivo final da Kelly reporta
> a página em 1920 px para 20", ou seja 96 px/in, então `pt = px × 0,75`.
>
> A primeira transcrição deste padrão chutou a escala e saiu pequena demais —
> o nome da seção vinha **34% menor**, a frase de abertura **38% menor**, o
> rodapé **29% menor**, o corpo **19% menor**. Decks gerados antes da medição
> carregam o erro.
>
> Lead, corpo, legenda e rótulo ficam no topo da faixa medida (o arquivo
> dela usa 22/18 numa página e 24/19 noutra): em projeção o corpo menor
> não se lê.

### A escala legada

`Deck(..., escala="legada")` traz de volta os tamanhos antigos. Existe por um
motivo só: o roteiro fixo em `modelos/revelacao-de-essencia/` foi diagramado à
mão contra eles, e trocar a escala sem rediagramar estoura todas as páginas.
**Não usar em material novo.**

---

## 5. Os sete arquétipos de página

| | Método | O que é |
|---|---|---|
| **A1** | `abertura()` | Logos KA + parceiro sobre a textura. Sem painel. Abre o documento. |
| **A2** | `capa(titulo_linhas, subtitulo, assinatura, data)` | Título em caixa alta, filete de acento, barra de assinatura (logo · método · data). |
| **A3** | `pagina(eyebrow, titulo)` | Página de conteúdo: eyebrow, título e filete. O arquétipo de trabalho. |
| **A4** | `divisor(numero, nome)` | Virada de tema: numeral, nome em caixa alta leve, filete atravessando. Nada mais. |
| **A5** | `com_foto(eyebrow, titulo, foto, lado, fatia)` | Página partida: foto sangrando numa lateral, texto na outra. Devolve `(slide, x, largura)`. |
| **A6** | `manifesto(eyebrow, linhas, apoio)` | Página de silêncio: uma frase grande e muito espaço. |
| **A7** | `fecho(frase, parceiro)` | Agradecimento e assinatura. Sem painel. |

A foto **alterna de lado** a cada aparição — o ritmo esquerda/direita é o que
impede a apresentação de virar uma sequência monótona.

### Primitivas

`slide()` · `bloco()` · `fio()` · `fio_v()` · `ponto()` · `anel()` ·
`caixa()` · `par()` · `txt()` · `texto()` · `foto()` · `logo()` ·
`eyebrow()` · `rotulo()` · `titulo()` · `rodape()` · `salvar()`

Notas:
- `foto()` faz center-crop sem distorcer. Sangrando na borda vai sem raio;
  contida, ganha canto arredondado.
- `anel()` é círculo de contorno fino — **nunca preenchido**.
- O raio do `roundRect` no OOXML é fração do lado menor, por isso `bloco()`
  converte polegadas em `adj` com `min(0.5, raio / min(w, h))`. Sem isso,
  formas de tamanhos diferentes saem com raios visualmente diferentes.

---

## 6. Assets

Em [`assets/`](assets), extraídos do arquivo aprovado pela Kelly:

| Arquivo | O que é |
|---|---|
| `textura-ondas.jpeg` | relevo de ondas, fundo de todos os slides (2500×1750) |
| `logo-ka.png` | monograma KA do rodapé |
| `logo-kelly-albert.png` | assinatura KELLY ALBERT, abertura e fecho |
| `logo-vm-rocks.png` | assinatura do parceiro VM Rocks Design |
| `traco.png` | traço manual do canto da capa |
| `simbolo-ikigai.png` / `.svg` | diagrama de círculos do Ikigai |

`referencia/PADRAO-KA-revelacao-de-essencia.pptx` é o arquivo aprovado pela
Kelly. **Nenhum slide dele é aproveitado** — ele existe só para herdar o tema
e as fontes Outfit incorporadas. O `Deck.__init__` limpa todos os slides
(inclusive derrubando as relações de `notesSlide` que o export do Canva
pendura em `presentation.xml`, sem o que o pacote sai com partes duplicadas).

---

## 7. Como verificar antes de entregar

LibreOffice Impress está instalado e **funciona**. Há um script pronto:

```bash
python3 modelos/<modelo>/gerar.py clientes/<cliente>     # gerar
padrao-ka/conferir.sh clientes/<cliente>/<arquivo>.pptx  # conferir
```

Ele converte para PDF, mede a caixa real de cada palavra com
`pdftotext -bbox` e aponta o que vazou, slide por slide. Também deixa a
prévia em PNG num diretório temporário, que ele informa no fim — vale olhar,
porque o teste pega texto fora do painel mas não pega filete encostando em
texto.

**Por que medir e não confiar no código:** as alturas declaradas no
python-pptx são só um chute. O texto quebra em mais linhas do que se espera e
vaza sem avisar. `pdftotext -bbox` dá a caixa **como renderizada** — é a única
maneira honesta de saber.

Critério: nenhuma palavra pode ter `yMax > 691,2 pt` (= 9,60") com
`yMin < 728 pt` (o rodapé legitimamente fica abaixo do painel).

A prévia só diz a verdade com as fontes instaladas
(`padrao-ka/instalar-fontes.sh`). Sem elas o LibreOffice cai na DejaVu Sans,
que é mais larga: a conferência acusa vazamento onde não há.

### A quebra de linha é medida, não estimada

`linhas()` repete, palavra por palavra, a quebra que o PowerPoint vai fazer —
medindo cada palavra na própria `Outfit 1 Light` com 3% de folga. Contar
caractere, como a primeira versão fazia, trata "iii" e "MMM" como a mesma
coisa e erra até 15%: páginas inteiras eram espremidas à toa, e outras
vazavam. Sem a fonte no disco o cálculo cai na conta por caractere, que é
grosseira mas nunca subestima.

Quando o texto ainda assim não cabe, o build **avisa** em vez de encolher a
fonte abaixo de 92%: a saída é cortar texto ou quebrar a página em duas.
