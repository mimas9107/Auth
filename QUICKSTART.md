# 🚀 快速上手指導書 (新手友善版)

本指南專為**完全沒有環境開發經驗**的使用者設計。只需跟著步驟操作，就能將認證功能加入您的專案。

---

## 🛠️ 第一步：安裝必備工具

在開始之前，您需要先安裝一個名為 `uv` 的現代化工具，它會幫您處理所有複雜的 Python 環境問題。

1. **打開終端機 (Terminal / PowerShell)**。
2. **複製並執行以下指令**：
   - **macOS / Linux**:
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   - **Windows (PowerShell)**:
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```
3. **重新啟動您的終端機**，輸入 `uv --version` 看到版本號即表示成功！

---

## 📂 第二步：將認證元件放入您的專案

假設您的專案目錄叫作 `MyProject`。

1. **複製檔案**：
   將本專案的 `backend/auth_service` 資料夾，整層複製到您的專案中：
   ```text
   MyProject/
   └── auth_service/  <-- 放入這裡
   ```

2. **複製前端資源**：
   將 `frontend/` 下的檔案複製到您的前端目錄。

---

## ⚙️ 第三步：建立設定檔

在您的專案根目錄下，建立一個文字檔命名為 `authconfig.json`，內容直接貼上：

```json
{
    "STORAGE_TYPE": "localjson",
    "STORAGE_BASE_URL": ".data",
    "STORAGE_AUTH_SECRET": "請隨便輸入一段長字串作為密鑰"
}
```

---

## 🐍 第四步：在程式碼中啟用

在您的 FastAPI 主程式 (`main.py`) 中加入這兩行：

```python
from fastapi import FastAPI
from auth_service.router import router as auth_router # 1. 匯入

app = FastAPI()

app.include_router(auth_router) # 2. 啟用認證功能
```

---

## 🏃 第五步：啟動服務

不用擔心手動安裝套件，`uv` 會自動幫您搞定。在終端機輸入：

```bash
uv run python main.py
```

恭喜您！您的應用程式現在已經具備了專業級的**註冊、登入與認證 API**。

---

## 🛠️ 常見問題與故障排除 (Troubleshooting)

如果您在執行時遇到困難，別擔心，這是常見的狀況：

### 1. 為什麼註冊時一直顯示「註冊失敗」或錯誤？
*   **最可能原因**：您使用的「使用者名稱」已經被註冊過了。
*   **解決方法**：換一個名字試試看。如果您想「砍掉重練」，直接刪除專案資料夾下的 `.data` 資料夾，系統就會變回像新裝的一樣。

### 2. 出現 `ModuleNotFoundError: No module named '...'` 怎麼辦？
*   **最可能原因**：雖然 `uv` 會自動處理，但有時候某些套件沒被偵測到。
*   **解決方法**：手動叫 `uv` 幫您補裝。例如缺 `dotenv` 就執行：
    ```bash
    uv add python-dotenv
    ```

### 3. 我打開瀏覽器卻看到 `404 Not Found`？
*   **最可能原因**：網址輸入錯誤，或是您的檔案放錯位置。
*   **檢查清單**：
    - 預設登入網址應該是 `http://localhost:8000/login.html`（請根據您的 PORT 調整）。
    - 確保 `login.html` 放在您程式碼指定的靜態檔案目錄中。

### 4. 伺服器啟動了，但點擊登入後完全沒反應？
*   **最可能原因**：伺服器還在「熱機」中，或者您的電腦防火牆擋住了通訊。
*   **解決方法**：啟動後請稍等約 3-5 秒再操作。另外，檢查瀏覽器的「開發者工具 (F12)」的 Console 分頁，看看是否有紅字錯誤。

### 5. 出現一堆像 `DeprecationWarning` 的黃色警告，程式壞了嗎？
*   **最可能原因**：那是 Python 在提醒一些舊的套件未來會改版。
*   **解決方法**：完全可以忽略它！這不影響您的功能運作，程式是健康的。

---

祝您開發愉快！如果有任何進階問題，請查閱完整版 `README.md`。
