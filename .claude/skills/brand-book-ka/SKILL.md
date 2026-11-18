---
name: "brand-book-ka"
description: "Monta o brand book (manual de marca) de um cliente do KA Inteligência para Marcas no modelo medido no Brand Book do Lucas Martini — 5 capítulos, 32 páginas, grade de duas colunas, trilho vertical, paleta e tipografia do cliente — e entrega em PPTX editável e PDF. USE SEMPRE que a Kelly pedir brand book, brandbook, manual de marca, manual de identidade, guia de marca, book da marca, ou pedir para adaptar/ajustar/revisar um brand book já feito. Também quando disser 'no modelo do Lucas', 'igual ao brand book do Lucas Martini' ou 'manual da marca X'. Monta pelas duas vias: pelo repositório (ka_brandbook.py, PPTX+PDF) ou como artefato do tipo Slides em qualquer conversa, com a mesma grade e a mesma escala."
---

# Brand Book KA — o modelo do Lucas Martini

Um brand book **não é apresentação. É manual.** Quem abre não está
assistindo: está consultando. Por isso a diagramação é outra — paginação no
trilho da margem, capítulos numerados, páginas inteiras de cor, e a
informação em duas colunas: o título à esquerda, o conteúdo à direita.

E é o **único documento do padrão KA que veste a identidade do cliente** —
paleta, logotipo **e tipografia** — não a do escritório.

Escreva sempre em português.

---

## 0. Duas vias

O brand book se monta de dois jeitos, e o que muda é só o montador — **o
roteiro, a grade e a escala são os mesmos**.

| Via | Quando | Montador | Entrega |
|---|---|---|---|
| **A · Repositório** | há o repositório `apresentacoes/` | `padrao-ka/ka_brandbook.py` | `.pptx` editável + `.pdf` |
| **B · Artefato** | qualquer conversa do claude.ai | artefato do tipo **Slides** | página publicada, link, exporta PPTX/PDF |

A via A é a entrega para o cliente: PPTX editável, medido na própria fonte,
conferido pelo pé. A via B é para **ver, revisar e compartilhar por link** —
e é a única possível quando não há repositório.

Quando houver as duas, a via A manda: o arquivo que o cliente recebe é o
`.pptx`.

---

## 1. Via A — o repositório

1. **Ler `padrao-ka/BRAND-BOOK.md`** — a grade, os 18 arquétipos e a paleta
   como parâmetro. Este arquivo é o contrato; a skill é o roteiro.
2. **Criar `clientes/<cliente>/brandbook.py`**, copiando
   `clientes/lucas-martini/brandbook.py` como referência viva (32 páginas,
   aprovado). Só conteúdo — a diagramação está no motor.
3. **Pôr os assets** em `clientes/<cliente>/assets/`:
   `marca/original/` (as versões do logo), `aplicacoes/`, `capa/`,
   `instagram/`, `grafismos/` e as fotos do cliente.
4. **Gerar**:
   ```bash
   python3 clientes/<cliente>/gerar.py brandbook
   ```
5. **Conferir — obrigatório**, antes de qualquer entrega:
   ```bash
   padrao-ka/conferir.sh clientes/<cliente>/<arquivo>.pptx --fundo 10.10
   python3 padrao-ka/conferir_voz.py clientes/<cliente>/brandbook.py
   ```
   E **olhar as páginas**: gerar o contato em PNG do PDF e ler as 32. O
   conferidor pega vazamento pelo pé; colisão de blocos e palavra cortada no
   meio só o olho pega.
6. **Commitar** no branch de trabalho e entregar o `.pptx` **e** o `.pdf` com
   `SendUserFile`.

Nunca entregar sem rodar o passo 5. Nunca diminuir corpo de fonte para
caber: **cortar texto** (regra do CLAUDE.md).

---

## 2. Via B — o artefato

Mesmo roteiro, mesma grade, mesma escala — traduzidos para a tela. A página
do artefato é **1920 × 1080 px**, e a conversão é exata: a página do brand
book tem 20", logo **1" = 96 px** e **1pt = 4/3 px**. Nada é reinventado.

### Começar

Publicar com `type_url` do tipo **Slides**
(`https://claude.ai/artifact/8jTsAFQMFDb2oA8MsPJ2eL`), um `title`, sem
arquivos, `auto_open: "after_first_write"`. O resultado traz a `url` e as
instruções do tipo; seguir dali.

