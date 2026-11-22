#!/usr/bin/env python3
"""Read-only analysis of the original four game-data blocks. Outputs a small report."""
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
parts=[root/"game-data"/"v1.1.6"/f"part-{i:02d}.txt" for i in range(1,5)]
chunks=[p.read_text(encoding="utf-8") for p in parts]
src="".join(chunks)
lines=["# NPC rendering audit (original game source)", "",
       f"- Total game source characters: {len(src):,}",
       f"- Part lengths: {[len(x) for x in chunks]}", ""]
patterns=[
    r"function actorDraw\s*\(",
    r"actorDraw\s*\(",
    r"ambient-town",
    r"ambient-camp",
    r"ambient-dusk",
    r"ambient-moon",
    r"ambient-forgecamp",
    r"ambient_",
    r"AMBIENT",
    r"ambient",
    r"wander",
    r"WANDER",
    r"walkNPC",
    r"drawNpc",
    r"drawNPC",
    r"npcDraw",
    r"drawActor",
    r"drawImage\s*\(\s*PIXEL_ART",
    r"actors\.webp",
    r"function draw",
]
for pat in patterns:
    matches=list(re.finditer(pat,src,re.IGNORECASE if pat in ["wander","ambient"] else 0))
    lines += [f"## Pattern \`{pat}\` (occurrences: {len(matches)})", ""]
    max_items=28 if pat in [r"ambient",r"AMBIENT",r"actorDraw\s*\(",r"ambient-town"] else 10
    for i,m in enumerate(matches[:max_items]):
        lo=max(0,m.start()-320)
        hi=min(len(src),m.end()+420)
        fragment=src[lo:hi]
        fragment=re.sub(r"data:image/\w+;base64,[A-Za-z0-9+/=]{60,}", "[embedded image omitted]",fragment)
        fragment=fragment.replace("<!--", "< !--")
        lines += [f"### {i+1}: offset {m.start():,}", "~~~javascript", fragment, "~~~", ""]
    if len(matches)>max_items:lines += [f"... {len(matches)-max_items} more matches omitted.", ""]
(root/"coordination").mkdir(exist_ok=True)
(root/"coordination"/"npc-render-audit.md").write_text("\n".join(lines),encoding="utf-8")
print(f"Generated NPC audit: {len(lines)} sections, {len(src)} source chars")

# Assess pixels in the exact numbered canonical source, without changing any authority files.
from PIL import Image, ImageDraw
from collections import Counter
from io import BytesIO
import base64

atlas=Image.open(root/"assets"/"authority"/"64px"/"authority_77_numbered.png").convert("RGBA")
columns=[[30,120],[170,262],[319,410],[454,548],[593,684],[731,825],[865,969],[1008,1101],[1152,1230],[1279,1369],[1415,1508]]
rows=[[0,140],[159,296],[314,446],[468,594],[614,727],[747,849],[868,965]]
stats=["# Canonical authority 64px crop diagnostics","",
       f"- Source dimensions: {atlas.size[0]}×{atlas.size[1]}", "- Target: 47–77 (31 moving NPCs)", ""]
w,h=8*118,4*151
preview=Image.new("RGB",(w,h),(231,238,232))
d=ImageDraw.Draw(preview)
for number in range(47,78):
    pos=number-1
    col=columns[pos%11];row=rows[pos//11]
    crop=atlas.crop((col[0],row[0],col[1]+1,row[1]+1))
    pixels=list(crop.getdata())
    corners=[crop.getpixel((x,y)) for x,y in [(0,0),(crop.width-1,0),(0,crop.height-1),(crop.width-1,crop.height-1)]]
    border=[*list(crop.crop((0,0,crop.width,2)).getdata()),*list(crop.crop((0,crop.height-2,crop.width,crop.height)).getdata())]
    popular=Counter((r//16*16,g//16*16,b//16*16,a//16*16) for r,g,b,a in border).most_common(4)
    alpha=sum(a<240 for r,g,b,a in pixels)
    stats.append(f"| {number} | {crop.width}×{crop.height} | {alpha*100/len(pixels):.1f}% | {corners} | {popular[:2]} |")
    i=number-47;x=(i%8)*118;y=(i//8)*151
    d.rectangle((x,y,x+117,y+150),outline=(170,185,174),width=1)
    d.text((x+5,y+5),f"#{number}",fill=(20,50,35))
    shrink=crop.copy()
    shrink.thumbnail((112,126),Image.Resampling.NEAREST)
    if shrink.mode=="RGBA":
        backdrop=Image.new("RGBA",shrink.size,(218,238,218,255))
        backdrop.alpha_composite(shrink)
        shrink=backdrop.convert("RGB")
    preview.paste(shrink,(x+(118-shrink.width)//2,y+17))
stats.insert(4,"| ID | Crop size | Alpha < 240 | Corner RGBA | Dominant border quantized RGBA |")
stats.insert(5,"|---|---|---:|---|---|")
(root/"coordination"/"npc-atlas-stats.md").write_text("\n".join(stats),encoding="utf-8")
buf=BytesIO();preview.save(buf,format="JPEG",quality=86,optimize=True)
(root/"coordination"/"npc-crop-preview.b64").write_text(base64.b64encode(buf.getvalue()).decode("ascii"),encoding="ascii")
print(f"Image audit: atlas {atlas.size}, preview {len(buf.getvalue()):,} bytes")
