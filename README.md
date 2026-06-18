---
name:          "README.md"
description:   "Main project documentation and overview."
created_date:  "2026/04/21 00:00:00"
modified_date: "2026/06/18 10:00:00"
project_version: "1.0.0"
document_version: "1.0.0"
agent_sign: ['gemini cli/gemini-2.0-flash-exp']
---
# Auth Service Component

這是一個解耦、可重複利用的前後端認證服務框架，專為快速整合使用者管理與 JWT 認證功能而設計。

## 🌟 核心特色

- **完全封裝**：認證邏輯獨立於業務代碼，支援 `FastAPI` 路由直接掛載。
- **動態配置**：透過 `authconfig.json` 集中管理存儲類型、安全密鑰與環境參數。
- **多後端支援**：抽象化存儲層，預留 `SQLite` 與 `Redis` 擴充介面（預設使用 `JSON` 檔案）。
- **前端元件化**：提供 `AuthClient` JS SDK 與具備 CSS 變數的樣式表，支援輕鬆換膚與整合。
- **環境友善**：支援 `uv` 套件管理，並將環境變數 (`.env`) 與應用配置 (`authconfig.json`) 完全隔離。

## 📁 目錄結構

```text
.
├── backend/
│   ├── auth_service/      # 核心認證封裝庫 (Reusable Package)
│   │   ├── config.py      # 配置讀取邏輯
│   │   ├── core.py        # 安全性工具 (JWT, Hashing)
│   │   ├── storage.py     # 存儲後端工廠
│   │   └── router.py      # FastAPI 認證路由
│   └── main.py            # 服務入口點範本
├── frontend/
│   ├── js/auth-client.js  # Frontend Client SDK
│   ├── css/auth-style.css # 元件化樣式表
│   └── login.html         # 通用登入頁面範本
├── example/               # 整合範例專案 (使用 uv 管理)
│   ├── app.py             # 範例整合應用
│   └── authconfig.json    # 範例配置文件
└── tests/                 # 單元測試與整合測試
```

## 🚀 快速開始

### 使用範例專案
確保您已安裝 [uv](https://github.com/astral-sh/uv)。

```bash
cd example
uv run python app.py
```

### 整合至現有後端
1. 將 `backend/auth_service` 拷貝至您的專案目錄。
2. 在 FastAPI 應用中掛載：
```python
from auth_service.router import router as auth_router
app.include_router(auth_router)
```

## ⚙️ 配置說明 (authconfig.json)

在執行目錄下建立 `authconfig.json`：
```json
{
    "STORAGE_TYPE": "localjson",
    "STORAGE_BASE_URL": ".data",
    "STORAGE_AUTH_ADMIN": "admin",
    "STORAGE_AUTH_SECRET": "your-secret-key"
}
```

## 🧪 測試

執行全域單元測試：
```bash
uv run pytest tests/
```

## 📄 授權
本專案採用 MIT 授權。
