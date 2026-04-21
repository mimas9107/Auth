import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod
from .config import config

class BaseStorage(ABC):
    @abstractmethod
    def load_users(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def save_users(self, users: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_user_data_file(self, username: str) -> Path:
        pass

class JSONStorage(BaseStorage):
    def __init__(self, storage_dir: str):
        self.base_dir = Path(storage_dir).resolve()
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.users_file = self.base_dir / "auth_users.json"

    def load_users(self) -> Dict[str, Any]:
        if not self.users_file.exists():
            return {}
        try:
            with open(self.users_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save_users(self, users: Dict[str, Any]) -> None:
        with open(self.users_file, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def get_user_data_file(self, username: str) -> Path:
        user_dir = self.base_dir / "user_configs"
        user_dir.mkdir(parents=True, exist_ok=True)
        return user_dir / f"config_{username}.json"

class SQLiteStorage(BaseStorage):
    def __init__(self, db_url: str):
        self.db_url = db_url
        # Placeholder for SQLite implementation
        print(f"SQLite Storage initialized with {db_url} (Stub)")

    def load_users(self) -> Dict[str, Any]: return {}
    def save_users(self, users: Dict[str, Any]) -> None: pass
    def get_user_data_file(self, username: str) -> Path: return Path("/tmp")

class RedisStorage(BaseStorage):
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        # Placeholder for Redis implementation
        print(f"Redis Storage initialized with {redis_url} (Stub)")

    def load_users(self) -> Dict[str, Any]: return {}
    def save_users(self, users: Dict[str, Any]) -> None: pass
    def get_user_data_file(self, username: str) -> Path: return Path("/tmp")

def get_storage() -> BaseStorage:
    s_type: str = config.storage_type.lower()
    s_url: str = config.storage_url
    
    if s_type == "sqlite":
        return SQLiteStorage(s_url)
    elif s_type == "redis":
        return RedisStorage(s_url)
    else:
        return JSONStorage(s_url)
