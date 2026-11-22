# NPC rendering audit (original game source)

- Total game source characters: 10,464,314
- Part lengths: [2699925, 2700000, 2699902, 2364487]

## Pattern \`function actorDraw\s*\(\` (occurrences: 1)

### 1: offset 7,171,128
~~~javascript
.y+23,n.type==='altar'?75:55,n.type==='altar'?90:71);
 g.font='bold 13px system-ui';g.textAlign='center';g.fillStyle='#fff1cd';g.fillText(n.name,n.x,n.y-46);g.restore()}
function objDraw(name,x,y,w,h){const im=PIXEL_ART.objects,i=objectIndex.get(name);if(i===undefined)return; spriteDraw(im,i*32,0,32,48,x-w/2,y-h,w,h)}
function actorDraw(key,x,y,dir=0,frame=0,w=64,h=64){const im=PIXEL_ART.actors;const i=actorIndex.get(key)??0;const f=Math.max(0,Math.min(2,frame|0));
 // 左向原始圖集中混有右向影格；改以完整右向步行列水平鏡像，確保移動與停止都一致朝左。
 if(dir===1){if(!im?.complete||!im.naturalWidth)return false;g.save();g.translate(Math.round(x),0);g.scale(-1,1);g.drawImage(im,f*32,(i*4+2)*32,32,32,-w/2,Math.round(y-h*.69),w,h);g.restore();return true}
 return spriteDraw(im,f*32,(i*4+dir)*3
~~~

## Pattern \`actorDraw\s*\(\` (occurrences: 11)

### 1: offset 7,171,137
~~~javascript
ype==='altar'?75:55,n.type==='altar'?90:71);
 g.font='bold 13px system-ui';g.textAlign='center';g.fillStyle='#fff1cd';g.fillText(n.name,n.x,n.y-46);g.restore()}
function objDraw(name,x,y,w,h){const im=PIXEL_ART.objects,i=objectIndex.get(name);if(i===undefined)return; spriteDraw(im,i*32,0,32,48,x-w/2,y-h,w,h)}
function actorDraw(key,x,y,dir=0,frame=0,w=64,h=64){const im=PIXEL_ART.actors;const i=actorIndex.get(key)??0;const f=Math.max(0,Math.min(2,frame|0));
 // 左向原始圖集中混有右向影格；改以完整右向步行列水平鏡像，確保移動與停止都一致朝左。
 if(dir===1){if(!im?.complete||!im.naturalWidth)return false;g.save();g.translate(Math.round(x),0);g.scale(-1,1);g.drawImage(im,f*32,(i*4+2)*32,32,32,-w/2,Math.round(y-h*.69),w,h);g.restore();return true}
 return spriteDraw(im,f*32,(i*4+dir)*3
~~~

### 2: offset 7,171,788
~~~javascript
32,32,-w/2,Math.round(y-h*.69),w,h);g.restore();return true}
 return spriteDraw(im,f*32,(i*4+dir)*32,32,32,x-w/2,y-h*.69,w,h)}
function drawAmbientNPC(n){const near=distance(hero,n)<80;g.save();g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:Math.floor(n.step)%3;actorDraw(n.actor,n.x,n.y+18,n.dir,frame,58,58);if(near||n.chat>0){g.font='bold 12px "Noto Sans TC",system-ui';const label=n.chat>0?n.line:n.name;const tw=Math.min(230,Math.max(72,g.measureText(label).width+22));g.fillStyle=n.chat>0?'#173c34f2':'#0a302bcc';g.beginPath();g.roundRect(n.x-tw/2,n.y-69,tw,26,7);g.fill();g.strokeStyle=n.chat>0?'#f1d27f':'#86b89a';g.stroke();g.fillStyle='#fff0c2';g.textAlign='center';g.fillText(label
~~~

### 3: offset 7,172,909
~~~javascript
n(clock*1.4+i)*10,y=425-i*6;g.beginPath();g.arc(x,y,5+Math.sin(clock*2+i)*2,0,TWO);g.fill()}g.restore()}
function drawNPC(n){const near=distance(hero,n)<115;g.save();
 g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();
 if(n.id.includes('board')){objDraw('book',n.x,n.y+20,60,71)}
 else {actorDraw(n.id,n.x,n.y+20,0,Math.floor(clock*2+n.x)%3,68,68)}
 const text=n.name;g.font='bold 15px "Noto Sans TC",system-ui';
 const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));
 g.fillStyle=near?'#103b32ed':'#0a2b27d9';g.beginPath();g.roundRect(n.x-tw/2,n.y-82,tw,29,7);g.fill();
 g.strokeStyle=near?'#f4d384':'#a0b98370';g.lineWidth=near?2:1;g.stroke();
 g.textAlign='center';g.fillStyle='#fff0c1';g.fillText(text
~~~

### 4: offset 7,175,051
~~~javascript
rif';g.fillText('*',e.x+e.r+7,e.y-20)}g.restore()}}
function drawHero(){g.save();if(hero.invuln>0&&Math.floor(clock*15)%2===0)g.globalAlpha=.52;
 g.fillStyle='#09191a9b';g.beginPath();g.ellipse(hero.x,hero.y+26,24,9,0,0,TWO);g.fill();
 const dir=hero.facing??0;
 const frame=hero.moving?Math.floor(hero.walk*1.25)%3:0;
 actorDraw(s.cls,hero.x,hero.y+20,dir,frame,66,66);
 if(hero.shield>0){g.strokeStyle='#a0eaffbb';g.lineWidth=3;g.beginPath();g.arc(hero.x,hero.y,42,0,TWO);g.stroke()}
 if(hero.slash>0){g.save();g.translate(hero.x,hero.y);g.rotate(hero.angle);g.strokeStyle='#ffe2a9';g.lineWidth=10;g.lineCap='round';g.beginPath();g.arc(0,0,70,-1.05,1.05);g.stroke();g.restore()}
  // Player identity is shown in the HUD; keep the world view free of
~~~

### 5: offset 7,195,216
~~~javascript
]))drawLeafSway(x,y,sz,frame);if(s.area==='town')drawFountainAnim(950,470);if(s.area==='moon')drawFountainAnim(803,448)}
function drawAmbientNPC(n){const near=distance(hero,n)<80;g.save();g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:(Math.floor(n.step)%2?1:2);actorDraw(n.actor,n.x,n.y+18,n.dir,frame,64,64);if(near){g.fillStyle='#0d3029e8';g.fillRect(n.x-70,n.y-60,140,26);g.strokeStyle='#f4d384';g.strokeRect(n.x-70,n.y-60,140,26);g.fillStyle='#fff0be';g.font='bold 13px system-ui';g.textAlign='center';g.fillText('F 對話 · '+n.name,n.x,n.y-42)}g.restore()}
function interaction(){if(mode!=='play')return;const n=nearest(NPCS[s.area]||[],108);if(n){talk(n);return}const citizen=nearest(ambi
~~~

### 6: offset 7,210,403
~~~javascript
ill; moving NPCs only alternate left/right foot poses. No alpha/brightness flash.
drawNPC=function(n){const near=distance(hero,n)<115;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);else actorDraw(n.actor||n.id,n.x,n.y+20,n.dir??0,0,68,68);const text=n.name;g.font='bold 15px "Noto Sans TC",system-ui';const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));g.fillStyle=near?'#103b32ed':'#0a2b27d9';g.beginPath();g.roundRect(n.x-tw/2,n.y-82,tw,29,7);g.fill();g.strokeStyle=near?'#f4d384':'#a0b98370';g.lineWidth=near?2:1;g.stroke();g.textAlign='center';g.fillStyle='#fff0c1';g.fillText(text,n.x,n.y-63);if(['
~~~

### 7: offset 7,211,804
~~~javascript
(type===2){g.fillRect(n.x-17,n.y-12,34,5)}else{g.fillRect(n.x+15,n.y-5,8,16)}g.restore()}
drawAmbientNPC=function(n){const near=distance(hero,n)<80;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:(Math.floor(n.step)%2?1:2);actorDraw(n.actor,n.x,n.y+18,n.dir,frame,64,64);ambientAccessory(n);if(near){g.fillStyle='#0d3029e8';g.fillRect(n.x-70,n.y-60,140,26);g.strokeStyle='#f4d384';g.strokeRect(n.x-70,n.y-60,140,26);g.fillStyle='#fff0be';g.font='bold 13px system-ui';g.textAlign='center';g.fillText('F 對話 · '+n.name,n.x,n.y-42)}g.restore()};

interaction=function(){if(mode!=='play')return;const n=nearest(NPCS[s.area]||[],108);if(n){talk(n);return}cons
~~~

### 8: offset 10,456,910
~~~javascript
'冒險者':'NPC'} 肖像" width="256" height="256" decoding="async" src="${src}"></div>`};
drawNPC=function(n){const near=distance(hero,n)<115;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);else actorDraw(n.actor||n.id,n.x,n.y+20,0,0,68,68);const text=n.name;g.font='bold 15px system-ui';const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));g.fillStyle=near?'#103b32ed':'#0a2b27d9';g.beginPath();g.roundRect(n.x-tw/2,n.y-82,tw,29,7);g.fill();g.strokeStyle=near?'#f4d384':'#a0b98370';g.lineWidth=near?2:1;g.stroke();g.textAlign='center';g.fillStyle='#fff0c1';g.fillText(text,n.x,n.y-63);if(['elder','guard','scout'
~~~

### 9: offset 10,457,856
~~~javascript
lStyle='#f8dca0';g.font='bold 13px system-ui';g.fillText('F 交談',n.x,n.y+50)}g.restore()};
drawAmbientNPC=function(n){const near=distance(hero,n)<80;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:(Math.floor(n.step)%2?1:2);actorDraw(n.actor,n.x,n.y+18,n.dir,frame,64,64);if(near){g.fillStyle='#0d3029e8';g.fillRect(n.x-70,n.y-60,140,26);g.strokeStyle='#f4d384';g.strokeRect(n.x-70,n.y-60,140,26);g.fillStyle='#fff0be';g.font='bold 13px system-ui';g.textAlign='center';g.fillText('F 對話 · '+n.name,n.x,n.y-42)}g.restore()};
window.starwoodPortraitFormat='static-webp-ready-for-animated-webp';

