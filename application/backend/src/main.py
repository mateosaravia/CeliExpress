from fastapi import FastAPI
import uvicorn
import secrets

from .routers.users import user_router

app = FastAPI(root_path="/api")

app.include_router(user_router.router)