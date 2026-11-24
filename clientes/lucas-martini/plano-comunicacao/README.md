# Plano de Comunicação e Conteúdo — o modelo

`MODELO-Plano-Lucas-Martini.pptx` é o arquivo **aprovado pela Kelly** em
outubro/2026: 46 páginas, seis capítulos, grade de 108 px, Outfit e paleta
KA. É dele que a skill `.claude/skills/plano-comunicacao-conteudo/` foi
medida, e é contra ele que se confere qualquer plano novo.

> **O título mudou.** Este arquivo ainda diz "Plano de Conteúdo" na capa e
> nos 46 rodapés. O nome correto, daqui em diante, é **Plano de Comunicação
> e Conteúdo**. O modelo vale pela diagramação e pela ordem, não pelo
> título.

`medidas.txt` é o mapa que a skill usa como prova: cada página com as
caixas na posição, no tamanho e na cor em que estão no arquivo. Quando uma
medida da skill for contestada, é aqui que se verifica.

Refazer o mapa depois de mexer no modelo:

```bash
python3 clientes/lucas-martini/plano-comunicacao/medir.py \
        clientes/lucas-martini/plano-comunicacao/MODELO-Plano-Lucas-Martini.pptx 1 46 \
        > clientes/lucas-martini/plano-comunicacao/medidas.txt
```

As duas versões anteriores continuam em `clientes/lucas-martini/`:
`Plano-de-Conteudo-Lucas-Martini.pptx` (32 páginas, motor declarativo) e
`…-KA.pptx` (48 páginas, antes dos cortes da Kelly). Nenhuma das duas é o
modelo — **esta é**.