const _baseLoadAreaOptimized=loadArea;
loadArea=function(id,s
~~~

### 10: offset 10,462,271
~~~javascript
a8';g.font='bold 14px system-ui';g.textAlign='center';
  g.fillText('✦',n.x,n.y-47);
  g.restore();
}
drawNPC=function(n){
  g.save();g.globalAlpha=1;g.shadowBlur=0;
  g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();
  if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);
  else actorDraw(n.actor||n.id,n.x,n.y+20,0,0,68,68);
  // No permanent NPC names or duplicate "F 交談" labels above or below sprites.
  swActorFocusV113(n);
  g.restore();
};
drawAmbientNPC=function(n){
  g.save();g.globalAlpha=1;g.shadowBlur=0;
  g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();
  const frame=n.wait>0?0:(Math.floor(n.step)%2?1:2);
  actorDraw(n.actor,n.x,n.y+18,n.dir,frame,64,64);
  s
~~~

### 11: offset 10,462,649
~~~javascript
manent NPC names or duplicate "F 交談" labels above or below sprites.
  swActorFocusV113(n);
  g.restore();
};
drawAmbientNPC=function(n){
  g.save();g.globalAlpha=1;g.shadowBlur=0;
  g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();
  const frame=n.wait>0?0:(Math.floor(n.step)%2?1:2);
  actorDraw(n.actor,n.x,n.y+18,n.dir,frame,64,64);
  swActorFocusV113(n);
  g.restore();
};
// Entrances keep their collision and F-interaction but no longer print labels across artwork.
drawDoor=function(d){
  g.save();
  if(s.area==='town'){
    // The illustrated house already has a door. Only hint at the threshold.
    g.fillStyle='#e4c78b80';g.fillRect(d.x-22,d.y-8,44,4);
  }else{
    g.fillStyle='#2a1d13';g.fillRect(d.x-d.
~~~

## Pattern \`ambient-town\` (occurrences: 0)

## Pattern \`ambient-camp\` (occurrences: 0)

## Pattern \`ambient-dusk\` (occurrences: 0)

## Pattern \`ambient-moon\` (occurrences: 0)

## Pattern \`ambient-forgecamp\` (occurrences: 0)

## Pattern \`ambient_\` (occurrences: 187)

### 1: offset 7,240,558
~~~javascript
 "v6_housekeeper_mara", "v6_secretary_elin", "v6_cook_bram", "v6_guest_roan", "v6_aide_sena", "v6_archivist_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambi
~~~

### 2: offset 7,240,579
~~~javascript
", "v6_secretary_elin", "v6_cook_bram", "v6_guest_roan", "v6_aide_sena", "v6_archivist_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambi
~~~

### 3: offset 7,240,600
~~~javascript
", "v6_cook_bram", "v6_guest_roan", "v6_aide_sena", "v6_archivist_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambi
~~~

### 4: offset 7,240,621
~~~javascript
6_guest_roan", "v6_aide_sena", "v6_archivist_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambi
~~~

### 5: offset 7,240,642
~~~javascript
de_sena", "v6_archivist_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambi
~~~

### 6: offset 7,240,663
~~~javascript
st_nora", "v6_astronomer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambient_moon_1", "v6_ambi
~~~

### 7: offset 7,240,684
~~~javascript
mer_vega", "v6_apprentice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambient_moon_1", "v6_ambient_moon_2", "v6_ambi
~~~

### 8: offset 7,240,705
~~~javascript
tice_tio", "v6_scribe_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambient_moon_1", "v6_ambient_moon_2", "v6_ambient_moon_3", "v6_ambi
~~~

### 9: offset 7,240,726
~~~javascript
_luna", "v6_baker_lumi", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambient_moon_1", "v6_ambient_moon_2", "v6_ambient_moon_3", "v6_ambient_forgecamp_0", "v6
~~~

### 10: offset 7,240,747
~~~javascript
i", "v6_florist_nia", "v6_innkeeper_doran", "v6_campcook_odo", "v6_weaver_mira", "v6_researcher_sol", "v6_quartermaster_bran", "v6_ambient_town_0", "v6_ambient_town_1", "v6_ambient_town_2", "v6_ambient_town_3", "v6_ambient_town_4", "v6_ambient_town_5", "v6_ambient_town_6", "v6_ambient_town_7", "v6_ambient_town_8", "v6_ambient_town_9", "v6_ambient_town_10", "v6_ambient_town_11", "v6_ambient_town_12", "v6_ambient_town_13", "v6_ambient_camp_0", "v6_ambient_camp_1", "v6_ambient_camp_2", "v6_ambient_camp_3", "v6_ambient_dusk_0", "v6_ambient_dusk_1", "v6_ambient_dusk_2", "v6_ambient_dusk_3", "v6_ambient_dusk_4", "v6_ambient_moon_0", "v6_ambient_moon_1", "v6_ambient_moon_2", "v6_ambient_moon_3", "v6_ambient_forgecamp_0", "v6_ambient_forgecamp_1"
~~~

... 177 more matches omitted.

## Pattern \`AMBIENT\` (occurrences: 30)

### 1: offset 32,247
~~~javascript
'星鑄工匠',role:'裝備・鍛造',x:390,y:375,emoji:'⚒️'},{id:'forgemerchant',name:'礦工商隊',role:'藥水・補給',x:625,y:685,emoji:'🎒'},{id:'forgehealer',name:'堡壘醫護員',role:'免費治療',x:950,y:665,emoji:'💚'},{id:'forgeboard',name:'前哨懸賞令',role:'討伐委託',x:1170,y:325,emoji:'📜'},{id:'forgeguard',name:'礦坑警衛',role:'支線任務',x:1190,y:630,emoji:'🛡️'}]
};
const AMBIENT_ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧
~~~

### 2: offset 32,392
~~~javascript
le:'免費治療',x:950,y:665,emoji:'💚'},{id:'forgeboard',name:'前哨懸賞令',role:'討伐委託',x:1170,y:325,emoji:'📜'},{id:'forgeguard',name:'礦坑警衛',role:'支線任務',x:1190,y:630,emoji:'🛡️'}]
};
const AMBIENT_ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],
~~~

### 3: offset 32,575
~~~javascript
ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],[430,470],[590,470],[740,470],[900,470],[1080,470],[1240,470],[1380,470]],
  [[745,245],[745,330],[745,425],[745,545],[745,655],[745,760]],
  [[330,610],[500,610],[665,610],[820,610],
~~~

### 4: offset 32,781
~~~javascript
,'諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],[430,470],[590,470],[740,470],[900,470],[1080,470],[1240,470],[1380,470]],
  [[745,245],[745,330],[745,425],[745,545],[745,655],[745,760]],
  [[330,610],[500,610],[665,610],[820,610],[980,610],[1140,610]],
  [[930,300],[1010,335],[1070,410],[1080,500],[1030,565],[940,590]],
  [[260,350],[350,385],[460,420],[545,480],[500,555],[390,590]],
  [[1190,350],[1300,380],[1390,430],[1400,535],[1
~~~

### 5: offset 34,200
~~~javascript
0]]],
 moon:[[[260,455],[500,455],[760,455],[1010,455],[1290,455]],[[420,300],[520,370],[610,520],[520,650]],[[980,330],[1100,410],[1180,560],[1050,690]]],
 forgecamp:[[[250,455],[480,455],[760,455],[1040,455],[1290,455]],[[500,300],[600,390],[690,540],[620,680]],[[1020,300],[1120,390],[1210,540],[1130,670]]]
};
const AMBIENT_COUNTS={town:14,camp:4,dusk:5,moon:4,forgecamp:4};
const CLASSES={novice:{name:'見習冒險者',icon:'🗡️',q:'星芒斬',e:'閃身',desc:'學會熟練使用武器，再尋找屬於自己的道路。'},knight:{name:'星盾騎士',icon:'🛡️',q:'獅心震擊',e:'鋼盾守護',desc:'承擔風暴的守護者，擅長近戰與防禦。',req:'擊敗 3 隻野狼',metric:'wolf',need:3,bonus:'最大 HP +55、防禦 +5'},mage:{name:'星語法師',icon:'🪄',q:'流星焰爆',e:'寒霜新星',desc:'探索星核奧秘，擅長範圍傷害與控制。',req:'取得 4 份星塵',metric:'dust',need:4,bonus:'最大 MP +70、攻擊 +6'},ranger:{name:
~~~

### 6: offset 5,613,232
~~~javascript
=FACING_ANGLE[dir]}
function updateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],acto
~~~

