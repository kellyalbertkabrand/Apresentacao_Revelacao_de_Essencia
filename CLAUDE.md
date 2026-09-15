# CLAUDE.md — Instruções do projeto

Repositório das apresentações do **KA · Inteligência para Marcas**
(Kelly Albert). Duas camadas, sempre nesta ordem:

| Camada | O que define | Onde está |
|---|---|---|
| **1. Padrão de layout** | a aparência de **todas** as apresentações do KA | `padrao-ka/` |
| **2. Modelo de apresentação** | o roteiro e o conteúdo de **um tipo** de entrega | `modelos/<tipo>/` |
| **3. Cliente** | os textos e as fotos de **um** projeto | `clientes/<cliente>/` |

O layout nunca muda de um tipo de apresentação para outro. O que muda é o
roteiro.

---

## Gatilho: "padrão KA" / "modelo padrão" / "layout padrão"

Qualquer pedido de gerar apresentação **sem outro modelo especificado** usa o
padrão KA. Não inventar outro estilo.

1. Ler **`padrao-ka/SISTEMA-VISUAL.md`** — grade, paleta, tipografia,
   os sete arquétipos de página e os assets.
2. Montar com **`padrao-ka/ka_layout.py`**, que já traz tudo isso pronto.
   Não redesenhar o sistema; usar os arquétipos.
3. **Conferir antes de entregar** — obrigatório:
   ```bash
   padrao-ka/conferir.sh <arquivo>.pptx
   ```
   Ele acusa qualquer texto que passe do fundo do painel (9,60") e deixa a
   prévia em PNG para inspeção visual.
4. Commitar no branch de trabalho e entregar o `.pptx` com `SendUserFile`.

## Gatilho: "revelação de essência"

Primeira etapa do Método Marca com Essência ©.

1. Ler **`modelos/revelacao-de-essencia/MODELO.md`** — a tese, as seis seções,
   o roteiro página a página e o contrato do `conteudo.py`.
2. Criar `clientes/<cliente>/` (copiando `clientes/flavia-muccelin/` como
   referência), preencher o `conteudo.py` e colocar as fotos em `assets/`.
3. Gerar:
   ```bash
   python3 modelos/revelacao-de-essencia/gerar.py clientes/<cliente>
   ```

Referência viva e completa: `clientes/flavia-muccelin/` — 31 slides,
aprovado pela Kelly.

---

## Regras visuais inegociáveis

Detalhe completo em `padrao-ka/SISTEMA-VISUAL.md`. O essencial:

- Formato 16:9 — 20" × 11,25".
- Textura de ondas no fundo de todo slide; painel claro `#F7F5F0` de cantos
  arredondados por cima, recuado 1,10", com o fundo em **9,60"**.
- **Fonte única: Outfit**, nas variantes nomeadas. Nada de Calibri, Playfair
  ou IBM Plex. O peso vem do **nome** da fonte, nunca de negrito sintético.
- **O filete organiza a página, não a caixa.** Encher de cartõezinhos foi
  exatamente o que a Kelly rejeitou como "grosseiro, pouco elegante".
- Hierarquia por **escala e ar**, não por peso: título grande em caixa baixa e
  peso leve. Caixa alta só na capa, nos rótulos miúdos e no rodapé.
- Um único acento quente, o terracota `#A9724A`, em filetes curtos, pontos de
  lista e numerais. Nunca em área grande.
- Círculos de contorno fino, **nunca preenchidos**.
- Rodapé: pílula `DOCUMENTO | MARCA` à esquerda, logo KA à direita. Sem número
  de página.
- Escala tipográfica fechada — não inventar tamanho fora da tabela.

## Quando o texto não couber

Cortar texto, **não** diminuir o corpo da fonte. Se não coube, o slide está
dizendo duas coisas — quebrar em duas páginas, como o gerador já faz com as
experiências formadoras e com a tabela de tensões.

## Ambiente

LibreOffice Impress **está instalado e funciona** — usar para conferir o
resultado, sempre. Para a prévia em imagem, trocar `Outfit 2 Semi-Bold` por
`Outfit 2 SemiBold` **numa cópia** antes de converter: o fontconfig local não
casa o nome com hífen e substitui por DejaVu Sans, fazendo a prévia mentir
sobre o peso. O arquivo entregue nunca é alterado.

## `arquivo/`

Material anterior ao padrão KA atual (modelo YUFIL, gerador da primeira
versão da Revelação de Essência). Mantido só como histórico — **não usar como
base para nada novo**.
