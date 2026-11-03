# PriceHunter 商品比價 Web App

這是一個以 Python Flask 製作的商品比價網站原型（MVP）。

## 功能
- 輸入商品關鍵字或商品網址
- 上傳 JPG / PNG / WEBP 商品圖片並在結果頁預覽
- 產生 Shopee、Taobao、momo、Tmall、Pinduoduo 五個平台的搜尋連結
- SQLite 儲存最近搜尋紀錄
- 響應式網頁介面

## 重要限制
目前版本**不會自動擷取各平台即時價格、庫存或商品圖片**，而是產生各平台搜尋連結，讓使用者在平台查看即時結果。圖片功能目前是上傳與預覽，尚未串接以圖搜圖服務。這是可展示、可操作的 MVP，不應將示範功能描述成已完成的自動爬蟲或 AI 圖片辨識。

## Windows 安裝與啟動
1. 安裝 Python 3.10 或更新版本。
2. 解壓縮專案，進入 `PriceHunter` 資料夾。
3. 在資料夾空白處開啟終端機（CMD / PowerShell）。
4. 執行：

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

5. 在瀏覽器開啟： http://127.0.0.1:5000

## 專案結構
```text
PriceHunter/
├── app.py
├── requirements.txt
├── README.md
├── modules/
│   ├── __init__.py
│   ├── url_generator.py
│   └── data_processor.py
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── css/style.css
│   ├── js/app.js
│   └── uploads/
└── database/
```

## 後續可擴充
- 串接官方商品 API 或授權資料來源
- 接入以圖搜圖服務
- 商品名稱、價格、運費與賣家資料正規化
- 匯率換算與跨平台價格比較
- 使用者帳號、收藏與價格追蹤