### 7: offset 5,613,263
~~~javascript
dateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.index
~~~

### 8: offset 5,613,617
~~~javascript
||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;contin
~~~

### 9: offset 5,613,633
~~~javascript
)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.rou
~~~

### 10: offset 5,613,661
~~~javascript
8013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p
~~~

### 11: offset 5,613,702
~~~javascript
;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.
~~~

### 12: offset 5,613,845
~~~javascript
)*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs
~~~

### 13: offset 5,613,885
~~~javascript
Cs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs(vy))n.dir=vx<0?1:2;else n.dir=vy<0?3:0;
~~~

### 14: offset 7,181,289
~~~javascript

AREAS.elderhouse1={name:'長老之家・一樓',safe:true,level:'1',subtitle:'長老家的一樓起居與會客空間',color:'#5b4638',unlocked:0,emoji:'🏠'};
AREAS.elderhouse2={name:'長老之家・二樓',safe:true,level:'1',subtitle:'書房與客房所在的二樓',color:'#64503d',unlocked:0,emoji:'🪜'};
GATES.elderhouse1=[]; GATES.elderhouse2=[];
NPCS.elderhouse1=[]; NPCS.elderhouse2=[];
AMBIENT_ROUTES.elderhouse1=[]; AMBIENT_ROUTES.elderhouse2=[];
AMBIENT_COUNTS.elderhouse1=0; AMBIENT_COUNTS.elderhouse2=0;
const DOORS={
  town:[{x:345,y:418,w:76,h:34,to:'elderhouse1',spawn:{x:802,y:730,facing:3},name:'進入長老之家'}],
  elderhouse1:[{x:802,y:782,w:92,h:28,to:'town',spawn:{x:345,y:446,facing:0},name:'離開長老之家'},{x:1190,y:240,w:70,h:70,to:'elderhouse2',spawn:{x:236,y:726,facing:2},name:'前往二樓'}],
  elderhouse2:[{x:22
~~~

### 15: offset 7,181,320
~~~javascript
一樓',safe:true,level:'1',subtitle:'長老家的一樓起居與會客空間',color:'#5b4638',unlocked:0,emoji:'🏠'};
AREAS.elderhouse2={name:'長老之家・二樓',safe:true,level:'1',subtitle:'書房與客房所在的二樓',color:'#64503d',unlocked:0,emoji:'🪜'};
GATES.elderhouse1=[]; GATES.elderhouse2=[];
NPCS.elderhouse1=[]; NPCS.elderhouse2=[];
AMBIENT_ROUTES.elderhouse1=[]; AMBIENT_ROUTES.elderhouse2=[];
AMBIENT_COUNTS.elderhouse1=0; AMBIENT_COUNTS.elderhouse2=0;
const DOORS={
  town:[{x:345,y:418,w:76,h:34,to:'elderhouse1',spawn:{x:802,y:730,facing:3},name:'進入長老之家'}],
  elderhouse1:[{x:802,y:782,w:92,h:28,to:'town',spawn:{x:345,y:446,facing:0},name:'離開長老之家'},{x:1190,y:240,w:70,h:70,to:'elderhouse2',spawn:{x:236,y:726,facing:2},name:'前往二樓'}],
  elderhouse2:[{x:220,y:734,w:70,h:70,to:'elderhous
~~~

### 16: offset 7,181,351
~~~javascript
e:'長老家的一樓起居與會客空間',color:'#5b4638',unlocked:0,emoji:'🏠'};
AREAS.elderhouse2={name:'長老之家・二樓',safe:true,level:'1',subtitle:'書房與客房所在的二樓',color:'#64503d',unlocked:0,emoji:'🪜'};
GATES.elderhouse1=[]; GATES.elderhouse2=[];
NPCS.elderhouse1=[]; NPCS.elderhouse2=[];
AMBIENT_ROUTES.elderhouse1=[]; AMBIENT_ROUTES.elderhouse2=[];
AMBIENT_COUNTS.elderhouse1=0; AMBIENT_COUNTS.elderhouse2=0;
const DOORS={
  town:[{x:345,y:418,w:76,h:34,to:'elderhouse1',spawn:{x:802,y:730,facing:3},name:'進入長老之家'}],
  elderhouse1:[{x:802,y:782,w:92,h:28,to:'town',spawn:{x:345,y:446,facing:0},name:'離開長老之家'},{x:1190,y:240,w:70,h:70,to:'elderhouse2',spawn:{x:236,y:726,facing:2},name:'前往二樓'}],
  elderhouse2:[{x:220,y:734,w:70,h:70,to:'elderhouse1',spawn:{x:1225,y:280,facing:
~~~

### 17: offset 7,181,381
~~~javascript
38',unlocked:0,emoji:'🏠'};
AREAS.elderhouse2={name:'長老之家・二樓',safe:true,level:'1',subtitle:'書房與客房所在的二樓',color:'#64503d',unlocked:0,emoji:'🪜'};
GATES.elderhouse1=[]; GATES.elderhouse2=[];
NPCS.elderhouse1=[]; NPCS.elderhouse2=[];
AMBIENT_ROUTES.elderhouse1=[]; AMBIENT_ROUTES.elderhouse2=[];
AMBIENT_COUNTS.elderhouse1=0; AMBIENT_COUNTS.elderhouse2=0;
const DOORS={
  town:[{x:345,y:418,w:76,h:34,to:'elderhouse1',spawn:{x:802,y:730,facing:3},name:'進入長老之家'}],
  elderhouse1:[{x:802,y:782,w:92,h:28,to:'town',spawn:{x:345,y:446,facing:0},name:'離開長老之家'},{x:1190,y:240,w:70,h:70,to:'elderhouse2',spawn:{x:236,y:726,facing:2},name:'前往二樓'}],
  elderhouse2:[{x:220,y:734,w:70,h:70,to:'elderhouse1',spawn:{x:1225,y:280,facing:1},name:'返回一樓'}]
};
const STAT
~~~

### 18: offset 7,185,104
~~~javascript
y,r=20,area=s.area){for(const o of getSolids(area)){if(circleHitsRect(x,y,r,o))return true}return false}
function resolveCircleMove(x,y,nx,ny,r=20,area=s.area){let rx=x,ry=y;if(!blockedAt(nx,y,r,area))rx=nx;if(!blockedAt(rx,ny,r,area))ry=ny;return {x:rx,y:ry}}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;const rng=seeded(78013+Math.max(0,ORDER.indexOf(area))*907);const actorPool=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng(
~~~

### 19: offset 7,185,135
~~~javascript
 of getSolids(area)){if(circleHitsRect(x,y,r,o))return true}return false}
function resolveCircleMove(x,y,nx,ny,r=20,area=s.area){let rx=x,ry=y;if(!blockedAt(nx,y,r,area))rx=nx;if(!blockedAt(rx,ny,r,area))ry=ny;return {x:rx,y:ry}}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;const rng=seeded(78013+Math.max(0,ORDER.indexOf(area))*907);const actorPool=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.fl
~~~

### 20: offset 7,185,637
~~~javascript
n','healer','guard','scout','wood','herbalist','cartographer','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:48+rng()*26,wait:rng()*1.2,dir:i%2?2:0,step:rng()*2,chat:0,actor:actorPool[i%actorPool.length],r:18})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy)
~~~

### 21: offset 7,185,653
~~~javascript
rd','scout','wood','herbalist','cartographer','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:48+rng()*26,wait:rng()*1.2,dir:i%2?2:0,step:rng()*2,chat:0,actor:actorPool[i%actorPool.length],r:18})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x
~~~

### 22: offset 7,185,680
~~~javascript
st','cartographer','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:48+rng()*26,wait:rng()*1.2,dir:i%2?2:0,step:rng()*2,chat:0,actor:actorPool[i%actorPool.length],r:18})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target
~~~

