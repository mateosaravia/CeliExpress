from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.user_schema import UserSchema

async def valid_user_post(user_data: UserSchema) -> UserSchema:
    exists_user_with_same_email = await user_service.exists_user_by_field("email", user_data.email)
    if exists_user_with_same_email.value:
        raise UserException.UserAlreadyExists

    exists_user_with_same_username = await user_service.exists_user_by_field("username", user_data.username)
    if exists_user_with_same_username.value:
        raise UserException.UsernameAlreadyExists
    
    return user_data
