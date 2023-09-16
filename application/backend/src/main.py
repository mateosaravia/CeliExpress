from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import uvicorn
import secrets

from .routers.users import user_router
from .utils.exceptions.app_exceptions import AppExceptionCase, app_exception_handler


app = FastAPI(root_path="/api")

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)

app.include_router(user_router.router)