### 23: offset 7,185,696
~~~javascript
r','artificer','duskhead','moonmerchant'];for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y])=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:48+rng()*26,wait:rng()*1.2,dir:i%2?2:0,step:rng()*2,chat:0,actor:actorPool[i%actorPool.length],r:18})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.leng
~~~

### 24: offset 7,222,220
~~~javascript
1';c.fillRect(x-16,y,32,8);c.fillStyle='#d7869c';c.fillRect(x-11,y-7,7,7);c.fillStyle='#f4e0a5';c.fillRect(x,y-10,7,7);c.fillStyle='#8dc47f';c.fillRect(x+9,y-6,7,7)}
 c.restore();
};
worldCacheKey='';

// --- Moving NPCs: each resident stays in a small assigned neighborhood and avoids actors/portals/terrain. ---
const AMBIENT_ZONES_V5={
 town:[{x1:260,y1:500,x2:560,y2:565},{x1:680,y1:285,x2:805,y2:555},{x1:760,y1:555,x2:1030,y2:605},{x1:1080,y1:500,x2:1310,y2:565}],
 camp:[{x1:470,y1:380,x2:720,y2:545},{x1:880,y1:390,x2:1080,y2:560}],
 dusk:[{x1:450,y1:390,x2:710,y2:555},{x1:870,y1:390,x2:1090,y2:555}],
 moon:[{x1:450,y1:390,x2:680,y2:560},{x1:930,y1:430,x2:1160,y2:590}],
 forgecamp:[{x1:480,y1:390,x2:710,y2:560},{x1:900,y1:390,x2:1110,y
~~~

### 25: offset 7,223,653
~~~javascript
return false;
 return true;
}
function chooseAmbientTargetV5(n,rng=Math.random){const z=n.zone;for(let t=0;t<28;t++){const x=z.x1+rng()*(z.x2-z.x1),y=z.y1+rng()*(z.y2-z.y1);if(npcPositionFreeV5(n,x,y)){n.tx=x;n.ty=y;return true}}n.tx=n.x;n.ty=n.y;return false}
buildAmbientNPCs=function(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,zones=AMBIENT_ZONES_V5[area]||[];if(!count||!zones.length)return;const rng=seeded(92021+Math.max(0,ORDER.indexOf(area))*1319),pool=actorPoolV5(area);for(let i=0;i<count;i++){const z=zones[i%zones.length];let n={ambient:true,name:AMBIENT_NAMES[(i+Math.max(0,ORDER.indexOf(area))*3)%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:(z.x1+z.x2)/2,y:(z.y1+z.y2)/2,zone:z,tx:0,ty:0,speed:43
~~~

### 26: offset 7,223,683
~~~javascript
function chooseAmbientTargetV5(n,rng=Math.random){const z=n.zone;for(let t=0;t<28;t++){const x=z.x1+rng()*(z.x2-z.x1),y=z.y1+rng()*(z.y2-z.y1);if(npcPositionFreeV5(n,x,y)){n.tx=x;n.ty=y;return true}}n.tx=n.x;n.ty=n.y;return false}
buildAmbientNPCs=function(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,zones=AMBIENT_ZONES_V5[area]||[];if(!count||!zones.length)return;const rng=seeded(92021+Math.max(0,ORDER.indexOf(area))*1319),pool=actorPoolV5(area);for(let i=0;i<count;i++){const z=zones[i%zones.length];let n={ambient:true,name:AMBIENT_NAMES[(i+Math.max(0,ORDER.indexOf(area))*3)%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:(z.x1+z.x2)/2,y:(z.y1+z.y2)/2,zone:z,tx:0,ty:0,speed:43+rng()*20,wait:rng()*.9,dir:i%
~~~

### 27: offset 7,223,906
~~~javascript
 false}
buildAmbientNPCs=function(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,zones=AMBIENT_ZONES_V5[area]||[];if(!count||!zones.length)return;const rng=seeded(92021+Math.max(0,ORDER.indexOf(area))*1319),pool=actorPoolV5(area);for(let i=0;i<count;i++){const z=zones[i%zones.length];let n={ambient:true,name:AMBIENT_NAMES[(i+Math.max(0,ORDER.indexOf(area))*3)%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:(z.x1+z.x2)/2,y:(z.y1+z.y2)/2,zone:z,tx:0,ty:0,speed:43+rng()*20,wait:rng()*.9,dir:i%2?2:0,step:rng()*2,chat:0,actor:pool[i%pool.length],r:18};for(let k=0;k<30;k++){const x=z.x1+rng()*(z.x2-z.x1),y=z.y1+rng()*(z.y2-z.y1);if(npcPositionFreeV5(n,x,y)){n.x=x;n.y=y;break}}ambientNPCs.push(n);chooseAmbientTarget
~~~

### 28: offset 7,223,958
~~~javascript
[];const count=AMBIENT_COUNTS[area]||0,zones=AMBIENT_ZONES_V5[area]||[];if(!count||!zones.length)return;const rng=seeded(92021+Math.max(0,ORDER.indexOf(area))*1319),pool=actorPoolV5(area);for(let i=0;i<count;i++){const z=zones[i%zones.length];let n={ambient:true,name:AMBIENT_NAMES[(i+Math.max(0,ORDER.indexOf(area))*3)%AMBIENT_NAMES.length],line:AMBIENT_LINES[i%AMBIENT_LINES.length],x:(z.x1+z.x2)/2,y:(z.y1+z.y2)/2,zone:z,tx:0,ty:0,speed:43+rng()*20,wait:rng()*.9,dir:i%2?2:0,step:rng()*2,chat:0,actor:pool[i%pool.length],r:18};for(let k=0;k<30;k++){const x=z.x1+rng()*(z.x2-z.x1),y=z.y1+rng()*(z.y2-z.y1);if(npcPositionFreeV5(n,x,y)){n.x=x;n.y=y;break}}ambientNPCs.push(n);chooseAmbientTargetV5(n,rng)}};
updateAmbientNPCs=function(dt){for(cons
~~~

... 2 more matches omitted.

## Pattern \`ambient\` (occurrences: 283)

### 1: offset 32,247
~~~javascript
'星鑄工匠',role:'裝備・鍛造',x:390,y:375,emoji:'⚒️'},{id:'forgemerchant',name:'礦工商隊',role:'藥水・補給',x:625,y:685,emoji:'🎒'},{id:'forgehealer',name:'堡壘醫護員',role:'免費治療',x:950,y:665,emoji:'💚'},{id:'forgeboard',name:'前哨懸賞令',role:'討伐委託',x:1170,y:325,emoji:'📜'},{id:'forgeguard',name:'礦坑警衛',role:'支線任務',x:1190,y:630,emoji:'🛡️'}]
};
const AMBIENT_ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧
~~~

### 2: offset 32,392
~~~javascript
le:'免費治療',x:950,y:665,emoji:'💚'},{id:'forgeboard',name:'前哨懸賞令',role:'討伐委託',x:1170,y:325,emoji:'📜'},{id:'forgeguard',name:'礦坑警衛',role:'支線任務',x:1190,y:630,emoji:'🛡️'}]
};
const AMBIENT_ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],
~~~

### 3: offset 32,575
~~~javascript
ACTORS=['traveler','guide','merchant','child','librarian','healer','guard','scout','wood','herbalist','cartographer','artificer'];
const AMBIENT_NAMES=['悠娜','柏恩','希亞','洛可','米婭','提歐','安妮','羅伊','菲恩','露西','凱拉','諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],[430,470],[590,470],[740,470],[900,470],[1080,470],[1240,470],[1380,470]],
  [[745,245],[745,330],[745,425],[745,545],[745,655],[745,760]],
  [[330,610],[500,610],[665,610],[820,610],
~~~

### 4: offset 32,781
~~~javascript
,'諾亞','席爾','艾薇','杜克','莉亞','托比','妮可','亞倫','芙雅','路克','莎菲','傑恩','可可','夏洛','維恩','茉莉','哈洛','伊森','蘿娜','柯特','奈奈'];
const AMBIENT_LINES=['今天的星燈特別明亮。','聽說旅行商人又帶了新貨。','噴水池旁邊最適合休息了。','守衛說最近原野的野狼變多了。','我正要去市場買晚餐。','冒險者公會今天很熱鬧。','花店的新月見花真漂亮。','如果要出城，記得多帶幾瓶藥水。','鍛造坊一早就傳來敲鐵聲。','長老似乎在等一位冒險者。','我喜歡沿著中央石板路散步。','星燈鎮雖小，卻總有人從遠方來。'];
const AMBIENT_ROUTES={
 town:[
  [[270,470],[430,470],[590,470],[740,470],[900,470],[1080,470],[1240,470],[1380,470]],
  [[745,245],[745,330],[745,425],[745,545],[745,655],[745,760]],
  [[330,610],[500,610],[665,610],[820,610],[980,610],[1140,610]],
  [[930,300],[1010,335],[1070,410],[1080,500],[1030,565],[940,590]],
  [[260,350],[350,385],[460,420],[545,480],[500,555],[390,590]],
  [[1190,350],[1300,380],[1390,430],[1400,535],[1
~~~

### 5: offset 34,200
~~~javascript
0]]],
 moon:[[[260,455],[500,455],[760,455],[1010,455],[1290,455]],[[420,300],[520,370],[610,520],[520,650]],[[980,330],[1100,410],[1180,560],[1050,690]]],
 forgecamp:[[[250,455],[480,455],[760,455],[1040,455],[1290,455]],[[500,300],[600,390],[690,540],[620,680]],[[1020,300],[1120,390],[1210,540],[1130,670]]]
};
const AMBIENT_COUNTS={town:14,camp:4,dusk:5,moon:4,forgecamp:4};
const CLASSES={novice:{name:'見習冒險者',icon:'🗡️',q:'星芒斬',e:'閃身',desc:'學會熟練使用武器，再尋找屬於自己的道路。'},knight:{name:'星盾騎士',icon:'🛡️',q:'獅心震擊',e:'鋼盾守護',desc:'承擔風暴的守護者，擅長近戰與防禦。',req:'擊敗 3 隻野狼',metric:'wolf',need:3,bonus:'最大 HP +55、防禦 +5'},mage:{name:'星語法師',icon:'🪄',q:'流星焰爆',e:'寒霜新星',desc:'探索星核奧秘，擅長範圍傷害與控制。',req:'取得 4 份星塵',metric:'dust',need:4,bonus:'最大 MP +70、攻擊 +6'},ranger:{name:
~~~

### 6: offset 38,059
~~~javascript
ount:{slime:0,wolf:0,forest:0,cave:0,ruins:0,dust:0},side:{},bounties:[],bountyDone:0,playtime:0,events:[],oreDiscount:false,saveVersion:2});
let s=INIT(),hero={x:550,y:470,r:21,angle:Math.PI/2,facing:0,walk:0,slash:0,shield:0,invuln:0,moving:false,vx:0,vy:0},enemies=[],nodes=[],projs=[],parts=[],floating=[],decors=[],ambientNPCs=[],clock=0,mode='menu',currentTab='hero',keys=new Set(),pad=new Set(),attackReady=0,qReady=0,eReady=0,spawnTimer=0,lastFrame=0,saveTimer=0,uiTimer=0,worldTick=0,showingModal=false,notifyTimer=0,camera={x:0,y:0};
const ART_DATA={"urls":{"actors":"[embedded image omitted]
~~~

### 7: offset 5,613,187
~~~javascript
setHeroFacing(dir){hero.facing=dir;hero.angle=FACING_ANGLE[dir]}
function updateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,na
~~~

### 8: offset 5,613,205
~~~javascript
{hero.facing=dir;hero.angle=FACING_ANGLE[dir]}
function updateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i
~~~

### 9: offset 5,613,232
~~~javascript
=FACING_ANGLE[dir]}
function updateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],acto
~~~

### 10: offset 5,613,263
~~~javascript
dateHeroFacing(dx,dy){if(!dx&&!dy)return;let dir=hero.facing;
 if(Math.abs(dx)>Math.abs(dy))dir=dx<0?1:2;else if(Math.abs(dy)>Math.abs(dx))dir=dy<0?3:0;
 else if(dir===1||dir===2)dir=dx<0?1:2;else dir=dy<0?3:0;setHeroFacing(dir)}
function buildAmbientNPCs(area){ambientNPCs=[];const count=AMBIENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.index
~~~

### 11: offset 5,613,556
~~~javascript
ENT_COUNTS[area]||0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.m
~~~

### 12: offset 5,613,574
~~~javascript
0,routes=AMBIENT_ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.
~~~

### 13: offset 5,613,591
~~~javascript
ROUTES[area]||[];if(!count||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n
~~~

### 14: offset 5,613,617
~~~javascript
||!routes.length)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;contin
~~~

### 15: offset 5,613,633
~~~javascript
)return;
 const rng=seeded(78013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.rou
~~~

### 16: offset 5,613,661
~~~javascript
8013+ORDER.indexOf(area)*907);for(let i=0;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p
~~~

### 17: offset 5,613,702
~~~javascript
;i<count;i++){const base=routes[i%routes.length],route=base.map(([x,y],j)=>({x:x+(rng()-.5)*22,y:y+(rng()-.5)*18}));const start=Math.floor(rng()*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.
~~~

### 18: offset 5,613,845
~~~javascript
)*route.length),p=route[start];ambientNPCs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs
~~~

### 19: offset 5,613,885
~~~javascript
Cs.push({ambient:true,id:'ambient-'+area+'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs(vy))n.dir=vx<0?1:2;else n.dir=vy<0?3:0;
~~~

### 20: offset 5,613,926
~~~javascript
'-'+i,name:AMBIENT_NAMES[i%AMBIENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs(vy))n.dir=vx<0?1:2;else n.dir=vy<0?3:0;const nearHero=Math.hypot(n.x-hero.x,n.y-
~~~

### 21: offset 5,613,957
~~~javascript
ENT_NAMES.length],actor:AMBIENT_ACTORS[(i+ORDER.indexOf(area)*3)%AMBIENT_ACTORS.length],x:p.x,y:p.y,route,target:(start+1)%route.length,speed:38+rng()*28,wait:rng()*1.8,dir:0,frame:0,step:rng()*8,chat:0,line:AMBIENT_LINES[(i*3+ORDER.indexOf(area))%AMBIENT_LINES.length]})}}
function updateAmbientNPCs(dt){for(const n of ambientNPCs){n.chat=Math.max(0,n.chat-dt);n.step+=dt*5.5;if(n.wait>0){n.wait-=dt;continue}const p=n.route[n.target],dx=p.x-n.x,dy=p.y-n.y,d=Math.hypot(dx,dy);if(d<8){n.x=p.x;n.y=p.y;n.target=(n.target+1)%n.route.length;n.wait=.35+((n.target*37+n.x*.01)%1.7);continue}
 const vx=dx/d,vy=dy/d;if(Math.abs(vx)>Math.abs(vy))n.dir=vx<0?1:2;else n.dir=vy<0?3:0;const nearHero=Math.hypot(n.x-hero.x,n.y-hero.y)<42;if(nearHero){n.wait=
~~~

### 22: offset 5,617,434
~~~javascript
spawn){s.area=id;mode='play';const info=AREAS[id];hero.x=spawn?.x??(id==='town'?550:220);hero.y=spawn?.y??460;hero.vx=0;hero.vy=0;setHeroFacing(spawn?.facing??s.facing??0);camera.x=clamp(hero.x-VW/2,0,GW-VW);camera.y=clamp(hero.y-VH/2,0,GH-VH);hero.invuln=1.3;enemies=[];projs=[];parts=[];floating=[];nodes=[];decors=[];ambientNPCs=[];SW_SKILL_BURSTS.length=0;spawnTimer=0;
 const rnd=seeded(1832+ORDER.indexOf(id)*4124);for(let i=0;i<115;i++){let x=80+rnd()*(GW-160),y=80+rnd()*(GH-160);if(info.safe && Math.abs(y-450)<105)continue;decors.push({x,y,size:8+rnd()*22,kind:Math.floor(rnd()*4),s:rnd()*TWO})}
 if(NODE_SPECS[id]){let z=0;for(const [type,count,emoji,name] of NODE_SPECS[id])for(let j=0;j<count;j++){let p=NODE_POS[(z*5+ORDER.indexOf(id
~~~

### 23: offset 5,618,080
~~~javascript
ype,count,emoji,name] of NODE_SPECS[id])for(let j=0;j<count;j++){let p=NODE_POS[(z*5+ORDER.indexOf(id)*2)%NODE_POS.length];if(type==='altar')p=[[310,260],[810,680],[1320,230]][j];nodes.push({id:type+'-'+j,type,name,emoji,x:p[0],y:p[1],respawn:0,used:type==='altar'&&(s.altarNodes||[]).includes('altar-'+j)});z++}}
 buildAmbientNPCs(id);if(id==='ruins' && !s.bossDead && s.main>=4)spawnBoss();if(!info.safe)spawnWave();$('mapLabel').innerHTML=info.safe?'<b>🛡️ 安全區</b>　與 NPC 交談、購物、接任務':'<b style="color:#ffb9ac">⚔️ 野外戰鬥區</b>　怪物會主動追擊，注意血量';updateHud();renderSide();}
function changeArea(to){if(!canGo(to)){toast('🔒 尚未解鎖：繼續推進主線任務');return}const back=(GATES[to]||[]).find(g=>g.to===s.area);let spawn=null;if(back){let facing=0;if(back.x<250)facing=2;el
~~~

### 24: offset 5,620,187
~~~javascript
or(Math.random()*pool.length)],x,y))}}
function nearest(items,range=92){let closest=null,best=range;for(const x of items){const d=distance(hero,x);if(d<best){best=d;closest=x}}return closest}
function interaction(){if(mode!=='play')return;const n=nearest(NPCS[s.area]||[],108);if(n){talk(n);return}const citizen=nearest(ambientNPCs,82);if(citizen){citizen.chat=2.7;citizen.wait=Math.max(citizen.wait,2.2);toast('💬 '+citizen.name+'：'+citizen.line);return}const gte=nearest(GATES[s.area]||[],108);if(gte){changeArea(gte.to);return}const node=nearest(nodes.filter(x=>!x.used&&x.respawn<=0),86);if(node){gather(node);return}toast('附近沒有可互動的物件，請靠近 NPC、採集點或傳送門')}
function gather(n){if(n.type==='altar'){if(s.main<4){toast('石碑仍被神秘力量封鎖');return}if(s.altar
~~~

### 25: offset 7,159,160
~~~javascript
);hero.moving=motion>5;if(hero.moving)hero.walk+=dt*(7.8+3.2*Math.min(1,motion/speed));
 // 鏡頭使用幀率無關的柔和追蹤，降低手機上因幀時間波動造成的頓挫。
 const camX=clamp(hero.x-VW/2,0,GW-VW),camY=clamp(hero.y-VH/2,0,GH-VH),camBlend=1-Math.exp(-18*dt);camera.x+=(camX-camera.x)*camBlend;camera.y+=(camY-camera.y)*camBlend;
 if(areaInfo().safe)updateAmbientNPCs(dt);
 if(!areaInfo().safe){spawnTimer-=dt;if(spawnTimer<=0){spawnWave();spawnTimer=8.5}for(const e of enemies)monsterAI(e,dt)}
 for(let i=projs.length-1;i>=0;i--){let p=projs[i];p.x+=p.vx*dt;p.y+=p.vy*dt;p.life-=dt;if(p.friendly){for(const e of enemies){if(e.dead||p.hitIds.has(e))continue;if(Math.hypot(p.x-e.x,p.y-e.y)<p.r+e.r){p.hitIds.add(e);hurtEnemy(e,p.dmg,16);p.piercing--;if(p.piercing<=0){p.life=0;break}}
~~~

### 26: offset 7,171,608
~~~javascript
中混有右向影格；改以完整右向步行列水平鏡像，確保移動與停止都一致朝左。
 if(dir===1){if(!im?.complete||!im.naturalWidth)return false;g.save();g.translate(Math.round(x),0);g.scale(-1,1);g.drawImage(im,f*32,(i*4+2)*32,32,32,-w/2,Math.round(y-h*.69),w,h);g.restore();return true}
 return spriteDraw(im,f*32,(i*4+dir)*32,32,32,x-w/2,y-h*.69,w,h)}
function drawAmbientNPC(n){const near=distance(hero,n)<80;g.save();g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:Math.floor(n.step)%3;actorDraw(n.actor,n.x,n.y+18,n.dir,frame,58,58);if(near||n.chat>0){g.font='bold 12px "Noto Sans TC",system-ui';const label=n.chat>0?n.line:n.name;const tw=Math.min(230,Math.max(72,g.measureText(label).width+22));g.fillStyle=n.chat>0?'#173c34f2':'#
~~~

### 27: offset 7,176,675
~~~javascript
,frame,p.x-size/2,p.y-size/2,size,size)){
     g.fillStyle=p.color;g.beginPath();g.arc(p.x,p.y,p.r,0,TWO);g.fill();
   }
 }else{g.fillStyle=p.color;g.shadowColor=p.color;g.shadowBlur=22;g.beginPath();g.arc(p.x,p.y,p.r,0,TWO);g.fill()}
 g.restore()}}
function drawOverlay(){const target=nearest([...(NPCS[s.area]||[]),...ambientNPCs,...(GATES[s.area]||[]),...nodes.filter(n=>!n.used&&n.respawn<=0)],110);if(target){g.fillStyle='#092028db';rrect(VW/2-190,VH-68,380,36,10);g.fill();g.strokeStyle='#b0ebbf99';g.lineWidth=1;g.stroke();g.font='bold 15px system-ui';g.textAlign='center';g.fillStyle='#fff0b9';g.fillText('按 F　'+(target.to?target.name:target.type?'採集 '+target.name:target.ambient?'和 '+target.name+' 聊聊':'與 '+target.name+' 互動'),VW/2,VH-45)}
~~~

### 28: offset 7,177,035
~~~javascript
des.filter(n=>!n.used&&n.respawn<=0)],110);if(target){g.fillStyle='#092028db';rrect(VW/2-190,VH-68,380,36,10);g.fill();g.strokeStyle='#b0ebbf99';g.lineWidth=1;g.stroke();g.font='bold 15px system-ui';g.textAlign='center';g.fillStyle='#fff0b9';g.fillText('按 F　'+(target.to?target.name:target.type?'採集 '+target.name:target.ambient?'和 '+target.name+' 聊聊':'與 '+target.name+' 互動'),VW/2,VH-45)}
 const boss=enemies.find(e=>e.type==='boss'&&!e.dead);if(boss){g.fillStyle='#081720c9';rrect(VW/2-220,17,440,47,10);g.fill();g.fillStyle='#f2c4cf';g.font='bold 16px system-ui';g.textAlign='center';g.fillText('👑 墮星之王 · 諾克斯'+(s.altar<3?'　【封印未解除】':''),VW/2,35);g.fillStyle='#161b30';g.fillRect(VW/2-197,45,394,8);g.fillStyle='#f18bba';g.fillRect(VW/2-197,45,394*
~~~

... 255 more matches omitted.

## Pattern \`wander\` (occurrences: 0)

## Pattern \`WANDER\` (occurrences: 0)

## Pattern \`walkNPC\` (occurrences: 0)

## Pattern \`drawNpc\` (occurrences: 0)

## Pattern \`drawNPC\` (occurrences: 8)

### 1: offset 7,172,703
~~~javascript
ath.sin(clock*.8+i)*55+(i%3)*135;g.fillStyle=i%2?'#f7d889bb':'#fff1caaa';g.fillRect(bx,by,3,3);g.fillRect(bx+4,by-2,3,3)}g.globalAlpha=.24;g.fillStyle='#d6f3dc';for(let i=0;i<4;i++){const x=850+i*35+Math.sin(clock*1.4+i)*10,y=425-i*6;g.beginPath();g.arc(x,y,5+Math.sin(clock*2+i)*2,0,TWO);g.fill()}g.restore()}
function drawNPC(n){const near=distance(hero,n)<115;g.save();
 g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();
 if(n.id.includes('board')){objDraw('book',n.x,n.y+20,60,71)}
 else {actorDraw(n.id,n.x,n.y+20,0,Math.floor(clock*2+n.x)%3,68,68)}
 const text=n.name;g.font='bold 15px "Noto Sans TC",system-ui';
 const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));
 g.fillStyle=near?'#103b32ed
~~~

### 2: offset 7,177,948
~~~javascript
s();for(const n of nodes)drawNode(n);if(areaInfo().safe){const layers=[];for(const n of NPCS[s.area]||[])layers.push({y:n.y,type:'npc',o:n});for(const n of ambientNPCs)layers.push({y:n.y,type:'ambient',o:n});layers.push({y:hero.y,type:'hero',o:hero});layers.sort((a,b)=>a.y-b.y);for(const a of layers){if(a.type==='npc')drawNPC(a.o);else if(a.type==='ambient')drawAmbientNPC(a.o);else drawHero()}drawTownAtmosphere()}else{for(const n of NPCS[s.area]||[])drawNPC(n);drawEnemies();drawProjectiles();swDrawSkillBursts();drawHero()}drawParticles();g.restore();drawOverlay();}
function loop(time){let dt=lastFrame?Math.min(.04,(time-lastFrame)/1000):.016;lastFrame=time;if(mode==='play')update(dt);else clock+=dt*.3;draw();requestAnimationFrame(loop)}

~~~

### 3: offset 7,178,082
~~~javascript
,o:n});for(const n of ambientNPCs)layers.push({y:n.y,type:'ambient',o:n});layers.push({y:hero.y,type:'hero',o:hero});layers.sort((a,b)=>a.y-b.y);for(const a of layers){if(a.type==='npc')drawNPC(a.o);else if(a.type==='ambient')drawAmbientNPC(a.o);else drawHero()}drawTownAtmosphere()}else{for(const n of NPCS[s.area]||[])drawNPC(n);drawEnemies();drawProjectiles();swDrawSkillBursts();drawHero()}drawParticles();g.restore();drawOverlay();}
function loop(time){let dt=lastFrame?Math.min(.04,(time-lastFrame)/1000):.016;lastFrame=time;if(mode==='play')update(dt);else clock+=dt*.3;draw();requestAnimationFrame(loop)}
function perform(action){if(action==='attack')basicAttack();if(action==='q')skillQ();if(action==='e')skillE();if(action==='interact')i
~~~

### 4: offset 7,197,498
~~~javascript
s();for(const n of nodes)drawNode(n);if(areaInfo().safe){const layers=[];for(const n of NPCS[s.area]||[])layers.push({y:n.y,type:'npc',o:n});for(const n of ambientNPCs)layers.push({y:n.y,type:'ambient',o:n});layers.push({y:hero.y,type:'hero',o:hero});layers.sort((a,b)=>a.y-b.y);for(const a of layers){if(a.type==='npc')drawNPC(a.o);else if(a.type==='ambient')drawAmbientNPC(a.o);else drawHero()}drawTownAtmosphere()}else{for(const n of NPCS[s.area]||[])drawNPC(n);drawEnemies();drawProjectiles();swDrawSkillBursts();drawHero()}drawParticles();g.restore();drawOverlay()}
function update(dt){clock+=dt;worldTick+=dt;uiTimer+=dt;saveTimer+=dt;s.playtime+=dt;hero.slash=Math.max(0,hero.slash-dt);hero.invuln=Math.max(0,hero.invuln-dt);hero.shield=Mat
~~~

### 5: offset 7,197,632
~~~javascript
,o:n});for(const n of ambientNPCs)layers.push({y:n.y,type:'ambient',o:n});layers.push({y:hero.y,type:'hero',o:hero});layers.sort((a,b)=>a.y-b.y);for(const a of layers){if(a.type==='npc')drawNPC(a.o);else if(a.type==='ambient')drawAmbientNPC(a.o);else drawHero()}drawTownAtmosphere()}else{for(const n of NPCS[s.area]||[])drawNPC(n);drawEnemies();drawProjectiles();swDrawSkillBursts();drawHero()}drawParticles();g.restore();drawOverlay()}
function update(dt){clock+=dt;worldTick+=dt;uiTimer+=dt;saveTimer+=dt;s.playtime+=dt;hero.slash=Math.max(0,hero.slash-dt);hero.invuln=Math.max(0,hero.invuln-dt);hero.shield=Math.max(0,hero.shield-dt);s.mp=Math.min(s.maxMp,s.mp+dt*2.8);let dx=0,dy=0;if(keys.has('w')||keys.has('arrowup')||pad.has('up'))dy--;if(
~~~

### 6: offset 7,210,165
~~~javascript
,7,7)}for(const [x,y] of [[520,500],[575,505],[1245,520],[1300,535],[720,700],[755,705]]){c.fillStyle='#3d6a43';c.beginPath();c.arc(x,y,15,0,TWO);c.fill();c.fillStyle='#e6c477';c.fillRect(x-3,y-3,6,6)}c.restore()};