**Sem design system.** O design system KA é a identidade do *escritório*, e
o brand book é o único documento que veste a do **cliente**. Então
`designSystems: []`, sem `project/ds/`, e a paleta do cliente declarada à
mão no `project/deck.css`. Dizer isso à Kelly em uma linha na entrega — é
escolha, não esquecimento.

### Os arquivos

- `project/deck.json` — `"v":5`, `lists:"css"`, `format` apontando para
  `project/deck.css`, `order` com os 32 ids, `sections` com os cinco
  capítulos, `cover` na capa e `faces` com as três fontes.
- `project/deck.css` — as variáveis da paleta e a grade. Uma vez só.
- `project/slides/<id>.html` — um `<section>` por página.

Ids legíveis, que digam a página: `capa`, `para-que-serve`, `conteudo`,
`cap1-marca`, `o-que-e`, `crenca`, … Assim o link `#slide-7` e a conversa
sobre o documento falam a mesma língua.

### As fontes

EB Garamond e DM Sans **estão no Google Fonts** — na tela elas renderizam
de verdade, o que o PPTX não consegue com as oficiais:

```json
"faces": {
  "eb-garamond": {"family": "EB Garamond",
    "href": "https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400..700&display=swap"},
  "dm-sans": {"family": "DM Sans",
    "href": "https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300..700&display=swap"},
  "outfit": {"family": "Outfit",
    "href": "https://fonts.googleapis.com/css2?family=Outfit:wght@300..700&display=swap"}
}
```

**Aqui o peso vem do `font-weight`, não do nome da fonte.** É a única regra
do padrão que se inverte entre as duas vias, e inverte por um motivo: no
PPTX cada peso precisa ser uma família própria porque o PowerPoint
sintetiza negrito; no navegador a fonte é variável e o peso é real.

| Papel | Família | `font-weight` |
|---|---|---|
| Título de página, capítulo | EB Garamond | 400 · 600 no nome do capítulo |
| Corpo | DM Sans | 300 |
| Rótulo, destaque, numeração | DM Sans | 600 |
| Assinatura do logotipo | Outfit | 400, caixa alta, `letter-spacing: 4px` |

### A grade, em pixels

```css
:root{
  --escuro:#4A534E; --escuro2:#5A635E; --claro:#F6F4EF; --areia:#CEC3B5;
  --tinta:#2C322E;  --corpo:#5F6661;   --suave:#9AA09A; --fio:#DCD8CE;
  --acento:#AE8C4E; --acento-escuro:#E3C88B;
  --sobre-escuro:#F2F0E9; --corpo-escuro:#D6DAD3;
}
section{
  padding:182px 173px 110px 110px;     /* y título 182 · pé útil 970 */
  display:flex; gap:211px;             /* 110 + 720 + 211 = 1041 */
  background:var(--claro); color:var(--corpo);
  font:300 28px/1.45 "DM Sans";
}
.esq{width:720px}                       /* título e resumo */
.dir{width:706px; margin-top:15px}      /* y corpo 197 */
```

| | Polegada | Pixel |
|---|---|---|
| Margem esquerda | 1,15" | **110** |
| Margem direita | 18,20" | **1747** (173 da borda) |
| Coluna da esquerda | 1,15" · 7,50" | 110 · **720** |
| Coluna da direita | 10,85" · 7,35" | 1041 · **706** |
| Primeira linha do título | 1,90" | **182** |
| Primeira linha da coluna direita | 2,05" | **197** |
| Trilho vertical | 19,25" | **1848** |
| **Pé útil** | 10,10" | **970** |

Altura útil abaixo do título: **788 px**. O tipo Slides sugere nada abaixo
de y 920 porque supõe uma faixa de rodapé; o brand book não tem rodapé — a
paginação vive no trilho da direita — então o piso é 970, o mesmo do
impresso.

### O trilho

**`writing-mode` não sobrevive** no tipo Slides. O trilho é um `<p>` fixado
e girado, com a origem no canto superior esquerdo — assim o texto cresce
para cima a partir do pé, e a caixa fica onde se manda:

```css
.trilho{
  position:absolute; left:1824px; top:946px; width:560px; margin:0;
  transform-origin:left top; transform:rotate(-90deg);
  font:500 24px/1 var(--sans); letter-spacing:3px; color:var(--suave);
}
```

```html
<p class="trilho"><span class="folio">12</span>&#160;&#160;&#160;&#160;BRANDBOOK <span class="barra">|</span> LUCAS MARTINI</p>
```

Uma linha só. Girada, o primeiro caractere cai embaixo — é por isso que o
número vem primeiro na marcação. **Nas páginas escuras o trilho não
existe**: nem nome, nem número.

