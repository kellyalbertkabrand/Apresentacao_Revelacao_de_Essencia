#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esqueleto da AULA: "Como transformar o livro em uma marca posicionada".
Formato: aula ao vivo de 60-75 min | Objetivo: gerar demanda para consultoria KA.
Padrao visual: MODELO YUFIL / Base Estrategica (ver MODELO-APRESENTACAO-YUFIL.md).
"""
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# ---- paleta ----
CREME=RGBColor(0xF6,0xF5,0xF0); PRETO=RGBColor(0x1A,0x1A,0x1A); PRETO0=RGBColor(0,0,0)
CORPO=RGBColor(0x7A,0x7A,0x72); AREIA=RGBColor(0xC8,0xBF,0xA8); BEGE=RGBColor(0xE8,0xE4,0xD8)
SALVIA=RGBColor(0xD4,0xD9,0xCB); BEGE2=RGBColor(0xED,0xED,0xDD); BRANCO=RGBColor(0xFF,0xFF,0xFF)
VERMELHO=RGBColor(0xFF,0x31,0x31)
F_TIT="Outfit"; F_BODY="Outfit"
EMU=914400; SW,SH=int(20*EMU),int(11.25*EMU)
ASSETS="/home/user/apresentacoes/assets"
TEXTURA=f"{ASSETS}/textura-papel.jpeg"; TRACO=f"{ASSETS}/traco.png"

prs=Presentation(); prs.slide_width=SW; prs.slide_height=SH
BLANK=prs.slide_layouts[6]
ROTEIRO=[]   # (n, titulo, nota de conducao) -> vira as notas do slide

def add_slide(grey=False):
    s=prs.slides.add_slide(BLANK)
    bg=s.background; bg.fill.solid(); bg.fill.fore_color.rgb=CREME
    if grey: s.shapes.add_picture(TEXTURA,0,0,SW,SH)
    return s

def box(s,x,y,w,h):
    tb=s.shapes.add_textbox(Emu(int(x*EMU)),Emu(int(y*EMU)),Emu(int(w*EMU)),Emu(int(h*EMU)))
    tb.text_frame.word_wrap=True; return tb,tb.text_frame

def run(p,text,size,color,font=F_BODY,bold=False,italic=False,spc=None):
    r=p.add_run(); r.text=text; r.font.size=Pt(size); r.font.name=font
    r.font.bold=bold; r.font.italic=italic; r.font.color.rgb=color
    if spc is not None: r._r.get_or_add_rPr().set('spc',str(int(spc*100)))
    return r

def rect(s,x,y,w,h,color):
    sp=s.shapes.add_shape(MSO_SHAPE.RECTANGLE,Emu(int(x*EMU)),Emu(int(y*EMU)),Emu(int(w*EMU)),Emu(int(h*EMU)))
    sp.fill.solid(); sp.fill.fore_color.rgb=color; sp.line.fill.background(); sp.shadow.inherit=False; return sp

def eyebrow(s,text,x=1.7,y=0.9):
    tb,tf=box(s,x,y,14,0.5); run(tf.paragraphs[0],text.upper(),16.5,CORPO,F_BODY,spc=2.5)

def h1(s,text,x=1.7,y=1.6,size=39,w=16.6):
    tb,tf=box(s,x,y,w,1.3); run(tf.paragraphs[0],text,size,PRETO,F_BODY,bold=True)

def paras(s,itens,x,y,w,h,size=27,color=CORPO,marker=None,mcolor=None,bold=False):
    tb,tf=box(s,x,y,w,h); first=True
    for t in itens:
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False
        if marker: run(p,marker+"  ",size,mcolor or AREIA,F_BODY,bold=True)
        run(p,t,size,color,F_BODY,bold=bold)
    return tf

def nota(s,text,y=10.15):
    """Placeholder de producao: o que a Kelly precisa completar neste slide."""
    tb,tf=box(s,1.7,y,16.6,0.6)
    run(tf.paragraphs[0],"[ "+text+" ]",15,AREIA,F_BODY,italic=True,spc=1)

def notas_slide(s,texto):
    s.notes_slide.notes_text_frame.text=texto

def cards(s,itens,y0=3.4,cols=2,cw=8.2,ch=2.6,gx=0.6,gy=0.4,x0=1.7,bg=BRANCO,
          ntam=33,ttam=24,dtam=18):
    for i,(num,tit,desc) in enumerate(itens):
        x=x0+(i%cols)*(cw+gx); y=y0+(i//cols)*(ch+gy)
        rect(s,x,y,cw,ch,bg)
        tb,tf=box(s,x+0.4,y+0.28,cw-0.8,ch-0.55)
        run(tf.paragraphs[0],num,ntam,AREIA,F_BODY,bold=True)
        run(tf.add_paragraph(),tit,ttam,PRETO,F_BODY,bold=True)
        run(tf.add_paragraph(),desc,dtam,CORPO,F_BODY)

def duas_colunas(s,tit_e,itens_e,tit_d,itens_d,y=3.2,h=6.4,size=22):
    rect(s,1.7,y,8.0,h,BRANCO)
    tb,tf=box(s,2.1,y+0.3,7.2,0.6); run(tf.paragraphs[0],tit_e,19.5,CORPO,F_BODY,bold=True,spc=1.5)
    paras(s,itens_e,2.1,y+1.1,7.2,h-1.4,size,PRETO,bold=True)
    rect(s,10.0,y,8.0,h,SALVIA)
    tb,tf=box(s,10.4,y+0.3,7.2,0.6); run(tf.paragraphs[0],tit_d,19.5,CORPO,F_BODY,bold=True,spc=1.5)
    paras(s,itens_d,10.4,y+1.1,7.2,h-1.4,size,CORPO)

def divisor(s,pre,destaque):
    tb,tf=box(s,2.2,3.9,16.6,3.6); p=tf.paragraphs[0]
    if pre: run(p,pre+" ",100,PRETO0,F_BODY)
    run(p,destaque,100,PRETO0,F_BODY,bold=True)

# =====================================================================
# ABERTURA  (0-08 min)
# =====================================================================
# 01 CAPA
s=add_slide(grey=True)
tb,tf=box(s,1.68,3.70,13.2,2.6)
run(tf.paragraphs[0],"COMO TRANSFORMAR O LIVRO",75,PRETO0,F_TIT,bold=True)
run(tf.add_paragraph(),"EM UMA MARCA POSICIONADA",75,PRETO0,F_TIT,bold=True,spc=1)
s.shapes.add_picture(TRACO,Emu(int(15.2*EMU)),Emu(int(4.0*EMU)),Emu(int(1.63*EMU)),Emu(int(1.94*EMU)))
tb,tf=box(s,1.68,6.45,14.5,0.9); p=tf.paragraphs[0]
run(p,"Uma aula para o empresário que quer ",30,PRETO,F_BODY)
run(p,"posicionar ou reposicionar a sua marca.",30,PRETO,F_BODY,bold=True)
tb,tf=box(s,1.68,8.5,9.0,1.2)
run(tf.paragraphs[0],"[MÊS/ANO]",19.5,PRETO0,F_BODY,spc=1.5)
p2=tf.add_paragraph()
run(p2,"Método ",26.5,PRETO,F_BODY); run(p2,"Marca com Essência ",26.5,PRETO,F_BODY,bold=True)
run(p2,"©",15,PRETO,F_BODY,bold=True)
notas_slide(s,"00:00 | Abertura. Nao se apresente ainda. Abra com a pergunta: 'quantos de voces ja leram um livro de negocios inteiro e nao mudaram uma virgula na empresa?' Essa e a dor que a aula resolve.")

# 02 SUMARIO
s=add_slide(grey=True)
tb,tf=box(s,1.9,0.9,10,1.6); run(tf.paragraphs[0],"O CAMINHO DE HOJE",68,PRETO0,F_TIT,bold=True)
itens=["O diagnóstico: por que marcas boas ficam invisíveis",
       "Como o livro funciona por dentro",
       "Mãos no livro: o protocolo de aplicação",
       "IA como copiloto da aplicação",
       "O que o livro resolve e o que exige acompanhamento",
       "Seu próximo passo"]
ys=[2.9,4.4,5.9]
for i,it in enumerate(itens):
    x = 1.9 if i<3 else 10.4
    y = ys[i%3]
    tb,tf=box(s,x,y,1.4,1.0); run(tf.paragraphs[0],f"{i+1:02d}",43,PRETO,F_BODY,bold=True)
    tb,tf=box(s,x+1.45,y+0.18,6.6,1.2); run(tf.paragraphs[0],it,27,CORPO,F_BODY)
notas_slide(s,"00:02 | Contrato da aula: 'em 70 minutos voce nao vai aprender sobre marca. Voce vai SAIR daqui com o Raio-X da sua marca preenchido.' Peca o livro aberto e caneta na mao.")

# 03 CITACAO DE ABERTURA
s=add_slide()
tb,tf=box(s,1.5,1.3,4,3); run(tf.paragraphs[0],"“",135,PRETO,F_BODY,bold=True)
tb,tf=box(s,3.5,3.4,13.5,4); p=tf.paragraphs[0]
run(p,"[FRASE DE ABERTURA DO LIVRO — a frase que resume a tese central, ",43,PRETO,F_BODY)
run(p,"com 3 a 5 palavras em bold]",43,PRETO,F_BODY,bold=True)
tb,tf=box(s,3.5,7.8,13.5,0.6)
run(tf.paragraphs[0],"[NOME DO LIVRO]  ·  [CAPÍTULO]",21,CORPO,F_BODY,bold=True,spc=2)
nota(s,"Escolher a frase do livro que mais provoca desconforto — não a mais bonita")
notas_slide(s,"00:04 | Leia a frase em voz alta e faca silencio de 3 segundos. Nao explique ainda.")

# 04 A PROMESSA DA AULA
s=add_slide()
eyebrow(s,"O que você leva daqui")
h1(s,"AO FINAL DESTA AULA, VOCÊ TERÁ:")
cards(s,[("01.","O diagnóstico da sua marca","Qual dos quatro sintomas de marca sem posicionamento é o seu."),
         ("02.","O mapa de leitura aplicada","Qual capítulo resolve qual problema — e em que ordem abrir."),
         ("03.","O Raio-X preenchido","Três respostas que já organizam a sua narrativa de marca."),
         ("04.","Um plano de 30 dias","O que fazer semana a semana para sair do papel.")])
notas_slide(s,"00:05 | Entregaveis concretos. Isso segura a atencao ate o fim. Repita: 'voce sai com entregavel, nao com anotacao'.")

# 05 QUEM FALA
s=add_slide()
rect(s,12.8,0,7.2,11.25,SALVIA)
eyebrow(s,"Quem conduz",1.5,1.0)
tb,tf=box(s,1.5,1.7,11,2.0)
run(tf.paragraphs[0],"[NOME]",51,PRETO,F_BODY,bold=True)
run(tf.add_paragraph(),"[ASSINATURA EM UMA LINHA]",51,PRETO,F_BODY,bold=True)
paras(s,["[Anos de estrada e o que isso te deu de leitura de mercado]",
         "[Número de marcas atendidas / setores]",
         "[Por que você escreveu este livro — a lacuna que viu]"],1.5,4.3,10.5,3,27,CORPO,marker="•")
tb,tf=box(s,1.5,7.6,10.5,1.4)
run(tf.paragraphs[0],"“[SUA FRASE DE AUTORIDADE — o que você acredita sobre marca]”",26,PRETO,F_BODY,bold=True,italic=True)
tb,tf=box(s,1.5,9.1,10.5,0.5)
run(tf.paragraphs[0],"[ATRIBUTO]  •  [ATRIBUTO]  •  [ATRIBUTO]  •  [ATRIBUTO]",18,PRETO,F_BODY,bold=True,spc=1.5)
nota(s,"Substituir foto: inserir imagem vertical no bloco verde à direita")
notas_slide(s,"00:07 | Autoridade em 90 segundos, nao em 5 minutos. Credencial que importa: resultado de cliente, nao curriculo.")

# =====================================================================
# BLOCO 1 - O DIAGNOSTICO  (08-22 min)
# =====================================================================
# 06 DIVISOR
s=add_slide(grey=True); divisor(s,"POR QUE MARCAS BOAS FICAM","INVISÍVEIS")
notas_slide(s,"00:08 | Bloco 1: o diagnostico. Objetivo: o empresario se reconhecer no problema antes de ouvir o metodo.")

# 07 EMPRESA x MARCA
s=add_slide()
eyebrow(s,"A distinção que muda tudo")
h1(s,"VOCÊ TEM UMA EMPRESA. VOCÊ TEM UMA MARCA?")
duas_colunas(s,"EMPRESA",["É o que você construiu","Existe no CNPJ e no operacional",
                          "Entrega produto e serviço","Concorre por preço e prazo",
                          "Você controla"],
               "MARCA",["É o que dizem de você quando você sai da sala",
                        "Existe na cabeça do cliente","Entrega significado e pertencimento",
                        "Concorre por preferência","Você só influencia"])
nota(s,"Puxar do capítulo do livro que trata dessa distinção")
notas_slide(s,"00:10 | Frase-chave: 'marca nao e o que voce diz que e. E o espaco que voce ocupa na cabeca de alguem.' Pergunte: 'o que dizem de voces quando voces saem da sala?'")

# 08 OS 4 SINTOMAS
s=add_slide()
eyebrow(s,"Diagnóstico")
h1(s,"OS 4 SINTOMAS DE UMA MARCA SEM POSICIONAMENTO")
cards(s,[("01.","Marca invisível","Você é bom, entrega bem — e ninguém sabe que você existe."),
         ("02.","Marca confusa","Cada peça fala uma coisa. O cliente não consegue te explicar para outro."),
         ("03.","Marca refém do preço","Sem percepção de valor, a única conversa possível é desconto."),
         ("04.","Marca inconsistente","A promessa da comunicação não bate com a experiência real.")])
notas_slide(s,"00:13 | Leia um a um e peca levantada de mao. Isso gera identificacao publica e prepara o Exercicio 1.")

# 09 POSICIONAR x REPOSICIONAR
s=add_slide()
eyebrow(s,"Duas rotas diferentes")
h1(s,"POSICIONAR OU REPOSICIONAR: QUAL É O SEU CASO?")
duas_colunas(s,"+ POSICIONAR",["Marca nova ou nunca definida","Não há percepção instalada a desfazer",
                               "O trabalho é escolher e ocupar","Risco: escolher por conveniência, não por essência",
                               "Tempo: mais curto"],
               "× REPOSICIONAR",["Marca com percepção já instalada","Há memória de mercado para reconstruir",
                                 "O trabalho é desconstruir antes de construir","Risco: abandonar o patrimônio que já tinha valor",
                                 "Tempo: mais longo, exige transição"])
nota(s,"Se o livro tem um capítulo específico sobre reposicionamento, citar aqui")
notas_slide(s,"00:16 | Regra pratica: reposicionar nao e apagar. E reinterpretar. Dar 1 exemplo real de cliente (com ou sem nome).")

# 10 O ERRO MAIS CARO
s=add_slide()
eyebrow(s,"O atalho que custa caro",2.3,2.4)
tb,tf=box(s,2.3,3.0,16,4); p=tf.paragraphs[0]
run(p,"TROCAR A ",100,PRETO,F_BODY); run(p,"LOGO",100,PRETO,F_BODY,bold=True)
p2=tf.add_paragraph()
run(p2,"NÃO É ",100,PRETO,F_BODY); run(p2,"POSICIONAR",100,PRETO,F_BODY,bold=True)
rect(s,2.5,7.5,15,0.04,AREIA)
tb,tf=box(s,2.5,7.9,15,1.7)
run(tf.paragraphs[0],"Identidade visual é consequência de estratégia. Quando vem antes, vira gosto pessoal — e gosto pessoal não sustenta preço.",30,CORPO,F_BODY)
notas_slide(s,"00:18 | Este e o slide que quebra a objecao mais comum ('ja fiz rebranding ano passado'). Ferida aberta: 'quanto voce ja gastou em visual sem mudar percepcao?'")

# 11 EXERCICIO 1
s=add_slide()
rect(s,0,0,9,11.25,BEGE2)
tb,tf=box(s,1.3,4.2,6.6,2.5)
run(tf.paragraphs[0],"EXERCÍCIO",68,PRETO,F_BODY,bold=True)
run(tf.add_paragraph(),"01",68,AREIA,F_BODY,bold=True)
eyebrow(s,"3 minutos · livro aberto",10.3,1.5)
tb,tf=box(s,10.3,2.2,8.2,1.6)
run(tf.paragraphs[0],"QUAL É O SEU SINTOMA?",45,PRETO,F_BODY,bold=True)
paras(s,["Escreva, em uma frase, o sintoma que mais te representa hoje.",
         "Escreva a última vez que um cliente te escolheu pelo preço.",
         "Escreva como você explicaria a sua marca em 10 segundos."],
      10.3,4.2,8.2,4,27,CORPO,marker="—")
tb,tf=box(s,10.3,8.3,8.2,1.4)
run(tf.paragraphs[0],"Guarde essa folha. Vamos voltar nela no final.",26,PRETO,F_BODY,bold=True)
notas_slide(s,"00:19 | 3 min de silencio real. Cronometre. Depois recolha 2 ou 3 respostas em voz alta. NAO corrija ninguem aqui.")

# =====================================================================
# BLOCO 2 - COMO O LIVRO FUNCIONA  (22-44 min)
# =====================================================================
# 12 DIVISOR
s=add_slide(grey=True); divisor(s,"COMO O LIVRO FUNCIONA","POR DENTRO")
notas_slide(s,"00:22 | Bloco 2: a arquitetura. Aqui voce ensina a LER, nao repete o conteudo do livro.")

# 13 O PRINCIPIO FUNDADOR
s=add_slide()
eyebrow(s,"O princípio que sustenta o método")
h1(s,"TODA MARCA FORTE NASCE DE DENTRO PARA FORA")
for i,(t,d,cor) in enumerate([("01. ESSÊNCIA DAS PESSOAS","Quem fundou, o que acredita, a história que originou tudo.",BRANCO),
                              ("02. CULTURA DA EMPRESA","O jeito que se formou por dentro, sem ninguém pedir.",BEGE),
                              ("03. CULTURA DA MARCA","Como o mercado enxerga tudo isso de fora.",SALVIA)]):
    y=3.3+i*2.2
    rect(s,1.7,y,16.6,1.9,cor)
    tb,tf=box(s,2.2,y+0.25,7.5,1.4); run(tf.paragraphs[0],t,27,PRETO,F_BODY,bold=True)
    tb,tf=box(s,9.5,y+0.32,8.3,1.4); run(tf.paragraphs[0],d,22,CORPO,F_BODY)
tb,tf=box(s,1.7,10.0,16.6,1.0)
run(tf.paragraphs[0],"O livro não inventa a sua marca. Ele traduz a marca que já existe.",30,PRETO,F_BODY,bold=True)
notas_slide(s,"00:24 | Base teorica: Edgar Schein (cultura organizacional). Cite sem academicismo. Frase de ouro: 'nada se inventa, tudo se traduz'.")

# 14 A JORNADA EM 5 CAMADAS
s=add_slide()
eyebrow(s,"A arquitetura do livro")
h1(s,"AS 5 CAMADAS — E POR QUE A ORDEM IMPORTA")
for i,(num,tit,desc) in enumerate([("01","ESSÊNCIA","De onde a marca vem"),
                                   ("02","ESTRATÉGIA","Que lugar ela ocupa"),
                                   ("03","PÚBLICO","Com quem ela fala"),
                                   ("04","VERBAL","Como ela diz"),
                                   ("05","ATIVAÇÃO","Onde ela aparece")]):
    x=1.7+i*3.38
    rect(s,x,3.6,3.1,4.6,BRANCO if i%2==0 else BEGE)
    tb,tf=box(s,x+0.35,3.9,2.5,3.9)
    run(tf.paragraphs[0],num,39,AREIA,F_BODY,bold=True)
    run(tf.add_paragraph(),tit,23,PRETO,F_BODY,bold=True)
    run(tf.add_paragraph(),desc,18,CORPO,F_BODY)
tb,tf=box(s,1.7,8.8,16.6,1.4); p=tf.paragraphs[0]
run(p,"Cada camada só se sustenta sobre a anterior. ",30,CORPO,F_BODY)
run(p,"Pular uma camada é o que faz o rebranding não pegar.",30,PRETO,F_BODY,bold=True)
nota(s,"Mapear aqui: qual capítulo do livro cobre cada camada")
notas_slide(s,"00:26 | Slide-mapa da aula inteira. Volte nele antes de cada camada. Peca para fotografarem.")

# 15-19 AS CINCO CAMADAS
CAMADAS=[("01","ESSÊNCIA","De onde a sua marca vem",
          ["Qual a história real de origem — não a versão de site","Em que o fundador acredita que o mercado não acredita",
           "Que fato concreto sustenta o que a marca promete"],
          "Entregável do capítulo: a sua história de origem escrita em 5 linhas.",
          "[CAPÍTULO(S) DO LIVRO]"),
         ("02","ESTRATÉGIA","Que lugar a sua marca ocupa",
          ["Posicionamento: o espaço que você escolhe ocupar na mente do cliente",
           "Golden Circle: por quê → como → o quê","Anti-território: o que a sua marca NÃO é"],
          "Entregável do capítulo: uma frase de posicionamento que o seu concorrente não poderia assinar.",
          "[CAPÍTULO(S) DO LIVRO]"),
         ("03","PÚBLICO E RELAÇÃO","Com quem a sua marca fala",
          ["Persona: não é dado demográfico, é dor, desejo e objeção",
           "Personalidade: como a marca se comporta","Arquétipo: o papel que ela ocupa na história do cliente"],
          "Entregável do capítulo: as três objeções que mais travam a sua venda.",
          "[CAPÍTULO(S) DO LIVRO]"),
         ("04","IDENTIDADE VERBAL","Como a sua marca diz o que diz",
          ["Manifesto: a declaração de crença da marca","Tom de voz: o jeito, não o assunto",
           "Bordões e vocabulário próprio: o que só você fala"],
          "Entregável do capítulo: 5 frases que só a sua marca poderia dizer.",
          "[CAPÍTULO(S) DO LIVRO]"),
         ("05","ATIVAÇÃO","Onde a sua marca aparece",
          ["Pilares de conteúdo: os temas que você tem direito de ocupar",
           "Consistência: a mesma marca em todos os pontos de contato",
           "Percepção: o que muda na cabeça de quem te vê"],
          "Entregável do capítulo: os 3 pilares de conteúdo da sua marca.",
          "[CAPÍTULO(S) DO LIVRO]")]
tempos=["00:28","00:31","00:34","00:37","00:40"]
for i,(num,tit,sub,bullets,entreg,cap) in enumerate(CAMADAS):
    s=add_slide()
    rect(s,14.6,0,5.4,11.25,SALVIA if i%2==0 else BEGE)
    tb,tf=box(s,15.1,4.3,4.4,3.0)
    run(tf.paragraphs[0],num,108,BRANCO,F_BODY,bold=True)
    eyebrow(s,f"Camada {num} · {cap}",1.5,1.0)
    tb,tf=box(s,1.5,1.6,12.6,2.4)
    run(tf.paragraphs[0],tit,51,PRETO,F_BODY,bold=True)
    run(tf.add_paragraph(),sub,30,CORPO,F_BODY)
    paras(s,bullets,1.5,4.6,12.6,3.6,25,CORPO,marker="—")
    rect(s,1.5,8.3,12.6,1.5,BRANCO)
    tb,tf=box(s,1.9,8.55,11.8,1.1)
    run(tf.paragraphs[0],entreg,24,PRETO,F_BODY,bold=True)
    nota(s,"Preencher o número do capítulo e 1 exemplo real de cliente")
    notas_slide(s,f"{tempos[i]} | Camada {num}. Regra: 1 conceito + 1 exemplo + 1 pergunta para a plateia. Nao passe de 3 minutos por camada.")

# 20 A REGRA DE OURO
s=add_slide()
eyebrow(s,"A regra que salva o projeto",2.3,2.6)
tb,tf=box(s,2.3,3.2,16,4); p=tf.paragraphs[0]
run(p,"NÃO PULE ",100,PRETO,F_BODY); run(p,"CAMADA",100,PRETO,F_BODY,bold=True)
rect(s,2.5,6.5,15,0.04,AREIA)
tb,tf=box(s,2.5,6.9,15,2.2)
run(tf.paragraphs[0],"Toda marca que “já tentou se posicionar e não funcionou” começou por uma camada de cima. Identidade verbal sem essência vira texto bonito. Conteúdo sem posicionamento vira volume sem lucro.",30,CORPO,F_BODY)
notas_slide(s,"00:43 | Este e o slide que justifica a consultoria mais tarde. Plante aqui, colha no Bloco 5.")

# =====================================================================
# BLOCO 3 - MAOS NO LIVRO  (44-56 min)
# =====================================================================
# 21 DIVISOR
s=add_slide(grey=True); divisor(s,"MÃOS NO","LIVRO")
notas_slide(s,"00:44 | Bloco 3: do conceito para o protocolo. Aqui a aula vira oficina.")

# 22 O PROTOCOLO
s=add_slide()
eyebrow(s,"Como ler para aplicar")
h1(s,"O PROTOCOLO DE LEITURA APLICADA")
cards(s,[("01.","Leia com caneta, não com marca-texto","Marca-texto guarda. Caneta decide. Escreva a sua resposta na margem."),
         ("02.","Um capítulo = um entregável","Não avance sem ter produzido o entregável daquele capítulo."),
         ("03.","Responda pela marca, não por você","A pergunta não é o que você acha. É o que a marca já é."),
         ("04.","Valide antes de publicar","Time, cliente antigo e cliente perdido. Nessa ordem.")])
notas_slide(s,"00:45 | Diferencial da aula: voce esta ensinando METODO DE USO, nao resumindo o livro. Diga isso em voz alta.")

# 23 AS PERGUNTAS QUE DESTRAVAM
s=add_slide()
eyebrow(s,"Quando travar")
h1(s,"AS 6 PERGUNTAS QUE DESTRAVAM QUALQUER CAPÍTULO")
perg=["O que a minha marca faz que ninguém mais faz do mesmo jeito?",
      "Se eu sumisse amanhã, o que faria falta no meu mercado?",
      "Por que o meu melhor cliente ficou?",
      "Por que o cliente que eu perdi foi embora?",
      "O que eu me recuso a fazer, mesmo dando dinheiro?",
      "O que eu quero que digam de mim quando eu não estiver na sala?"]
for i,q in enumerate(perg):
    x=1.7+(i%2)*8.8; y=3.3+(i//2)*2.2
    rect(s,x,y,8.0,1.9,BRANCO)
    tb,tf=box(s,x+0.4,y+0.35,0.9,1.2); run(tf.paragraphs[0],f"{i+1:02d}",27,AREIA,F_BODY,bold=True)
    tb,tf=box(s,x+1.4,y+0.35,6.3,1.3); run(tf.paragraphs[0],q,21,PRETO,F_BODY,bold=True)
notas_slide(s,"00:48 | Peca para fotografarem. Este slide costuma virar print compartilhado — e uma isca organica.")

# 24 EXERCICIO 2
s=add_slide()
rect(s,0,0,9,11.25,BEGE2)
tb,tf=box(s,1.3,4.2,6.6,2.5)
run(tf.paragraphs[0],"EXERCÍCIO",68,PRETO,F_BODY,bold=True)
run(tf.add_paragraph(),"02",68,AREIA,F_BODY,bold=True)
eyebrow(s,"6 minutos · o entregável da aula",10.3,1.3)
tb,tf=box(s,10.3,2.0,8.2,1.6)
run(tf.paragraphs[0],"O RAIO-X DA SUA MARCA",45,PRETO,F_BODY,bold=True)
paras(s,["ORIGEM — Por que esta marca existe, além de dar lucro?",
         "LUGAR — Que espaço só ela pode ocupar no seu mercado?",
         "PROVA — Que fato concreto sustenta isso hoje?"],
      10.3,4.0,8.2,4,27,PRETO,marker="—",bold=True)
tb,tf=box(s,10.3,8.0,8.2,2.0)
run(tf.paragraphs[0],"Se você não consegue responder a terceira, o problema não é comunicação. É estratégia.",26,CORPO,F_BODY)
notas_slide(s,"00:50 | Coracao da aula. 6 min cronometrados. Depois, 3 voluntarios leem em voz alta e VOCE devolve leitura ao vivo — e aqui que a consultoria se vende sozinha.")

# 25 OS 3 ERROS
s=add_slide()
eyebrow(s,"O que trava a aplicação")
h1(s,"OS 3 ERROS DE QUEM APLICA SOZINHO")
duas_colunas(s,"× O ERRO",["Responder o que soa bonito","Copiar o posicionamento do concorrente",
                           "Fazer sozinho, dentro da própria cabeça","Mudar tudo de uma vez",
                           "Parar na definição"],
               "+ A CORREÇÃO",["Responder o que é verificável na operação",
                               "Procurar o espaço que o concorrente deixou vazio",
                               "Validar com quem compra e com quem não comprou",
                               "Transição com marcos e datas",
                               "Definição só vira marca quando vira rotina"])
notas_slide(s,"00:56 | Prepare o terreno da oferta sem vender ainda. 'Fazer sozinho dentro da propria cabeca' e a objecao central.")

# =====================================================================
# BLOCO 4 - IA COMO COPILOTO  (58-64 min)
# =====================================================================
# 26 DIVISOR
s=add_slide(grey=True); divisor(s,"IA COMO COPILOTO","DA APLICAÇÃO")
notas_slide(s,"00:58 | Bloco 4: diferencial competitivo da aula. Ninguem no mercado de branding esta ensinando isso direito.")

# 27 O QUE A IA FAZ / NAO FAZ
s=add_slide()
eyebrow(s,"O limite certo da ferramenta")
h1(s,"A IA ACELERA A TRADUÇÃO. ELA NÃO CRIA A ESSÊNCIA.")
duas_colunas(s,"+ O QUE A IA FAZ BEM",["Organizar respostas cruas em estrutura",
                                        "Gerar 20 versões de uma frase para você escolher 1",
                                        "Ler avaliações e achar padrões de percepção",
                                        "Checar consistência entre peças",
                                        "Simular objeções do seu cliente"],
               "× O QUE A IA NUNCA FARÁ",["Saber por que você fundou a empresa",
                                          "Ter acesso ao que só o seu time viveu",
                                          "Decidir o que você se recusa a fazer",
                                          "Assumir o risco de uma escolha de posicionamento",
                                          "Substituir a validação com gente real"])
notas_slide(s,"01:00 | Frase-chave: 'IA nao tem essencia. Ela tem padrao. Essencia e o que voce vive; padrao e o que todo mundo ja escreveu.'")

# 28 4 USOS PRATICOS
s=add_slide()
eyebrow(s,"Do livro para a prática, com IA")
h1(s,"4 USOS PRÁTICOS COM O LIVRO NA MÃO")
cards(s,[("01.","Transcrever e destilar","Grave 20 min falando sobre a origem da marca. Peça à IA para extrair crenças e repetições."),
         ("02.","Espelho de percepção","Cole avaliações, prints e DMs. Peça o mapa do que o mercado já pensa de você."),
         ("03.","Gerador de variações","Dê a sua frase de posicionamento e peça 20 versões — escolha, não aceite."),
         ("04.","Auditor de consistência","Suba suas últimas 10 peças e pergunte: isso soa como a mesma marca?")])
nota(s,"Se quiser, entregar os 4 prompts prontos como bônus da aula")
notas_slide(s,"01:02 | Oferta de bonus: os 4 prompts prontos em troca do e-mail/WhatsApp. Melhor ponto de captura de lead da aula.")

# =====================================================================
# BLOCO 5 - O SALTO  (64-72 min)
# =====================================================================
# 29 DIVISOR
s=add_slide(grey=True); divisor(s,"O QUE O LIVRO RESOLVE","E O QUE NÃO")
notas_slide(s,"01:04 | Bloco 5: a oferta. Tom de honestidade, nao de pitch. Voce esta qualificando, nao empurrando.")

# 30 SOZINHO x COM ACOMPANHAMENTO
s=add_slide()
eyebrow(s,"Honestidade sobre o alcance do livro")
h1(s,"DOIS CAMINHOS LEGÍTIMOS")
duas_colunas(s,"+ O LIVRO RESOLVE SOZINHO",["Clareza sobre o que é marca e o que não é",
                                             "Diagnóstico do próprio sintoma",
                                             "Primeira versão da essência e do posicionamento",
                                             "Linguagem comum com o seu time",
                                             "Critério para não gastar errado"],
               "× O QUE EXIGE ACOMPANHAMENTO",["Enxergar o que você não consegue ver de dentro",
                                               "Decidir entre dois caminhos igualmente bons",
                                               "Reposicionamento com patrimônio de marca em jogo",
                                               "Alinhar sócios que discordam",
                                               "Transformar definição em rotina que se sustenta"])
notas_slide(s,"01:05 | Nao ataque o 'sozinho'. Valide. Quem se ve na coluna da direita se autoqualifica — e esses sao os seus clientes.")

# 31 COMO O ESCRITORIO TRABALHA
s=add_slide()
eyebrow(s,"Quando faz sentido chamar o escritório")
h1(s,"COMO CONDUZIMOS UM PROCESSO COMPLETO")
for i,(num,tit,desc) in enumerate([("01","LAPIDAÇÃO DE ESSÊNCIA","Entrevistas com sócios e mapeamento cultural."),
                                   ("02","BASE ESTRATÉGICA","Causa, posicionamento, arquétipo e pilares."),
                                   ("03","IDENTIDADE VERBAL","Manifesto, tom de voz e léxico próprio."),
                                   ("04","PLANO DE COMUNICAÇÃO","Pilares, calendário e ativação de percepção.")]):
    x=1.7+i*4.23
    rect(s,x,3.6,3.95,4.6,BRANCO if i%2==0 else BEGE)
    tb,tf=box(s,x+0.4,3.9,3.2,3.9)
    run(tf.paragraphs[0],num,39,AREIA,F_BODY,bold=True)
    run(tf.add_paragraph(),tit,21,PRETO,F_BODY,bold=True)
    run(tf.add_paragraph(),desc,18,CORPO,F_BODY)
tb,tf=box(s,1.7,8.9,16.6,1.2)
run(tf.paragraphs[0],"[FRASE DE FECHAMENTO DO SEU MÉTODO — o resultado que o cliente leva]",27,CORPO,F_BODY)
nota(s,"Ajustar as 4 etapas ao seu escopo atual e incluir prazo médio")
notas_slide(s,"01:07 | Mostre o processo, nao o preco. Preco e conversa individual. Aqui voce so instala a percepcao de metodo.")

# 32 O PROXIMO PASSO
s=add_slide()
rect(s,10.6,0,9.4,11.25,BEGE2)
eyebrow(s,"Seu próximo passo",1.5,1.6)
tb,tf=box(s,1.5,2.3,8.6,2.6)
run(tf.paragraphs[0],"VOLTE NA FOLHA",51,PRETO,F_BODY,bold=True)
run(tf.add_paragraph(),"DO EXERCÍCIO 01",51,PRETO,F_BODY,bold=True)
paras(s,["Releia o sintoma que você escreveu no começo da aula.",
         "Compare com o Raio-X que você acabou de preencher.",
         "A distância entre os dois é exatamente o seu trabalho de marca."],
      1.5,5.6,8.6,3.2,27,CORPO,marker="—")
eyebrow(s,"Se quiser conduzir isso comigo",11.2,2.3)
tb,tf=box(s,11.2,3.0,7.8,1.6)
run(tf.paragraphs[0],"[CHAMADA PARA AÇÃO]",39,PRETO,F_BODY,bold=True)
paras(s,["[O que a pessoa faz agora: link, QR code, WhatsApp]",
         "[O que ela recebe: diagnóstico, conversa, proposta]",
         "[Prazo ou limite de vagas, se houver]"],
      11.2,4.9,7.8,3.5,24,CORPO,marker="—")
nota(s,"Inserir QR code no bloco à direita")
notas_slide(s,"01:09 | Fechamento do circulo aberto no Exercicio 1. Convite direto, uma vez so, sem repetir tres vezes.")

# 33 MANIFESTO FINAL
s=add_slide()
eyebrow(s,"Para levar daqui",2.3,2.6)
tb,tf=box(s,2.3,3.2,16,4); p=tf.paragraphs[0]
run(p,"MARCA NÃO SE ",100,PRETO,F_BODY); run(p,"LÊ.",100,PRETO,F_BODY,bold=True)
p2=tf.add_paragraph()
run(p2,"MARCA SE ",100,PRETO,F_BODY); run(p2,"CONSTRÓI.",100,PRETO,F_BODY,bold=True)
rect(s,2.5,7.4,15,0.04,AREIA)
tb,tf=box(s,2.5,7.8,15,1.7)
run(tf.paragraphs[0],"O livro te dá o método. A decisão de aplicar é a única parte que ninguém faz por você.",30,CORPO,F_BODY)
notas_slide(s,"01:11 | Pausa. Deixe o slide no ar enquanto abre para perguntas.")

# 34 ENCERRAMENTO
s=add_slide()
tb,tf=box(s,1.7,4.0,16,2); run(tf.paragraphs[0],"MUITO OBRIGADA!",70,PRETO0,F_TIT)
tb,tf=box(s,1.7,6.2,14,1.6)
run(tf.paragraphs[0],"Se esta aula mudou uma decisão sua sobre a sua marca, ela já pagou o tempo que você investiu aqui.",30,PRETO,F_BODY)
tb,tf=box(s,1.7,8.2,14,0.8)
run(tf.paragraphs[0],"[SEU @ · SEU SITE · SEU CONTATO]",24,CORPO,F_BODY,spc=1.5)
notas_slide(s,"01:13 | Encerre no horario. Ultima frase dita em voz alta deve ser o convite, nao o agradecimento.")

out="/home/user/apresentacoes/AULA-LIVRO-POSICIONAMENTO.pptx"
prs.save(out)
print("salvo:",out,"| slides:",len(prs.slides._sldIdLst))
