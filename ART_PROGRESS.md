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

## 2026-11-20 GitHub Actions 靜態檢查機制

- 已新增 `scripts/audit-game.mjs`（分支提交 `c5449bc`）：唯讀檢查 HTML 存在、必要美術檔、外部 WebP 檔頭並輸出 Actions summary。靜態檢查通過不代表視覺 QA 完成。
- 已在預設分支 `main` 新增 `.github/workflows/starwood-static-audit.yml`（提交 `46e6600`），每五分鐘排程（GitHub 可能延遲），檢出本開發分支執行檢查；權限 `contents: read`、不自動提交、不部署。
- 兩檔已重新讀取核對；GitHub workflow runs 端點在現有連接器不可讀，尚未取得首次執行成功紀錄。請至 Actions 頁確認；如有警告與錯誤依實際日誌排除。
- 這是 GitHub 靜態監測，**不是**每五分鐘運行 ChatGPT 自主開發；原 Chat 排程仍為每小時一次。A03 視覺與圖集檢驗仍未完成。

## 2026-11-20 實際美術資產查核與開發方向修正

- 依使用者要求，**停止每五分鐘的純靜態查核**：`main` 的 `.github/workflows/starwood-static-audit.yml` 已刪除（commit `a2d7aff`）。保留原本每小時 Chat 開發排程。
- GitHub 目錄清單核對：`assets/portraits/` 實際有 **78 張 WebP**，其中以五個告示牌檔名 `board/campboard/duskboard/moonboard/forgeboard` 排除後，**73 張 NPC 肖像**；`assets/common/` 14 個檔案。已建立附 Git blob SHA 與大小的逐檔 manifest：`art/asset-inventory.json`（commit `abf0acd`）。這完成**肖像外部檔案存在性與名稱清冊**，不等同已通過 A03/A04 的尺寸、透明邊界、動畫或畫面 QA。
- **具體待修問題**：`assets/common/avatar_knight.webp`、`avatar_novice.webp`、`avatar_ranger.webp` 三檔 Git SHA 完全相同（`be989b4e84dea69a5e46ed28af479091957b9b5f`），代表位元內容相同。若設計上應有不同職業外觀，必須補三者各自設計或明確指定共用圖，不能假定已完成獨立外觀。**未擅自覆蓋素材**。
- 建議修正優先序：(1) 檢驗職業初始頭像是否符合不同職業設定；(2) 由 GitHub 可讀的源碼或下載副本核對 `V6_ACTOR_MAP` 對應與方向、行走幀；(3) 確認肖像真實尺寸和 `object-fit:cover` 是否裁切，再作最小改動；(4) 補怪物幀數的實際圖集驗證。
- 由於本環境 GitHub `fetch_file` 對 2.31 MB `index.html` 回傳空字串、容器網路無法連線下載，尚無法安全修改遊戲主程式；請勿把 A03 或 A04 標為完成。

## 2026-11-20 可視化美術檢查頁

- 已建立 `art/review.html`（commit `8397a56`），直接從 GitHub 原始圖片來源顯示三個重複玩家頭像，以及 73 張 NPC 肖像與 5 張告示牌，提供分類和檔名搜尋。這是**可實際查看來源圖片**的頁面，不代表角色已改圖或正式遊戲已更新。
- 三個玩家頭像（knight、novice、ranger）同 SHA，頁面可直接作為重複素材的視覺覆核介面；不可擅自改成其他既有職業頭像。
- 已刪除開發分支不再需要的 `scripts/audit-game.mjs`（commit `752cfc8`）；每五分鐘 Actions workflow 先前已移除。只保留可供美術人工審查的清冊與頁面。
- 待辦：確認人物外觀設計是否需要區分三職業；取得 2.31MB 主程式可供局部安全修改的文字版本，逐一驗證角色對應與動畫；完成後才提供可遊玩的修正版。

## 2026-11-20 角色候選設計與實際對照頁

- 新增三個互不相同的 32×32 SVG 像素風格角色候選圖：`art/candidates/knight.svg`（銀甲）、`novice.svg`（學徒）、`ranger.svg`（森林弓手）。保留原本 `assets/common/avatar_*.webp` 完整不動；這是設計草稿，不是直接可用的遊戲 WebP 圖集。
- 新增 `art/class-comparison.html`（commit `fbb024b`），於同一畫面左右呈現 GitHub 原始職業頭像與候選新圖，並連至 NPC 美術檢視頁。
- 檔案可由 GitHub 再讀取；但原始 WebP 仍無法透過現有工具擷取像素內容，不宣稱完成實際遊戲內的替換或走路幀動畫。
- 後續優先：確認遊戲使用 `avatar_knight/novice/ranger.webp` 的位置、候選外觀接受程度；再製作相容的原圖尺寸／幀數版本、在開發版接入並 QA。勿直接覆蓋已有優秀美術。
