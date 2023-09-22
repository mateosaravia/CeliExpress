from ....services.users import user_service
from ....utils.exceptions.users.user_exceptions import UserException
from ....data_access.schemas.users.user_schema import UserSchema
from ....utils.results.result_handler import Result, handle_result

async def valid_user_post(user_data: UserSchema):
    user_with_same_email = await user_service.get_user_by_field("email", user_data.email)
    if user_with_same_email.value is not None:
        raise UserException.UserAlreadyExists

    user_with_same_username = await user_service.get_user_by_field("username", user_data.username)
    if user_with_same_username.value is not None:
        raise UserException.UsernameAlreadyExists

    return user_data