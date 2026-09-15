# Apresentações · KA — Inteligência para Marcas

Sistema de apresentações do escritório de branding de Kelly Albert. Gera
`.pptx` por código, para que o padrão visual seja o mesmo em toda entrega e o
trabalho fique na estratégia, não no arrasta-caixinha.

## Como está organizado

```
padrao-ka/              O PADRÃO DE LAYOUT — vale para toda apresentação KA
  SISTEMA-VISUAL.md       grade, paleta, tipografia, arquétipos de página
  ka_layout.py            o motor; não conhece conteúdo nenhum
  conferir.sh             renderiza e acusa texto vazando do painel
  assets/                 textura, logos, símbolos

modelos/                UM MODELO POR TIPO DE APRESENTAÇÃO
  revelacao-de-essencia/
    MODELO.md             a tese, as seis seções, o roteiro, o contrato
    gerar.py              monta o deck a partir do conteúdo do cliente

clientes/               UM PROJETO POR CLIENTE
  flavia-muccelin/
    conteudo.py           só dados: os textos da apresentação
    assets/               as fotos, nomeadas pelo slide de destino

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
```

Sai um `.pptx` de 31 slides na pasta do cliente.

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
