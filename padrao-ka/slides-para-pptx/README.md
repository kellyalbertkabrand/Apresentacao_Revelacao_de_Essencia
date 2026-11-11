# Slides → PPTX editável

Converte uma apresentação do **Padrão KA** que vive num artefato do tipo
Slides (HTML em 1920 × 1080) num **PowerPoint nativo**: cada texto vira caixa
de texto na Outfit certa, cada filete e cada pílula viram forma, cada foto
vira imagem já cortada e com os cantos do layout. Nada de slide-imagem — a
Kelly abre no PowerPoint e edita palavra por palavra.

A conversão não redesenha nada: ela **mede** o slide no próprio navegador, com
as fontes do KA instaladas, e repõe o que mediu em OOXML. Posição, corpo,
entrelinha, letter-spacing, cor e quebra de linha saem iguais.

## Como rodar

A pasta do deck é a que tem `project/deck.json`, `project/slides/*.html` e
`assets/`. Falta só um `mapa.json` ligando o id de cada blob do artefato ao
arquivo correspondente em `assets/`:

```json
{ "c223da446a73d54aba9fd7506f031a37": "c1-a.png",
  "b44607f35b0c6b54d374724d7c525aa9": "vm-rocks.png" }
```

Com ele no lugar:

```bash
cd padrao-ka/slides-para-pptx
node   extrair.js     <pasta-do-deck>          # mede tudo -> edit/spec.json
node   ilustracoes.js <pasta-do-deck>          # rasteriza SVG e logos
python3 montar.py     <pasta-do-deck> saida.pptx
```

Para conferir, o caminho de sempre:

```bash
libreoffice --headless --convert-to pdf saida.pptx
```

## O que cada etapa faz

| Etapa | O que resolve |
|---|---|
| `extrair.js` | Abre cada slide no Chromium com a Outfit de verdade e anota, elemento por elemento, a caixa medida, os trechos de texto (com o peso e a cor de cada um), o fundo, o raio dos cantos e os filetes de cada lado. |
| `ilustracoes.js` | Os desenhos em SVG e os logos vetoriais viram PNG com fundo transparente a 4× — é o único jeito de levá-los para o PPTX sem perder o traço. |
| `montar.py` | Fecha o arquivo: caixa de texto, forma, imagem. Tira o estilo de tema de cada forma (senão o PowerPoint devolve sombra e contorno que o padrão KA não tem) e guarda o `<aside>` do slide como nota do apresentador. |

## O que a conversão garante

- **Peso pelo nome da fonte**, como manda o padrão: 300 → `Outfit 1 Light`,
  500 → `Outfit 1 Medium`, 600 → `Outfit 1 Semi-Bold`, 700 → `Outfit 1 Bold`.
  Nada de negrito sintético.
- **1 px = 0,5 pt.** O slide de 1920 px vira 13,333 × 7,5 polegadas, então o
  corpo de 32 px sai exatamente em 16 pt e o título de 52 px em 26 pt.
- **Entrelinha exata** (`line_spacing` em pontos), não múltiplo — é o que
  mantém o ar do layout.
- **Filete de um lado só** vira barra fina, não contorno de caixa.
- Foto com `object-fit: cover` é **cortada no centro** antes de entrar, e o
  `border-radius` vira máscara com alfa. Foto cheia sai em JPEG, foto com
  canto redondo em PNG — o arquivo fica um terço do tamanho.

## O que ela não faz

- Gradiente, sombra e filtro CSS: o padrão KA não usa, então não foram
  implementados.
- O desenho em SVG continua sendo imagem dentro do PPTX. Editável é o texto.
- A conferência é por comparação: renderize o PPTX em PNG e compare com o
  `png/` do deck. Diferença média acima de ~8 (numa escala de 0 a 255) quer
  dizer que alguma coisa saiu do lugar.
