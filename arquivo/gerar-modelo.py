#!/usr/bin/env python3
# Gera .pptx modelo reproduzindo fielmente o padrao visual da apresentacao YUFIL.
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ---- paleta ----
CREME=RGBColor(0xF6,0xF5,0xF0); PRETO=RGBColor(0x1A,0x1A,0x1A); PRETO0=RGBColor(0,0,0)
CORPO=RGBColor(0x7A,0x7A,0x72); AREIA=RGBColor(0xC8,0xBF,0xA8); BEGE=RGBColor(0xE8,0xE4,0xD8)
SALVIA=RGBColor(0xD4,0xD9,0xCB); BEGE2=RGBColor(0xED,0xED,0xDD); BRANCO=RGBColor(0xFF,0xFF,0xFF)
VERMELHO=RGBColor(0xFF,0x31,0x31)
F_TIT="Outfit"; F_BODY="Outfit"
EMU=914400; SW,SH=int(20*EMU),int(11.25*EMU)
ASSETS="/home/user/apresentacoes/assets"
TEXTURA=f"{ASSETS}/textura-papel.jpeg"; TRACO=f"{ASSETS}/traco.png"; LOGO=f"{ASSETS}/logo-ka.png"

prs=Presentation(); prs.slide_width=SW; prs.slide_height=SH
BLANK=prs.slide_layouts[6]

def add_slide(grey=False):
    s=prs.slides.add_slide(BLANK)
    bg=s.background; bg.fill.solid(); bg.fill.fore_color.rgb=CREME   # gelo (padrão)
    if grey:                          # só divisores de tema: textura cinza tela cheia
        s.shapes.add_picture(TEXTURA,0,0,SW,SH)
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

def footer(s):                        # sem rodape nem logotipo (a pedido)
    pass

def eyebrow(s,text,x=1.7,y=0.9):
    tb,tf=box(s,x,y,12,0.5); run(tf.paragraphs[0],text.upper(),16.5,CORPO,F_BODY,spc=2.5)

# =====================================================================
# 1. CAPA  (fundo CINZA, texto 75/75, traço decorativo, assinatura)
# =====================================================================
s=add_slide(grey=True)
tb,tf=box(s,1.68,3.93,12.2,2.4)
run(tf.paragraphs[0],"BASE ESTRATÉGICA DA MARCA",75,PRETO0,F_TIT,bold=True)
run(tf.add_paragraph(),"YUFIL",75,PRETO0,F_TIT,bold=True,spc=1)
s.shapes.add_picture(TRACO,Emu(int(13.07*EMU)),Emu(int(4.13*EMU)),Emu(int(1.63*EMU)),Emu(int(1.94*EMU)))
tb,tf=box(s,1.68,6.37,13.0,0.9); p=tf.paragraphs[0]
run(p,"Construção estratégica para ",30,PRETO,F_BODY)
run(p,"clareza, consistência e expansão.",30,PRETO,F_BODY,bold=True)
tb,tf=box(s,1.68,8.52,8.7,1.1)
run(tf.paragraphs[0],"MARÇO/2026",19.5,PRETO0,F_BODY,spc=1.5)
p2=tf.add_paragraph()
run(p2,"Método ",26.5,PRETO,F_BODY)
run(p2,"Marca com Essência ",26.5,PRETO,F_BODY,bold=True)
run(p2,"©",15,PRETO,F_BODY,bold=True)

# =====================================================================
# 2. SUMÁRIO  (fundo CINZA, geometria exata: 5 itens esq + 4 dir)
# =====================================================================
s=add_slide(grey=True)
tb,tf=box(s,1.9,0.9,10,1.6); run(tf.paragraphs[0],"SUMÁRIO",78,PRETO0,F_TIT,bold=True)
itens=["Leitura do momento da marca","Definição central da marca","Causa, liderança e tribo",
       "Golden Circle","Proposta de valor e posicionamento","Arquitetura de marca",
       "Territórios, pilares e público","Personalidade e tom de voz","Manifesto e síntese final"]
ys_esq=[2.62,3.78,4.94,6.10,7.26]; ys_dir=[2.62,3.85,5.08,6.55]
for i,it in enumerate(itens):
    if i<5: x,y=1.9,ys_esq[i]
    else:   x,y=10.61,ys_dir[i-5]
    tb,tf=box(s,x,y,1.4,1.0); run(tf.paragraphs[0],f"{i+1:02d}",43,PRETO,F_BODY,bold=True)
    tb,tf=box(s,x+1.45,y+0.18,6.8,1.0); run(tf.paragraphs[0],it,30,CORPO,F_BODY)