// Fixed NPCs stand still; moving NPCs only alternate left/right foot poses. No alpha/brightness flash.
drawNPC=function(n){const near=distance(hero,n)<115;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);else actorDraw(n.actor||n.id,n.x,n.y+20,n.dir??0,0,68,68);const text=n.name;g.font='bold 15px "Noto Sans TC",system-ui';const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));g.fillSty
~~~

### 7: offset 10,456,672
~~~javascript
efault();ev.stopImmediatePropagation();modalClose()}},true);
portraitMarkup=function(id,cls='portrait-box'){const src=id==='hero'?heroPortrait():npcPortrait(id);return `<div class="${cls}"><img data-portrait-id="${id}" alt="${id==='hero'?'冒險者':'NPC'} 肖像" width="256" height="256" decoding="async" src="${src}"></div>`};
drawNPC=function(n){const near=distance(hero,n)<115;g.save();g.globalAlpha=1;g.shadowBlur=0;g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);else actorDraw(n.actor||n.id,n.x,n.y+20,0,0,68,68);const text=n.name;g.font='bold 15px system-ui';const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));g.fillStyle=near?'#103b32ed':'#
~~~

### 8: offset 10,462,053
~~~javascript
torFocusV113(n){
  if(!swFocusedTargetV113 || swFocusedTargetV113.o!==n)return;
  g.save();
  g.strokeStyle='#e5c88be6';g.lineWidth=2;
  g.beginPath();g.ellipse(n.x,n.y+31,27,8,0,0,TWO);g.stroke();
  g.fillStyle='#f8e2a8';g.font='bold 14px system-ui';g.textAlign='center';
  g.fillText('✦',n.x,n.y-47);
  g.restore();
}
drawNPC=function(n){
  g.save();g.globalAlpha=1;g.shadowBlur=0;
  g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();
  if(n.id.includes('board'))objDraw('book',n.x,n.y+20,60,71);
  else actorDraw(n.actor||n.id,n.x,n.y+20,0,0,68,68);
  // No permanent NPC names or duplicate "F 交談" labels above or below sprites.
  swActorFocusV113(n);
  g.restore();
};
drawAmbientNPC=function(n){
  g.save();g.g
~~~

## Pattern \`npcDraw\` (occurrences: 0)

## Pattern \`drawActor\` (occurrences: 0)

## Pattern \`drawImage\s*\(\s*PIXEL_ART\` (occurrences: 0)

## Pattern \`actors\.webp\` (occurrences: 0)

## Pattern \`function draw\` (occurrences: 23)

### 1: offset 7,165,750
~~~javascript
eTable(c,520,650);cafeTable(c,1210,330);
 // 木箱、告示、花盆與小型街景
 for(const [x,y] of [[248,646],[300,650],[1335,645],[1410,650],[1000,300]]){c.fillStyle='#6f4a2c';c.fillRect(x-16,y-18,32,28);c.strokeStyle='#bb8750';c.strokeRect(x-16,y-18,32,28)}
 for(const [x,y] of [[556,360],[1160,720],[250,385]])pixelPlanter(c,x,y,62);
}

