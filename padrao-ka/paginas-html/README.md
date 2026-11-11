# Páginas HTML do Padrão KA

`ka_gerador.py` é a biblioteca de arquétipos do **Padrão KA de apresentações**
— o mesmo desenho dos decks que vivem num artefato do tipo Slides: papel
`#F8F7F2`, marinho `#152535` só nas viradas, caramelo `#D86F2A`, Outfit,
margem de 108px, rodapé com pílula e assinatura.

Cada função devolve o HTML de um slide de 1920 × 1080, pronto para o artefato
**ou** para virar PowerPoint editável com `padrao-ka/slides-para-pptx/`.

## Os arquétipos

| Função | Quando usar |
|---|---|
| `pg_abertura` | A folha de rosto, só com as duas assinaturas. |
| `pg_capa` | Título em dois pesos, assinatura do cliente, método e data. |
| `pg_sumario` | As seções numeradas, em duas colunas. |
| `pg_divisor` | Virada de seção: marinho, número, nome em 120px e a foto à direita. |
| `pg_texto` | Um título e um bloco de texto. O arroz com feijão. |
| `pg_camadas` | Rótulo e texto lado a lado, separados por filete. Nunca empilhados. |
| `pg_cartoes` | Dois a quatro cartões claros, lado a lado. |
| `pg_caixa` | Um cartão grande com rótulo, frase e explicação. |
| `pg_chips` | Uma fileira de pílulas curtas — atributos, etapas, palavras. |
| `pg_lista` | Itens marcados com a barra caramelo, em colunas. |
| `pg_frase` | Página-manifesto em marinho, com ou sem foto. |
| `pg_manifesto` | O manifesto da marca, respirado. |
| `pg_obrigada` | O fecho, com as assinaturas e o desenho em traço. |

## Como usar

```python
import sys; sys.path.insert(0, 'padrao-ka/paginas-html')
from ka_gerador import *

rod = rodape('BASE ESTRATÉGICA', 'LUCAS MARTINI')
gravar('meu-deck', 'pilares', pg_camadas('pilares', 'PILARES DA **MARCA**', [
    ('PROTEÇÃO', 'Preservar o que foi construído.'),
    ('PLANEJAMENTO', 'Antecipar riscos e criar alternativas.')], rod))
```

O `**` marca o negrito do título em dois pesos — a assinatura do formato.
A pasta precisa de `project/deck.json` (com a `order`), `assets/` e um
`mapa.json` ligando o id de cada blob ao arquivo. Depois:

```bash
node    padrao-ka/slides-para-pptx/conferir.js    meu-deck   # mede e acusa vazamento
node    padrao-ka/slides-para-pptx/extrair.js     meu-deck
node    padrao-ka/slides-para-pptx/ilustracoes.js meu-deck
python3 padrao-ka/slides-para-pptx/montar.py      meu-deck saida.pptx
```

`conferir.js` é obrigatório antes de entregar: ele acusa qualquer elemento que
passe da margem ou estoure a própria caixa.

Referência viva: `clientes/lucas-martini/revelacao_ka.py` (29 páginas) e
`clientes/lucas-martini/base_estrategica_ka.py` (19 páginas).
