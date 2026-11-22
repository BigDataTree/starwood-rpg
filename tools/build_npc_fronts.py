#!/usr/bin/env python3
"""Reproducible 31-player-moving-NPC front assets derived from the canonical 77 atlas."""
from pathlib import Path
from collections import deque
from PIL import Image, ImageDraw
from io import BytesIO
import base64, hashlib, json

root=Path(__file__).resolve().parents[1]
source=root/"assets/authority/64px/authority_77_numbered.png"
manifest_path=root/"assets/authority/64px/authority_manifest.json"
out_dir=root/"assets/authority/64px/fronts"
out_dir.mkdir(parents=True,exist_ok=True)
characters=json.loads(manifest_path.read_text("utf-8"))["characters"]
atlas=Image.open(source).convert("RGBA")
assert atlas.size==(1536,980),atlas.size
cols=[[30,120],[170,262],[319,410],[454,548],[593,684],[731,825],[865,969],[1008,1101],[1152,1230],[1279,1369],[1415,1508]]
rows=[[0,140],[159,296],[314,446],[468,594],[614,727],[747,849],[868,965]]
original_sha=hashlib.sha256(source.read_bytes()).hexdigest()
items=[]; metrics=[]
board=Image.new("RGB",(8*112,4*125),(224,237,230))
draw=ImageDraw.Draw(board)
for num in range(47,78):
    entry=characters[num-1]
    assert int(entry["number"])==num
    actor_id=entry["actor_id"]
    assert actor_id.startswith("ambient-")
    index=num-1
    col=cols[index%11];row=rows[index//11]
    box=[col[0],row[0],col[1]+1,row[1]+1]
    crop=atlas.crop(tuple(box))
    w,h=crop.size;data=bytearray(crop.tobytes())
    seen=bytearray(w*h)
    queue=deque()
    def eligible(x,y):
        k=(y*w+x)*4
        r,g,b=data[k],data[k+1],data[k+2]
        return min(r,g,b)>=190 and max(r,g,b)-min(r,g,b)<=35
    def enter(x,y):
        index=y*w+x
        if seen[index] or not eligible(x,y):return
        seen[index]=1
        queue.append(index)
    for x in range(w):enter(x,0);enter(x,h-1)
    for y in range(h):enter(0,y);enter(w-1,y)
    while queue:
        p=queue.popleft()
        x,y=p%w,p//w
        if x:enter(x-1,y)
        if x+1<w:enter(x+1,y)
        if y:enter(x,y-1)
        if y+1<h:enter(x,y+1)
    for pos in range(w*h):
        if not seen[pos]:continue
        idx=pos*4
        r,g,b=data[idx],data[idx+1],data[idx+2]
        # Optical white-background removal only from the connected exterior.
        # Preserve enclosed white clothing, skin and highlights within dark outlines.
        minimum=min(r,g,b)
        if minimum>=246:
            data[idx+3]=0
        else:
            a=min(1.0,max(0.0,(254-minimum)/254))
            alpha=round(255*a)
            if alpha<=2:
                data[idx+3]=0
            else:
                data[idx+3]=alpha
                for channel in range(3):
                    val=data[idx+channel]
                    corrected=(val-(1-a)*254)/a
                    data[idx+channel]=max(0,min(255,round(corrected)))
    cut=Image.frombytes("RGBA",(w,h),bytes(data))
    a=cut.getchannel("A")
    bbox=a.point(lambda v:255 if v>14 else 0).getbbox()
    assert bbox is not None,(num,actor_id)
    silhouette=cut.crop(bbox)
    sw,sh=silhouette.size
    scale=min(60/sw,60/sh)
    size=(max(1,round(sw*scale)),max(1,round(sh*scale)))
    scaled=silhouette.resize(size,Image.Resampling.NEAREST)
    face=Image.new("RGBA",(64,64),(0,0,0,0))
    x=(64-size[0])//2;y=63-size[1]
    face.alpha_composite(scaled,(x,y))
    filename=f"{num:02d}_{actor_id}.png"
    face.save(out_dir/filename,optimize=True)
    # Verify no opaque number in reserved outer border; all 4 corners remain transparent.
    corners=[face.getpixel((px,py))[3] for px,py in [(0,0),(0,63),(63,0),(63,63)]]
    assert max(corners)==0,(num,"corner not transparent",corners)
    cover=sum(px[3]>200 for px in face.getdata())
    assert cover>120,(num,"too few opaque pixels",cover)
    items.append({
       "number":num,"actor_id":actor_id,"source":str(source.relative_to(root)),
       "source_sha256":original_sha,"crop_xyxy":box,
       "output":str((out_dir/filename).relative_to(root)),
       "size":[64,64],"format":"RGBA",
       "validation":"machine-checked; visual acceptance pending"
    })
    metrics.append({"number":num,"actor_id":actor_id,"crop_size":[w,h],
       "silhouette_bbox":list(bbox),"opaque_pixels":cover,
       "bytes":(out_dir/filename).stat().st_size,"corner_alpha":corners})
    i=num-47;tx=i%8*112;ty=i//8*125
    draw.rectangle((tx,ty,tx+111,ty+124),outline=(175,195,180),width=1)
    draw.text((tx+5,ty+4),str(num),fill=(20,55,44))
    # Composite on green background so white artifacts are visually obvious.
    checker=Image.new("RGBA",(90,90),(112,185,130,255))
    checker.alpha_composite(face.resize((90,90),Image.Resampling.NEAREST))
    board.paste(checker.convert("RGB"),(tx+11,ty+24))
assert len(items)==31
manifest={"schema_version":1,"derived_from":str(source.relative_to(root)),
 "source_sha256":original_sha,"approved_numbering":"47–77",
 "status":"source-preserving derived sprites; manual visual review recommended",
 "image_count":len(items),"characters":items}
(out_dir/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(root/"coordination").mkdir(exist_ok=True)
(root/"coordination"/"npc-fronts-quality.json").write_text(json.dumps({
 "source_sha256":original_sha,"image_count":len(items),"metrics":metrics
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
buffer=BytesIO();board.save(buffer,format="JPEG",quality=88,optimize=True)
(root/"coordination"/"npc-fronts-preview.b64").write_text(base64.b64encode(buffer.getvalue()).decode("ascii"),encoding="ascii")
print(f"Built {len(items)} RGBA sprites, authority sha256={original_sha}")