function drawCachedScenery(c){
 const a=s.area, dark=['cave','ruins'].includes(a);
 const houses={
 town:[[208,195,274,212,'長老之家','green'],[870,125,265,210,'旅行商店','green'],[1150,198,238,208,'轉職殿堂','blue'],[1035,692,243,178,'鍛造坊','amber'],[180,699,203,165,'星燈學院','blue'],[1300,685,205,170,'療癒所','green'],[28,122,190,162,'晨光麵包坊','amber'],[1378,116,190,164,'花香旅店','green'],[610,706,220,165,'冒險者公會','amber']],
 camp:[[235,102,220,169,'斥候
~~~

### 2: offset 7,169,635
~~~javascript
 }
   if(horizontal||vertical||plaza){tile=dark?(hash%3===0?22:7):safe?(hash%4===0?14:(hash%3===0?4:3)):(hash%3===0?13:3);
     if(a==='town'&&plaza&&decor===4)tile=47;
     if(a==='moon'&&decor===7)tile=48;
     if(a==='ruins'&&decor===6)tile=50;
   }
   tileAt(c,tile,x,y);
 }
 drawCachedScenery(c);worldCacheKey=a;
}
function drawGround(){if(worldCacheKey!==s.area||!worldCache)rebuildWorldCache();if(worldCache){g.drawImage(worldCache,camera.x,camera.y,VW,VH,camera.x,camera.y,VW,VH)}}
function drawGates(){for(const p of GATES[s.area]){let open=canGo(p.to),t=clock*2.3;
 g.save();g.translate(p.x,p.y);g.fillStyle='#0c2734';g.fillRect(-37,-44,74,89);g.strokeStyle=open?'#9ef0d7':'#b58b8b';g.lineWidth=6;g.strokeRect(-37,-44,74,89);
 for(let k=0;k<5;
~~~

### 3: offset 7,169,805
~~~javascript
    if(a==='moon'&&decor===7)tile=48;
     if(a==='ruins'&&decor===6)tile=50;
   }
   tileAt(c,tile,x,y);
 }
 drawCachedScenery(c);worldCacheKey=a;
}
function drawGround(){if(worldCacheKey!==s.area||!worldCache)rebuildWorldCache();if(worldCache){g.drawImage(worldCache,camera.x,camera.y,VW,VH,camera.x,camera.y,VW,VH)}}
function drawGates(){for(const p of GATES[s.area]){let open=canGo(p.to),t=clock*2.3;
 g.save();g.translate(p.x,p.y);g.fillStyle='#0c2734';g.fillRect(-37,-44,74,89);g.strokeStyle=open?'#9ef0d7':'#b58b8b';g.lineWidth=6;g.strokeRect(-37,-44,74,89);
 for(let k=0;k<5;k++){const yy=-32+k*17;g.fillStyle=open?`rgba(122,230,204,${.24+.18*(1+Math.sin(t+k))})`:'#82566b75';g.fillRect(-25,yy,50,10)}
 g.fillStyle='#ffeac0';g.font='bold 17px sy
~~~

### 4: offset 7,170,406
~~~javascript
k*17;g.fillStyle=open?`rgba(122,230,204,${.24+.18*(1+Math.sin(t+k))})`:'#82566b75';g.fillRect(-25,yy,50,10)}
 g.fillStyle='#ffeac0';g.font='bold 17px system-ui';g.textAlign='center';g.fillText(p.name,0,-72);
 g.font='12px system-ui';g.fillStyle=open?'#c2ead6':'#f5b9ba';g.fillText(open?'F 穿越':'尚未解鎖',0,68);g.restore()}}
