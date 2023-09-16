from fastapi import APIRouter, Depends
from ...utils.results.results_handler import handle_result

from .user_dependencies import valid_user_post
from ...data_access.models.users.user_model import UserModel
from ...data_access.schemas.users.user_schema import UserSchema
from ...services.users import user_service
from ...utils.exceptions.users.user_exceptions import AppException

router = APIRouter()

@router.post("/signup", response_model=UserSchema)
async def signup(user_data: UserSchema = Depends(valid_user_post)):
    result = await user_service.create_user(user_data)
    return handle_result(result)