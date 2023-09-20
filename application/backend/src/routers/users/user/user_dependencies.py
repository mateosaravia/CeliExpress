from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.user_schema import UserSchema

async def valid_user_post(user_data: UserSchema):
    user = await user_service.get_user(user_data.email)
    if user:
        Result(UserException.UserAlreadyExists())
    return user_data