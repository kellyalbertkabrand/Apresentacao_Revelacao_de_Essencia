# Flávia Pereira Muccelin — FORMA e My Home

Duas entregas, dois motores.

| Arquivo | O que é | Páginas | Como gerar |
|---|---|---|---|
| `conteudo.py` | Revelação de Essência — origem identitária da fundadora | 31 | `python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin` |
| `sociedade.py` | Duas trajetórias, uma nova força — Flávia & Elandi | 26 | `python3 clientes/flavia-muccelin/gerar.py sociedade` |

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
