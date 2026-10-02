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
| `base_estrategica.py` | Base Estratégica da Marca — posicionamento e comunicação | 30 |
| `assets/` | as 14 fotografias | — |

---

## A edição: 63 e 69 páginas viraram 30 cada

A primeira montagem tinha 63 slides e dizia a mesma coisa que estes 30: cada
descoberta vinha anunciada numa página, desenvolvida na seguinte e repetida
numa terceira em caixa alta.

Aqui cada descoberta ocupa **uma página só** — a afirmação, a evidência e a
leitura juntas. Nenhuma ideia do material original saiu; o que saiu foi a
repetição. Por seção:

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

### A Base Estratégica tem uma restrição própria

São **nove seções**, e os divisores sozinhos ocupam 9 das 30 páginas. Com
capa, sumário, abertura e fecho, sobram **17 para o conteúdo** — menos de duas
por seção. Por isso ali os cinco pilares viraram uma página, os quatro
públicos viraram uma, e o Golden Circle inteiro cabe numa só.

Se a Kelly quiser mais fôlego nessa apresentação, o caminho não é cortar mais
conteúdo: é **reduzir o número de seções** ou aceitar passar de 30.

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
