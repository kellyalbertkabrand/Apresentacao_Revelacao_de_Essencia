# Lucas Martini · Proteção & Sucessão

Duas apresentações no padrão KA, montadas pelo roteiro declarativo
([`padrao-ka/ROTEIRO-DECLARATIVO.md`](../../padrao-ka/ROTEIRO-DECLARATIVO.md)).

```bash
python3 clientes/lucas-martini/gerar.py                   # as duas
python3 clientes/lucas-martini/gerar.py revelacao         # só uma
```

Cada deck sai em **`.pptx` e `.pdf`** na própria pasta.

| Arquivo | O que é | Slides |
|---|---|---|
| `revelacao.py` | Revelação de Essência — origem identitária do fundador | 30 |
| `base_estrategica.py` | Base Estratégica da Marca — na diagramação do brand book | 18 |
| `brandbook.py` | Brand Book — a mesma base em formato de manual | 27 |
| `assets/` | as 14 fotografias | — |
| `assets/marca/` | o logotipo do Lucas, recortado com fundo transparente | — |

## O brand book

A Base Estratégica tem 30 páginas de apresentação; o brand book tem 27 de
**manual**, na diagramação do Brand Book KA 2026
([`padrao-ka/BRAND-BOOK.md`](../../padrao-ka/BRAND-BOOK.md)) e vestido com a
identidade do Lucas: verde `#4A534E`, dourado do escudo, areia e papel.

```bash
python3 clientes/lucas-martini/gerar.py brandbook
padrao-ka/conferir.sh clientes/lucas-martini/Brand-Book-Lucas-Martini.pptx --fundo 10.30
```

Nada foi inventado: cada definição vem da Base aprovada. **Duas páginas são
derivação, não transcrição**, e precisam do aval da Kelly:

1. **"As palavras da marca"** (vocabulário) — montada a partir dos
   territórios e do "nunca" da personalidade. A Base não trazia glossário.
2. **"O que preserva a marca"** (usos do logo) — regras de respiro,
   contraste, proporção e tamanho mínimo. São as regras usuais de manual,
   escritas para este escudo.

Duas observações de produção:

- **O logotipo saiu do Canva em 592 px de largura** — foi o que a API
  entregou; o download em alta resolução está bloqueado. Serve para tela e
  para o PDF; para impressão grande, trocar pelos arquivos originais em
  `assets/marca/`.
- **As fontes da marca (Allrounder e DM Sans) não estão instaladas aqui.** O
  documento está composto em Outfit, como todo o padrão KA, e a página de
  tipografia diz isso em nota. Com os arquivos das fontes, a troca é de um
  minuto.

## O que veio do arquivo final da Kelly

A capa, o sumário e a tipografia foram **medidos** no `.pptx` que ela mandou
(a VFinal da Revelação), não estimados:

| | No arquivo dela |
|---|---|
| Capa | sem painel — a textura corre de borda a borda; título 75pt em caixa alta com 3pt de espacejamento; traço no canto; barra de assinatura com quatro filetes |
| Sumário | **SUMÁRIO** em 78pt Ultra-Bold **acima** do painel; numerais terracota em 15,5pt; nome 25pt; descrição 18pt |
| Família de texto | **Outfit 1** (576 trechos em `Outfit 1 Light`) — a Outfit 2 ficou no eyebrow e na assinatura da capa |
| Corpo | lead 24pt · corpo 21pt |

### Duas diferenças conscientes

1. **A Base Estratégica vai sem rodapé** — foi o que ela marcou nas quatro
   capturas do Canva. A Revelação mantém o rodapé, como no arquivo dela.
   Trocar é uma linha: `RODAPE = False` em `base_estrategica.py`.
2. **O sumário da Base não tem descrição sob cada nome.** São nove seções
   contra as seis da Revelação: com descrição, o índice fecharia o painel sem
   ar nenhum. Se ela preferir a descrição, o caminho é reduzir o número de
   seções, não espremer as linhas.

---

## A edição

A **Revelação** tinha 63 slides e dizia o mesmo que estes 30: cada descoberta
vinha anunciada numa página, desenvolvida na seguinte e repetida numa terceira
em caixa alta. Aqui cada descoberta ocupa **uma página só** — a afirmação, a
evidência e a leitura juntas. Nenhuma ideia saiu; o que saiu foi a repetição.

| Seção | Antes | Agora |
|---|---|---|
| Abertura e método | 6 | 4 |
| 01 A origem | 7 | 3 |
| 02 As tensões | 11 | 4 |
| 03 Os padrões | 5 | 2 |
| 04 O Ikigai | 13 | 3 |
| 05 A essência | 8 | 3 |
| 06 A marca | 6 | 2 |
| Divisores, capa, sumário, fecho | 7 | 9 |

As quatro páginas separadas de Paixão, Profissão, Missão e Vocação viraram
uma só — que é o que o Ikigai é: os quatro encontros numa página.

## A Base Estratégica foi refeita na diagramação do brand book

Depois de ver os slides do Brand Book KA 2026, a Kelly pediu outro padrão de
página para **todas** as apresentações:

> Título e um bloco de texto. Título e um bloco de texto. Não quero um texto
> pequeno, uma linha, outro texto embaixo.

A Base passou a usar o motor do brand book
([`padrao-ka/BRAND-BOOK.md`](../../padrao-ka/BRAND-BOOK.md)): título à
esquerda com o filete, bloco de texto à direita, papel limpo, só a paginação
no alto. **18 páginas**, com o conteúdo que ela escreveu, na ordem dela — a
essência em 01 e o Lucas em 02.

Três decisões de montagem, para ela conferir:

1. **Sem páginas de separação.** O título de cada página já é o nome do tema;
   um separador com o mesmo nome seria repetição. Ligar é uma linha.
2. **Três páginas viraram colunas** (causa/liderança/tribo, arquétipos,
   Golden Circle, arquitetura) — é o arranjo da página de arquétipos do brand
   book dela. Nos rótulos dessas colunas há uma síntese de duas ou três
   palavras feita a partir do texto dela ("Preparar antes", "Enxergar
   antes"), para o nome da coluna caber em caixa alta.
3. **As marcas de origem saíram.** "Identidade Verbal - Lucas José…",
   "mft-nwyj-ixz…" e "IKIGAI Empresarial…" são referências da ferramenta, não
   conteúdo de slide.

A versão anterior, de 51 páginas no painel sobre textura, está no histórico
do git.

## As fotografias: vertical por padrão, rosto sempre inteiro

O material do Lucas chegou com **13 imagens em 16:9** e **uma em retrato**
(a 01). Duas decisões vêm daí, e as duas são aritmética, não gosto.

### 1. A tira vertical é o padrão

Numa faixa horizontal o corte é **vertical** e come a maior parte da altura.
Numa tira vertical o corte é horizontal, e a cabeça ocupa uma fração bem menor
da largura. Medindo foto por foto o quanto cada tratamento exige para o rosto
sobreviver:

| | faixa horizontal | tira vertical |
|---|---|---|
| o rosto exige | **52% a 86%** da página | **26% a 42%** |
| sobra para o texto | nada, em quase todas | a página quase inteira |

Com 16:9, **uma faixa horizontal que preserva o rosto não deixa página para o
texto**. Por isso a distribuição final:

| Tratamento | Páginas |
|---|---|
| Tira vertical | **7** |
| Tela cheia (horizontal, sem recorte nenhum) | **4** |
| Faixa horizontal | 0 |

A tela cheia é o horizontal que funciona com este material: a foto aparece
inteira, nada é cortado, e o texto vai por cima com véu.

### 2. O rosto nunca é cortado — e isso é conferido

`padrao-ka/rostos.py` detecta a cabeça de cada foto e grava `rostos.json`
nesta pasta. O motor lê o mapa e calcula o recorte que mantém a cabeça inteira,
com folga. Quando não cabe, ele cresce a tira; se ainda não cabe, vira a página
de orientação e **avisa no build** — cortar o rosto não é uma saída.

```bash
python3 padrao-ka/rostos.py clientes/lucas-martini/assets        # ao trocar fotos
python3 padrao-ka/conferir_rostos.py <arquivo>.pptx clientes/lucas-martini/assets
```

A conferência abre o `.pptx` pronto, lê o recorte **real** gravado em cada
imagem e confere contra o mapa. Hoje: **12 fotografias, nenhuma cabeça
cortada.**

A imagem 04 (o jovem no caixa eletrônico) não tem rosto detectado porque o
Lucas não aparece nela — fica de fora da conferência.

## O gabarito de imagens

Seguido slide a slide. Três observações sobre o que mudou e por quê:

1. **A imagem 07 ficou de fora das duas apresentações**, como pedido — o
   monitor tem conteúdo gerado dentro da própria imagem.
2. **Nenhuma fotografia se repete em slides consecutivos.** Quando uma volta,
   volta em escala, lado ou recorte diferentes.
3. **`IMG_1214.JPG` (o letreiro real da Prudential) não veio no pacote.** O
   slide "A seguradora entrega o instrumento / Lucas constrói a estratégia"
   está usando a imagem 01. Se a foto real aparecer, é trocar o `IMG[1]` desse
   slide em `base_estrategica.py`.

### Slides que pedem imagem conceitual e hoje são só tipográficos

Dois pontos onde a diretriz previa uma fotografia que ainda não existe. Estão
resolvidos com composição tipográfica, que funciona — mas ganhariam com a
imagem certa:

- **"Uma história sobre construção"** (Revelação) — pedia casa em construção,
  mãos construindo, estrutura. Hoje: título, lead e destaque.
- **"Dignidade financeira"** (Revelação) — pedia uma família em situação
  cotidiana, sem tragédia, transmitindo vida seguindo normalmente. Hoje:
  lista de quatro leituras.

---

## O que conferir antes de mandar para o cliente

```bash
padrao-ka/conferir.sh clientes/lucas-martini/<arquivo>.pptx
```

O script acusa qualquer texto que passe do fundo do painel e deixa a prévia em
PNG. Ele pega texto vazando; **não pega enquadramento ruim** — o recorte das
fotografias ainda precisa de olho humano.
