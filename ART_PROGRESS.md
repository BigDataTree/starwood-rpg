# 《星森傳說》NPC／怪物美術整合進度

> 自動接續工作紀錄；以 GitHub 實際檔案為唯一真實來源，未驗證事項不得宣稱完成。
> 本次開始：2026-11-20。來源：`main/index.html`，Git blob `daa21a4666b369ff8f07fb3e5fedde550aa057e4`。
> 開發分支：`automation/npc-sprite-audit-20261120`。未經 QA 不合併至 main。

## 計數與定義（已完成靜態盤點）

- **73 個有專屬 V6 美術對應的 NPC 身分**（`V6_ACTOR_MAP` 有 73 筆，`V6_PORTRAITS` 對應 73 筆，靜態鍵名一一對應）。其中 **42 位具名角色**（包含長老之家 9 位、各區新增 7 位等），**31 位動態居民**（星燈鎮 14、綠葉營地 4、暮枝 5、月泉 4、星鑄前哨 4）。
- 另有 **5 個告示牌**（board、campboard、duskboard、moonboard、forgeboard），屬地圖互動物件，不應當作必須會走動的 NPC。
- **9 種怪物/BOSS**（slime、wolf、spider、treant、bat、golem、wraith、sentinel、boss），其中 8 種一般怪物、1 位 BOSS。
- 各區的 V6 人物對應數（不含告示牌）：town 26、camp 9、dusk 10、moon 10、forgecamp 9、elderhouse1 5、elderhouse2 4，共 73。
- **注意**：「存在對應鍵」不表示圖片辨識度、尺寸、走路幀數、相容性、可見結果已通過驗證；目前尚未執行完整視覺 QA。

## 初步程式風險（待重現／修復）

1. 對話肖像 CSS：`.portrait-box img` 使用 `object-fit:cover`；`.portrait-box` 自身有 `border:2px` 與 `overflow:hidden`；`.portrait-box:after` 疊了 256×256 文字欄。可能造成角色肖像邊緣被裁切、附加邊框、比例不當。需確認實際圖片像素尺寸、框架尺寸與行動裝置顯示後再改。
2. 一般怪物繪製片段使用 `(Math.floor(clock*4+e.phase)%2)*32`，看起來只輪播**兩幀**；需確認怪物 atlas 幀數、方向、現有素材是否包含可用多幀，不可只改動畫索引而越界。
3. 移動 NPC 的 V6 身分與 `V6_ACTOR_MAP` 對應存在，但仍需逐地圖驗證 `buildAmbientNPCs`、`actorDraw`、方向與幀索引是否真正使用其專屬行走圖。
4. `index.html` 內嵌大量 WebP／base64 美術資源（約 2.29M 字元）；未必適合直接整份複寫，修改時須保持原有資料完整並避免體積失控。

## 接續任務（依順序，每次取低風險可完成項目）

- [x] A01：讀取 GitHub 與 `main/index.html`。
- [x] A02：建立 73 人物、5 告示牌、9 怪物的靜態分類基線。
- [ ] A03：逐一確認全部 73 人物 atlas 的對應關係、方向/行走幀與實際 sprite 尺寸，生成可機械驗證的 manifest。
- [ ] A04：檢查全部 73 張 256×256 肖像的實際尺寸、透明邊界、臉部安全區；列出問題清單。
- [ ] A05：為真正缺漏或不符合設計的角色訂出 256×256／32×32 一致的美術規格，避免重製已合格者。
- [ ] A06：分批製作或修正 NPC 的四方向移動精靈圖與怪物動畫圖集。
- [ ] A07：修正對話肖像顯示與各地圖 NPC 動畫索引，留存測試證據。
- [ ] A08：進行桌機／手機 QA、格式與效能測試，保護現有遊戲機制。
- [ ] A09：通過 QA 後才準備合併／發布手機網址、ZIP、真正離線的 HTML 單檔。

## 自動工作原則

- **只使用一般 Chat 可用工具**，不主動呼叫 Work、Codex、雲端電腦或瀏覽器操作，避免 Work／Codex 額度；無法從工具直接證明實際扣點狀態。
- 每次先讀此文件與 GitHub 的新提交，核對進度；只做 1 個小型、可驗證工作單元；必要時使用獨立分支提交，保留原功能。
- 執行工具不支援或 GitHub 無寫入權限時，只回報事實與可用的下一步，不要宣稱已修改或重複建立排程。
- 只有可驗證時才將項目勾選；避免重新產圖或覆寫已經完成的素材。
- 所有工作完成且確認 QA 後，停止後續自動排程並回報。

## 2026-11-20 本輪 A03 預備查核（未完成 A03）

- 透過 GitHub compare API 比對 `main...automation/npc-sprite-audit-20261120`：狀態 `ahead`、ahead 1／behind 0，差異僅新增 `ART_PROGRESS.md`（40 行），未發現分支覆寫 `index.html` 或既有美術資產。
- 主線 `index.html` Git blob SHA 仍為 `daa21a4666b369ff8f07fb3e5fedde550aa057e4`，與原盤點所記錄者相同。
- 嘗試以 GitHub fetch_file 讀取完整 `index.html` 與 1–100 行，均回傳空字串；GitHub 程式碼搜尋 `V6_ACTOR_MAP` 亦無結果。因此本輪**無法可靠擷取 atlas 定義或逐角色檢查**，不得推定方向、幀數或尺寸正確，A03 保持未完成。
- 下一輪：取得支援大型單檔的原始碼存取方式（例如分塊 Git blob、可讀的原始碼副本或 checkout），先抽取 `V6_ACTOR_MAP`、方向與 sprite 尺寸規則，再建立逐角色 manifest。不得在無法驗證時更改素材。
