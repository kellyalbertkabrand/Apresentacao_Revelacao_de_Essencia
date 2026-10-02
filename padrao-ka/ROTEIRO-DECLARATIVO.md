# ROTEIRO DECLARATIVO — páginas como dados

Extensão do sistema visual KA para apresentações cujo roteiro **não é fixo**.

O modelo da Revelação de Essência tem um roteiro fechado: seis seções, páginas
na mesma ordem, um contrato de campos (`modelos/revelacao-de-essencia/`). Isso
funciona quando a entrega se repete igual de cliente para cliente.

Nem toda apresentação é assim. Uma Base Estratégica tem nove seções e muda de
estrutura conforme a marca; uma Revelação pode pedir doze páginas de frase e
três tabelas. Para esses casos, [`ka_paginas.py`](ka_paginas.py) oferece uma
rota diferente: **o conteúdo declara a lista de páginas**.

```python
PAGINAS = [
    {"tipo": "divisor", "numero": "01", "nome": "A origem"},
    {"tipo": "declaracao", "linhas": ["A história não é a revelação.",
                                      "A história é a evidência."]},
    {"tipo": "texto", "titulo": "Uma história sobre construção",
     "lead": "...", "destaque": "Segurança pode levar anos para ser construída.",
     "foto": "09_origem.png", "lado": "cima"},
]
```

A aparência continua sendo a do [SISTEMA-VISUAL.md](SISTEMA-VISUAL.md): mesma
grade, mesma paleta, mesma escala tipográfica, mesmos filetes. O que muda é só
a liberdade de ordenar as páginas.

---

## 1. Os arquétipos

| `tipo` | O que é | Campos |
|---|---|---|
| `abertura` | logos sobre a textura | — |
| `capa` | título em caixa alta sobre a textura, traço no canto e barra de assinatura | `titulo` (lista), `subtitulo` (lista: nome + descritor), `assinatura`, `data`, `foto` (opcional) |
| `sumario` | índice numerado | `itens`: `(num, nome[, descrição])` |
| `divisor` | virada de seção | `numero`, `nome`, `apoio` |
| `declaracao` | **a página de silêncio**: uma frase grande e muito ar | `linhas`, `apoio`, `eyebrow`, `marcar` |
| `texto` | eyebrow, título, filete, lead, parágrafos, destaque | `titulo`, `lead`, `paragrafos`, `itens`, `destaque` |
| `lista` | itens com ponto; vira duas colunas se a lista for longa | `lead`, `itens`, `destaque`, `grade` |
| `colunas` | 2–4 colunas de `(rótulo, texto)` | `colunas`, `equacao`, `fecho` |
| `palavras` | palavras soltas como composição | `palavras`, `grade`, `tam`, `destaque` |
| `camadas` | rótulo → leitura, empilhados: a escada de significado | `camadas`: `(rótulo, texto)` |
| `fluxo` | passos encadeados na horizontal, com seta | `passos`, `sintese` |
| `contraste` | dois campos em oposição, separados por `×` | `esquerda`, `direita`: `(rótulo, [itens])` |
| `alternativas` | "em vez de / preferir" — a troca de linguagem | `pares`, `rot_evitar`, `rot_preferir` |
| `ficha` | prancha-resumo em duas colunas | `campos`: `(rótulo, valor)` |
| `ikigai` | os quatro anéis + as quatro leituras | `campos`, `centro` |
| `manifesto` | texto longo em duas colunas | `paragrafos`, `assinatura` |
| `foto_cheia` | foto em tela cheia com véu, texto branco | `foto`, `linhas`, `apoio`, `veu`, `foco` |
| `fecho` | agradecimento e assinatura | `frase` |

Todos aceitam `eyebrow`, `titulo` e `tam_titulo`.

---

## 2. Fotografia: por que a faixa é horizontal

O modelo da Revelação sangra a foto numa **faixa vertical** de ~40% da
largura. Isso pede imagem em **retrato** — era o caso do material da Flávia.

Quando o material chega em 16:9, como o do Lucas, essa faixa recorta a
fotografia a **um quarto da largura original**. Por isso aqui a foto entra de
duas outras maneiras:

- **faixa horizontal** — `"lado": "cima"` ou `"baixo"`. A foto sangra de ponta
  a ponta e o painel claro ocupa o resto. **Só funciona com foto cujo rosto
  caiba numa faixa curta** (ver abaixo).
- **tela cheia com véu** — `tipo: "foto_cheia"`. Para as frases que precisam
  de peso emocional.

- **tira vertical** — `"lado": "direita"` ou `"esquerda"`. A foto sangra numa
  lateral e o texto ocupa a outra. **É o tratamento padrão.**

### O rosto nunca é cortado

`padrao-ka/rostos.py` detecta a cabeça de cada foto e grava `rostos.json` ao
lado delas. O motor lê esse mapa e calcula o recorte que mantém a cabeça
inteira — com folga. Não é estimativa: é conta sobre a posição medida.

