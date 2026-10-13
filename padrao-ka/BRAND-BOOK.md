# BRAND BOOK — a terceira família de documentos do KA

A Revelação de Essência e a Base Estratégica são **apresentações**: painel
claro sobre a textura de ondas, uma ideia por página, muito ar.

O brand book é outra coisa: é **manual**. Tem cabeçalho com paginação,
capítulos numerados, página inteira de cor e a informação organizada em duas
colunas — o título à esquerda, o conteúdo à direita. Quem abre um brand book
não está assistindo: está consultando.

Motor: [`ka_brandbook.py`](ka_brandbook.py). Diagramação medida página a
página no **Brand Book KA 2026**.

```python
from ka_brandbook import Brandbook
d = Brandbook(marca="LUCAS MARTINI", documento="Brand Book",
              paleta=PALETA, logos=LOGOS)
d.montar(PAGINAS)
d.salvar("Brand-Book.pptx")
```

Referência viva: [`clientes/lucas-martini/brandbook.py`](../clientes/lucas-martini/brandbook.py)
— 27 páginas.

---

## 1. A grade

| | Medida |
|---|---|
| Página | 20" × 11,25" |
| Margens | 1,00" à esquerda, 19,00" à direita |
| Coluna da esquerda | x 1,00" · largura 7,60" — o título e o resumo |
| Coluna da direita | x 10,85" · largura 7,50" — o conteúdo |
| Cabeçalho | y 0,68" |
| Primeira linha do título | y 1,90" |
| Pé útil | 10,30" — nada de texto abaixo disto |

O cabeçalho é o que faz o documento parecer manual: um filete vertical de
acento, o nome do documento e da marca em caixa alta espacejada à esquerda, e
a paginação `NN / total` à direita.

## 2. A paleta é parâmetro

O brand book é o único documento do padrão que **veste a identidade do
cliente**, não a do KA. A paleta entra como dicionário:

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
    "corpo_escuro": "C8CCC6",
}
```

A tipografia **não** é parâmetro: é a Outfit, como em todo o padrão KA. Se a
marca do cliente tem fonte própria, ela é **nomeada** na página de
tipografia; o documento continua composto na Outfit, e a página diz isso.

## 3. Os quatorze arquétipos

| `tipo` | O que é | Campos |
|---|---|---|
| `capa` | logo centrado sobre a cor da marca, trama e edição | `titulo`, `edicao`, `logo_largura`, `logo_y` |
| `indice` | capítulo, nome e legenda, separados por filete | `itens`: `(num, nome, legenda)` |
| `divisor` | capítulo: página inteira de cor, numeral, nome em bold | `numero`, `nome`, `legenda` |
| `texto` | título à esquerda, parágrafos à direita | `titulo`, `resumo`, `marcado`, `paragrafos` |
| `lista` | linhas com seta, separadas por filete | `titulo`, `resumo`, `rotulo`, `itens`, `fecho` |
| `colunas` | 2–4 colunas de `(rótulo, nome, texto)` | `colunas`, `fecho` |
| `numerais` | pilares numerados 01…05 | `itens`: `(nome, texto)` |
| `declaracao` | a página de silêncio: uma frase, muito ar | `linhas`, `apoio`, `tam`, `agua` |
| `pares` | em vez de / prefere — o que a marca risca e o que assina | `pares` |
| `meia` | meia página de cor, meia de imagem | `linhas`, `foto`, `corte`, `lado` |
| `paleta` | amostras de cor com código e uso | `cores`: `(nome, hex, uso)` |
| `marca` | versões do logo, cada uma no seu fundo | `versoes`: `(nome, arquivo, fundo, legenda)` |
| `tipografia` | espécimes e hierarquia | `familias`, `nota` |
| `fecho` | logo, frase e assinatura | `frase`, `assinatura` |

Todos aceitam `olho` (o rótulo de acento acima do título) e `tom`
(`claro`, `escuro` ou `areia`).

## 4. Negrito e riscado no meio do texto

No brand book o negrito carrega a frase que a pessoa precisa levar embora —
sem ele o texto vira um bloco cinza. O conteúdo marca com `**`, e o riscado,
que a página de vocabulário usa para o que a marca não diz, com `~~`:

```python
"Use como guia antes de criar. **Marca consistente é marca reconhecida.**"
"~~Fatalidade · desespero · oportunidade imperdível~~"
```

O peso vem do nome da fonte (Outfit 1 Semi-Bold), nunca de negrito sintético.

## 5. A marca d'água

O Brand Book KA usa as letras do próprio logotipo, gigantes e quase
apagadas, nas páginas de capítulo. O equivalente aqui é
`logos["escudo"]` — o símbolo da marca, a 10–13% de opacidade, sangrando
pela direita. É sombra, não ilustração: se der para ler, está forte demais.

A trama de pontos (`trama.py` gera as três variantes) é a única textura.

## 6. Conferência

O brand book não tem painel: a página inteira é área útil, e o limite passa
a ser 10,30".

```bash
padrao-ka/conferir.sh <arquivo>.pptx --fundo 10.30
```
