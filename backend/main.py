import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from auth_service.router import router as auth_router

app = FastAPI(title="Auth Service API", version="1.0.0")

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Auth Router
app.include_router(auth_router)

# Serve Frontend Static Files
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.environ.get("AUTH_SERVICE_PORT", 8844))
    print(f"Auth Service started at http://localhost:{PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