```bash
python3 padrao-ka/rostos.py clientes/<cliente>/assets     # depois de trocar fotos
python3 padrao-ka/conferir_rostos.py <arquivo>.pptx clientes/<cliente>/assets
```

O `conferir_rostos.py` abre o `.pptx` pronto, lê o recorte **real** gravado em
cada imagem e confere contra o mapa. Casa as fotos por conteúdo, porque o
python-pptx renomeia tudo para `image1.png` no caminho.

Quando o recorte não comporta a cabeça, o motor **não corta**: ele age, nesta
ordem.

1. Cresce a faixa (ou a tira) até a cabeça caber.
2. Se a faixa necessária não deixa espaço para o texto, **vira tira
   vertical** — e avisa no build.
3. Se nem a tira resolve, avisa alto.

### Por que a tira vertical é o padrão

Numa faixa horizontal o corte é **vertical** e come 60% da altura. Numa tira
vertical o corte é horizontal, e a cabeça ocupa uma fração bem menor da
largura. Com o material do Lucas (13 fotos em 16:9), a conta fica assim:

| | faixa horizontal | tira vertical |
|---|---|---|
| altura/largura que o rosto exige | **52% a 86%** da página | **26% a 42%** |
| sobra para o texto | nada, na maioria | a página quase inteira |

Ou seja: com foto 16:9, **uma faixa horizontal que preserva o rosto não deixa
página para o texto**. O horizontal que funciona é a tela cheia, onde a foto
aparece inteira e nada é cortado.

Dois parâmetros ainda controlam o enquadramento manualmente, quando não há
mapa de rostos:

| | |
|---|---|
| `fatia` | quanto da altura a faixa pede (padrão 0,42) |
| `fatia_v` | quanto da largura a tira pede (padrão 0,38; cresce até 0,46) |
| `foco` | que parte da imagem sobrevive ao corte: `0` = topo, `0,5` = centro |

Com `rostos.json` presente, o `foco` é calculado e o valor manual é ignorado.

---

## 3. As três regras de ajuste automático

Texto de cliente nunca tem o tamanho do texto de exemplo. Três mecanismos
impedem que isso vire página estourada:

1. **A faixa cede altura ao texto** (`_fatia`). Uma faixa de 42% com lead,
   parágrafo e destaque embaixo obriga a reduzir o corpo até ficar ilegível.
   Melhor a foto perder dois centímetros do que a leitura perder dois pontos.
2. **O miolo mede antes de desenhar** (`corpo`). Quando não cabe, aperta
   primeiro os intervalos e só depois reduz o corpo — e nunca abaixo de 85%,
   porque a partir daí o texto deixa de ser legível na projeção.
3. **As listas e as camadas se redistribuem.** Lista longa de itens curtos vai
   para duas colunas em vez de espremer a entrelinha; cada degrau da escada
   tem a altura do seu próprio texto, não uma fatia igual.

Nada disso dispensa a conferência:

```bash
padrao-ka/conferir.sh <arquivo>.pptx
```

E quando mesmo assim não couber, a correção certa continua sendo **cortar
texto**, não diminuir corpo. Se não coube, o slide está dizendo duas coisas.

---

## 4. Uso

```python
import sys, os
sys.path.insert(0, "padrao-ka")
from ka_paginas import DeckNarrativo

d = DeckNarrativo(documento="Base Estratégica da Marca",
                  marca="Lucas Martini",
                  assets="clientes/lucas-martini/assets")
d.montar(PAGINAS)
d.salvar("saida.pptx")
```

Exemplo completo e vivo: `clientes/lucas-martini/` — duas apresentações, 63 e
69 slides, montadas a partir de dois módulos de conteúdo.

---

## O rodapé é opcional

A Kelly pediu a Base Estratégica **sem rodapé** — a pílula `DOCUMENTO | MARCA`
e o logo KA saem de todas as páginas. A Revelação mantém o rodapé, como no
arquivo final dela.

```python
# no conteudo.py do cliente
RODAPE = False
```

O `gerar.py` do cliente repassa:

```python
d = DeckNarrativo(documento=C.DOCUMENTO, marca=C.MARCA,
                  assets=..., rodape=getattr(C, "RODAPE", True))
```

---

## Quando o texto não cabe

O motor mede o texto na própria fonte (veja SISTEMA-VISUAL.md) e monta cada
página pela altura real de cada bloco. Se ainda assim não couber, ele **avisa
no build** em vez de espremer:

```
! texto nao cabe em "Reconhecimento × exposição": sobram 0.21" para cortar
```

A saída é cortar texto ou quebrar a página em duas — nunca diminuir o corpo
abaixo de 92%, nem espremer a linha. Espremer a caixa não encolhe o texto:
faz o filete da linha seguinte passar por cima da última linha.
