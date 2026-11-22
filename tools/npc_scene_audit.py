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
