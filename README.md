# 娛樂城品牌頁面自動生成系統 (Elementor API)

這是一個全自動化的 WordPress 發布系統，能夠讀取預設的 Elementor 模板，將特定的品牌資料動態合成到 HTML 程式碼中，並且透過 WordPress REST API **直接發布成 Elementor 頁面**，完全不需要經過手動匯入 JSON 或 Elementor 編輯器。

## 📁 目錄結構

- `brands.json`：存放所有娛樂城品牌內容設定的資料庫，當您需要修改優缺點、新增品牌時，請編輯這個檔案。
- `template.json`：從 `kg娛樂城` 頁面匯出下來的原始 Elementor 模板檔案。系統會以此檔案作為框架。
- `src/html_templates.py`：存放兩個主要的 HTML 區塊（上方卡片與下方詳細評測）。
- `generate_brand_page.py`：主程式，負責將 `brands.json` 裡的資料結合 `html_templates.py`，覆寫進 `template.json` 中，並透過 API 直接發布至 WordPress。

## 🚀 如何使用

### 1. 🤖 讓 AI 幫您自動建立 / 修改品牌（推薦做法）
這是最快、最不會出錯的方式。您只需要直接對 AI（我）下達指令，剩下的 JSON 編輯、發布與更新，全部都會自動完成！

**💡 實用指令範本（您可以直接複製並修改）：**

- **新增一個全新品牌**：
  > 「請幫我在這套流程中新增一個品牌，名稱是『王者娛樂城』，網址是 `https://example.com`，Logo 圖片網址是 `https://example.com/logo.png`。這個娛樂城主打『首儲送2000』與『出金免手續費』。請幫我生成相關的優缺點、優惠內容，並直接發布。」

- **修改既有品牌的內容**：
  > 「請幫我修改『大將軍娛樂城』的內容。在『缺點』的地方幫我新增一條：『目前暫停支援信用卡儲值』。修改後請幫我重新發布。」

- **批量更新或重新發布**：
  > 「請幫我把所有品牌的發布作者，都改成只從『林思穎』或『張 Tung』隨機挑選，然後全部重新發布一次。」

當您說出這些指令時，AI 會自動幫您修改底層的 `brands.json`，並自動執行發布腳本。

### 2. 💻 手動修改品牌資料 (進階使用者)
如果您想自己動手改，請打開 `brands.json`，您可以：
- **修改既有內容**：直接修改裡面關於「優點(pros)」、「缺點(cons)」、「優惠(promo_details)」等陣列內容。
- **新增品牌**：依照格式複製一份現有的品牌區塊，並將最外層的 key（例如 `e88games`）改成新品牌的 Slug。

### 2. 執行發布
在終端機中，執行以下指令（請將 `[brand_slug]` 替換成在 `brands.json` 中定義的 key）：

```bash
python3 generate_brand_page.py [brand_slug]
```

**範例：更新/發布大將軍娛樂城**
```bash
python3 generate_brand_page.py grwin
```

如果頁面不存在，系統會自動建立新的頁面；如果頁面（根據 Slug）已經存在，系統會直接更新該頁面的內容。

## 🔑 環境變數設定
API 的認證金鑰目前寫死在 `generate_brand_page.py` 中。為了安全起見，您未來可以將其抽出為 `.env` 檔案。目前使用的是應用程式密碼 (Application Password) 進行驗證。
