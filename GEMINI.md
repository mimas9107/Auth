# Auth Service Component (認證服務元件)

這是一個解耦、可重複利用的前後端認證服務框架，支援多種存儲後端與集中化配置。

## 專案概述
- **核心目標**：提供一個獨立於業務邏輯的認證模組。
- **架構特點**：
  - **後端 (FastAPI)**：封裝為 `auth_service` Python 套件。
  - **配置系統**：使用 `authconfig.json` 管理存儲類型與安全性參數。
  - **存儲抽象化**：支援 `localjson`, `sqlite`, `redis` (後兩者為預留結構)。
  - **前端 (Vanilla JS)**：提供 `AuthClient` SDK。

## 目錄結構
- `backend/auth_service/`：**核心認證庫**
  - `config.py`：讀取 `authconfig.json`。
  - `storage.py`：動態切換存儲後端 (JSON, SQLite, Redis)。
- `example/`：**使用範例 (使用 uv 管理)**
  - `app.py`：範例應用程式。
  - `authconfig.json`：應用程式特定的認證配置。
  - `.env`：執行環境變數。

## 快速啟動範例

```bash
cd example
uv run python app.py
```

## 配置指南 (authconfig.json)
| 參數 | 說明 | 範例 |
| :--- | :--- | :--- |
| `STORAGE_TYPE` | 存儲後端類型 | `localjson`, `sqlite`, `redis` |
| `STORAGE_BASE_URL` | 資料夾路徑或連線字串 | `.data` |
| `STORAGE_AUTH_ADMIN` | 預設管理員名稱 | `admin` |
| `STORAGE_AUTH_SECRET` | JWT 加密密鑰 | `your-secret-key` |

## 元件化特色
1. **動態配置**：元件會自動尋找執行路徑下的 `authconfig.json`。
2. **存儲切換**：無需修改程式碼，僅需更改配置即可切換資料存儲後端。
3. **環境隔離**：認證配置 (`authconfig.json`) 與環境變數 (`.env`) 完全分離。
