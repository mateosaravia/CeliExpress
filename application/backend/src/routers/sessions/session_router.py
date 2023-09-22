from fastapi import APIRouter
from ...utils.results.result_handler import handle_result

from ...data_access.schemas.sessions.session_schema import SessionSchema
from ...services.sessions import session_service
from .session_dependencies import valid_user_login

router = APIRouter()

@router.post("/login")
async def login(credentials: SessionSchema):
    token = await session_service.login(credentials)
    return handle_result(token)

@router.post("/logout")
async def logout(token):
    result = await session_service.logout(token)
    return handle_result(result)