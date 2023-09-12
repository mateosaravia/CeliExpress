from fastapi import FastAPI

import .user_dependencies
from ..data_access.models.users.user_model import UserModel
from ..data_access.schemas.users.user_schema import UserSchema

router = FastAPI()

@router.post("/signup", response_model=UserResponse)
async def signup(user_data: UserSchema = Depends(user_dependencies.valid_user_request)):
    posted_user = await user_service.create_user(user_data)
    return posted_user