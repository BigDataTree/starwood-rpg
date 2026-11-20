# starwood-rpg

《星森傳說》GitHub Pages 遊戲專案。

## 手機更新方式：只上傳一個 ZIP

之後不需要再逐一上傳 `assets/` 裡的圖片。

1. 將最新版 GitHub Pages 壓縮包重新命名為 **`site.zip`**。
2. 到此 repository 的根目錄。
3. 使用 **Add file → Upload files** 上傳或覆蓋 `site.zip`。
4. Commit changes。
5. GitHub Actions 會自動：
   - 解壓 `site.zip`
   - 更新根目錄的 `index.html`
   - 更新整個 `assets/`
   - 自動 commit 並 push 回 `main`
6. 原有 GitHub Pages 會再依 `main` 自動發布新版。

ZIP 內應至少包含：

```text
index.html
assets/
  common/
  portraits/
  ui/
```

也支援 ZIP 外面多包一層資料夾，只要裡面能找到 `index.html`。

## 自動化工作流程

Workflow：`.github/workflows/deploy-site-zip.yml`

觸發條件：`main` 分支上的 `site.zip` 有更新，或手動執行 workflow。

> 注意：不要把 GitHub Actions workflow 一起放進 ZIP。Action 只會替換網站的 `index.html` 與 `assets/`，不會刪除 workflow 或 README。
