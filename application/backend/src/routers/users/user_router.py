from fastapi import APIRouter, Depends

from . import user_dependencies
from ...data_access.models.users.user_model import UserModel
from ...data_access.schemas.users.user_schema import UserSchema

router = APIRouter()

@router.post("/signup", response_model=UserSchema)
async def signup(user_data: UserSchema): #
    posted_user = await user_service.create_user(user_data)
    return posted_user