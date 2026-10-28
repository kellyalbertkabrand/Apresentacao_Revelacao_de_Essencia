# O PADRÃO — medido no arquivo da Kelly

Em outubro/2026 a Kelly pegou a apresentação *Duas Trajetórias, Uma Nova
Força* e **rediagramou à mão**, slide a slide. Depois mandou o arquivo com um
pedido: que **todas** as apresentações do Projeto Marca com Essência sigam
aquele formato — fonte, tamanhos, títulos, espaço para imagem e o layout de
um slide para o outro.

Este documento é o mapeamento desse arquivo. **Não é interpretação: é
medição.** Cada número aqui saiu da árvore XML do `.pptx` dela, lida forma
por forma, e é o que `ka_layout.py` e `ka_paginas.py` passaram a produzir.

Página: **20" × 11,25"**. Fundo: textura de ondas a 32%. Painel claro
`#F8F7F2` recuado 1,10", fundo em **9,60"**. **Sem rodapé** em nenhuma
página. Tudo isso já era o padrão e continua.

---

## 1. A paleta, conferida

| Papel | Antes | **Agora** | Onde |
|---|---|---|---|
| Painel | `#F8F7F2` | `#F8F7F2` | o claro de sempre |
| Tinta | `#1C1C1A` | `#1C1C1A` | títulos, listas, camadas |
| Corpo | `#6B6B66` | `#6B6B66` | o texto corrido |
| **Filete** | `#DFDDD7` | **`#A5A49F`** | o mesmo cinza da legenda — não um mais claro |
| **Acento** | `#A9724A` | **`#CC754E`** | terracota mais vivo |
| Declaração | — | **`#323330`** | a frase grande da página de silêncio |

Duas mudanças reais: o **filete escureceu** (ela usa o mesmo cinza do rótulo,
não um tom apagado) e o **terracota abriu** — `#CC754E` no lugar de
`#A9724A`.

## 2. A escala tipográfica, medida

Fonte única: **Outfit 1**, nas variantes nomeadas. A Outfit 2 só sobrevive
na assinatura da capa.

| Elemento | Corpo | Variante | Cor | Entrelinha |
|---|---|---|---|---|
| Título da capa | 75 | Bold | tinta | 1,10 |
| Subtítulo da capa | 30 | Bold + Regular | tinta | — |
| Assinatura do método | 26,8 | Light + Semi-Bold | tinta | — |
| Data | 19,5 | Regular | tinta | — |
| **Nome da seção (virada)** | **143,5** | **Bold** | tinta | 1,10 |
| **Apoio da virada** | **65** | Light | tinta | 1,16 |
| **Título de página** | **42** | **Light + Bold** | tinta | **1,37** |
| **Corpo** | **25** | Light | corpo | **1,40** |
| **Item de lista** | **30** | Light | **tinta** | 1,40 |
| Rótulo de camada | **18** | Semi-Bold, spc 2,82 | tinta / acento no último | — |
| Leitura da camada | **25** | Light | **tinta** | 1,40 |
| Rótulo de coluna | **25** | Light | tinta | 1,40 |
| Texto de coluna | 25 | Light | corpo | 1,40 |
| Frase de declaração | **37** | Light + Bold | **grafite** | 1,40 |
| Frase sobre fotografia | 28 | Light | tinta | 1,34 |
| **OBRIGADA!** | **95** | Light | tinta | 1,12 |
| Nota de produção | 17 | Light | corpo | 1,40 |

### A entrelinha passou a ser EXATA

O arquivo dela grava entrelinha **exata** — 35pt para corpo de 25, 57,4pt
para título de 42 — e não um múltiplo da altura de linha da fonte. O motor
passou a gravar igual, e isso resolveu de brinde um problema antigo: a conta
de altura virou a própria medida (`linhas × corpo × espaço`), sem fator de
correção. O `ENTRELINHA = 1.24` que existia para compensar a diferença entre
o que se pedia e o que o PowerPoint compunha **deixou de ser necessário**.

## 3. A assinatura do padrão: o título em dois pesos

É o que mais muda a cara da apresentação. O título vai em **caixa alta, 42pt**
— e a frase-chave vem em **Bold**, na mesma linha e no mesmo corpo:

> A MENINA QUE **NÃO ACEITOU OS LIMITES**
> **UM PADRÃO** QUE ATRAVESSA SUA HISTÓRIA
> A **ESSÊNCIA** EMPREENDEDORA DE FLÁVIA
> FLÁVIA É **MAIS DO QUE A FUNDADORA**

O peso marca **o que a página está dizendo** — não o tamanho, não a cor. No
conteúdo isso se escreve com `**`:

```python
{"tipo": "texto", "titulo": "A menina que **não aceitou os limites**", ...}
```

Vale também nos parágrafos, nos itens de lista, nas camadas e nas colunas.
Título de duas ou três palavras fica **sem** marcação: marcar quase tudo é o
mesmo que não marcar nada — o negrito só funciona enquanto for exceção.

## 4. Os quatro tratamentos de imagem

| Tratamento | Medida | Quando |
|---|---|---|
| **Tira sangrando** | 7,60" de largura, altura cheia, esquerda ou direita | o padrão |
| **Imagem solta** | ~6,95" × 7,85", cantos arredondados, pousada sobre o painel à direita | quando a foto deve conviver com o painel, não substituí-lo |
| **Tela cheia com cartão** | foto 20 × 11,25 + cartão claro de 8,54" no alto à direita | a frase sobre a fotografia |
| **Virada de seção** | tela cheia, texto em branco | abertura de tema |

```python
{"tipo": "texto", "foto": "retrato.png", "lado": "solta",
 "imagem": "Briefing do que entra ali.", "titulo": "...", "paragrafos": [...]}
```

**O véu morreu.** Na página de frase sobre fotografia, o texto não vem mais em
branco sobre um véu escuro: vem num **cartão do mesmo claro do painel**,
encostado no alto à direita. O véu escurecia a imagem inteira para salvar o
texto; o cartão preserva a fotografia e ainda assim garante leitura.

## 5. Os filetes têm dois papéis

- **Fino, cinza, 0,012"** — organiza: abaixo do título e entre as camadas.
- **Grosso, acento, 0,062"** — abre um campo: no topo de cada coluna. Entre
  duas colunas entra também um filete vertical de acento, 0,021".
- **Curto, acento, 1,30" × 0,03"** — fecha a escada das camadas, por baixo.

O marcador de lista é um **quadrado de acento de 0,112"**, não um ponto
cinza — e é a única cor da página.

O rótulo da camada é espacejado em **2,82pt por caractere**, e esse
espacejamento entra na conta de largura: num rótulo de 27 letras ele soma mais
de uma polegada. Cada degrau tem a altura do **maior** dos dois lados — um
rótulo que quebra em duas linhas precisa de espaço tanto quanto uma leitura
longa.

## 6. A virada de seção

Sem painel. A textura corre de borda a borda e o nome da seção entra
**gigante, em Bold, alinhado à direita**, com a linha de apoio no mesmo eixo.
A borda direita é **18,875"** — medida nos dois divisores dela.

O nome **cede corpo até caber**: 143,5pt é o teto, não uma obrigação.
"CULTURA ORGANIZACIONAL" não cabe em 143,5pt largura nenhuma.

E o cálculo de caber é feito **na Bold**, não na Light. É o único display do
padrão que sai em Bold, e a Bold é visivelmente mais larga: medindo pela Light,
"HISTÓRIA E ORIGEM" passava na conta e quebrava em duas linhas no arquivo.

## 7. Uma ressalva honesta: dois slides fora do padrão

Dos 26 slides do arquivo, **24 estão no sistema Outfit 1**. Os slides **20 e
23** vieram em **TT Norms** e **Outfit 2**, com espacejamento negativo e
corpos quebrados (40,2 · 25,1 · 22,3 · 23,4pt) — são os dois que ela
reconstruiu no Canva, e a fonte padrão do Canva vazou junto.

**Esses dois não entraram no padrão.** Seguir o anexo "exatamente" nesses
slides significaria colocar uma fonte que não é da KA dentro do sistema. O
que eles têm de bom — o filete grosso de acento no topo da coluna e o divisor
vertical entre as duas — foi adotado; a tipografia deles, não.

---

## Conferência

```bash
padrao-ka/conferir.sh <arquivo>.pptx     # nada passa de 9,60"
python3 padrao-ka/conferir_voz.py        # terceira pessoa
```
