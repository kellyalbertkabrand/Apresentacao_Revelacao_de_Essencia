---
name: "brand-book-ka"
description: "Monta o brand book (manual de marca) de um cliente do KA Inteligência para Marcas no modelo medido no Brand Book do Lucas Martini — 5 capítulos, 32 páginas, grade de duas colunas, trilho vertical, paleta e tipografia do cliente — e entrega em PPTX editável e PDF. USE SEMPRE que a Kelly pedir brand book, brandbook, manual de marca, manual de identidade, guia de marca, book da marca, ou pedir para adaptar/ajustar/revisar um brand book já feito. Também quando disser 'no modelo do Lucas', 'igual ao brand book do Lucas Martini' ou 'manual da marca X'."
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

## 1. Fluxo

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

## 2. O roteiro: 5 capítulos, 32 páginas

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

## 3. A grade

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

## 4. A paleta é parâmetro

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

## 5. A tipografia é do cliente

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

Duas regras:

- **O peso vem do nome da fonte**, nunca de negrito sintético. Por isso cada
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

## 6. Os dezoito arquétipos

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

## 7. Fotografia e marca d'água

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

## 8. A voz: terceira pessoa

Vale a regra do CLAUDE.md, inteira. Nada de "nossa origem", "nossos
valores", "assumimos responsabilidade". O mesmo arquivo precisa servir para
apresentar a marca a um sócio, a um candidato ou ao mercado: em terceira
pessoa ele afirma; na primeira, ele desabafa.

Duas exceções, e só estas duas: **o manifesto** (é o gênero em que a marca
fala) e **a fala de exemplo** numa página de tom de voz.

**O manifesto vai em caixa baixa**, não em versal. Pedido da Kelly em
novembro/2026: em caixa alta não lê, e manifesto é para ler.

---

## 9. O que já custou rodada

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

## 10. A entrega

Em poucas linhas: o que foi feito, o que mudou desde a última versão e o que
a Kelly precisa conferir ou decidir. Sempre `.pptx` **e** `.pdf`.

Se alguma fonte oficial ficou de fora por licença, dizer **nessa mesma
mensagem** — qual é, por quê, o que entrou no lugar e quanto custa trocar.
