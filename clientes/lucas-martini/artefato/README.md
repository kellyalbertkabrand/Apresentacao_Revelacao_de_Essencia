# Brand Book do Lucas — a via do artefato

As mesmas 32 páginas do `.pptx`, montadas como artefato do tipo **Slides**.
Mesmo roteiro, mesma grade, mesma escala — em pixel em vez de polegada
(1" = 96 px, 1pt = 4/3 px). A tradução está em
`.claude/skills/brand-book-ka/SKILL.md`, §2.

```
project/deck.json     o índice: ordem, capítulos, fontes
project/deck.css      a grade e a paleta, uma vez só
project/slides/*.html uma página por arquivo
```

## Conferir antes de publicar

Não há `conferir.sh` aqui: o equivalente é `ver.js`, que abre cada página no
Chromium com as fontes de verdade, tira o PNG e acusa o que passa do pé
útil (970 px) ou sai da margem.

```bash
node ver.js uma-pagina instagram        # algumas
node ver.js $(python3 -c "import json;print(' '.join(json.load(open('project/deck.json'))['order']))")
```

`blobs.json` liga cada `/_blob/<id>` ao arquivo em `assets/`, para a prévia
local mostrar as imagens — no artefato publicado os ids resolvem sozinhos.
Trocar de artefato significa reenviar os assets e refazer esse mapa.
