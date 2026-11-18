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
— 32 páginas, cinco capítulos. O roteiro página a página está na skill
`.claude/skills/brand-book-ka/SKILL.md`.

---

## 1. A grade

| | Medida |
|---|---|
| Página | 20" × 11,25" |
| Margens | 1,15" à esquerda, 18,20" à direita (`ML`, `MR`) |
| Coluna da esquerda | x 1,15" · largura 7,50" — o título e o resumo |
| Coluna da direita | x 10,85" · largura 7,35" — o conteúdo |
| Trilho vertical | x 19,25" (`X_TRILHO`) |
| Primeira linha do título | y 1,90" (`Y_TITULO`) |
| Primeira linha da coluna direita | y 2,05" (`Y_CORPO`) |
| Pé útil | **10,10"** — nada de texto abaixo disto |

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

Os parágrafos saem com as **linhas equilibradas**: em vez de encher a
primeira linha e largar uma palavra órfã na última, a caixa é apertada até o
limite em que o texto ainda ocupa o mesmo número de linhas, e a quebra se
distribui sozinha. A medida é feita palavra a palavra, cada uma no seu peso
— o negrito é mais largo que o leve, e medir tudo em Light estourava a
caixa. Para desligar numa página, `equilibrar=False` na chamada.

O cabeçalho é um **trilho vertical na margem direita**: o nome do documento
de pé, lendo de baixo para cima, e o número da página no pé do trilho. A
margem é de 1,15" nos quatro lados (`ML`, `MR`, `FUNDO`), e o trilho vive em
`X_TRILHO`, na faixa entre a margem e a borda — nunca dentro da coluna de
texto.

## A tipografia é do cliente

O brand book é o único documento do padrão que veste a **tipografia da
marca do cliente**, e não a do escritório. A divisão é sempre a mesma, e
está no alto de `ka_brandbook.py`:

| Camada | O que compõe | Constantes |
|---|---|---|
| **Display** | título de página, numeral e nome de capítulo | `TIT`, `TIT_SEMI` |
| **Texto** | corpo, rótulo, legenda, numeração | `LIGHT`, `REG`, `SEMI`, `BOLD` |
| **Assinatura** | a linha que acompanha o logotipo | `ASSINATURA` |

Trocar a tipografia de um brand book é mudar esses nomes e pôr os `.ttf`
em `padrao-ka/fontes/`. **A medida refaz sozinha**: `F_CORPO`,
`F_CORPO_SEMI` e `F_TIT` apontam para os arquivos com que o texto é
medido, e `linhas`/`altura` aceitam o arquivo como parâmetro. Nada muda de
lugar na grade.

Duas regras seguem valendo. O peso vem do **nome** da fonte, nunca de
negrito sintético — por isso cada peso é uma família própria (`DM Sans
Light`, `DM Sans SemiBold`). E a fonte que o escritório **não pode
licenciar** para o arquivo é nomeada na página de tipografia e substituída
no documento pela mais próxima que se pode: é o caso da Allrounder e da
Codec Pro do Lucas Martini, que têm licença só de Canva.

### Lucas Martini

| Camada | Oficial | No arquivo |
|---|---|---|
| Display | Allrounder (Identity Letters) | EB Garamond |
| Texto | DM Sans | DM Sans — a própria |
| Assinatura | Codec Pro (Zetafonts) | Outfit 1 |

## 3. Os dezoito arquétipos

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
| `aplicacoes` | a marca nas peças: uma foto grande ao lado do texto, ou uma fileira delas | `fotos`: `(arquivo, legenda)`, `texto`, `nota`, `y` |
| `fecho` | logo, frase e assinatura | `frase`, `assinatura` |
| `instagram` | a marca na rede: perfil num celular, destaques e feed | `texto`, `icones`: `(arquivo, nome)`, `celular`, `posts` |
| `creditos` | a última página: a marca do cliente no alto e, embaixo, as assinaturas de quem fez | `marca`, `olho`, `logos`: `(arquivo, largura, legenda)`, `gap`, `tam_mais`, `disposicao` |

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

O peso vem do nome da fonte (DM Sans SemiBold), nunca de negrito sintético.

## 5. A marca d'água

O Brand Book KA usa as letras do próprio logotipo, gigantes e quase
apagadas, nas páginas de capítulo. O equivalente aqui é
`logos["escudo"]` — o símbolo da marca, a 10–13% de opacidade, sangrando
pela direita. É sombra, não ilustração: se der para ler, está forte demais.

A trama de pontos (`trama.py` gera as três variantes) é a única textura.

## 6. Conferência

O brand book não tem painel: a página inteira é área útil, e o limite passa
a ser 10,10".

```bash
padrao-ka/conferir.sh <arquivo>.pptx --fundo 10.10
python3 padrao-ka/conferir_voz.py clientes/<cliente>/brandbook.py
```

O conferidor pega vazamento pelo pé. **Colisão de blocos e palavra cortada
no meio só o olho pega** — gerar o contato em PNG do PDF e ler as páginas,
uma a uma, antes de entregar.
