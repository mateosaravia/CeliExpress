from fastapi import Request
from starlette.responses import JSONResponse

class AppExceptionCase(Exception):
    def __init__(self, status_code: int, exception_case: str):
        self.exception_case = exception_case
        self.status_code = status_code

async def app_exception_handler(request: Request, exc: AppExceptionCase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "Exception": exc.exception_case,
        },
    )