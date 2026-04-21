from datetime import datetime
from typing import Optional, Any, Dict
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .models import UserAuth, Token, UserResponse
from .core import (
    get_password_hash, 
    verify_password, 
    create_access_token, 
    decode_access_token
)
from .storage import get_storage

router = APIRouter(prefix="/api/auth", tags=["auth"])
storage = get_storage()  # Use the factory
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    username = decode_access_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username

@router.post("/register")
def register(user: UserAuth) -> Dict[str, Any]:
    users = storage.load_users()
    if user.username in users:
        raise HTTPException(status_code=400, detail="使用者名稱已存在")

    users[user.username] = {
        "password": get_password_hash(user.password),
        "created_at": datetime.now().isoformat(),
    }
    storage.save_users(users)
    return {"success": True, "message": "註冊成功"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Dict[str, Any]:
    users = storage.load_users()
    user = users.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="帳號或密碼錯誤",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": form_data.username,
    }

@router.get("/me", response_model=UserResponse)
def get_me(username: str = Depends(get_current_user)) -> UserResponse:
    return UserResponse(username=username)
