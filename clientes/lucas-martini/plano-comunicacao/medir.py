import sys
from pptx import Presentation
from pptx.util import Emu
from pptx.enum.shapes import MSO_SHAPE_TYPE
p = Presentation(sys.argv[1])
ini, fim = int(sys.argv[2]), int(sys.argv[3])
for i, s in enumerate(p.slides, 1):
    if not (ini <= i <= fim): continue
    print(f"\n=== SLIDE {i:02d} " + "="*52)
    itens = []
    for sh in s.shapes:
        x, y = round(Emu(sh.left).inches,2), round(Emu(sh.top).inches,2)
        w, h = round(Emu(sh.width).inches,2), round(Emu(sh.height).inches,2)
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            itens.append((y, x, f"[IMG {w}x{h} @ {x},{y}]"))
        elif sh.has_text_frame and sh.text_frame.text.strip():
            t = sh.text_frame.text.strip().replace("\n", " ⏎ ")
            r0 = next((r for par in sh.text_frame.paragraphs for r in par.runs), None)
            tam = r0.font.size.pt if r0 and r0.font.size else '?'
            fo = (r0.font.name or '?') if r0 else '?'
            cor = ''
            try:
                if r0 and r0.font.color and r0.font.color.rgb: cor = '#'+str(r0.font.color.rgb)
            except Exception: pass
            itens.append((y, x, f"({x},{y} {w}x{h}) {tam}pt {fo} {cor} :: {t[:95]}"))
        elif sh.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE or sh.shape_type == 1:
            f = ''
            try:
                if sh.fill.type is not None and sh.fill.type == 1: f = '#'+str(sh.fill.fore_color.rgb)
            except Exception: pass
            itens.append((y, x, f"[FORMA {w}x{h} @ {x},{y} {f}]"))
    for _, _, t in sorted(itens):
        print("  " + t)
