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
| `revelacao.py` | Revelação de Essência — origem identitária do fundador | 63 |
| `base_estrategica.py` | Base Estratégica da Marca — posicionamento e comunicação | 69 |
| `assets/` | as 14 fotografias | — |

---

## As fotografias, e por que a faixa aqui é horizontal

O material do Lucas chegou com **13 imagens em 16:9** e **uma em retrato**
(a 01, o retrato corporativo).

O modelo da Revelação de Essência sangra a foto numa **faixa vertical** de
~40% da largura — foi feito para o material da Flávia, que veio em retrato.
Aplicado aqui, esse corte reduziria cada fotografia a **um quarto da largura
original**, exatamente o "excesso de recortes" que a diretriz pedia para
evitar.

Por isso, nestes dois decks a fotografia entra de três maneiras:

| Tratamento | Quando | Como fica |
|---|---|---|
| **Faixa horizontal** (`lado: "cima"`/`"baixo"`) | o caso normal, com 16:9 | sangra de ponta a ponta; o painel claro ocupa o resto |
| **Tela cheia com véu** (`tipo: "foto_cheia"`) | frases que precisam de peso | foto inteira, texto branco por cima |
| **Tira vertical** (`lado: "direita"`/`"esquerda"`) | **só a imagem 01**, que é retrato | o tratamento do deck da Flávia |

O motor recusa sozinho retrato em faixa horizontal: imagem com proporção
abaixo de 1,15 vai automaticamente para a tira vertical.

### `foco`: por que existe

Numa faixa horizontal o corte é **vertical**, e centralizar decapita as
pessoas. `foco` diz que parte da imagem sobrevive: `0` é o topo, `0,5` o
centro. Retrato em pé pede entre 0,08 e 0,16; cena de mesa, entre 0,20 e 0,28.

---

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
