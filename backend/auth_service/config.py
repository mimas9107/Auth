import json
import os
from pathlib import Path
from typing import Any, Dict

class AuthConfig:
    def __init__(self, config_path: str = "authconfig.json"):
        self.config_path = Path(config_path)
        self.settings: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        # Default settings
        defaults = {
            "STORAGE_TYPE": "localjson",
            "STORAGE_BASE_URL": ".data",
            "STORAGE_AUTH_ADMIN": "admin",
            "STORAGE_AUTH_SECRET": "auth-service-default-secret-key",
            "ACCESS_TOKEN_EXPIRE_MINUTES": 10080  # 7 days
        }
        
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_settings = json.load(f)
                    defaults.update(file_settings)
            except Exception as e:
                print(f"Warning: Failed to load {self.config_path}: {e}")
        
        return defaults

    @property
    def storage_type(self) -> str:
        return self.settings.get("STORAGE_TYPE", "localjson")

    @property
    def storage_url(self) -> str:
        return self.settings.get("STORAGE_BASE_URL", ".data")

    @property
    def admin_user(self) -> str:
        return self.settings.get("STORAGE_AUTH_ADMIN", "admin")

    @property
    def secret_key(self) -> str:
        return self.settings.get("STORAGE_AUTH_SECRET", "auth-service-default-secret-key")

    @property
    def expire_minutes(self) -> int:
        return int(self.settings.get("ACCESS_TOKEN_EXPIRE_MINUTES", 10080))

# Global configuration instance
config = AuthConfig()