footer(s)

# =====================================================================
# 3. DIVISOR DE SEÇÃO  (= slide 14 original: fundo CINZA + texto gigante 100pt)
# =====================================================================
s=add_slide(grey=True)
tb,tf=box(s,2.53,4.31,16.35,2.84); p=tf.paragraphs[0]
run(p,"O MOMENTO ATUAL DA ",100,PRETO0,F_BODY,bold=True)
run(p,"YUFIL",100,PRETO0,F_BODY,bold=True)
footer(s)

# =====================================================================
# 4. CITAÇÃO
# =====================================================================
s=add_slide()
tb,tf=box(s,1.5,1.3,4,3); run(tf.paragraphs[0],"“",135,PRETO,F_BODY,bold=True)
tb,tf=box(s,3.5,3.5,13,4); p=tf.paragraphs[0]
run(p,"A YUFIL ",43,PRETO,F_BODY); run(p,"não nasce ",43,PRETO,F_BODY,bold=True)
run(p,"de uma oportunidade de mercado. Ela nasce do encontro entre ",43,PRETO,F_BODY)
run(p,"duas forças complementares.",43,PRETO,F_BODY,bold=True)
tb,tf=box(s,3.5,7.6,13,0.6)
run(tf.paragraphs[0],"ESSÊNCIA HUMANA + DIREÇÃO DE PROJETO",21,CORPO,F_BODY,bold=True,spc=2)
footer(s)

# =====================================================================
# 5. PERFIL / ESSÊNCIA
# =====================================================================
s=add_slide()
rect(s,12.8,0,7.2,11.25,SALVIA)
eyebrow(s,"Essência dos fundadores",1.5,1.0)
tb,tf=box(s,1.5,1.7,11,1.8)
run(tf.paragraphs[0],"A FORÇA QUE ORIGINA",51,PRETO,F_BODY,bold=True)
run(tf.add_paragraph(),"E TRANSFORMA",51,PRETO,F_BODY,bold=True)
tb,tf=box(s,1.5,4.0,10.5,3)
for t in ["37 anos dentro do salão — a técnica que veio da prática.",
          "A leitura concreta das dores do cabelo e da rotina.",
          "A visão de uma linha técnica para casa."]:
    p=tf.add_paragraph() if tf.paragraphs[0].runs else tf.paragraphs[0]
    run(p,"•  "+t,27,CORPO,F_BODY)
tb,tf=box(s,1.5,7.2,10.5,1.4)
run(tf.paragraphs[0],"“A mesma tesoura que tirou a minha visão foi a ferramenta que mudou a minha vida.”",
    26,PRETO,F_BODY,bold=True,italic=True)
tb,tf=box(s,1.5,8.9,10.5,0.5)
run(tf.paragraphs[0],"TÉCNICA  •  INOVAÇÃO  •  ORIGEM  •  AUTORIDADE",18,PRETO,F_BODY,bold=True,spc=1.5)
footer(s)

# =====================================================================
# 6. DECLARAÇÃO COM IMAGEM
# =====================================================================
s=add_slide()
rect(s,0,0,9,11.25,BEGE2)
eyebrow(s,"Leitura do momento",10.3,1.4)
tb,tf=box(s,10.3,2.1,8.2,1.2); run(tf.paragraphs[0],"O INSIGHT DA YUFIL",51,PRETO,F_BODY,bold=True)
tb,tf=box(s,10.3,3.6,8.2,4.5)
for t in ["cabelos difíceis de tratar","rotinas cada vez mais complicadas",
          "excesso de produto sem resultado real","promessas que não se sustentam"]:
    p=tf.add_paragraph() if tf.paragraphs[0].runs else tf.paragraphs[0]
    run(p,"✕  ",27,VERMELHO,F_BODY,bold=True); run(p,t,27,PRETO0,F_BODY)
tb,tf=box(s,10.3,7.6,8.2,1.5); p=tf.paragraphs[0]
run(p,"O problema não é a falta de produto. É o ",30,PRETO0,F_BODY,bold=True)
run(p,"excesso no cuidado.",30,AREIA,F_BODY,bold=True)
footer(s)