### O piso de 24 px

O tipo Slides não aceita texto abaixo de 24 px, e a escala impressa tem três
tamanhos menores que isso. Não é limitação: é a diferença entre os meios. Um
manual se lê a um palmo; um artefato, a um metro. Então o miúdo sobe para o
piso, e **só o miúdo**:

| Elemento | pt no PPTX | px direto | **px na tela** |
|---|---|---|---|
| Nome do capítulo | 70 | 93 | 93 |
| Numeral do capítulo | 58 | 77 | 77 |
| Frase da página de silêncio | 52 | 69 | 69 |
| Título de página | 45 | 60 | 60 |
| Numeral de pilar | 44 | 59 | 59 |
| Nome de coluna, de versão | 26 | 35 | 35 |
| Linha de abertura | 22 | 29 | 29 |
| **Corpo** | 21 | 28 | **28** |
| Nota miúda | 16,5 | 22 | **24** ← piso |
| Eyebrow | 12,5 | 17 | **24** ← piso |
| Trilho e paginação | 11,5 | 15 | **24** ← piso |

Nenhum outro tamanho muda. Mexer no corpo ou no título para "caber melhor"
quebra a relação com a via A, e aí os dois documentos deixam de ser o mesmo
documento.

### Imagens

Logo, fotos, mockups e grafismos entram como **asset** (`publish` com
`asset: true`) e o `<img src>` recebe a `url` que o upload devolveu, tal e
qual. Nunca `data:` URI, nunca caminho local, nunca link de fora.

Foto de virada de capítulo: `object-fit: cover`, metade direita da página,
e o **rosto nunca cortado** — conferir olhando, que aqui não há
`conferir_rostos.py`.

### Ritmo da montagem

`project/deck.json`, `project/deck.css` e a capa primeiro, numa publicação
só. Depois **três páginas por mensagem**, na ordem do `order`. São 32
páginas: onze mensagens. Não tentar mandar tudo de uma vez.

Referência viva: **`clientes/lucas-martini/artefato/`** — as 32 páginas do
Lucas nesta via, com o `deck.css` inteiro e o conferidor.

### Quando não couber

Os mesmos dois ajustes do motor, agora em CSS:

```css
.dir.alto{top:155px}                     /* o y_direita: a coluna sobe quando a lista e longa */
.lista.apertada .item{padding:17px 0}    /* o passo aperta numa lista de sete linhas */
```

Primeiro sobe a coluna, depois aperta o passo. **Cortar texto** só depois
dos dois, e **nunca** diminuir o corpo.

Numa caixa com borda e largura fixa, `box-sizing:border-box` — sem ele a
borda soma 1 px e a última coluna estoura a margem.

### Conferir

Não há `conferir.sh` aqui. O que substitui — e
`clientes/lucas-martini/artefato/ver.js` já traz pronto: abre cada página
no Chromium com as fontes de verdade, tira o PNG e acusa o que passa de
970 ou sai da margem:

1. **Pré-visualizar** as páginas de risco — as de muito texto (02, 05, 09,
   12, 21, 30) e as de montagem fina (20, 23, 26, 31).
2. **Medir a altura à mão** antes de escrever: título ≈ tamanho × linhas ×
   1,1; parágrafo = linhas × 28 × 1,45. Passou de 788 px abaixo do título?
   **Cortar texto**, nunca diminuir o corpo.
3. **O texto quebra só em espaço**: dimensionar a caixa pela palavra mais
   longa (≈ 0,6 × tamanho por caractere). É o mesmo erro que no PPTX
   cortava `responsabilid/ade`.

---

## 3. O roteiro: 5 capítulos, 32 páginas

É este o modelo. A ordem é a tese do Método Marca com Essência ©: a marca
antes do público, o público antes da voz, a voz antes do visual, e o
manifesto por último porque só faz sentido depois de tudo.

