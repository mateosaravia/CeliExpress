from ...utils.exceptions.sessions.session_exceptions import SessionException
from ...utils.results.result_handler import Result
from ...utils import hasher

from ...data_access.schemas.sessions.session_schema import SessionSchema
from ..users import user_service
from ..tokens import token_service

async def login(login_credentials: SessionSchema):
    service_result = await user_service.get_user_by_field("email", login_credentials.email)
    user = service_result.value

    if user is None:
        return Result(SessionException.InvalidCredentials())

    valid_password = hasher.verify_password(login_credentials.password, user.password)
    if not valid_password:
        return Result(SessionException.InvalidCredentials())

    token = token_service.create_access_token(user.email, user.role)
    return Result(token)

async def logout():
    pass