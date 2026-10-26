# Flávia Pereira Muccelin — FORMA e My Home

Duas entregas, dois motores.

| Arquivo | O que é | Páginas | Como gerar |
|---|---|---|---|
| `conteudo.py` | Revelação de Essência — origem identitária da fundadora | 31 | `python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin` |
| `sociedade.py` | Duas trajetórias, uma nova força — Flávia & Elandi | 26 | `python3 clientes/flavia-muccelin/gerar.py sociedade` |
| `cultura.py` | Cultura Organizacional — FORMA e My Home | 24 | `python3 clientes/flavia-muccelin/gerar.py cultura` |

A Revelação tem **roteiro fixo** e gerador próprio. A apresentação da
sociedade tem roteiro próprio e usa o **roteiro declarativo**
([`padrao-ka/ROTEIRO-DECLARATIVO.md`](../../padrao-ka/ROTEIRO-DECLARATIVO.md)).

A identidade visual é a mesma nas duas, e é a mesma do Lucas: painel claro
sobre a textura de ondas, Outfit, acento terracota.

---

## Duas trajetórias, uma nova força

Documento de alinhamento societário entre Flávia e Elandi, para a FORMA e a
My Home. O conteúdo veio da Kelly em 21 slides; sai aqui em 26 páginas, e a
razão é a regra dela:

> "Um título e um texto num slide."

Três slides do roteiro carregavam dois blocos distintos — a citação do
Elandi e a leitura dela, a narrativa final e a sua conclusão. Empilhar os
dois é o que a regra proíbe, então cada bloco virou a sua própria página. O
texto é o dela, palavra por palavra, na ordem dela.

**Sem rodapé** (`RODAPE = False`): sem a pílula `DOCUMENTO | MARCA` e sem o
logo KA no pé, como ela pediu.

### Duas decisões de estrutura, assinaladas

1. **Não há sumário.** O roteiro desta versão não traz seções, e inventar
   nomes de capítulo seria escrever por cima dela. É uma narrativa contínua
   — a Flávia, o Elandi, o encontro — e lê melhor assim. Se quiser índice, é
   só nomear as três partes.
2. **"O próximo capítulo" é título de duas páginas**, a 02 e a 21. No
   roteiro dela isso abre e fecha o documento. Ficou como ela escreveu.

### Como o conteúdo virou página

| Arquétipo | Onde |
|---|---|
| `texto` | a narrativa corrida — a maioria das páginas |
| `lista` | o padrão que atravessa a história (slide 04) |
| `camadas` | as essências de cada um (slides 05 e 11): rótulo e leitura lado a lado |
| `colunas` | papéis, as duas empresas, onde cada um gera valor (16, 18, 19) |
| `declaracao` | a abertura e a conquista final |
| `foto_cheia` | a citação do Elandi |

### As imagens ainda não existem

Seis páginas pedem fotografia e trazem a **marcação**: a área exata que a
imagem vai ocupar, com o briefing do que entra ali.

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `sociedade-casa-portao.png` | a casa além do portão — o lugar da história |
| `sociedade-ambiente-forma.png` | um ambiente assinado pela FORMA |
| `sociedade-produto-my-home.png` | um produto My Home, o que nasceu da sobra |
| `sociedade-flavia-equipe.png` | Flávia com a equipe, liderança em ação |
| `sociedade-elandi-retrato.png` | retrato do Elandi, meio corpo |
| `sociedade-flavia-elandi.png` | os dois em conversa de trabalho — tela cheia |

Quando esses arquivos entrarem em `assets/` com esses nomes, **a marcação
desaparece sozinha e nada muda de lugar**. Depois de colocá-los, rodar o
mapa de rostos para que o corte nunca decepe ninguém:

```bash
python3 padrao-ka/rostos.py clientes/flavia-muccelin/assets
python3 clientes/flavia-muccelin/gerar.py sociedade
python3 padrao-ka/conferir_rostos.py \
    clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elandi.pptx \
    clientes/flavia-muccelin/assets
```

### Conferência

```bash
padrao-ka/conferir.sh clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elandi.pptx
```

---

## Cultura Organizacional — FORMA e My Home

A Kelly pediu **o mais visual possível**, dentro da estrutura, das cores e do
layout padrão. No padrão KA isso não é encher a página de caixas: é usar os
arquétipos que carregam a ideia na forma, e deixar o parágrafo corrido só
onde ele é mesmo necessário.

| Arquétipo | Papel | Páginas |
|---|---|---|
| `divisor` com foto | a virada de tema em tela cheia de imagem | 5 |
| `declaracao` | a página de silêncio: uma frase, muito ar | 6 |
| `camadas` | rótulo e leitura lado a lado — valores e a tabela do futuro | 2 |
| `colunas` | os três comportamentos, em paralelo | 1 |
| `lista` | a cultura nas pequenas decisões | 1 |
| `foto_cheia` | o princípio cultural, em tela cheia | 1 |
| `texto` | só onde o conteúdo é mesmo narrativa | 4 |

As 15 páginas do roteiro saem em 24: os cinco "ABERTURA DO TEMA" viram
divisores de verdade, e cada frase-tese que ela escreveu em negrito ganha a
sua página de silêncio em vez de ficar empilhada embaixo do parágrafo.

### Duas observações

1. O documento trazia **dois sumários** — um de capa e o do SLIDE 02. Valeu
   o do slide 02, que é o que está dentro da apresentação.
2. Os nomes citados no slide 09 — **Letícia, Mapinha e Joel** — ficaram como
   ela escreveu. Se a apresentação for para a equipe inteira, vale conferir
   se todos topam ser citados.

### As dez imagens

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `cultura-div-origem.png` | virada 01 — a primeira oficina, o lugar onde começou |
| `cultura-div-valores.png` | virada 02 — alguém concentrado no trabalho, plano fechado |
| `cultura-div-jeito-de-trabalhar.png` | virada 03 — a oficina em movimento, plano aberto |
| `cultura-div-pratica.png` | virada 04 — montagem na casa do cliente |
| `cultura-div-futuro.png` | virada 05 — um ambiente entregue, imagem de horizonte |
| `cultura-oficina-forma.png` | o ofício: marcenaria, máquina, material |
| `cultura-flavia-equipe.png` | Flávia com a equipe, liderança próxima |
| `cultura-equipe-conversa.png` | duas ou três pessoas conversando no trabalho |
| `cultura-maos-trabalho.png` | mãos, ferramenta, acabamento — detalhe fechado |
| `cultura-time-completo.png` | o time completo, tela cheia na página do princípio |

Enquanto não existirem, cada página mostra a **marcação**: a área exata com o
briefing. Quando entrarem em `assets/` com esses nomes, a marcação some e
nada muda de lugar.

```bash
python3 padrao-ka/rostos.py clientes/flavia-muccelin/assets
python3 clientes/flavia-muccelin/gerar.py cultura
padrao-ka/conferir.sh clientes/flavia-muccelin/Cultura-Organizacional-Forma-e-My-Home.pptx
```
