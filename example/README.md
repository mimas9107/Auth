# AuthService Example

這是一個整合 `AuthService` 元件的範例專案。

## 如何啟動

1. **確保已安裝 `uv`**：
   如果尚未安裝，請參考 [uv 官方文件](https://github.com/astral-sh/uv)。

2. **啟動應用程式**：
   在 `example/` 目錄下執行：
   ```bash
   uv run python app.py
   ```

3. **訪問頁面**：
   - 登入頁面：`http://localhost:8000/login.html`
   - API 測試：`http://localhost:8000/api/hello`

## 配置說明
- `authconfig.json`：控制認證元件的核心設定（存儲類型、密鑰等）。
- `.env`：控制應用程式執行環境（埠號、偵錯模式等）。
