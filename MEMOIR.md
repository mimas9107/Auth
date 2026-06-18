---
name:          "MEMOIR.md"
description:   "Project architectural decisions and historical context."
created_date:  "2026/06/18 10:00:00"
modified_date: "2026/06/18 10:00:00"
project_version: "1.0.0"
document_version: "1.0.0"
agent_sign: ['gemini cli/gemini-2.0-flash-exp']
---
# Project Memoir: Auth Service Component

## 核心設計哲學
本專案的初衷是將認證邏輯從複雜的業務系統 (Viewpoints) 中抽離，建立一個「隨插即用」的認證元件。我們優先考慮開發者的便利性與系統的可維護性。

## 關鍵架構決策 (ADR)

### 1. 使用 JSON 檔案作為預設存儲 (localjson)
- **決策內容**：在開發初期與小型應用中，預設不依賴資料庫服務。
- **動機**：降低初次使用的門檻，便於測試與展示。
- **影響**：在大規模併發場景下需切換至 `sqlite` 或 `redis`。

### 2. 強制性配置分離
- **決策內容**：將 `authconfig.json` 作為主要的配置媒介，而非僅依賴環境變數。
- **動機**：認證參數（如 Secret, Admin 名稱）通常是應用層級的，而非基礎設施層級的。
- **影響**：簡化了在不同環境 (Dev, Prod) 間遷移時的配置同步。

### 3. 前端 SDK 封裝
- **決策內容**：提供一個物件導向的 `AuthClient`。
- **動機**：避免前端工程師重複撰寫 Fetch API、Token 處理與頁面守衛邏輯。
- **影響**：大幅提升了前端整合速度。

## 歷史里程碑
- **2026/04/21**: 1.0.0 正式版發布。完成從 Viewpoints 的解耦，實作動態配置與存儲工廠模式。
- **2026/06/18**: 標準化專案文件標頭，導入 `version-sync-checker` 機制。