function drawNode(n){if(n.used||n.respawn>0)return;const types={herb:'herb',charm:'star',leaf:'leaf',flower:'flower',crystal:'crystal',ore:'ore',page:'book',altar:'altar'};
 const t=types[n.type]||'flower';g.save();g.fillStyle='#081b2080';g.beginPath();g.ellipse(n.x,n.y+19,27,7,0,0,TWO);g.fill();
 if(!swDrawGatheredItem(n.type,n.x,n.y+23,n.type==='altar'?75:55,n.type==='altar'?90:66))objDraw(t,n.x,n.y+23,n.type==='altar'?75:55,n.
~~~

### 5: offset 7,171,595
~~~javascript
);
 // 左向原始圖集中混有右向影格；改以完整右向步行列水平鏡像，確保移動與停止都一致朝左。
 if(dir===1){if(!im?.complete||!im.naturalWidth)return false;g.save();g.translate(Math.round(x),0);g.scale(-1,1);g.drawImage(im,f*32,(i*4+2)*32,32,32,-w/2,Math.round(y-h*.69),w,h);g.restore();return true}
 return spriteDraw(im,f*32,(i*4+dir)*32,32,32,x-w/2,y-h*.69,w,h)}
function drawAmbientNPC(n){const near=distance(hero,n)<80;g.save();g.fillStyle='#09191573';g.beginPath();g.ellipse(n.x,n.y+25,19,6,0,0,TWO);g.fill();const frame=n.wait>0?0:Math.floor(n.step)%3;actorDraw(n.actor,n.x,n.y+18,n.dir,frame,58,58);if(near||n.chat>0){g.font='bold 12px "Noto Sans TC",system-ui';const label=n.chat>0?n.line:n.name;const tw=Math.min(230,Math.max(72,g.measureText(label).width+22));g.fillStyle=n.chat>0?'#173c3
~~~

### 6: offset 7,172,244
~~~javascript
ne:n.name;const tw=Math.min(230,Math.max(72,g.measureText(label).width+22));g.fillStyle=n.chat>0?'#173c34f2':'#0a302bcc';g.beginPath();g.roundRect(n.x-tw/2,n.y-69,tw,26,7);g.fill();g.strokeStyle=n.chat>0?'#f1d27f':'#86b89a';g.stroke();g.fillStyle='#fff0c2';g.textAlign='center';g.fillText(label,n.x,n.y-51)}g.restore()}
function drawTownAtmosphere(){if(s.area!=='town')return;g.save();for(let i=0;i<9;i++){const bx=180+((i*173+clock*(12+i*1.4))%1250),by=250+Math.sin(clock*.8+i)*55+(i%3)*135;g.fillStyle=i%2?'#f7d889bb':'#fff1caaa';g.fillRect(bx,by,3,3);g.fillRect(bx+4,by-2,3,3)}g.globalAlpha=.24;g.fillStyle='#d6f3dc';for(let i=0;i<4;i++){const x=850+i*35+Math.sin(clock*1.4+i)*10,y=425-i*6;g.beginPath();g.arc(x,y,5+Math.sin(clock*2+i)*2,0,TWO);g.fil
~~~

### 7: offset 7,172,694
~~~javascript
,by=250+Math.sin(clock*.8+i)*55+(i%3)*135;g.fillStyle=i%2?'#f7d889bb':'#fff1caaa';g.fillRect(bx,by,3,3);g.fillRect(bx+4,by-2,3,3)}g.globalAlpha=.24;g.fillStyle='#d6f3dc';for(let i=0;i<4;i++){const x=850+i*35+Math.sin(clock*1.4+i)*10,y=425-i*6;g.beginPath();g.arc(x,y,5+Math.sin(clock*2+i)*2,0,TWO);g.fill()}g.restore()}
function drawNPC(n){const near=distance(hero,n)<115;g.save();
 g.fillStyle='#0a1b1795';g.beginPath();g.ellipse(n.x,n.y+29,23,7,0,0,TWO);g.fill();
 if(n.id.includes('board')){objDraw('book',n.x,n.y+20,60,71)}
 else {actorDraw(n.id,n.x,n.y+20,0,Math.floor(clock*2+n.x)%3,68,68)}
 const text=n.name;g.font='bold 15px "Noto Sans TC",system-ui';
 const tw=Math.min(195,Math.max(80,g.measureText(text).width+26));
 g.fillStyle=near?'#103b3
~~~

### 8: offset 7,173,675
~~~javascript
f(['elder','guard','scout','seer'].includes(n.id)&&s.main!==6){
    g.fillStyle='#fff0b2';g.strokeStyle='#875726';g.lineWidth=2;g.font='bold 27px system-ui';g.strokeText('!',n.x,n.y-92);g.fillText('!',n.x,n.y-92)
 }
 if(near){g.fillStyle='#f8dca0';g.font='bold 13px system-ui';g.fillText('F 交談',n.x,n.y+50)}g.restore()}