| # | Página | Arquétipo |
|---|---|---|
| 01 | Capa — a arte da marca, `BRAND BOOK` e o ano | `capa` |
| 02 | Para que serve este brand book | `texto` |
| 03 | Conteúdo — os cinco capítulos | `indice` |
| **04** | **Virada · 01 A MARCA** | `divisor` |
| 05 | O que esta marca é | `texto` |
| 06 | A crença fundadora (página escura, de silêncio) | `declaracao` |
| 07 | Essência da marca — essência · razão de ser · causa | `colunas` |
| 08 | Golden Circle — por quê, como e o quê | `colunas` |
| 09 | Posicionamento | `texto` |
| 10 | Arquitetura — as frentes de atuação | `colunas` |
| **11** | **Virada · 02 PÚBLICO E TERRITÓRIO** | `divisor` |
| 12 | Para quem a marca fala | `lista` |
| 13 | Os territórios de comunicação | `lista` |
| 14 | Os cinco pilares | `numerais` |
| **15** | **Virada · 03 VOZ** | `divisor` |
| 16 | Personalidade — postura, relação, forma | `colunas` |
| 17 | Tom de voz — em vez de / prefere | `pares` |
| 18 | As palavras da marca — verbos, próprias, nunca usar | `colunas` |
| **19** | **Virada · 04 IDENTIDADE VISUAL** | `divisor` |
| 20 | As versões da marca | `marca` |
| 21 | O que preserva a marca — os usos | `lista` |
| 22 | A paleta | `paleta` |
| 23 | A tipografia | `tipografia` |
| 24 | A marca aplicada | `aplicacoes` |
| 25 | As peças | `aplicacoes` |
| 26 | A marca no Instagram | `instagram` |
| 27 | Os grafismos | `aplicacoes` |
| **28** | **Virada · 05 MANIFESTO** | `divisor` |
| 29 | O manifesto (página escura) | `declaracao` |
| 30 | A marca em uma página — a síntese | `lista` |
| 31 | Créditos — quem assinou o quê | `creditos` |
| 32 | Fecho — só a marca do cliente | `creditos` |

**As viradas de capítulo levam fotografia do cliente** em tela cheia à
direita, sem paginação e sem o nome do documento no trilho — a página de
cor é respiro, não formulário.

Adaptar o roteiro é legítimo: cliente sem Instagram perde a 26, cliente sem
peças impressas perde a 25. **Tirar capítulo inteiro, não.** São cinco.

---

## 4. A grade

Em polegadas, que é a medida da via A. Em pixel, na via B — a tabela de
conversão está em **§2**.

| | Medida |
|---|---|
| Página | 20" × 11,25" (16:9) |
| Margem | 1,15" à esquerda · 18,20" à direita (`ML`, `MR`) |
| Coluna da esquerda | x 1,15" · largura 7,50" — título e resumo |
| Coluna da direita | x 10,85" · largura 7,35" — o conteúdo |
| Primeira linha do título | y 1,90" (`Y_TITULO`) |
| Primeira linha da coluna direita | y 2,05" (`Y_CORPO`) |
| Trilho vertical | x 19,25" (`X_TRILHO`) |
| **Pé útil** | **10,10"** — nada de texto abaixo disto |

O **trilho vertical** na margem direita é o que faz o documento parecer
manual: o nome do documento e da marca de pé, lendo de baixo para cima, e o
número da página no pé do trilho. **Nas páginas escuras o trilho some** —
sem nome, sem número.

Escala tipográfica fechada — não inventar tamanho fora dela:

| Elemento | pt |
|---|---|
| Título de página, caixa alta | 45 |
| Nome do capítulo, na virada | 70 |
| Numeral do capítulo | 58 |
| Frase da página de silêncio | 52 |
| Numeral de pilar | 44 |
| Nome de coluna, de pilar, de versão | 26 |
| Linha de abertura da coluna esquerda | 22 |
| **Corpo** | **21** |
| Nota miúda | 16,5 |
| Eyebrow e paginação | 12,5 · 11,5 |

---

## 5. A paleta é parâmetro

Entra como dicionário no `brandbook.py` do cliente. As doze chaves:

```python
PALETA = {
    "escuro": "4A534E",         # a cor da marca — capa, capítulo, assinatura
    "escuro2": "5A635E",        # o mesmo tom acima, para volume
    "claro": "F6F4EF",          # papel
    "areia": "CEC3B5",          # superfície de apoio
    "tinta": "2C322E",          # títulos
    "corpo": "5F6661",          # corpo de texto
    "suave": "9AA09A",          # rótulo apagado
    "fio": "DCD8CE",            # filetes
    "acento": "AE8C4E",         # acento sobre papel
    "acento_escuro": "E3C88B",  # acento sobre a cor da marca
    "sobre_escuro": "F2F0E9",   # texto sobre a cor da marca
    "corpo_escuro": "D6DAD3",   # corpo sobre a cor da marca
}
```

Toda página aceita `tom`: `claro`, `areia` ou `escuro`.

