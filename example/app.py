import os
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Add backend directory to sys.path
backend_path = Path(__file__).parent.parent / "backend"
if str(backend_path) not in sys.path:
    sys.path.append(str(backend_path))

from auth_service.router import router as auth_router

def create_app():
    app = FastAPI(title="Example Integrated App")
    
    # Include the Auth Component
    app.include_router(auth_router)
    
    # Mount frontend files
    frontend_dir = Path(__file__).parent.parent / "frontend"
    if frontend_dir.exists():
        app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="static")

    @app.get("/api/hello")
    def hello():
        return {"message": "Hello from Integrated App!"}
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    from dotenv import load_dotenv
    
    load_dotenv()
    port = int(os.environ.get("APP_PORT", 8000))
    
    print("=" * 60)
    print(f"Example App started at http://localhost:{port}")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=port)
