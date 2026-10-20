# Flávia Pereira Muccelin — FORMA e My Home

Duas entregas, dois motores.

| Arquivo | O que é | Páginas | Como gerar |
|---|---|---|---|
| `conteudo.py` | Revelação de Essência — origem identitária da fundadora | 31 | `python3 modelos/revelacao-de-essencia/gerar.py clientes/flavia-muccelin` |
| `sociedade.py` | Duas trajetórias. Uma nova força. — Flávia & Elande | 20 | `python3 clientes/flavia-muccelin/gerar.py sociedade` |

A Revelação tem **roteiro fixo** e gerador próprio. A apresentação da
sociedade tem roteiro próprio e usa o **roteiro declarativo**
([`padrao-ka/ROTEIRO-DECLARATIVO.md`](../../padrao-ka/ROTEIRO-DECLARATIVO.md)).

A identidade visual é a mesma nas duas, e é a mesma do Lucas: painel claro
sobre a textura de ondas, Outfit, acento terracota.

---

## Duas trajetórias. Uma nova força.

Documento de alinhamento societário entre Flávia e Elande, para a FORMA e a
My Home. O conteúdo veio da Kelly em 10 slides; sai aqui em 20 páginas, e a
razão é a regra dela:

> "Um título e um texto num slide."

Cada slide do documento carregava até quatro blocos — rótulo, atributos,
lista, citação e fecho. Empilhar os quatro é exatamente o que a regra
proíbe, então cada bloco virou a sua própria página. O texto é o dela,
palavra por palavra, na ordem dela.

**Sem rodapé** (`RODAPE = False`): sem a pílula `DOCUMENTO | MARCA` e sem o
logo KA no pé, como ela pediu.

### Uma correção de ordem, assinalada

No documento original o sumário lista *Papéis e responsabilidades* em 04,
mas o slide correspondente aparece **depois** de *Onde nasce a potência* e
de *Os pontos de atenção*. O sumário aqui foi renumerado para seguir a ordem
da narrativa escrita. Se a ordem certa for a do sumário, é trocar a posição
de três páginas em `sociedade.py` — cinco minutos.

### As imagens ainda não existem

Quatro páginas pedem fotografia e trazem a **marcação**: a área exata que a
imagem vai ocupar, com o briefing do que entra ali.

| Arquivo esperado em `assets/` | O que é |
|---|---|
| `sociedade-flavia-retrato.png` | retrato da Flávia, meio corpo |
| `sociedade-elande-retrato.png` | retrato do Elande, mesmo enquadramento |
| `sociedade-flavia-elande.png` | os dois em conversa de trabalho |
| `sociedade-rotina-noite.png` | a mesa de trabalho em casa, à noite |

Quando esses arquivos entrarem em `assets/` com esses nomes, **a marcação
desaparece sozinha e nada muda de lugar**. Depois de colocá-los, rodar o
mapa de rostos para que o corte nunca decepe ninguém:

```bash
python3 padrao-ka/rostos.py clientes/flavia-muccelin/assets
python3 clientes/flavia-muccelin/gerar.py sociedade
python3 padrao-ka/conferir_rostos.py \
    clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elande.pptx \
    clientes/flavia-muccelin/assets
```

### Conferência

```bash
padrao-ka/conferir.sh clientes/flavia-muccelin/Duas-Trajetorias-Uma-Nova-Forca-Flavia-e-Elande.pptx
```
