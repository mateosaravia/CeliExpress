from ...data_access.schemas.users.user_schema import UserSchema
from ...data_access.repositories.users import user_repository
from ...utils.results.result_handler import Result
from ...utils.exceptions.users.user_exceptions import UserException

async def create_user(user_data):
    exists = await get_user(email)
    if exists:
        Result(UserException.UserAlreadyExists())

    added_user = await user_repository.add_user(user_data)
    return Result(added_user)

async def get_user_by_email(email):
    user = await user_repository.get_user_by_email(email)
    return Result(user)

async def get_user_by_username(username):
    user = await user_repository.get_user_by_username(email)
    return Result(user)