**Texto sobre fundo escuro precisa de mais contraste do que parece.** O
`corpo_escuro` do Lucas foi aberto de `C8CCC6` para `D6DAD3` justamente
porque a leitura não fechava na projeção.

---

## 6. A tipografia é do cliente

Três camadas, e a divisão nunca muda:

| Camada | O que compõe | Constantes em `ka_brandbook.py` |
|---|---|---|
| **Display** | título de página, numeral e nome de capítulo | `TIT`, `TIT_SEMI` |
| **Texto** | corpo, rótulo, legenda, numeração | `LIGHT`, `REG`, `SEMI`, `BOLD` |
| **Assinatura** | a linha que acompanha o logotipo | `ASSINATURA` |

Trocar a tipografia é mudar esses nomes e pôr os `.ttf` em
`padrao-ka/fontes/`. **A medida refaz sozinha** — `F_CORPO`, `F_CORPO_SEMI`
e `F_TIT` dizem com que arquivo cada camada é medida. Nada muda de lugar na
grade. Depois, sempre:

```bash
padrao-ka/instalar-fontes.sh
```

Duas regras — a primeira **só na via A**:

- **No PPTX o peso vem do nome da fonte**, nunca de negrito sintético. No
  artefato é o contrário: `font-weight`, porque a fonte do navegador é
  variável e o peso é real (§2). Por isso cada
  peso é uma família própria (`DM Sans Light`, `DM Sans SemiBold`). Se o
  nome não existe no sistema, o LibreOffice cai numa fonte qualquer e a
  prévia mente — conferir com `pdffonts` depois de gerar.
- **A fonte que o escritório não pode licenciar é nomeada, não usada.** A
  licença do Canva não sai do Canva: não dá para exportar o `.ttf` nem usar
  num PPTX. Então ela entra **nomeada** na página de tipografia — é a
  oficial da marca, o manual precisa dizer isso — e o documento sai composto
  na mais próxima que se pode licenciar. Dizer isso à Kelly na entrega, com
  o custo da licença, e deixar claro que trocar depois é soltar o `.ttf` na
  pasta.

**Lucas Martini:**

| Camada | Oficial | No arquivo |
|---|---|---|
| Display | Allrounder, Identity Letters | EB Garamond |
| Texto | DM Sans | DM Sans — a própria (OFL) |
| Assinatura | Codec Pro, Zetafonts | Outfit 1 |

---

## 7. Os dezoito arquétipos

Todos aceitam `olho` (o rótulo de acento acima do título) e `tom`.

| `tipo` | O que é | Campos |
|---|---|---|
| `capa` | a arte ou a cor da marca, o nome do documento e a edição | `titulo`, `edicao`, `foto`, `logo`, `logo_largura`, `y_titulo` |
| `indice` | capítulo, nome e legenda, separados por filete | `itens`: `(num, nome, legenda)` |
| `divisor` | virada de capítulo: numeral, nome, foto em tela cheia | `numero`, `nome`, `legenda`, `foto`, `foco`, `corte` |
| `texto` | título à esquerda, parágrafos à direita | `titulo`, `resumo`, `marcado`, `paragrafos` |
| `lista` | linhas com seta, separadas por filete | `titulo`, `resumo`, `rotulo`, `itens`, `fecho`, `y_direita` |
| `colunas` | 2–4 colunas de `(rótulo, nome, texto)` | `colunas`, `fecho` |
| `numerais` | pilares numerados 01…05 | `itens`: `(nome, texto)` |
| `declaracao` | a página de silêncio: uma frase, muito ar | `linhas`, `apoio`, `tam`, `agua`, `caixa_alta`, `espaco` |
| `pares` | em vez de / prefere — o que a marca risca e o que assina | `pares` |
| `meia` | meia página de cor, meia de imagem | `linhas`, `foto`, `corte`, `lado` |
| `paleta` | amostras de cor com código e uso | `cores`: `(nome, hex, uso)` |
| `marca` | versões do logo, cada uma no seu fundo | `versoes`: `(nome, arquivo, fundo, legenda)` |
| `tipografia` | espécimes, cada um na sua fonte | `familias`: `(nome, fonte, amostra, uso[, spc])`, `nota`, `passo`, `respiro` |
| `aplicacoes` | a marca nas peças: uma foto grande ou uma fileira delas | `fotos`: `(arquivo, legenda)`, `texto`, `nota`, `y` |
| `instagram` | perfil num celular, destaques e feed | `texto`, `icones`, `celular`, `posts` |
| `creditos` | a marca no alto e, embaixo, as assinaturas de quem fez | `marca`, `olho`, `logos`: `(arquivo, largura, legenda)`, `gap`, `tam_mais`, `disposicao` |
| `fecho` | logo, frase e assinatura | `frase`, `assinatura` |
| `abertura` · `capa_ka` | heranças do padrão de apresentação | — |

