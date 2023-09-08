from fastapi import FastAPI
import ...dependencies.users.user_dependencies as user_dependencies
import ...services.users.user_service as user_service
from ...schemas.users.user_schema import UserSchema

router = FastAPI()

@router.post("/signup", response_model=UserResponse)
async def signup(user_data: UserSchema = Depends(user_dependencies.valid_user_request)):
    posted_user = await user_service.create_user(user_data)
    return posted_user