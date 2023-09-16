from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

async def http_exception_handler(
    request: Request, exc: HTTPException
) -> JSONResponse:
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)