function drawEnemies(){const im=PIXEL_ART.monsters;
 for(const e of enemies){if(e.dead)continue;const m=MONSTERS[e.type],boss=e.type==='boss';g.save();
 /* v1.1.5: 受擊時不再閃爍或使角色半透明；由血條與傷害數字提示。 */
 const width=boss?128:e.type==='golem'||e.type==='sentinel'?72:64;
 g.fillStyle='#0515188a';g.beginPath();g.ellipse(e.x,e.y+26,width*.34,9,0,0,TWO);g.fill();
 if(boss){if(!e.swCast||!swDrawMonsterCast(e,width)){if(!e.swMoving||!swDrawMovin
~~~

### 9: offset 7,174,783
~~~javascript
,e.y-width*.69,width,width)}}
 g.fillStyle='#0b1d24';g.fillRect(e.x-e.r-6,e.y-e.r-31,e.r*2+12,8);
 g.fillStyle=boss?'#ee89c4':'#f6b188';g.fillRect(e.x-e.r-6,e.y-e.r-31,(e.r*2+12)*clamp(e.hp/e.maxHp,0,1),8);
 if(e.slow>0){g.fillStyle='#b8eaf7';g.font='bold 17px sans-serif';g.fillText('*',e.x+e.r+7,e.y-20)}g.restore()}}
function drawHero(){g.save();if(hero.invuln>0&&Math.floor(clock*15)%2===0)g.globalAlpha=.52;
 g.fillStyle='#09191a9b';g.beginPath();g.ellipse(hero.x,hero.y+26,24,9,0,0,TWO);g.fill();
 const dir=hero.facing??0;
 const frame=hero.moving?Math.floor(hero.walk*1.25)%3:0;
 actorDraw(s.cls,hero.x,hero.y+20,dir,frame,66,66);
 if(hero.shield>0){g.strokeStyle='#a0eaffbb';g.lineWidth=3;g.beginPath();g.arc(hero.x,hero.y,42,0,TWO);g.stroke()}
~~~

### 10: offset 7,175,688
~~~javascript
(0,0,70,-1.05,1.05);g.stroke();g.restore()}
  // Player identity is shown in the HUD; keep the world view free of overlapping text.
 if(s.hp<s.maxHp){g.fillStyle='#081b20';g.fillRect(hero.x-29,hero.y-46,58,6);g.fillStyle=s.hp/s.maxHp<.3?'#f76d79':'#81e6ac';g.fillRect(hero.x-29,hero.y-46,58*s.hp/s.maxHp,6)}g.restore()}
function drawParticles(){for(const p of parts){g.save();g.globalAlpha=Math.min(1,p.life/p.max);g.fillStyle=p.color;g.shadowColor=p.color;g.shadowBlur=9;g.beginPath();g.arc(p.x,p.y,p.r,0,TWO);g.fill();g.restore()}for(const p of floating){g.save();g.globalAlpha=clamp(p.life,0,1);g.fillStyle=p.color;g.font='bold 19px system-ui';g.textAlign='center';g.strokeStyle='#0b222a';g.lineWidth=4;g.strokeText(String(p.text),p.x,p.y);g.fillText
~~~

... 13 more matches omitted.
