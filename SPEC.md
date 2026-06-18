---
name:          "SPEC.md"
description:   "Technical specifications for the Auth Service Component."
created_date:  "2026/06/18 10:00:00"
modified_date: "2026/06/18 10:00:00"
project_version: "1.0.0"
document_version: "1.0.0"
agent_sign: ['gemini cli/gemini-2.0-flash-exp']
---
# Technical Specification: Auth Service Component

## 1. 系統架構
本元件採解耦設計，分為後端核心服務、前端 SDK 與配置系統三部分。

### 1.1 後端 (FastAPI)
- **auth_service/core.py**: 處理密碼雜湊 (Passlib) 與 JWT 簽發/驗證 (python-jose)。
- **auth_service/storage.py**: 存儲抽象層，支援多種後端。
- **auth_service/config.py**: 讀取 `authconfig.json` 並提供全域配置。
- **auth_service/router.py**: 提供標準的 RESTful 認證路由 (/login, /register, /verify)。

### 1.2 前端 SDK
- **auth-client.js**: 提供 `AuthClient` 類別，封裝 API 請求、Token 管理 (localStorage) 與頁面轉址。
- **auth-style.css**: 提供預設的登入介面樣式，支援 CSS 變數自定義。

## 2. 存儲抽象化 (Storage Abstraction)
支援以下存儲類型：
- `localjson` (預設): 使用單一 JSON 檔案存儲使用者資料。
- `sqlite`: (預留) 使用 SQLite 資料庫。
- `redis`: (預留) 使用 Redis 進行 Token 黑名單或 Session 管理。

## 3. 配置規範 (authconfig.json)
| 欄位 | 型別 | 說明 |
| :--- | :--- | :--- |
| `STORAGE_TYPE` | string | `localjson` \| `sqlite` \| `redis` |
| `STORAGE_BASE_URL` | string | 資料存放路徑或資料庫連線字串 |
| `STORAGE_AUTH_ADMIN` | string | 系統預設管理員帳號 |
| `STORAGE_AUTH_SECRET` | string | JWT 加密 Secret |

## 4. API 路由定義
- `POST /auth/login`: 使用者登入。
- `POST /auth/register`: 使用者註冊。
- `GET /auth/verify`: 驗證 Token 有效性。