### Negrito e riscado

O conteúdo marca com `**`; o riscado, que a página de vocabulário usa para o
que a marca **não** diz, com `~~`:

```python
"Use como guia antes de criar. **Marca consistente é marca reconhecida.**"
"~~Fatalidade · desespero · oportunidade imperdível~~"
```

No brand book o negrito carrega a frase que a pessoa leva embora — sem ele o
texto vira bloco cinza. Mas **só funciona enquanto for exceção**: uma frase
por página, não um parágrafo inteiro.

---

## 8. Fotografia e marca d'água

- **O rosto nunca é cortado.** Depois de trocar qualquer foto:
  ```bash
  python3 padrao-ka/rostos.py clientes/<cliente>/assets
  python3 padrao-ka/conferir_rostos.py <arquivo>.pptx clientes/<cliente>/assets
  ```
- **A foto do cliente entra de tempos em tempos** — nas viradas de capítulo.
  Um manual só com texto não convence ninguém de que a marca é de alguém.
- **A marca d'água é sombra, não ilustração**: o símbolo a 10–13% de
  opacidade, sangrando pela direita. Se der para ler, está forte demais.
- A trama de pontos (`trama.py`) é a única textura.

---

## 9. A voz: terceira pessoa

Vale a regra do CLAUDE.md, inteira. Nada de "nossa origem", "nossos
valores", "assumimos responsabilidade". O mesmo arquivo precisa servir para
apresentar a marca a um sócio, a um candidato ou ao mercado: em terceira
pessoa ele afirma; na primeira, ele desabafa.

Duas exceções, e só estas duas: **o manifesto** (é o gênero em que a marca
fala) e **a fala de exemplo** numa página de tom de voz.

**O manifesto vai em caixa baixa**, não em versal. Pedido da Kelly em
novembro/2026: em caixa alta não lê, e manifesto é para ler.

---

## 10. O que já custou rodada

Erros reais, cada um de uma entrega. Conferir antes de repetir.

- **Logotipo com placa de cor grudada.** O PNG que o cliente manda muitas
  vezes traz um retângulo da cor de fundo por baixo da arte. Render sobre
  magenta expõe; `padrao-ka/tirar_placa.py` remove. As bordas da placa
  (alpha 192/128) ficam fora do bbox detectado e deixam fantasma — usar
  `--folga`.
- **Logo fora do centro do quadrado.** `centrar()` mexe em formas, não em
  imagens: a figura precisa se chamar `marca-logo`.
- **Legenda que não descreve a imagem.** Na página de versões, escrever a
  legenda olhando a imagem, não a lista.
- **Palavra cortada no meio** (`responsabilid/ade`). O equilíbrio de linhas
  podia apertar a caixa até menos que a palavra mais larga — a conta cabia,
  o PowerPoint cortava. Hoje há piso em `equilibrio()`.
- **Parágrafo estourando a caixa por uma linha.** O negrito é mais largo que
  o leve: medir tudo no peso leve subestima. `linhas_ricas()` mede palavra a
  palavra, **cada uma no seu peso e na fonte certa**.
- **Linhas desequilibradas.** Toda caixa de mais de uma linha sai
  equilibrada — em vez de encher a primeira e largar a órfã na última, a
  caixa é apertada até o limite do mesmo número de linhas. Desligar com
  `equilibrar=False`.
- **Numeração nas páginas de cor.** Não tem. Nem nome de documento.
- **Entregar o PPTX como imagem.** Nunca. O PPTX tem que ser editável, texto
  vivo em caixa de texto.
- **Arte de capa em baixa.** 1920 × 1080 dá 96 dpi numa página de 20": serve
  para tela, fica mole impresso. Avisar e pedir a arte maior.

---

## 11. A entrega

Em poucas linhas: o que foi feito, o que mudou desde a última versão e o que
a Kelly precisa conferir ou decidir.

- **Via A**: sempre `.pptx` **e** `.pdf`, por `SendUserFile`.
- **Via B**: dizer o que a página mostra e o que falta. Nunca colar a `url`
  crua no texto.

Se alguma fonte oficial ficou de fora por licença, dizer **nessa mesma
mensagem** — qual é, por quê, o que entrou no lugar e quanto custa trocar.
