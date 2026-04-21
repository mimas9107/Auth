import os
import json
import pytest
import shutil
from pathlib import Path

@pytest.fixture(autouse=True)
def setup_test_env(tmp_path, monkeypatch):
    # 建立一個臨時的配置檔案
    config_file = tmp_path / "authconfig.json"
    data_dir = tmp_path / ".test_data"
    data_dir.mkdir()
    
    config_data = {
        "STORAGE_TYPE": "localjson",
        "STORAGE_BASE_URL": str(data_dir),
        "STORAGE_AUTH_SECRET": "test-secret-key"
    }
    
    with open(config_file, "w") as f:
        json.dump(config_data, f)
    
    # 強制 AuthConfig 讀取這個臨時檔案
    monkeypatch.chdir(tmp_path)
    
    # 讓 backend 模組可以被匯入
    backend_path = Path(__file__).parent.parent / "backend"
    monkeypatch.syspath_prepend(str(backend_path))
    
    yield tmp_path
    
    # 清理殘留資料 (pytest 會自動處理 tmp_path，這裡主要是心理安全)
