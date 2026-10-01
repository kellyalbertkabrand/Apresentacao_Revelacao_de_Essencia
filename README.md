# Apresentações · KA — Inteligência para Marcas

Sistema de apresentações do escritório de branding de Kelly Albert. Gera
`.pptx` por código, para que o padrão visual seja o mesmo em toda entrega e o
trabalho fique na estratégia, não no arrasta-caixinha.

## Como está organizado

```
padrao-ka/              O PADRÃO DE LAYOUT — vale para toda apresentação KA
  SISTEMA-VISUAL.md       grade, paleta, tipografia, arquétipos de página
  ka_layout.py            o motor; não conhece conteúdo nenhum
  ka_paginas.py           arquétipos de página para roteiro declarativo
  ROTEIRO-DECLARATIVO.md  quando o roteiro não é fixo: páginas como dados
  conferir.sh             renderiza e acusa texto vazando do painel
  assets/                 textura, logos, símbolos

modelos/                UM MODELO POR TIPO DE APRESENTAÇÃO
  revelacao-de-essencia/
    MODELO.md             a tese, as seis seções, o roteiro, o contrato
    gerar.py              monta o deck a partir do conteúdo do cliente

clientes/               UM PROJETO POR CLIENTE
  flavia-muccelin/        roteiro fixo — usa modelos/revelacao-de-essencia
    conteudo.py           só dados: os textos da apresentação
    assets/               as fotos, nomeadas pelo slide de destino
  lucas-martini/          roteiro declarativo — duas apresentações
    revelacao.py          Revelação de Essência (63 slides)
    base_estrategica.py   Base Estratégica da Marca (69 slides)
    gerar.py              monta as duas, em .pptx e .pdf

referencia/             o .pptx aprovado — herda tema e as fontes Outfit
arquivo/                material anterior ao padrão atual; histórico
```

A separação é o ponto: **layout**, **roteiro** e **conteúdo** vivem em
arquivos diferentes e mudam em ritmos diferentes. Trocar o texto de um cliente
não encosta no layout; ajustar o layout melhora todas as apresentações de uma
vez.

## Gerar

```bash
python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin
python3 clientes/lucas-martini/gerar.py
```

Sai o `.pptx` (e, no caso do Lucas, também o `.pdf`) na pasta do cliente.

**Duas rotas**, conforme a entrega:

- **Roteiro fixo** (`modelos/<tipo>/`) — quando a apresentação se repete igual
  de cliente para cliente, como a Revelação de Essência. O conteúdo preenche
  um contrato de campos.
- **Roteiro declarativo** (`padrao-ka/ka_paginas.py`) — quando cada entrega
  tem estrutura própria. O conteúdo declara a lista de páginas.

O layout é o mesmo nas duas.

## Conferir

```bash
padrao-ka/conferir.sh clientes/flavia-muccelin/Revelacao-de-Essencia-Flavia-Pereira-Muccelin.pptx
```

O texto real quebra em mais linhas do que as alturas declaradas no código
supõem, então conferir é obrigatório. O script renderiza com o LibreOffice e
mede a caixa real de cada palavra — detalhe em
[`padrao-ka/SISTEMA-VISUAL.md`](padrao-ka/SISTEMA-VISUAL.md) §7.

## Um cliente novo

```bash
cp -r clientes/flavia-muccelin clientes/<novo>
```

Depois trocar os textos em `conteudo.py` e as fotos em `assets/`.
O contrato de cada campo está em
[`modelos/revelacao-de-essencia/MODELO.md`](modelos/revelacao-de-essencia/MODELO.md) §5.

## Requisitos

`python-pptx` e `Pillow`. Para conferir a prévia, LibreOffice Impress e
`poppler-utils` (`pdftotext`, `pdftoppm`).
