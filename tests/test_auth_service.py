import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI

def test_auth_flow():
    # 延遲匯入，確保 AuthConfig 已經讀取了 monkeypatch 後的環境
    from auth_service.router import router
    
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    # 1. 註冊 (應成功 200)
    resp = client.post("/api/auth/register", json={"username": "alice", "password": "password123"})
    assert resp.status_code == 200
    assert resp.json()["success"] is True

    # 2. 重複註冊 (應失敗 400)
    resp = client.post("/api/auth/register", json={"username": "alice", "password": "password123"})
    assert resp.status_code == 400

    # 3. 登入 (應成功)
    resp = client.post("/api/auth/login", data={"username": "alice", "password": "password123"})
    assert resp.status_code == 200
    token = resp.json()["access_token"]

    # 4. 驗證權杖 (應成功)
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/api/auth/me", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["username"] == "alice"

def test_invalid_login():
    from auth_service.router import router
    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    resp = client.post("/api/auth/login", data={"username": "bob", "password": "wrongpassword"})
    assert resp.status_code == 401
