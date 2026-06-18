---
name:          "CHANGELOG.md"
description:   "Project version history and release notes."
created_date:  "2026/04/21 00:00:00"
modified_date: "2026/06/18 10:00:00"
project_version: "1.0.0"
document_version: "1.0.0"
agent_sign: ['gemini cli/gemini-2.0-flash-exp']
---
# CHANGELOG

本專案版本遵循 `MAJOR.MINOR.PATCH` 規範。

## [1.0.0] - 2026-04-21

### 🚀 新增 (Added)
- **元件化重構**：從 `viewpoints` 專案中拆解並重新定義為獨立的認證服務元件。
- **後端封裝**：新增 `auth_service` Python 套件，包含 `core`, `models`, `router`, `storage`, `config` 模組。
- **動態配置系統**：實作 `authconfig.json` 設定機制，支援存儲類型與安全性參數的動態調整。
- **前端 SDK**：推出 `AuthClient` JS SDK 與 `auth-style.css` 元件樣式。
- **範例專案**：新增 `example/` 目錄，示範如何使用 `uv` 整合並運行認證元件。
- **測試體系**：建立基於 `pytest` 的單元測試環境，支援自動化隔離測試。
- **型別標註增強 (Type Safety)**：
  - 後端：為所有 Python 函式與路由導入完整的 **Type Hints**。
  - 前端：為 `AuthClient` SDK 導入完整的 **JSDoc** 註解與型別定義。

### 🔄 變更 (Changed)
- **全面命名重塑**：移除所有 `viewpoints` 硬編碼字眼，統一改為服務導向的通用命名。
- **架構解耦**：將存儲邏輯與認證路由分離，實作存儲層工廠模式。
- **設定隔離**：將 API 配置與執行環境變數分離，優化安全性。

### 🧹 移除 (Removed)
- 移除了所有與「監視器牆」相關的業務邏輯。
- 移為了舊版的 `start-server-fastapi.py` 單體程式碼。

---

> 最初版本 (拆解自 Viewpoints) 定義為 0.9.0。本次完整元件化重構標誌著正式版本 1.0.0 的誕生。