# =====================================================================
# 7. MANIFESTO GIGANTE
# =====================================================================
s=add_slide()
eyebrow(s,"Essência da YUFIL",2.3,2.4)
tb,tf=box(s,2.3,3.0,15.4,4); p=tf.paragraphs[0]
run(p,"CUIDADO REAL ",100,PRETO,F_BODY); run(p,"PARA A ",100,PRETO,F_BODY)
run(p,"VIDA REAL",100,PRETO,F_BODY,bold=True)
rect(s,2.5,6.6,15,0.04,AREIA)
tb,tf=box(s,2.5,7.1,15,1.7)
run(tf.paragraphs[0],"A YUFIL nasce da experiência prática de quem vive o cuidado todos os dias.",30,CORPO,F_BODY)
footer(s)

# =====================================================================
# 8. CARTÕES / GRADE
# =====================================================================
s=add_slide()
eyebrow(s,"Proposta de valor",1.5,1.0)
tb,tf=box(s,1.5,1.6,16,1.2); run(tf.paragraphs[0],"O QUE A YUFIL ENTREGA",39,PRETO,F_BODY,bold=True)
cards=[("01.","Autoridade técnica","Fórmulas com base em 37 anos de prática real."),
       ("02.","Formato concentrado","Menos produto, menos volume, menos descarte."),
       ("03.","Experiência que não pesa","Cuidar sem que vire um ritual cansativo."),
       ("04.","Coerência que fideliza","A marca faz o que diz, sem hipérboles.")]
cw,ch,gx,gy,x0,y0=8.2,2.6,0.6,0.4,1.5,3.4
for i,(num,tit,desc) in enumerate(cards):
    x=x0+(i%2)*(cw+gx); y=y0+(i//2)*(ch+gy)
    rect(s,x,y,cw,ch,BRANCO)
    tb,tf=box(s,x+0.4,y+0.3,cw-0.8,ch-0.6)
    run(tf.paragraphs[0],num,33,AREIA,F_BODY,bold=True)
    run(tf.add_paragraph(),tit,24,PRETO,F_BODY,bold=True)
    run(tf.add_paragraph(),desc,18,CORPO,F_BODY)
footer(s)

# =====================================================================
# 9. COMPARAÇÃO EM DUAS COLUNAS
# =====================================================================
s=add_slide()
eyebrow(s,"Identidade da marca",1.7,1.0)
tb,tf=box(s,1.7,1.6,16,1.2); run(tf.paragraphs[0],"O QUE A MARCA...",39,PRETO,F_BODY,bold=True)
rect(s,1.7,3.2,8.0,6.4,BRANCO)
tb,tf=box(s,2.1,3.5,7.2,0.6); run(tf.paragraphs[0],"+ VALORIZA",19.5,CORPO,F_BODY,bold=True,spc=1.5)
tb,tf=box(s,2.1,4.3,7.2,5)
for t in ["Inovação real de formato","Clareza e honestidade","Estética funcional e limpa",
          "Inteligência na rotina","Sustentabilidade coerente"]:
    p=tf.add_paragraph() if tf.paragraphs[0].runs else tf.paragraphs[0]; run(p,t,22,PRETO,F_BODY,bold=True)
rect(s,10.0,3.2,8.0,6.4,SALVIA)
tb,tf=box(s,10.4,3.5,7.2,0.6); run(tf.paragraphs[0],"× EVITA",19.5,CORPO,F_BODY,bold=True,spc=1.5)
tb,tf=box(s,10.4,4.3,7.2,5)
for t in ["Mais do mesmo sem diferenciação","Complexidade desnecessária","Excesso de passos e produtos",
          "Promessas milagrosas","Visual 'natureba' sem substância"]:
    p=tf.add_paragraph() if tf.paragraphs[0].runs else tf.paragraphs[0]; run(p,t,22,CORPO,F_BODY)
footer(s)

# =====================================================================
# 10. ENCERRAMENTO
# =====================================================================
s=add_slide()
tb,tf=box(s,1.7,4.0,16,2); run(tf.paragraphs[0],"MUITO OBRIGADA!",70,PRETO0,F_TIT)
tb,tf=box(s,1.7,6.2,14,1.5)
run(tf.paragraphs[0],"Aplicando os conteúdos deste documento na prática, você garante uma marca construída com consistência e clareza.",30,PRETO,F_BODY)

out="/home/user/apresentacoes/MODELO-BASE-ESTRATEGICA.pptx"
prs.save(out)
print("salvo:",out,"| slides:",len(prs.slides._sldIdLst))
