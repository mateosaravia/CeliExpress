from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import uvicorn
import secrets

from .routers.users import user_router
from .routers.users import supplier_router
from .routers.users import driver_router
from .routers.users import restaurant_router
from .utils.exceptions.app_exceptions import AppExceptionCase, app_exception_handler
from .utils.exceptions.request_exceptions import request_validation_exception_handler
from .config.database import create_tables

create_tables()

app = FastAPI(root_path="/api")

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)

@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)

app.include_router(user_router.router)
app.include_router(supplier_router.router)
app.include_router(driver_router.router)
app.include_router(restaurant_router.router)